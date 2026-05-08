#!/usr/bin/env python3
"""Normalize component metadata into placement constraints."""

from __future__ import annotations

import argparse

from _placement_common import STAGE_INDEX, component_size, dump_json, load_json, normalize_edge, placement_stage_for_role


def enrich_component(component: dict) -> dict:
    role = str(component.get("role", "")).strip().upper()
    stage_name = placement_stage_for_role(role)
    width, height = component_size(component)
    preferred_edge = normalize_edge(component.get("preferred_edge"))

    enriched = dict(component)
    enriched["role"] = role
    enriched["placement_stage"] = STAGE_INDEX[stage_name]
    enriched["stage_name"] = stage_name
    enriched["preferred_edge"] = preferred_edge
    enriched["must_be_edge_facing"] = role in {"USB_C", "BARREL_JACK", "EDGE_CONNECTOR"}
    enriched["fixed_mechanical"] = bool(component.get("fixed_mechanical", False)) or role in {
        "MOUNTING_HOLE",
        "USB_C",
        "BARREL_JACK",
        "EDGE_CONNECTOR",
        "RF_CONNECTOR",
    }
    enriched["must_be_accessible"] = bool(component.get("must_be_accessible", False)) or role in {
        "USB_C",
        "BARREL_JACK",
        "RESET_BUTTON",
        "BOOT_BUTTON",
        "LED",
        "TEST_PAD",
    }
    enriched["current_flow_order"] = int(component.get("current_flow_order", 0))
    enriched["courtyard_width_mm"] = width
    enriched["courtyard_height_mm"] = height
    return enriched


def validate(payload: dict) -> list[str]:
    errors: list[str] = []
    board = payload.get("board", {})
    for key in ("width_mm", "height_mm", "shape", "edge_clearance_mm"):
        if key not in board:
            errors.append(f"board.{key} is required")
    components = payload.get("components")
    if not isinstance(components, list) or not components:
        errors.append("components must be a non-empty list")
        return errors
    for component in components:
        ref = component.get("ref", "<unknown>")
        for key in ("ref", "role", "width_mm", "height_mm", "courtyard_width_mm", "courtyard_height_mm"):
            if key not in component:
                errors.append(f"{ref}: missing {key}")
        role = str(component.get("role", "")).strip().upper()
        if role in {"USB_C", "BARREL_JACK", "EDGE_CONNECTOR"} and not normalize_edge(component.get("preferred_edge")):
            errors.append(f"{ref}: fixed edge connector is missing preferred_edge")
        if role == "RF_MODULE":
            if float(component.get("keepout_width_mm", 0.0)) <= 0 or float(component.get("keepout_height_mm", 0.0)) <= 0:
                errors.append(f"{ref}: RF module is missing keepout dimensions")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_json", help="Project placement input JSON.")
    parser.add_argument("output_json", help="Normalized placement constraints JSON.")
    args = parser.parse_args()

    payload = load_json(args.input_json)
    errors = validate(payload)
    enriched = {
        "project": payload.get("project", ""),
        "board": payload.get("board", {}),
        "placement_settings": payload.get("placement_settings", {}),
        "components": [enrich_component(component) for component in payload.get("components", [])],
        "validation_errors": errors,
        "status": "AUTO_BLOCKED_MISSING_DATA" if errors else "PASS",
    }
    dump_json(args.output_json, enriched)
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
