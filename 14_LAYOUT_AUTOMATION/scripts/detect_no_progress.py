#!/usr/bin/env python3
"""Detect repeated no-progress routing loops from project routing history."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from routing_stage_contracts import (
    discover_edit_required_runs,
    dump_json,
    dump_markdown,
    recommended_stage_for_blockers,
    repo_root_from,
    resolve_project_path,
)


def _repeated_blockers(previous: dict[str, Any], current: dict[str, Any]) -> list[str]:
    previous_tokens = set(previous.get("blocker_tokens", []))
    current_tokens = set(current.get("blocker_tokens", []))
    return sorted(previous_tokens & current_tokens)


def _trigger_for_pair(previous: dict[str, Any], current: dict[str, Any]) -> tuple[str | None, list[str], list[str]]:
    repeated_blockers = _repeated_blockers(previous, current)
    repeated_blocker = bool(repeated_blockers) and (
        current["hash_changed"] is False or current["made_progress"] is False or bool(current["drc_worsened"])
    )
    no_hash_change_pair = previous["hash_changed"] is False and current["hash_changed"] is False
    no_reduction_pair = (
        previous.get("progress_comparable", False)
        and current.get("progress_comparable", False)
        and previous["made_progress"] is False
        and current["made_progress"] is False
    )
    drc_worsened_pair = (
        previous.get("drc_comparable", False)
        and current.get("drc_comparable", False)
        and bool(previous["drc_worsened"])
        and bool(current["drc_worsened"])
    )
    reasons: list[str] = []
    if no_hash_change_pair:
        reasons.append("no PCB hash change on two consecutive edit-required runs")
    if no_reduction_pair:
        reasons.append("no unrouted/unconnected reduction on two consecutive edit-required runs")
    if drc_worsened_pair:
        reasons.append("DRC worsened on two consecutive edit-required runs")
    if repeated_blocker:
        reasons.append("same blocker repeats on consecutive edit-required runs")
    if reasons:
        if no_hash_change_pair:
            return "NO_HASH_CHANGE_PAIR", reasons, repeated_blockers
        if no_reduction_pair:
            return "NO_REDUCTION_PAIR", reasons, repeated_blockers
        if drc_worsened_pair:
            return "DRC_WORSENED_PAIR", reasons, repeated_blockers
        return "REPEATED_BLOCKER_PAIR", reasons, repeated_blockers
    return None, [], []


def analyze_no_progress(project: Path) -> dict[str, Any]:
    runs = discover_edit_required_runs(project)
    events: list[dict[str, Any]] = []
    for previous, current in zip(runs, runs[1:]):
        trigger, reasons, repeated_blockers = _trigger_for_pair(previous, current)
        if not trigger:
            continue
        blockers = repeated_blockers or current["blocker_tokens"] or previous["blocker_tokens"]
        target_stage, recommendation = recommended_stage_for_blockers(blockers)
        events.append(
            {
                "trigger": trigger,
                "reason_lines": reasons,
                "previous_report": previous["name"],
                "current_report": current["name"],
                "previous_stage": previous["stage"],
                "current_stage": current["stage"],
                "previous_status": previous["status"],
                "current_status": current["status"],
                "blocker_tokens": blockers,
                "exact_repeated_blocker": repeated_blockers,
                "recommended_target_stage": target_stage,
                "recommended_targeted_repair": recommendation,
            }
        )

    latest_event = events[-1] if events else None
    status = "BLOCKED_REPAIR_MODE" if latest_event else "PROGRESS_CONTINUABLE"
    return {
        "project": project.name,
        "status": status,
        "edit_required_run_count": len(runs),
        "no_progress_event_count": len(events),
        "runs": runs,
        "events": events,
        "exact_repeated_blocker": latest_event["exact_repeated_blocker"] if latest_event else [],
        "recommended_target_stage": latest_event["recommended_target_stage"] if latest_event else None,
        "recommended_targeted_repair": latest_event["recommended_targeted_repair"] if latest_event else None,
    }


def render_markdown(result: dict[str, Any]) -> str:
    lines = [
        "# No-Progress Detector",
        "",
        f"- Project: `{result['project']}`",
        f"- Status: `{result['status']}`",
        f"- Edit-required runs reviewed: `{result['edit_required_run_count']}`",
        f"- No-progress events: `{result['no_progress_event_count']}`",
        "",
        "## Events",
    ]
    if result["events"]:
        for event in result["events"]:
            lines.append(
                f"- `{event['trigger']}` between `{event['previous_report']}` and `{event['current_report']}`"
            )
            for reason in event["reason_lines"]:
                lines.append(f"  - Reason: {reason}")
            if event["exact_repeated_blocker"]:
                lines.append("  - Exact repeated blocker: " + ", ".join(f"`{item}`" for item in event["exact_repeated_blocker"]))
            lines.append(f"  - Recommended target stage: `{event['recommended_target_stage']}`")
            lines.append(f"  - Recommended targeted repair: {event['recommended_targeted_repair']}")
    else:
        lines.append("- `_none_`")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--project", required=True)
    parser.add_argument("--output-json")
    parser.add_argument("--markdown")
    args = parser.parse_args()

    repo_root = repo_root_from(args.repo_root)
    project = resolve_project_path(repo_root, args.project)
    result = analyze_no_progress(project)

    if args.output_json:
        dump_json(args.output_json, result)
    if args.markdown:
        dump_markdown(args.markdown, render_markdown(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
