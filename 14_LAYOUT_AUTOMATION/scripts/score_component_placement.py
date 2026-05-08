#!/usr/bin/env python3
"""Score a placement plan from collision and ordering evidence."""

from __future__ import annotations

import argparse

from _placement_common import STAGE_INDEX, dump_json, load_json


def stage_order_score(placements: list[dict]) -> int:
    last = -1
    penalties = 0
    for placement in placements:
        stage = STAGE_INDEX.get(placement.get("stage_name", ""), 99)
        if stage < last:
            penalties += 5
        last = max(last, stage)
    return max(0, 20 - penalties)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("placement_plan_json")
    parser.add_argument("collision_report_json")
    parser.add_argument("output_json")
    args = parser.parse_args()

    plan = load_json(args.placement_plan_json)
    collision_report = load_json(args.collision_report_json)
    placements = plan.get("placements", [])
    collisions = collision_report.get("collisions", [])
    edge_violations = collision_report.get("edge_clearance_violations", [])
    unplaced_refs = plan.get("unplaced_refs", [])

    grouping_score = max(0, 20 - 4 * len(unplaced_refs))
    order_score = stage_order_score(placements)
    collision_score = max(0, 30 - 10 * len(collisions) - 6 * len(edge_violations))
    accessibility_score = 20
    for placement in placements:
        stage = placement.get("stage_name")
        if stage == "TEST_PADS" and placement.get("y_mm", 0.0) < 2.0:
            accessibility_score -= 5
        if stage == "LEDS" and placement.get("group") == "USB_PATH":
            accessibility_score -= 2
    routing_feasibility_score = 10 if not collisions and len(unplaced_refs) <= 2 else 0

    total_score = max(
        0,
        min(
            100,
            grouping_score + order_score + collision_score + accessibility_score + routing_feasibility_score,
        ),
    )

    if collision_report["status"] != "PASS":
        status = "AUTO_BLOCKED_BAD_LAYOUT"
    elif total_score >= 80:
        status = "PASS"
    else:
        status = "AUTO_BLOCKED_BAD_LAYOUT"

    result = {
        "project": plan.get("project", ""),
        "status": status,
        "total_score": total_score,
        "scores": {
            "grouping_score": grouping_score,
            "stage_order_score": order_score,
            "collision_score": collision_score,
            "accessibility_score": accessibility_score,
            "routing_feasibility_score": routing_feasibility_score,
        },
        "collisions": collisions,
        "edge_clearance_violations": edge_violations,
        "unplaced_refs": unplaced_refs,
        "blocked_reasons": collisions + edge_violations + [f"{ref}: unplaced" for ref in unplaced_refs],
    }
    dump_json(args.output_json, result)
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
