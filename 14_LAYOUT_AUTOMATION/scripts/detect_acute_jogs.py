#!/usr/bin/env python3
"""Detect acute non-45 routing jogs."""

from __future__ import annotations

import argparse

from route_quality_common import ACUTE_JOG_FOUND, detector_findings, detector_result, load_json, write_result


def parse_args_markdown(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--markdown", help="Optional Markdown output path")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture_json")
    parser.add_argument("output_json")
    parse_args_markdown(parser)
    args = parser.parse_args()

    payload = load_json(args.fixture_json)
    findings = detector_findings(payload, "acute_jogs")
    status = "PASS" if not findings else ACUTE_JOG_FOUND
    result = detector_result(payload, "detect_acute_jogs", findings, status=status)
    write_result(args.output_json, result, args.markdown, "Acute Jog Detection")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
