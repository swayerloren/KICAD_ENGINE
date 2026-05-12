#!/usr/bin/env python3
"""Check KiCad DRC and schematic-parity status for a PCB."""

from __future__ import annotations

import argparse
from pathlib import Path

from _pcb_quality_common import PASS, build_context, evaluate_pcb_drc, result_to_markdown, write_json, write_markdown


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, help="Active project path or .kicad_pcb path.")
    parser.add_argument("--config", help="Optional constraints file path.")
    parser.add_argument("--drc-report", help="Optional output .rpt path for the live DRC/parity run.")
    parser.add_argument("--output-json", help="Optional JSON output path.")
    parser.add_argument("--markdown", help="Optional Markdown output path.")
    parser.add_argument("--no-fail", action="store_true", help="Always return 0 after writing outputs.")
    args = parser.parse_args()

    context = build_context(args.project, config_path=args.config, drc_report_path=args.drc_report)
    result = evaluate_pcb_drc(context)
    if args.output_json:
        write_json(args.output_json, result)
    if args.markdown:
        write_markdown(args.markdown, result_to_markdown("PCB DRC Check", result))
    print(f"PCB_DRC_CHECK_STATUS: {result['status']}")
    print(f"PCB_DRC_CHECK_SUMMARY: {result['summary']}")
    return 0 if args.no_fail or result["status"] == PASS else 1


if __name__ == "__main__":
    raise SystemExit(main())
