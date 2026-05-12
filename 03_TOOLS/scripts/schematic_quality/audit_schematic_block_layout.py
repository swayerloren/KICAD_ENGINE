#!/usr/bin/env python3
"""Audit functional block grouping and block-flow layout in a schematic."""

from __future__ import annotations

from pathlib import Path

from schematic_quality_common import (
    BLOCK_DEFINITIONS,
    BLOCK_ORDER,
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    CHECK_STATUS_WARN,
    build_audit_result,
    check_record,
    common_parser,
    exit_code_for,
    extract_symbols,
    extract_text_items,
    heading_positions,
    load_schematic,
    assign_blocks,
    is_power_symbol,
    rect_distance,
    rects_overlap,
    write_outputs,
)


def run_audit(schematic: Path) -> dict:
    root = load_schematic(schematic)
    symbols = extract_symbols(root)
    texts = extract_text_items(root, symbols)
    headings = heading_positions(texts)
    blocks, unassigned = assign_blocks(symbols, headings)
    findings: list[dict[str, str]] = []

    for block in BLOCK_DEFINITIONS:
        block_data = blocks[block["id"]]
        if not block_data["heading_text"]:
            findings.append(check_record(CHECK_STATUS_FAIL, "BLOCK_HEADING_MISSING", f"Expected functional block heading is missing: {block['title']}.", "", block["id"]))
        elif block_data["symbol_count"] == 0:
            findings.append(check_record(CHECK_STATUS_WARN, "BLOCK_HAS_NO_ASSIGNED_SYMBOLS", f"Block heading exists but no symbols were assigned: {block['title']}.", "", block["id"]))
        else:
            findings.append(check_record(CHECK_STATUS_PASS, "BLOCK_PRESENT", f"Functional block detected: {block['title']}.", "", block["id"]))

    heading_list = [(block_id, headings[block_id]["at"]["x"], headings[block_id]["at"]["y"]) for block_id in BLOCK_ORDER if block_id in headings]
    if len(heading_list) >= 3:
        x_violations = 0
        y_violations = 0
        previous_x = None
        previous_y = None
        for _, current_x, current_y in heading_list:
            if previous_x is not None and current_x < previous_x - 5.0:
                x_violations += 1
            if previous_y is not None and current_y < previous_y - 5.0:
                y_violations += 1
            previous_x = current_x
            previous_y = current_y
        if min(x_violations, y_violations) > 1:
            findings.append(check_record(CHECK_STATUS_WARN, "BLOCK_FLOW_DISORDERED", "Block headings do not form a clean left-to-right or top-to-bottom flow.", "", f"x_violations={x_violations}, y_violations={y_violations}"))
        else:
            flow = "LEFT_TO_RIGHT" if x_violations <= y_violations else "TOP_TO_BOTTOM"
            findings.append(check_record(CHECK_STATUS_PASS, "BLOCK_FLOW_PRESENT", f"Functional block headings show a readable {flow} flow.", "", flow))
    else:
        findings.append(check_record(CHECK_STATUS_WARN, "INSUFFICIENT_BLOCK_HEADINGS_FOR_FLOW_CHECK", "Not enough recognized block headings were found for a robust flow check."))

    non_power_symbols = [symbol for symbol in symbols if not is_power_symbol(symbol)]
    for index, first in enumerate(non_power_symbols):
        for second in non_power_symbols[index + 1 :]:
            if rects_overlap(first["bbox"], second["bbox"], margin=0.0):
                findings.append(
                    check_record(
                        CHECK_STATUS_WARN,
                        "SYMBOL_BBOX_OVERLAP_ESTIMATE",
                        "Estimated symbol bounding boxes overlap.",
                        f"{first.get('reference', '')} {second.get('reference', '')}".strip(),
                        f"{first.get('lib_id', '')} <-> {second.get('lib_id', '')}",
                    )
                )
            elif rect_distance(first["bbox"], second["bbox"]) < 1.0:
                findings.append(
                    check_record(
                        CHECK_STATUS_WARN,
                        "SYMBOL_SPACING_TIGHT_ESTIMATE",
                        "Estimated symbol spacing is very tight.",
                        f"{first.get('reference', '')} {second.get('reference', '')}".strip(),
                        f"{rect_distance(first['bbox'], second['bbox']):.2f} mm",
                    )
                )

    if unassigned:
        findings.append(
            check_record(
                CHECK_STATUS_WARN,
                "UNASSIGNED_SYMBOLS",
                "Some symbols could not be assigned to a functional block cleanly.",
                "",
                ", ".join(symbol.get("reference", "") for symbol in unassigned if symbol.get("reference")),
            )
        )

    return build_audit_result(
        "block_layout",
        "Schematic Block Layout Audit",
        schematic,
        findings,
        {
            "blocks": {
                key: {
                    "block_id": value["block_id"],
                    "title": value["title"],
                    "heading_text": value["heading_text"],
                    "heading_at": value["heading_at"],
                    "bbox": value["bbox"],
                    "centroid": value["centroid"],
                    "symbol_count": value["symbol_count"],
                }
                for key, value in blocks.items()
            },
            "unassigned_symbols": [symbol.get("reference", "") for symbol in unassigned],
        },
    )


def main() -> int:
    parser = common_parser("Audit functional block grouping and schematic flow.")
    args = parser.parse_args()
    result = run_audit(Path(args.schematic))
    write_outputs(result, Path(args.output) if args.output else None, Path(args.json_output) if args.json_output else None)
    return exit_code_for(result, args.no_fail)


if __name__ == "__main__":
    raise SystemExit(main())
