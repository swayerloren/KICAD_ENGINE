#!/usr/bin/env python3
"""Audit high-risk footprint proof requirements."""

from __future__ import annotations

from pathlib import Path

from footprint_package_common import (
    CHECK_STATUS_FAIL,
    CHECK_STATUS_NEEDS_HUMAN_REVIEW,
    CHECK_STATUS_PASS,
    boolish,
    build_audit_result,
    check_record,
    common_parser,
    default_output_dir,
    exit_code_for,
    load_physical_symbols,
    locate_lock_file,
    normalize_text,
    read_lock_rows,
    resolve_project_and_schematic,
    write_outputs,
)


def requires_pin_mapping(category: str) -> bool:
    return category in {"pmos_or_fet", "module_or_mcu", "regulator"}


def requires_orientation_proof(category: str) -> bool:
    return category in {"usb_connector", "barrel_jack", "connector"}


def requires_three_d_status(category: str) -> bool:
    return category in {"usb_connector", "barrel_jack", "connector", "mounting_hole"}


def row_has_orientation_proof(row: dict[str, str]) -> bool:
    notes = normalize_text(row.get("notes", ""))
    return "orientation" in notes or "mechanical proof" in notes or "connector proof" in notes or "mouth" in notes


def run_audit(schematic: Path, project_root: Path | None, explicit_lock: str = "") -> dict:
    symbols = [symbol for symbol in load_physical_symbols(schematic) if symbol.get("high_risk")]
    lock_path = locate_lock_file(project_root, explicit_lock)
    _, row_index = read_lock_rows(lock_path)
    findings = []

    if lock_path is None or not lock_path.exists():
        findings.append(
            check_record(
                CHECK_STATUS_FAIL,
                "LOCK_FILE_REQUIRED_FOR_HIGH_RISK_REVIEW",
                "High-risk footprint review cannot run without FOOTPRINT_LOCK.csv.",
                "",
                str(lock_path) if lock_path else "",
            )
        )
        return build_audit_result(
            "high_risk_footprint_audit",
            "High Risk Footprint Audit",
            schematic,
            findings,
            {
                "high_risk_symbol_count": len(symbols),
                "lock_file": str(lock_path) if lock_path else "",
            },
        )

    for symbol in symbols:
        row = row_index.get(symbol["reference"].upper())
        if row is None:
            findings.append(
                check_record(
                    CHECK_STATUS_FAIL,
                    "HIGH_RISK_LOCK_ROW_MISSING",
                    "High-risk symbol is missing a lock-file row.",
                    symbol["reference"],
                    str(lock_path),
                )
            )
            continue

        category = str(symbol.get("category", ""))
        if boolish(row.get("package_drawing_checked", "")) is not True:
            findings.append(
                check_record(
                    CHECK_STATUS_FAIL,
                    "HIGH_RISK_PACKAGE_DRAWING_REQUIRED",
                    "High-risk symbol does not have package-drawing proof recorded.",
                    symbol["reference"],
                    str(lock_path),
                )
            )

        if requires_pin_mapping(category) and boolish(row.get("pin_mapping_checked", "")) is not True:
            findings.append(
                check_record(
                    CHECK_STATUS_FAIL,
                    "PIN_MAPPING_PROOF_REQUIRED",
                    "High-risk symbol requires explicit pin-mapping proof.",
                    symbol["reference"],
                    str(lock_path),
                )
            )

        if requires_orientation_proof(category) and not row_has_orientation_proof(row):
            findings.append(
                check_record(
                    CHECK_STATUS_FAIL,
                    "CONNECTOR_ORIENTATION_PROOF_MISSING",
                    "Connector/mechanical orientation proof is missing from the lock notes.",
                    symbol["reference"],
                    str(lock_path),
                )
            )

        three_d = boolish(row.get("3d_model_available", ""))
        human_review_required = boolish(row.get("human_review_required", ""))
        if requires_three_d_status(category) and three_d is not True:
            status = CHECK_STATUS_NEEDS_HUMAN_REVIEW if human_review_required is True else CHECK_STATUS_FAIL
            findings.append(
                check_record(
                    status,
                    "THREE_D_MODEL_OR_HUMAN_REVIEW_REQUIRED",
                    "Connector/mechanical part is missing 3D-model proof and requires explicit human review.",
                    symbol["reference"],
                    str(lock_path),
                )
            )

        if human_review_required is True:
            findings.append(
                check_record(
                    CHECK_STATUS_NEEDS_HUMAN_REVIEW,
                    "HIGH_RISK_PART_REQUIRES_HUMAN_REVIEW",
                    "Lock row explicitly marks this high-risk footprint for human review.",
                    symbol["reference"],
                    str(lock_path),
                )
            )

    if not findings:
        findings.append(
            check_record(
                CHECK_STATUS_PASS,
                "HIGH_RISK_FOOTPRINTS_VERIFIED",
                "All high-risk footprint rows include the required extra proof.",
                "",
                str(lock_path),
            )
        )

    return build_audit_result(
        "high_risk_footprint_audit",
        "High Risk Footprint Audit",
        schematic,
        findings,
        {
            "high_risk_symbol_count": len(symbols),
            "lock_file": str(lock_path),
            "high_risk_references": [symbol["reference"] for symbol in symbols],
        },
    )


def main() -> int:
    parser = common_parser("Audit high-risk footprint proof requirements.")
    args = parser.parse_args()
    project_root, schematic = resolve_project_and_schematic(args.project, args.schematic)
    result = run_audit(schematic, project_root, args.lock_file)
    report_dir = default_output_dir(project_root, schematic)
    output_path = Path(args.output) if args.output else report_dir / "high_risk_footprints.md"
    json_path = Path(args.json_output) if args.json_output else report_dir / "high_risk_footprints.json"
    write_outputs(result, output_path, json_path)
    print(str(json_path))
    return exit_code_for(result, args.no_fail)


if __name__ == "__main__":
    raise SystemExit(main())
