#!/usr/bin/env python3
"""Extract physical symbols and risk metadata from a KiCad schematic."""

from __future__ import annotations

from pathlib import Path

from footprint_package_common import (
    common_parser,
    default_output_dir,
    exit_code_for,
    load_physical_symbols,
    resolve_project_and_schematic,
    write_outputs,
)


def run_extract(schematic: Path) -> dict:
    symbols = load_physical_symbols(schematic)
    return {
        "audit_id": "physical_symbol_extract",
        "title": "Physical Symbol Extract",
        "generated_at": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
        "schematic": str(schematic),
        "summary": {
            "status": "PASS",
            "counts": {
                "PASS": len(symbols),
                "WARN": 0,
                "FAIL": 0,
                "NEEDS_HUMAN_REVIEW": 0,
            },
        },
        "physical_symbol_count": len(symbols),
        "high_risk_count": sum(1 for symbol in symbols if symbol.get("high_risk")),
        "symbols": [
            {
                "reference": symbol["reference"],
                "value": symbol["value"],
                "lib_id": symbol["lib_id"],
                "footprint": symbol["footprint"],
                "category": symbol["category"],
                "risk": symbol["risk"],
                "high_risk": symbol["high_risk"],
                "risk_reason": symbol["risk_reason"],
            }
            for symbol in symbols
        ],
        "findings": [],
    }


def markdown_report(result: dict) -> str:
    lines = [
        "# Physical Symbol Extract",
        "",
        f"Generated: `{result['generated_at']}`",
        f"Schematic: `{result['schematic']}`",
        "",
        f"- Physical symbols: {result['physical_symbol_count']}",
        f"- High-risk symbols: {result['high_risk_count']}",
        "",
        "## Symbols",
        "",
        "| Reference | Value | Symbol | Footprint | Category | Risk |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for symbol in result["symbols"]:
        lines.append(
            "| `{reference}` | `{value}` | `{lib_id}` | `{footprint}` | `{category}` | `{risk}` |".format(
                reference=symbol["reference"],
                value=symbol["value"],
                lib_id=symbol["lib_id"],
                footprint=symbol["footprint"],
                category=symbol["category"],
                risk=symbol["risk"],
            )
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = common_parser("Extract physical symbols and risk metadata from a KiCad schematic.")
    args = parser.parse_args()
    project_root, schematic = resolve_project_and_schematic(args.project, args.schematic)
    result = run_extract(schematic)
    report_dir = default_output_dir(project_root, schematic)
    output_path = Path(args.output) if args.output else report_dir / "physical_symbols.md"
    json_path = Path(args.json_output) if args.json_output else report_dir / "physical_symbols.json"
    if json_path:
        json_path.parent.mkdir(parents=True, exist_ok=True)
        json_path.write_text(__import__("json").dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown_report(result), encoding="utf-8")
    print(str(json_path))
    return exit_code_for(result, args.no_fail)


if __name__ == "__main__":
    raise SystemExit(main())
