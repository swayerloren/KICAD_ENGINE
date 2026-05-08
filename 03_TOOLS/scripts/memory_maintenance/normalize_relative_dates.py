#!/usr/bin/env python3
"""Detect relative date language in memory/history markdown.

Default mode reports only. This script does not rewrite prose automatically;
unresolved vague dates are flagged for human review.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from run_memory_maintenance import detect_relative_dates


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--project", default="04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE")
    parser.add_argument("--apply", action="store_true", help="Reserved; writes no source edits.")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    project = (root / args.project).resolve()
    hits = detect_relative_dates(root, [root / "01_MEMORY", root / "02_HISTORY", project / "memory", project / "history", project / "reports"])
    print(json.dumps({"relative_date_hits": hits}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
