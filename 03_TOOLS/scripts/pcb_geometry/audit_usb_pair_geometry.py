#!/usr/bin/env python3
"""Audit routed USB pair geometry for angle, zigzag, and detour problems."""

from __future__ import annotations

import argparse
from pathlib import Path

from _pcb_geometry_common import audit_result, load_payload, write_json_and_markdown, usb_pair_findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tracks_json", help="Input geometry JSON path")
    parser.add_argument("output_json", help="Output audit JSON path")
    parser.add_argument("--markdown", help="Optional Markdown output path")
    args = parser.parse_args()

    payload = load_payload(args.tracks_json)
    result = audit_result(payload, "audit_usb_pair_geometry", usb_pair_findings(payload), "USB_PAIR_GEOMETRY")
    result["summary"]["usb_path_count"] = sum(1 for item in payload.get("traces", []) if item.get("usb", False))
    write_json_and_markdown(args.output_json, result, args.markdown, "USB Pair Geometry Audit")

    print(f"USB_PAIR_AUDIT_STATUS: {result['status']}")
    print(f"USB_PAIR_FINDING_COUNT: {result.get('summary', {}).get('finding_count', 0)}")
    print(f"USB_PAIR_OUTPUT_JSON: {Path(args.output_json).resolve()}")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
