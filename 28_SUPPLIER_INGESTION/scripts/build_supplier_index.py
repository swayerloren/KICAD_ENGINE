#!/usr/bin/env python3
"""Build an index of normalized supplier records."""

from __future__ import annotations

import argparse
import json
from collections import Counter
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
        if not isinstance(items, list):
            continue
        for item in items:
            if isinstance(item, dict):
                item["_source_file"] = str(path)
                records.append(item)
    return records


def nested(record: dict[str, Any], *keys: str, default: str = "") -> str:
    value: Any = record
    for key in keys:
        if not isinstance(value, dict):
            return default
        value = value.get(key)
    return str(value).strip() if value not in (None, "") else default


def main() -> int:
    parser = argparse.ArgumentParser(description="Build supplier ingestion index reports.")
    parser.add_argument("--normalized-dir", default="28_SUPPLIER_INGESTION/normalized")
    parser.add_argument("--output-dir", default="28_SUPPLIER_INGESTION/reports")
    args = parser.parse_args()

    normalized_dir = Path(args.normalized_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    records = load_records(normalized_dir)
    generated = datetime.now().isoformat(timespec="seconds")
    by_supplier = Counter(nested(r, "source", "supplier", default="Unknown") for r in records)
    by_status = Counter(str(r.get("verification_status", "UNVERIFIED")) for r in records)
    data = {
        "generated_at": generated,
        "record_count": len(records),
        "by_supplier": dict(by_supplier),
        "by_verification_status": dict(by_status),
        "records": records,
    }
    json_path = output_dir / "SUPPLIER_INDEX.json"
    md_path = output_dir / "SUPPLIER_INDEX.md"
    json_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    lines = [
        "# Supplier Ingestion Index",
        "",
        "Status: `AUTO_GENERATED`",
        "",
        f"Generated: `{generated}`",
        f"Record count: `{len(records)}`",
        "",
        "## By Supplier",
        "",
    ]
    for supplier, count in sorted(by_supplier.items()):
        lines.append(f"- `{supplier}`: {count}")
    lines.extend(["", "## By Verification Status", ""])
    for status, count in sorted(by_status.items()):
        lines.append(f"- `{status}`: {count}")
    lines.extend(["", "## Records", "", "| Supplier | MPN | SKU | Status | Source File |", "| --- | --- | --- | --- | --- |"])
    for record in records:
        lines.append(
            "| `{supplier}` | `{mpn}` | `{sku}` | `{status}` | `{source}` |".format(
                supplier=nested(record, "source", "supplier", default="Unknown"),
                mpn=nested(record, "manufacturer", "manufacturer_part_number"),
                sku=nested(record, "supplier_part", "supplier_sku"),
                status=record.get("verification_status", "UNVERIFIED"),
                source=record.get("_source_file", ""),
            )
        )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json_path)
    print(md_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
