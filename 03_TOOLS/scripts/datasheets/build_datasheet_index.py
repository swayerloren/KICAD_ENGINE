#!/usr/bin/env python3
"""Build a markdown datasheet source index from CSV/JSON source lists."""

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


def write_index(records: List[Dict[str, str]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    sorted_records = sorted(records, key=lambda r: (r["vendor"], r["family"], r["part_number"], r["document_type"]))
    lines = [
        "# Datasheet Source Index",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "This index is generated from source-list CSV/JSON files. It is metadata only and does not prove document verification.",
        "",
        "| Vendor | Family | Part / Topic | Document Type | Title | Source URL | Target Folder | Redistribution | Notes | Source List |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for record in sorted_records:
        lines.append(
            "| {vendor} | {family} | {part} | {doctype} | {title} | {url} | {folder} | {redistribution} | {notes} | {source} |".format(
                vendor=record["vendor"],
                family=record["family"],
                part=record["part_number"],
                doctype=record["document_type"],
                title=record["title"],
                url=record["source_url"],
                folder=record["local_target_folder"],
                redistribution=record["public_redistribution_status"],
                notes=record["notes"].replace("|", "\\|"),
                source=record["_source_file"],
            )
        )
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="*", default=["06_DATASHEETS/00_INDEX/source_lists"])
    parser.add_argument("--output", default="05_OUTPUTS/datasheet_research/datasheet_source_index.md")
    parser.add_argument("--download", action="store_true", help="Reserved for future use. Currently disabled.")
    args = parser.parse_args()

    if args.download:
        print("--download is disabled. This script only builds metadata indexes.", file=sys.stderr)
        return 2

    records = read_records(discover_inputs(args.inputs))
    write_index(records, Path(args.output))
    print(f"Wrote {args.output} for {len(records)} records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
