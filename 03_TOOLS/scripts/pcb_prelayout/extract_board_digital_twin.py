#!/usr/bin/env python3
"""Extract a read-only board digital twin for the PCB prelayout engine."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from _prelayout_common import (
    build_board_profile,
    build_connector_truth,
    build_live_placement_state,
    choose_projection_net_names,
    dump_json,
    dump_markdown,
    infer_connector_type,
    iso_now,
    load_live_state,
    load_routing_schema,
    locate_pcb,
    locate_project,
    mechanical_conflict_pairs,
    repo_rel,
    route_class_for_net,
)


def extract_board_digital_twin(project_path: str | Path) -> dict[str, Any]:
    project = locate_project(project_path)
    pcb_path = locate_pcb(project)
    live_state = load_live_state(project)
    routing_schema = load_routing_schema(project)
    placement_state = build_live_placement_state(pcb_path)

    board_profile = build_board_profile(live_state)
    components = placement_state["components"]
    board_profile["rf_module_present"] = any(component.get("role") == "RF_MODULE" for component in components)

    connector_truth_candidates = []
    for component in components:
        connector_type = infer_connector_type(component)
        if connector_type in {"USB_C", "BARREL_JACK", "EDGE_CONNECTOR"} or str(component.get("ref", "")).upper().startswith("J"):
            intended_edge = component.get("edge_proximity", {}).get("edge")
            connector_truth_candidates.append(build_connector_truth(component, board_profile, intended_edge))

    twin = {
        "schema_version": "1.0",
        "generated_at": iso_now(),
        "project": project.name,
        "project_path": repo_rel(project),
        "source_pcb": repo_rel(pcb_path),
        "source_sha256": board_profile["source_sha256"],
        "board_profile": board_profile,
        "live_board_context": board_profile["live_board_context"],
        "nets": [],
        "projection_net_names": [],
        "components": components,
        "connector_truth_candidates": connector_truth_candidates,
        "fixed_mechanical_refs": [component["ref"] for component in components if component.get("fixed_mechanical")],
        "mechanical_conflict_pairs": mechanical_conflict_pairs(components),
        "source_artifacts": {
            "live_project_state_json": repo_rel(project / "reports" / "LIVE_PROJECT_STATE.json"),
            "routing_schema_json": repo_rel(project / "reports" / "live_project_state" / "LIVE_PROJECT_STATE_ROUTING_SCHEMA.json"),
        },
    }

    for net in routing_schema.get("nets", []) or []:
        twin["nets"].append(
            {
                "name": net.get("name", ""),
                "role": net.get("role", "LOW_RISK"),
                "power": bool(net.get("power")),
                "usb": bool(net.get("usb")),
                "critical": bool(net.get("critical")),
                "routing_priority": int(net.get("routing_priority", 0)),
                "routing_status": net.get("routing_status", ""),
                "route_class": route_class_for_net(str(net.get("name", "")), {"nets": [net]}),
                "pads": net.get("pads", []),
            }
        )
    twin["projection_net_names"] = choose_projection_net_names(twin)
    return twin


def twin_markdown(twin: dict[str, Any]) -> str:
    board = twin["board_profile"]
    live = twin["live_board_context"]
    connector_rows = []
    for truth in twin["connector_truth_candidates"]:
        connector_rows.append(
            [
                str(truth["ref"]),
                str(truth["connector_type"]),
                str(truth["intended_edge"]),
                str(truth["mating_direction"]),
                str(truth["truth_status"]),
            ]
        )
    lines = [
        "# PCB Digital Twin",
        "",
        f"Generated: `{twin['generated_at']}`",
        "",
        f"Project: `{twin['project']}`",
        f"Source PCB: `{twin['source_pcb']}`",
        f"Source hash: `{twin['source_sha256']}`",
        "",
        "## Board Profile",
        "",
        f"- Shape: `{board['board_shape']}`",
        f"- Size: `{board['board_width_mm']} mm x {board['board_height_mm']} mm`",
        f"- Mounting holes: `{board['mounting_hole_count']}`",
        f"- RF module present: `{board['rf_module_present']}`",
        "",
        "## Live Board Context",
        "",
        f"- DRC result: `{live['drc_result']}`",
        f"- Violations: `{live['violation_count']}`",
        f"- Unconnected items: `{live['unconnected_count']}`",
        f"- Detectable unrouted nets: `{live['detectable_unrouted_net_count']}`",
        "",
        f"- Component count: `{len(twin['components'])}`",
        f"- Projection net count: `{len(twin['projection_net_names'])}`",
        "",
        "## Connector Truth Candidates",
        "",
        (
            "| Ref | Type | Intended Edge | Mating Direction | Status |\n"
            "| --- | --- | --- | --- | --- |"
            if connector_rows
            else "_No connector candidates found._"
        ),
    ]
    if connector_rows:
        for row in connector_rows:
            lines.append(f"| `{row[0]}` | `{row[1]}` | `{row[2]}` | `{row[3]}` | `{row[4]}` |")
    lines.extend(
        [
            "",
            "## Projection Nets",
            "",
        ]
    )
    for name in twin["projection_net_names"]:
        lines.append(f"- `{name}`")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, help="Active project path.")
    parser.add_argument("--output-json", required=True, help="Output twin JSON path.")
    parser.add_argument("--markdown", help="Optional Markdown summary path.")
    args = parser.parse_args()

    twin = extract_board_digital_twin(args.project)
    dump_json(args.output_json, twin)
    if args.markdown:
        dump_markdown(args.markdown, twin_markdown(twin))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

