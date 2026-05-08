#!/usr/bin/env python3
"""Build a read-only KiCad symbol library index."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from kicad_library_common import (
    default_output_dir,
    detect_kicad_root,
    ensure_safe_output_dir,
    fail,
    kicad_share_root,
    parse_lib_table,
    read_text,
    user_config_roots,
    utc_stamp,
    write_json,
    write_markdown,
)


UNIT_SUFFIX = re.compile(r"_\d+_\d+$")
SYMBOL_PATTERN = re.compile(r"\(symbol\s+\"([^\"]+)\"")
PROPERTY_PATTERN = re.compile(r"\(property\s+\"([^\"]+)\"\s+\"([^\"]*)\"")


def extract_balanced_block(text: str, start: int) -> str:
    depth = 0
    in_string = False
    escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == "\"":
                in_string = False
            continue
        if char == "\"":
            in_string = True
        elif char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return text[start : index + 1]
    return text[start:]


def extract_symbols(path: Path) -> list[dict[str, object]]:
    text = read_text(path)
    rows = []
    seen = set()
    for match in SYMBOL_PATTERN.finditer(text):
        name = match.group(1)
        if UNIT_SUFFIX.search(name):
            continue
        if name in seen:
            continue
        seen.add(name)
        block = extract_balanced_block(text, match.start())
        properties = {prop.group(1): prop.group(2) for prop in PROPERTY_PATTERN.finditer(block)}
        extends = re.search(r"\(extends\s+\"([^\"]+)\"", block)
        rows.append(
            {
            "library": path.stem,
            "symbol": name,
            "library_file": str(path),
                "extends": extends.group(1) if extends else "",
                "footprint_field": properties.get("Footprint", ""),
                "datasheet": properties.get("Datasheet", ""),
                "keywords": properties.get("ki_keywords", ""),
                "description": properties.get("Description", ""),
            }
        )
    return rows


def build_index(kicad_root: Path, version_preference: str) -> dict[str, object]:
    share = kicad_share_root(kicad_root)
    symbols_root = share / "symbols"
    template_root = share / "template"
    if not symbols_root.exists():
        fail(f"Symbol root not found: {symbols_root}")

    libraries = []
    symbols = []
    for path in sorted(symbols_root.glob("*.kicad_sym")):
        entries = extract_symbols(path)
        libraries.append(
            {
                "library": path.stem,
                "path": str(path),
                "symbol_count": len(entries),
                "size_bytes": path.stat().st_size,
            }
        )
        symbols.extend(entries)

    table_paths = [template_root / "sym-lib-table"]
    for root in user_config_roots(version_preference):
        table_paths.append(root / "sym-lib-table")
    table_entries = []
    for table_path in table_paths:
        table_entries.extend(parse_lib_table(table_path))

    return {
        "generated_at": utc_stamp(),
        "kicad_root": str(kicad_root),
        "symbols_root": str(symbols_root),
        "user_config_roots": [str(p) for p in user_config_roots(version_preference)],
        "library_tables_read": [str(p) for p in table_paths if p.exists()],
        "summary": {
            "symbol_libraries": len(libraries),
            "symbols_indexed": len(symbols),
            "symbol_table_entries": len(table_entries),
        },
        "libraries": libraries,
        "symbol_table_entries": table_entries,
        "symbols": symbols,
        "safety": [
            "Read-only inspection of KiCad install and user-global library tables.",
            "No KiCad install files are modified.",
            "No user-global library tables are modified.",
        ],
    }


def write_summary(output_dir: Path, index: dict[str, object]) -> None:
    summary = index["summary"]
    lines = [
        "# Symbol Index Summary",
        "",
        f"Generated: {index['generated_at']}",
        "",
        f"KiCad root: `{index['kicad_root']}`",
        f"Symbol root: `{index['symbols_root']}`",
        "",
        "## Counts",
        "",
        f"- Symbol libraries: {summary['symbol_libraries']}",
        f"- Symbols indexed: {summary['symbols_indexed']}",
        f"- Library table entries parsed: {summary['symbol_table_entries']}",
        "",
        "## Largest Libraries",
        "",
        "| Library | Symbols | Path |",
        "| --- | ---: | --- |",
    ]
    libraries = sorted(index["libraries"], key=lambda row: row["symbol_count"], reverse=True)[:20]
    for row in libraries:
        lines.append(f"| `{row['library']}` | {row['symbol_count']} | `{row['path']}` |")
    lines.extend(
        [
            "",
            "## Safety",
            "",
            "- This summary was generated by read-only filesystem inspection.",
            "- Candidate symbols still require pin, unit, footprint-field, and datasheet verification.",
        ]
    )
    write_markdown(output_dir / "symbol_index_summary.md", lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a read-only KiCad symbol index.")
    parser.add_argument("--kicad-root", help="KiCad install root. Defaults to detected KiCad 9 root.")
    parser.add_argument("--version", default="9.0", help="KiCad config version to inspect. Default: 9.0")
    parser.add_argument("--output-dir", default=str(default_output_dir()), help="Generated index output folder.")
    args = parser.parse_args()

    kicad_root = detect_kicad_root(args.kicad_root, args.version)
    if not kicad_root:
        fail("KiCad root not found. Pass --kicad-root.")
    output_dir = ensure_safe_output_dir(Path(args.output_dir), kicad_root, args.version)
    index = build_index(kicad_root, args.version)
    write_json(output_dir / "symbol_index.json", index)
    write_summary(output_dir, index)
    print(f"Wrote {output_dir / 'symbol_index.json'}")
    print(f"Wrote {output_dir / 'symbol_index_summary.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
