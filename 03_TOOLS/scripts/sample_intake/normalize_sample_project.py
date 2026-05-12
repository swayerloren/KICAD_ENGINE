#!/usr/bin/env python3
"""Dry-run-first creation of a normalized working sample copy."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from sample_intake_common import (
    IMPORTED_ROOT,
    NORMALIZED_ROOT,
    REVIEW_ROOT,
    ensure_not_active_project,
    is_inside,
    repo_rel,
    timestamp_slug,
    utc_now_iso,
    write_json,
    write_markdown,
)


def report_markdown(report: dict[str, object]) -> str:
    errors = report.get("errors", [])
    return "\n".join(
        [
            "# Sample Normalization Report",
            "",
            f"Status: `{report['status']}`",
            f"Generated: `{report['generated_at']}`",
            f"Sample ID: `{report['sample_id']}`",
            f"Imported path: `{report['imported_path']}`",
            f"Normalized path: `{report['normalized_path']}`",
            f"Copied: `{str(report['copied']).lower()}`",
            "",
            "## Errors",
            "",
        ]
        + ([f"- {item}" for item in errors] if errors else ["- none"])
        + ["", "Imported originals remain read-only.", ""]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Create or preview a normalized working copy from an imported sample.")
    parser.add_argument("--sample-id", required=True)
    parser.add_argument("--imported-path", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, default=NORMALIZED_ROOT)
    parser.add_argument("--reports-dir", type=Path, default=REVIEW_ROOT)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    imported = args.imported_path.resolve()
    ensure_not_active_project(imported)
    run_id = timestamp_slug()
    normalized_path = args.out_dir / f"{args.sample_id}_{run_id}"
    errors: list[str] = []
    if not imported.exists() or not imported.is_dir():
        errors.append("imported_path must be an existing folder.")
    if not is_inside(imported, IMPORTED_ROOT):
        errors.append("Normalization must start from 32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals.")

    copied = False
    status = "DRY_RUN_READY_TO_COPY" if not errors else "DRY_RUN_BLOCKED"
    if args.apply and not errors:
        args.out_dir.mkdir(parents=True, exist_ok=True)
        shutil.copytree(imported, normalized_path)
        copied = True
        status = "NORMALIZED_COPY_CREATED"
    elif args.apply:
        status = "NORMALIZED_COPY_BLOCKED"

    report = {
        "schema_version": "1.0",
        "tool": "normalize_sample_project",
        "generated_at": utc_now_iso(),
        "sample_id": args.sample_id,
        "imported_path": str(imported),
        "normalized_path": str(normalized_path),
        "status": status,
        "copied": copied,
        "read_only_mode": not args.apply,
        "errors": errors,
    }

    args.reports_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.reports_dir / f"normalized_copy_{args.sample_id}_{run_id}.json"
    md_path = args.reports_dir / f"normalized_copy_{args.sample_id}_{run_id}.md"
    write_json(json_path, report)
    write_markdown(md_path, report_markdown(report))
    print(f"Wrote normalization report: {repo_rel(md_path)}")
    return 1 if errors and args.apply else 0


if __name__ == "__main__":
    raise SystemExit(main())
