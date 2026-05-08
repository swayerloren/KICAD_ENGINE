#!/usr/bin/env python3
"""Inventory installed KiCad symbols.

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

from index_symbols import build_index  # noqa: E402
from kicad_library_common import detect_kicad_root, ensure_safe_output_dir, fail, score_text, write_json, write_markdown  # noqa: E402


KEY_QUERIES = [
    "ESP32",
    "STM32",
    "PIC16",
    "PIC18",
    "RP2040",
    "USB C",
    "MCP2562FD",
    "SN65HVD230",
    "LM2596",
    "AMS1117",
    "TVS",
    "Polyfuse",
]


def default_output_dir() -> Path:
    return ROOT / "29_FOOTPRINT_GAP_ANALYSIS" / "GENERATED_INDEXES"


def find_symbol_hits(index: dict[str, Any], query: str, limit: int = 20) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for symbol in index.get("symbols", []):
        text = " ".join(
            [
                str(symbol.get("library", "")),
                str(symbol.get("symbol", "")),
                str(symbol.get("description", "")),
                str(symbol.get("keywords", "")),
                str(symbol.get("footprint_field", "")),
            ]
        )
        score, matched = score_text(query, text)
        if score <= 0:
            continue
        rows.append(
            {
                "score": score,
                "matched_tokens": matched,
                "library": symbol.get("library", ""),
                "symbol": symbol.get("symbol", ""),
                "footprint_field": symbol.get("footprint_field", ""),
                "description": symbol.get("description", ""),
                "verification_status": "UNVERIFIED_CANDIDATE",
            }
        )
    rows.sort(key=lambda row: (-int(row["score"]), str(row["library"]), str(row["symbol"])))
    return rows[:limit]


def write_inventory_markdown(path: Path, index: dict[str, Any]) -> None:
    summary = index["summary"]
    lines = [
        "# Installed KiCad Symbol Inventory",
        "",
        f"Generated: `{index['generated_at']}`",
        "",
        "Status: `LOCAL_READ_ONLY_INVENTORY`",
        "",
        f"KiCad root: `{index['kicad_root']}`",
        f"Symbol root: `{index['symbols_root']}`",
        "",
        "## Counts",
        "",
        f"- Symbol libraries: {summary['symbol_libraries']}",
        f"- Symbols indexed: {summary['symbols_indexed']}",
        f"- Symbol library table entries parsed: {summary['symbol_table_entries']}",
        "",
        "## Largest Installed Symbol Libraries",
        "",
        "| Library | Symbols |",
        "| --- | ---: |",
    ]
    for row in sorted(index["libraries"], key=lambda item: item["symbol_count"], reverse=True)[:30]:
        lines.append(f"| `{row['library']}` | {row['symbol_count']} |")
    lines.extend(["", "## Common-Part Symbol Candidate Hits", "", "| Query | Hits | Status |", "| --- | ---: | --- |"])
    for query in KEY_QUERIES:
        hits = find_symbol_hits(index, query, 1000)
        lines.append(f"| `{query}` | {len(hits)} | `UNVERIFIED_CANDIDATES` |")
    lines.extend(
        [
            "",
            "## Interpretation Rules",
            "",
            "- A symbol hit does not verify pinout, power pins, hidden pins, or footprint field correctness.",
            "- Symbol-to-footprint mappings must be checked against datasheet pinout and package drawing evidence.",
            "- Installed KiCad global symbol libraries are read-only system resources for this workflow.",
        ]
    )
    write_markdown(path, lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only installed KiCad symbol inventory.")
    parser.add_argument("--kicad-root", help="KiCad install root. Defaults to detected KiCad 9 root.")
    parser.add_argument("--version", default="9.0", help="KiCad config version. Default: 9.0")
    parser.add_argument("--output-dir", default=str(default_output_dir()), help="Generated output folder.")
    args = parser.parse_args()

    kicad_root = detect_kicad_root(args.kicad_root, args.version)
    if not kicad_root:
        fail("KiCad root not found. Pass --kicad-root.")
    output_dir = ensure_safe_output_dir(Path(args.output_dir), kicad_root, args.version)
    index = build_index(kicad_root, args.version)
    index["candidate_hits"] = {query: find_symbol_hits(index, query, 25) for query in KEY_QUERIES}
    write_json(output_dir / "installed_kicad_symbol_inventory.json", index)
    write_inventory_markdown(ROOT / "29_FOOTPRINT_GAP_ANALYSIS" / "INSTALLED_KICAD_SYMBOL_INVENTORY.md", index)
    write_inventory_markdown(output_dir / "installed_kicad_symbol_inventory.md", index)
    print(json.dumps(index["summary"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

