#!/usr/bin/env python3
"""Read-only license screening for a local sample project folder."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from sample_intake_common import (
    REVIEW_ROOT,
    find_license_files,
    repo_rel,
    screen_license_text,
    slugify,
    utc_now_iso,
    write_json,
    write_markdown,
)


def public_bundle_status(status: str) -> str:
    return "PUBLIC_BUNDLE_ALLOWED" if status == "PUBLIC_BUNDLE_ALLOWED" else "EXCLUDED_BY_DEFAULT"


def build_record(sample_path: Path, sample_id: str) -> dict[str, object]:
    license_files = find_license_files(sample_path)
    license_name = "UNKNOWN"
    notes = "No common license file found."
    status = "NO_LICENSE_FOUND"
    excerpt = ""
    if license_files:
        text = license_files[0].read_text(encoding="utf-8", errors="replace")
        status, license_name, notes = screen_license_text(text[:20000])
        excerpt = " ".join(text.split())[:500]
    return {
        "schema_version": "1.0",
        "tool": "audit_sample_license",
        "generated_at": utc_now_iso(),
        "read_only_mode": True,
        "sample_id": sample_id,
        "sample_path": str(sample_path),
        "license_files": [repo_rel(path) for path in license_files],
        "license_name": license_name,
        "license_status": status,
        "public_bundle_status": public_bundle_status(status),
        "human_review_required": status != "PUBLIC_BUNDLE_ALLOWED",
        "notes": notes,
        "license_text_excerpt": excerpt,
    }


def markdown(record: dict[str, object]) -> str:
    return "\n".join(
        [
            "# Sample License Audit",
            "",
            f"Status: `{record['license_status']}`",
            f"Sample: `{record['sample_id']}`",
            f"Sample path: `{record['sample_path']}`",
            f"License name: `{record['license_name']}`",
            f"Public bundle status: `{record['public_bundle_status']}`",
            f"Human review required: `{str(record['human_review_required']).lower()}`",
            "",
            "## Notes",
            "",
            str(record.get("notes") or "No notes."),
            "",
            "## License Files",
            "",
        ]
        + [f"- `{item}`" for item in record.get("license_files", [])]
        + [
            "",
            "## Warning",
            "",
            "This is practical screening only. Human license review is still required before public bundling.",
            "",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a local sample folder for license evidence.")
    parser.add_argument("--sample-path", type=Path, required=True)
    parser.add_argument("--sample-id", default="")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--report-dir", type=Path, default=REVIEW_ROOT)
    args = parser.parse_args()

    sample_path = args.sample_path.resolve()
    sample_id = args.sample_id or slugify(sample_path.name)
    record = build_record(sample_path, sample_id)

    json_output = args.json_output
    md_output = args.output
    if not json_output and not md_output:
        json_output = args.report_dir / f"{sample_id}_license_audit.json"
        md_output = args.report_dir / f"{sample_id}_license_audit.md"

    if json_output:
        write_json(json_output, record)
    if md_output:
        write_markdown(md_output, markdown(record))
        print(f"Wrote license audit: {repo_rel(md_output)}")
    else:
        print(json.dumps(record, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
