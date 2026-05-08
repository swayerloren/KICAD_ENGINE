#!/usr/bin/env python3
"""Create a footprint requirements checklist stub for a new part."""

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
    return f"""# Footprint Checklist: {part}

Status: UNVERIFIED_FOOTPRINT

Generated: {date.today().isoformat()}

## Source

- Vendor: {optional(args.vendor)}
- Part number: {part}
- Package: {optional(args.package)}
- Datasheet URL: {optional(args.datasheet_url)}
- Local datasheet path: {optional(args.datasheet_local_path)}
- Package drawing: {UNKNOWN}
- Land pattern: {UNKNOWN}

## Geometry To Extract

- Pad count: {UNKNOWN}
- Pad numbering: {UNKNOWN}
- Pitch: {UNKNOWN}
- Pad dimensions: {UNKNOWN}
- Drill sizes: {UNKNOWN}
- Slot dimensions: {UNKNOWN}
- Exposed pad: {UNKNOWN}
- Body outline: {UNKNOWN}
- Courtyard: {UNKNOWN}
- Fab outline: {UNKNOWN}
- Silkscreen and orientation marker: {UNKNOWN}
- Footprint origin: {UNKNOWN}
- 3D model status: {UNKNOWN}

## Pin 1 And Orientation

- Pin 1 location: {UNKNOWN}
- Board side: {UNKNOWN}
- Connector mating direction if applicable: {UNKNOWN}
- Human orientation review needed: Yes

## AI Warnings

- Do not approve this footprint until exact package or connector drawing evidence is reviewed.
- Do not use pitch, pin count, or package name alone.
- Connector footprints require exact manufacturer drawing and human review.

## Related Standards

- `11_LIBRARY_FACTORY/footprints/FOOTPRINT_QA_CHECKLIST.md`
- `11_LIBRARY_FACTORY/footprints/CONNECTOR_FOOTPRINT_RULES.md`
- `13_PART_INGESTION/FOOTPRINT_REQUIREMENTS_EXTRACTION.md`
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a footprint checklist stub.")
    parser.add_argument("--part-number")
    parser.add_argument("--vendor")
    parser.add_argument("--package")
    parser.add_argument("--datasheet-url")
    parser.add_argument("--datasheet-local-path")
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{clean_token(args.part_number)}_FOOTPRINT_CHECKLIST.md"
    output_path.write_text(build_markdown(args), encoding="utf-8")
    print(json.dumps({"markdown": str(output_path), "status": "UNVERIFIED_FOOTPRINT"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

