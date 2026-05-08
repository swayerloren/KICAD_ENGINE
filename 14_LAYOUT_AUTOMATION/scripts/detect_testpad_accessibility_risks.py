#!/usr/bin/env python3
"""Detect test-pad accessibility risks from a live or copied KiCad PCB."""

from __future__ import annotations

import argparse
from pathlib import Path

from _placement_common import (
    TEST_PAD_EDGE_DISTANCE_MM,
    TEST_PAD_ROW_SPACING_MIN_MM,
    bboxes_overlap,
    build_live_placement_state,
    dump_json,
    dump_markdown,
)


def edge_corridor(board_bbox: dict, pad: dict, half_width_mm: float = 1.1) -> dict:
    center = pad["body_center"]
    edge = pad["edge_proximity"]["edge"]
    if edge == "right":
        return {"xmin": center["x_mm"], "xmax": board_bbox["xmax"], "ymin": center["y_mm"] - half_width_mm, "ymax": center["y_mm"] + half_width_mm}
    if edge == "left":
        return {"xmin": board_bbox["xmin"], "xmax": center["x_mm"], "ymin": center["y_mm"] - half_width_mm, "ymax": center["y_mm"] + half_width_mm}
    if edge == "top":
        return {"xmin": center["x_mm"] - half_width_mm, "xmax": center["x_mm"] + half_width_mm, "ymin": board_bbox["ymin"], "ymax": center["y_mm"]}
    return {"xmin": center["x_mm"] - half_width_mm, "xmax": center["x_mm"] + half_width_mm, "ymin": center["y_mm"], "ymax": board_bbox["ymax"]}


def analyze_testpad_accessibility_risks(state: dict) -> dict:
    board_bbox = state["board"]["bbox"]
    testpads = [item for item in state["components"] if item["role"] == "TEST_PAD"]
    non_testpads = [item for item in state["components"] if item["role"] != "TEST_PAD"]
    findings: list[dict] = []
    warnings: list[str] = []
    hard_fails: list[str] = []
    score = 10

    if not testpads:
        return {
            "project": state["project"],
            "tool": "detect_testpad_accessibility_risks",
            "status": "PASS",
            "score": score,
            "hard_fail_statuses": [],
            "warnings": ["No test pads found; accessibility audit not applicable."],
            "findings": [],
        }

    edges = {str(item["edge_proximity"]["edge"]) for item in testpads}
    if len(edges) > 1:
        warnings.append("Test pads are split across multiple board edges.")
        score -= 2

    for pad in testpads:
        edge = str(pad["edge_proximity"]["edge"])
        distance_mm = float(pad["edge_proximity"]["distance_mm"])
        if distance_mm > TEST_PAD_EDGE_DISTANCE_MM:
            hard_fails.append("TEST_PADS_INACCESSIBLE")
            findings.append(
                {
                    "ref": pad["ref"],
                    "status": "TEST_PADS_INACCESSIBLE",
                    "edge": edge,
                    "reason": f"Test pad sits {distance_mm:.2f} mm from its nearest board edge, beyond the accessibility threshold.",
                    "recommended_fix": "Move the test pad closer to an accessible board edge or group it into a reachable probe row.",
                }
            )
            score -= 4
            continue

        corridor = edge_corridor(board_bbox, pad)
        blockers = [item["ref"] for item in non_testpads if bboxes_overlap(item["body_bbox"], corridor)]
        if blockers:
            hard_fails.append("TEST_PADS_INACCESSIBLE")
            findings.append(
                {
                    "ref": pad["ref"],
                    "status": "TEST_PADS_INACCESSIBLE",
                    "edge": edge,
                    "reason": f"Probe corridor to the board edge is blocked by {', '.join(blockers)}.",
                    "recommended_fix": "Clear the corridor between the test pad and the nearest board edge or move the pad to a cleaner edge row.",
                }
            )
            score -= 4

    right_edge = [item for item in testpads if str(item["edge_proximity"]["edge"]) == "right"]
    if len(right_edge) >= 2:
        ordered = sorted(right_edge, key=lambda item: float(item["body_center"]["y_mm"]))
        for left, right in zip(ordered, ordered[1:]):
            spacing_mm = abs(float(right["body_center"]["y_mm"]) - float(left["body_center"]["y_mm"]))
            if spacing_mm < TEST_PAD_ROW_SPACING_MIN_MM:
                warnings.append(f"Test pad spacing between {left['ref']} and {right['ref']} is only {spacing_mm:.2f} mm.")
                score -= 1

    result = {
        "project": state["project"],
        "tool": "detect_testpad_accessibility_risks",
        "status": "PASS" if not hard_fails else "AUTO_BLOCKED_BAD_LAYOUT",
        "score": max(0, score),
        "hard_fail_statuses": sorted(set(hard_fails)),
        "warnings": warnings,
        "findings": findings,
        "testpad_count": len(testpads),
    }
    return result


def render_markdown(result: dict) -> str:
    lines = [
        "# Test Pad Accessibility Risks",
        "",
        f"- Project: `{result['project']}`",
        f"- Status: `{result['status']}`",
        f"- Score: `{result['score']}` / 10",
        f"- Test pads reviewed: `{result['testpad_count']}`",
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
            lines.append(f"- `{finding['ref']}` `{finding['status']}` on `{finding['edge']}`: {finding['reason']}")
            lines.append(f"  - Recommended fix: {finding['recommended_fix']}")
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
    result = analyze_testpad_accessibility_risks(state)
    dump_json(args.output_json, result)
    if args.markdown:
        dump_markdown(args.markdown, render_markdown(result))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
