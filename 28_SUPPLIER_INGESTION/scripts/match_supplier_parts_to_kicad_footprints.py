#!/usr/bin/env python3
"""Create conservative footprint-risk candidate notes from supplier package text."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any


KEYWORD_MAP = {
    "qfn": ["QFN", "DFN"],
    "dfn": ["DFN", "QFN"],
    "qfp": ["QFP", "LQFP", "TQFP"],
    "lqfp": ["LQFP", "QFP"],
    "tqfp": ["TQFP", "QFP"],
    "soic": ["SOIC"],
    "sop": ["SOIC", "SOP"],
    "sot-23": ["SOT-23"],
    "sot23": ["SOT-23"],
    "usb-c": ["USB_C", "USB-C"],
    "u.fl": ["U.FL", "IPEX", "MHF"],
    "sma": ["SMA"],
    "module": ["Module"],
}


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
            records.extend(item for item in items if isinstance(item, dict))
    return records


def nested(record: dict[str, Any], *keys: str) -> str:
    value: Any = record
    for key in keys:
        if not isinstance(value, dict):
            return ""
        value = value.get(key)
    return str(value).strip() if value not in (None, "") else ""


def package_keywords(text: str) -> list[str]:
    lowered = text.lower()
    found: list[str] = []
    for key, values in KEYWORD_MAP.items():
        if key in lowered:
            found.extend(values)
    pin_match = re.search(r"\b(\d{2,3})\s*(pin|pins|p)\b", lowered)
    if pin_match:
        found.append(pin_match.group(1))
    return sorted(set(found))


def main() -> int:
    parser = argparse.ArgumentParser(description="Match supplier package text to candidate KiCad footprint keywords.")
    parser.add_argument("--normalized-dir", default="28_SUPPLIER_INGESTION/normalized")
    parser.add_argument("--output-dir", default="28_SUPPLIER_INGESTION/reports")
    args = parser.parse_args()

    records = load_records(Path(args.normalized_dir))
    generated = datetime.now().isoformat(timespec="seconds")
    rows = []
    for record in records:
        mpn = nested(record, "manufacturer", "manufacturer_part_number")
        package_text = " ".join(
            [
                nested(record, "package", "supplier_package"),
                nested(record, "package", "manufacturer_package"),
                nested(record, "supplier_part", "description"),
            ]
        )
        keywords = package_keywords(package_text)
        rows.append(
            {
                "manufacturer_part_number": mpn,
                "supplier": nested(record, "source", "supplier"),
                "supplier_sku": nested(record, "supplier_part", "supplier_sku"),
                "package_text": package_text.strip(),
                "candidate_keywords": keywords,
                "match_status": "CANDIDATE_ONLY" if keywords else "NO_CANDIDATE",
                "verification_status": "UNVERIFIED",
                "human_review_required": True,
                "notes": "Supplier package text is not footprint verification.",
            }
        )

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "SUPPLIER_TO_KICAD_FOOTPRINT_CANDIDATES.json"
    md_path = output_dir / "SUPPLIER_TO_KICAD_FOOTPRINT_CANDIDATES.md"
    json_path.write_text(json.dumps({"generated_at": generated, "matches": rows}, indent=2), encoding="utf-8")
    lines = [
        "# Supplier To KiCad Footprint Candidates",
        "",
        "Status: `AUTO_GENERATED_UNVERIFIED`",
        "",
        f"Generated: `{generated}`",
        "",
        "| MPN | Supplier | SKU | Candidate Keywords | Status |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| `{row['manufacturer_part_number']}` | `{row['supplier']}` | `{row['supplier_sku']}` | `{', '.join(row['candidate_keywords'])}` | `{row['match_status']}` |"
        )
    lines.extend(
        [
            "",
            "## Rule",
            "",
            "These are search hints only. Exact KiCad footprints require manufacturer package drawings and human review.",
        ]
    )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json_path)
    print(md_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
