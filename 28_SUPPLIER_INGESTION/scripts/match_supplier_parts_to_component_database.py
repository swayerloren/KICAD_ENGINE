#!/usr/bin/env python3
"""Match normalized supplier records to component database files by text evidence."""

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
                    records.append(item)
    return records


def nested(record: dict[str, Any], *keys: str) -> str:
    value: Any = record
    for key in keys:
        if not isinstance(value, dict):
            return ""
        value = value.get(key)
    return str(value).strip() if value not in (None, "") else ""


def collect_component_text(root: Path) -> list[dict[str, str]]:
    files: list[dict[str, str]] = []
    for pattern in ("*.md", "*.json"):
        for path in sorted(root.rglob(pattern), key=lambda item: str(item).lower()):
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            files.append({"path": str(path), "text": text.lower()})
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description="Match supplier records to 08_COMPONENT_DATABASE records.")
    parser.add_argument("--normalized-dir", default="28_SUPPLIER_INGESTION/normalized")
    parser.add_argument("--component-db", default="08_COMPONENT_DATABASE")
    parser.add_argument("--output-dir", default="28_SUPPLIER_INGESTION/reports")
    args = parser.parse_args()

    records = load_records(Path(args.normalized_dir))
    component_files = collect_component_text(Path(args.component_db))
    generated = datetime.now().isoformat(timespec="seconds")
    matches = []
    for record in records:
        mpn = nested(record, "manufacturer", "manufacturer_part_number")
        if not mpn:
            continue
        mpn_lower = mpn.lower()
        found = [item["path"] for item in component_files if mpn_lower in item["text"]]
        matches.append(
            {
                "manufacturer_part_number": mpn,
                "supplier": nested(record, "source", "supplier"),
                "supplier_sku": nested(record, "supplier_part", "supplier_sku"),
                "component_database_matches": found,
                "match_status": "CANDIDATE_MATCH" if found else "NO_MATCH_FOUND",
                "verification_status": "UNVERIFIED",
            }
        )

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "SUPPLIER_TO_COMPONENT_DATABASE_MATCHES.json"
    md_path = output_dir / "SUPPLIER_TO_COMPONENT_DATABASE_MATCHES.md"
    json_path.write_text(json.dumps({"generated_at": generated, "matches": matches}, indent=2), encoding="utf-8")
    lines = [
        "# Supplier To Component Database Matches",
        "",
        "Status: `AUTO_GENERATED_UNVERIFIED`",
        "",
        f"Generated: `{generated}`",
        "",
        "| MPN | Supplier | SKU | Match Status | Candidate Files |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in matches:
        files = "<br>".join(f"`{path}`" for path in item["component_database_matches"])
        lines.append(
            f"| `{item['manufacturer_part_number']}` | `{item['supplier']}` | `{item['supplier_sku']}` | `{item['match_status']}` | {files} |"
        )
    lines.extend(["", "Matches are text candidates only and require human review."])
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json_path)
    print(md_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
