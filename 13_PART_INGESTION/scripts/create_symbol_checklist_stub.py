#!/usr/bin/env python3
"""Create a symbol requirements checklist stub for a new part."""

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
    part = optional(args.part_number)
    return f"""# Symbol Checklist: {part}

Status: UNVERIFIED_SYMBOL

Generated: {date.today().isoformat()}

## Source

- Vendor: {optional(args.vendor)}
- Part number: {part}
- Package: {optional(args.package)}
- Datasheet URL: {optional(args.datasheet_url)}
- Local datasheet path: {optional(args.datasheet_local_path)}
- Pin table source: {UNKNOWN}

## Pinout To Extract

- Pin count: {UNKNOWN}
- Pin numbers: {UNKNOWN}
- Pin names: {UNKNOWN}
- Pin functions: {UNKNOWN}
- Electrical types: {UNKNOWN}
- Power pins: {UNKNOWN}
- Ground pins: {UNKNOWN}
- No-connect pins: {UNKNOWN}
- Exposed pad pins: {UNKNOWN}
- Reset, boot, programming, clock pins: {UNKNOWN}
- Interface pins: {UNKNOWN}

## KiCad Symbol Candidate Review

- Candidate symbol: {UNKNOWN}
- All source pins present: Not reviewed
- All symbol pins in source: Not reviewed
- Power pins visible or intentionally hidden: Not reviewed
- Multi-unit behavior reviewed: Not reviewed
- Datasheet/source field added: Not reviewed

## AI Warnings

- Do not create or approve a symbol from memory.
- Do not use a pinout from a different package or module.
- Keep status `UNVERIFIED_SYMBOL` until every pin is source-checked.

## Related Standards

- `11_LIBRARY_FACTORY/symbols/SYMBOL_QA_CHECKLIST.md`
- `11_LIBRARY_FACTORY/symbols/SYMBOL_CREATION_STANDARD.md`
- `13_PART_INGESTION/SYMBOL_REQUIREMENTS_EXTRACTION.md`
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a symbol checklist stub.")
    parser.add_argument("--part-number")
    parser.add_argument("--vendor")
    parser.add_argument("--package")
    parser.add_argument("--datasheet-url")
    parser.add_argument("--datasheet-local-path")
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{clean_token(args.part_number)}_SYMBOL_CHECKLIST.md"
    output_path.write_text(build_markdown(args), encoding="utf-8")
    print(json.dumps({"markdown": str(output_path), "status": "UNVERIFIED_SYMBOL"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

