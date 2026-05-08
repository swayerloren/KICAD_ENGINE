#!/usr/bin/env python3
"""Score real-board placement readiness before routing."""

from __future__ import annotations

import argparse
from pathlib import Path

from _placement_common import (
    BOARD_EDGE_COMPONENT_MARGIN_MM,
    HARD_FAIL_STATUSES,
    bbox_distance,
    bbox_overlap_area,
    bbox_within_bounds,
    build_live_placement_state,
    dump_json,
    dump_markdown,
    expand_bbox,
    overhang_amounts,
)
from detect_antenna_keepout_placement_risks import analyze_antenna_keepout_placement_risks
from detect_connector_orientation_risks import analyze_connector_orientation_risks
from detect_power_path_placement_risks import analyze_power_path_placement_risks
from detect_testpad_accessibility_risks import analyze_testpad_accessibility_risks
from detect_usb_cluster_placement_risks import analyze_usb_cluster_placement_risks


def summarize_board_fit(state: dict) -> dict:
    board_bbox = state["board"]["bbox"]
    findings: list[dict] = []
    warnings: list[str] = []
    hard_fails: list[str] = []
    score = 15

    for component in state["components"]:
        role = component["role"]
        if role in {"USB_C", "BARREL_JACK", "EDGE_CONNECTOR"}:
            edge = str(component["edge_proximity"]["edge"])
            overhang = overhang_amounts(board_bbox, component["courtyard_bbox"])
            off_edge = {name: value for name, value in overhang.items() if name != edge and value > 0.5}
            if off_edge:
                hard_fails.append("FOOTPRINT_OUTSIDE_BOARD")
                findings.append(
                    {
                        "ref": component["ref"],
                        "status": "FOOTPRINT_OUTSIDE_BOARD",
                        "reason": f"Edge connector overhang spills beyond non-target board sides: {off_edge}.",
                        "recommended_fix": "Keep connector overhang only on the intended mating edge.",
                    }
                )
                score -= 6
        else:
            if not bbox_within_bounds(component["body_bbox"], board_bbox, margin_mm=BOARD_EDGE_COMPONENT_MARGIN_MM):
                hard_fails.append("FOOTPRINT_OUTSIDE_BOARD")
                findings.append(
                    {
                        "ref": component["ref"],
                        "status": "FOOTPRINT_OUTSIDE_BOARD",
                        "reason": "Component body extends beyond the live board outline.",
                        "recommended_fix": "Move the footprint fully inside the board outline or change the board outline.",
                    }
                )
                score -= 6
            elif not bbox_within_bounds(component["courtyard_bbox"], board_bbox, margin_mm=0.5):
                warnings.append(f"{component['ref']}: courtyard approaches or crosses the board edge margin.")
                score -= 1

    return {
        "category": "board_outline_mechanical_fit",
        "score": max(0, score),
        "hard_fail_statuses": sorted(set(hard_fails)),
        "warnings": warnings,
        "findings": findings,
    }


def summarize_clearance(state: dict) -> dict:
    components = [item for item in state["components"] if not item["mounting_hole"]]
    findings: list[dict] = []
    warnings: list[str] = []
    hard_fails: list[str] = []
    score = 10

    for index, left in enumerate(components):
        for right in components[index + 1 :]:
            overlap_area = bbox_overlap_area(left["body_bbox"], right["body_bbox"])
            if overlap_area > 0.01:
                hard_fails.append("COURTYARD_BODY_OVERLAP")
                findings.append(
                    {
                        "ref_pair": f"{left['ref']} / {right['ref']}",
                        "status": "COURTYARD_BODY_OVERLAP",
                        "reason": f"Component body boxes overlap by {overlap_area:.3f} mm^2.",
                        "recommended_fix": "Separate the footprints so body and courtyard regions no longer overlap.",
                    }
                )
                score -= 5
                continue
            near_left = expand_bbox(left["body_bbox"], 0.2)
            near_right = expand_bbox(right["body_bbox"], 0.2)
            if bbox_overlap_area(near_left, near_right) > 0.01:
                warnings.append(f"{left['ref']} / {right['ref']}: clearance is very tight.")
                score -= 1
            elif bbox_distance(left["body_bbox"], right["body_bbox"]) < 0.25:
                warnings.append(f"{left['ref']} / {right['ref']}: sub-0.25 mm body-to-body gap.")
                score -= 1

    return {
        "category": "courtyard_body_clearance",
        "score": max(0, score),
        "hard_fail_statuses": sorted(set(hard_fails)),
        "warnings": warnings,
        "findings": findings,
    }


def summarize_routing_feasibility(category_results: list[dict]) -> dict:
    hard_fails = sorted({item for result in category_results for item in result.get("hard_fail_statuses", []) if item in HARD_FAIL_STATUSES})
    findings: list[dict] = []
    score = 5

    impossible_sources = {
        "FOOTPRINT_OUTSIDE_BOARD",
        "COURTYARD_BODY_OVERLAP",
        "ESP32_ANTENNA_KEEPOUT_BLOCKED",
    }
    if impossible_sources & set(hard_fails):
        findings.append(
            {
                "status": "PLACEMENT_CREATES_IMPOSSIBLE_ROUTE",
                "reason": "Mechanical or keepout hard fails already make routing continuation unsafe.",
                "recommended_fix": "Resolve board-fit, clearance, or antenna issues before any further routing.",
            }
        )
        hard_fails.append("PLACEMENT_CREATES_IMPOSSIBLE_ROUTE")
        score = 0
    elif {"POWER_PATH_SCATTERED_BEYOND_THRESHOLD", "USB_CLUSTER_TOO_SPREAD"} & set(hard_fails):
        findings.append(
            {
                "status": "PLACEMENT_CREATES_IMPOSSIBLE_ROUTE",
                "reason": "Critical functional clusters are spread far enough apart that clean routing is unlikely without placement repair.",
                "recommended_fix": "Compact the failing cluster before continuing routing.",
            }
        )
        hard_fails.append("PLACEMENT_CREATES_IMPOSSIBLE_ROUTE")
        score = 0

    return {
        "category": "routing_feasibility",
        "score": score,
        "hard_fail_statuses": sorted(set(hard_fails)),
        "warnings": [],
        "findings": findings,
    }


def classify_result(total_score: int, hard_fails: list[str]) -> str:
    if hard_fails:
        return "PLACEMENT_BLOCKED_HUMAN_REVIEW"
    if total_score >= 80:
        return "PLACEMENT_READY_FOR_ROUTING"
    return "PLACEMENT_REPAIR_REQUIRED"


def build_result(state: dict) -> dict:
    connector = analyze_connector_orientation_risks(state)
    board_fit = summarize_board_fit(state)
    antenna = analyze_antenna_keepout_placement_risks(state)
    power = analyze_power_path_placement_risks(state)
    usb = analyze_usb_cluster_placement_risks(state)
    testpads = analyze_testpad_accessibility_risks(state)
    clearance = summarize_clearance(state)

    category_results = [
        {
            "category": "connector_orientation_proof",
            "score": connector["score"],
            "hard_fail_statuses": connector["hard_fail_statuses"],
            "warnings": connector["warnings"],
            "findings": connector["findings"],
        },
        board_fit,
        {
            "category": "antenna_keepout_compliance",
            "score": antenna["score"],
            "hard_fail_statuses": antenna["hard_fail_statuses"],
            "warnings": antenna["warnings"],
            "findings": antenna["findings"],
        },
        {
            "category": "power_path_adjacency",
            "score": power["score"],
            "hard_fail_statuses": power["hard_fail_statuses"],
            "warnings": power["warnings"],
            "findings": power["findings"],
        },
        {
            "category": "usb_cluster_compactness",
            "score": usb["score"],
            "hard_fail_statuses": usb["hard_fail_statuses"],
            "warnings": usb["warnings"],
            "findings": usb["findings"],
        },
        {
            "category": "testpad_accessibility",
            "score": testpads["score"],
            "hard_fail_statuses": testpads["hard_fail_statuses"],
            "warnings": testpads["warnings"],
            "findings": testpads["findings"],
        },
        clearance,
    ]
    routing_feasibility = summarize_routing_feasibility(category_results)
    category_results.append(routing_feasibility)

    total_score = sum(int(result["score"]) for result in category_results)
    hard_fails = sorted({item for result in category_results for item in result["hard_fail_statuses"]})
    warnings = [warning for result in category_results for warning in result["warnings"]]
    findings = [finding for result in category_results for finding in result["findings"]]
    status = classify_result(total_score, hard_fails)

    return {
        "project": state["project"],
        "tool": "score_placement_readiness",
        "status": status,
        "summary": {
            "total_score": total_score,
            "component_count": len(state["components"]),
            "track_count": len(state["tracks"]),
            "via_count": len(state["vias"]),
        },
        "scores": {
            "connector_orientation_proof": category_results[0]["score"],
            "board_outline_mechanical_fit": category_results[1]["score"],
            "antenna_keepout_compliance": category_results[2]["score"],
            "power_path_adjacency": category_results[3]["score"],
            "usb_cluster_compactness": category_results[4]["score"],
            "test_pad_accessibility": category_results[5]["score"],
            "courtyard_body_clearance": category_results[6]["score"],
            "routing_feasibility": category_results[7]["score"],
        },
        "hard_fail_statuses": hard_fails,
        "warnings": warnings,
        "findings": findings,
        "source_pcb": state["source_pcb"],
        "source_sha256": state["source_sha256"],
        "unsupported_extract_notes": state["unsupported_extract_notes"],
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Placement Readiness Scorecard",
        "",
        f"- Project: `{result['project']}`",
        f"- Status: `{result['status']}`",
        f"- Source PCB: `{result['source_pcb']}`",
        f"- Source SHA256: `{result['source_sha256']}`",
        f"- Total score: `{result['summary']['total_score']}` / 100",
        f"- Components reviewed: `{result['summary']['component_count']}`",
        "",
        "## Category Scores",
    ]
    for name, score in result["scores"].items():
        lines.append(f"- `{name}`: `{score}`")
    lines.extend(["", "## Hard Fails"])
    if result["hard_fail_statuses"]:
        lines.extend(f"- `{item}`" for item in result["hard_fail_statuses"])
    else:
        lines.append("- `_none_`")
    lines.extend(["", "## Findings"])
    if result["findings"]:
        for finding in result["findings"]:
            ref_text = finding.get("ref") or finding.get("ref_pair") or finding.get("from_stage", "n/a")
            lines.append(f"- `{ref_text}` `{finding['status']}`: {finding['reason']}")
            lines.append(f"  - Recommended fix: {finding['recommended_fix']}")
    else:
        lines.append("- `_none_`")
    lines.extend(["", "## Warnings"])
    if result["warnings"]:
        lines.extend(f"- {item}" for item in result["warnings"])
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
    result = build_result(state)
    dump_json(args.output_json, result)
    if args.markdown:
        dump_markdown(args.markdown, render_markdown(result))
    return 0 if result["status"] == "PLACEMENT_READY_FOR_ROUTING" else 1


if __name__ == "__main__":
    raise SystemExit(main())
