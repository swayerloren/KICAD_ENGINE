#!/usr/bin/env python3
"""Detect unnecessary zigzags and detours."""

from __future__ import annotations

import argparse

from route_quality_common import (
    CRITICAL_LOOP_DETOUR_FOUND,
    UNNECESSARY_ZIGZAG_FOUND,
    detector_findings,
    detector_result,
    load_json,
    write_result,
)


def parse_args_markdown(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--markdown", help="Optional Markdown output path")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture_json")
    parser.add_argument("output_json")
    parse_args_markdown(parser)
    args = parser.parse_args()

    payload = load_json(args.fixture_json)
    findings = detector_findings(payload, "unnecessary_zigzags") + detector_findings(payload, "critical_detours")
    statuses = {item["status"] for item in findings}
    if not findings:
        status = "PASS"
    elif UNNECESSARY_ZIGZAG_FOUND in statuses:
        status = UNNECESSARY_ZIGZAG_FOUND
    else:
        status = CRITICAL_LOOP_DETOUR_FOUND
    result = detector_result(payload, "detect_unnecessary_zigzags", findings, status=status)
    write_result(args.output_json, result, args.markdown, "Unnecessary Zigzag Detection")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
