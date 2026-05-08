#!/usr/bin/env python3
"""Find unresolved NEEDS_REVIEW/BLOCKED markers and high-risk symbols without markers."""

from __future__ import annotations

from pathlib import Path

from schematic_check_common import (
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    CHECK_STATUS_WARN,
    build_report_data,
    check_record,
    common_parser,
    exit_code_for,
    load_schematic,
    risk_categories,
    schematic_text_items,
    symbol_instances,
    symbol_search_text,
    write_optional_reports,
)


MARKERS = ("NEEDS_REVIEW", "BLOCKED", "UNVERIFIED", "TODO", "TBD")


def run_checks(schematic: Path) -> list[dict[str, str]]:
    root = load_schematic(schematic)
    checks: list[dict[str, str]] = []
    symbols = symbol_instances(root)
    marker_hits = 0

    for symbol in symbols:
        reference = str(symbol.get("reference", ""))
        text_upper = symbol_search_text(symbol).upper()
        found = [marker for marker in MARKERS if marker in text_upper]
        if found:
            marker_hits += 1
            checks.append(check_record(CHECK_STATUS_FAIL, "UNRESOLVED_REVIEW_MARKER_ON_SYMBOL", f"Unresolved review marker present: {', '.join(found)}.", reference, str(symbol.get("value", ""))))

        risks = risk_categories(symbol)
        if risks and not found and "VERIFIED" not in text_upper:
            checks.append(check_record(CHECK_STATUS_FAIL, "HIGH_RISK_SYMBOL_WITHOUT_REVIEW_MARKER", f"High-risk symbol lacks explicit VERIFIED/NEEDS_REVIEW/BLOCKED status: {', '.join(risks)}.", reference, str(symbol.get("value", ""))))

    for text in schematic_text_items(root):
        text_upper = text.upper()
        found = [marker for marker in MARKERS if marker in text_upper]
        if found:
            marker_hits += 1
            checks.append(check_record(CHECK_STATUS_FAIL, "UNRESOLVED_REVIEW_MARKER_IN_TEXT", f"Unresolved review marker present in schematic note: {', '.join(found)}.", "", text[:160]))

    if marker_hits == 0:
        checks.append(check_record(CHECK_STATUS_PASS, "NO_REVIEW_MARKERS_FOUND", "No unresolved NEEDS_REVIEW/BLOCKED/TODO/TBD markers were detected."))
    else:
        checks.append(check_record(CHECK_STATUS_WARN, "REVIEW_MARKERS_REQUIRE_GATE_BLOCKER", "Any unresolved review marker must block schematic-to-PCB gate until resolved or explicitly accepted by human review.", "", str(marker_hits)))
    return checks


def main() -> int:
    parser = common_parser("Check unresolved NEEDS_REVIEW/BLOCKED markers in a KiCad schematic.")
    args = parser.parse_args()
    schematic = Path(args.schematic)
    checks = run_checks(schematic)
    data = build_report_data(args, checks)
    write_optional_reports(args, "Needs Review Marker Check", data)
    return exit_code_for(data, args.no_fail)


if __name__ == "__main__":
    raise SystemExit(main())
