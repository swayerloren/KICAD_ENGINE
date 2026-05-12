#!/usr/bin/env python3
"""Shared helpers for the footprint/package proof engine."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[3]
QUALITY_DIR = SCRIPT_DIR.parent / "schematic_quality"
if str(QUALITY_DIR) not in sys.path:
    sys.path.insert(0, str(QUALITY_DIR))

from schematic_quality_common import (  # type: ignore  # noqa: E402
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    CHECK_STATUS_WARN,
    extract_symbols,
    find_project_schematic,
    is_physical_symbol,
    load_schematic,
)


CHECK_STATUS_NEEDS_HUMAN_REVIEW = "NEEDS_HUMAN_REVIEW"

DEFAULT_LOCK_NAME = "FOOTPRINT_LOCK.csv"
DEFAULT_PARTS_LIST_NAME = "SCHEMATIC_READY_PARTS_LIST.md"
DEFAULT_REVIEW_LIST_NAME = "NEEDS_REVIEW_BEFORE_SCHEMATIC.md"

REQUIRED_LOCK_COLUMNS = [
    "reference",
    "value",
    "manufacturer_part_number",
    "package",
    "kicad_symbol",
    "kicad_footprint",
    "datasheet_or_source_url",
    "package_drawing_checked",
    "pin_mapping_checked",
    "3d_model_available",
    "risk",
    "human_review_required",
    "notes",
]

YES_VALUES = {"1", "true", "yes", "y", "pass", "passed", "verified", "available", "present", "checked"}
NO_VALUES = {"0", "false", "no", "n", "fail", "failed", "missing", "none", "not available", "unchecked", "blank"}


def normalize_text(*parts: object) -> str:
    return " ".join(str(part or "") for part in parts).strip().lower()


def reference_prefix(reference: str) -> str:
    match = re.match(r"[A-Z]+", reference.strip().upper())
    return match.group(0) if match else ""


def boolish(value: str) -> bool | None:
    normalized = str(value or "").strip().lower()
    if not normalized:
        return None
    if normalized in YES_VALUES:
        return True
    if normalized in NO_VALUES:
        return False
    return None


def source_reference_present(value: str) -> bool:
    return bool(str(value or "").strip())


def find_project_root_from_schematic(schematic: Path) -> Path | None:
    resolved = schematic.resolve()
    for parent in resolved.parents:
        if (parent / "kicad").exists():
            return parent
    return None


def resolve_project_and_schematic(project_arg: str, schematic_arg: str) -> tuple[Path | None, Path]:
    if schematic_arg:
        schematic = Path(schematic_arg).resolve()
        project_root = Path(project_arg).resolve() if project_arg else find_project_root_from_schematic(schematic)
        return project_root, schematic
    if not project_arg:
        raise SystemExit("Either --project or --schematic is required.")
    project_root = Path(project_arg).resolve()
    return project_root, find_project_schematic(project_root)


def common_parser(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--project", default="", help="Active project root containing a kicad/ folder.")
    parser.add_argument("--schematic", default="", help="Exact .kicad_sch path.")
    parser.add_argument("--lock-file", default="", help="Optional explicit lock-file path.")
    parser.add_argument("--output", default="", help="Optional markdown output path.")
    parser.add_argument("--json-output", default="", help="Optional JSON output path.")
    parser.add_argument("--no-fail", action="store_true", help="Return exit code 0 even when the audit fails.")
    return parser


def classify_symbol(symbol: dict[str, Any]) -> dict[str, str | bool]:
    reference = str(symbol.get("reference", "")).strip()
    value = str(symbol.get("value", "")).strip()
    lib_id = str(symbol.get("lib_id", "")).strip()
    text = normalize_text(reference, value, lib_id, symbol.get("footprint", ""))
    prefix = reference_prefix(reference)

    category = "generic_component"
    risk = "MEDIUM"
    reason = "Physical symbol requires a lock row and source evidence."

    if prefix == "TP" or "testpoint" in text or "test point" in text:
        category = "test_pad"
        risk = "HIGH"
        reason = "Test pads require intentional footprint sizing and service intent."
    elif prefix == "MH" or "mountinghole" in text or "mounting hole" in text:
        category = "mounting_hole"
        risk = "HIGH"
        reason = "Mounting holes are mechanical-critical footprints."
    elif prefix == "J" and ("usb" in text or "receptacle" in text or "type-c" in text):
        category = "usb_connector"
        risk = "HIGH"
        reason = "USB connectors require exact mechanical and orientation proof."
    elif prefix == "J" and ("barrel" in text or "dc jack" in text or "power jack" in text or "jack" in text):
        category = "barrel_jack"
        risk = "HIGH"
        reason = "Barrel jacks require exact mechanical orientation proof."
    elif prefix == "J":
        category = "connector"
        risk = "HIGH"
        reason = "Connectors require exact package and orientation proof."
    elif prefix == "Q" or "mosfet" in text or "pmos" in text or "reverse polarity" in text or "ao3401" in text:
        category = "pmos_or_fet"
        risk = "HIGH"
        reason = "PMOS and FETs require explicit pin-mapping proof."
    elif prefix == "U" and ("esp32" in text or "stm32" in text or "module" in text or "mcu" in text):
        category = "module_or_mcu"
        risk = "HIGH"
        reason = "Modules and MCUs are high-risk package assignments."
    elif prefix == "U" and ("regulator" in text or "buck" in text or "ldo" in text or "ap63203" in text):
        category = "regulator"
        risk = "HIGH"
        reason = "Regulators require package and pinout proof."
    elif prefix == "SW" or "sw_push" in text or "button" in text:
        category = "switch"
        risk = "HIGH"
        reason = "Switches are high-risk due to mechanical orientation and pin format."
    elif prefix == "D" and ("esd" in text or "tvs" in text or "tpd2eusb" in text):
        category = "esd_or_tvs"
        risk = "HIGH"
        reason = "ESD and TVS devices are high-risk polarity-sensitive parts."
    elif prefix == "U" and ("esd" in text or "tvs" in text or "tpd2eusb" in text or "protection" in text):
        category = "esd_or_tvs"
        risk = "HIGH"
        reason = "Protection devices require exact package and orientation proof."
    elif prefix == "D":
        category = "diode_or_led"
        risk = "HIGH"
        reason = "Diodes and LEDs are polarity-sensitive footprints."
    elif prefix == "F" or "fuse" in text or "polyfuse" in text:
        category = "fuse"
        risk = "HIGH"
        reason = "Fuses require exact package and service-intent proof."
    elif prefix == "L" or "inductor" in text:
        category = "inductor"
        risk = "HIGH"
        reason = "Inductors require exact package and current-family proof."
    elif prefix == "C" and ("electrolytic" in text or "tantalum" in text or "polarized" in text):
        category = "polarized_capacitor"
        risk = "HIGH"
        reason = "Polarized capacitors require package and polarity review."
    elif prefix in {"R", "C"}:
        category = "passive"
        risk = "LOW"
        reason = "Basic passives still require exact package evidence but are usually low risk."
    else:
        category = "general_component"
        risk = "MEDIUM"
        reason = "Component is physical and needs package/source verification."

    return {
        "reference": reference,
        "value": value,
        "lib_id": lib_id,
        "footprint": str(symbol.get("footprint", "")).strip(),
        "category": category,
        "risk": risk,
        "high_risk": risk == "HIGH",
        "risk_reason": reason,
    }


def load_physical_symbols(schematic: Path) -> list[dict[str, Any]]:
    root = load_schematic(schematic)
    symbols = [symbol for symbol in extract_symbols(root) if is_physical_symbol(symbol)]
    enriched: list[dict[str, Any]] = []
    for symbol in symbols:
        enriched_symbol = dict(symbol)
        enriched_symbol.update(classify_symbol(symbol))
        enriched.append(enriched_symbol)
    return enriched


def locate_lock_file(project_root: Path | None, explicit_path: str = "") -> Path | None:
    if explicit_path:
        return Path(explicit_path).resolve()
    if project_root is None:
        return None
    return project_root / DEFAULT_LOCK_NAME


def read_lock_rows(lock_path: Path | None) -> tuple[list[dict[str, str]], dict[str, dict[str, str]]]:
    if lock_path is None or not lock_path.exists():
        return [], {}
    rows: list[dict[str, str]] = []
    index: dict[str, dict[str, str]] = {}
    with lock_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for raw_row in reader:
            row = {str(key or "").strip(): str(value or "").strip() for key, value in raw_row.items()}
            rows.append(row)
            reference = row.get("reference", "").upper()
            if reference:
                index[reference] = row
    return rows, index


def summarize_status(findings: list[dict[str, str]]) -> dict[str, Any]:
    counts = Counter(item["status"] for item in findings)
    if counts.get(CHECK_STATUS_FAIL, 0):
        status = CHECK_STATUS_FAIL
    elif counts.get(CHECK_STATUS_NEEDS_HUMAN_REVIEW, 0):
        status = CHECK_STATUS_NEEDS_HUMAN_REVIEW
    elif counts.get(CHECK_STATUS_WARN, 0):
        status = CHECK_STATUS_WARN
    else:
        status = CHECK_STATUS_PASS
    return {
        "status": status,
        "counts": {
            CHECK_STATUS_PASS: counts.get(CHECK_STATUS_PASS, 0),
            CHECK_STATUS_WARN: counts.get(CHECK_STATUS_WARN, 0),
            CHECK_STATUS_FAIL: counts.get(CHECK_STATUS_FAIL, 0),
            CHECK_STATUS_NEEDS_HUMAN_REVIEW: counts.get(CHECK_STATUS_NEEDS_HUMAN_REVIEW, 0),
        },
    }


def check_record(status: str, code: str, message: str, reference: str = "", evidence: str = "") -> dict[str, str]:
    return {
        "status": status,
        "code": code,
        "reference": reference,
        "message": message,
        "evidence": evidence,
    }


def build_audit_result(
    audit_id: str,
    title: str,
    schematic: Path,
    findings: list[dict[str, str]],
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    result: dict[str, Any] = {
        "audit_id": audit_id,
        "title": title,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "schematic": str(schematic),
        "findings": findings,
        "summary": summarize_status(findings),
    }
    if extra:
        result.update(extra)
    return result


def audit_markdown(result: dict[str, Any]) -> str:
    counts = result["summary"]["counts"]
    lines = [
        f"# {result['title']}",
        "",
        f"Status: `{result['summary']['status']}`",
        "",
        f"Generated: `{result['generated_at']}`",
        f"Schematic: `{result['schematic']}`",
        "",
        "## Summary",
        "",
        f"- Pass: {counts[CHECK_STATUS_PASS]}",
        f"- Warn: {counts[CHECK_STATUS_WARN]}",
        f"- Fail: {counts[CHECK_STATUS_FAIL]}",
        f"- Needs human review: {counts[CHECK_STATUS_NEEDS_HUMAN_REVIEW]}",
        "",
        "## Findings",
        "",
        "| Status | Code | Reference | Message | Evidence |",
        "| --- | --- | --- | --- | --- |",
    ]
    for finding in result["findings"]:
        lines.append(
            "| `{status}` | `{code}` | `{reference}` | {message} | `{evidence}` |".format(
                status=finding["status"],
                code=finding["code"],
                reference=finding.get("reference", ""),
                message=str(finding["message"]).replace("|", "\\|"),
                evidence=str(finding.get("evidence", "")).replace("|", "\\|"),
            )
        )
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- This is a read-only audit.",
            "- Blank footprints, missing lock rows, and high-risk evidence gaps are PCB-update blockers.",
            "",
        ]
    )
    return "\n".join(lines)


def write_outputs(result: dict[str, Any], output: Path | None, json_output: Path | None) -> None:
    if json_output:
        json_output.parent.mkdir(parents=True, exist_ok=True)
        json_output.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    markdown = audit_markdown(result)
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(markdown, encoding="utf-8")
    else:
        print(markdown)


def exit_code_for(result: dict[str, Any], no_fail: bool) -> int:
    if no_fail:
        return 0
    return 0 if result["summary"]["status"] == CHECK_STATUS_PASS else 1


def default_output_dir(project_root: Path | None, schematic: Path) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if project_root is not None:
        return project_root / "reports" / "footprint_package" / timestamp
    return schematic.parent / "reports" / "footprint_package" / timestamp


def support_file_paths(project_root: Path | None) -> dict[str, str]:
    if project_root is None:
        return {
            "footprint_lock": "",
            "parts_list": "",
            "needs_review_list": "",
        }
    return {
        "footprint_lock": str(project_root / DEFAULT_LOCK_NAME),
        "parts_list": str(project_root / DEFAULT_PARTS_LIST_NAME),
        "needs_review_list": str(project_root / DEFAULT_REVIEW_LIST_NAME),
    }
