#!/usr/bin/env python3
"""Create a datasheet summary Markdown stub.

The script does not download, parse, or redistribute datasheets.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path


UNKNOWN = "Unknown - requires source verification"


def clean_token(value: str | None) -> str:
    value = (value or "UNKNOWN").strip()
    value = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_")
    return value.upper() or "UNKNOWN"


def optional(value: str | None) -> str:
    return value.strip() if value and value.strip() else UNKNOWN


def build_markdown(args: argparse.Namespace) -> str:
    vendor = optional(args.vendor)
    part_number = optional(args.part_number)
    record_id = f"{clean_token(vendor)}_{clean_token(part_number)}_DATASHEET_SUMMARY"
    today = date.today().isoformat()
    return f"""# Datasheet Summary: {part_number}

```yaml
record_type: DATASHEET_SUMMARY
record_id: {record_id}
vendor: {vendor}
part_number: {part_number}
family: {optional(args.family)}
package: {optional(args.package)}
document_type: DATASHEET
document_title: {optional(args.document_title)}
revision: {UNKNOWN}
document_date: {UNKNOWN}
source_url: {optional(args.datasheet_url)}
source_access_date: {today if args.datasheet_url else UNKNOWN}
local_filename: {UNKNOWN}
local_path: {optional(args.datasheet_local_path)}
verification_status: NOT_VERIFIED
summary_author: AI_GENERATED_STUB
summary_date: {today}
```

## Source Policy

- This is a stub generated from user-provided metadata.
- No PDF was downloaded or redistributed by this script.
- Public records may remain link-only unless redistribution rights are confirmed.

## Identification

- Exact part number: {part_number}
- Vendor: {vendor}
- Variants covered: {UNKNOWN}
- Lifecycle status: {UNKNOWN}

## Electrical

- Voltage range: {UNKNOWN}
- Current limits: {UNKNOWN}
- Absolute maximum ratings: {UNKNOWN}
- Recommended operating conditions: {UNKNOWN}
- Power budget notes: {UNKNOWN}

## Pinout And Package

- Pin count: {UNKNOWN}
- Package type: {optional(args.package)}
- Pinout notes: {UNKNOWN}
- Orientation notes: {UNKNOWN}
- Package drawing reference: {UNKNOWN}

## KiCad Links

- Related KiCad symbol: {UNKNOWN}
- Related KiCad footprint: {UNKNOWN}
- Related KiCad 3D model: {UNKNOWN}
- Symbol verification notes: {UNKNOWN}
- Footprint verification notes: {UNKNOWN}

## Layout And Design

- Special layout rules: {UNKNOWN}
- Decoupling notes: {UNKNOWN}
- Thermal notes: {UNKNOWN}
- RF or high-speed notes: {UNKNOWN}
- Connector orientation notes: {UNKNOWN}

## Errata And Risk

- Known errata: {UNKNOWN}
- Design risks:
  - Treating this stub as verified design data.
  - Using a symbol or footprint before source review.

## Citations

- Field: source document
  - Source location: {optional(args.datasheet_url) if args.datasheet_url else optional(args.datasheet_local_path)}
  - Note: Source pointer only; exact fields still require review.

## Review History

- {today}: Stub created by `13_PART_INGESTION/scripts/create_datasheet_summary_stub.py`.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a datasheet summary Markdown stub.")
    parser.add_argument("--part-number")
    parser.add_argument("--vendor")
    parser.add_argument("--family")
    parser.add_argument("--package")
    parser.add_argument("--document-title")
    parser.add_argument("--datasheet-url")
    parser.add_argument("--datasheet-local-path")
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = clean_token(args.part_number)
    output_path = output_dir / f"{stem}_DATASHEET_SUMMARY.md"
    output_path.write_text(build_markdown(args), encoding="utf-8")
    print(json.dumps({"markdown": str(output_path), "status": "NOT_VERIFIED"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

