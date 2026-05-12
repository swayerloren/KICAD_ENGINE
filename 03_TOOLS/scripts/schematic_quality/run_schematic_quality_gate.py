#!/usr/bin/env python3
"""Run the schematic quality gate in read-only mode."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

from audit_schematic_annotation import run_audit as run_annotation_audit
from audit_schematic_block_layout import run_audit as run_block_layout_audit
from audit_schematic_footprints import run_audit as run_footprint_audit
from audit_schematic_text_overlaps import run_audit as run_text_overlap_audit
from audit_wire_vs_label_balance import run_audit as run_wire_label_audit
from extract_schematic_symbols import run_extract
from generate_schematic_quality_report import markdown_report
from schematic_quality_common import (
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    CHECK_STATUS_WARN,
    audit_markdown,
    check_record,
    default_output_dir,
    detect_closeup_visual_status,
    detect_native_annotation_status,
    exit_code_for,
    find_project_schematic,
    run_erc,
)


def summarize_gate_status(statuses: list[str]) -> str:
    if CHECK_STATUS_FAIL in statuses:
        return CHECK_STATUS_FAIL
    if CHECK_STATUS_WARN in statuses:
        return CHECK_STATUS_WARN
    return CHECK_STATUS_PASS


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the read-only schematic quality gate.")
    parser.add_argument("--project", required=True, help="Active project root.")
    parser.add_argument("--output-dir", default="", help="Optional output directory.")
    parser.add_argument("--no-fail", action="store_true", help="Return exit code 0 even when the gate fails.")
    args = parser.parse_args()

    project_root = Path(args.project)
    schematic = find_project_schematic(project_root)
    output_dir = Path(args.output_dir) if args.output_dir else default_output_dir(project_root)
    output_dir.mkdir(parents=True, exist_ok=True)

    extract_result = run_extract(schematic)
    annotation_result = run_annotation_audit(schematic)
    footprint_result = run_footprint_audit(schematic)
    overlap_result = run_text_overlap_audit(schematic)
    block_result = run_block_layout_audit(schematic)
    wire_result = run_wire_label_audit(schematic)

    audit_results = {
        "symbols": extract_result,
        "annotation": annotation_result,
        "footprints": footprint_result,
        "text_overlaps": overlap_result,
        "block_layout": block_result,
        "wire_vs_label": wire_result,
    }

    output_files: dict[str, str] = {}
    for audit_name, audit_result in audit_results.items():
        json_path = output_dir / f"{audit_name}.json"
        md_path = output_dir / f"{audit_name}.md"
        json_path.write_text(json.dumps(audit_result, indent=2, sort_keys=True), encoding="utf-8")
        md_path.write_text(audit_markdown(audit_result), encoding="utf-8")
        output_files[f"{audit_name}_json"] = str(json_path)
        output_files[f"{audit_name}_md"] = str(md_path)

    erc_path = output_dir / "erc_report.raw.txt"
    erc_result = run_erc(schematic, erc_path)
    native_annotation = detect_native_annotation_status(project_root)
    human_visual = detect_closeup_visual_status(project_root)

    gate_findings = [
        check_record(native_annotation["status"], "NATIVE_ANNOTATION_PROOF", native_annotation["message"], "", native_annotation["evidence"]),
        check_record(erc_result["status"], "ERC_PROOF", erc_result["message"], "", erc_result["evidence"]),
        check_record(human_visual["status"], "HUMAN_VISUAL_PROOF", human_visual["message"], "", human_visual["evidence"]),
    ]

    readability_status = summarize_gate_status(
        [
            block_result["summary"]["status"],
            overlap_result["summary"]["status"],
            wire_result["summary"]["status"],
            human_visual["status"],
        ]
    )
    gate_status = summarize_gate_status(
        [
            annotation_result["summary"]["status"],
            footprint_result["summary"]["status"],
            block_result["summary"]["status"],
            overlap_result["summary"]["status"],
            wire_result["summary"]["status"],
            native_annotation["status"],
            erc_result["status"],
            human_visual["status"],
        ]
    )

    combined = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "project": str(project_root),
        "schematic": str(schematic),
        "gate_status": gate_status,
        "readability_status": readability_status,
        "native_annotation": native_annotation,
        "erc": erc_result,
        "human_visual": human_visual,
        "audits": audit_results,
        "gate_findings": gate_findings,
        "output_files": output_files | {"erc_report": str(erc_path)},
    }

    combined_json = output_dir / "schematic_quality_report.json"
    combined_md = output_dir / "schematic_quality_report.md"
    combined_json.write_text(json.dumps(combined, indent=2, sort_keys=True), encoding="utf-8")
    combined_md.write_text(markdown_report(combined), encoding="utf-8")
    print(str(combined_json))
    return 0 if args.no_fail else (1 if gate_status == CHECK_STATUS_FAIL else 0)


if __name__ == "__main__":
    raise SystemExit(main())
