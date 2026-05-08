#!/usr/bin/env python3
"""Create footprint gap reports and backlog from component/footprint candidate matches."""

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


def write_markdown(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def default_match_file() -> Path:
    return ROOT / "29_FOOTPRINT_GAP_ANALYSIS" / "GENERATED_INDEXES" / "component_db_to_footprint_matches.json"


def risk_bucket(row: dict[str, Any]) -> str:
    category = str(row.get("category", "")).upper()
    text = " ".join(
        [
            str(row.get("part_number", "")),
            str(row.get("category", "")),
            " ".join(str(note) for note in row.get("risk_notes", [])),
        ]
    ).lower()
    connector_patterns = [
        "connector",
        "receptacle",
        "barrel jack",
        "u.fl",
        "ufl",
        "ipex",
        "mhf",
        "rp-sma",
        "sma edge",
        "sma connector",
        "jst",
        "terminal block",
        "pin header",
        "pigtail",
    ]
    if category == "04_CONNECTORS" or any(token in text for token in connector_patterns):
        return "connector"
    if category == "01_MICROCONTROLLERS" or any(token in text for token in ["esp32", "stm32", "pic", "rp2040", "microcontroller", "module"]):
        return "mcu_module"
    if category in {"02_POWER", "05_PROTECTION"} or any(token in text for token in ["lm2596", "ams1117", "regulator", "power", "tvs", "polyfuse", "mosfet", "esd"]):
        return "power"
    return "general"


def priority(row: dict[str, Any]) -> str:
    bucket = risk_bucket(row)
    if row.get("candidate_count", 0) == 0:
        return "P0_MISSING_CANDIDATES"
    if bucket == "connector":
        return "P0_HUMAN_MECHANICAL_REVIEW"
    if bucket in {"mcu_module", "power"}:
        return "P1_PACKAGE_DRAWING_REVIEW"
    return "P2_VERIFY_BEFORE_USE"


def md_table(rows: list[dict[str, Any]]) -> list[str]:
    lines = ["| Priority | Part | Category | Candidate Count | Exact Verification | Notes |", "| --- | --- | --- | ---: | --- | --- |"]
    if not rows:
        lines.append("| NONE | NONE | NONE | 0 | NONE | No rows in this category. |")
        return lines
    for row in rows:
        notes = " ".join(row.get("risk_notes", []))
        lines.append(
            f"| `{priority(row)}` | `{row.get('part_number', '')}` | `{row.get('category', '')}` | {row.get('candidate_count', 0)} | `{row.get('exact_footprint_verification', 'UNVERIFIED')}` | {notes} |"
        )
    return lines


def write_gap_doc(path: Path, title: str, rows: list[dict[str, Any]], intro: list[str]) -> None:
    lines = [f"# {title}", "", "Status: `UNVERIFIED_FOOTPRINT_GAP_REPORT`", ""]
    lines.extend(intro)
    lines.extend(["", "## Candidate Rows", ""])
    lines.extend(md_table(rows))
    lines.extend(
        [
            "",
            "## Approval Rule",
            "",
            "A row in this report is not a verified footprint. Approval requires exact manufacturer package drawing, pad numbering, orientation, courtyard, paste/mask, 3D/mechanical review where useful, and human review for high-risk categories.",
        ]
    )
    write_markdown(path, lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create missing footprint and high-risk backlog reports.")
    parser.add_argument("--match-file", default=str(default_match_file()))
    parser.add_argument("--output-root", default=str(ROOT / "29_FOOTPRINT_GAP_ANALYSIS"))
    parser.add_argument("--summary-output", default=str(ROOT / "05_OUTPUTS" / "footprint_gap_analysis" / "FOOTPRINT_GAP_SUMMARY.md"))
    parser.add_argument("--history-report", default=str(ROOT / "02_HISTORY" / "design_reviews" / "KICAD_FOOTPRINT_GAP_ANALYSIS_REPORT.md"))
    args = parser.parse_args()

    match_path = Path(args.match_file)
    if not match_path.exists():
        raise SystemExit(f"Match file not found. Run match_component_db_to_footprints.py first: {match_path}")
    payload = read_json(match_path)
    rows = payload.get("matches", [])
    missing = [row for row in rows if row.get("candidate_count", 0) == 0 or row.get("exact_footprint_verification") != "VERIFIED"]
    connectors = [row for row in missing if risk_bucket(row) == "connector"]
    mcu_modules = [row for row in missing if risk_bucket(row) == "mcu_module"]
    power = [row for row in missing if risk_bucket(row) == "power"]
    high_risk = [row for row in missing if priority(row).startswith("P0") or priority(row).startswith("P1")]
    backlog = sorted(missing, key=lambda row: (priority(row), str(row.get("part_number", ""))))

    output_root = Path(args.output_root)
    write_gap_doc(
        output_root / "MISSING_FOOTPRINT_CANDIDATES.md",
        "Missing Footprint Candidates",
        missing,
        [
            f"- Component records checked: {payload.get('records_checked', 0)}",
            f"- Rows requiring verification or missing candidates: {len(missing)}",
        ],
    )
    write_gap_doc(
        output_root / "HIGH_RISK_FOOTPRINTS.md",
        "High-Risk Footprints",
        high_risk,
        [
            "- High-risk categories include USB-C, RF connectors, ESP32 modules, STM32 packages, PMOS/SOT-23, ESD diode arrays, barrel jacks, automotive connectors, mounting holes, test pads, and regulator packages.",
            "- Treat these as blocked for production use until exact package/mechanical review is complete.",
        ],
    )
    write_gap_doc(
        output_root / "CONNECTOR_FOOTPRINT_GAPS.md",
        "Connector Footprint Gaps",
        connectors,
        [
            "- Connector rows require exact manufacturer part number, drawing, pin numbering, mating connector, cable/board-edge orientation, 3D/mechanical review, and human review.",
        ],
    )
    write_gap_doc(
        output_root / "MCU_MODULE_FOOTPRINT_GAPS.md",
        "MCU And Module Footprint Gaps",
        mcu_modules,
        [
            "- MCU and module rows require exact orderable package suffix, package drawing, pin-1 orientation, exposed pad/keepout review where applicable, and symbol-to-footprint pin mapping.",
        ],
    )
    write_gap_doc(
        output_root / "POWER_PACKAGE_FOOTPRINT_GAPS.md",
        "Power Package Footprint Gaps",
        power,
        [
            "- Power rows require exact package/thermal drawing, pad numbering, exposed pad, copper/thermal requirements, and layout-loop review.",
        ],
    )
    write_gap_doc(
        output_root / "FOOTPRINT_CREATION_BACKLOG.md",
        "Footprint Creation Backlog",
        backlog,
        [
            "- This backlog lists candidate or missing footprints that must be verified or created as project-local library items before production use.",
            "- Installed KiCad candidates should be verified first; custom footprints should be created only when no verified installed footprint matches the exact drawing.",
        ],
    )

    summary_lines = [
        "# Footprint Gap Summary",
        "",
        "Status: `LOCAL_READ_ONLY_GAP_SUMMARY`",
        "",
        f"- Component records checked: {payload.get('records_checked', 0)}",
        f"- Records with candidates: {payload.get('matches_with_candidates', 0)}",
        f"- Records without candidates: {payload.get('records_without_candidates', 0)}",
        f"- Rows requiring verification or missing candidates: {len(missing)}",
        f"- Connector high-risk rows: {len(connectors)}",
        f"- MCU/module high-risk rows: {len(mcu_modules)}",
        f"- Power/protection high-risk rows: {len(power)}",
        "",
        "## Result",
        "",
        "No exact footprint is approved by this report. Candidate matches remain `UNVERIFIED` until package drawing and human review are complete.",
    ]
    write_markdown(Path(args.summary_output), summary_lines)
    write_markdown(Path(args.history_report), summary_lines + ["", "## Source", "", f"- Match file: `{match_path}`"])
    write_json(output_root / "GENERATED_INDEXES" / "footprint_creation_backlog.json", {"summary": summary_lines, "rows": backlog})
    print(json.dumps({"missing_or_unverified": len(missing), "connector": len(connectors), "mcu_module": len(mcu_modules), "power": len(power)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
