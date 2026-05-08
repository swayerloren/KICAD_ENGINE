#!/usr/bin/env python3
"""Generate AI-readable datasheet summary stubs from source-list rows."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List


FIELDS = [
    "vendor",
    "family",
    "part_number",
    "document_type",
    "title",
    "source_url",
    "local_target_folder",
    "public_redistribution_status",
    "notes",
]

UNKNOWN = "Unknown - requires source verification"


def safe_name(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", value.strip())
    cleaned = re.sub(r"_+", "_", cleaned).strip("_")
    return cleaned or "UNKNOWN"


def discover_inputs(raw_inputs: Iterable[str]) -> List[Path]:
    paths: List[Path] = []
    for raw in raw_inputs:
        path = Path(raw)
        if path.is_dir():
            paths.extend(sorted(path.glob("*.csv")))
            paths.extend(sorted(path.glob("*.json")))
        elif path.exists():
            paths.append(path)
        else:
            raise FileNotFoundError(path)
    return paths


def read_records(paths: Iterable[Path]) -> List[Dict[str, str]]:
    records: List[Dict[str, str]] = []
    for path in paths:
        if path.suffix.lower() == ".csv":
            with path.open("r", encoding="utf-8-sig", newline="") as handle:
                for row in csv.DictReader(handle):
                    normalized = {field: (row.get(field) or "").strip() for field in FIELDS}
                    normalized["_source_file"] = str(path)
                    records.append(normalized)
        elif path.suffix.lower() == ".json":
            with path.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
            items = data.get("records", data) if isinstance(data, dict) else data
            if not isinstance(items, list):
                raise ValueError(f"JSON source list must contain a list: {path}")
            for item in items:
                normalized = {field: str(item.get(field, "") or "").strip() for field in FIELDS}
                normalized["_source_file"] = str(path)
                records.append(normalized)
    return records


def record_matches(record: Dict[str, str], part_filter: str) -> bool:
    if not part_filter:
        return True
    needle = part_filter.lower()
    haystack = " ".join(record.get(field, "") for field in FIELDS).lower()
    return needle in haystack


def stub_text(record: Dict[str, str]) -> str:
    title = record.get("part_number") or record.get("title") or "Unknown Document"
    return "\n".join(
        [
            f"# Datasheet Summary Stub: {title}",
            "",
            f"Generated: {datetime.now().isoformat(timespec='seconds')}",
            "",
            "Status: summary stub only. No document content has been reviewed.",
            "",
            "## Source Metadata",
            "",
            f"- Vendor: {record.get('vendor') or UNKNOWN}",
            f"- Family: {record.get('family') or UNKNOWN}",
            f"- Part / Topic: {record.get('part_number') or UNKNOWN}",
            f"- Document Type: {record.get('document_type') or UNKNOWN}",
            f"- Title: {record.get('title') or UNKNOWN}",
            f"- Source URL: {record.get('source_url') or UNKNOWN}",
            f"- Local Target Folder: {record.get('local_target_folder') or UNKNOWN}",
            f"- Public Redistribution Status: {record.get('public_redistribution_status') or UNKNOWN}",
            f"- Source List: {record.get('_source_file') or UNKNOWN}",
            "",
            "## Verification State",
            "",
            "- Source URL checked: No",
            "- Document downloaded: No",
            "- Redistribution reviewed: No",
            "- Revision checked: No",
            "- Summary extracted from source: No",
            "",
            "## Electrical / Mechanical Summary",
            "",
            f"- Voltage range: {UNKNOWN}",
            f"- Current limits: {UNKNOWN}",
            f"- Absolute maximum ratings: {UNKNOWN}",
            f"- Recommended operating conditions: {UNKNOWN}",
            f"- Pin count: {UNKNOWN}",
            f"- Package type: {UNKNOWN}",
            f"- Special layout rules: {UNKNOWN}",
            f"- Known errata: {UNKNOWN}",
            f"- Lifecycle status: {UNKNOWN}",
            "",
            "## KiCad Links",
            "",
            f"- Related KiCad symbol: {UNKNOWN}",
            f"- Related KiCad footprint: {UNKNOWN}",
            f"- Related KiCad 3D model: {UNKNOWN}",
            "",
            "## Open Questions",
            "",
            "- Verify official source URL.",
            "- Verify document revision/date.",
            "- Confirm redistribution status before bundling.",
            "- Extract summary with page/section citations before design use.",
            "",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="*", default=["06_DATASHEETS/00_INDEX/source_lists"])
    parser.add_argument("--output-dir", default="05_OUTPUTS/datasheet_research/summary_stubs")
    parser.add_argument("--part", default="", help="Optional substring filter for part/topic/title.")
    parser.add_argument("--download", action="store_true", help="Reserved for future use. Currently disabled.")
    args = parser.parse_args()

    if args.download:
        print("--download is disabled. This script only creates summary stubs.", file=sys.stderr)
        return 2

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    records = [r for r in read_records(discover_inputs(args.inputs)) if record_matches(r, args.part)]
    for record in records:
        base = "_".join(
            [
                safe_name(record.get("vendor", "")),
                safe_name(record.get("part_number", "") or record.get("title", "")),
                safe_name(record.get("document_type", "")),
            ]
        )
        (output_dir / f"{base}_SUMMARY_STUB.md").write_text(stub_text(record), encoding="utf-8")
    print(f"Wrote {len(records)} summary stubs to {output_dir}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
