#!/usr/bin/env python3
"""Compatibility wrapper for maintenance-due checks."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = next((path for path in [SCRIPT_DIR, *SCRIPT_DIR.parents] if (path / "AGENTS.md").exists()), SCRIPT_DIR).resolve()
MAINTENANCE_DIR = REPO_ROOT / "03_TOOLS" / "scripts" / "maintenance"
if str(MAINTENANCE_DIR) not in sys.path:
    sys.path.insert(0, str(MAINTENANCE_DIR))

from prompt_counter import counter_path, read_count, repo_root_from, threshold  # type: ignore  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True, help="Active project path.")
    args = parser.parse_args()

    repo_root = repo_root_from(REPO_ROOT)
    project = Path(args.project).resolve()
    path = counter_path(project)
    count = read_count(path)
    due = count >= threshold(repo_root)
    print(f"PROMPT_COUNTER_FILE: {path}")
    print(f"PROMPT_COUNT: {count}")
    print(f"MAINTENANCE_THRESHOLD: {threshold(repo_root)}")
    print(f"MAINTENANCE_DUE: {'YES' if due else 'NO'}")
    if due:
        print("RESULT: BLOCK_ENGINEERING_WORK_UNTIL_MAINTENANCE_RUNS")
        print(f"RUN: python 03_TOOLS\\scripts\\maintenance\\run_maintenance_cycle.py --project {project}")
    else:
        print("RESULT: MAINTENANCE_NOT_DUE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
