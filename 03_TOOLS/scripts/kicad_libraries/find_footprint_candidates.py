#!/usr/bin/env python3
"""Find KiCad footprint candidates from the generated footprint index."""

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
from index_footprints import build_index


HIGH_RISK_KEYWORDS = {
    "usb": "Connector orientation, shell pads, CC pins, shield grounding, and exact drawing are high-risk.",
    "typec": "USB-C footprints are not interchangeable across manufacturers.",
    "connector": "Connector pin numbering, mating face, cable exit, and mechanical orientation require drawing review.",
    "ufl": "U.FL/IPEX variants are mechanically high-risk.",
    "sma": "SMA and RP-SMA orientation/gender and edge-launch geometry require exact drawing review.",
    "qfn": "QFN exposed pad, thermal vias, paste, and pin 1 orientation require package drawing review.",
    "dfn": "DFN exposed pad, paste, and pin 1 orientation require package drawing review.",
    "bga": "BGA footprint, ball map, escape routing, and fab capability require detailed review.",
}


def risk_notes(text: str) -> list[str]:
    compact = text.lower().replace("-", "").replace("_", "")
    notes = []
    for key, note in HIGH_RISK_KEYWORDS.items():
        if key in compact:
            notes.append(note)
    if not notes:
        notes.append("Verify exact manufacturer package drawing before use.")
    return notes


def find_candidates(query: str, index: dict[str, object], limit: int) -> list[dict[str, object]]:
    rows = []
    for footprint in index.get("footprints", []):
        core_text = " ".join(
            [
                str(footprint.get("library", "")),
                str(footprint.get("footprint", "")),
                str(footprint.get("tags", "")),
                " ".join(footprint.get("model_paths", [])),
            ]
        )
        desc_text = str(footprint.get("description", ""))
        core_score, core_matched = score_text(query, core_text)
        if core_score <= 0:
            continue
        desc_score, desc_matched = score_text(query, desc_text)
        score = core_score + (desc_score // 3)
        matched = list(dict.fromkeys(core_matched + desc_matched))
        if score > 0:
            rows.append(
                {
                    "score": score,
                    "matched_tokens": matched,
                    "library": footprint.get("library"),
                    "footprint": footprint.get("footprint"),
                    "path": footprint.get("path"),
                    "description": footprint.get("description", ""),
                    "tags": footprint.get("tags", ""),
                    "pad_count": footprint.get("pad_count"),
                    "pad_names_sample": footprint.get("pad_names_sample", []),
                    "model_paths": footprint.get("model_paths", []),
                    "risk_notes": risk_notes(core_text + " " + desc_text),
                    "verification_warning": "Candidate only. Verify package drawing, pad numbers, orientation, courtyard, paste/mask, and 3D model.",
                }
            )
    rows.sort(key=lambda row: (-int(row["score"]), str(row["library"]), str(row["footprint"])))
    return rows[:limit]


def write_candidate_files(output_dir: Path, query: str, candidates: list[dict[str, object]]) -> None:
    slug = slugify(query)
    payload = {
        "query": query,
        "candidate_type": "footprint",
        "verification_policy": "Do not assert correctness until verified against exact manufacturer package drawing.",
        "candidates": candidates,
    }
    write_json(output_dir / f"footprint_candidates_{slug}.json", payload)
    lines = [
        f"# Footprint Candidates: {query}",
        "",
        "Status: candidate search only. These are not approved footprints.",
        "",
        "| Score | Library | Footprint | Pads | Matched Tokens | Risk Notes |",
        "| ---: | --- | --- | ---: | --- | --- |",
    ]
    if not candidates:
        lines.append("| 0 | None | None | 0 | None | No footprint candidates found. |")
    for row in candidates:
        notes = " ".join(row["risk_notes"])
        lines.append(
            f"| {row['score']} | `{row['library']}` | `{row['footprint']}` | {row['pad_count']} | `{', '.join(row['matched_tokens'])}` | {notes} |"
        )
    lines.extend(
        [
            "",
            "## Rule",
            "",
            "A footprint candidate is only a search result. It is not correct until the exact manufacturer package drawing, pad numbering, orientation, courtyard, paste/mask, and 3D model are checked.",
        ]
    )
    write_markdown(output_dir / f"footprint_candidates_{slug}.md", lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Find footprint candidates from generated KiCad footprint index.")
    parser.add_argument("query", help="Part, module, connector, package, or keyword query.")
    parser.add_argument("--footprint-index", help="Path to footprint_index.json. If missing, a temporary index is built read-only.")
    parser.add_argument("--kicad-root", help="KiCad install root used if index must be built.")
    parser.add_argument("--version", default="9.0", help="KiCad config version. Default: 9.0")
    parser.add_argument("--output-dir", default=str(default_output_dir()), help="Generated output folder.")
    parser.add_argument("--limit", type=int, default=25)
    args = parser.parse_args()

    kicad_root = detect_kicad_root(args.kicad_root, args.version)
    output_dir = ensure_safe_output_dir(Path(args.output_dir), kicad_root, args.version)
    index_path = Path(args.footprint_index) if args.footprint_index else output_dir / "footprint_index.json"
    if index_path.exists():
        index = load_json(index_path)
    else:
        if not kicad_root:
            fail("KiCad root not found and footprint_index.json is missing.")
        index = build_index(kicad_root, args.version)
    candidates = find_candidates(args.query, index, args.limit)
    write_candidate_files(output_dir, args.query, candidates)
    print(f"Wrote footprint candidate files for: {args.query}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
