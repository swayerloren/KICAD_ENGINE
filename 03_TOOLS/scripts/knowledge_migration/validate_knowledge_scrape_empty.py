#!/usr/bin/env python3
"""Check whether knowledge_scrape is empty or removable."""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate whether knowledge_scrape is empty.")
    parser.add_argument("--repo-root", default=".", help="Repository root.")
    parser.add_argument("--source-root", default="knowledge_scrape", help="Source folder.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    source_root = (repo_root / args.source_root).resolve()
    if not source_root.exists():
        print("SOURCE_ROOT_ALREADY_REMOVED")
        return 0

    files = [path for path in source_root.rglob("*") if path.is_file()]
    directories = [path for path in source_root.rglob("*") if path.is_dir()]
    empty_directories = [path for path in directories if not any(path.iterdir())]

    print(f"REMAINING_FILE_COUNT: {len(files)}")
    print(f"REMAINING_DIRECTORY_COUNT: {len(directories)}")
    print(f"EMPTY_DIRECTORY_COUNT: {len(empty_directories)}")
    if files:
        print("VALIDATION_RESULT: NOT_EMPTY")
        return 1
    print("VALIDATION_RESULT: EMPTY_OR_REMOVABLE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
