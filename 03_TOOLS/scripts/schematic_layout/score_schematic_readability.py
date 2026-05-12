#!/usr/bin/env python3
"""Score schematic readability without editing the schematic."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from schematic_layout_common import (
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    CHECK_STATUS_WARN,
    VISUAL_SCORE_WEIGHTS,
    common_parser,
    default_report_dir,
    ensure_report_dir,
    infer_project_root,
    load_layout_context,
    overall_status_from_scores,
    points_for_status,
    resolve_project_and_schematic,
    write_markdown_and_json,
)

from audit_local_wire_usage import run_audit as run_local_wire_audit
from audit_visual_flow import run_audit as run_visual_flow_audit
from audit_schematic_annotation import run_audit as run_annotation_audit
from audit_schematic_footprints import run_audit as run_footprint_audit
from audit_schematic_text_overlaps import run_audit as run_text_overlap_audit
from schematic_quality_common import detect_native_annotation_status, run_erc


def category_status_from_findings(result: dict[str, Any], fail_codes: set[str], warn_codes: set[str]) -> str:
    findings = result.get("findings", [])
    if any(item.get("status") == CHECK_STATUS_FAIL and item.get("code") in fail_codes for item in findings):
        return CHECK_STATUS_FAIL
    if any(item.get("status") in {CHECK_STATUS_FAIL, CHECK_STATUS_WARN} and item.get("code") in warn_codes.union(fail_codes) for item in findings):
        return CHECK_STATUS_WARN
    return CHECK_STATUS_PASS


def reference_status(reference_metrics: dict[str, Any]) -> str:
    overlap_count = int(reference_metrics.get("overlapping_reference_count", 0))
    visible_count = int(reference_metrics.get("visible_reference_count", 0))
    if visible_count == 0:
        return CHECK_STATUS_FAIL
    if overlap_count == 0:
        return CHECK_STATUS_PASS
    if overlap_count <= 2:
        return CHECK_STATUS_WARN
    return CHECK_STATUS_FAIL


def annotation_gate_status(annotation_result: dict[str, Any], native_annotation: dict[str, str]) -> str:
    annotation_status = annotation_result.get("summary", {}).get("status", CHECK_STATUS_FAIL)
    native_status = native_annotation.get("status", CHECK_STATUS_FAIL)
    if annotation_status == CHECK_STATUS_FAIL or native_status == CHECK_STATUS_FAIL:
        return CHECK_STATUS_FAIL
    if annotation_status == CHECK_STATUS_WARN or native_status == CHECK_STATUS_WARN:
        return CHECK_STATUS_WARN
    return CHECK_STATUS_PASS


def block_grouping_status(visual_flow_result: dict[str, Any]) -> str:
    return category_status_from_findings(
        visual_flow_result,
        fail_codes={"BLOCK_MISSING", "POWER_FLOW_DISORDERED", "BUCK_TOO_FAR_FROM_INPUT", "RESET_BOOT_TOO_FAR", "SYMBOL_EXPLOSION"},
        warn_codes={"BLOCK_REGION_OFF_TEMPLATE", "BUCK_NEAR_INPUT_WARN", "RESET_BOOT_NEAR_ESP32_WARN", "UNASSIGNED_SYMBOLS_WARN"},
    )


def power_flow_status(visual_flow_result: dict[str, Any]) -> str:
    return category_status_from_findings(
        visual_flow_result,
        fail_codes={"POWER_FLOW_DISORDERED", "BUCK_TOO_FAR_FROM_INPUT"},
        warn_codes={"BLOCK_REGION_OFF_TEMPLATE", "BUCK_NEAR_INPUT_WARN"},
    )


def label_balance_status(local_wire_result: dict[str, Any]) -> str:
    return category_status_from_findings(
        local_wire_result,
        fail_codes={"LOCAL_BLOCK_HAS_LABELS_BUT_NO_WIRES", "LOCAL_BLOCK_TOO_LABEL_HEAVY"},
        warn_codes={"PIN_LABEL_OVERUSE", "REPEATED_LOCAL_NET_LABELS"},
    )


def overlap_status(overlap_result: dict[str, Any], reference_metrics: dict[str, Any]) -> str:
    overlap_fail = overlap_result.get("summary", {}).get("status", CHECK_STATUS_FAIL)
    ref_status = reference_status(reference_metrics)
    if CHECK_STATUS_FAIL in {overlap_fail, ref_status}:
        return CHECK_STATUS_FAIL
    if CHECK_STATUS_WARN in {overlap_fail, ref_status}:
        return CHECK_STATUS_WARN
    return CHECK_STATUS_PASS


def build_result(project_root: Path | None, schematic: Path, report_dir: Path) -> dict[str, Any]:
    context = load_layout_context(schematic)
    visual_flow_result = run_visual_flow_audit(schematic)
    local_wire_result = run_local_wire_audit(schematic)
    annotation_result = run_annotation_audit(schematic)
    footprint_result = run_footprint_audit(schematic)
    overlap_result = run_text_overlap_audit(schematic)
    native_annotation = detect_native_annotation_status(project_root) if project_root else {
        "status": CHECK_STATUS_WARN,
        "message": "Project-root native annotation evidence is unavailable for schematic-only mode.",
        "evidence": "",
    }
    erc_path = report_dir / "erc_report.raw.txt"
    erc_result = run_erc(schematic, erc_path)

    category_statuses = {
        "block_grouping": block_grouping_status(visual_flow_result),
        "local_wire_clarity": local_wire_result["status"],
        "label_usage_balance": label_balance_status(local_wire_result),
        "overlap_count": overlap_status(overlap_result, context["reference_metrics"]),
        "reference_readability": reference_status(context["reference_metrics"]),
        "power_flow_readability": power_flow_status(visual_flow_result),
        "usb_path_readability": context["usb_metrics"]["status"],
        "esp32_pin_readability": context["esp32_metrics"]["status"],
        "erc_status": erc_result["status"],
        "annotation_status": annotation_gate_status(annotation_result, native_annotation),
        "footprint_status": footprint_result.get("summary", {}).get("status", CHECK_STATUS_FAIL),
    }

    categories: dict[str, Any] = {}
    total = 0.0
    for category, weight in VISUAL_SCORE_WEIGHTS.items():
        status = category_statuses[category]
        earned = points_for_status(status, weight)
        total += earned
        categories[category] = {
            "weight": weight,
            "status": status,
            "points_earned": earned,
        }

    total_score = int(round(total))
    overall_status = overall_status_from_scores(category_statuses, total_score)
    return {
        "generated_at": context["generated_at"],
        "project": str(project_root) if project_root else "",
        "schematic": str(schematic),
        "report_dir": str(report_dir),
        "scorecard_id": "schematic_readability_score",
        "overall_status": overall_status,
        "total_score": total_score,
        "pass_threshold": 85,
        "warn_threshold": 70,
        "categories": categories,
        "context": {
            "template_id": context["template_id"],
            "diagram_bbox": context["diagram_bbox"],
            "reference_metrics": context["reference_metrics"],
            "esp32_metrics": context["esp32_metrics"],
            "usb_metrics": context["usb_metrics"],
        },
        "evidence": {
            "visual_flow_status": visual_flow_result["status"],
            "local_wire_usage_status": local_wire_result["status"],
            "annotation_audit_status": annotation_result.get("summary", {}).get("status", CHECK_STATUS_FAIL),
            "footprint_audit_status": footprint_result.get("summary", {}).get("status", CHECK_STATUS_FAIL),
            "text_overlap_status": overlap_result.get("summary", {}).get("status", CHECK_STATUS_FAIL),
            "native_annotation_status": native_annotation["status"],
            "erc_status": erc_result["status"],
            "erc_report": str(erc_path),
        },
    }


def build_markdown(result: dict[str, Any]) -> str:
    lines = [
        "# Schematic Readability Score",
        "",
        f"Status: `{result['overall_status']}`",
        f"Score: `{result['total_score']}/100`",
        "",
        f"Generated: `{result['generated_at']}`",
        f"Schematic: `{result['schematic']}`",
        "",
        "## Category Scores",
        "",
        "| Category | Status | Weight | Points |",
        "| --- | --- | --- | --- |",
    ]
    for category, payload in result["categories"].items():
        label = category.replace("_", " ").title()
        lines.append(f"| {label} | `{payload['status']}` | `{payload['weight']}` | `{payload['points_earned']}` |")
    lines.extend(
        [
            "",
            "## Key Evidence",
            "",
            f"- Visual flow: `{result['evidence']['visual_flow_status']}`",
            f"- Local wire usage: `{result['evidence']['local_wire_usage_status']}`",
            f"- Annotation audit: `{result['evidence']['annotation_audit_status']}`",
            f"- Native annotation proof: `{result['evidence']['native_annotation_status']}`",
            f"- Footprint audit: `{result['evidence']['footprint_audit_status']}`",
            f"- Text overlap audit: `{result['evidence']['text_overlap_status']}`",
            f"- ERC: `{result['evidence']['erc_status']}`",
            "",
            "## Context Highlights",
            "",
            f"- USB path readability: `{result['context']['usb_metrics']['status']}`",
            f"- ESP32 pin readability: `{result['context']['esp32_metrics']['status']}`",
            f"- Overlapping references: `{result['context']['reference_metrics']['overlapping_reference_count']}`",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = common_parser("Score schematic readability without editing the schematic.")
    args = parser.parse_args()
    project_root, schematic = resolve_project_and_schematic(args.project, args.schematic)
    project_root = project_root or infer_project_root(schematic)
    report_dir = ensure_report_dir(project_root, schematic, args.report_dir)
    report_dir.mkdir(parents=True, exist_ok=True)
    result = build_result(project_root, schematic, report_dir)
    output = Path(args.output) if args.output else report_dir / "schematic_readability_score.md"
    json_output = Path(args.json_output) if args.json_output else report_dir / "schematic_readability_score.json"
    write_markdown_and_json(build_markdown(result), result, output, json_output)
    print(str(json_output))
    return 0 if args.no_fail or result["overall_status"] != CHECK_STATUS_FAIL else 1


if __name__ == "__main__":
    raise SystemExit(main())
