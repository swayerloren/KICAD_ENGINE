#!/usr/bin/env python3
"""Run the full enforceable read-only PCB quality gate."""

from __future__ import annotations

import argparse
from pathlib import Path

from _pcb_quality_common import PASS_FINAL_ROUTING, build_context, build_gate_result, default_output_dir, evaluate_all_checks, gate_markdown, write_json, write_markdown


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, help="Active project path or .kicad_pcb path.")
    parser.add_argument("--config", help="Optional constraints file path.")
    parser.add_argument("--output-dir", help="Optional output directory.")
    parser.add_argument("--no-fail", action="store_true", help="Always return 0 after writing outputs.")
    args = parser.parse_args()

    project_path = Path(args.project).resolve() if Path(args.project).is_absolute() else None
    context = build_context(args.project, config_path=args.config)
    output_dir = Path(args.output_dir).resolve() if args.output_dir else default_output_dir(context["project"])
    output_dir.mkdir(parents=True, exist_ok=True)
    context["drc_report_path"] = output_dir / "pcb_quality_drc.rpt"

    checks = evaluate_all_checks(context)
    for stem, result in checks.items():
        write_json(output_dir / f"{stem}.json", result)
        write_markdown(output_dir / f"{stem}.md", f"# {stem}\n\n```json\n{__import__('json').dumps(result, indent=2)}\n```\n")

    gate = build_gate_result(context, checks)
    gate_json = output_dir / "pcb_quality_gate_result.json"
    gate_md = output_dir / "PCB_QUALITY_GATE_REPORT.md"
    write_json(gate_json, gate)
    write_markdown(gate_md, gate_markdown(gate))

    print(f"PCB_QUALITY_GATE_STATUS: {gate['status']}")
    print(f"PCB_QUALITY_GATE_JSON: {gate_json.resolve()}")
    print(f"PCB_QUALITY_GATE_MD: {gate_md.resolve()}")
    return 0 if args.no_fail or gate["status"] == PASS_FINAL_ROUTING else 1


if __name__ == "__main__":
    raise SystemExit(main())
