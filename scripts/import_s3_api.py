#!/usr/bin/env python3
"""Build offline Markdown articles for the indexed Amazon S3 operations."""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from html import escape, unescape
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from tempfile import NamedTemporaryFile
from time import sleep
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit
from urllib.request import urlopen

if __package__:
    from .s3_markdown import has_title, html_to_markdown, validate_markdown
else:
    from s3_markdown import has_title, html_to_markdown, validate_markdown


AWS_API = "https://docs.aws.amazon.com/AmazonS3/latest/API/"
ROOT = Path(__file__).resolve().parents[1]
OPERATION_LINK = re.compile(r"Docs/API/([A-Za-z][A-Za-z0-9]*)/README\.md")
HREF = re.compile(r"""(<a\b[^<>]*?)\s+href\s*=\s*(["'])(.*?)\2""", re.I | re.S)
AWS_OPERATION_PATH = re.compile(r"/AmazonS3/latest/API/API_([A-Za-z][A-Za-z0-9]*)\.html")
LOCAL_OPERATION_PATH = re.compile(r"\.\./([A-Za-z][A-Za-z0-9]*)/\1\.md")


class ArticleParser(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=False)
        self.container = None
        self.depth = 0
        self.parts = []
        self.complete = False
        self.feed(source)
        self.close()

    def handle_starttag(self, tag, attrs):
        if self.complete:
            return
        if self.container is None:
            attributes = dict(attrs)
            if attributes.get("id") == "main-col-body":
                self.container = tag
                self.depth = 1
            return
        if tag == self.container:
            self.depth += 1
        self.handle_startendtag(tag, attrs)

    def handle_startendtag(self, tag, attrs):
        if self.depth:
            self.parts.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        if not self.depth:
            return
        if tag == self.container:
            self.depth -= 1
            if not self.depth:
                self.complete = True
                return
        self.parts.append(f"</{tag}>")

    def handle_data(self, data):
        if self.depth:
            self.parts.append(data)

    def handle_entityref(self, name):
        self.handle_data(f"&{name};")

    def handle_charref(self, name):
        self.handle_data(f"&#{name};")


def localize_links(html, operation, indexed):
    def local_href(match):
        tag_start, quote, value = match.groups()
        if value.startswith("#"):
            return match.group()

        value = unescape(value)
        url = urlsplit(urljoin(AWS_API, value))
        target = AWS_OPERATION_PATH.fullmatch(url.path) if url.netloc == "docs.aws.amazon.com" else None
        relative = urlsplit(value)
        if not relative.scheme and not relative.netloc:
            target = target or LOCAL_OPERATION_PATH.fullmatch(relative.path)
        if not target or target[1] not in indexed:
            return tag_start

        name = target[1]
        path = f"../{name}/{name}.md"
        if url.fragment:
            path = f"#{url.fragment}" if name == operation else f"{path}#{url.fragment}"
        return f"{tag_start} href={quote}{escape(path, quote=True)}{quote}"

    return HREF.sub(local_href, html)


def format_snapshot(operation, article):
    return (
        f"> Источник и автор — Amazon Web Services, Amazon S3 API Reference, статья `API_{operation}.html`. "
        "Текст документации — CC BY-SA 4.0. Примеры кода — MIT-0. "
        "Статья преобразована в Markdown. Ссылки на операции ведут к локальным копиям, "
        "ссылки на материалы вне справочника оставлены обычным текстом.\n\n"
        f"{article}\n"
    )


def fetch(operation, indexed):
    url = f"{AWS_API}API_{operation}.html"
    for attempt in range(3):
        try:
            with urlopen(url, timeout=20) as response:
                source = response.read().decode(response.headers.get_content_charset() or "utf-8")
            break
        except HTTPError as error:
            if error.code not in (429, 500, 502, 503, 504) or attempt == 2:
                raise
        except (URLError, TimeoutError):
            if attempt == 2:
                raise
        sleep(2 ** attempt)

    article = ArticleParser(source)
    body = "".join(article.parts).strip()
    title = rf"<h1\b[^>]*>\s*{re.escape(operation)}\s*</h1>"
    if not article.complete or not body or not re.search(title, source):
        raise ValueError(f"Не найден полный HTML статьи {operation}")
    if not re.search(title, body):
        body = f"<h1>{operation}</h1>\n{body}"

    return markdown_snapshot(operation, body, indexed)


def markdown_snapshot(operation, html, indexed):
    article = html_to_markdown(localize_links(html, operation, indexed))
    validate_markdown(article, operation)
    return format_snapshot(operation, article)


def snapshot_path(operation):
    return ROOT / "Docs" / "API" / operation / f"{operation}.md"


def read_local_article(operation):
    article = snapshot_path(operation).read_text(encoding="utf-8-sig").lstrip()
    if article.startswith("> Источник и автор —"):
        article = article.partition("\n\n")[2]
    return article.lstrip()


def check_local(operation, _indexed):
    validate_markdown(read_local_article(operation), operation)


def convert_local(operation, indexed):
    article = read_local_article(operation)
    if has_title(article, operation):
        validate_markdown(article, operation)
        return None
    if not article.startswith("<div>"):
        raise ValueError("Ожидалась статья в Markdown или прежний HTML-снимок")
    return markdown_snapshot(operation, article, indexed)


def write_snapshot(operation, content):
    target = snapshot_path(operation)
    with NamedTemporaryFile(mode="w", encoding="utf-8", dir=target.parent, delete=False) as output:
        staging = Path(output.name)
        try:
            output.write(content)
            output.close()
            staging.replace(target)
        finally:
            staging.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--check", action="store_true", help="Проверить Markdown-статьи без сети и записи файлов.")
    modes.add_argument("--convert-local", action="store_true", help="Преобразовать скачанные статьи без сети.")
    parser.add_argument("operation", nargs="*", help="Операции для обновления. Без аргументов импортируются все.")
    args = parser.parse_args()
    indexed = OPERATION_LINK.findall((ROOT / "README.md").read_text(encoding="utf-8"))
    if not indexed or len(indexed) != len(set(indexed)):
        parser.error("Оглавление README.md пустое или содержит дубликаты операций")
    operations = list(dict.fromkeys(args.operation)) or indexed
    indexed_names = set(indexed)
    unknown = sorted(set(operations) - indexed_names)
    if unknown:
        parser.error(f"Неизвестные операции: {', '.join(unknown)}")

    failed = set()
    saved = 0
    if args.check:
        build, mode = check_local, "--check "
    elif args.convert_local:
        build, mode = convert_local, "--convert-local "
    else:
        build, mode = fetch, ""
    with ThreadPoolExecutor(max_workers=6) as executor:
        pending = {executor.submit(build, operation, indexed_names): operation for operation in operations}
        for future in as_completed(pending):
            operation = pending[future]
            try:
                content = future.result()
                if content is not None:
                    write_snapshot(operation, content)
                    saved += 1
            except (OSError, ValueError) as error:
                print(f"{operation}: {error}", file=sys.stderr)
                failed.add(operation)

    if args.check:
        print(f"Проверено статей: {len(operations) - len(failed)} из {len(operations)}", flush=True)
    elif args.convert_local:
        print(f"Преобразовано: {saved}. Уже в Markdown: {len(operations) - saved - len(failed)}", flush=True)
    else:
        print(f"Сохранено страниц: {saved} из {len(operations)}", flush=True)
    if failed:
        retry = " ".join(operation for operation in operations if operation in failed)
        parser.exit(1, f"Повторный запуск — python3 scripts/import_s3_api.py {mode}{retry}\n")


if __name__ == "__main__":
    main()
