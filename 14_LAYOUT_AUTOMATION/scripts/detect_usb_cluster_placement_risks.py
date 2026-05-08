#!/usr/bin/env python3
"""Detect USB cluster placement risks from a live or copied KiCad PCB."""

from __future__ import annotations

import argparse
from pathlib import Path

from _placement_common import build_live_placement_state, dump_json, dump_markdown, point_distance


def analyze_usb_cluster_placement_risks(state: dict) -> dict:
    components = state["components"]
    usb_connectors = [item for item in components if item["role"] == "USB_C"]
    if not usb_connectors:
        result = {
            "project": state["project"],
            "tool": "detect_usb_cluster_placement_risks",
            "status": "PASS",
            "score": 10,
            "hard_fail_statuses": [],
            "warnings": ["No USB-C connector found; USB cluster audit not applicable."],
            "findings": [],
        }
        return result

    connector = usb_connectors[0]
    connector_center = connector["courtyard_center"]
    usb_esd = [item for item in components if item["role"] == "ESD_USB"]
    usb_cc = [item for item in components if item["role"] == "USB_CC"]
    usb_series = [item for item in components if item["role"] == "USB_SERIES"]

    findings: list[dict] = []
    warnings: list[str] = []
    hard_fails: list[str] = []
    score = 10

    for item in usb_esd:
        gap_mm = point_distance(connector_center, item["body_center"])
        if gap_mm > 16.0:
            hard_fails.append("USB_CLUSTER_TOO_SPREAD")
            findings.append(
                {
                    "ref": item["ref"],
                    "status": "USB_CLUSTER_TOO_SPREAD",
                    "gap_mm": round(gap_mm, 3),
                    "reason": "USB ESD part is too far from the connector to protect the entry point cleanly.",
                    "recommended_fix": "Move the ESD device closer to the USB connector pads and keep the exposed stub length short.",
                }
            )
            score -= 4
    for item in usb_cc:
        gap_mm = point_distance(connector_center, item["body_center"])
        if gap_mm > 14.0:
            hard_fails.append("USB_CLUSTER_TOO_SPREAD")
            findings.append(
                {
                    "ref": item["ref"],
                    "status": "USB_CLUSTER_TOO_SPREAD",
                    "gap_mm": round(gap_mm, 3),
                    "reason": "CC pull resistor is too far from the USB connector for a compact CC cluster.",
                    "recommended_fix": "Keep CC resistors close to the connector and on short direct paths.",
                }
            )
            score -= 3
    series_distances: list[tuple[str, float]] = []
    for item in usb_series:
        gap_mm = point_distance(connector_center, item["body_center"])
        series_distances.append((item["ref"], gap_mm))
        if gap_mm > 22.0:
            hard_fails.append("USB_CLUSTER_TOO_SPREAD")
            findings.append(
                {
                    "ref": item["ref"],
                    "status": "USB_CLUSTER_TOO_SPREAD",
                    "gap_mm": round(gap_mm, 3),
                    "reason": "USB series resistor sits too far from the connector-side data entry path.",
                    "recommended_fix": "Move series parts into a tighter connector-to-ESD-to-series-to-MCU chain.",
                }
            )
            score -= 3

    if len(series_distances) == 2:
        mismatch_mm = abs(series_distances[0][1] - series_distances[1][1])
        if mismatch_mm > 4.0:
            warnings.append(f"USB series pair placement is asymmetric by {mismatch_mm:.2f} mm.")
            score -= 1

    result = {
        "project": state["project"],
        "tool": "detect_usb_cluster_placement_risks",
        "status": "PASS" if not hard_fails else "AUTO_BLOCKED_BAD_LAYOUT",
        "score": max(0, score),
        "hard_fail_statuses": sorted(set(hard_fails)),
        "warnings": warnings,
        "findings": findings,
        "connector_ref": connector["ref"],
        "series_pair_distances_mm": {ref: round(distance, 3) for ref, distance in series_distances},
    }
    return result


def render_markdown(result: dict) -> str:
    lines = [
        "# USB Cluster Placement Risks",
        "",
        f"- Project: `{result['project']}`",
        f"- Status: `{result['status']}`",
        f"- Score: `{result['score']}` / 10",
        f"- USB connector: `{result.get('connector_ref', 'n/a')}`",
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
            lines.append(f"- `{finding['ref']}` `{finding['status']}` at `{finding['gap_mm']}` mm: {finding['reason']}")
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
    result = analyze_usb_cluster_placement_risks(state)
    dump_json(args.output_json, result)
    if args.markdown:
        dump_markdown(args.markdown, render_markdown(result))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
