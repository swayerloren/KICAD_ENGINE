#!/usr/bin/env python3
"""Extract routed track geometry from a real KiCad PCB in read-only mode."""

from __future__ import annotations

import argparse
from pathlib import Path

from _pcb_geometry_common import build_geometry_payload, extraction_markdown, write_json_and_markdown


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--project", help="Active project directory")
    group.add_argument("--pcb", help="Direct .kicad_pcb path")
    parser.add_argument("--output-json", required=True, help="Output geometry JSON path")
    parser.add_argument("--markdown", help="Optional Markdown output path")
    args = parser.parse_args()

    target = args.project or args.pcb
    payload = build_geometry_payload(str(target))
    write_json_and_markdown(args.output_json, payload, args.markdown, "PCB Geometry Track Extraction", extraction_markdown(payload))

    print("TRACK_EXTRACTION_STATUS: PASS")
    print(f"TRACK_PATH_COUNT: {payload.get('summary', {}).get('path_count', 0)}")
    print(f"TRACK_OUTPUT_JSON: {Path(args.output_json).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
