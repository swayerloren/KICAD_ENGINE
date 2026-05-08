#!/usr/bin/env python3
"""Automatically select the best non-failed PCB layout variant."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from compare_layout_variants import pick_best_candidate, rank_results
from score_layout_variant import load_variant_file, score_variant


def _text_report(payload: dict) -> str:
    lines = [
        f"Selection status: {payload['selection_status']}",
        f"Variant count: {payload['variant_count']}",
    ]
    if payload["selected_variant_id"] is None:
        lines.append("Selected variant: NONE")
        lines.append(f"Reason: {payload['selection_reason']}")
    else:
        lines.extend(
            [
                f"Selected variant: {payload['selected_variant_id']}",
                f"Selected variant status: {payload['selected_variant_status']}",
                f"Selected score: {payload['selected_total_score']}",
                f"Reason: {payload['selection_reason']}",
            ]
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("variant_files", nargs="+", help="At least three variant files.")
    parser.add_argument(
        "--format",
        choices=("json", "text"),
        default="text",
        help="Output format.",
    )
    parser.add_argument("--output", help="Optional output file path.")
    args = parser.parse_args()

    if len(args.variant_files) < 3:
        print("ERROR: auto_select_best_variant.py requires at least three variants.", file=sys.stderr)
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
            "variant_count": len(results),
            "ranked_results": ranked,
            "selected_variant_id": None,
            "selected_variant_status": None,
            "selected_total_score": None,
            "selection_status": "AUTO_BLOCKED_BAD_LAYOUT",
            "selection_reason": "Every candidate has a hard fail, so no variant is selectable.",
        }
    else:
        payload = {
            "variant_count": len(results),
            "ranked_results": ranked,
            "selected_variant_id": selected["variant_id"],
            "selected_variant_status": selected["status"],
            "selected_total_score": selected["total_score"],
            "selection_status": "AUTO_SELECTED",
            "selection_reason": (
                f"{selected['variant_id']} was selected because it is the highest-ranked "
                f"non-failed variant at score {selected['total_score']}."
            ),
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
