#!/usr/bin/env python3
"""Compile superseded/stale report index without deleting old reports."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

from run_memory_maintenance import detect_stale_reports, list_markdown


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--project", default="04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    project = (root / args.project).resolve()
    rows = detect_stale_reports(root, project)
    text = list_markdown("Superseded Reports", "ACTIVE_EVIDENCE", rows, datetime.now().isoformat(timespec="seconds"), project.name)
    target = project / "memory" / "SUPERSEDED_REPORTS.md"
    if args.apply:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8", newline="\n")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
