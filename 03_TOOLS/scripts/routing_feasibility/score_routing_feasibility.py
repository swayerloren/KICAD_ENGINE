from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_metrics(payload: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    metrics = payload.get("metrics", payload)
    context = {
        "review_status": payload.get("review_status", metrics.get("review_status", "REVIEW_ONLY")),
        "run_status": payload.get("run_status", "COMPLETED"),
        "project": payload.get("project"),
        "variant_id": payload.get("variant_id"),
    }
    return metrics, context


def classify(metrics: dict[str, Any], context: dict[str, Any]) -> dict[str, Any]:
    if context["run_status"] == "UNAVAILABLE":
        return {
            "review_status": "REVIEW_ONLY",
            "routing_feasibility_status": "NEEDS_HUMAN_REVIEW",
            "routing_feasibility_score_0_to_10": None,
            "score_available": False,
            "reason": "FreeRouting runtime unavailable. Fall back to manual routing-feasibility scoring.",
            "notes": [
                "This is not a routing failure.",
                "Use manual routing-projection evidence for the sandbox score.",
            ],
        }

    total_nets = int(metrics.get("total_nets") or 0)
    unrouted_count = int(metrics.get("unrouted_net_count") or len(metrics.get("unrouted_nets") or []))
    via_count = metrics.get("via_count")
    congestion_mentions = int(metrics.get("congestion_mentions") or 0)
    trace_length_mm = metrics.get("reported_trace_length_mm")
    unrouted_ratio = (unrouted_count / total_nets) if total_nets > 0 else 0.0

    score = 10
    reasons: list[str] = []

    if total_nets > 0:
        if unrouted_ratio > 0.25:
            score -= 6
            reasons.append("High unrouted-net ratio suggests an implausible or congested placement.")
        elif unrouted_ratio > 0.10:
            score -= 4
            reasons.append("Moderate unrouted-net ratio suggests meaningful congestion.")
        elif unrouted_count > 0:
            score -= 2
            reasons.append("A small unrouted-net set remains.")

    if via_count is not None:
        if via_count > 80:
            score -= 3
            reasons.append("High via count suggests escape or channel pressure.")
        elif via_count > 50:
            score -= 2
            reasons.append("Moderate via pressure detected.")
        elif via_count > 25:
            score -= 1
            reasons.append("Some via pressure detected.")

    if congestion_mentions >= 4:
        score -= 2
        reasons.append("FreeRouting output reported repeated congestion-style signals.")
    elif congestion_mentions >= 1:
        score -= 1
        reasons.append("FreeRouting output reported at least one congestion-style signal.")

    if isinstance(trace_length_mm, (int, float)):
        if trace_length_mm > 200:
            score -= 2
            reasons.append("Reported trace length looks long for a compact-board feasibility probe.")
        elif trace_length_mm > 120:
            score -= 1
            reasons.append("Reported trace length may indicate a longer-than-ideal path set.")

    score = max(0, min(10, score))

    if context["run_status"] in {"TIMEOUT", "ERROR"}:
        status = "NEEDS_HUMAN_REVIEW"
        reasons.append("Dry run did not complete cleanly.")
    elif total_nets > 0 and unrouted_ratio > 0.25:
        status = "FAIL"
    elif score >= 8 and unrouted_count == 0:
        status = "PASS"
    else:
        status = "NEEDS_HUMAN_REVIEW"

    notes = [
        "REVIEW_ONLY: do not treat this output as final routing approval.",
        "USB, RF, switching-regulator, and high-current nets still require human engineering review.",
    ]
    notes.extend(reasons)

    return {
        "review_status": "REVIEW_ONLY",
        "routing_feasibility_status": status,
        "routing_feasibility_score_0_to_10": score,
        "score_available": True,
        "unrouted_ratio": round(unrouted_ratio, 4) if total_nets > 0 else None,
        "notes": notes,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Score FreeRouting dry-run feasibility evidence.")
    parser.add_argument("input_json", type=Path, help="Path to a run manifest or parsed-metrics JSON file.")
    parser.add_argument("--output-json", type=Path, help="Optional JSON output path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payload = load_json(args.input_json.resolve())
    metrics, context = normalize_metrics(payload)
    result = {
        "tool": "score_routing_feasibility",
        "project": context.get("project"),
        "variant_id": context.get("variant_id"),
        "input_json": str(args.input_json.resolve()),
        "result": classify(metrics, context),
    }

    serialized = json.dumps(result, indent=2)
    if args.output_json is not None:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(serialized + "\n", encoding="utf-8")
    print(serialized)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
