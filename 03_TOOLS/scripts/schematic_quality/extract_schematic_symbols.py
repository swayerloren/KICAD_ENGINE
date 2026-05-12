#!/usr/bin/env python3
"""Extract symbol instances and estimated geometry from a KiCad schematic."""

from __future__ import annotations

import json
from pathlib import Path

from schematic_quality_common import (
    build_audit_result,
    common_parser,
    extract_symbols,
    extract_text_items,
    heading_positions,
    load_schematic,
    assign_blocks,
    write_outputs,
)


def run_extract(schematic: Path) -> dict:
    root = load_schematic(schematic)
    symbols = extract_symbols(root)
    texts = extract_text_items(root, symbols)
    headings = heading_positions(texts)
    blocks, unassigned = assign_blocks(symbols, headings)
    findings = []
    for symbol in symbols:
        findings.append(
            {
                "status": "PASS",
                "code": "SYMBOL_EXTRACTED",
                "reference": symbol.get("reference", ""),
                "message": f"{symbol.get('lib_id', '')} extracted.",
                "evidence": symbol.get("block_id", ""),
            }
        )
    return build_audit_result(
        "extract_schematic_symbols",
        "Extracted Schematic Symbols",
        schematic,
        findings,
        {
            "symbol_count": len(symbols),
            "symbols": symbols,
            "headings": headings,
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
    parser = common_parser("Extract schematic symbols and estimated geometry.")
    args = parser.parse_args()
    result = run_extract(Path(args.schematic))
    output = Path(args.output) if args.output else None
    json_output = Path(args.json_output) if args.json_output else None
    if json_output and not output:
        json_output.parent.mkdir(parents=True, exist_ok=True)
        json_output.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    else:
        write_outputs(result, output, json_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
