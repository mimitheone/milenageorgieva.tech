#!/usr/bin/env python3
"""Add date frontmatter and Related notes sections from LinkedIn footers."""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

DOCS = Path(__file__).resolve().parents[1] / "docs"

MONTHS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}

LINKEDIN_FOOTER = re.compile(
    r"\*Originally published on \[LinkedIn\].*?, (\d{1,2}) (\w+) (\d{4})\.\*"
)
FRONTMATTER = re.compile(r"^---\s*\n(?:.*\n)*?---\s*\n", re.MULTILINE)
TITLE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
RELATED_SECTION = re.compile(
    r"\n## Related notes\n(?:- .+\n)+\n(?=---\n\n\*Originally published)",
    re.MULTILINE,
)

# Symmetric pairs: each entry lists related doc paths (relative to docs/).
RELATED: dict[str, list[str]] = {
    "llm/llm-cost-predictability.md": ["llm/llm-cost-optimization.md"],
    "llm/llm-cost-optimization.md": ["llm/llm-cost-predictability.md"],
    "agents/darwin-godel-machine.md": [
        "agents/self-improving-agents.md",
        "agents/dependency-inversion-principle.md",
    ],
    "agents/self-improving-agents.md": [
        "agents/darwin-godel-machine.md",
        "agents/dependency-inversion-principle.md",
        "agents/designing-an-agent.md",
    ],
    "agents/dependency-inversion-principle.md": [
        "agents/darwin-godel-machine.md",
        "agents/self-improving-agents.md",
        "ai-architecture/agent-contracts.md",
    ],
    "agents/what-is-an-agent.md": [
        "agents/designing-an-agent.md",
        "agents/agent-definition-template.md",
        "agents/core-design-principles.md",
    ],
    "agents/designing-an-agent.md": [
        "agents/what-is-an-agent.md",
        "agents/agent-definition-template.md",
        "agents/fallback-architecture.md",
    ],
    "agents/agent-definition-template.md": [
        "agents/what-is-an-agent.md",
        "agents/designing-an-agent.md",
    ],
    "agents/core-design-principles.md": [
        "agents/fallback-architecture.md",
        "agents/what-is-an-agent.md",
        "ai-architecture/ai-systems-architecture.md",
    ],
    "agents/fallback-architecture.md": [
        "agents/core-design-principles.md",
        "agents/designing-an-agent.md",
    ],
    "agents/agent-to-agent-protocol.md": [
        "agents/agent-communication-patterns.md",
    ],
    "agents/agent-communication-patterns.md": [
        "agents/agent-to-agent-protocol.md",
        "ai-architecture/agent-contracts.md",
    ],
    "ai-architecture/single-responsibility-principle.md": [
        "ai-architecture/interface-segregation-principle.md",
        "agents/designing-an-agent.md",
    ],
    "ai-architecture/interface-segregation-principle.md": [
        "ai-architecture/single-responsibility-principle.md",
        "ai-architecture/agent-contracts.md",
    ],
    "ai-architecture/agent-contracts.md": [
        "ai-architecture/interface-segregation-principle.md",
        "agents/agent-to-agent-protocol.md",
        "agents/agent-communication-patterns.md",
    ],
    "ai-architecture/components-and-skills.md": [
        "agents/designing-an-agent.md",
        "ai-architecture/reuse-release-equivalence-principle.md",
    ],
    "ai-architecture/reuse-release-equivalence-principle.md": [
        "ai-architecture/components-and-skills.md",
        "ai-architecture/acyclic-dependency-principle.md",
    ],
    "ai-architecture/acyclic-dependency-principle.md": [
        "ai-architecture/stable-dependencies-principle.md",
        "ai-architecture/reuse-release-equivalence-principle.md",
    ],
    "ai-architecture/stable-dependencies-principle.md": [
        "ai-architecture/acyclic-dependency-principle.md",
        "agents/dependency-inversion-principle.md",
    ],
    "ai-architecture/ai-systems-architecture.md": [
        "agents/core-design-principles.md",
        "agents/fallback-architecture.md",
        "ai-architecture/single-responsibility-principle.md",
    ],
    "machine-learning/overfitting-in-business.md": [
        "ai-act/bias-and-fairness-controls.md",
        "machine-learning/ml-algorithms.md",
    ],
    "machine-learning/clustering.md": [
        "machine-learning/knn.md",
        "machine-learning/ml-algorithms.md",
    ],
    "machine-learning/knn.md": [
        "machine-learning/clustering.md",
        "machine-learning/ml-algorithms.md",
    ],
    "machine-learning/shap.md": [
        "machine-learning/ml-algorithms.md",
        "machine-learning/overfitting-in-business.md",
    ],
    "machine-learning/ml-algorithms.md": [
        "machine-learning/arima.md",
        "machine-learning/clustering.md",
        "machine-learning/knn.md",
        "machine-learning/shap.md",
    ],
    "machine-learning/arima.md": [
        "machine-learning/ml-algorithms.md",
        "machine-learning/overfitting-in-business.md",
        "machine-learning/shap.md",
    ],
    "guardrails/prompt-injection.md": [
        "guardrails/ai-guardrails.md",
        "guardrails/secure-rag.md",
    ],
    "guardrails/ai-guardrails.md": [
        "guardrails/prompt-injection.md",
        "guardrails/safety-enforcement.md",
        "guardrails/relevance-control.md",
    ],
    "guardrails/relevance-control.md": [
        "guardrails/ai-guardrails.md",
        "guardrails/secure-rag.md",
    ],
    "guardrails/tool-access-control.md": [
        "guardrails/rule-based-filters.md",
        "guardrails/safety-enforcement.md",
    ],
    "guardrails/rule-based-filters.md": [
        "guardrails/tool-access-control.md",
        "guardrails/safety-enforcement.md",
        "guardrails/ai-guardrails.md",
    ],
    "guardrails/pii-protection.md": [
        "guardrails/secure-rag.md",
        "guardrails/ai-guardrails.md",
    ],
    "guardrails/secure-rag.md": [
        "guardrails/prompt-injection.md",
        "guardrails/relevance-control.md",
        "guardrails/pii-protection.md",
    ],
    "guardrails/safety-enforcement.md": [
        "guardrails/ai-guardrails.md",
        "guardrails/tool-access-control.md",
        "guardrails/rule-based-filters.md",
    ],
    "ai-act/eu-ai-act-implementation.md": [
        "ai-act/high-risk-ai-systems.md",
        "ai-act/risk-management.md",
        "ai-act/human-in-the-loop.md",
        "ai-act/monitoring-and-post-market-surveillance.md",
    ],
    "ai-act/high-risk-ai-systems.md": [
        "ai-act/eu-ai-act-implementation.md",
        "ai-act/risk-management.md",
        "ai-act/human-in-the-loop.md",
    ],
    "ai-act/human-in-the-loop.md": [
        "ai-act/high-risk-ai-systems.md",
        "ai-act/risk-management.md",
        "ai-act/monitoring-and-post-market-surveillance.md",
    ],
    "ai-act/risk-management.md": [
        "ai-act/high-risk-ai-systems.md",
        "ai-act/human-in-the-loop.md",
        "ai-act/logging-and-auditability.md",
    ],
    "ai-act/bias-and-fairness-controls.md": [
        "machine-learning/overfitting-in-business.md",
        "ai-act/logging-and-auditability.md",
        "ai-act/high-risk-ai-systems.md",
    ],
    "ai-act/logging-and-auditability.md": [
        "ai-act/risk-management.md",
        "ai-act/monitoring-and-post-market-surveillance.md",
        "ai-act/bias-and-fairness-controls.md",
    ],
    "ai-act/monitoring-and-post-market-surveillance.md": [
        "ai-act/logging-and-auditability.md",
        "ai-act/human-in-the-loop.md",
        "ai-act/high-risk-ai-systems.md",
    ],
}


def parse_linkedin_date(text: str) -> str | None:
    match = LINKEDIN_FOOTER.search(text)
    if not match:
        return None
    day, month_name, year = match.groups()
    month = MONTHS.get(month_name.lower())
    if not month:
        raise ValueError(f"Unknown month: {month_name}")
    return datetime(int(year), month, int(day)).strftime("%Y-%m-%d")


def get_title(path: Path) -> str:
    content = path.read_text(encoding="utf-8")
    body = FRONTMATTER.sub("", content, count=1) if content.startswith("---") else content
    match = TITLE.search(body)
    if not match:
        raise ValueError(f"No title in {path}")
    return match.group(1).strip()


def build_related_section(from_file: Path, related_docs: list[str]) -> str:
    lines = ["## Related notes", ""]
    for to_doc in related_docs:
        target = DOCS / to_doc
        title = get_title(target)
        href = os_path_relative(from_file.parent, target).as_posix()
        lines.append(f"- [{title}]({href})")
    lines.append("")
    return "\n".join(lines) + "\n"


def os_path_relative(from_dir: Path, to_file: Path) -> Path:
    return Path(__import__("os").path.relpath(to_file, start=from_dir))


def ensure_frontmatter(content: str, iso_date: str) -> str:
    if content.startswith("---"):
        if re.search(r"^date:\s*", content, re.MULTILINE):
            return content
        return content.replace("---\n", f"---\ndate: {iso_date}\n", 1)
    return f"---\ndate: {iso_date}\n---\n\n{content}"


def insert_related(content: str, section: str) -> str:
    marker = "---\n\n*Originally published on [LinkedIn]"
    if marker not in content:
        return content
    if "## Related notes" in content:
        content = RELATED_SECTION.sub("\n", content)
    return content.replace(marker, section + marker, 1)


def process_file(rel_path: str) -> None:
    path = DOCS / rel_path
    content = path.read_text(encoding="utf-8")
    iso_date = parse_linkedin_date(content)
    if not iso_date:
        return

    updated = ensure_frontmatter(content, iso_date)

    if rel_path in RELATED:
        section = build_related_section(path, RELATED[rel_path])
        updated = insert_related(updated, section)

    if updated != content:
        path.write_text(updated, encoding="utf-8")
        print(f"updated {rel_path}")


def main() -> None:
    for rel_path in sorted(RELATED.keys()):
        process_file(rel_path)

    for path in DOCS.rglob("*.md"):
        rel = path.relative_to(DOCS).as_posix()
        if rel in RELATED:
            continue
        content = path.read_text(encoding="utf-8")
        if not LINKEDIN_FOOTER.search(content):
            continue
        iso_date = parse_linkedin_date(content)
        if not iso_date:
            continue
        updated = ensure_frontmatter(content, iso_date)
        if updated != content:
            path.write_text(updated, encoding="utf-8")
            print(f"dated {rel}")


if __name__ == "__main__":
    main()
