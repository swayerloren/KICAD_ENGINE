#!/usr/bin/env python3
"""Build supplier footprint match indexes."""

from __future__ import annotations

import argparse
import json
from collections import Counter
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
        "# Supplier Footprint Match Index",
        "",
        "Status: `GENERATED_INDEX`",
        "",
        "## Summary",
        "",
        f"- Records indexed: {payload['summary']['records_indexed']}",
        f"- Example-only records: {payload['summary']['example_only_records']}",
        f"- Human review required: {payload['summary']['human_review_required']}",
        "",
        "## Confidence Counts",
        "",
        "| Confidence | Count |",
        "| --- | ---: |",
    ]
    for key, value in sorted(payload["summary"]["confidence_counts"].items()):
        lines.append(f"| `{key}` | {value} |")
    lines.extend(["", "## Records", "", "| Record | Supplier | MPN | Confidence | Footprint | Human Review |", "| --- | --- | --- | --- | --- | --- |"])
    for row in payload["records"]:
        lines.append(
            f"| `{row['record_id']}` | `{row['supplier']}` | `{row['mpn']}` | `{row['confidence_level']}` | `{row['kicad_footprint_candidate']}` | `{row['human_review_required']}` |"
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def collect_records(root: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*.json")):
        if "reports" in path.parts:
            continue
        try:
            data = read_json(path)
        except Exception:
            continue
        if isinstance(data, dict) and "mpn" in data:
            row = {
                "path": str(path),
                "record_id": data.get("record_id", "UNKNOWN"),
                "record_type": data.get("record_type", "UNKNOWN"),
                "supplier": data.get("supplier", "UNKNOWN"),
                "supplier_sku": data.get("supplier_sku", "UNKNOWN"),
                "manufacturer": data.get("manufacturer", "UNKNOWN"),
                "mpn": data.get("mpn", "UNKNOWN"),
                "confidence_level": data.get("confidence_level", "UNVERIFIED"),
                "kicad_symbol_candidate": data.get("kicad_symbol_candidate", "UNKNOWN"),
                "kicad_footprint_candidate": data.get("kicad_footprint_candidate", "UNKNOWN"),
                "footprint_status": data.get("footprint_status", "UNVERIFIED"),
                "pinout_status": data.get("pinout_status", "UNVERIFIED"),
                "connector_orientation_status": data.get("connector_orientation_status", "UNVERIFIED"),
                "human_review_required": data.get("human_review_required", True),
                "high_risk_categories": data.get("high_risk_categories", []),
            }
            records.append(row)
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description="Build supplier footprint match index.")
    parser.add_argument("--matches-root", default=str(ROOT / "30_SUPPLIER_FOOTPRINT_MATCHES" / "matches"))
    parser.add_argument("--output-json", default=str(ROOT / "30_SUPPLIER_FOOTPRINT_MATCHES" / "reports" / "match_index.json"))
    parser.add_argument("--output-md", default=str(ROOT / "30_SUPPLIER_FOOTPRINT_MATCHES" / "reports" / "MATCH_INDEX.md"))
    args = parser.parse_args()

    records = collect_records(Path(args.matches_root))
    confidence_counts = Counter(row["confidence_level"] for row in records)
    payload = {
        "summary": {
            "records_indexed": len(records),
            "example_only_records": sum(1 for row in records if str(row["record_type"]).startswith("EXAMPLE_ONLY")),
            "human_review_required": sum(1 for row in records if row["human_review_required"]),
            "confidence_counts": dict(confidence_counts),
        },
        "records": records,
    }
    write_json(Path(args.output_json), payload)
    write_markdown(Path(args.output_md), payload)
    print(json.dumps(payload["summary"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

