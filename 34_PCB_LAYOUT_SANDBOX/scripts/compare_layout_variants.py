#!/usr/bin/env python3
"""Compare at least three PCB layout variants and rank the best candidate."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from score_layout_variant import load_variant_file, score_variant


STATUS_PRIORITY = {
    "PASS": 0,
    "AUTO_BLOCKED_MISSING_DATA": 1,
    "AUTO_BLOCKED_BAD_LAYOUT": 2,
    "FAIL": 3,
}


def rank_results(results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        results,
        key=lambda item: (
            STATUS_PRIORITY.get(item["status"], 99),
            -item["total_score"],
            item["total_penalty"],
            -item["category_subtotal"],
            item["variant_id"],
        ),
    )


def pick_best_candidate(results: list[dict[str, Any]]) -> dict[str, Any] | None:
    eligible = [item for item in results if item["status"] != "FAIL"]
    ranked = rank_results(eligible)
    return ranked[0] if ranked else None


def _selection_reason(selected: dict[str, Any]) -> str:
    return (
        f"{selected['variant_id']} is the highest-ranked non-failed variant. "
        f"It scored {selected['total_score']} with status {selected['status']}."
    )


def _text_report(
    payload: dict[str, Any],
) -> str:
    lines = ["Variant Ranking:"]
    for item in payload["ranked_results"]:
        lines.append(
            "- "
            f"{item['variant_id']}: status={item['status']}, "
            f"total={item['total_score']}, "
            f"drc_risk={item['drc_precheck_risk_level']}, "
            f"uncertainty_risk={item['human_uncertainty_risk_level']}"
        )
    lines.append("")
    lines.append(f"Comparison status: {payload['comparison_status']}")
    if payload["selected_variant_id"] is None:
        lines.append("Selected variant: NONE")
        lines.append(f"Selection status: {payload['selection_status']}")
        lines.append(f"Reason: {payload['selection_reason']}")
    else:
        lines.append(f"Selected variant: {payload['selected_variant_id']}")
        lines.append(f"Selected variant status: {payload['selected_variant_status']}")
        lines.append(f"Selection status: {payload['selection_status']}")
        lines.append(f"Reason: {payload['selection_reason']}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "variant_files",
        nargs="+",
        help="At least three JSON files or Markdown files with fenced JSON.",
    )
    parser.add_argument(
        "--format",
        choices=("json", "text"),
        default="text",
        help="Output format.",
    )
    parser.add_argument("--output", help="Optional output file path.")
    args = parser.parse_args()

    if len(args.variant_files) < 3:
        print("ERROR: compare_layout_variants.py requires at least three variants.", file=sys.stderr)
        return 2

    try:
        results = [
            score_variant(load_variant_file(path), source=str(Path(path)))
            for path in args.variant_files
        ]
    except Exception as exc:  # pragma: no cover
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    ranked = rank_results(results)
    selected = pick_best_candidate(results)

    if selected is None:
        payload = {
            "comparison_status": "AUTO_BLOCKED_BAD_LAYOUT",
            "variant_count": len(results),
            "results": results,
            "ranked_results": ranked,
            "selected_variant_id": None,
            "selected_variant_status": None,
            "selection_status": "AUTO_BLOCKED_BAD_LAYOUT",
            "selection_reason": "Every candidate has at least one hard fail.",
        }
    else:
        payload = {
            "comparison_status": "PASS",
            "variant_count": len(results),
            "results": results,
            "ranked_results": ranked,
            "selected_variant_id": selected["variant_id"],
            "selected_variant_status": selected["status"],
            "selection_status": "AUTO_SELECTED",
            "selection_reason": _selection_reason(selected),
        }

    rendered = (
        json.dumps(payload, indent=2, sort_keys=True)
        if args.format == "json"
        else _text_report(payload)
    )

    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
