"""Set a uniform last-updated date on all pages without changing publication dates."""

from __future__ import annotations

LAST_UPDATED = "1 August 2026"
LAST_UPDATED_ISO = "2026-08-01"


def on_page_markdown(markdown: str, *, page, config, **kwargs) -> str:
    page.meta["git_revision_date_localized"] = LAST_UPDATED
    page.meta["git_revision_date_localized_raw_date"] = LAST_UPDATED
    page.meta["git_revision_date_localized_raw_iso_date"] = LAST_UPDATED_ISO
    return markdown
