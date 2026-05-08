#!/usr/bin/env python3
"""Detect ESP32 antenna-keepout placement risks from a live or copied KiCad PCB."""

from __future__ import annotations

import argparse
from pathlib import Path

from _placement_common import (
    bbox_center,
    bboxes_overlap,
    build_live_placement_state,
    dump_json,
    dump_markdown,
    segment_intersects_bbox,
)


def analyze_antenna_keepout_placement_risks(state: dict) -> dict:
    rf_modules = [item for item in state["components"] if item["role"] == "RF_MODULE"]
    findings: list[dict] = []
    warnings: list[str] = []
    hard_fails: list[str] = []
    score = 15

    if not rf_modules:
        return {
            "project": state["project"],
            "tool": "detect_antenna_keepout_placement_risks",
            "status": "PASS",
            "score": score,
            "hard_fail_statuses": [],
            "warnings": ["No RF module found; antenna keepout audit not applicable."],
            "findings": [],
        }

    rf_module = rf_modules[0]
    antenna = rf_module.get("antenna_keepout")
    if not antenna or antenna.get("status") != "INFERRED":
        warnings.append("RF module exists but antenna keepout could not be inferred from live footprint geometry.")
        return {
            "project": state["project"],
            "tool": "detect_antenna_keepout_placement_risks",
            "status": "PASS",
            "score": 8,
            "hard_fail_statuses": [],
            "warnings": warnings,
            "findings": [],
            "rf_module_ref": rf_module["ref"],
        }

    keepout_bbox = antenna["bbox"]

    for component in state["components"]:
        if component["ref"] == rf_module["ref"]:
            continue
        if bboxes_overlap(component["body_bbox"], keepout_bbox):
            hard_fails.append("ESP32_ANTENNA_KEEPOUT_BLOCKED")
            findings.append(
                {
                    "ref": component["ref"],
                    "status": "ESP32_ANTENNA_KEEPOUT_BLOCKED",
                    "layer": component["side"],
                    "coordinates": bbox_center(component["body_bbox"]),
                    "reason": "Component body intrudes the inferred ESP32 antenna keepout region.",
                    "recommended_fix": "Move the intruding component away from the antenna zone and keep the antenna-side board area open.",
                }
            )
            score -= 8

    for track in state["tracks"]:
        if segment_intersects_bbox(track["start_mm"], track["end_mm"], keepout_bbox):
            hard_fails.append("ESP32_ANTENNA_KEEPOUT_BLOCKED")
            findings.append(
                {
                    "ref": track["net"],
                    "status": "ESP32_ANTENNA_KEEPOUT_BLOCKED",
                    "layer": track["layer"],
                    "coordinates": track["start_mm"],
                    "reason": "Trace geometry crosses the inferred ESP32 antenna keepout region.",
                    "recommended_fix": "Keep all routed copper out of the inferred antenna keepout region.",
                }
            )
            score -= 4

    for via in state["vias"]:
        point_bbox = {
            "xmin": float(via["x_mm"]),
            "xmax": float(via["x_mm"]),
            "ymin": float(via["y_mm"]),
            "ymax": float(via["y_mm"]),
        }
        if bboxes_overlap(point_bbox, keepout_bbox):
            hard_fails.append("ESP32_ANTENNA_KEEPOUT_BLOCKED")
            findings.append(
                {
                    "ref": via["net"],
                    "status": "ESP32_ANTENNA_KEEPOUT_BLOCKED",
                    "layer": "VIA",
                    "coordinates": {"x_mm": via["x_mm"], "y_mm": via["y_mm"]},
                    "reason": "Via sits inside the inferred ESP32 antenna keepout region.",
                    "recommended_fix": "Move the via outside the antenna keepout region.",
                }
            )
            score -= 3

    result = {
        "project": state["project"],
        "tool": "detect_antenna_keepout_placement_risks",
        "status": "PASS" if not hard_fails else "AUTO_BLOCKED_BAD_LAYOUT",
        "score": max(0, score),
        "rf_module_ref": rf_module["ref"],
        "keepout_side": antenna["side"],
        "keepout_depth_mm": antenna["depth_mm"],
        "hard_fail_statuses": sorted(set(hard_fails)),
        "warnings": warnings,
        "findings": findings,
    }
    return result


def render_markdown(result: dict) -> str:
    lines = [
        "# Antenna Keepout Placement Risks",
        "",
        f"- Project: `{result['project']}`",
        f"- Status: `{result['status']}`",
        f"- Score: `{result['score']}` / 15",
        f"- RF module: `{result.get('rf_module_ref', 'n/a')}`",
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
            lines.append(f"- `{finding['ref']}` `{finding['status']}` on `{finding['layer']}`: {finding['reason']}")
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
    result = analyze_antenna_keepout_placement_risks(state)
    dump_json(args.output_json, result)
    if args.markdown:
        dump_markdown(args.markdown, render_markdown(result))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
