#!/usr/bin/env python3
"""Plan a cleaner functional-block layout for a KiCad schematic."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from schematic_layout_common import (
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    CHECK_STATUS_WARN,
    LAYOUT_TEMPLATE_ESP32_DEV_BOARD,
    common_parser,
    ensure_report_dir,
    infer_project_root,
    load_layout_context,
    resolve_project_and_schematic,
    serializable_blocks,
    write_markdown_and_json,
)

from audit_local_wire_usage import run_audit as run_local_wire_audit
from audit_visual_flow import run_audit as run_visual_flow_audit


REGION_TARGETS = {
    "upper_left": (0.18, 0.18),
    "upper_left_to_center": (0.32, 0.24),
    "center_or_upper_center": (0.58, 0.30),
    "lower_left_or_center": (0.32, 0.72),
    "right_or_lower_right": (0.78, 0.62),
    "lower_grouped_service_area": (0.60, 0.84),
    "separate_mechanical_area": (0.82, 0.14),
}


def target_point(diagram_bbox: dict[str, float], desired_region: str, esp32_centroid: dict[str, float] | None) -> dict[str, float]:
    if desired_region == "near_esp32" and esp32_centroid is not None:
        return {"x": round(esp32_centroid["x"] + 18.0, 2), "y": round(esp32_centroid["y"] + 12.0, 2)}
    x_ratio, y_ratio = REGION_TARGETS.get(desired_region, (0.5, 0.5))
    width = max(1.0, diagram_bbox["x2"] - diagram_bbox["x1"])
    height = max(1.0, diagram_bbox["y2"] - diagram_bbox["y1"])
    return {
        "x": round(diagram_bbox["x1"] + width * x_ratio, 2),
        "y": round(diagram_bbox["y1"] + height * y_ratio, 2),
    }


def build_plan(schematic: Path) -> dict[str, Any]:
    context = load_layout_context(schematic)
    visual_flow_result = run_visual_flow_audit(schematic)
    local_wire_result = run_local_wire_audit(schematic)
    esp32_block = context["blocks"]["esp32_module"]
    esp32_centroid = esp32_block["centroid"] if esp32_block["symbol_count"] else None
    plan_items: list[dict[str, Any]] = []

    for block_id, rules in LAYOUT_TEMPLATE_ESP32_DEV_BOARD["blocks"].items():
        block = context["blocks"][block_id]
        current_region = context["block_regions"][block_id]
        target = target_point(context["diagram_bbox"], rules["desired_region"], esp32_centroid)
        if block["symbol_count"] == 0:
            status = CHECK_STATUS_FAIL if block_id in {"input_power_protection", "buck_regulator", "esp32_module", "usb_c_data", "reset_boot"} else CHECK_STATUS_WARN
            movement = {"dx": 0.0, "dy": 0.0}
            action = "Add or clearly identify this functional block before cleanup scoring can pass."
        else:
            dx = round(target["x"] - block["centroid"]["x"], 2)
            dy = round(target["y"] - block["centroid"]["y"], 2)
            movement = {"dx": dx, "dy": dy}
            if current_region["horizontal"] in rules["allowed_horizontal"] and current_region["vertical"] in rules["allowed_vertical"]:
                status = CHECK_STATUS_PASS
                action = "Keep the block in its current region and focus on local cleanup."
            else:
                status = CHECK_STATUS_WARN
                action = "Move this block toward the template target region before final visual cleanup."
        plan_items.append(
            {
                "block_id": block_id,
                "title": block["title"],
                "status": status,
                "desired_region": rules["desired_region"],
                "current_region": current_region["region"],
                "target_centroid": target,
                "movement_delta_mm": movement,
                "references": [symbol.get("reference", "") for symbol in block["symbols"]],
                "action": action,
                "flow_notes": rules["flow_notes"],
            }
        )

    recommendations = [
        "Use short wires inside each functional block before adding local net labels.",
        "Preserve cross-block labels for power rails and long-distance nets only.",
        "Create whitespace around the ESP32 module before final text cleanup.",
        "Keep USB-C support parts physically grouped in the same visual block.",
    ]
    if visual_flow_result["status"] != CHECK_STATUS_PASS:
        recommendations.append("Reorder the main power path so input power, buck regulator, and ESP32 read left-to-right.")
    if local_wire_result["status"] != CHECK_STATUS_PASS:
        recommendations.append("Replace repeated local labels inside blocks with direct short wires where readability improves.")
    if context["unassigned_symbols"]:
        references = ", ".join(symbol.get("reference", "") for symbol in context["unassigned_symbols"] if symbol.get("reference"))
        recommendations.append(f"Group detached symbols into named functional blocks: {references}")

    return {
        "generated_at": context["generated_at"],
        "schematic": context["schematic"],
        "planner_id": "schematic_block_layout_plan",
        "template_id": context["template_id"],
        "visual_flow_status": visual_flow_result["status"],
        "local_wire_status": local_wire_result["status"],
        "blocks": serializable_blocks(context),
        "plan_items": plan_items,
        "recommendations": recommendations,
    }


def build_markdown(result: dict[str, Any]) -> str:
    lines = [
        "# Schematic Block Layout Plan",
        "",
        f"Generated: `{result['generated_at']}`",
        f"Schematic: `{result['schematic']}`",
        "",
        f"- Visual flow status: `{result['visual_flow_status']}`",
        f"- Local wire status: `{result['local_wire_status']}`",
        "",
        "## Planned Block Actions",
        "",
        "| Block | Status | Current Region | Desired Region | Move (dx, dy mm) |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["plan_items"]:
        move = f"{item['movement_delta_mm']['dx']}, {item['movement_delta_mm']['dy']}"
        lines.append(f"| {item['title']} | `{item['status']}` | `{item['current_region']}` | `{item['desired_region']}` | `{move}` |")
    lines.extend(
        [
            "",
            "## Recommendations",
            "",
        ]
    )
    for entry in result["recommendations"]:
        lines.append(f"- {entry}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = common_parser("Plan a cleaner functional-block layout without editing the schematic.")
    args = parser.parse_args()
    project_root, schematic = resolve_project_and_schematic(args.project, args.schematic)
    project_root = project_root or infer_project_root(schematic)
    report_dir = ensure_report_dir(project_root, schematic, args.report_dir)
    report_dir.mkdir(parents=True, exist_ok=True)
    result = build_plan(schematic)
    output = Path(args.output) if args.output else report_dir / "schematic_block_layout_plan.md"
    json_output = Path(args.json_output) if args.json_output else report_dir / "schematic_block_layout_plan.json"
    write_markdown_and_json(build_markdown(result), result, output, json_output)
    print(str(json_output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
