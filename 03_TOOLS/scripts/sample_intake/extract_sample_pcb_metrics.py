#!/usr/bin/env python3
"""Extract read-only PCB reference metrics from a KiCad sample board."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any

from sample_intake_common import first_pcb, repo_rel, slugify, utc_now_iso, write_json, write_markdown


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
PCB_GEOMETRY_DIR = REPO_ROOT / "03_TOOLS" / "scripts" / "pcb_geometry"
if str(PCB_GEOMETRY_DIR) not in sys.path:
    sys.path.insert(0, str(PCB_GEOMETRY_DIR))

from _pcb_geometry_common import (  # type: ignore  # noqa: E402
    aggregate_trace_quality_findings,
    build_geometry_payload,
    power_loop_findings,
    usb_pair_findings,
)


def distance_to_edge(component: dict[str, Any], outline: dict[str, Any]) -> float | None:
    if not outline or "xmin" not in outline:
        return None
    x_mm = float(component.get("x_mm", 0.0))
    y_mm = float(component.get("y_mm", 0.0))
    distances = [
        abs(x_mm - float(outline["xmin"])),
        abs(float(outline["xmax"]) - x_mm),
        abs(y_mm - float(outline["ymin"])),
        abs(float(outline["ymax"]) - y_mm),
    ]
    return round(min(distances), 3)


def connector_components(payload: dict[str, Any]) -> list[dict[str, Any]]:
    connectors: list[dict[str, Any]] = []
    for component in payload.get("components", []):
        ref = str(component.get("ref", "")).upper()
        text = " ".join(
            [
                ref,
                str(component.get("value", "")),
                str(component.get("kind", "")),
                str(component.get("footprint_name", "")),
            ]
        ).lower()
        if ref.startswith("J") or any(token in text for token in ("usb", "connector", "barrel", "jack", "header")):
            connectors.append(component)
    return connectors


def connector_edge_summary(payload: dict[str, Any]) -> dict[str, Any]:
    outline = payload.get("board_outline", {})
    connectors = connector_components(payload)
    details: list[dict[str, Any]] = []
    edge_aligned = 0
    for component in connectors:
        edge_distance = distance_to_edge(component, outline)
        aligned = edge_distance is not None and edge_distance <= 2.5
        if aligned:
            edge_aligned += 1
        details.append(
            {
                "reference": component.get("ref", ""),
                "value": component.get("value", ""),
                "footprint_name": component.get("footprint_name", ""),
                "distance_to_edge_mm": edge_distance,
                "edge_aligned": aligned,
            }
        )
    return {
        "connector_count": len(connectors),
        "edge_aligned_count": edge_aligned,
        "details": details,
    }


def zone_usage_summary(payload: dict[str, Any]) -> dict[str, Any]:
    zones = payload.get("zones", [])
    gnd_zones = [zone for zone in zones if str(zone.get("net", "")).upper() == "GND"]
    return {
        "zone_count": len(zones),
        "gnd_zone_count": len(gnd_zones),
        "ground_strategy": payload.get("ground_strategy", {}).get("strategy", "NOT_EXTRACTED"),
    }


def clustering_summary(payload: dict[str, Any]) -> dict[str, Any]:
    counts = Counter()
    for component in payload.get("components", []):
        ref = str(component.get("ref", "")).upper()
        text = " ".join(
            [
                ref,
                str(component.get("value", "")),
                str(component.get("kind", "")),
                str(component.get("footprint_name", "")),
            ]
        ).lower()
        if ref.startswith("J") or "usb" in text or "jack" in text:
            counts["connectors"] += 1
        elif "esp32" in text or "module" in text or ref.startswith("U"):
            counts["logic_or_modules"] += 1
        elif any(token in text for token in ("regulator", "buck", "inductor", "pmos", "fuse", "tvs")):
            counts["power_cluster"] += 1
        elif ref.startswith("TP"):
            counts["test_points"] += 1
        elif ref.startswith("MH"):
            counts["mechanical"] += 1
        elif ref.startswith("D") or "led" in text:
            counts["leds"] += 1
        else:
            counts["other"] += 1
    return dict(counts)


def drc_summary(pcb_path: Path, run_drc_check: bool) -> dict[str, Any]:
    if not run_drc_check:
        return {"status": "NOT_RUN", "violations": None, "unconnected_items": None, "message": "DRC was not requested."}
    with tempfile.TemporaryDirectory(prefix="sample_pcb_drc_") as temp_dir:
        output_path = Path(temp_dir) / "sample_drc.json"
        completed = subprocess.run(
            ["kicad-cli", "pcb", "drc", "--format", "json", "--output", str(output_path), str(pcb_path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        if completed.returncode != 0:
            return {
                "status": "FAIL",
                "violations": None,
                "unconnected_items": None,
                "message": (completed.stderr or completed.stdout).strip(),
            }
        payload = json.loads(output_path.read_text(encoding="utf-8", errors="replace")) if output_path.exists() else {}
        violations = len(payload.get("violations", []))
        unconnected = len(payload.get("unconnected_items", []))
        status = "PASS" if violations == 0 and unconnected == 0 else "FAIL"
        return {
            "status": status,
            "violations": violations,
            "unconnected_items": unconnected,
            "message": "DRC JSON parsed.",
        }


def extract_metrics(pcb_path: Path, run_drc_check: bool = False) -> dict[str, Any]:
    payload = build_geometry_payload(pcb_path)
    outline = payload.get("board_outline", {})
    all_trace_findings = aggregate_trace_quality_findings(payload)
    angle_counts = Counter(item.get("status", "") for item in all_trace_findings)
    usb_findings = usb_pair_findings(payload)
    power_findings = power_loop_findings(payload)
    return {
        "schema_version": "1.0",
        "tool": "extract_sample_pcb_metrics",
        "status": "METRICS_EXTRACTED",
        "generated_at": utc_now_iso(),
        "read_only_mode": True,
        "sample_id": slugify(pcb_path.parent.name),
        "pcb_path": str(pcb_path),
        "metrics": {
            "board_size_mm": {
                "width_mm": outline.get("width_mm"),
                "height_mm": outline.get("height_mm"),
            },
            "footprint_count": len(payload.get("components", [])),
            "mounting_hole_count": sum(1 for item in payload.get("components", []) if item.get("mounting_hole")),
            "connector_edge_placement": connector_edge_summary(payload),
            "routing_angle_patterns": dict(angle_counts),
            "zone_usage": zone_usage_summary(payload),
            "via_count": payload.get("summary", {}).get("via_count", 0),
            "drc_result": drc_summary(pcb_path, run_drc_check),
            "component_clustering": clustering_summary(payload),
            "usb_routing_quality": {
                "status": "PASS" if not usb_findings else "FAIL",
                "finding_count": len(usb_findings),
            },
            "power_layout_quality": {
                "status": "PASS" if not power_findings else "FAIL",
                "finding_count": len(power_findings),
            },
            "routing_status": payload.get("routing_status", {}),
        },
    }


def markdown(metrics: dict[str, Any]) -> str:
    details = metrics["metrics"]
    connector = details["connector_edge_placement"]
    drc = details["drc_result"]
    return "\n".join(
        [
            "# Sample PCB Metrics",
            "",
            f"Status: `{metrics['status']}`",
            f"PCB: `{metrics['pcb_path']}`",
            "",
            "## Summary",
            "",
            f"- board_width_mm: `{details['board_size_mm']['width_mm']}`",
            f"- board_height_mm: `{details['board_size_mm']['height_mm']}`",
            f"- footprint_count: `{details['footprint_count']}`",
            f"- mounting_hole_count: `{details['mounting_hole_count']}`",
            f"- connector_count: `{connector['connector_count']}`",
            f"- edge_aligned_connectors: `{connector['edge_aligned_count']}`",
            f"- via_count: `{details['via_count']}`",
            f"- drc_status: `{drc['status']}`",
            f"- usb_routing_quality: `{details['usb_routing_quality']['status']}`",
            f"- power_layout_quality: `{details['power_layout_quality']['status']}`",
            "",
            "## Routing Angle Patterns",
            "",
        ]
        + [f"- {name}: `{count}`" for name, count in sorted(details["routing_angle_patterns"].items())]
        + [
            "",
            "## Component Clustering",
            "",
        ]
        + [f"- {name}: `{count}`" for name, count in sorted(details["component_clustering"].items())]
        + [
            "",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract read-only PCB metrics from a KiCad sample board.")
    parser.add_argument("--sample-path", type=Path, help="Sample folder containing a .kicad_pcb file.")
    parser.add_argument("--pcb", type=Path, help="Direct path to a .kicad_pcb file.")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--run-drc", action="store_true")
    args = parser.parse_args()

    if not args.sample_path and not args.pcb:
        raise SystemExit("Provide --sample-path or --pcb.")
    pcb_path = args.pcb.resolve() if args.pcb else first_pcb(args.sample_path.resolve())
    metrics = extract_metrics(pcb_path, run_drc_check=args.run_drc)

    if args.json_output:
        write_json(args.json_output, metrics)
    if args.output:
        write_markdown(args.output, markdown(metrics))
        print(f"Wrote PCB metrics: {repo_rel(args.output)}")
    elif not args.json_output:
        print(json.dumps(metrics, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
