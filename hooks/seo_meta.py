"""Populate page title and meta description from markdown for site-wide SEO."""

from __future__ import annotations

import re

FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
H1 = re.compile(r"^#\s+(.+)$", re.MULTILINE)
MAX_DESCRIPTION = 160

SECTION_LABELS: dict[str, str] = {
    "llm": "Large Language Models",
    "agents": "AI Agents",
    "ai-architecture": "Systems Architecture",
    "machine-learning": "Machine Learning",
    "guardrails": "Guardrails",
    "ai-act": "AI Act",
    "paths": "Learning Paths",
}


def _strip_frontmatter(markdown: str) -> str:
    if markdown.startswith("---"):
        match = FRONTMATTER.match(markdown)
        if match:
            return markdown[match.end() :]
    return markdown


def _extract_h1(body: str) -> str | None:
    match = H1.search(body)
    return match.group(1).strip() if match else None


def _truncate(text: str, max_len: int = MAX_DESCRIPTION) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= max_len:
        return text
    cut = text[: max_len - 1].rsplit(" ", 1)[0]
    return f"{cut}…"


def _extract_description(body: str) -> str | None:
    lines = body.splitlines()
    h1_idx = next(
        (i for i, line in enumerate(lines) if line.startswith("# ") and not line.startswith("## ")),
        None,
    )
    if h1_idx is None:
        return None

    parts: list[str] = []
    started = False
    for line in lines[h1_idx + 1 :]:
        stripped = line.strip()
        if not stripped:
            if started:
                break
            continue
        if stripped.startswith("#") or stripped.startswith("!") or stripped.startswith("---"):
            break
        if stripped.startswith("<!--"):
            continue
        parts.append(stripped)
        started = True
        joined = " ".join(parts)
        if stripped.endswith(".") and len(joined) >= 40:
            break
        if len(joined) >= MAX_DESCRIPTION:
            break

    if not parts:
        return None
    return _truncate(" ".join(parts))


def _section_from_path(src_path: str) -> str | None:
    top = src_path.split("/", 1)[0]
    return SECTION_LABELS.get(top)


def on_page_markdown(markdown: str, *, page, config, **kwargs) -> str:
    body = _strip_frontmatter(markdown)

    if not page.meta.get("title") and page.file.src_uri != "index.md":
        title = _extract_h1(body)
        if title:
            page.meta["title"] = title

    if not page.meta.get("description"):
        description = _extract_description(body)
        if description:
            page.meta["description"] = description

    section = _section_from_path(page.file.src_path)
    if section:
        page.meta["article_section"] = section

    return markdown
