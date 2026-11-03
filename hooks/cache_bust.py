"""Append git revision to static assets so CDN caches refresh after deploy."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

THEME_ASSET = re.compile(
    r"(?P<url>assets/(?:stylesheets|javascripts)/[^\"'?#]+)(?=[\"'])"
)


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

    for html_path in site_dir.rglob("*.html"):
        content = html_path.read_text(encoding="utf-8")
        updated = THEME_ASSET.sub(
            lambda match: f"{match.group('url')}?v={revision}",
            content,
        )
        if updated != content:
            html_path.write_text(updated, encoding="utf-8")
