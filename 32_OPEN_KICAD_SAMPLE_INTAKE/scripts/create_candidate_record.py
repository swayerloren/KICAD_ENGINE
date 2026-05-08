"""Create a sample candidate record.

Default mode is dry-run. Pass --apply to write candidate Markdown/JSON records
under 32_OPEN_KICAD_SAMPLE_INTAKE/candidates.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def slugify(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9_.-]+", "_", value.strip()).strip("_").lower()
    return slug or "sample_candidate"


def record_from_args(args: argparse.Namespace) -> dict[str, object]:
    sample_id = args.sample_id or slugify(args.project_name)
    return {
        "sample_id": sample_id,
        "project_name": args.project_name,
        "source_url": args.source_url,
        "source_host": args.source_host,
        "source_owner": args.source_owner,
        "license_name": args.license_name,
        "license_status": args.license_status,
        "candidate_status": "CANDIDATE_LINK_ONLY",
        "public_bundle_status": "EXCLUDED_BY_DEFAULT",
        "benchmark_candidate_status": "NOT_CANDIDATE",
        "human_review_required": True,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "notes": args.notes,
    }


def markdown(record: dict[str, object]) -> str:
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
            "- import_status: `CANDIDATE_LINK_ONLY`",
            "- public_bundle_status: `EXCLUDED_BY_DEFAULT`",
            "- human_review_required: `true`",
            "",
            "## Notes",
            "",
            str(record["notes"] or "No notes."),
            "",
            "## Safety",
            "",
            "No project files have been imported by this record. License and KiCad-file presence still require review.",
        ]
    ) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a KiCad sample candidate record.")
    parser.add_argument("--project-name", required=True)
    parser.add_argument("--source-url", required=True)
    parser.add_argument("--sample-id")
    parser.add_argument("--source-host", default="UNKNOWN")
    parser.add_argument("--source-owner", default="UNKNOWN")
    parser.add_argument("--license-name", default="UNKNOWN")
    parser.add_argument("--license-status", default="NEEDS_HUMAN_LICENSE_REVIEW")
    parser.add_argument("--notes", default="")
    parser.add_argument("--out-dir", type=Path, default=ROOT / "candidates")
    parser.add_argument("--apply", action="store_true", help="Write candidate record files.")
    args = parser.parse_args()

    record = record_from_args(args)
    if not args.apply:
        print(json.dumps({"status": "DRY_RUN_ONLY", "would_create": record}, indent=2))
        return 0

    args.out_dir.mkdir(parents=True, exist_ok=True)
    base = args.out_dir / str(record["sample_id"])
    md_path = base.with_suffix(".md")
    json_path = base.with_suffix(".json")
    if md_path.exists() or json_path.exists():
        raise FileExistsError(f"Candidate record already exists for {record['sample_id']}")
    md_path.write_text(markdown(record), encoding="utf-8")
    json_path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote candidate record: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
