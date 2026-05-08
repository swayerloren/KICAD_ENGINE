#!/usr/bin/env python3
"""Compare KiCad Engine component database records to installed KiCad footprints.

This script produces candidate matches only. It never verifies a footprint.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
import re
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
from kicad_library_common import detect_kicad_root, ensure_safe_output_dir, fail, score_text, write_json, write_markdown  # noqa: E402


HIGH_RISK_TERMS = {
    "usb": "USB and USB-C connector footprint/orientation risk.",
    "type-c": "USB-C footprints are not interchangeable.",
    "ufl": "RF connector mechanical compatibility risk.",
    "sma": "RF connector gender/orientation/edge-launch risk.",
    "esp32": "Module land pattern and antenna keepout risk.",
    "stm32": "Exact package suffix and pin-1/package drawing risk.",
    "pic": "Exact package suffix and pinout risk.",
    "rp2040": "QFN package drawing and exposed pad risk.",
    "lm2596": "Power/thermal package and layout risk.",
    "ams1117": "Regulator package and pinout variant risk.",
    "tvs": "Polarity/package risk.",
    "polyfuse": "Package and current rating risk.",
    "mosfet": "Gate/source/drain pin mapping risk.",
    "ao3401": "PMOS SOT-23 pin mapping and orientation risk.",
    "connector": "Connector orientation and mating-part risk.",
}

STOP_QUERY_WORDS = {
    "unknown",
    "requires",
    "source",
    "verification",
    "verify",
    "exact",
    "package",
    "drawing",
    "candidate",
    "candidates",
    "kicad",
    "library",
    "search",
    "before",
    "use",
    "part",
    "number",
    "manufacturer",
    "status",
    "unverified",
}


def default_output_dir() -> Path:
    return ROOT / "29_FOOTPRINT_GAP_ANALYSIS" / "GENERATED_INDEXES"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def collect_records(component_root: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted(component_root.rglob("*.json")):
        if "GENERATED_INDEXES" in path.parts:
            continue
        try:
            data = read_json(path)
        except Exception:
            continue
        candidates: list[Any]
        if isinstance(data, dict) and isinstance(data.get("records"), list):
            candidates = data["records"]
        elif isinstance(data, list):
            candidates = data
        else:
            candidates = []
        for item in candidates:
            if not isinstance(item, dict):
                continue
            part_number = str(item.get("part_number", "")).strip()
            if not part_number:
                continue
            records.append(
                {
                    "source_file": str(path),
                    "record_id": item.get("record_id", ""),
                    "part_number": part_number,
                    "vendor": item.get("vendor", ""),
                    "family": item.get("family", ""),
                    "category": item.get("category", ""),
                    "package": item.get("package", item.get("package_type", "")),
                    "kicad_footprint_candidates": item.get("kicad_footprint_candidates", []),
                    "verification_status": item.get("verification_status", item.get("verified_status", "")),
                    "footprint_status": item.get("footprint_status", ""),
                    "package_drawing_status": item.get("package_drawing_status", ""),
                    "human_review_required": item.get("human_review_required", True),
                }
            )
    return records


def normalize_candidate_text(value: Any) -> str:
    if isinstance(value, list):
        return " ".join(str(item) for item in value)
    return str(value)


def clean_query_text(value: str) -> str:
    lowered = value.lower()
    if "unknown - requires source verification" in lowered:
        return ""
    tokens = re.split(r"[^A-Za-z0-9_.:+/-]+", value)
    kept = []
    for token in tokens:
        stripped = token.strip()
        if not stripped:
            continue
        if stripped.lower() in STOP_QUERY_WORDS:
            continue
        if len(stripped) < 2:
            continue
        kept.append(stripped)
    return " ".join(kept)


def detect_risks(record: dict[str, Any]) -> list[str]:
    text = " ".join(
        [
            str(record.get("part_number", "")),
            str(record.get("vendor", "")),
            str(record.get("family", "")),
            str(record.get("category", "")),
            str(record.get("package", "")),
            normalize_candidate_text(record.get("kicad_footprint_candidates", "")),
        ]
    ).lower()
    normalized = re.sub(r"[^a-z0-9.+-]+", " ", text)
    notes = []
    if re.search(r"\busb\b|\busb[-_ ]?c\b|\btype[-_ ]?c\b", normalized):
        notes.append(HIGH_RISK_TERMS["usb"])
    if re.search(r"\bu\.?fl\b|\bipex\b|\bmhf\b", normalized):
        notes.append(HIGH_RISK_TERMS["ufl"])
    if re.search(r"\brp[-_ ]?sma\b|\bsma edge\b|\bsma connector\b", normalized):
        notes.append(HIGH_RISK_TERMS["sma"])
    for term, note in HIGH_RISK_TERMS.items():
        if term in {"usb", "type-c", "ufl", "sma"}:
            continue
        if re.search(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", normalized):
            notes.append(note)
    if not notes:
        notes.append("Exact package drawing verification required before use.")
    return list(dict.fromkeys(notes))


def find_footprint_candidates(record: dict[str, Any], footprints: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    query = " ".join(
        [
            clean_query_text(str(record.get("part_number", ""))),
            clean_query_text(str(record.get("package", ""))),
            clean_query_text(normalize_candidate_text(record.get("kicad_footprint_candidates", ""))),
        ]
    ).strip()
    if not query:
        return []
    rows: list[dict[str, Any]] = []
    for footprint in footprints:
        text = " ".join(
            [
                str(footprint.get("library", "")),
                str(footprint.get("footprint", "")),
                str(footprint.get("description", "")),
                str(footprint.get("tags", "")),
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
                "path": footprint.get("path", ""),
                "verification_status": "UNVERIFIED_CANDIDATE",
                "warning": "Do not use without exact package drawing and orientation review.",
            }
        )
    rows.sort(key=lambda row: (-int(row["score"]), str(row["library"]), str(row["footprint"])))
    return rows[:limit]


def build_matches(kicad_root: Path, version: str, component_root: Path, limit: int) -> dict[str, Any]:
    footprint_index = build_index(kicad_root, version)
    records = collect_records(component_root)
    matches = []
    for record in records:
        candidates = find_footprint_candidates(record, footprint_index.get("footprints", []), limit)
        package_status = str(record.get("package_drawing_status", "") or "").upper()
        footprint_status = str(record.get("footprint_status", "") or "").upper()
        exact_verified = "VERIFIED" in package_status and "UNVERIFIED" not in package_status and "VERIFIED" in footprint_status and "UNVERIFIED" not in footprint_status
        matches.append(
            {
                **record,
                "candidate_count": len(candidates),
                "top_candidates": candidates,
                "risk_notes": detect_risks(record),
                "exact_footprint_verification": "VERIFIED" if exact_verified else "UNVERIFIED",
                "human_review_required": True,
            }
        )
    return {
        "kicad_root": str(kicad_root),
        "component_root": str(component_root),
        "records_checked": len(records),
        "matches_with_candidates": sum(1 for row in matches if row["candidate_count"] > 0),
        "records_without_candidates": sum(1 for row in matches if row["candidate_count"] == 0),
        "verification_policy": "Candidate only. Exact footprint verification remains UNVERIFIED unless package drawing evidence exists.",
        "matches": matches,
    }


def write_match_markdown(path: Path, payload: dict[str, Any]) -> None:
    lines = [
        "# Component Database To Installed Footprint Candidate Matches",
        "",
        "Status: `UNVERIFIED_CANDIDATE_MATCHES`",
        "",
        f"KiCad root: `{payload['kicad_root']}`",
        f"Component root: `{payload['component_root']}`",
        "",
        "## Summary",
        "",
        f"- Component records checked: {payload['records_checked']}",
        f"- Records with at least one footprint candidate: {payload['matches_with_candidates']}",
        f"- Records without footprint candidates: {payload['records_without_candidates']}",
        "",
        "## Matches",
        "",
        "| Part | Category | Candidates | Exact Verification | Top Candidate | Risk |",
        "| --- | --- | ---: | --- | --- | --- |",
    ]
    for row in payload["matches"]:
        top = row["top_candidates"][0] if row["top_candidates"] else {}
        top_text = f"{top.get('library', '')}:{top.get('footprint', '')}" if top else "NONE"
        risk = " ".join(row["risk_notes"])
        lines.append(
            f"| `{row['part_number']}` | `{row.get('category', '')}` | {row['candidate_count']} | `{row['exact_footprint_verification']}` | `{top_text}` | {risk} |"
        )
    lines.extend(
        [
            "",
            "## Rule",
            "",
            "These are candidate search results only. They do not approve a footprint for schematic, PCB, BOM, or manufacturing work.",
        ]
    )
    write_markdown(path, lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Match component database records to installed KiCad footprint candidates.")
    parser.add_argument("--kicad-root", help="KiCad install root. Defaults to detected KiCad 9 root.")
    parser.add_argument("--version", default="9.0", help="KiCad config version. Default: 9.0")
    parser.add_argument("--component-root", default=str(ROOT / "08_COMPONENT_DATABASE"))
    parser.add_argument("--output-dir", default=str(default_output_dir()), help="Generated output folder.")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    kicad_root = detect_kicad_root(args.kicad_root, args.version)
    if not kicad_root:
        fail("KiCad root not found. Pass --kicad-root.")
    output_dir = ensure_safe_output_dir(Path(args.output_dir), kicad_root, args.version)
    payload = build_matches(kicad_root, args.version, Path(args.component_root), args.limit)
    write_json(output_dir / "component_db_to_footprint_matches.json", payload)
    write_match_markdown(output_dir / "component_db_to_footprint_matches.md", payload)
    print(json.dumps({k: payload[k] for k in ["records_checked", "matches_with_candidates", "records_without_candidates"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
