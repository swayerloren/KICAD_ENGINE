#!/usr/bin/env python3
"""Run all routing geometry hard-fail checks for a routing fixture."""

from __future__ import annotations

import argparse

from route_quality_common import analyze_payload_geometry, detector_result, load_json, write_result


def parse_args_markdown(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--markdown", help="Optional Markdown output path")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture_json")
    parser.add_argument("output_json")
    parse_args_markdown(parser)
    args = parser.parse_args()

    payload = load_json(args.fixture_json)
    geometry = analyze_payload_geometry(payload)
    status = "PASS" if not geometry["findings"] else "AUTO_BLOCKED_BAD_LAYOUT"
    result = detector_result(payload, "routing_geometry_quality", geometry["findings"], status=status)
    result["trace_reports"] = geometry["trace_reports"]
    result["finding_counts"] = geometry["finding_counts"]
    write_result(args.output_json, result, args.markdown, "Routing Geometry Quality")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
