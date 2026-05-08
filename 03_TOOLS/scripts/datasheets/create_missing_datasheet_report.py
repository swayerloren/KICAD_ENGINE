#!/usr/bin/env python3
"""Create a markdown report of missing or weak datasheet metadata."""

from __future__ import annotations

import argparse
import csv
import json
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

WEAK_REDISTRIBUTION = {"", "UNKNOWN", "REQUIRES_LICENSE_REVIEW"}


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


def missing_reasons(record: Dict[str, str]) -> List[str]:
    reasons: List[str] = []
    for field in FIELDS:
        if not record.get(field):
            reasons.append(f"Missing {field}")
    if record.get("source_url", "").lower().endswith(".pdf"):
        reasons.append("Direct PDF URL needs license and revision review")
    if record.get("public_redistribution_status", "").upper() in WEAK_REDISTRIBUTION:
        reasons.append("Redistribution status needs review")
    if "placeholder" in record.get("notes", "").lower():
        reasons.append("Placeholder row needs curation")
    return reasons


def write_report(records: List[Dict[str, str]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    rows = [(record, missing_reasons(record)) for record in records]
    weak = [(record, reasons) for record, reasons in rows if reasons]
    lines = [
        "# Missing Datasheet Metadata Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        f"Records reviewed: {len(records)}",
        f"Records needing work: {len(weak)}",
        "",
        "| Vendor | Family | Part / Topic | Document Type | Reasons | Source List |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for record, reasons in weak:
        lines.append(
            "| {vendor} | {family} | {part} | {doctype} | {reasons} | {source} |".format(
                vendor=record.get("vendor", ""),
                family=record.get("family", ""),
                part=record.get("part_number", ""),
                doctype=record.get("document_type", ""),
                reasons="; ".join(reasons).replace("|", "\\|"),
                source=record.get("_source_file", ""),
            )
        )
    lines.extend(
        [
            "",
            "## Next Steps",
            "",
            "- Add official product/documentation URLs where missing.",
            "- Keep direct PDFs out of public release unless redistribution is confirmed.",
            "- Promote rows only after source, revision, and license review.",
        ]
    )
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="*", default=["06_DATASHEETS/00_INDEX/source_lists"])
    parser.add_argument("--output", default="05_OUTPUTS/datasheet_research/missing_datasheet_report.md")
    parser.add_argument("--download", action="store_true", help="Reserved for future use. Currently disabled.")
    args = parser.parse_args()

    if args.download:
        print("--download is disabled. This script only reports missing metadata.", file=sys.stderr)
        return 2

    records = read_records(discover_inputs(args.inputs))
    write_report(records, Path(args.output))
    print(f"Wrote {args.output} for {len(records)} records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
