#!/usr/bin/env python3
"""Extract readability-oriented metrics from a KiCad sample schematic."""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any

from sample_intake_common import first_schematic, repo_rel, slugify, utc_now_iso, write_json, write_markdown


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
SCHEMATIC_QUALITY_DIR = REPO_ROOT / "03_TOOLS" / "scripts" / "schematic_quality"
if str(SCHEMATIC_QUALITY_DIR) not in sys.path:
    sys.path.insert(0, str(SCHEMATIC_QUALITY_DIR))

from schematic_quality_common import (  # type: ignore  # noqa: E402
    assign_blocks,
    extract_symbols,
    extract_text_items,
    extract_wire_segments,
    find_project_schematic,
    heading_positions,
    is_physical_symbol,
    line_box_with_margin,
    load_schematic,
    rects_overlap,
    run_erc,
    walk_lists,
)


def count_sheet_references(root: list[Any]) -> int:
    return 1 + sum(1 for node in walk_lists(root) if isinstance(node, list) and node and node[0] == "sheet")


def annotation_summary(symbols: list[dict[str, Any]]) -> dict[str, Any]:
    references = [str(symbol.get("reference", "")).strip() for symbol in symbols if is_physical_symbol(symbol)]
    unresolved = [ref for ref in references if not ref or "?" in ref]
    duplicates = sorted(ref for ref, count in Counter(ref for ref in references if ref).items() if count > 1)
    status = "PASS" if not unresolved and not duplicates else "FAIL"
    return {
        "status": status,
        "unresolved_reference_count": len(unresolved),
        "duplicate_reference_count": len(duplicates),
        "duplicate_references": duplicates,
    }


def footprint_summary(symbols: list[dict[str, Any]]) -> dict[str, Any]:
    physical = [symbol for symbol in symbols if is_physical_symbol(symbol)]
    missing = [str(symbol.get("reference", "")) for symbol in physical if not str(symbol.get("footprint", "")).strip()]
    return {
        "status": "PASS" if not missing else "FAIL",
        "missing_footprint_count": len(missing),
        "missing_footprint_references": missing[:50],
    }


def overlap_summary(text_items: list[dict[str, Any]], symbols: list[dict[str, Any]], wires: list[dict[str, Any]]) -> dict[str, Any]:
    overlapping_items: list[dict[str, Any]] = []
    for item in text_items:
        bbox = item.get("bbox", {})
        if not bbox:
            continue
        symbol_hits = [str(symbol.get("reference", "")) for symbol in symbols if rects_overlap(bbox, symbol.get("bbox", {}))]
        wire_hits = sum(1 for wire in wires if rects_overlap(bbox, line_box_with_margin(wire, margin=0.2)))
        if symbol_hits or wire_hits:
            overlapping_items.append(
                {
                    "kind": item.get("kind", ""),
                    "text": item.get("text", ""),
                    "owner_reference": item.get("owner_reference", ""),
                    "symbol_hits": symbol_hits[:10],
                    "wire_hits": wire_hits,
                }
            )
    return {
        "status": "PASS" if not overlapping_items else "FAIL",
        "overlap_count": len(overlapping_items),
        "overlapping_items": overlapping_items[:50],
    }


def erc_summary(schematic_path: Path, run_erc_check: bool) -> dict[str, Any]:
    if not run_erc_check:
        return {"status": "NOT_RUN", "message": "ERC was not requested for this metrics extraction."}
    with tempfile.TemporaryDirectory(prefix="sample_sch_erc_") as temp_dir:
        erc_path = Path(temp_dir) / "sample_erc.rpt"
        result = run_erc(schematic_path, erc_path)
        result["evidence"] = result.get("evidence", "")
        return result


def extract_metrics(schematic_path: Path, run_erc_check: bool = False) -> dict[str, Any]:
    root = load_schematic(schematic_path)
    symbols = extract_symbols(root)
    text_items = extract_text_items(root, symbols)
    wires = extract_wire_segments(root)
    headings = heading_positions(text_items)
    blocks, unassigned = assign_blocks(symbols, headings)
    label_count = sum(1 for item in text_items if str(item.get("kind", "")).endswith("label"))
    wire_count = len(wires)
    wire_to_label_ratio = round(wire_count / label_count, 3) if label_count else None
    block_summary = [
        {
            "block_id": block_id,
            "title": block["title"],
            "heading_text": block.get("heading_text", ""),
            "symbol_count": block.get("symbol_count", 0),
        }
        for block_id, block in blocks.items()
    ]
    return {
        "schema_version": "1.0",
        "tool": "extract_sample_schematic_metrics",
        "status": "METRICS_EXTRACTED",
        "generated_at": utc_now_iso(),
        "read_only_mode": True,
        "sample_id": slugify(schematic_path.parent.name),
        "schematic_path": str(schematic_path),
        "metrics": {
            "sheet_count": count_sheet_references(root),
            "symbol_count": len(symbols),
            "physical_symbol_count": sum(1 for symbol in symbols if is_physical_symbol(symbol)),
            "wire_count": wire_count,
            "label_count": label_count,
            "wire_to_label_ratio": wire_to_label_ratio,
            "block_titles": [item.get("text", "") for item in headings.values()],
            "annotation_completeness": annotation_summary(symbols),
            "footprint_completeness": footprint_summary(symbols),
            "erc_result": erc_summary(schematic_path, run_erc_check),
            "visual_overlap_estimate": overlap_summary(text_items, symbols, wires),
        },
        "block_summary": block_summary,
        "unassigned_symbol_count": len(unassigned),
    }


def markdown(metrics: dict[str, Any]) -> str:
    details = metrics["metrics"]
    annotation = details["annotation_completeness"]
    footprint = details["footprint_completeness"]
    overlap = details["visual_overlap_estimate"]
    erc = details["erc_result"]
    block_rows = [
        [item["block_id"], item["title"], item["symbol_count"], item["heading_text"]]
        for item in metrics.get("block_summary", [])
        if item.get("symbol_count") or item.get("heading_text")
    ]
    lines = [
        "# Sample Schematic Metrics",
        "",
        f"Status: `{metrics['status']}`",
        f"Schematic: `{metrics['schematic_path']}`",
        "",
        "## Summary",
        "",
        f"- sheet_count: `{details['sheet_count']}`",
        f"- symbol_count: `{details['symbol_count']}`",
        f"- physical_symbol_count: `{details['physical_symbol_count']}`",
        f"- wire_count: `{details['wire_count']}`",
        f"- label_count: `{details['label_count']}`",
        f"- wire_to_label_ratio: `{details['wire_to_label_ratio']}`",
        f"- annotation_status: `{annotation['status']}`",
        f"- footprint_status: `{footprint['status']}`",
        f"- erc_status: `{erc['status']}`",
        f"- overlap_status: `{overlap['status']}`",
        "",
        "## Block Titles",
        "",
    ]
    if details["block_titles"]:
        lines.extend(f"- {title}" for title in details["block_titles"])
    else:
        lines.append("- none detected")
    lines.extend(["", "## Block Summary", ""])
    if block_rows:
        lines.extend(
            [
                "| block_id | title | symbol_count | heading_text |",
                "| --- | --- | ---: | --- |",
            ]
        )
        for row in block_rows:
            lines.append(f"| `{row[0]}` | {row[1]} | {row[2]} | {row[3]} |")
    else:
        lines.append("_no blocks detected_")
    lines.extend(
        [
            "",
            "## Quality Flags",
            "",
            f"- unresolved_reference_count: `{annotation['unresolved_reference_count']}`",
            f"- duplicate_reference_count: `{annotation['duplicate_reference_count']}`",
            f"- missing_footprint_count: `{footprint['missing_footprint_count']}`",
            f"- overlap_count: `{overlap['overlap_count']}`",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract readability-oriented metrics from a KiCad sample schematic.")
    parser.add_argument("--sample-path", type=Path, help="Sample folder containing a .kicad_sch file.")
    parser.add_argument("--schematic", type=Path, help="Direct path to a .kicad_sch file.")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--run-erc", action="store_true")
    args = parser.parse_args()

    if not args.sample_path and not args.schematic:
        raise SystemExit("Provide --sample-path or --schematic.")
    schematic_path = args.schematic.resolve() if args.schematic else first_schematic(args.sample_path.resolve())
    metrics = extract_metrics(schematic_path, run_erc_check=args.run_erc)

    if args.json_output:
        write_json(args.json_output, metrics)
    if args.output:
        write_markdown(args.output, markdown(metrics))
        print(f"Wrote schematic metrics: {repo_rel(args.output)}")
    elif not args.json_output:
        print(json.dumps(metrics, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
