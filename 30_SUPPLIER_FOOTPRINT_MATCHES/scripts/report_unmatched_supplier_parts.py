#!/usr/bin/env python3
"""Report normalized supplier parts that do not have footprint match records."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


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


def write_markdown(path: Path, payload: dict[str, Any]) -> None:
    lines = [
        "# Unmatched Supplier Parts Report",
        "",
        "Status: `GENERATED_REPORT`",
        "",
        f"- Supplier records scanned: {payload['summary']['supplier_records_scanned']}",
        f"- Match records scanned: {payload['summary']['match_records_scanned']}",
        f"- Unmatched supplier records: {payload['summary']['unmatched_supplier_records']}",
        "",
        "| Supplier | MPN | SKU | Source File |",
        "| --- | --- | --- | --- |",
    ]
    if not payload["unmatched"]:
        lines.append("| NONE | NONE | NONE | No unmatched supplier records found or no supplier records available. |")
    for row in payload["unmatched"]:
        lines.append(f"| `{row['supplier']}` | `{row['mpn']}` | `{row['supplier_sku']}` | `{row['source_file']}` |")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def as_records(data: Any) -> list[dict[str, Any]]:
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if isinstance(data, dict):
        for key in ["records", "parts", "supplier_parts", "normalized_records"]:
            if isinstance(data.get(key), list):
                return [item for item in data[key] if isinstance(item, dict)]
        if data.get("mpn") or data.get("manufacturer_part_number") or data.get("part_number"):
            return [data]
    return []


def collect_supplier_parts(root: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    if not root.exists():
        return rows
    for path in sorted(root.rglob("*.json")):
        try:
            records = as_records(read_json(path))
        except Exception:
            continue
        for record in records:
            mpn = str(record.get("mpn") or record.get("manufacturer_part_number") or record.get("part_number") or "").strip()
            sku = str(record.get("supplier_sku") or record.get("sku") or record.get("digikey_part_number") or record.get("mouser_part_number") or record.get("lcsc_part_number") or "").strip()
            supplier = str(record.get("supplier") or record.get("source") or "UNKNOWN").strip().lower()
            if mpn or sku:
                rows.append({"mpn": mpn, "supplier_sku": sku, "supplier": supplier, "source_file": str(path)})
    return rows


def collect_match_keys(root: Path) -> tuple[set[str], int]:
    keys: set[str] = set()
    if not root.exists():
        return keys, 0
    record_count = 0
    for path in sorted(root.rglob("*.json")):
        try:
            data = read_json(path)
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        if data.get("mpn") or data.get("supplier_sku") or data.get("jlc_lcsc_part_number"):
            record_count += 1
        for value in [data.get("mpn"), data.get("supplier_sku"), data.get("jlc_lcsc_part_number")]:
            if value and str(value).upper() != "UNKNOWN":
                keys.add(str(value).strip().lower())
    return keys, record_count


def main() -> int:
    parser = argparse.ArgumentParser(description="Report supplier records without footprint match records.")
    parser.add_argument("--supplier-root", default=str(ROOT / "28_SUPPLIER_INGESTION" / "normalized"))
    parser.add_argument("--matches-root", default=str(ROOT / "30_SUPPLIER_FOOTPRINT_MATCHES" / "matches"))
    parser.add_argument("--output-json", default=str(ROOT / "30_SUPPLIER_FOOTPRINT_MATCHES" / "reports" / "unmatched_supplier_parts.json"))
    parser.add_argument("--output-md", default=str(ROOT / "30_SUPPLIER_FOOTPRINT_MATCHES" / "reports" / "UNMATCHED_SUPPLIER_PARTS.md"))
    args = parser.parse_args()

    supplier_parts = collect_supplier_parts(Path(args.supplier_root))
    match_keys, match_record_count = collect_match_keys(Path(args.matches_root))
    unmatched = []
    for row in supplier_parts:
        keys = {row["mpn"].lower(), row["supplier_sku"].lower()} - {""}
        if not keys & match_keys:
            unmatched.append(row)
    payload = {
        "summary": {
            "supplier_records_scanned": len(supplier_parts),
            "match_records_scanned": match_record_count,
            "match_keys_scanned": len(match_keys),
            "unmatched_supplier_records": len(unmatched),
        },
        "unmatched": unmatched,
    }
    write_json(Path(args.output_json), payload)
    write_markdown(Path(args.output_md), payload)
    print(json.dumps(payload["summary"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
