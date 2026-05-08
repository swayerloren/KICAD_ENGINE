#!/usr/bin/env python3
"""Create a supplier metadata gap report from normalized records."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any


def load_records(root: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*.json"), key=lambda item: str(item).lower()):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        items = data.get("records") if isinstance(data, dict) else data
        if isinstance(items, dict):
            items = [items]
        if isinstance(items, list):
            for item in items:
                if isinstance(item, dict):
                    item["_source_file"] = str(path)
                    records.append(item)
    return records


def nested(record: dict[str, Any], *keys: str) -> Any:
    value: Any = record
    for key in keys:
        if not isinstance(value, dict):
            return None
        value = value.get(key)
    return value


def missing(value: Any) -> bool:
    return value in (None, "", [], {}) or str(value).strip().lower() in {"unknown", "unverified"}


def gaps_for(record: dict[str, Any]) -> list[str]:
    gaps: list[str] = []
    if missing(nested(record, "manufacturer", "manufacturer_part_number")):
        gaps.append("missing_mpn")
    if missing(nested(record, "supplier_part", "supplier_sku")):
        gaps.append("missing_supplier_sku")
    if missing(nested(record, "source", "source_url")) and missing(nested(record, "source", "source_file")):
        gaps.append("missing_source_evidence")
    if missing(nested(record, "source", "retrieved_at")):
        gaps.append("missing_source_date")
    if not nested(record, "datasheets"):
        gaps.append("missing_datasheet_link")
    if missing(nested(record, "package", "manufacturer_package")) and missing(nested(record, "package", "supplier_package")):
        gaps.append("missing_package_text")
    if nested(record, "footprint_risk", "footprint_status") != "FOOTPRINT_VERIFIED_AGAINST_DRAWING":
        gaps.append("footprint_not_verified")
    return gaps


def main() -> int:
    parser = argparse.ArgumentParser(description="Create supplier ingestion gap report.")
    parser.add_argument("--normalized-dir", default="28_SUPPLIER_INGESTION/normalized")
    parser.add_argument("--output-dir", default="28_SUPPLIER_INGESTION/reports")
    args = parser.parse_args()

    records = load_records(Path(args.normalized_dir))
    generated = datetime.now().isoformat(timespec="seconds")
    rows = []
    for record in records:
        gaps = gaps_for(record)
        if gaps:
            rows.append(
                {
                    "manufacturer_part_number": nested(record, "manufacturer", "manufacturer_part_number") or "",
                    "supplier": nested(record, "source", "supplier") or "Unknown",
                    "supplier_sku": nested(record, "supplier_part", "supplier_sku") or "",
                    "gaps": gaps,
                    "source_file": record.get("_source_file", ""),
                }
            )

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "SUPPLIER_GAP_REPORT.json"
    md_path = output_dir / "SUPPLIER_GAP_REPORT.md"
    json_path.write_text(json.dumps({"generated_at": generated, "gaps": rows}, indent=2), encoding="utf-8")
    lines = [
        "# Supplier Gap Report",
        "",
        "Status: `AUTO_GENERATED`",
        "",
        f"Generated: `{generated}`",
        f"Records with gaps: `{len(rows)}`",
        "",
        "| Supplier | MPN | SKU | Gaps | Source File |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| `{row['supplier']}` | `{row['manufacturer_part_number']}` | `{row['supplier_sku']}` | `{', '.join(row['gaps'])}` | `{row['source_file']}` |"
        )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json_path)
    print(md_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
