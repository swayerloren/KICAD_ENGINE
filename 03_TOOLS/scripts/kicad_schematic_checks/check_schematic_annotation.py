#!/usr/bin/env python3
"""Check KiCad schematic annotation and reference-designator completeness."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from schematic_check_common import (
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    CHECK_STATUS_WARN,
    build_report_data,
    category_matches,
    check_record,
    common_parser,
    exit_code_for,
    has_verification_status,
    is_physical_symbol,
    load_schematic,
    parse_bom_lock,
    reference_prefix,
    risk_categories,
    symbol_instances,
    write_optional_reports,
)


def is_vague_value(value: str) -> bool:
    clean = value.strip().lower()
    return clean in {"", "connector", "generic", "tbd", "unknown", "needs_review", "mosfet", "regulator"} or clean.endswith(" generic")


def run_checks(schematic: Path, bom_lock: Path | None) -> list[dict[str, str]]:
    root = load_schematic(schematic)
    symbols = symbol_instances(root)
    checks: list[dict[str, str]] = []
    bom = parse_bom_lock(bom_lock)
    ref_counts = Counter(str(symbol.get("reference", "")).upper() for symbol in symbols if symbol.get("reference"))

    for symbol in symbols:
        reference = str(symbol.get("reference", "")).strip()
        value = str(symbol.get("value", "")).strip()
        footprint = str(symbol.get("footprint", "")).strip()
        props = symbol.get("properties", {})
        lib_id = str(symbol.get("lib_id", ""))

        if "Reference" not in props:
            checks.append(check_record(CHECK_STATUS_FAIL, "MISSING_REFERENCE_FIELD", "Symbol has no Reference property.", "", lib_id))
        elif not reference:
            checks.append(check_record(CHECK_STATUS_FAIL, "BLANK_REFERENCE", "Reference field is blank.", "", lib_id))
        elif reference.endswith("?"):
            checks.append(check_record(CHECK_STATUS_FAIL, "UNANNOTATED_REFERENCE", "Reference still ends in '?'.", reference, lib_id))
        else:
            checks.append(check_record(CHECK_STATUS_PASS, "REFERENCE_PRESENT", "Reference is present and annotated.", reference, lib_id))

        if reference and ref_counts[reference.upper()] > 1 and not reference.upper().startswith("#"):
            checks.append(check_record(CHECK_STATUS_FAIL, "DUPLICATE_REFERENCE", "Reference appears more than once.", reference, lib_id))

        if "Value" not in props:
            checks.append(check_record(CHECK_STATUS_FAIL, "MISSING_VALUE_FIELD", "Symbol has no Value property.", reference, lib_id))
        elif not value:
            checks.append(check_record(CHECK_STATUS_FAIL, "BLANK_VALUE", "Value field is blank.", reference, lib_id))
        elif is_vague_value(value) and reference.upper() in bom["references"]:
            checks.append(
                check_record(
                    CHECK_STATUS_WARN,
                    "VAGUE_VALUE_WHEN_BOM_LOCK_EXISTS",
                    "Value looks vague while BOM lock contains an entry for this reference.",
                    reference,
                    bom["references"][reference.upper()].get("line", ""),
                )
            )
        else:
            checks.append(check_record(CHECK_STATUS_PASS, "VALUE_PRESENT", "Value field is present.", reference, value))

        if is_physical_symbol(symbol):
            if "Footprint" not in props:
                checks.append(check_record(CHECK_STATUS_FAIL, "MISSING_FOOTPRINT_FIELD", "Physical symbol has no Footprint property.", reference, lib_id))
            elif not footprint:
                checks.append(check_record(CHECK_STATUS_FAIL, "NO_FOOTPRINT_ASSIGNED", "Physical symbol has no footprint assigned.", reference, lib_id))
            else:
                checks.append(check_record(CHECK_STATUS_PASS, "FOOTPRINT_ASSIGNED", "Footprint field is populated.", reference, footprint))

            if "Datasheet" not in props:
                checks.append(check_record(CHECK_STATUS_WARN, "MISSING_DATASHEET_FIELD", "Physical symbol has no Datasheet property.", reference, lib_id))

            if reference_prefix(reference) and reference_prefix(reference) not in {"TP", "MH"}:
                matches, expected = category_matches(symbol)
                if not matches:
                    checks.append(
                        check_record(
                            CHECK_STATUS_WARN,
                            "REFERENCE_CATEGORY_MISMATCH",
                            f"Reference prefix suggests {expected}, but symbol/value text does not clearly match.",
                            reference,
                            f"{lib_id} / {value}",
                        )
                    )

        risks = risk_categories(symbol)
        if risks and not has_verification_status(symbol):
            checks.append(
                check_record(
                    CHECK_STATUS_FAIL,
                    "HIGH_RISK_PART_WITHOUT_VERIFICATION_STATUS",
                    f"High-risk categories require Verification_Status or explicit NEEDS_REVIEW/BLOCKED marker: {', '.join(risks)}.",
                    reference,
                    f"{lib_id} / {value}",
                )
            )

    if not symbols:
        checks.append(check_record(CHECK_STATUS_FAIL, "NO_SYMBOLS_FOUND", "No schematic symbol instances were found.", "", str(schematic)))
    if bom_lock and not bom["exists"]:
        checks.append(check_record(CHECK_STATUS_WARN, "BOM_LOCK_NOT_FOUND", "BOM lock was requested but does not exist.", "", str(bom_lock)))
    return checks


def main() -> int:
    parser = common_parser("Check KiCad schematic annotation, values, footprints, and high-risk verification fields.")
    args = parser.parse_args()
    schematic = Path(args.schematic)
    bom_lock = Path(args.bom_lock) if args.bom_lock else None
    checks = run_checks(schematic, bom_lock)
    data = build_report_data(args, checks)
    write_optional_reports(args, "Schematic Annotation Check", data)
    return exit_code_for(data, args.no_fail)


if __name__ == "__main__":
    raise SystemExit(main())
