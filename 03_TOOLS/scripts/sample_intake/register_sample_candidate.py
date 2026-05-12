#!/usr/bin/env python3
"""Create a sample candidate record for open-source KiCad project intake."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from sample_intake_common import CANDIDATE_ROOT, candidate_record, repo_rel, slugify, write_json, write_markdown


def record_markdown(record: dict[str, object]) -> str:
    kicad_files = record.get("kicad_files_present", {})
    return "\n".join(
        [
            "# Sample Candidate Record",
            "",
            f"- sample_id: `{record['sample_id']}`",
            f"- project_name: {record['project_name']}",
            f"- source_url: {record['source_url']}",
            f"- source_host: {record['source_host']}",
            f"- source_owner: {record['source_owner']}",
            f"- license_name: {record['license_name']}",
            f"- license_status: `{record['license_status']}`",
            f"- public_bundle_status: `{record['public_bundle_status']}`",
            f"- candidate_status: `{record['candidate_status']}`",
            f"- human_review_required: `{str(record['human_review_required']).lower()}`",
            f"- kicad_pro_present: `{str(bool(kicad_files.get('kicad_pro'))).lower()}`",
            f"- kicad_sch_present: `{str(bool(kicad_files.get('kicad_sch'))).lower()}`",
            f"- kicad_pcb_present: `{str(bool(kicad_files.get('kicad_pcb'))).lower()}`",
            f"- estimated_size_class: `{record['estimated_size_class']}`",
            "",
            "## Notes",
            "",
            str(record.get("notes") or "No notes."),
            "",
            "## Safety",
            "",
            "This record does not import project files by itself. License, file presence, and quality still require review.",
            "",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Create or preview a KiCad sample candidate record.")
    parser.add_argument("--project-name", required=True)
    parser.add_argument("--source-url", required=True)
    parser.add_argument("--sample-id", default="")
    parser.add_argument("--source-host", default="UNKNOWN")
    parser.add_argument("--source-owner", default="UNKNOWN")
    parser.add_argument("--license-name", default="UNKNOWN")
    parser.add_argument("--license-status", default="NEEDS_HUMAN_LICENSE_REVIEW")
    parser.add_argument("--notes", default="")
    parser.add_argument("--estimated-size-class", default="UNKNOWN")
    parser.add_argument("--sample-path", type=Path)
    parser.add_argument("--out-dir", type=Path, default=CANDIDATE_ROOT)
    parser.add_argument("--apply", action="store_true", help="Write candidate JSON and Markdown records.")
    args = parser.parse_args()

    record = candidate_record(
        project_name=args.project_name,
        source_url=args.source_url,
        sample_id=args.sample_id or slugify(args.project_name),
        source_host=args.source_host,
        source_owner=args.source_owner,
        license_name=args.license_name,
        license_status=args.license_status,
        notes=args.notes,
        estimated_size_class=args.estimated_size_class,
        sample_path=args.sample_path.resolve() if args.sample_path else None,
    )
    if not args.apply:
        print(json.dumps({"status": "DRY_RUN_ONLY", "would_create": record}, indent=2))
        return 0

    args.out_dir.mkdir(parents=True, exist_ok=True)
    base = args.out_dir / str(record["sample_id"])
    json_path = base.with_suffix(".json")
    md_path = base.with_suffix(".md")
    if json_path.exists() or md_path.exists():
        raise FileExistsError(f"Candidate record already exists: {repo_rel(json_path)}")
    write_json(json_path, record)
    write_markdown(md_path, record_markdown(record))
    print(f"Wrote candidate record: {repo_rel(json_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
