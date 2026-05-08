#!/usr/bin/env python3
"""Place fixed mechanical components from normalized placement constraints."""

from __future__ import annotations

import argparse

from _placement_common import bbox_from_center, component_size, dump_json, load_json


def place_mounting_holes(components: list[dict], board: dict) -> list[dict]:
    width = float(board["width_mm"])
    height = float(board["height_mm"])
    clearance = float(board["edge_clearance_mm"])
    corners = [
        (clearance, clearance),
        (width - clearance, clearance),
        (clearance, height - clearance),
        (width - clearance, height - clearance),
    ]
    placements: list[dict] = []
    for component, (x_mm, y_mm) in zip(components, corners):
        width_mm, height_mm = component_size(component)
        placements.append(
            {
                "ref": component["ref"],
                "x_mm": x_mm,
                "y_mm": y_mm,
                "rotation_deg": int(component.get("rotation_deg", 0)),
                "stage_name": component["stage_name"],
                "reason": "corner mounting-hole placement",
                "bbox": bbox_from_center(x_mm, y_mm, width_mm, height_mm),
            }
        )
    return placements


def place_edge_component(component: dict, board: dict, edge_slot: int, edge_count: int) -> dict:
    board_w = float(board["width_mm"])
    board_h = float(board["height_mm"])
    clearance = float(board["edge_clearance_mm"])
    width_mm, height_mm = component_size(component)
    edge = component.get("preferred_edge") or "bottom"
    slot_pitch_x = board_w / (edge_count + 1)
    slot_pitch_y = board_h / (edge_count + 1)
    if edge == "bottom":
        x_mm = slot_pitch_x * (edge_slot + 1)
        y_mm = clearance + height_mm / 2.0
        rotation = 0
    elif edge == "top":
        x_mm = slot_pitch_x * (edge_slot + 1)
        y_mm = board_h - clearance - height_mm / 2.0
        rotation = 180
    elif edge == "left":
        x_mm = clearance + width_mm / 2.0
        y_mm = slot_pitch_y * (edge_slot + 1)
        rotation = 90
    else:
        x_mm = board_w - clearance - width_mm / 2.0
        y_mm = slot_pitch_y * (edge_slot + 1)
        rotation = 270
    return {
        "ref": component["ref"],
        "x_mm": round(x_mm, 3),
        "y_mm": round(y_mm, 3),
        "rotation_deg": int(component.get("rotation_deg", rotation)),
        "stage_name": component["stage_name"],
        "reason": f"edge placement on {edge}",
        "bbox": bbox_from_center(x_mm, y_mm, width_mm, height_mm),
    }


def place_rf_module(component: dict, board: dict) -> dict:
    board_w = float(board["width_mm"])
    board_h = float(board["height_mm"])
    clearance = float(board["edge_clearance_mm"])
    width_mm, height_mm = component_size(component)
    x_mm = board_w / 2.0
    y_mm = board_h - clearance - height_mm / 2.0
    keepout_w = float(component.get("keepout_width_mm", width_mm))
    keepout_h = float(component.get("keepout_height_mm", height_mm))
    return {
        "ref": component["ref"],
        "x_mm": round(x_mm, 3),
        "y_mm": round(y_mm, 3),
        "rotation_deg": int(component.get("rotation_deg", 0)),
        "stage_name": component["stage_name"],
        "reason": "RF module placed first with antenna edge clearance",
        "bbox": bbox_from_center(x_mm, y_mm, width_mm, height_mm),
        "keepout_bbox": bbox_from_center(x_mm, y_mm, keepout_w, keepout_h),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("constraints_json")
    parser.add_argument("output_json")
    args = parser.parse_args()

    payload = load_json(args.constraints_json)
    board = payload["board"]
    components = payload["components"]
    placements: list[dict] = []
    holes = [item for item in components if item["role"] == "MOUNTING_HOLE"]
    placements.extend(place_mounting_holes(holes, board))

    edge_components = [
        item
        for item in components
        if item["role"] in {"USB_C", "BARREL_JACK", "EDGE_CONNECTOR", "RF_CONNECTOR"}
    ]
    for index, component in enumerate(edge_components):
        placements.append(place_edge_component(component, board, index, len(edge_components)))

    for component in components:
        if component["role"] == "RF_MODULE":
            placements.append(place_rf_module(component, board))

    result = {
        "project": payload.get("project", ""),
        "board": board,
        "placements": placements,
        "status": "PASS" if not payload.get("validation_errors") else "AUTO_BLOCKED_MISSING_DATA",
        "validation_errors": payload.get("validation_errors", []),
    }
    dump_json(args.output_json, result)
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
