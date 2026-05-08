#!/usr/bin/env python3
"""Detect power-path placement risks from a live or copied KiCad PCB."""

from __future__ import annotations

import argparse
from pathlib import Path

from _placement_common import build_live_placement_state, dump_json, dump_markdown, point_distance


POWER_NETS = {"/+5V_IN", "/+5V_FUSED", "/+5V_PROTECTED", "/BUCK_BST", "/BUCK_SW", "+3V3", "3V3"}


def center_of_group(components: list[dict]) -> dict[str, float]:
    count = max(1, len(components))
    return {
        "x_mm": round(sum(float(item["x_mm"]) for item in components) / count, 6),
        "y_mm": round(sum(float(item["y_mm"]) for item in components) / count, 6),
    }


def has_power_net(component: dict) -> bool:
    nets = {str(item).upper() for item in component.get("pad_nets", [])}
    return bool(nets & POWER_NETS)


def stage_components(state: dict) -> dict[str, list[dict]]:
    components = state["components"]
    return {
        "input_connector": [item for item in components if item["role"] in {"BARREL_JACK", "EDGE_CONNECTOR"} and has_power_net(item)],
        "fuse": [item for item in components if item["role"] == "FUSE"],
        "protection_cluster": [
            item
            for item in components
            if item["role"] in {"PMOS_PROTECTION", "TVS", "INPUT_CAP"} and has_power_net(item)
        ],
        "regulator": [item for item in components if item["role"] == "REGULATOR"],
        "output_cluster": [item for item in components if item["role"] in {"INDUCTOR", "OUTPUT_CAP"}],
    }


def analyze_power_path_placement_risks(state: dict) -> dict:
    stages = stage_components(state)
    present = [name for name, items in stages.items() if items]
    findings: list[dict] = []
    warnings: list[str] = []
    hard_fails: list[str] = []
    score = 15

    if len(present) < 4:
        warnings.append("Power-path staging is incomplete; not enough identifiable components were found for a full adjacency audit.")
        score -= 5

    centroids = {name: center_of_group(items) for name, items in stages.items() if items}
    stage_order = ["input_connector", "fuse", "protection_cluster", "regulator", "output_cluster"]
    thresholds = {
        ("input_connector", "fuse"): 15.0,
        ("fuse", "protection_cluster"): 18.0,
        ("protection_cluster", "regulator"): 18.0,
        ("regulator", "output_cluster"): 18.0,
    }

    input_center = centroids.get("input_connector")
    output_center = centroids.get("output_cluster")
    axis = None
    direction = None
    if input_center and output_center:
        dx = abs(float(output_center["x_mm"]) - float(input_center["x_mm"]))
        dy = abs(float(output_center["y_mm"]) - float(input_center["y_mm"]))
        axis = "y" if dy >= dx else "x"
        direction = 1 if float(output_center[f"{axis}_mm"]) > float(input_center[f"{axis}_mm"]) else -1

    previous_name = None
    previous_center = None
    for name in stage_order:
        current_center = centroids.get(name)
        if not current_center:
            continue
        if previous_name and previous_center:
            gap_mm = point_distance(previous_center, current_center)
            threshold = thresholds.get((previous_name, name), 18.0)
            if gap_mm > threshold:
                hard_fails.append("POWER_PATH_SCATTERED_BEYOND_THRESHOLD")
                findings.append(
                    {
                        "status": "POWER_PATH_SCATTERED_BEYOND_THRESHOLD",
                        "from_stage": previous_name,
                        "to_stage": name,
                        "gap_mm": round(gap_mm, 3),
                        "reason": f"Power path stage gap exceeds {threshold:.1f} mm.",
                        "recommended_fix": "Compress the input-to-regulator path so current flows through adjacent parts without long cross-board detours.",
                    }
                )
                score -= 6
            elif gap_mm > threshold * 0.75:
                warnings.append(f"{previous_name} -> {name} spacing is looser than preferred ({gap_mm:.2f} mm).")
                score -= 2
            if axis and direction is not None:
                previous_axis = float(previous_center[f"{axis}_mm"])
                current_axis = float(current_center[f"{axis}_mm"])
                delta = current_axis - previous_axis
                if delta * direction < -2.0:
                    hard_fails.append("POWER_PATH_SCATTERED_BEYOND_THRESHOLD")
                    findings.append(
                        {
                            "status": "POWER_PATH_SCATTERED_BEYOND_THRESHOLD",
                            "from_stage": previous_name,
                            "to_stage": name,
                            "gap_mm": round(gap_mm, 3),
                            "reason": "Power path stages reverse direction along the dominant board axis, creating a scattered current-flow order.",
                            "recommended_fix": "Reorder the fuse, protection, and regulator cluster so current flow is monotonic from connector to output stage.",
                        }
                    )
                    score -= 6
        previous_name = name
        previous_center = current_center

    result = {
        "project": state["project"],
        "tool": "detect_power_path_placement_risks",
        "status": "PASS" if not hard_fails else "AUTO_BLOCKED_BAD_LAYOUT",
        "score": max(0, score),
        "stages_present": present,
        "hard_fail_statuses": sorted(set(hard_fails)),
        "warnings": warnings,
        "findings": findings,
        "stage_centroids": centroids,
    }
    return result


def render_markdown(result: dict) -> str:
    lines = [
        "# Power Path Placement Risks",
        "",
        f"- Project: `{result['project']}`",
        f"- Status: `{result['status']}`",
        f"- Score: `{result['score']}` / 15",
        f"- Stages present: `{', '.join(result['stages_present']) or 'none'}`",
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
            lines.append(
                f"- `{finding['status']}` `{finding['from_stage']}` -> `{finding['to_stage']}` gap `{finding['gap_mm']}` mm: {finding['reason']}"
            )
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
    result = analyze_power_path_placement_risks(state)
    dump_json(args.output_json, result)
    if args.markdown:
        dump_markdown(args.markdown, render_markdown(result))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
