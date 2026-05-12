#!/usr/bin/env python3
"""Build a reference-style index from controlled open-source KiCad samples."""

from __future__ import annotations

import argparse
from pathlib import Path
from statistics import mean
from typing import Any

from extract_sample_pcb_metrics import extract_metrics as extract_pcb_metrics
from extract_sample_schematic_metrics import extract_metrics as extract_schematic_metrics
from sample_intake_common import (
    REFERENCE_ROOT,
    REVIEW_ROOT,
    collect_kicad_file_summary,
    discover_sample_directories,
    first_pcb,
    first_schematic,
    preferred_sample_path,
    repo_rel,
    utc_now_iso,
    write_json,
    write_markdown,
)


def sample_record(sample_id: str, sample_path: Path, source_kind: str, run_erc: bool, run_drc: bool) -> dict[str, Any]:
    summary = collect_kicad_file_summary(sample_path)
    schematic_metrics = None
    pcb_metrics = None
    schematic_error = ""
    pcb_error = ""

    if summary["kicad_sch_count"]:
        try:
            schematic_metrics = extract_schematic_metrics(first_schematic(sample_path), run_erc_check=run_erc)
        except Exception as exc:  # pragma: no cover - defensive dry-run reporting
            schematic_error = str(exc)
    if summary["kicad_pcb_count"]:
        try:
            pcb_metrics = extract_pcb_metrics(first_pcb(sample_path), run_drc_check=run_drc)
        except Exception as exc:  # pragma: no cover - defensive dry-run reporting
            pcb_error = str(exc)

    return {
        "sample_id": sample_id,
        "source_kind": source_kind,
        "sample_path": str(sample_path),
        "kicad_file_summary": summary,
        "schematic_metrics": schematic_metrics,
        "schematic_error": schematic_error,
        "pcb_metrics": pcb_metrics,
        "pcb_error": pcb_error,
    }


def aggregate(records: list[dict[str, Any]]) -> dict[str, Any]:
    wire_label_ratios = [
        record["schematic_metrics"]["metrics"]["wire_to_label_ratio"]
        for record in records
        if record.get("schematic_metrics")
        and record["schematic_metrics"]["metrics"].get("wire_to_label_ratio") is not None
    ]
    board_widths = [
        record["pcb_metrics"]["metrics"]["board_size_mm"]["width_mm"]
        for record in records
        if record.get("pcb_metrics") and record["pcb_metrics"]["metrics"]["board_size_mm"].get("width_mm") is not None
    ]
    board_heights = [
        record["pcb_metrics"]["metrics"]["board_size_mm"]["height_mm"]
        for record in records
        if record.get("pcb_metrics") and record["pcb_metrics"]["metrics"]["board_size_mm"].get("height_mm") is not None
    ]
    edge_alignment_rates = [
        (
            record["pcb_metrics"]["metrics"]["connector_edge_placement"]["edge_aligned_count"]
            / record["pcb_metrics"]["metrics"]["connector_edge_placement"]["connector_count"]
        )
        for record in records
        if record.get("pcb_metrics")
        and record["pcb_metrics"]["metrics"]["connector_edge_placement"]["connector_count"] > 0
    ]
    return {
        "sample_count": len(records),
        "schematic_metric_count": sum(1 for record in records if record.get("schematic_metrics")),
        "pcb_metric_count": sum(1 for record in records if record.get("pcb_metrics")),
        "average_wire_to_label_ratio": round(mean(wire_label_ratios), 3) if wire_label_ratios else None,
        "average_board_width_mm": round(mean(board_widths), 3) if board_widths else None,
        "average_board_height_mm": round(mean(board_heights), 3) if board_heights else None,
        "average_connector_edge_alignment_rate": round(mean(edge_alignment_rates), 3) if edge_alignment_rates else None,
    }


def markdown(index: dict[str, Any]) -> str:
    rows: list[str] = []
    for record in index["samples"]:
        schematic_status = (
            record["schematic_metrics"]["metrics"]["annotation_completeness"]["status"]
            if record.get("schematic_metrics")
            else "NOT_PRESENT"
        )
        pcb_status = (
            record["pcb_metrics"]["metrics"]["usb_routing_quality"]["status"]
            if record.get("pcb_metrics")
            else "NOT_PRESENT"
        )
        rows.append(
            f"| `{record['sample_id']}` | `{record['source_kind']}` | `{record['kicad_file_summary']['kicad_sch_count']}` | `{record['kicad_file_summary']['kicad_pcb_count']}` | `{schematic_status}` | `{pcb_status}` |"
        )
    lines = [
        "# Reference Style Index",
        "",
        f"Status: `{index['status']}`",
        f"Generated: `{index['generated_at']}`",
        "",
        "## Aggregate Metrics",
        "",
        f"- sample_count: `{index['aggregate']['sample_count']}`",
        f"- schematic_metric_count: `{index['aggregate']['schematic_metric_count']}`",
        f"- pcb_metric_count: `{index['aggregate']['pcb_metric_count']}`",
        f"- average_wire_to_label_ratio: `{index['aggregate']['average_wire_to_label_ratio']}`",
        f"- average_board_width_mm: `{index['aggregate']['average_board_width_mm']}`",
        f"- average_board_height_mm: `{index['aggregate']['average_board_height_mm']}`",
        f"- average_connector_edge_alignment_rate: `{index['aggregate']['average_connector_edge_alignment_rate']}`",
        "",
        "## Sample Coverage",
        "",
        "| sample_id | source_kind | schematic_count | pcb_count | schematic_annotation_status | pcb_usb_status |",
        "| --- | --- | ---: | ---: | --- | --- |",
    ]
    lines.extend(rows or ["| `_none_` | `missing` | `0` | `0` | `NOT_PRESENT` | `NOT_PRESENT` |"])
    lines.extend(
        [
            "",
            "## Use Rule",
            "",
            "Use this index to compare generated work against reviewed human-made examples. Do not treat the sample corpus as automatic correctness proof.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a reference-style index from controlled sample projects.")
    parser.add_argument("--apply", action="store_true", help="Write outputs under 07_REFERENCE_DESIGNS.")
    parser.add_argument("--run-erc", action="store_true")
    parser.add_argument("--run-drc", action="store_true")
    args = parser.parse_args()

    discovered = discover_sample_directories()
    samples: list[dict[str, Any]] = []
    for sample_id, slots in sorted(discovered.items()):
        sample_path, source_kind = preferred_sample_path(slots)
        if not sample_path:
            continue
        samples.append(sample_record(sample_id, sample_path, source_kind, run_erc=args.run_erc, run_drc=args.run_drc))

    index = {
        "schema_version": "1.0",
        "tool": "build_reference_style_index",
        "status": "REFERENCE_STYLE_INDEX_WRITTEN" if args.apply else "REFERENCE_STYLE_INDEX_DRY_RUN",
        "generated_at": utc_now_iso(),
        "read_only_mode": not args.apply,
        "samples": samples,
        "aggregate": aggregate(samples),
    }

    if args.apply:
        json_path = REFERENCE_ROOT / "REFERENCE_STYLE_INDEX.generated.json"
        md_path = REFERENCE_ROOT / "REFERENCE_STYLE_INDEX.generated.md"
    else:
        json_path = REVIEW_ROOT / "reference_style_index_dry_run.json"
        md_path = REVIEW_ROOT / "reference_style_index_dry_run.md"
    write_json(json_path, index)
    write_markdown(md_path, markdown(index))
    print(f"Wrote reference style index: {repo_rel(md_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
