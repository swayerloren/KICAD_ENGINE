#!/usr/bin/env python3
"""Audit power-path and switching-loop geometry for detours and plane-split risk."""

from __future__ import annotations

import argparse
from pathlib import Path

from _pcb_geometry_common import audit_result, load_payload, power_loop_findings, write_json_and_markdown


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tracks_json", help="Input geometry JSON path")
    parser.add_argument("output_json", help="Output audit JSON path")
    parser.add_argument("--markdown", help="Optional Markdown output path")
    args = parser.parse_args()

    payload = load_payload(args.tracks_json)
    result = audit_result(payload, "audit_power_loop_geometry", power_loop_findings(payload), "POWER_LOOP_GEOMETRY")
    write_json_and_markdown(args.output_json, result, args.markdown, "Power Loop Geometry Audit")

    print(f"POWER_LOOP_AUDIT_STATUS: {result['status']}")
    print(f"POWER_LOOP_FINDING_COUNT: {result.get('summary', {}).get('finding_count', 0)}")
    print(f"POWER_LOOP_OUTPUT_JSON: {Path(args.output_json).resolve()}")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
