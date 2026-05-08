#!/usr/bin/env python3
"""Detect connector orientation risks from a live or copied KiCad PCB."""

from __future__ import annotations

import argparse
from pathlib import Path

from _placement_common import (
    EDGE_CONNECTOR_MAX_EDGE_DISTANCE_MM,
    build_live_placement_state,
    dump_json,
    dump_markdown,
    orientation_family,
    overhang_amounts,
)


def expected_orientation(edge: str) -> str:
    return "horizontal" if edge in {"top", "bottom"} else "vertical"


def failure_status(role: str) -> str:
    return "USB_CONNECTOR_ORIENTATION_UNKNOWN" if role == "USB_C" else "POWER_CONNECTOR_ORIENTATION_UNKNOWN"


def analyze_connector_orientation_risks(state: dict) -> dict:
    board_bbox = state["board"]["bbox"]
    connectors = [item for item in state["components"] if item["role"] in {"USB_C", "BARREL_JACK", "EDGE_CONNECTOR"}]
    findings: list[dict] = []
    hard_fails: list[str] = []
    warnings: list[str] = []
    score = 20

    for component in connectors:
        edge = str(component["edge_proximity"]["edge"])
        distance_mm = float(component["edge_proximity"]["distance_mm"])
        family = orientation_family(float(component["rotation_deg"]))
        expected = expected_orientation(edge)
        overhang = overhang_amounts(board_bbox, component["courtyard_bbox"])
        off_edge_overhang = {name: value for name, value in overhang.items() if name != edge and value > 0.5}

        if distance_mm > EDGE_CONNECTOR_MAX_EDGE_DISTANCE_MM or family != expected:
            status = failure_status(component["role"])
            hard_fails.append(status)
            findings.append(
                {
                    "ref": component["ref"],
                    "role": component["role"],
                    "status": status,
                    "edge": edge,
                    "rotation_deg": component["rotation_deg"],
                    "distance_mm": round(distance_mm, 3),
                    "reason": "Connector is not convincingly edge-facing for its nearest board edge.",
                    "recommended_fix": "Move the connector tight to the intended board edge and align its rotation so the mating face exits the board edge cleanly.",
                }
            )
            score -= 10
        elif off_edge_overhang:
            warnings.append(f"{component['ref']}: connector overhangs non-edge sides {off_edge_overhang}")
            findings.append(
                {
                    "ref": component["ref"],
                    "role": component["role"],
                    "status": "WARNING",
                    "edge": edge,
                    "rotation_deg": component["rotation_deg"],
                    "distance_mm": round(distance_mm, 3),
                    "reason": f"Connector courtyard extends beyond non-target board sides: {off_edge_overhang}.",
                    "recommended_fix": "Confirm the overhang is intentional and mechanically acceptable.",
                }
            )
            score -= 2

    result = {
        "project": state["project"],
        "tool": "detect_connector_orientation_risks",
        "status": "PASS" if not hard_fails else "AUTO_BLOCKED_BAD_LAYOUT",
        "score": max(0, score),
        "connector_count": len(connectors),
        "hard_fail_statuses": sorted(set(hard_fails)),
        "warnings": warnings,
        "findings": findings,
    }
    return result


def render_markdown(result: dict) -> str:
    lines = [
        "# Connector Orientation Risks",
        "",
        f"- Project: `{result['project']}`",
        f"- Status: `{result['status']}`",
        f"- Score: `{result['score']}` / 20",
        f"- Connectors reviewed: `{result['connector_count']}`",
        "",
        "## Hard Fails",
    ]
    if result["hard_fail_statuses"]:
        lines.extend(f"- `{item}`" for item in result["hard_fail_statuses"])
    else:
        lines.append("- `_none_`")
    lines.extend(["", "## Findings"])
    if result["findings"]:
        for finding in result["findings"]:
            lines.extend(
                [
                    f"- `{finding['ref']}` `{finding['status']}` on `{finding['edge']}` at {finding['rotation_deg']} deg",
                    f"  - Reason: {finding['reason']}",
                    f"  - Recommended fix: {finding['recommended_fix']}",
                ]
            )
    else:
        lines.append("- `_none_`")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pcb_file")
    parser.add_argument("output_json")
    parser.add_argument("--markdown")
    args = parser.parse_args()

    state = build_live_placement_state(Path(args.pcb_file))
    result = analyze_connector_orientation_risks(state)
    dump_json(args.output_json, result)
    if args.markdown:
        dump_markdown(args.markdown, render_markdown(result))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
