#!/usr/bin/env python3
"""Build a routing reliability KPI dashboard from project routing history."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from detect_no_progress import analyze_no_progress
from routing_stage_contracts import (
    discover_edit_required_runs,
    dump_json,
    dump_markdown,
    latest_live_state,
    repo_root_from,
    reroute_revert_metrics,
    resolve_project_path,
    stale_report_count,
)


def reliability_score(
    live_state: dict[str, Any] | None,
    runs: list[dict[str, Any]],
    no_progress: dict[str, Any],
    reroute_metrics: dict[str, int],
) -> int:
    score = 100
    unchanged_runs = sum(1 for run in runs if run["hash_changed"] is False)
    geometry_failures = sum(len(run["geometry_failures"]) for run in runs)
    if live_state:
        drc = live_state.get("drc", {})
        score -= int(drc.get("violation_count", 0)) * 5
        score -= min(20, int(drc.get("unconnected_count", 0)) // 4)
        score -= min(15, int(live_state.get("pcb", {}).get("unrouted_net_count", 0)) * 2)
    score -= unchanged_runs * 2
    score -= no_progress["no_progress_event_count"] * 8
    if no_progress["status"] == "BLOCKED_REPAIR_MODE":
        score -= 15
    score -= geometry_failures * 2
    score -= reroute_metrics["revert_count"] * 2
    score += min(10, sum(1 for run in runs if run["made_progress"]))
    return max(0, min(100, score))


def build_dashboard(project: Path) -> dict[str, Any]:
    runs = discover_edit_required_runs(project)
    live_state = latest_live_state(project)
    no_progress = analyze_no_progress(project)
    reroute_metrics = reroute_revert_metrics(project)
    hash_delta_runs = [
        {
            "report": run["name"],
            "stage": run["stage"],
            "hash_before": run["pcb_hash_before"],
            "hash_after": run["pcb_hash_after"],
            "hash_changed": run["hash_changed"],
        }
        for run in runs
    ]
    drc_trend = [
        {
            "report": run["name"],
            "stage": run["stage"],
            "drc_violations_after": run["drc_violations_after"],
            "unconnected_after": run["unconnected_after"],
            "unrouted_after": run["unrouted_after"],
        }
        for run in runs
    ]
    net_reductions = [
        {
            "report": run["name"],
            "stage": run["stage"],
            "unconnected_delta": run["unconnected_delta"],
            "unrouted_delta": run["unrouted_delta"],
            "made_progress": run["made_progress"],
        }
        for run in runs
    ]
    dashboard = {
        "project": project.name,
        "generated_from": str(project),
        "edit_required_runs": len(runs),
        "pcb_hash_deltas": hash_delta_runs,
        "net_reductions": net_reductions,
        "drc_trend": drc_trend,
        "geometry_failures": [
            {"report": run["name"], "stage": run["stage"], "failures": run["geometry_failures"]}
            for run in runs
            if run["geometry_failures"]
        ],
        "stale_report_blocks": stale_report_count(project),
        "no_progress_status": no_progress["status"],
        "no_progress_events": no_progress["events"],
        "reroute_revert_count": reroute_metrics,
        "current_reliability_score": reliability_score(live_state, runs, no_progress, reroute_metrics),
        "current_live_state": {
            "pcb_hash": live_state["source_files"]["kicad_pcb"]["sha256"] if live_state else None,
            "unrouted_net_count": live_state["pcb"]["unrouted_net_count"] if live_state else None,
            "unconnected_count": live_state["drc"]["unconnected_count"] if live_state else None,
            "drc_violations": live_state["drc"]["violation_count"] if live_state else None,
        },
    }
    return dashboard


def render_markdown(dashboard: dict[str, Any]) -> str:
    lines = [
        "# Routing Reliability Dashboard",
        "",
        f"- Project: `{dashboard['project']}`",
        f"- Edit-required runs: `{dashboard['edit_required_runs']}`",
        f"- Current reliability score: `{dashboard['current_reliability_score']}` / 100",
        f"- No-progress status: `{dashboard['no_progress_status']}`",
        f"- Stale report blocks: `{dashboard['stale_report_blocks']}`",
        f"- Reroute count: `{dashboard['reroute_revert_count']['reroute_count']}`",
        f"- Revert/reject count: `{dashboard['reroute_revert_count']['revert_count']}`",
        "",
        "## Current Live State",
        f"- PCB hash: `{dashboard['current_live_state']['pcb_hash']}`",
        f"- Unrouted nets: `{dashboard['current_live_state']['unrouted_net_count']}`",
        f"- Unconnected items: `{dashboard['current_live_state']['unconnected_count']}`",
        f"- DRC violations: `{dashboard['current_live_state']['drc_violations']}`",
        "",
        "## No-Progress Events",
    ]
    if dashboard["no_progress_events"]:
        for event in dashboard["no_progress_events"]:
            lines.append(f"- `{event['trigger']}` between `{event['previous_report']}` and `{event['current_report']}`")
            if event["exact_repeated_blocker"]:
                lines.append("  - Repeated blocker: " + ", ".join(f"`{item}`" for item in event["exact_repeated_blocker"]))
            lines.append(f"  - Targeted repair: {event['recommended_targeted_repair']}")
    else:
        lines.append("- `_none_`")
    lines.extend(["", "## DRC Trend"])
    for row in dashboard["drc_trend"]:
        lines.append(
            f"- `{row['report']}` -> violations `{row['drc_violations_after']}`, unconnected `{row['unconnected_after']}`, unrouted `{row['unrouted_after']}`"
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--project", required=True)
    parser.add_argument("--output-json", required=True)
    parser.add_argument("--markdown", required=True)
    args = parser.parse_args()

    repo_root = repo_root_from(args.repo_root)
    project = resolve_project_path(repo_root, args.project)
    dashboard = build_dashboard(project)
    dump_json(args.output_json, dashboard)
    dump_markdown(args.markdown, render_markdown(dashboard))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
