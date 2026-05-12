#!/usr/bin/env python3
"""Inventory every file under knowledge_scrape without moving anything."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


URL_ID_RE = re.compile(r"(url_\d{6})", re.IGNORECASE)
SKIP_DIRS = {".git", "__pycache__", ".venv", "venv", "node_modules"}


def rel(path: Path, root: Path) -> str:
    return str(path.relative_to(root)).replace("/", "\\")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inventory knowledge_scrape files.")
    parser.add_argument("--repo-root", default=".", help="Repository root.")
    parser.add_argument("--source-root", default="knowledge_scrape", help="Source folder to inventory.")
    parser.add_argument("--output", required=True, help="Inventory CSV output path.")
    return parser.parse_args()


def detect_file_type(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix:
        return suffix.lstrip(".")
    return "no_extension"


def build_rows(repo_root: Path, source_root: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for file_path in sorted(source_root.rglob("*"), key=lambda item: rel(item, repo_root).lower()):
        if not file_path.is_file():
            continue
        if any(part in SKIP_DIRS for part in file_path.parts):
            continue
        relative = rel(file_path, repo_root)
        parent = rel(file_path.parent, repo_root)
        source_relative = rel(file_path, source_root)
        top_level = source_relative.split("\\", 1)[0] if "\\" in source_relative else "__ROOT__"
        match = URL_ID_RE.search(file_path.name)
        rows.append(
            {
                "original_path": relative,
                "file_type": detect_file_type(file_path),
                "size_bytes": str(file_path.stat().st_size),
                "top_level_folder": top_level or "__ROOT__",
                "parent_folder": parent,
                "extension": file_path.suffix.lower(),
                "url_index_id": match.group(1).lower() if match else "",
            }
        )
    return rows


def write_csv(output_path: Path, rows: list[dict[str, str]]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "original_path",
        "file_type",
        "size_bytes",
        "top_level_folder",
        "parent_folder",
        "extension",
        "url_index_id",
    ]
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    source_root = (repo_root / args.source_root).resolve()
    output_path = (repo_root / args.output).resolve()

    if not source_root.exists():
        raise SystemExit(f"SOURCE_ROOT_NOT_FOUND: {source_root}")

    rows = build_rows(repo_root, source_root)
    write_csv(output_path, rows)

    folder_count = len({row["top_level_folder"] for row in rows})
    print(f"INVENTORY_WRITTEN: {output_path}")
    print(f"FILE_COUNT: {len(rows)}")
    print(f"TOP_LEVEL_FOLDER_COUNT: {folder_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
