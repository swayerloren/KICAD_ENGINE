#!/usr/bin/env python3
"""Evaluate whether a project may enter a requested routing stage."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from detect_no_progress import analyze_no_progress
from routing_stage_contracts import (
    RoutingStageContract,
    STAGE_CONTRACTS,
    dump_json,
    dump_markdown,
    expand_required_matches,
    latest_live_state,
    latest_placement_scorecard_status,
    repo_root_from,
    resolve_project_path,
    stage_contract,
)


def evaluate_stage(project: Path, contract: RoutingStageContract) -> dict[str, Any]:
    file_matches = expand_required_matches(project, contract.required_input_files)
    missing = [pattern for pattern, matches in file_matches.items() if not matches]
    live_state = latest_live_state(project)
    placement_status = latest_placement_scorecard_status(project)
    no_progress = analyze_no_progress(project)

    blockers: list[str] = []
    warnings: list[str] = []
    evidence: list[dict[str, str]] = []

    if missing:
        blockers.extend(f"Missing required input pattern: {pattern}" for pattern in missing)
    else:
        evidence.append({"source": "FILES_PRESENT", "message": "All required stage input file patterns resolved to at least one file."})

    if contract.name != "placement_readiness":
        if placement_status != "PLACEMENT_READY_FOR_ROUTING":
            blockers.append(
                "Placement readiness scorecard is not exact PLACEMENT_READY_FOR_ROUTING."
            )
        else:
            evidence.append({"source": "PLACEMENT_SCORECARD", "message": "Placement readiness scorecard is exact PLACEMENT_READY_FOR_ROUTING."})

    if live_state:
        drc = live_state.get("drc", {})
        current_phase = live_state.get("current_real_phase", {})
        evidence.append(
            {
                "source": "LIVE_PROJECT_STATE",
                "message": (
                    f"Live PCB hash {live_state['source_files']['kicad_pcb']['sha256']} "
                    f"with {live_state['pcb']['unrouted_net_count']} unrouted nets and "
                    f"{drc.get('unconnected_count', 'unknown')} unconnected items."
                ),
            }
        )
        if contract.name == "placement_readiness":
            pass
        elif drc.get("violation_count", 0) > 0:
            blockers.append("Live DRC violations are nonzero.")
        elif current_phase.get("routing_plan_may_continue") is False:
            warnings.append("Live project state still says routing_plan_may_continue=false; this stage should only proceed as targeted repair work.")
    else:
        blockers.append("LIVE_PROJECT_STATE.json is missing.")

    if no_progress["status"] == "BLOCKED_REPAIR_MODE" and contract.name not in {
        no_progress.get("recommended_target_stage"),
        "trace_geometry_cleanup",
    }:
        blockers.append(
            "No-progress detector is in BLOCKED_REPAIR_MODE. Broad routing must stop until the targeted repair stage is handled."
        )
        warnings.append(
            f"Recommended target stage: {no_progress.get('recommended_target_stage')} -> {no_progress.get('recommended_targeted_repair')}"
        )

    if blockers:
        status = "STAGE_BLOCKED"
        pass_output = contract.fail_outputs[0]
    else:
        status = "STAGE_READY"
        pass_output = contract.pass_output

    return {
        "project": project.name,
        "stage": contract.name,
        "status": status,
        "stage_output": pass_output,
        "required_input_matches": file_matches,
        "allowed_nets": contract.allowed_nets,
        "forbidden_nets": contract.forbidden_nets,
        "drc_requirement": contract.drc_requirement,
        "geometry_requirement": contract.geometry_requirement,
        "hash_delta_required": contract.hash_delta_required,
        "copied_board_rehearsal_required": contract.copied_board_rehearsal_required,
        "next_allowed_stage": contract.next_allowed_stage,
        "blockers": blockers,
        "warnings": warnings,
        "evidence": evidence,
        "no_progress_status": no_progress["status"],
        "recommended_targeted_repair": no_progress.get("recommended_targeted_repair"),
    }


def render_markdown(result: dict[str, Any]) -> str:
    lines = [
        "# Staged Routing Runner",
        "",
        f"- Project: `{result['project']}`",
        f"- Stage: `{result['stage']}`",
        f"- Status: `{result['status']}`",
        f"- Stage output: `{result['stage_output']}`",
        f"- Next allowed stage: `{result['next_allowed_stage']}`",
        "",
        "## Blockers",
    ]
    if result["blockers"]:
        lines.extend(f"- {item}" for item in result["blockers"])
    else:
        lines.append("- `_none_`")
    lines.extend(["", "## Warnings"])
    if result["warnings"]:
        lines.extend(f"- {item}" for item in result["warnings"])
    else:
        lines.append("- `_none_`")
    lines.extend(["", "## Evidence"])
    if result["evidence"]:
        for item in result["evidence"]:
            lines.append(f"- `{item['source']}`: {item['message']}")
    else:
        lines.append("- `_none_`")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--project", required=True)
    parser.add_argument("--stage", required=True, choices=sorted(STAGE_CONTRACTS))
    parser.add_argument("--output-json")
    parser.add_argument("--markdown")
    args = parser.parse_args()

    repo_root = repo_root_from(args.repo_root)
    project = resolve_project_path(repo_root, args.project)
    contract = stage_contract(args.stage)
    result = evaluate_stage(project, contract)
    if args.output_json:
        dump_json(args.output_json, result)
    if args.markdown:
        dump_markdown(args.markdown, render_markdown(result))
    return 0 if result["status"] == "STAGE_READY" else 1


if __name__ == "__main__":
    raise SystemExit(main())
