#!/usr/bin/env python3
"""Wrapper for the existing memory index builder."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--apply", action="store_true", help="Indexes are rebuilt only in apply mode.")
    args = parser.parse_args()
    if not args.apply:
        print("DRY_RUN: would run 03_TOOLS/scripts/indexing/build_memory_index.py")
        return 0
    root = Path(args.repo_root).resolve()
    return subprocess.call([sys.executable, str(root / "03_TOOLS/scripts/indexing/build_memory_index.py"), "--repo-root", str(root)])


if __name__ == "__main__":
    raise SystemExit(main())
