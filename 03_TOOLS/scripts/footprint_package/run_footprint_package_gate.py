#!/usr/bin/env python3
"""Run the combined footprint/package gate in read-only mode."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

from audit_blank_footprints import run_audit as run_blank_audit
from audit_footprint_lock import run_audit as run_lock_audit
from audit_high_risk_footprints import run_audit as run_high_risk_audit
from extract_physical_symbols import markdown_report as extract_markdown
from extract_physical_symbols import run_extract
from footprint_package_common import (
    CHECK_STATUS_FAIL,
    CHECK_STATUS_NEEDS_HUMAN_REVIEW,
    CHECK_STATUS_PASS,
    CHECK_STATUS_WARN,
    DEFAULT_PARTS_LIST_NAME,
    DEFAULT_REVIEW_LIST_NAME,
    audit_markdown,
    default_output_dir,
    locate_lock_file,
    read_lock_rows,
    resolve_project_and_schematic,
    support_file_paths,
)
from generate_footprint_assignment_plan import markdown_report as plan_markdown


def summarize_gate_status(statuses: list[str]) -> str:
    if CHECK_STATUS_FAIL in statuses:
        return CHECK_STATUS_FAIL
    if CHECK_STATUS_NEEDS_HUMAN_REVIEW in statuses:
        return CHECK_STATUS_NEEDS_HUMAN_REVIEW
    if CHECK_STATUS_WARN in statuses:
        return CHECK_STATUS_WARN
    return CHECK_STATUS_PASS


def gate_markdown(result: dict) -> str:
    lines = [
        "# Footprint Package Gate Report",
        "",
        f"Gate status: `{result['gate_status']}`",
        "",
        f"Generated: `{result['generated_at']}`",
        f"Project: `{result['project']}`",
        f"Schematic: `{result['schematic']}`",
        "",
        "## Counts",
        "",
        f"- Physical symbols: {result['physical_symbol_count']}",
        f"- Blank footprints: {result['blank_footprint_count']}",
        f"- High-risk symbols: {result['high_risk_symbol_count']}",
        f"- Lock file present: `{result['lock_file_present']}`",
        f"- Parts list present: `{result['parts_list_present']}`",
        f"- Review list present: `{result['review_list_present']}`",
        "",
        "## Blocking Findings",
        "",
        "| Status | Code | Reference | Message | Evidence |",
        "| --- | --- | --- | --- | --- |",
    ]
    for finding in result["blocking_findings"]:
        lines.append(
            "| `{status}` | `{code}` | `{reference}` | {message} | `{evidence}` |".format(
                status=finding["status"],
                code=finding["code"],
                reference=finding.get("reference", ""),
                message=str(finding["message"]).replace("|", "\\|"),
                evidence=str(finding.get("evidence", "")).replace("|", "\\|"),
            )
        )
    lines.extend(
        [
            "",
            "## Output Files",
            "",
        ]
    )
    for key, path in sorted(result["outputs"].items()):
        lines.append(f"- `{key}`: `{path}`")
    lines.extend(
        [
            "",
            "## Gate Rule",
            "",
            "- Do not update PCB from schematic unless this gate is exactly `PASS`.",
            "- Blank footprints, missing lock rows, and unreviewed high-risk parts are hard blockers.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the combined footprint/package gate in read-only mode.")
    parser.add_argument("--project", required=True, help="Active project root.")
    parser.add_argument("--output-dir", default="", help="Optional output directory.")
    parser.add_argument("--lock-file", default="", help="Optional explicit lock-file path.")
    parser.add_argument("--no-fail", action="store_true", help="Return exit code 0 even when the gate fails.")
    args = parser.parse_args()

    project_root, schematic = resolve_project_and_schematic(args.project, "")
    if project_root is None:
        raise SystemExit("--project is required for the combined footprint/package gate.")
    output_dir = Path(args.output_dir).resolve() if args.output_dir else default_output_dir(project_root, schematic)
    output_dir.mkdir(parents=True, exist_ok=True)

    extract_result = run_extract(schematic)
    blank_result = run_blank_audit(schematic)
    lock_result = run_lock_audit(schematic, project_root, args.lock_file)
    high_risk_result = run_high_risk_audit(schematic, project_root, args.lock_file)

    extract_json = output_dir / "physical_symbols.json"
    extract_md = output_dir / "physical_symbols.md"
    extract_json.write_text(json.dumps(extract_result, indent=2, sort_keys=True), encoding="utf-8")
    extract_md.write_text(extract_markdown(extract_result), encoding="utf-8")

    audit_payloads = {
        "blank_footprints": blank_result,
        "footprint_lock": lock_result,
        "high_risk_footprints": high_risk_result,
    }

    outputs = {
        "physical_symbols_json": str(extract_json),
        "physical_symbols_md": str(extract_md),
    }
    for name, payload in audit_payloads.items():
        json_path = output_dir / f"{name}.json"
        md_path = output_dir / f"{name}.md"
        json_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
        md_path.write_text(audit_markdown(payload), encoding="utf-8")
        outputs[f"{name}_json"] = str(json_path)
        outputs[f"{name}_md"] = str(md_path)

    plan_json = output_dir / "footprint_assignment_plan.json"
    plan_md = output_dir / "footprint_assignment_plan.md"
    lock_path = locate_lock_file(project_root, args.lock_file)
    _, row_index = read_lock_rows(lock_path)
    plan_result = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "schematic": str(schematic),
        "physical_symbol_count": extract_result["physical_symbol_count"],
        "lock_file": str(lock_path) if lock_path else "",
        "lock_file_present": bool(lock_path and lock_path.exists()),
        "assignments": [
            {
                "reference": symbol["reference"],
                "value": symbol["value"],
                "manufacturer_part_number": row_index.get(symbol["reference"].upper(), {}).get("manufacturer_part_number", ""),
                "kicad_symbol": symbol["lib_id"],
                "kicad_footprint": symbol["footprint"],
                "package": row_index.get(symbol["reference"].upper(), {}).get("package", ""),
                "risk": symbol["risk"],
                "high_risk": bool(symbol["high_risk"]),
                "risk_reason": symbol["risk_reason"],
                "category": symbol["category"],
                "recommended_action": (
                    "Assign a footprint, then create a lock-file row with source and package proof."
                    if not str(symbol.get("footprint", "")).strip()
                    else "Complete the lock-file evidence and required review fields."
                ),
                "notes": row_index.get(symbol["reference"].upper(), {}).get("notes", ""),
            }
            for symbol in extract_result["symbols"]
        ],
    }
    plan_json.write_text(json.dumps(plan_result, indent=2, sort_keys=True), encoding="utf-8")
    plan_md.write_text(plan_markdown(plan_result), encoding="utf-8")
    outputs["footprint_assignment_plan_json"] = str(plan_json)
    outputs["footprint_assignment_plan_md"] = str(plan_md)

    support_paths = support_file_paths(project_root)
    parts_list_path = Path(support_paths["parts_list"])
    review_list_path = Path(support_paths["needs_review_list"])

    blocking_findings = []
    for payload in (blank_result, lock_result, high_risk_result):
        for finding in payload["findings"]:
            if finding["status"] in {CHECK_STATUS_FAIL, CHECK_STATUS_NEEDS_HUMAN_REVIEW}:
                blocking_findings.append(finding)

    gate_status = summarize_gate_status(
        [
            blank_result["summary"]["status"],
            lock_result["summary"]["status"],
            high_risk_result["summary"]["status"],
        ]
    )

    if not parts_list_path.exists():
        blocking_findings.append(
            {
                "status": CHECK_STATUS_WARN,
                "code": "PARTS_LIST_MISSING",
                "reference": "",
                "message": f"{DEFAULT_PARTS_LIST_NAME} is missing.",
                "evidence": str(parts_list_path),
            }
        )
    if not review_list_path.exists():
        blocking_findings.append(
            {
                "status": CHECK_STATUS_WARN,
                "code": "REVIEW_LIST_MISSING",
                "reference": "",
                "message": f"{DEFAULT_REVIEW_LIST_NAME} is missing.",
                "evidence": str(review_list_path),
            }
        )

    result = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "project": str(project_root),
        "schematic": str(schematic),
        "gate_status": gate_status,
        "physical_symbol_count": extract_result["physical_symbol_count"],
        "blank_footprint_count": blank_result.get("blank_footprint_count", 0),
        "lock_file_present": bool(lock_path and lock_path.exists()),
        "parts_list_present": parts_list_path.exists(),
        "review_list_present": review_list_path.exists(),
        "high_risk_symbol_count": high_risk_result.get("high_risk_symbol_count", 0),
        "blocking_findings": blocking_findings,
        "outputs": outputs,
    }

    gate_json = output_dir / "footprint_gate_result.json"
    gate_md = output_dir / "FOOTPRINT_PACKAGE_GATE_REPORT.md"
    gate_json.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    gate_md.write_text(gate_markdown(result), encoding="utf-8")
    print(str(gate_json))

    if args.no_fail:
        return 0
    return 0 if gate_status == CHECK_STATUS_PASS else 1


if __name__ == "__main__":
    raise SystemExit(main())
