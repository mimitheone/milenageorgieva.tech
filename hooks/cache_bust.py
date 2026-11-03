"""Append git revision to static assets so CDN caches refresh after deploy."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

THEME_ASSET = re.compile(
    r"(?P<url>(?:\.\./)*assets/(?:stylesheets|javascripts)/[^\"'?#]+)(?=[\"'])"
)
DEPLOY_MARKER = re.compile(r"<!-- deploy: [a-f0-9]+ -->\n?", re.IGNORECASE)


def _git_revision(config_file: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=config_file.parent,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "dev"


def on_config(config, **kwargs):
    config_file = Path(getattr(config, "config_file_path", "mkdocs.yml"))
    revision = _git_revision(config_file)

    config.extra_css = [
        f"{href}?v={revision}" if href.split("?")[0].endswith("extra.css") else href
        for href in config.extra_css
    ]


def on_post_build(config, **kwargs):
    config_file = Path(getattr(config, "config_file_path", "mkdocs.yml"))
    revision = _git_revision(config_file)
    site_dir = Path(config.site_dir)

    marker = f"<!-- deploy: {revision} -->\n"

    for html_path in site_dir.rglob("*.html"):
        original = html_path.read_text(encoding="utf-8")
        content = DEPLOY_MARKER.sub("", original, count=1)
        updated = THEME_ASSET.sub(
            lambda match: f"{match.group('url')}?v={revision}",
            content,
        )
        if "<!doctype html>" in updated[:50].lower():
            updated = re.sub(
                r"(<!doctype html>\s*)",
                rf"\1{marker}",
                updated,
                count=1,
                flags=re.IGNORECASE,
            )
        if updated != original:
            html_path.write_text(updated, encoding="utf-8")
