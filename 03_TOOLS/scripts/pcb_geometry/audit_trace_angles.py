#!/usr/bin/env python3
"""Detect right-angle and acute-angle trace geometry failures."""

from __future__ import annotations

import argparse
from pathlib import Path

from _pcb_geometry_common import audit_result, load_payload, trace_angle_findings, write_json_and_markdown


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tracks_json", help="Input geometry JSON path")
    parser.add_argument("output_json", help="Output audit JSON path")
    parser.add_argument("--markdown", help="Optional Markdown output path")
    args = parser.parse_args()

    payload = load_payload(args.tracks_json)
    result = audit_result(payload, "audit_trace_angles", trace_angle_findings(payload), "TRACE_ANGLES")
    write_json_and_markdown(args.output_json, result, args.markdown, "Trace Angle Audit")

    print(f"TRACE_ANGLE_AUDIT_STATUS: {result['status']}")
    print(f"TRACE_ANGLE_FINDING_COUNT: {result.get('summary', {}).get('finding_count', 0)}")
    print(f"TRACE_ANGLE_OUTPUT_JSON: {Path(args.output_json).resolve()}")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
