#!/usr/bin/env python3
"""Compatibility wrapper for resetting prompt counter after maintenance."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = next((path for path in [SCRIPT_DIR, *SCRIPT_DIR.parents] if (path / "AGENTS.md").exists()), SCRIPT_DIR).resolve()
MAINTENANCE_DIR = REPO_ROOT / "03_TOOLS" / "scripts" / "maintenance"
if str(MAINTENANCE_DIR) not in sys.path:
    sys.path.insert(0, str(MAINTENANCE_DIR))

from prompt_counter import counter_path, read_count, repo_root_from, write_counter  # type: ignore  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True, help="Active project path.")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    repo_root = repo_root_from(REPO_ROOT)
    project = Path(args.project).resolve()
    path = counter_path(project)
    if args.apply:
        write_counter(project, 0, "reset after successful maintenance cycle", repo_root)
        mode = "APPLIED"
    else:
        mode = "DRY_RUN"
    print(f"{mode}: {'reset' if args.apply else 'would reset'} {path} to 0")
    print("MAINTENANCE_DUE: NO")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
