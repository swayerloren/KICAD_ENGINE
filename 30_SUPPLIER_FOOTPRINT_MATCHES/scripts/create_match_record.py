#!/usr/bin/env python3
"""Create a supplier-to-KiCad footprint match record.

This script is offline and non-destructive. It does not call supplier APIs,
download PDFs, or edit KiCad files.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
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

ALLOWED_SUPPLIERS = {"digikey", "mouser", "jlcpcb", "lcsc", "manual_verified"}


def repo_root() -> Path:
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "AGENTS.md").exists():
            return parent
    return Path.cwd()


ROOT = repo_root()


def utc_stamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slugify(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "_", value.strip().upper()).strip("_")
    return slug or "UNKNOWN"


def split_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def detect_high_risk(text: str) -> list[str]:
    lowered = text.lower()
    risks: list[str] = []
    checks = [
        ("USB-C_CONNECTOR", ["usb-c", "usb c", "type-c", "type c", "receptacle"]),
        ("RF_CONNECTOR", ["u.fl", "ufl", "ipex", "mhf", "sma", "rp-sma"]),
        ("CONNECTOR", ["connector", "header", "terminal", "barrel jack", "jack"]),
        ("PMOS_OR_MOSFET", ["pmos", "p-channel", "mosfet", "ao3401"]),
        ("ESD_ARRAY", ["esd", "tvs", "tusb", "tpd"]),
        ("MCU_MODULE", ["esp32", "wroom", "wrover", "mini-1", "module"]),
        ("BARE_MCU_PACKAGE", ["stm32", "pic", "rp2040", "qfn", "bga", "wlcsp", "lqfp", "ufqfp"]),
        ("REGULATOR", ["regulator", "buck", "ldo", "ap63203", "lm2596", "ams1117"]),
    ]
    for label, terms in checks:
        if any(term in lowered for term in terms):
            risks.append(label)
    return list(dict.fromkeys(risks))


def normalize_record(record: dict[str, Any]) -> dict[str, Any]:
    text = " ".join(str(record.get(key, "")) for key in ["mpn", "manufacturer", "package_name_from_supplier", "kicad_footprint_candidate"])
    risks = list(dict.fromkeys(record.get("high_risk_categories", []) + detect_high_risk(text)))
    record["high_risk_categories"] = risks
    if risks:
        record["human_review_required"] = True
    if record["confidence_level"] not in ALLOWED_CONFIDENCE:
        record["confidence_level"] = "UNVERIFIED"
    if record["supplier"] not in ALLOWED_SUPPLIERS:
        record["supplier"] = "manual_verified"
    return record


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_markdown(path: Path, record: dict[str, Any]) -> None:
    lines = [
        f"# Supplier Footprint Match - {record['mpn']}",
        "",
        f"Status: `{record['confidence_level']}`",
        f"Record type: `{record['record_type']}`",
        "",
        "## Identity",
        "",
        f"- Manufacturer: `{record['manufacturer']}`",
        f"- MPN: `{record['mpn']}`",
        f"- Supplier: `{record['supplier']}`",
        f"- Supplier SKU: `{record['supplier_sku']}`",
        f"- JLC/LCSC part number: `{record['jlc_lcsc_part_number']}`",
        "",
        "## Sources",
        "",
        f"- Datasheet URL: `{record['datasheet_url']}`",
        f"- Supplier package name: `{record['package_name_from_supplier']}`",
        f"- Package drawing source: `{record['package_drawing_source']}`",
        "",
        "## KiCad Candidates",
        "",
        f"- Symbol: `{record['kicad_symbol_candidate']}`",
        f"- Footprint: `{record['kicad_footprint_candidate']}`",
        f"- 3D model: `{record['kicad_3d_model_candidate']}`",
        "",
        "## Status",
        "",
        f"- Footprint status: `{record['footprint_status']}`",
        f"- Pinout status: `{record['pinout_status']}`",
        f"- Connector orientation status: `{record['connector_orientation_status']}`",
        f"- Human review required: `{record['human_review_required']}`",
        f"- High-risk categories: `{', '.join(record['high_risk_categories']) or 'NONE'}`",
        "",
        "## Notes",
        "",
    ]
    for note in record["notes"]:
        lines.append(f"- {note}")
    lines.extend(
        [
            "",
            "## Rule",
            "",
            "This match record does not approve a footprint unless exact package drawing evidence, pinout/pad mapping, orientation review, and human review requirements are satisfied.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a supplier-to-KiCad footprint match record.")
    parser.add_argument("--manufacturer", required=True)
    parser.add_argument("--mpn", required=True)
    parser.add_argument("--supplier", default="manual_verified", choices=sorted(ALLOWED_SUPPLIERS))
    parser.add_argument("--supplier-sku", default="UNKNOWN")
    parser.add_argument("--jlc-lcsc-part-number", default="UNKNOWN")
    parser.add_argument("--datasheet-url", default="UNKNOWN")
    parser.add_argument("--package-name-from-supplier", default="UNKNOWN")
    parser.add_argument("--package-drawing-source", default="UNKNOWN")
    parser.add_argument("--kicad-symbol-candidate", default="UNKNOWN")
    parser.add_argument("--kicad-footprint-candidate", default="UNKNOWN")
    parser.add_argument("--kicad-3d-model-candidate", default="UNKNOWN")
    parser.add_argument("--footprint-status", default="UNVERIFIED")
    parser.add_argument("--pinout-status", default="UNVERIFIED")
    parser.add_argument("--connector-orientation-status", default="UNVERIFIED")
    parser.add_argument("--confidence-level", default="UNVERIFIED", choices=sorted(ALLOWED_CONFIDENCE))
    parser.add_argument("--high-risk-categories", default="")
    parser.add_argument("--note", action="append", default=[])
    parser.add_argument("--example-only", action="store_true")
    parser.add_argument("--output-dir", help="Output directory. Defaults to matches/<supplier>.")
    args = parser.parse_args()

    now = utc_stamp()
    record_type = "EXAMPLE_ONLY_SUPPLIER_FOOTPRINT_MATCH" if args.example_only else "SUPPLIER_FOOTPRINT_MATCH"
    prefix = "EXAMPLE_ONLY_" if args.example_only else ""
    record_id = f"{prefix}{slugify(args.supplier)}_{slugify(args.manufacturer)}_{slugify(args.mpn)}"
    record = normalize_record(
        {
            "record_id": record_id,
            "record_type": record_type,
            "manufacturer": args.manufacturer,
            "mpn": args.mpn,
            "supplier": args.supplier,
            "supplier_sku": args.supplier_sku,
            "jlc_lcsc_part_number": args.jlc_lcsc_part_number,
            "datasheet_url": args.datasheet_url,
            "package_name_from_supplier": args.package_name_from_supplier,
            "package_drawing_source": args.package_drawing_source,
            "kicad_symbol_candidate": args.kicad_symbol_candidate,
            "kicad_footprint_candidate": args.kicad_footprint_candidate,
            "kicad_3d_model_candidate": args.kicad_3d_model_candidate,
            "footprint_status": args.footprint_status,
            "pinout_status": args.pinout_status,
            "connector_orientation_status": args.connector_orientation_status,
            "human_review_required": True,
            "confidence_level": args.confidence_level,
            "high_risk_categories": split_csv(args.high_risk_categories),
            "evidence": [],
            "notes": args.note or ["Created as placeholder match record. Exact footprint verification required."],
            "created_at": now,
            "updated_at": now,
        }
    )
    output_dir = Path(args.output_dir) if args.output_dir else ROOT / "30_SUPPLIER_FOOTPRINT_MATCHES" / "matches" / record["supplier"]
    json_path = output_dir / f"{record_id}.json"
    md_path = output_dir / f"{record_id}.md"
    write_json(json_path, record)
    write_markdown(md_path, record)
    print(json.dumps({"json": str(json_path), "markdown": str(md_path), "record_id": record_id}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

