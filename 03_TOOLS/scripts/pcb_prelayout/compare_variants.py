#!/usr/bin/env python3
"""Compare prelayout variant scores and select the best candidate."""

from __future__ import annotations

import argparse
from typing import Any

from _prelayout_common import dump_json, dump_markdown, load_json


STATUS_PRIORITY = {
    "PASS": 0,
    "AUTO_BLOCKED_MISSING_DATA": 1,
    "AUTO_BLOCKED_BAD_LAYOUT": 2,
    "FAIL": 3,
}


def compare_variant_scores(scores: list[dict[str, Any]]) -> dict[str, Any]:
    ranked = sorted(
        scores,
        key=lambda item: (
            STATUS_PRIORITY.get(item["status"], 99),
            -float(item["total_score"]),
            int(item.get("projected_open_nets_count", 0)),
            len(item.get("hard_fail_codes", [])),
            item["variant_id"],
        ),
    )
    passing = [score for score in ranked if score["status"] == "PASS"]
    selected = ranked[0] if ranked else None
    return {
        "variant_count": len(scores),
        "passing_variant_count": len(passing),
        "ranked_scores": ranked,
        "selected_variant_id": selected["variant_id"] if selected else None,
        "selected_variant_status": selected["status"] if selected else None,
        "selected_total_score": selected["total_score"] if selected else None,
    }


def comparison_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# Variant Comparison",
        "",
        f"Variant count: `{payload['variant_count']}`",
        f"Passing variants: `{payload['passing_variant_count']}`",
        f"Selected variant: `{payload['selected_variant_id']}`",
        f"Selected status: `{payload['selected_variant_status']}`",
        "",
        "| Variant | Status | Total Score | Projected Open Nets | Live Open Nets |",
        "| --- | --- | --- | --- | --- |",
    ]
    for score in payload["ranked_scores"]:
        lines.append(
            f"| `{score['variant_id']}` | `{score['status']}` | `{score['total_score']}` | "
            f"`{score['projected_open_nets_count']}` | `{score['live_open_nets_count']}` |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("score_json", nargs="+", help="Input variant score JSON file(s).")
    parser.add_argument("output_json", help="Output comparison JSON file.")
    parser.add_argument("--markdown", help="Optional Markdown output path.")
    args = parser.parse_args()

    scores = [load_json(path) for path in args.score_json]
    payload = compare_variant_scores(scores)
    dump_json(args.output_json, payload)
    if args.markdown:
        dump_markdown(args.markdown, comparison_markdown(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
