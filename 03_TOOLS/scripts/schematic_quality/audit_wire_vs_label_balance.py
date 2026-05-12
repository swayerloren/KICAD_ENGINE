#!/usr/bin/env python3
"""Audit whether local blocks rely too heavily on isolated net labels."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from schematic_quality_common import (
    BLOCK_DEFINITIONS,
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    CHECK_STATUS_WARN,
    build_audit_result,
    check_record,
    common_parser,
    exit_code_for,
    extract_symbols,
    extract_text_items,
    extract_wire_segments,
    heading_positions,
    load_schematic,
    assign_blocks,
    rects_overlap,
    write_outputs,
)


def point_in_bbox(x: float, y: float, bbox: dict[str, float], margin: float = 3.0) -> bool:
    return (bbox["x1"] - margin) <= x <= (bbox["x2"] + margin) and (bbox["y1"] - margin) <= y <= (bbox["y2"] + margin)


def run_audit(schematic: Path) -> dict:
    root = load_schematic(schematic)
    symbols = extract_symbols(root)
    texts = extract_text_items(root, symbols)
    wires = extract_wire_segments(root)
    headings = heading_positions(texts)
    blocks, _ = assign_blocks(symbols, headings)
    findings: list[dict[str, str]] = []
    label_items = [item for item in texts if item["kind"] == "label"]

    for block in BLOCK_DEFINITIONS:
        block_data = blocks[block["id"]]
        bbox = block_data["bbox"]
        labels = [item for item in label_items if point_in_bbox(item["at"]["x"], item["at"]["y"], bbox)]
        wire_count = sum(1 for segment in wires if point_in_bbox(segment["midpoint"]["x"], segment["midpoint"]["y"], bbox))
        label_counts = Counter(item["text"] for item in labels)
        repeated_local = {name: count for name, count in label_counts.items() if count >= 3}

        if len(labels) > wire_count and len(labels) >= 4:
            findings.append(
                check_record(
                    CHECK_STATUS_WARN,
                    "LOCAL_LABEL_HEAVY_BLOCK",
                    "Block uses more labels than local wire segments, which may reduce readability.",
                    "",
                    f"{block['title']}: labels={len(labels)}, wires={wire_count}",
                )
            )
        else:
            findings.append(
                check_record(
                    CHECK_STATUS_PASS,
                    "WIRE_LABEL_BALANCE_OK",
                    "Local wire-vs-label balance is acceptable for this block.",
                    "",
                    f"{block['title']}: labels={len(labels)}, wires={wire_count}",
                )
            )

        if repeated_local:
            findings.append(
                check_record(
                    CHECK_STATUS_WARN,
                    "REPEATED_LOCAL_LABELS",
                    "A local block repeats the same net labels many times; use more local wiring.",
                    "",
                    f"{block['title']}: {', '.join(f'{name} x{count}' for name, count in repeated_local.items())}",
                )
            )

    return build_audit_result("wire_vs_label", "Wire Vs Net Label Balance Audit", schematic, findings)


def main() -> int:
    parser = common_parser("Audit local wiring vs isolated net-label use.")
    args = parser.parse_args()
    result = run_audit(Path(args.schematic))
    write_outputs(result, Path(args.output) if args.output else None, Path(args.json_output) if args.json_output else None)
    return exit_code_for(result, args.no_fail)


if __name__ == "__main__":
    raise SystemExit(main())
