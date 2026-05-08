#!/usr/bin/env python3
"""Check supplier-to-KiCad footprint match confidence rules."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ALLOWED_CONFIDENCE = {
    "VERIFIED_EXACT_PACKAGE_DRAWING",
    "VERIFIED_VENDOR_FOOTPRINT",
    "MATCHED_BY_PACKAGE_NAME_ONLY",
    "MATCHED_BY_GENERIC_FOOTPRINT",
    "UNVERIFIED",
    "REJECTED",
}

HIGH_RISK_LABELS = {"CONNECTOR", "USB-C_CONNECTOR", "RF_CONNECTOR", "PMOS_OR_MOSFET", "ESD_ARRAY", "MCU_MODULE", "BARE_MCU_PACKAGE", "REGULATOR"}


def repo_root() -> Path:
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "AGENTS.md").exists():
            return parent
    return Path.cwd()


ROOT = repo_root()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_markdown(path: Path, rows: list[dict[str, Any]]) -> None:
    lines = [
        "# Supplier Footprint Match Confidence Report",
        "",
        "| Record | Confidence | Result | Findings |",
        "| --- | --- | --- | --- |",
    ]
    if not rows:
        lines.append("| NONE | NONE | PASS | No records checked. |")
    for row in rows:
        findings = "<br>".join(row["findings"]) if row["findings"] else "No blocking findings."
        lines.append(f"| `{row['record_id']}` | `{row['confidence_level']}` | `{row['result']}` | {findings} |")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def iter_record_paths(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return [p for p in sorted(path.rglob("*.json")) if not p.name.endswith("_index.json")]


def has_human_review_evidence(record: dict[str, Any]) -> bool:
    for item in record.get("evidence", []):
        if isinstance(item, dict) and item.get("type") == "HUMAN_REVIEW" and item.get("status") == "VERIFIED":
            return True
    return False


def check_record(record: dict[str, Any]) -> dict[str, Any]:
    findings: list[str] = []
    confidence = record.get("confidence_level", "UNVERIFIED")
    high_risk = bool(set(record.get("high_risk_categories", [])) & HIGH_RISK_LABELS)
    package_source = str(record.get("package_drawing_source", "")).strip().upper()
    footprint_status = str(record.get("footprint_status", "")).strip().upper()
    orientation_status = str(record.get("connector_orientation_status", "")).strip().upper()
    if confidence not in ALLOWED_CONFIDENCE:
        findings.append(f"Invalid confidence level `{confidence}`.")
    if confidence == "VERIFIED_EXACT_PACKAGE_DRAWING" and package_source in {"", "UNKNOWN"}:
        findings.append("Exact package drawing confidence requires package drawing source.")
    if confidence == "VERIFIED_VENDOR_FOOTPRINT" and not record.get("evidence"):
        findings.append("Vendor footprint confidence requires evidence entries.")
    if high_risk and confidence in {"MATCHED_BY_PACKAGE_NAME_ONLY", "MATCHED_BY_GENERIC_FOOTPRINT"} and footprint_status == "VERIFIED":
        findings.append("High-risk footprint cannot be verified from package name or generic footprint.")
    if high_risk and confidence.startswith("VERIFIED") and not has_human_review_evidence(record):
        findings.append("High-risk verified confidence requires verified human-review evidence.")
    if any(label in record.get("high_risk_categories", []) for label in ["CONNECTOR", "USB-C_CONNECTOR", "RF_CONNECTOR"]) and orientation_status != "VERIFIED":
        findings.append("Connector/RF/USB-C match requires connector orientation verification before approval.")
    if record.get("record_type", "").startswith("EXAMPLE_ONLY") and confidence.startswith("VERIFIED"):
        findings.append("EXAMPLE_ONLY records must not be marked as verified.")
    result = "PASS" if not findings else "FAIL"
    return {
        "record_id": record.get("record_id", "UNKNOWN"),
        "mpn": record.get("mpn", "UNKNOWN"),
        "confidence_level": confidence,
        "high_risk": high_risk,
        "result": result,
        "findings": findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check supplier footprint match confidence.")
    parser.add_argument("--input", default=str(ROOT / "30_SUPPLIER_FOOTPRINT_MATCHES" / "matches"))
    parser.add_argument("--output-json", default=str(ROOT / "30_SUPPLIER_FOOTPRINT_MATCHES" / "reports" / "match_confidence_report.json"))
    parser.add_argument("--output-md", default=str(ROOT / "30_SUPPLIER_FOOTPRINT_MATCHES" / "reports" / "MATCH_CONFIDENCE_REPORT.md"))
    args = parser.parse_args()

    rows = []
    for path in iter_record_paths(Path(args.input)):
        try:
            record = read_json(path)
        except Exception as exc:
            rows.append({"record_id": str(path), "confidence_level": "UNKNOWN", "high_risk": False, "result": "FAIL", "findings": [f"Could not parse JSON: {exc}"]})
            continue
        if isinstance(record, dict) and "mpn" in record:
            rows.append(check_record(record))
    payload = {
        "records_checked": len(rows),
        "pass": sum(1 for row in rows if row["result"] == "PASS"),
        "fail": sum(1 for row in rows if row["result"] == "FAIL"),
        "rows": rows,
    }
    write_json(Path(args.output_json), payload)
    write_markdown(Path(args.output_md), rows)
    print(json.dumps({k: payload[k] for k in ["records_checked", "pass", "fail"]}, indent=2))
    return 0 if payload["fail"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

