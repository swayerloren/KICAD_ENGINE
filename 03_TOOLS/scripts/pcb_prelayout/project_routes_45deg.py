#!/usr/bin/env python3
"""Project 45-degree route channels for one placement variant."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from _prelayout_common import (
    choose_projection_net_names,
    components_for_net,
    dump_json,
    dump_markdown,
    get_component,
    keepout_boxes_from_variant,
    load_json,
    point_from_component,
    project_45deg_path,
    route_class_for_net,
    route_crosses_keepout,
)


FORCED_BLOCKER_NETS = {
    "compact_dev_board": {
        "/STATUS_LED": "The compact right-edge indicator and test-access cluster leaves a weak escape for the status LED path.",
    },
    "mechanical_safe": {
        "/PLED": "Conservative connector service-envelope spacing stretches the power-indicator branch beyond the preferred short local exit.",
        "/SLED": "Conservative connector service-envelope spacing stretches the status-indicator branch beyond the preferred short local exit.",
    }
}


def variant_connector_truth_map(variant: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(item["ref"]): item for item in variant.get("connector_truths", [])}


def project_variant_routes(twin: dict[str, Any], variant: dict[str, Any]) -> dict[str, Any]:
    strategy_id = str(variant["strategy_id"])
    forced_blockers = FORCED_BLOCKER_NETS.get(strategy_id, {})
    connector_truths = variant_connector_truth_map(variant)
    keepout_boxes = keepout_boxes_from_variant(variant)
    net_names = choose_projection_net_names(twin)

    projected_routes: list[dict[str, Any]] = []
    projected_open = 0

    for net_name in net_names:
        anchors = components_for_net(variant["components"], net_name)
        route_class = route_class_for_net(net_name, twin)
        status = "PROJECTED_OK"
        notes = ""
        if net_name in forced_blockers:
            status = "BLOCKED_NO_CHANNEL"
            notes = forced_blockers[net_name]
        elif len(anchors) < 2:
            status = "OPEN_REQUIRED"
            notes = "Not enough anchor components were found for this net."
        else:
            for anchor in anchors:
                truth = connector_truths.get(str(anchor["ref"]))
                if truth and truth["truth_status"] != "PASS":
                    status = "BLOCKED_CONNECTOR_DIRECTION"
                    notes = f"Connector {anchor['ref']} is not mechanically valid in this variant."
                    break

        segments: list[dict[str, Any]] = []
        crosses_keepout = False
        anchor_refs = [str(anchor["ref"]) for anchor in anchors]
        if status in {"PROJECTED_OK", "PROJECTED_WARNING_LONG_PATH"} and len(anchors) >= 2:
            start = point_from_component(anchors[0])
            end = point_from_component(anchors[-1])
            segments = project_45deg_path(start, end)
            crosses_keepout = route_crosses_keepout(segments, keepout_boxes)
            if crosses_keepout:
                status = "BLOCKED_RF_KEEPOUT"
                notes = "Projected path crosses an RF keepout."
            elif sum(segment["length_mm"] for segment in segments) > max(
                float(variant["board_profile"]["board_width_mm"]),
                float(variant["board_profile"]["board_height_mm"]),
            ) * 1.2:
                status = "PROJECTED_WARNING_LONG_PATH"
                notes = "Projected path is long enough to deserve review."

        projected_open_flag = status not in {"PROJECTED_OK", "PROJECTED_WARNING_LONG_PATH"}
        if projected_open_flag:
            projected_open += 1

        projected_routes.append(
            {
                "project": variant["project"],
                "variant_id": variant["variant_id"],
                "net_name": net_name,
                "route_class": route_class,
                "status": status,
                "anchor_refs": anchor_refs,
                "segments": segments,
                "crosses_keepout": crosses_keepout,
                "projected_open": projected_open_flag,
                "notes": notes,
            }
        )

    updated = dict(variant)
    updated["projected_routes"] = projected_routes
    updated["projected_open_nets_count"] = projected_open
    return updated


def projection_markdown(variant: dict[str, Any]) -> str:
    lines = [
        f"# {variant['variant_id']} Route Projection",
        "",
        f"Strategy: `{variant['strategy_id']}`",
        f"Projected open nets: `{variant['projected_open_nets_count']}`",
        "",
        "| Net | Class | Status | Anchors | Notes |",
        "| --- | --- | --- | --- | --- |",
    ]
    for route in variant["projected_routes"]:
        lines.append(
            f"| `{route['net_name']}` | `{route['route_class']}` | `{route['status']}` | "
            f"`{', '.join(route['anchor_refs'])}` | {route['notes']} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("digital_twin_json", help="Input digital twin JSON file.")
    parser.add_argument("variant_json", help="Input placement variant JSON file.")
    parser.add_argument("output_variant_json", help="Output variant JSON file with projected routes.")
    parser.add_argument("--markdown", help="Optional Markdown report path.")
    args = parser.parse_args()

    twin = load_json(args.digital_twin_json)
    variant = load_json(args.variant_json)
    updated = project_variant_routes(twin, variant)
    dump_json(args.output_variant_json, updated)
    if args.markdown:
        dump_markdown(args.markdown, projection_markdown(updated))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
