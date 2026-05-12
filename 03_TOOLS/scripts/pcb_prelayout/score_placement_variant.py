#!/usr/bin/env python3
"""Score one placement variant after route projection."""

from __future__ import annotations

import argparse
from typing import Any

from _prelayout_common import (
    component_outside_board,
    dump_json,
    dump_markdown,
    mechanical_conflict_pairs,
    load_json,
)


STATUS_PRIORITY = {
    "PASS": 0,
    "AUTO_BLOCKED_MISSING_DATA": 1,
    "AUTO_BLOCKED_BAD_LAYOUT": 2,
    "FAIL": 3,
}


def route_statuses_by_prefix(variant: dict[str, Any], prefixes: tuple[str, ...]) -> list[str]:
    statuses: list[str] = []
    for route in variant.get("projected_routes", []):
        name = str(route.get("net_name", ""))
        if name.startswith(prefixes) or name in prefixes:
            statuses.append(str(route.get("status", "")))
    return statuses


def score_variant(variant: dict[str, Any]) -> dict[str, Any]:
    components = variant.get("components", [])
    component_map = {str(component["ref"]): component for component in components}
    connector_truths = variant.get("connector_truths", [])
    projected_routes = variant.get("projected_routes", [])
    board_profile = variant["board_profile"]
    live = board_profile["live_board_context"]

    missing_data = not connector_truths or not projected_routes
    hard_fail_codes: list[str] = []
    blocking_reasons: list[str] = []

    overlap_pairs = mechanical_conflict_pairs(components)
    hard_overlap_pairs = [
        pair
        for pair in overlap_pairs
        if component_map[pair[0]].get("fixed_mechanical")
        or component_map[pair[1]].get("fixed_mechanical")
        or component_map[pair[0]].get("role") == "RF_MODULE"
        or component_map[pair[1]].get("role") == "RF_MODULE"
    ]
    outside_refs = [
        component["ref"]
        for component in components
        if component_outside_board(component, board_profile) and not component.get("fixed_mechanical")
    ]

    truth_fail_count = sum(1 for truth in connector_truths if truth["truth_status"] == "FAIL")
    truth_unknown_count = sum(1 for truth in connector_truths if truth["truth_status"] == "UNKNOWN")
    truth_human_review_count = sum(1 for truth in connector_truths if truth["truth_status"] == "NEEDS_HUMAN_REVIEW")
    projected_open_nets_count = int(variant.get("projected_open_nets_count", 0))
    keepout_crossings = sum(1 for route in projected_routes if route.get("crosses_keepout"))

    if truth_fail_count:
        hard_fail_codes.append("CONNECTOR_DIRECTION_FAIL")
        blocking_reasons.append(f"{truth_fail_count} connector truth record(s) failed.")
    if truth_unknown_count:
        hard_fail_codes.append("CONNECTOR_DIRECTION_UNKNOWN")
        blocking_reasons.append(f"{truth_unknown_count} connector truth record(s) remain unknown.")
    if truth_human_review_count:
        hard_fail_codes.append("CONNECTOR_ORIENTATION_NEEDS_HUMAN_REVIEW")
        blocking_reasons.append(f"{truth_human_review_count} connector truth record(s) still require human review.")
    if projected_open_nets_count:
        hard_fail_codes.append("PROJECTED_OPEN_NETS_PRESENT")
        blocking_reasons.append(f"{projected_open_nets_count} projected open net(s) remain.")
    if keepout_crossings:
        hard_fail_codes.append("PROJECTED_RF_KEEPOUT_CROSSING")
        blocking_reasons.append(f"{keepout_crossings} projected route(s) cross an RF keepout.")
    if hard_overlap_pairs:
        hard_fail_codes.append("MECHANICAL_COMPONENT_OVERLAP")
        blocking_reasons.append(f"{len(hard_overlap_pairs)} critical component overlap pair(s) exist.")
    if outside_refs:
        hard_fail_codes.append("COMPONENT_OUTSIDE_BOARD")
        blocking_reasons.append(f"{len(outside_refs)} component(s) sit outside the board outline.")

    mechanical_correctness = max(0, 20 - min(20, len(hard_overlap_pairs) * 6 + len(outside_refs) * 4))
    connector_truth_correctness = max(0, 20 - truth_fail_count * 12 - truth_unknown_count * 8 - truth_human_review_count * 8)
    rf_keepout_correctness = max(0, 15 - keepout_crossings * 15)

    power_statuses = route_statuses_by_prefix(
        variant,
        ("/+5V_IN", "/+5V_FUSED", "/+5V_PROTECTED", "+3V3"),
    )
    power_path_logic = 15
    if any(status.startswith("BLOCKED") or status == "OPEN_REQUIRED" for status in power_statuses):
        power_path_logic = 0
    elif any(status == "PROJECTED_WARNING_LONG_PATH" for status in power_statuses):
        power_path_logic = 9

    usb_statuses = route_statuses_by_prefix(
        variant,
        ("/DM_C", "/DM_E", "/DP_C", "/DP_E", "/CC1", "/CC2", "/SHIELD"),
    )
    usb_data_path_logic = 10
    if any(status.startswith("BLOCKED") or status == "OPEN_REQUIRED" for status in usb_statuses):
        usb_data_path_logic = 0
    elif any(status == "PROJECTED_WARNING_LONG_PATH" for status in usb_statuses):
        usb_data_path_logic = 6

    component_grouping = max(0, 10 - min(10, len(overlap_pairs) * 2))
    route_feasibility = 10 if projected_open_nets_count == 0 and keepout_crossings == 0 else 0

    category_scores = {
        "mechanical_correctness": mechanical_correctness,
        "connector_truth_correctness": connector_truth_correctness,
        "rf_keepout_correctness": rf_keepout_correctness,
        "power_path_logic": power_path_logic,
        "usb_data_path_logic": usb_data_path_logic,
        "component_grouping": component_grouping,
        "route_feasibility": route_feasibility,
    }
    total_score = sum(category_scores.values())
    live_open_nets_count = int(live["unconnected_count"]) + int(live["detectable_unrouted_net_count"])

    if missing_data:
        status = "AUTO_BLOCKED_MISSING_DATA"
        blocking_reasons.append("Connector truth or projected-route evidence is missing.")
    elif hard_fail_codes:
        status = "FAIL"
    elif total_score < 80:
        status = "AUTO_BLOCKED_BAD_LAYOUT"
        blocking_reasons.append(f"Total score {total_score} is below the pass threshold 80.")
    else:
        status = "PASS"

    return {
        "project": variant["project"],
        "variant_id": variant["variant_id"],
        "status": status,
        "total_score": total_score,
        "category_scores": category_scores,
        "hard_fail_codes": hard_fail_codes,
        "blocking_reasons": blocking_reasons,
        "projected_open_nets_count": projected_open_nets_count,
        "live_open_nets_count": live_open_nets_count,
        "overlap_pairs": overlap_pairs,
        "hard_overlap_pairs": hard_overlap_pairs,
        "outside_board_refs": outside_refs,
    }


def score_markdown(score: dict[str, Any]) -> str:
    lines = [
        f"# {score['variant_id']} Score",
        "",
        f"Status: `{score['status']}`",
        f"Total score: `{score['total_score']}`",
        f"Projected open nets: `{score['projected_open_nets_count']}`",
        f"Live open nets: `{score['live_open_nets_count']}`",
        "",
        "| Category | Score |",
        "| --- | --- |",
    ]
    for key, value in score["category_scores"].items():
        lines.append(f"| `{key}` | `{value}` |")
    if score["hard_fail_codes"]:
        lines.extend(["", "## Hard Fails", ""])
        for code in score["hard_fail_codes"]:
            lines.append(f"- `{code}`")
    if score["blocking_reasons"]:
        lines.extend(["", "## Blocking Reasons", ""])
        for reason in score["blocking_reasons"]:
            lines.append(f"- {reason}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("variant_json", help="Input projected placement variant JSON file.")
    parser.add_argument("output_json", help="Output score JSON file.")
    parser.add_argument("--markdown", help="Optional Markdown output path.")
    args = parser.parse_args()

    variant = load_json(args.variant_json)
    score = score_variant(variant)
    dump_json(args.output_json, score)
    if args.markdown:
        dump_markdown(args.markdown, score_markdown(score))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
