"""Find and read the local Amazon S3 API reference."""

from dataclasses import dataclass
import re

if __package__:
    from .import_s3_api import OPERATION_LINK, ROOT, snapshot_path
    from .s3_markdown import FENCE
else:
    from import_s3_api import OPERATION_LINK, ROOT, snapshot_path
    from s3_markdown import FENCE


HEADING = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.+?)\s*$")
HEADING_LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")
MAX_SEARCH_RESULTS = 20
SNIPPET_LENGTH = 260


@dataclass(frozen=True)
class Heading:
    level: int
    title: str
    index: int


def normalize(text):
    return " ".join(text.casefold().split())


def headings(lines):
    fence = ""
    for index, line in enumerate(lines):
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
        if not fence and (match := HEADING.fullmatch(line)):
            marker, title = match.groups()
            title = HEADING_LINK.sub(r"\1", title).strip("`")
            yield Heading(len(marker), title, index)


def list_operations(prefix=""):
    index = (ROOT / "README.md").read_text(encoding="utf-8")
    names = sorted(set(OPERATION_LINK.findall(index)))
    prefix = normalize(prefix)
    return [name for name in names if name.casefold().startswith(prefix)]


def get_operation(name, section=""):
    canonical_names = {operation.casefold(): operation for operation in list_operations()}
    operation = canonical_names.get(normalize(name))
    if operation is None:
        raise ValueError(f"Unknown S3 operation {name!r}. Use list_operations to find its name.")

    path = snapshot_path(operation)
    markdown = path.read_text(encoding="utf-8-sig")
    source = path.relative_to(ROOT).as_posix()
    if not normalize(section):
        return f"Source: {source}\n\n{markdown}"

    lines = markdown.splitlines()
    article_headings = list(headings(lines))
    section_name = normalize(section)
    matches = []
    for position, heading in enumerate(article_headings):
        if normalize(heading.title) != section_name:
            continue
        end = next(
            (other.index for other in article_headings[position + 1:] if other.level <= heading.level),
            len(lines),
        )
        excerpt = "\n".join(lines[heading.index:end]).rstrip()
        matches.append(f"Source: {source}, line {heading.index + 1}\n\n{excerpt}")

    if not matches:
        titles = ", ".join(dict.fromkeys(heading.title for heading in article_headings))
        raise ValueError(f"Section {section!r} was not found in {operation}. Available headings: {titles}")
    return "\n\n".join(matches)


def search_docs(query, limit=5):
    phrase = normalize(query)
    if not phrase:
        raise ValueError("Provide an operation name, header, error code, or other search terms.")
    terms = phrase.split()
    results = []
    for operation in list_operations():
        path = snapshot_path(operation)
        lines = path.read_text(encoding="utf-8-sig").splitlines()
        source = path.relative_to(ROOT).as_posix()
        article_headings = list(headings(lines))
        ends = [heading.index for heading in article_headings[1:]] + [len(lines)]
        for heading, end in zip(article_headings, ends):
            title = normalize(heading.title)
            body = lines[heading.index + 1:end]
            searchable = normalize(" ".join([heading.title, *body]))
            context = f"{operation.casefold()} {searchable}"
            if not any(term in searchable for term in terms) or not all(term in context for term in terms):
                continue

            rank = 3
            if title == phrase:
                rank = 0
            elif phrase in title:
                rank = 1
            elif phrase in searchable:
                rank = 2
            snippet = best_snippet(body, heading.title, phrase, terms)
            results.append((rank, {
                "operation": operation,
                "section": heading.title,
                "source": source,
                "line": heading.index + 1,
                "snippet": snippet,
            }))
    results.sort(key=lambda match: match[0])
    return [hit for _, hit in results[:limit]]


def best_snippet(body, title, phrase, terms):
    candidates = [" ".join(line.split()) for line in body if line.strip()]
    snippet = max(
        candidates,
        key=lambda line: (phrase in normalize(line), sum(term in normalize(line) for term in terms)),
        default=title,
    )
    if len(snippet) <= SNIPPET_LENGTH:
        return snippet

    match = re.search(re.escape(phrase), snippet, re.IGNORECASE)
    if match is None:
        match = re.search("|".join(map(re.escape, terms)), snippet, re.IGNORECASE)
    start = max(0, match.start() - 60) if match else 0
    end = start + SNIPPET_LENGTH
    return ("…" if start else "") + snippet[start:end] + ("…" if end < len(snippet) else "")
