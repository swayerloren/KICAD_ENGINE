#!/usr/bin/env python3
"""Detect overlap, edge-clearance, and keepout violations in a placement plan."""

from __future__ import annotations

import argparse

from _placement_common import bbox_inside_board, bboxes_overlap, dump_json, load_json


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("placement_plan_json")
    parser.add_argument("output_json")
    args = parser.parse_args()

    plan = load_json(args.placement_plan_json)
    board = plan["board"]
    width = float(board["width_mm"])
    height = float(board["height_mm"])
    clearance = float(board["edge_clearance_mm"])
    placements = plan.get("placements", [])
    collisions: list[str] = []
    edge_violations: list[str] = []

    for index, left in enumerate(placements):
        bbox = left.get("bbox")
        if bbox and not bbox_inside_board(bbox, width, height, clearance):
            edge_violations.append(f"{left['ref']}: board-edge clearance violation")
        for right in placements[index + 1 :]:
            if left.get("bbox") and right.get("bbox") and bboxes_overlap(left["bbox"], right["bbox"]):
                collisions.append(f"{left['ref']} overlaps {right['ref']}")
            if left.get("keepout_bbox") and right.get("bbox") and bboxes_overlap(left["keepout_bbox"], right["bbox"]):
                collisions.append(f"{right['ref']} intrudes keepout of {left['ref']}")
            if right.get("keepout_bbox") and left.get("bbox") and bboxes_overlap(right["keepout_bbox"], left["bbox"]):
                collisions.append(f"{left['ref']} intrudes keepout of {right['ref']}")

    result = {
        "project": plan.get("project", ""),
        "status": "PASS" if not collisions and not edge_violations else "AUTO_BLOCKED_BAD_LAYOUT",
        "collisions": collisions,
        "edge_clearance_violations": edge_violations,
        "placement_count": len(placements),
    }
    dump_json(args.output_json, result)
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
