"""Inject the latest published articles into the homepage at build time."""

from __future__ import annotations

import re
from datetime import date, datetime
from pathlib import Path

MARKER = "<!-- recent-posts -->"
ARTICLE_PATH = re.compile(
    r"^(llm|agents|ai-architecture|machine-learning|guardrails|ai-act)/"
    r"(?!index\.md)[^/]+\.md$"
)
FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
DATE_FIELD = re.compile(r"^date:\s*(\S+)\s*$", re.MULTILINE)
TITLE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
RECENT_COUNT = 7


def _parse_date(raw: str) -> date:
    return datetime.strptime(raw.strip(), "%Y-%m-%d").date()


def _parse_title(content: str) -> str | None:
    body = FRONTMATTER.sub("", content, count=1) if content.startswith("---") else content
    match = TITLE.search(body)
    return match.group(1).strip() if match else None


def _collect_recent_posts(docs_dir: Path) -> list[tuple[date, str, str]]:
    posts: list[tuple[date, str, str]] = []

    for path in docs_dir.rglob("*.md"):
        rel = path.relative_to(docs_dir).as_posix()
        if not ARTICLE_PATH.match(rel):
            continue

        content = path.read_text(encoding="utf-8")
        frontmatter = FRONTMATTER.match(content)
        if not frontmatter:
            continue

        date_match = DATE_FIELD.search(frontmatter.group(1))
        if not date_match:
            continue

        title = _parse_title(content)
        if not title:
            continue

        posts.append((_parse_date(date_match.group(1)), title, rel))

    posts.sort(key=lambda item: item[0], reverse=True)
    return posts[:RECENT_COUNT]


def _format_section(posts: list[tuple[date, str, str]]) -> str:
    if not posts:
        return "## Recent publications\n\n_No posts yet._\n"

    lines = ["## Recent publications", ""]
    for published, title, rel_path in posts:
        href = rel_path.removesuffix(".md") + "/"
        label = f"{published.day} {published.strftime('%B %Y')}"
        lines.append(f"- [{title}]({href}) — {label}")
    lines.append("")
    return "\n".join(lines)


def on_page_markdown(markdown: str, *, page, config, **kwargs) -> str:
    if page.file.src_uri != "index.md":
        return markdown
    if MARKER not in markdown:
        return markdown

    docs_dir = Path(config.docs_dir)
    posts = _collect_recent_posts(docs_dir)
    section = _format_section(posts)
    return markdown.replace(MARKER, section)
