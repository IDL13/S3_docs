"""Render the markup used by Amazon S3 API articles as Markdown."""

from dataclasses import dataclass, field
from html.parser import HTMLParser
import re
from urllib.parse import unquote, urlsplit


HEADINGS = {"h1": 1, "h2": 2, "h3": 3}
BLOCKS = {*HEADINGS, "h6", "div", "p", "pre", "dl", "dt", "dd", "ul", "li"}
WIDGETS = {"awsdocs-page-header-container", "code-btn-container"}
FENCE = re.compile(r"^[ \t>]*(`{3,}|~{3,})(.*)$")
INLINE_CODE = re.compile(r"(?<!`)(`+)(?!`).*?(?<!`)\1(?!`)")
RAW_HTML = re.compile(r"(?<!\\)<(?:/?[a-z][\w-]*(?=[\s/>])[^<>]*>|!--)", re.I)


def has_title(markdown, operation):
    return markdown.split("\n", 1)[0].rstrip() == f"# {operation}"


def validate_markdown(markdown, operation):
    if not has_title(markdown, operation):
        raise ValueError(f"Ожидался Markdown-заголовок # {operation}")

    fence = ""
    for number, line in enumerate(markdown.splitlines(), start=1):
        match = FENCE.fullmatch(line)
        if match:
            marker, info = match.groups()
            if fence:
                if marker.startswith(fence) and not info.strip():
                    fence = ""
                continue
            if marker[0] == "~" or "`" not in info:
                fence = marker
                continue
        if not fence and RAW_HTML.search(INLINE_CODE.sub("", line)):
            raise ValueError(f"HTML вне блока кода, строка статьи {number}")

    if fence:
        raise ValueError("Незакрытый блок кода Markdown")


@dataclass
class Node:
    tag: str
    attrs: dict = field(default_factory=dict)
    children: list = field(default_factory=list)


class ArticleTree(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.root = Node("article")
        self.stack = [self.root]
        self.feed(html)
        self.close()
        if len(self.stack) != 1:
            raise ValueError("В HTML остались незакрытые элементы")

    def handle_starttag(self, tag, attrs):
        if tag == "br":
            self.handle_data("\n")
            return
        node = Node(tag, dict(attrs))
        self.stack[-1].children.append(node)
        self.stack.append(node)

    def handle_endtag(self, tag):
        if len(self.stack) == 1 or self.stack[-1].tag != tag:
            raise ValueError(f"Непарный HTML-тег </{tag}>")
        self.stack.pop()

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def classes(node):
    return node.attrs.get("class", "").split()


def widget(node):
    return node.tag.startswith(("awsdocs-", "awsui-")) or WIDGETS.intersection(classes(node))


def plain(node):
    if isinstance(node, str):
        return node
    if widget(node):
        return ""
    return "".join(map(plain, node.children))


def normalize(text):
    return re.sub(r"[ \t\r\n\f]+", " ", text)


def escape_text(text):
    return re.sub(r'([\\`*\[\]<>]|(?<!\w)_|_(?!\w))', r'\\\1', text)


def join_inline(parts):
    chunks = []
    for part in parts:
        if chunks and chunks[-1].endswith(" "):
            part = part.lstrip(" ")
        if part:
            chunks.append(part)
    return "".join(chunks)


def backticks(text, minimum=1):
    longest = max((len(run) for run in re.findall(r"`+", text)), default=0)
    return "`" * max(minimum, longest + 1)


def code_block(node):
    text = plain(node)
    text = re.sub(r"\A(?:[ \t]*\n)+|(?:\n[ \t]*)+\Z", "", text)
    first = text.lstrip().split("\n", 1)[0]
    language = ""
    if re.match(r"(?:[A-Z]+\s+\S+\s+)?HTTP/\d", first):
        language = "http"
    elif re.match(r"<[!?A-Za-z]", first):
        language = "xml"
    fence = backticks(text, minimum=3)
    return f"{fence}{language}\n{text}\n{fence}"


def slug(text):
    text = normalize(text).strip().lower()
    return re.sub(r"[^\w -]", "", text).replace(" ", "-")


class MarkdownArticle:
    def __init__(self, root):
        self.levels = {}
        self.anchors = {}
        self.used_slugs = set()
        self.section_level = 1
        self.index_headings(root)

    def index_headings(self, node):
        if isinstance(node, str) or widget(node):
            return
        if node.tag in HEADINGS:
            self.section_level = self.levels[id(node)] = HEADINGS[node.tag]
        elif node.tag == "dt":
            self.levels[id(node)] = min(6, self.section_level + 1)

        if id(node) in self.levels:
            base = slug(plain(node))
            anchor = base
            suffix = 1
            while anchor in self.used_slugs:
                anchor = f"{base}-{suffix}"
                suffix += 1
            self.used_slugs.add(anchor)
            if node.attrs.get("id"):
                self.anchors[node.attrs["id"]] = anchor

        for child in node.children:
            self.index_headings(child)

    def inline(self, node, heading=False):
        if isinstance(node, str):
            return escape_text(normalize(node))
        if widget(node):
            return ""

        content = join_inline(self.inline(child, heading) for child in node.children)
        text = content.strip()
        if not text:
            return content

        if node.tag == "code":
            code = re.sub(r"[ \t]*\n[ \t]*", " ", plain(node)).strip()
            fence = backticks(code)
            pad = " " if code.startswith("`") or code.endswith("`") else ""
            text = f"{fence}{pad}{code}{pad}{fence}"
        elif node.tag in {"b", "em"} and not heading:
            marker = "**" if node.tag == "b" else "*"
            text = f"{marker}{text}{marker}"
        elif node.tag == "a" and node.attrs.get("href"):
            href = urlsplit(node.attrs["href"])
            target = ""
            if not href.scheme and not href.netloc:
                if href.path:
                    target = href.path
                elif unquote(href.fragment) in self.anchors:
                    target = f"#{self.anchors[unquote(href.fragment)]}"
            if target:
                text = f"[{text}]({target})"
        leading = " " if content.startswith(" ") else ""
        trailing = " " if content.endswith(" ") else ""
        return f"{leading}{text}{trailing}"

    def paragraphs(self, children):
        chunks = []
        pending = []
        for child in children:
            if isinstance(child, Node) and child.tag in BLOCKS:
                chunks.append(join_inline(pending).strip())
                pending.clear()
                chunks.append(self.block(child))
            else:
                pending.append(self.inline(child))
        chunks.append(join_inline(pending).strip())
        return "\n\n".join(chunk for chunk in chunks if chunk)

    def block(self, node):
        if widget(node):
            return ""
        if id(node) in self.levels:
            text = join_inline(self.inline(child, heading=True) for child in node.children).strip()
            return f"{'#' * self.levels[id(node)]} {text}"
        if node.tag == "h6":
            return f"**{normalize(plain(node)).strip()}**"
        if node.tag == "pre":
            return code_block(node)
        if node.tag == "ul":
            items = []
            for child in node.children:
                if isinstance(child, Node) and child.tag == "li":
                    lines = self.paragraphs(child.children).split("\n")
                    items.append("\n".join(["- " + lines[0], *("  " + line if line else "" for line in lines[1:])]))
            return "\n".join(items)
        text = self.paragraphs(node.children)
        if node.tag == "div" and "awsdocs-note" in classes(node):
            return "\n".join(f"> {line}" if line else ">" for line in text.split("\n"))
        return text


def html_to_markdown(html):
    root = ArticleTree(html).root
    return MarkdownArticle(root).paragraphs(root.children)
