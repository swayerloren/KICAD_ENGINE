#!/usr/bin/env python3
"""Run the routing engine on a copied real KiCad PCB in read-only mode."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from _routing_common import dump_json, dump_markdown, load_json, make_markdown, markdown_table


def run_python(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, text=True, capture_output=True)


def run_checked(command: list[str]) -> dict[str, Any]:
    completed = run_python(command)
    return {
        "command": command,
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def parse_drc_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    violations = payload.get("violations", [])
    errors = [item for item in violations if str(item.get("severity", "")).lower() == "error"]
    warnings = [item for item in violations if str(item.get("severity", "")).lower() == "warning"]
    unconnected = payload.get("unconnected_items", [])
    risk = "LOW"
    if errors or unconnected:
        risk = "HIGH"
    elif warnings:
        risk = "MEDIUM"
    return {
        "risk": risk,
        "violation_count": len(violations),
        "error_count": len(errors),
        "warning_count": len(warnings),
        "unconnected_count": len(unconnected),
        "raw": payload,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pcb_file", help="Input copied .kicad_pcb file")
    parser.add_argument("output_root", help="Output directory root")
    parser.add_argument("--report-json", help="Optional summary JSON path")
    parser.add_argument("--report-markdown", help="Optional summary Markdown path")
    args = parser.parse_args()

    pcb_file = Path(args.pcb_file).resolve()
    output_root = Path(args.output_root).resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    script_dir = Path(__file__).resolve().parent
    schema_json = output_root / "routing_schema.json"
    schema_md = output_root / "routing_schema.md"
    drc_json = output_root / "drc.json"
    plan_json = output_root / "routing_plan.json"
    plan_md = output_root / "routing_plan.md"
    critical_json = output_root / "critical_nets.json"
    critical_md = output_root / "critical_nets.md"
    unrouted_json = output_root / "unrouted.json"
    unrouted_md = output_root / "unrouted.md"
    keepout_json = output_root / "keepout_violations.json"
    keepout_md = output_root / "keepout_violations.md"
    audit_json = output_root / "trace_audit.json"
    audit_md = output_root / "trace_audit.md"
    score_json = output_root / "score.json"
    score_md = output_root / "score.md"

    steps: list[dict[str, Any]] = []
    steps.append(
        run_checked(
            [
                sys.executable,
                str(script_dir / "extract_kicad_pcb_to_routing_schema.py"),
                str(pcb_file),
                str(schema_json),
                "--markdown",
                str(schema_md),
            ]
        )
    )

    drc_result: dict[str, Any] = {
        "risk": "NOT_EXTRACTED",
        "violation_count": "NOT_EXTRACTED",
        "error_count": "NOT_EXTRACTED",
        "warning_count": "NOT_EXTRACTED",
        "unconnected_count": "NOT_EXTRACTED",
    }
    drc = subprocess.run(
        [
            "kicad-cli",
            "pcb",
            "drc",
            "--format",
            "json",
            "--severity-all",
            "--output",
            str(drc_json),
            str(pcb_file),
        ],
        text=True,
        capture_output=True,
    )
    steps.append({"command": drc.args, "returncode": drc.returncode, "stdout": drc.stdout, "stderr": drc.stderr})
    if drc_json.exists():
        drc_result = parse_drc_json(drc_json)
        schema = load_json(schema_json)
        schema["routing_status"]["drc_risk"] = drc_result["risk"]
        schema["routing_status"]["drc_violation_count"] = drc_result["violation_count"]
        schema["routing_status"]["drc_unconnected_count"] = drc_result["unconnected_count"]
        dump_json(schema_json, schema)

    for command in (
        [sys.executable, str(script_dir / "generate_routing_plan.py"), str(schema_json), str(plan_json), "--markdown", str(plan_md)],
        [sys.executable, str(script_dir / "route_critical_nets_plan.py"), str(plan_json), str(critical_json), "--markdown", str(critical_md)],
        [sys.executable, str(script_dir / "detect_unrouted_nets.py"), str(schema_json), str(unrouted_json), "--markdown", str(unrouted_md)],
        [sys.executable, str(script_dir / "detect_trace_keepout_violations.py"), str(schema_json), str(keepout_json), "--markdown", str(keepout_md)],
        [sys.executable, str(script_dir / "trace_by_trace_audit.py"), str(schema_json), str(audit_json), "--markdown", str(audit_md)],
        [
            sys.executable,
            str(script_dir / "score_routing_plan.py"),
            str(schema_json),
            str(plan_json),
            str(critical_json),
            str(unrouted_json),
            str(keepout_json),
            str(audit_json),
            str(score_json),
            "--markdown",
            str(score_md),
        ],
    ):
        steps.append(run_checked(command))

    schema = load_json(schema_json)
    score = load_json(score_json) if score_json.exists() else {"status": "AUTO_BLOCKED_MISSING_DATA", "blocked_reasons": ["score output missing"], "readiness": {"ready_for_real_kicad_test": False, "exact_blockers": ["score output missing"]}}
    summary = {
        "schema_version": "1.0",
        "tool": "run_real_board_routing_audit",
        "project": schema.get("project", pcb_file.stem),
        "status": score.get("status", "AUTO_BLOCKED_MISSING_DATA"),
        "summary": {
            "board_path": str(pcb_file),
            "component_count": len(schema.get("components", [])),
            "net_count": len(schema.get("nets", [])),
            "track_count": len(schema.get("tracks", [])),
            "via_count": len(schema.get("vias", [])),
            "zone_count": len(schema.get("zones", [])),
            "keepout_count": len(schema.get("keepouts", [])),
            "drc_risk": drc_result["risk"],
            "drc_violation_count": drc_result["violation_count"],
        },
        "readiness": {
            "ready_for_copied_board_live_test": schema_json.exists() and plan_json.exists() and audit_json.exists() and score_json.exists(),
            "ready_for_active_project_routing": False,
            "exact_blockers": score.get("readiness", {}).get("exact_blockers", []),
        },
        "drc": drc_result,
        "steps": steps,
        "not_extracted": schema.get("not_extracted", []),
    }

    if args.report_json:
        dump_json(args.report_json, summary)
    if args.report_markdown:
        rows = [[Path(step["command"][1]).name if isinstance(step.get("command"), list) and len(step["command"]) > 1 else str(step.get("command")), step["returncode"]] for step in steps]
        text = make_markdown(
            "Real Board Routing Audit",
            {
                "project": summary["project"],
                "status": summary["status"],
                "ready_for_copied_board_live_test": summary["readiness"]["ready_for_copied_board_live_test"],
                "ready_for_active_project_routing": summary["readiness"]["ready_for_active_project_routing"],
            },
            [
                ("Pipeline Steps", markdown_table(["step", "returncode"], rows)),
                ("DRC", markdown_table([ "risk", "violations", "errors", "warnings", "unconnected"], [[drc_result["risk"], drc_result["violation_count"], drc_result["error_count"], drc_result["warning_count"], drc_result["unconnected_count"]]])),
                ("Not Extracted", "\n".join(f"- {item}" for item in summary["not_extracted"]) if summary["not_extracted"] else "_none_"),
                ("Blockers", "\n".join(f"- {item}" for item in summary["readiness"]["exact_blockers"]) if summary["readiness"]["exact_blockers"] else "_none_"),
            ],
        )
        dump_markdown(args.report_markdown, text)

    return 0 if summary["readiness"]["ready_for_copied_board_live_test"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
