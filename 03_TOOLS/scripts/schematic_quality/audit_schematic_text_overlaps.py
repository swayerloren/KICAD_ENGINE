#!/usr/bin/env python3
"""Audit approximate text overlap risks in a KiCad schematic."""

from __future__ import annotations

from pathlib import Path

from schematic_quality_common import (
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    CHECK_STATUS_WARN,
    build_audit_result,
    check_record,
    common_parser,
    exit_code_for,
    extract_symbols,
    extract_text_items,
    is_power_symbol,
    line_box_with_margin,
    load_schematic,
    rects_overlap,
    write_outputs,
)


def run_audit(schematic: Path) -> dict:
    root = load_schematic(schematic)
    symbols = extract_symbols(root)
    texts = extract_text_items(root, symbols)
    findings: list[dict[str, str]] = []

    for index, first in enumerate(texts):
        for second in texts[index + 1 :]:
            if rects_overlap(first["bbox"], second["bbox"], margin=0.1):
                findings.append(
                    check_record(
                        CHECK_STATUS_WARN,
                        "TEXT_TEXT_OVERLAP_ESTIMATE",
                        "Estimated overlap between visible text items.",
                        f"{first.get('owner_reference', '')} {second.get('owner_reference', '')}".strip(),
                        f"{first['kind']}:{first['text']} <-> {second['kind']}:{second['text']}",
                    )
                )

    for text in texts:
        kind = str(text["kind"])
        if kind.startswith("label"):
            continue
        if kind.startswith("property:Footprint") or kind.startswith("property:Datasheet"):
            continue
        for symbol in symbols:
            if text.get("owner_reference", "") == symbol.get("reference", ""):
                continue
            if is_power_symbol(symbol):
                continue
            if rects_overlap(text["bbox"], symbol["bbox"], margin=0.2):
                findings.append(
                    check_record(
                        CHECK_STATUS_FAIL,
                        "TEXT_OVER_SYMBOL_BODY_ESTIMATE",
                        "Estimated visible text overlap with a symbol body.",
                        str(text.get("owner_reference", "")),
                        f"{kind}:{text['text']} vs {symbol.get('reference', '')}",
                    )
                )
            for pin in symbol.get("pin_points", []):
                if (
                    text["bbox"]["x1"] <= pin["x"] <= text["bbox"]["x2"]
                    and text["bbox"]["y1"] <= pin["y"] <= text["bbox"]["y2"]
                ):
                    findings.append(
                        check_record(
                            CHECK_STATUS_FAIL,
                            "TEXT_OVER_PIN_ESTIMATE",
                            "Estimated visible text overlap with a symbol pin connection.",
                            str(text.get("owner_reference", "")),
                            f"{kind}:{text['text']} vs {symbol.get('reference', '')}",
                        )
                    )

    from schematic_quality_common import extract_wire_segments

    wires = extract_wire_segments(root)
    for text in texts:
        kind = str(text["kind"])
        if kind.startswith("label"):
            continue
        for segment in wires:
            if rects_overlap(text["bbox"], line_box_with_margin(segment), margin=0.0):
                findings.append(
                    check_record(
                        CHECK_STATUS_WARN,
                        "TEXT_OVER_WIRE_ESTIMATE",
                        "Estimated visible text overlap with a wire segment.",
                        str(text.get("owner_reference", "")),
                        f"{kind}:{text['text']}",
                    )
                )

    if not findings:
        findings.append(check_record(CHECK_STATUS_PASS, "NO_ESTIMATED_TEXT_OVERLAPS", "No estimated visible text overlaps were detected."))
    return build_audit_result(
        "text_overlaps",
        "Schematic Text Overlap Audit",
        schematic,
        findings,
        {"visible_text_count": len(texts)},
    )


def main() -> int:
    parser = common_parser("Audit approximate visible text overlaps in a schematic.")
    args = parser.parse_args()
    result = run_audit(Path(args.schematic))
    write_outputs(result, Path(args.output) if args.output else None, Path(args.json_output) if args.json_output else None)
    return exit_code_for(result, args.no_fail)


if __name__ == "__main__":
    raise SystemExit(main())
