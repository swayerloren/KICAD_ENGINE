#!/usr/bin/env python3
"""Normalize supplier part records without live API calls or downloads."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "supplier_part_normalized_v0.1"


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def read_records(path: Path) -> list[dict[str, Any]]:
    if path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            if isinstance(data.get("records"), list):
                return [dict(item) for item in data["records"] if isinstance(item, dict)]
            return [data]
        if isinstance(data, list):
            return [dict(item) for item in data if isinstance(item, dict)]
        raise ValueError(f"Unsupported JSON structure in {path}")
    if path.suffix.lower() == ".csv":
        with path.open(newline="", encoding="utf-8-sig") as handle:
            return [dict(row) for row in csv.DictReader(handle)]
    raise ValueError(f"Unsupported input type: {path.suffix}")


def clean(value: Any, default: str = "") -> str:
    if value is None:
        return default
    text = str(value).strip()
    return text if text else default


def pick(row: dict[str, Any], *names: str, default: str = "") -> str:
    lower = {str(key).lower(): value for key, value in row.items()}
    for name in names:
        if name in row and clean(row[name]):
            return clean(row[name])
        value = lower.get(name.lower())
        if clean(value):
            return clean(value)
    return default


def parse_int(value: Any) -> int | None:
    text = clean(value)
    if not text:
        return None
    try:
        return int(float(text.replace(",", "")))
    except ValueError:
        return None


def parse_price_breaks(value: Any) -> list[dict[str, Any]]:
    text = clean(value)
    if not text:
        return []
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return [{"raw": text, "status": "UNVERIFIED"}]
    if isinstance(data, list):
        return data
    return [{"raw": data, "status": "UNVERIFIED"}]


def normalize_record(
    row: dict[str, Any],
    *,
    source_file: str = "",
    default_source_type: str = "manual_source_link",
) -> dict[str, Any]:
    supplier = pick(row, "supplier", "distributor", default="Unknown")
    source_url = pick(row, "source_url", "supplier_part_url", "url")
    datasheet_url = pick(row, "datasheet_url", "datasheet", "document_url")
    verification_status = pick(row, "verification_status", default="UNVERIFIED")
    retrieved_at = pick(row, "retrieved_at", "source_date", "imported_at", default=now_iso())
    source_type = pick(row, "source_type", default=default_source_type)
    mpn = pick(row, "manufacturer_part_number", "mpn", "part_number")
    manufacturer = pick(row, "manufacturer", "manufacturer_name", "vendor")
    supplier_sku = pick(row, "supplier_sku", "sku", "supplier_part_number")
    price_breaks = parse_price_breaks(pick(row, "price_breaks_json", "price_breaks"))

    datasheets: list[dict[str, Any]] = []
    if datasheet_url:
        datasheets.append(
            {
                "document_title": pick(row, "datasheet_title", default=f"{mpn} datasheet link"),
                "document_type": pick(row, "document_type", default="datasheet"),
                "source_url": datasheet_url,
                "public_redistribution_status": pick(
                    row, "public_redistribution_status", default="REDISTRIBUTION_UNKNOWN"
                ),
                "verification_status": verification_status,
            }
        )

    package_text = pick(row, "manufacturer_package", "package", "package_type")
    supplier_package = pick(row, "supplier_package", "case_package", default=package_text)
    footprint_notes = []
    if not package_text and not supplier_package:
        footprint_notes.append("Package data missing; footprint cannot be inferred.")
    else:
        footprint_notes.append("Package text is candidate evidence only; verify footprint against exact drawing.")

    return {
        "schema_version": SCHEMA_VERSION,
        "verification_status": verification_status or "UNVERIFIED",
        "source": {
            "supplier": supplier,
            "source_type": source_type,
            "source_url": source_url,
            "source_file": source_file,
            "retrieved_at": retrieved_at,
            "terms_review_status": pick(row, "terms_review_status", default="UNVERIFIED"),
        },
        "manufacturer": {
            "name": manufacturer,
            "manufacturer_part_number": mpn,
            "lifecycle_status": pick(row, "lifecycle_status", default="UNKNOWN"),
        },
        "supplier_part": {
            "supplier_sku": supplier_sku,
            "supplier_part_url": pick(row, "supplier_part_url", default=source_url),
            "description": pick(row, "description"),
            "category": pick(row, "category"),
        },
        "package": {
            "supplier_package": supplier_package,
            "manufacturer_package": package_text,
            "pin_count": pick(row, "pin_count", default="Unknown"),
            "package_confidence": "UNVERIFIED",
        },
        "inventory_price": {
            "currency": pick(row, "currency"),
            "stock_quantity": parse_int(pick(row, "stock_quantity", "stock")),
            "minimum_order_quantity": parse_int(pick(row, "minimum_order_quantity", "moq")),
            "price_breaks": price_breaks,
        },
        "datasheets": datasheets,
        "footprint_risk": {
            "kicad_symbol_candidates": [],
            "kicad_footprint_candidates": [],
            "footprint_status": "UNVERIFIED",
            "risk_notes": footprint_notes,
        },
        "notes": [pick(row, "notes")] if pick(row, "notes") else [],
    }


def safe_stem(path: Path) -> str:
    return "".join(ch if ch.isalnum() or ch in "-_." else "_" for ch in path.stem)


def write_outputs(records: list[dict[str, Any]], output_dir: Path, stem: str) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": now_iso(),
        "record_count": len(records),
        "records": records,
    }
    json_path = output_dir / f"{stem}.normalized.json"
    md_path = output_dir / f"{stem}.normalized.md"
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    lines = [
        "# Normalized Supplier Parts",
        "",
        "Status: `AUTO_GENERATED_UNVERIFIED`",
        "",
        f"Generated: `{payload['generated_at']}`",
        f"Record count: `{len(records)}`",
        "",
        "| Supplier | MPN | Supplier SKU | Verification | Footprint Status |",
        "| --- | --- | --- | --- | --- |",
    ]
    for record in records:
        lines.append(
            "| `{supplier}` | `{mpn}` | `{sku}` | `{status}` | `{footprint}` |".format(
                supplier=record["source"]["supplier"],
                mpn=record["manufacturer"]["manufacturer_part_number"],
                sku=record["supplier_part"]["supplier_sku"],
                status=record["verification_status"],
                footprint=record["footprint_risk"]["footprint_status"],
            )
        )
    lines.extend(
        [
            "",
            "## Rules",
            "",
            "- This output is normalized metadata, not sourcing approval.",
            "- Do not treat supplier package text as footprint verification.",
            "- Do not treat stock/pricing as current without checking `retrieved_at`.",
            "- Datasheet links are link-only unless redistribution is reviewed.",
            "",
        ]
    )
    md_path.write_text("\n".join(lines), encoding="utf-8")
    return json_path, md_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize supplier part records from JSON or CSV.")
    parser.add_argument("--input", required=True, help="Input JSON or CSV file.")
    parser.add_argument("--output-dir", default="28_SUPPLIER_INGESTION/normalized")
    parser.add_argument("--source-type", default="manual_source_link")
    args = parser.parse_args()

    input_path = Path(args.input).resolve()
    records = [
        normalize_record(row, source_file=str(input_path), default_source_type=args.source_type)
        for row in read_records(input_path)
    ]
    json_path, md_path = write_outputs(records, Path(args.output_dir), safe_stem(input_path))
    print(json_path)
    print(md_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
