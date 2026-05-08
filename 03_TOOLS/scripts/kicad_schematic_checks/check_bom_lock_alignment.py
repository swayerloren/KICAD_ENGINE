#!/usr/bin/env python3
"""Compare parseable BOM lock references against schematic references and values."""

from __future__ import annotations

from pathlib import Path

from schematic_check_common import (
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    CHECK_STATUS_WARN,
    build_report_data,
    check_record,
    common_parser,
    exit_code_for,
    load_schematic,
    parse_bom_lock,
    symbol_instances,
    write_optional_reports,
)


def run_checks(schematic: Path, bom_lock: Path | None) -> list[dict[str, str]]:
    checks: list[dict[str, str]] = []
    if not bom_lock:
        return [check_record(CHECK_STATUS_FAIL, "BOM_LOCK_REQUIRED", "BOM lock path is required for alignment checking.")]

    root = load_schematic(schematic)
    symbols = symbol_instances(root)
    by_ref = {str(symbol.get("reference", "")).upper(): symbol for symbol in symbols if symbol.get("reference")}
    bom = parse_bom_lock(bom_lock)
    if not bom["exists"]:
        return [check_record(CHECK_STATUS_FAIL, "BOM_LOCK_NOT_FOUND", "BOM lock file does not exist.", "", str(bom_lock))]

    if not bom["references"]:
        checks.append(check_record(CHECK_STATUS_WARN, "NO_PARSEABLE_BOM_REFERENCES", "No parseable reference designators were found in the BOM lock file.", "", str(bom_lock)))

    for ref, item in sorted(bom["references"].items()):
        if ref not in by_ref:
            checks.append(check_record(CHECK_STATUS_FAIL, "BOM_REFERENCE_MISSING_FROM_SCHEMATIC", "BOM lock reference does not exist in schematic.", ref, item.get("line", "")))
            continue
        symbol = by_ref[ref]
        value = str(symbol.get("value", ""))
        mpn_candidates = item.get("mpn_candidates", "")
        if mpn_candidates and value and value.lower() not in item.get("line", "").lower():
            checks.append(
                check_record(
                    CHECK_STATUS_WARN,
                    "SCHEMATIC_VALUE_NOT_OBVIOUS_IN_BOM_LOCK",
                    "Schematic value is not an obvious substring of the BOM lock row; human review required.",
                    ref,
                    f"value={value}; bom={item.get('line', '')}",
                )
            )
        else:
            checks.append(check_record(CHECK_STATUS_PASS, "BOM_REFERENCE_ALIGNED", "BOM lock reference exists in schematic.", ref, value))

    schematic_only = sorted(ref for ref in by_ref if not ref.startswith("#") and ref not in bom["references"])
    if schematic_only:
        checks.append(check_record(CHECK_STATUS_WARN, "SCHEMATIC_REFERENCES_NOT_IN_BOM_LOCK", "Schematic has references not found in parseable BOM lock rows.", "", ", ".join(schematic_only[:80])))
    return checks


def main() -> int:
    parser = common_parser("Check KiCad schematic reference alignment against a BOM lock file.")
    args = parser.parse_args()
    schematic = Path(args.schematic)
    bom_lock = Path(args.bom_lock) if args.bom_lock else None
    checks = run_checks(schematic, bom_lock)
    data = build_report_data(args, checks)
    write_optional_reports(args, "BOM Lock Alignment Check", data)
    return exit_code_for(data, args.no_fail)


if __name__ == "__main__":
    raise SystemExit(main())
