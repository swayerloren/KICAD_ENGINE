#!/usr/bin/env python3
"""Move a single knowledge_scrape item based on the migration ledger."""

from __future__ import annotations

import argparse
import csv
import shutil
import subprocess
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Move one knowledge_scrape item from the migration ledger.")
    parser.add_argument("--repo-root", default=".", help="Repository root.")
    parser.add_argument("--ledger", required=True, help="Ledger CSV path.")
    parser.add_argument("--original-path", required=True, help="Repo-relative source file path from the ledger.")
    parser.add_argument(
        "--normalized-source",
        help="Required for MOVE_NORMALIZED apply mode. Path to a pre-created normalized canonical file.",
    )
    parser.add_argument("--apply", action="store_true", help="Actually perform the move.")
    return parser.parse_args()


def load_ledger(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        return rows, list(reader.fieldnames or [])


def write_ledger(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def git_tracked(repo_root: Path, relative_path: str) -> bool:
    result = subprocess.run(
        ["git", "ls-files", "--error-unmatch", relative_path],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode == 0


def git_mv(repo_root: Path, src: str, dst: str) -> None:
    destination = Path(dst)
    destination.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["git", "mv", src, dst],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(f"git mv failed for {src} -> {dst}\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}")


def prune_empty_parents(path: Path, stop_at: Path) -> None:
    current = path.parent
    while current != stop_at and current.exists():
        if any(current.iterdir()):
            return
        current.rmdir()
        current = current.parent


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    ledger_path = (repo_root / args.ledger).resolve()
    rows, fieldnames = load_ledger(ledger_path)

    match = None
    for row in rows:
        if row["original_path"] == args.original_path:
            match = row
            break
    if match is None:
        raise SystemExit(f"LEDGER_ROW_NOT_FOUND: {args.original_path}")

    src = (repo_root / match["original_path"]).resolve()
    dst = (repo_root / match["canonical_destination"]).resolve()
    action = match["action"]

    print(f"ACTION: {action}")
    print(f"SOURCE: {src}")
    print(f"DESTINATION: {dst}")

    if not args.apply:
        print("DRY_RUN_ONLY")
        return 0

    if not src.exists():
        raise SystemExit(f"SOURCE_NOT_FOUND: {src}")

    if action == "MOVE_NORMALIZED":
        if not args.normalized_source:
            raise SystemExit("MOVE_NORMALIZED_REQUIRES --normalized-source in apply mode.")
        normalized_source = (repo_root / args.normalized_source).resolve()
        if not normalized_source.exists():
            raise SystemExit(f"NORMALIZED_SOURCE_NOT_FOUND: {normalized_source}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        if normalized_source != dst:
            shutil.copy2(normalized_source, dst)
        archive_root = repo_root / "02_HISTORY" / "knowledge_scrape_migration" / "original_archives"
        archive_path = archive_root / Path(match["original_path"]).relative_to("knowledge_scrape")
        archive_path.parent.mkdir(parents=True, exist_ok=True)
        if git_tracked(repo_root, match["original_path"]):
            git_mv(repo_root, match["original_path"], str(archive_path.relative_to(repo_root)).replace("/", "\\"))
        else:
            shutil.move(str(src), str(archive_path))
        match["canonical_destination"] = str(dst.relative_to(repo_root)).replace("/", "\\")
        match["notes"] = (match["notes"] + " | normalized_source_applied").strip(" |")
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        destination_rel = str(dst.relative_to(repo_root)).replace("/", "\\")
        if git_tracked(repo_root, match["original_path"]):
            git_mv(repo_root, match["original_path"], destination_rel)
        else:
            shutil.move(str(src), str(dst))
        prune_empty_parents(src, repo_root / "knowledge_scrape")

    match["moved_yes_no"] = "YES"
    match["migration_date"] = date.today().isoformat()
    match["validation_status"] = "MOVED_PENDING_POST_MOVE_VALIDATION"
    write_ledger(ledger_path, fieldnames, rows)

    print("MOVE_APPLIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
