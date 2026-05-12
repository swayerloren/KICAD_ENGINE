#!/usr/bin/env python3
"""Generate a footprint assignment plan from the saved schematic."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from footprint_package_common import (
    default_output_dir,
    load_physical_symbols,
    locate_lock_file,
    read_lock_rows,
    resolve_project_and_schematic,
)


def recommended_action(symbol: dict, row: dict | None) -> str:
    if not str(symbol.get("footprint", "")).strip():
        return "Assign a footprint, then create a lock-file row with source and package proof."
    if row is None:
        return "Add a FOOTPRINT_LOCK.csv row with package evidence and risk classification."
    if not str(row.get("datasheet_or_source_url", "")).strip():
        return "Add datasheet/source evidence to the lock row."
    if str(row.get("package_drawing_checked", "")).strip().lower() not in {"yes", "true", "1", "verified", "checked"}:
        return "Review the package drawing and mark package_drawing_checked=yes."
    if symbol.get("high_risk"):
        return "Complete high-risk review proof before schematic-to-PCB update."
    return "Row is close to ready; verify final notes and human-review status."


def markdown_report(result: dict) -> str:
    lines = [
        "# Footprint Assignment Plan",
        "",
        f"Generated: `{result['generated_at']}`",
        f"Schematic: `{result['schematic']}`",
        "",
        f"- Physical symbols: {result['physical_symbol_count']}",
        f"- Lock file present: `{result['lock_file_present']}`",
        "",
        "## Planned Actions",
        "",
        "| Reference | Value | Footprint | Risk | Category | Recommended action |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["assignments"]:
        lines.append(
            "| `{reference}` | `{value}` | `{footprint}` | `{risk}` | `{category}` | {recommended_action} |".format(
                reference=item["reference"],
                value=item["value"],
                footprint=item["kicad_footprint"],
                risk=item["risk"],
                category=item["category"],
                recommended_action=item["recommended_action"].replace("|", "\\|"),
            )
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Generate a footprint assignment plan from the saved schematic.")
    parser.add_argument("--project", default="", help="Active project root containing a kicad/ folder.")
    parser.add_argument("--schematic", default="", help="Exact .kicad_sch path.")
    parser.add_argument("--lock-file", default="", help="Optional explicit lock-file path.")
    parser.add_argument("--output", default="", help="Optional markdown output path.")
    parser.add_argument("--json-output", default="", help="Optional JSON output path.")
    parser.add_argument("--no-fail", action="store_true", help="Return exit code 0.")
    args = parser.parse_args()

    project_root, schematic = resolve_project_and_schematic(args.project, args.schematic)
    symbols = load_physical_symbols(schematic)
    lock_path = locate_lock_file(project_root, args.lock_file)
    _, row_index = read_lock_rows(lock_path)

    assignments = []
    for symbol in symbols:
        row = row_index.get(symbol["reference"].upper())
        assignments.append(
            {
                "reference": symbol["reference"],
                "value": symbol["value"],
                "manufacturer_part_number": row.get("manufacturer_part_number", "") if row else "",
                "kicad_symbol": symbol["lib_id"],
                "kicad_footprint": symbol["footprint"],
                "package": row.get("package", "") if row else "",
                "risk": symbol["risk"],
                "high_risk": bool(symbol["high_risk"]),
                "risk_reason": symbol["risk_reason"],
                "category": symbol["category"],
                "recommended_action": recommended_action(symbol, row),
                "notes": row.get("notes", "") if row else "",
            }
        )

    result = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "schematic": str(schematic),
        "physical_symbol_count": len(symbols),
        "lock_file": str(lock_path) if lock_path else "",
        "lock_file_present": bool(lock_path and lock_path.exists()),
        "assignments": assignments,
    }

    report_dir = default_output_dir(project_root, schematic)
    output_path = Path(args.output) if args.output else report_dir / "footprint_assignment_plan.md"
    json_path = Path(args.json_output) if args.json_output else report_dir / "footprint_assignment_plan.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown_report(result), encoding="utf-8")
    json_path.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(str(json_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
