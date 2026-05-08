#!/usr/bin/env python3
"""Find KiCad symbol candidates from the generated symbol index."""

from __future__ import annotations

import argparse
from pathlib import Path

from kicad_library_common import (
    default_output_dir,
    detect_kicad_root,
    ensure_safe_output_dir,
    fail,
    load_json,
    score_text,
    slugify,
    write_json,
    write_markdown,
)
from index_symbols import build_index


def find_candidates(query: str, index: dict[str, object], limit: int) -> list[dict[str, object]]:
    rows = []
    for symbol in index.get("symbols", []):
        text = " ".join(
            [
                str(symbol.get("library", "")),
                str(symbol.get("symbol", "")),
                str(symbol.get("extends", "")),
                str(symbol.get("footprint_field", "")),
                str(symbol.get("keywords", "")),
                str(symbol.get("description", "")),
            ]
        )
        score, matched = score_text(query, text)
        if score > 0:
            rows.append(
                {
                    "score": score,
                    "matched_tokens": matched,
                    "library": symbol.get("library"),
                    "symbol": symbol.get("symbol"),
                    "library_file": symbol.get("library_file"),
                    "extends": symbol.get("extends", ""),
                    "footprint_field": symbol.get("footprint_field", ""),
                    "keywords": symbol.get("keywords", ""),
                    "description": symbol.get("description", ""),
                    "verification_warning": "Candidate only. Verify pins, units, power pins, aliases, and footprint field against datasheet.",
                }
            )
    rows.sort(key=lambda row: (-int(row["score"]), str(row["library"]), str(row["symbol"])))
    return rows[:limit]


def write_candidate_files(output_dir: Path, query: str, candidates: list[dict[str, object]]) -> None:
    slug = slugify(query)
    payload = {
        "query": query,
        "candidate_type": "symbol",
        "verification_policy": "Do not assert correctness until verified against exact datasheet and project requirements.",
        "candidates": candidates,
    }
    write_json(output_dir / f"symbol_candidates_{slug}.json", payload)
    lines = [
        f"# Symbol Candidates: {query}",
        "",
        "Status: candidate search only. These are not approved symbols.",
        "",
        "| Score | Library | Symbol | Matched Tokens | Warning |",
        "| ---: | --- | --- | --- | --- |",
    ]
    if not candidates:
        lines.append("| 0 | None | None | None | No symbol candidates found. |")
    for row in candidates:
        lines.append(
            f"| {row['score']} | `{row['library']}` | `{row['symbol']}` | `{', '.join(row['matched_tokens'])}` | Verify pins, units, power pins, and footprint field. |"
        )
    lines.extend(
        [
            "",
            "## Rule",
            "",
            "A symbol candidate is only a search result. It is not correct until pin names, pin numbers, units, power pins, and intended footprint are checked against the exact source document.",
        ]
    )
    write_markdown(output_dir / f"symbol_candidates_{slug}.md", lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Find symbol candidates from generated KiCad symbol index.")
    parser.add_argument("query", help="Part, module, connector, or keyword query.")
    parser.add_argument("--symbol-index", help="Path to symbol_index.json. If missing, a temporary index is built read-only.")
    parser.add_argument("--kicad-root", help="KiCad install root used if index must be built.")
    parser.add_argument("--version", default="9.0", help="KiCad config version. Default: 9.0")
    parser.add_argument("--output-dir", default=str(default_output_dir()), help="Generated output folder.")
    parser.add_argument("--limit", type=int, default=25)
    args = parser.parse_args()

    kicad_root = detect_kicad_root(args.kicad_root, args.version)
    output_dir = ensure_safe_output_dir(Path(args.output_dir), kicad_root, args.version)
    index_path = Path(args.symbol_index) if args.symbol_index else output_dir / "symbol_index.json"
    if index_path.exists():
        index = load_json(index_path)
    else:
        if not kicad_root:
            fail("KiCad root not found and symbol_index.json is missing.")
        index = build_index(kicad_root, args.version)
    candidates = find_candidates(args.query, index, args.limit)
    write_candidate_files(output_dir, args.query, candidates)
    print(f"Wrote symbol candidate files for: {args.query}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
