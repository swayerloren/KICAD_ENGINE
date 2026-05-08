#!/usr/bin/env python3
"""Place non-mechanical component groups around fixed placements."""

from __future__ import annotations

import argparse

from _placement_common import STAGE_ORDER, bbox_from_center, bboxes_overlap, component_size, dump_json, load_json


def candidate_positions(board: dict, gap_mm: float) -> list[tuple[float, float]]:
    width = float(board["width_mm"])
    height = float(board["height_mm"])
    clearance = float(board["edge_clearance_mm"]) + gap_mm
    cols = 6
    rows = 8
    xs = [clearance + (width - 2 * clearance) * (index + 1) / (cols + 1) for index in range(cols)]
    ys = [clearance + (height - 2 * clearance) * (index + 1) / (rows + 1) for index in range(rows)]
    positions: list[tuple[float, float]] = []
    for y_mm in ys:
        for x_mm in xs:
            positions.append((round(x_mm, 3), round(y_mm, 3)))
    return positions


def forbidden_bboxes(fixed_plan: dict) -> list[dict]:
    boxes: list[dict] = []
    for placement in fixed_plan.get("placements", []):
        if "bbox" in placement:
            boxes.append(placement["bbox"])
        if "keepout_bbox" in placement:
            boxes.append(placement["keepout_bbox"])
    return boxes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("constraints_json")
    parser.add_argument("fixed_plan_json")
    parser.add_argument("output_json")
    args = parser.parse_args()

    constraints = load_json(args.constraints_json)
    fixed_plan = load_json(args.fixed_plan_json)
    board = constraints["board"]
    settings = constraints.get("placement_settings", {})
    gap_mm = float(settings.get("group_gap_mm", settings.get("default_gap_mm", 0.5)))
    blocked_boxes = forbidden_bboxes(fixed_plan)
    taken_boxes = list(blocked_boxes)
    candidates = candidate_positions(board, gap_mm)
    placements = list(fixed_plan.get("placements", []))
    warnings: list[str] = []

    components = sorted(
        constraints["components"],
        key=lambda item: (
            item["placement_stage"],
            item.get("current_flow_order", 0),
            item["ref"],
        ),
    )

    placed_refs = {item["ref"] for item in placements}
    active_stage_names = [name for name in STAGE_ORDER if name not in {"BOARD_OUTLINE", "MOUNTING_HOLES", "EDGE_CONNECTORS", "RF_AND_KEEPOUT"}]

    for component in components:
        if component["ref"] in placed_refs or component["stage_name"] not in active_stage_names:
            continue
        width_mm, height_mm = component_size(component)
        bbox = None
        chosen = None
        for x_mm, y_mm in candidates:
            bbox = bbox_from_center(x_mm, y_mm, width_mm, height_mm)
            if any(bboxes_overlap(bbox, other) for other in taken_boxes):
                continue
            chosen = (x_mm, y_mm)
            break
        if chosen is None:
            warnings.append(f"{component['ref']}: no collision-free placement candidate found")
            continue
        x_mm, y_mm = chosen
        placement = {
            "ref": component["ref"],
            "x_mm": x_mm,
            "y_mm": y_mm,
            "rotation_deg": int(component.get("rotation_deg", 0)),
            "stage_name": component["stage_name"],
            "group": component.get("group", ""),
            "reason": f"group placement for {component['stage_name']}",
            "bbox": bbox,
        }
        placements.append(placement)
        taken_boxes.append(bbox)
        placed_refs.add(component["ref"])

    status = "PASS" if not warnings and not constraints.get("validation_errors") else "AUTO_BLOCKED_BAD_LAYOUT"
    result = {
        "project": constraints.get("project", ""),
        "board": board,
        "placements": placements,
        "warnings": warnings,
        "status": status,
        "unplaced_refs": [component["ref"] for component in components if component["ref"] not in placed_refs],
    }
    dump_json(args.output_json, result)
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
