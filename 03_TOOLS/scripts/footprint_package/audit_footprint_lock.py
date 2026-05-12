#!/usr/bin/env python3
"""Audit FOOTPRINT_LOCK.csv against the saved schematic."""

from __future__ import annotations

from pathlib import Path

from footprint_package_common import (
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    CHECK_STATUS_WARN,
    REQUIRED_LOCK_COLUMNS,
    boolish,
    build_audit_result,
    check_record,
    common_parser,
    default_output_dir,
    exit_code_for,
    load_physical_symbols,
    locate_lock_file,
    read_lock_rows,
    resolve_project_and_schematic,
    source_reference_present,
    write_outputs,
)


def run_audit(schematic: Path, project_root: Path | None, explicit_lock: str = "") -> dict:
    symbols = load_physical_symbols(schematic)
    lock_path = locate_lock_file(project_root, explicit_lock)
    rows, row_index = read_lock_rows(lock_path)
    findings = []

    if lock_path is None or not lock_path.exists():
        findings.append(
            check_record(
                CHECK_STATUS_FAIL,
                "FOOTPRINT_LOCK_MISSING",
                "FOOTPRINT_LOCK.csv is missing.",
                "",
                str(lock_path) if lock_path else "",
            )
        )
        return build_audit_result(
            "footprint_lock_audit",
            "Footprint Lock Audit",
            schematic,
            findings,
            {
                "lock_file": str(lock_path) if lock_path else "",
                "lock_file_present": False,
                "required_columns": REQUIRED_LOCK_COLUMNS,
                "missing_lock_rows": len(symbols),
            },
        )

    missing_columns = [column for column in REQUIRED_LOCK_COLUMNS if column not in rows[0].keys()] if rows else REQUIRED_LOCK_COLUMNS
    if missing_columns:
        findings.append(
            check_record(
                CHECK_STATUS_FAIL,
                "LOCK_COLUMNS_MISSING",
                f"Lock file is missing required columns: {', '.join(missing_columns)}.",
                "",
                str(lock_path),
            )
        )

    missing_rows = 0
    unverified_rows = 0
    mismatched_footprints = 0
    for symbol in symbols:
        reference = symbol["reference"].upper()
        row = row_index.get(reference)
        if row is None:
            missing_rows += 1
            findings.append(
                check_record(
                    CHECK_STATUS_FAIL,
                    "LOCK_ROW_MISSING",
                    "Physical symbol is missing a lock-file row.",
                    symbol["reference"],
                    str(lock_path),
                )
            )
            continue

        if row.get("kicad_symbol", "").strip() and row.get("kicad_symbol", "").strip() != symbol["lib_id"]:
            findings.append(
                check_record(
                    CHECK_STATUS_WARN,
                    "LOCK_SYMBOL_MISMATCH",
                    "Lock-file symbol does not exactly match the current schematic lib_id.",
                    symbol["reference"],
                    str(lock_path),
                )
            )

        if str(symbol.get("footprint", "")).strip() and row.get("kicad_footprint", "").strip() and row.get("kicad_footprint", "").strip() != str(symbol.get("footprint", "")).strip():
            mismatched_footprints += 1
            findings.append(
                check_record(
                    CHECK_STATUS_FAIL,
                    "LOCK_FOOTPRINT_MISMATCH",
                    "Lock-file footprint does not match the current schematic footprint field.",
                    symbol["reference"],
                    str(lock_path),
                )
            )

        if not source_reference_present(row.get("datasheet_or_source_url", "")):
            unverified_rows += 1
            findings.append(
                check_record(
                    CHECK_STATUS_FAIL,
                    "SOURCE_EVIDENCE_MISSING",
                    "Lock row is missing datasheet/source evidence.",
                    symbol["reference"],
                    str(lock_path),
                )
            )

        if row.get("risk", "").strip().upper() not in {"LOW", "MEDIUM", "HIGH"}:
            unverified_rows += 1
            findings.append(
                check_record(
                    CHECK_STATUS_FAIL,
                    "RISK_CLASSIFICATION_MISSING",
                    "Lock row is missing a valid LOW/MEDIUM/HIGH risk classification.",
                    symbol["reference"],
                    str(lock_path),
                )
            )

        if boolish(row.get("package_drawing_checked", "")) is not True:
            unverified_rows += 1
            findings.append(
                check_record(
                    CHECK_STATUS_FAIL,
                    "PACKAGE_DRAWING_NOT_CHECKED",
                    "Lock row does not prove package drawing review.",
                    symbol["reference"],
                    str(lock_path),
                )
            )

    if not findings:
        findings.append(
            check_record(
                CHECK_STATUS_PASS,
                "FOOTPRINT_LOCK_COMPLETE",
                "FOOTPRINT_LOCK.csv covers every physical symbol with the required proof fields.",
                "",
                str(lock_path),
            )
        )

    return build_audit_result(
        "footprint_lock_audit",
        "Footprint Lock Audit",
        schematic,
        findings,
        {
            "lock_file": str(lock_path),
            "lock_file_present": True,
            "required_columns": REQUIRED_LOCK_COLUMNS,
            "row_count": len(rows),
            "missing_lock_rows": missing_rows,
            "unverified_rows": unverified_rows,
            "mismatched_footprints": mismatched_footprints,
        },
    )


def main() -> int:
    parser = common_parser("Audit FOOTPRINT_LOCK.csv against the saved schematic.")
    args = parser.parse_args()
    project_root, schematic = resolve_project_and_schematic(args.project, args.schematic)
    result = run_audit(schematic, project_root, args.lock_file)
    report_dir = default_output_dir(project_root, schematic)
    output_path = Path(args.output) if args.output else report_dir / "footprint_lock.md"
    json_path = Path(args.json_output) if args.json_output else report_dir / "footprint_lock.json"
    write_outputs(result, output_path, json_path)
    print(str(json_path))
    return exit_code_for(result, args.no_fail)


if __name__ == "__main__":
    raise SystemExit(main())
