#!/usr/bin/env python3
"""Audit schematic references, duplicates, and unresolved placeholders."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from schematic_quality_common import (
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    build_audit_result,
    check_record,
    common_parser,
    exit_code_for,
    extract_symbols,
    is_power_symbol,
    load_schematic,
    write_outputs,
)


def run_audit(schematic: Path) -> dict:
    root = load_schematic(schematic)
    symbols = extract_symbols(root)
    references = [str(symbol.get("reference", "")).strip().upper() for symbol in symbols if symbol.get("reference")]
    counts = Counter(references)
    findings: list[dict[str, str]] = []

    for symbol in symbols:
        reference = str(symbol.get("reference", "")).strip()
        lib_id = str(symbol.get("lib_id", ""))
        value = str(symbol.get("value", "")).strip()
        if not reference:
            findings.append(check_record(CHECK_STATUS_FAIL, "BLANK_REFERENCE", "Reference field is blank.", "", lib_id))
        elif reference.endswith("?"):
            findings.append(check_record(CHECK_STATUS_FAIL, "UNRESOLVED_REFERENCE", "Reference still ends with '?'.", reference, lib_id))
        else:
            findings.append(check_record(CHECK_STATUS_PASS, "REFERENCE_RESOLVED", "Reference is resolved.", reference, lib_id))

        if counts.get(reference.upper(), 0) > 1 and not reference.upper().startswith("#"):
            findings.append(check_record(CHECK_STATUS_FAIL, "DUPLICATE_REFERENCE", "Reference appears more than once.", reference, lib_id))

        if not value:
            findings.append(check_record(CHECK_STATUS_FAIL, "BLANK_VALUE", "Value field is blank.", reference, lib_id))

        if is_power_symbol(symbol) and reference.endswith("?"):
            findings.append(check_record(CHECK_STATUS_FAIL, "POWER_SYMBOL_UNANNOTATED", "Power symbol reference still ends with '?'.", reference, lib_id))

    if not symbols:
        findings.append(check_record(CHECK_STATUS_FAIL, "NO_SYMBOLS_FOUND", "No symbol instances were extracted.", "", str(schematic)))
    return build_audit_result("annotation", "Schematic Annotation Audit", schematic, findings, {"symbol_count": len(symbols)})


def main() -> int:
    parser = common_parser("Audit schematic annotation and unresolved references.")
    args = parser.parse_args()
    result = run_audit(Path(args.schematic))
    write_outputs(result, Path(args.output) if args.output else None, Path(args.json_output) if args.json_output else None)
    return exit_code_for(result, args.no_fail)


if __name__ == "__main__":
    raise SystemExit(main())
