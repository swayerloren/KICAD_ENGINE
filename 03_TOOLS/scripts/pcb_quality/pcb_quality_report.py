#!/usr/bin/env python3
"""Render a Markdown PCB quality report from a saved gate JSON result."""

from __future__ import annotations

import argparse

from _pcb_quality_common import gate_markdown, load_json, write_markdown


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gate-json", required=True, help="Existing pcb_quality_gate_result.json path.")
    parser.add_argument("--output", required=True, help="Markdown output path.")
    args = parser.parse_args()

    payload = load_json(args.gate_json)
    write_markdown(args.output, gate_markdown(payload))
    print(f"PCB_QUALITY_REPORT_RENDERED: {args.output}")
    print(f"PCB_QUALITY_GATE_STATUS: {payload.get('status', '')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
