#!/usr/bin/env python3
"""Inventory installed KiCad footprints and summarize high-risk candidate areas.

Read-only with respect to KiCad installation and user KiCad configuration.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def repo_root() -> Path:
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "AGENTS.md").exists():
            return parent
    return Path.cwd()


ROOT = repo_root()
KICAD_LIBRARY_SCRIPT_DIR = ROOT / "03_TOOLS" / "scripts" / "kicad_libraries"
if str(KICAD_LIBRARY_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(KICAD_LIBRARY_SCRIPT_DIR))

from index_footprints import build_index  # noqa: E402
from kicad_library_common import (  # noqa: E402
    detect_kicad_root,
    ensure_safe_output_dir,
    fail,
    score_text,
    write_json,
    write_markdown,
)


HIGH_RISK_QUERIES: dict[str, list[str]] = {
    "USB-C connectors": ["usb c", "typec", "type c", "usb_c"],
    "RF connectors": ["u.fl", "ufl", "ipex", "mhf", "sma", "rp-sma"],
    "ESP32 modules": ["esp32", "wroom", "wrover", "mini-1"],
    "STM32 packages": ["lqfp", "ufqfp", "wlcsp", "stm32", "bga"],
    "PMOS/SOT-23 mapping": ["sot-23", "sot23", "ao3401", "mosfet"],
    "ESD diode arrays": ["esd", "tvs", "sod", "sot-23-6", "sot-666"],
    "Barrel jacks": ["barrel", "dc jack", "dcjack"],
    "Automotive connectors": ["automotive", "molex", "te connectivity", "jst"],
    "Mounting holes": ["mountinghole", "mounting hole", "mounting"],
    "Test pads": ["testpoint", "test point", "testpad", "test pad"],
    "Regulator packages": ["sot-223", "to-263", "to-252", "dfn", "qfn", "soic"],
}


def default_output_dir() -> Path:
    return ROOT / "29_FOOTPRINT_GAP_ANALYSIS" / "GENERATED_INDEXES"


def candidate_rows(index: dict[str, Any], query: str, limit: int = 20) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for footprint in index.get("footprints", []):
        text = " ".join(
            [
                str(footprint.get("library", "")),
                str(footprint.get("footprint", "")),
                str(footprint.get("description", "")),
                str(footprint.get("tags", "")),
                " ".join(footprint.get("model_paths", [])),
            ]
        )
        score, matched = score_text(query, text)
        if score <= 0:
            continue
        rows.append(
            {
                "score": score,
                "matched_tokens": matched,
                "library": footprint.get("library", ""),
                "footprint": footprint.get("footprint", ""),
                "pad_count": footprint.get("pad_count", 0),
                "description": footprint.get("description", ""),
                "path": footprint.get("path", ""),
                "verification_status": "UNVERIFIED_CANDIDATE",
            }
        )
    rows.sort(key=lambda row: (-int(row["score"]), str(row["library"]), str(row["footprint"])))
    return rows[:limit]


def build_gap_inventory(kicad_root: Path, version: str) -> dict[str, Any]:
    index = build_index(kicad_root, version)
    category_hits = {
        category: {
            "queries": queries,
            "candidate_count": sum(len(candidate_rows(index, query, 1000)) for query in queries),
            "top_candidates": [
                candidate
                for query in queries
                for candidate in candidate_rows(index, query, 5)
            ][:20],
            "verification_status": "UNVERIFIED_CANDIDATES",
        }
        for category, queries in HIGH_RISK_QUERIES.items()
    }
    index["gap_analysis"] = {
        "high_risk_categories": category_hits,
        "verification_policy": "Candidate footprints require exact package drawing and human review before approval.",
    }
    return index


def write_inventory_markdown(path: Path, index: dict[str, Any]) -> None:
    summary = index["summary"]
    lines = [
        "# Installed KiCad Footprint Inventory",
        "",
        f"Generated: `{index['generated_at']}`",
        "",
        "Status: `LOCAL_READ_ONLY_INVENTORY`",
        "",
        f"KiCad root: `{index['kicad_root']}`",
        f"Footprint root: `{index['footprints_root']}`",
        "",
        "## Counts",
        "",
        f"- Footprint libraries: {summary['footprint_libraries']}",
        f"- Footprint files: {summary['footprints_indexed']}",
        f"- Footprints with 3D model references: {summary['footprints_with_3d_model_refs']}",
        f"- Footprint library table entries parsed: {summary['footprint_table_entries']}",
        "",
        "## Largest Installed Footprint Libraries",
        "",
        "| Library | Footprints |",
        "| --- | ---: |",
    ]
    for row in sorted(index["libraries"], key=lambda item: item["footprint_count"], reverse=True)[:30]:
        lines.append(f"| `{row['library']}` | {row['footprint_count']} |")
    lines.extend(["", "## High-Risk Candidate Categories", "", "| Category | Keyword hits | Status |", "| --- | ---: | --- |"])
    for category, payload in index["gap_analysis"]["high_risk_categories"].items():
        lines.append(f"| {category} | {payload['candidate_count']} | `{payload['verification_status']}` |")
    lines.extend(
        [
            "",
            "## Interpretation Rules",
            "",
            "- A high candidate count does not mean the exact needed footprint exists.",
            "- USB-C, RF, connector, PMOS, ESD, regulator, mounting-hole, and test-pad footprints require package/mechanical drawing review.",
            "- Installed KiCad global libraries are system resources. Index them read-only; do not modify them.",
        ]
    )
    write_markdown(path, lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only installed KiCad footprint inventory.")
    parser.add_argument("--kicad-root", help="KiCad install root. Defaults to detected KiCad 9 root.")
    parser.add_argument("--version", default="9.0", help="KiCad config version. Default: 9.0")
    parser.add_argument("--output-dir", default=str(default_output_dir()), help="Generated output folder.")
    args = parser.parse_args()

    kicad_root = detect_kicad_root(args.kicad_root, args.version)
    if not kicad_root:
        fail("KiCad root not found. Pass --kicad-root.")
    output_dir = ensure_safe_output_dir(Path(args.output_dir), kicad_root, args.version)
    index = build_gap_inventory(kicad_root, args.version)
    write_json(output_dir / "installed_kicad_footprint_inventory.json", index)
    write_inventory_markdown(ROOT / "29_FOOTPRINT_GAP_ANALYSIS" / "INSTALLED_KICAD_FOOTPRINT_INVENTORY.md", index)
    write_inventory_markdown(output_dir / "installed_kicad_footprint_inventory.md", index)
    print(json.dumps(index["summary"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

