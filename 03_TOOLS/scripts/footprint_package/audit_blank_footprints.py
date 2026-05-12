#!/usr/bin/env python3
"""Audit physical symbols for blank or missing footprints."""

from __future__ import annotations

from pathlib import Path

from footprint_package_common import (
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    build_audit_result,
    check_record,
    common_parser,
    default_output_dir,
    exit_code_for,
    load_physical_symbols,
    resolve_project_and_schematic,
    write_outputs,
)


def run_audit(schematic: Path) -> dict:
    symbols = load_physical_symbols(schematic)
    findings = []
    for symbol in symbols:
        if not str(symbol.get("footprint", "")).strip():
            findings.append(
                check_record(
                    CHECK_STATUS_FAIL,
                    "BLANK_FOOTPRINT",
                    "Physical symbol has a blank footprint field.",
                    symbol["reference"],
                    str(schematic),
                )
            )
    if not findings:
        findings.append(
            check_record(
                CHECK_STATUS_PASS,
                "ALL_PHYSICAL_SYMBOLS_HAVE_FOOTPRINTS",
                "All physical symbols have a non-blank footprint field.",
                "",
                str(schematic),
            )
        )
    return build_audit_result(
        "blank_footprint_audit",
        "Blank Footprint Audit",
        schematic,
        findings,
        {
            "physical_symbol_count": len(symbols),
            "blank_footprint_count": sum(1 for symbol in symbols if not str(symbol.get("footprint", "")).strip()),
        },
    )


def main() -> int:
    parser = common_parser("Audit physical symbols for blank or missing footprints.")
    args = parser.parse_args()
    project_root, schematic = resolve_project_and_schematic(args.project, args.schematic)
    result = run_audit(schematic)
    report_dir = default_output_dir(project_root, schematic)
    output_path = Path(args.output) if args.output else report_dir / "blank_footprints.md"
    json_path = Path(args.json_output) if args.json_output else report_dir / "blank_footprints.json"
    write_outputs(result, output_path, json_path)
    print(str(json_path))
    return exit_code_for(result, args.no_fail)


if __name__ == "__main__":
    raise SystemExit(main())
