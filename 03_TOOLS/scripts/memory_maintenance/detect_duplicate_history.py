#!/usr/bin/env python3
"""Detect duplicate blocker/history topics without deleting records."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from run_memory_maintenance import detect_duplicate_history


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--project", default="04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    project = (root / args.project).resolve()
    print(json.dumps(detect_duplicate_history(root, project), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
