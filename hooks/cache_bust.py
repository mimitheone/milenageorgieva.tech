"""Append git revision to extra.css so CDN caches refresh after deploy."""

from __future__ import annotations

import subprocess
from pathlib import Path


def on_config(config, **kwargs):
    config_file = Path(getattr(config, "config_file_path", "mkdocs.yml"))
    try:
        revision = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=config_file.parent,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        revision = "dev"

    config.extra_css = [
        f"{href}?v={revision}" if href.split("?")[0].endswith("extra.css") else href
        for href in config.extra_css
    ]
