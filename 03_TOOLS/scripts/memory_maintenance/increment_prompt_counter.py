#!/usr/bin/env python3
"""Compatibility wrapper for the maintenance prompt counter."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = next((path for path in [SCRIPT_DIR, *SCRIPT_DIR.parents] if (path / "AGENTS.md").exists()), SCRIPT_DIR).resolve()
MAINTENANCE_DIR = REPO_ROOT / "03_TOOLS" / "scripts" / "maintenance"
if str(MAINTENANCE_DIR) not in sys.path:
    sys.path.insert(0, str(MAINTENANCE_DIR))

from prompt_counter import counter_path, read_count, repo_root_from, threshold, write_counter  # type: ignore  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True, help="Active project path.")
    parser.add_argument("--reason", default="meaningful repo task")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    repo_root = repo_root_from(REPO_ROOT)
    project = Path(args.project).resolve()
    path = counter_path(project)
    old = read_count(path)
    new = old + 1
    if args.apply:
        write_counter(project, new, args.reason, repo_root)
        mode = "APPLIED"
    else:
        mode = "DRY_RUN"
    print(f"{mode}: {path} {old} -> {new}")
    print(f"MAINTENANCE_DUE: {'YES' if new >= threshold(repo_root) else 'NO'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
