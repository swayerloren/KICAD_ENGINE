#!/usr/bin/env python3
"""Audit schematic footprint assignment readiness."""

from __future__ import annotations

from pathlib import Path

from schematic_quality_common import (
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    MARKER_TOKENS,
    build_audit_result,
    check_record,
    common_parser,
    exit_code_for,
    extract_symbols,
    is_physical_symbol,
    load_schematic,
    write_outputs,
)


def run_audit(schematic: Path) -> dict:
    root = load_schematic(schematic)
    symbols = extract_symbols(root)
    findings: list[dict[str, str]] = []
    physical_count = 0

    for symbol in symbols:
        if not is_physical_symbol(symbol):
            continue
        physical_count += 1
        reference = str(symbol.get("reference", "")).strip()
        footprint = str(symbol.get("footprint", "")).strip()
        value = str(symbol.get("value", "")).strip()
        if not footprint:
            findings.append(check_record(CHECK_STATUS_FAIL, "BLANK_FOOTPRINT", "Physical symbol has no footprint assigned.", reference, symbol.get("lib_id", "")))
        else:
            findings.append(check_record(CHECK_STATUS_PASS, "FOOTPRINT_PRESENT", "Footprint field is populated.", reference, footprint))

        upper_value = value.upper()
        if any(token in upper_value for token in MARKER_TOKENS):
            findings.append(check_record(CHECK_STATUS_FAIL, "VISIBLE_REVIEW_MARKER_IN_VALUE", "Visible symbol value still carries a review marker.", reference, value))

    if physical_count == 0:
        findings.append(check_record(CHECK_STATUS_FAIL, "NO_PHYSICAL_SYMBOLS", "No physical symbols were detected.", "", str(schematic)))
    return build_audit_result(
        "footprints",
        "Schematic Footprint Audit",
        schematic,
        findings,
        {"physical_symbol_count": physical_count},
    )


def main() -> int:
    parser = common_parser("Audit schematic footprint assignment and visible review markers.")
    args = parser.parse_args()
    result = run_audit(Path(args.schematic))
    write_outputs(result, Path(args.output) if args.output else None, Path(args.json_output) if args.json_output else None)
    return exit_code_for(result, args.no_fail)


if __name__ == "__main__":
    raise SystemExit(main())
