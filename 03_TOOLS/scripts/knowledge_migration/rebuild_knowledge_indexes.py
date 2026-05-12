#!/usr/bin/env python3
"""Rebuild repo-wide indexes after knowledge migration work."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


COMMANDS = [
    ["python", "03_TOOLS/scripts/indexing/build_repo_index.py", "--repo-root", "."],
    ["python", "03_TOOLS/scripts/indexing/build_memory_index.py", "--repo-root", "."],
    ["python", "03_TOOLS/scripts/indexing/build_history_index.py", "--repo-root", "."],
    ["python", "03_TOOLS/scripts/ai_quality/build_ai_quality_index.py", "--repo-root", "."],
    ["python", "03_TOOLS/scripts/ai_quality/build_current_known_problems.py", "--repo-root", "."],
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Rebuild indexes after knowledge migration work.")
    parser.add_argument("--repo-root", default=".", help="Repository root.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    for command in COMMANDS:
        completed = subprocess.run(command, cwd=repo_root, capture_output=True, text=True, check=False)
        if completed.returncode != 0:
            raise SystemExit(
                "INDEX_REBUILD_FAILED:\n"
                f"command={' '.join(command)}\n"
                f"stdout=\n{completed.stdout}\n"
                f"stderr=\n{completed.stderr}"
            )
        print(f"INDEX_REBUILT: {' '.join(command[1:3])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
