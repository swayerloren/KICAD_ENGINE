#!/usr/bin/env python3
"""Canonical live-state gate wrapper for project phase checks."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from live_state_authority import (  # type: ignore  # noqa: E402
    build_live_state_authority_bundle,
    repo_root_from,
    resolve_project_path,
)
from project_state_common import PHASE_NAMES  # type: ignore  # noqa: E402


ALIASES = {
    "0": 0,
    "phase0": 0,
    "intake": 0,
    "1": 1,
    "phase1": 1,
    "schematic": 1,
    "schematic_gate": 1,
    "2": 2,
    "phase2": 2,
    "pcb": 2,
    "pcb_create": 2,
    "pcb_creation": 2,
    "pcb_update": 2,
    "update_pcb": 2,
    "3": 3,
    "phase3": 3,
    "placement_plan": 3,
    "placement_planning": 3,
    "4": 4,
    "phase4": 4,
    "mechanical": 4,
    "mechanical_setup": 4,
    "5": 5,
    "phase5": 5,
    "placement": 5,
    "component_placement": 5,
    "6": 6,
    "phase6": 6,
    "placement_audit": 6,
    "orientation": 6,
    "7": 7,
    "phase7": 7,
    "zones": 7,
    "ground": 7,
    "8": 8,
    "phase8": 8,
    "routing": 8,
    "route": 8,
    "9": 9,
    "phase9": 9,
    "final_pcb": 9,
    "final_pcb_audit": 9,
    "10": 10,
    "phase10": 10,
    "jlcpcb": 10,
    "production": 10,
    "production_review": 10,
    "dfm": 10,
    "dfa": 10,
    "11": 11,
    "phase11": 11,
    "export": 11,
    "not_final": 11,
    "not_final_export": 11,
    "fab_export": 11,
    "12": 12,
    "phase12": 12,
    "upload_feedback": 12,
    "jlc_feedback": 12,
    "13": 13,
    "phase13": 13,
    "signoff": 13,
    "final_signoff": 13,
}


def parse_phase(raw: str) -> int:
    key = raw.strip().lower().replace("-", "_").replace(" ", "_")
    if key.startswith("phase_"):
        key = "phase" + key.split("_", 1)[1]
    if key not in ALIASES:
        valid = ", ".join(str(number) for number in sorted(PHASE_NAMES))
        raise SystemExit(f"Unknown phase '{raw}'. Use one of: {valid}")
    return ALIASES[key]


def generic_phase_result(phase: int, live_state: dict[str, object], reconciliation: dict[str, object]) -> dict[str, object]:
    source_files = live_state["source_files"]  # type: ignore[index]
    pcb = live_state["pcb"]  # type: ignore[index]
    drc = live_state["drc"]  # type: ignore[index]
    phase8 = reconciliation["phase_results"]["8"]  # type: ignore[index]

    result = {
        "phase": phase,
        "name": PHASE_NAMES[phase],
        "result": "BLOCKED",
        "phase_status": "BLOCKED",
        "next_required_phase": phase,
        "blockers": [],
        "warnings": [],
        "evidence_decisions": [],
    }

    if phase == 0:
        result["result"] = "ALLOWED"
        result["phase_status"] = "PROJECT_IDENTIFIED"
        return result
    if phase == 1:
        if source_files["kicad_sch"]["exists"]:  # type: ignore[index]
            result["result"] = "ALLOWED"
            result["phase_status"] = "SCHEMATIC_PRESENT"
            result["next_required_phase"] = 2
            result["evidence_decisions"] = [{"source": "LIVE_FILE_EVIDENCE", "message": "Live schematic file exists."}]
        else:
            result["blockers"] = ["Live schematic file is missing."]
        return result
    if phase in {4, 5, 6, 7}:
        if pcb["exists"]:  # type: ignore[index]
            result["result"] = "ALLOWED"
            result["phase_status"] = "LIVE_BOARD_EXISTS_HUMAN_REVIEW_REQUIRED"
            result["next_required_phase"] = min(phase + 1, 13)
            result["evidence_decisions"] = [
                {
                    "source": "LIVE_FILE_EVIDENCE",
                    "message": f"Live PCB exists with {pcb['footprint_count']} footprints and {pcb['track_count']} tracks.",
                }
            ]
            result["warnings"] = ["Phase order is being interpreted from live board evidence because later physical work already exists."]
        else:
            result["blockers"] = ["Live PCB file is missing."]
            result["next_required_phase"] = 2
        return result
    if phase >= 9:
        if phase8["result"] == "BLOCKED":  # type: ignore[index]
            result["blockers"] = ["Routing phase is still blocked by live board evidence."]
            result["evidence_decisions"] = [{"source": "LIVE_FILE_EVIDENCE", "message": "Routing remains incomplete or unsafe on the live board."}]
            result["warnings"] = ["Downstream production/export/signoff phases cannot continue while live routing is blocked."]
            result["phase_status"] = "PHASE_8_NOT_COMPLETE"
            result["next_required_phase"] = 8
            return result
        if drc["result"] == "FAIL" or pcb["unrouted_net_count"] > 0:  # type: ignore[index]
            result["blockers"] = ["Live DRC or unrouted-net evidence is still failing."]
            result["evidence_decisions"] = [{"source": "LIVE_FILE_EVIDENCE", "message": "Final PCB evidence is not clean enough for downstream phases."}]
            result["phase_status"] = "FINAL_EVIDENCE_NOT_CLEAN"
            result["next_required_phase"] = 8
            return result
        result["result"] = "ALLOWED"
        result["phase_status"] = "LIVE_BOARD_EVIDENCE_CLEAN"
        result["next_required_phase"] = min(phase + 1, 13)
        return result
    return result


def task_contract_failure_result(phase: int, task_contract: dict[str, object]) -> dict[str, object]:
    errors = [str(item) for item in task_contract.get("errors", [])]  # type: ignore[union-attr]
    warnings = [str(item) for item in task_contract.get("warnings", [])]  # type: ignore[union-attr]
    evidence_decisions = [
        {
            "source": "TASK_CONTRACT_FAILURE",
            "message": error,
        }
        for error in errors
    ] or [
        {
            "source": "TASK_CONTRACT_FAILURE",
            "message": "Task contract validation failed.",
        }
    ]
    return {
        "phase": phase,
        "name": PHASE_NAMES[phase],
        "result": "BLOCKED",
        "phase_status": "TASK_CONTRACT_FAILURE",
        "next_required_phase": phase,
        "blockers": [f"Task contract validation failed: {error}" for error in errors] or ["Task contract validation failed."],
        "warnings": warnings,
        "evidence_decisions": evidence_decisions,
    }


def resolve_phase_result(phase: int, bundle: dict[str, object]) -> dict[str, object]:
    task_contract = bundle.get("task_contract_validation")
    if isinstance(task_contract, dict) and task_contract.get("valid") is False:
        return task_contract_failure_result(phase, task_contract)

    reconciliation = bundle["reconciliation"]  # type: ignore[index]
    phase_result = reconciliation["phase_results"].get(str(phase))  # type: ignore[index]
    if phase_result is None:
        phase_result = generic_phase_result(phase, bundle["live_state"], reconciliation)  # type: ignore[index]
    return phase_result


def emit_phase_gate_output(project: Path, phase: int, phase_result: dict[str, object], bundle: dict[str, object]) -> None:
    live_state = bundle["live_state"]  # type: ignore[index]
    stale_audit = bundle["stale_audit"]  # type: ignore[index]
    live_state_source = bundle["live_state_source"]  # type: ignore[index]
    gate_status = phase_result["result"]  # type: ignore[index]
    next_phase = phase_result["next_required_phase"]  # type: ignore[index]

    print(f"PHASE_GATE_RESULT: {gate_status}")
    print(f"PROJECT: {project}")
    print(f"REQUESTED_PHASE: {phase} - {PHASE_NAMES[phase]}")
    print(f"PHASE_STATUS: {phase_result['phase_status']}")
    print(f"LIVE_PROJECT_STATE_FILE: {project / 'reports' / 'LIVE_PROJECT_STATE.json'}")
    print(f"LIVE_PROJECT_STATE_SOURCE: {live_state_source['mode']}")
    print(f"LIVE_PROJECT_STATE_FRESHNESS_REASON: {live_state_source['reason']}")
    print(f"NEXT_REQUIRED_PHASE: {next_phase} - {PHASE_NAMES[next_phase]}")

    blockers = phase_result["blockers"]  # type: ignore[index]
    print("MISSING_PREREQUISITES:")
    if blockers:
        for blocker in blockers:
            print(f"- {blocker}")
    else:
        print("- none")

    print("EVIDENCE_DECISIONS:")
    for decision in phase_result["evidence_decisions"]:  # type: ignore[index]
        print(f"- {decision['source']}: {decision['message']}")

    stale_rows = stale_audit["stale_rows"]  # type: ignore[index]
    if stale_rows:
        for row in stale_rows:
            print(f"- STALE_REPORT_IGNORED: {row['file']} -> {', '.join(row['reasons'])}")
    else:
        print("- STALE_REPORT_IGNORED: none")

    print("WARNINGS:")
    warnings = phase_result["warnings"]  # type: ignore[index]
    if warnings:
        for warning in warnings:
            print(f"- HUMAN_REVIEW_REQUIRED: {warning}")
    else:
        print("- none")

    print("READ_ONLY_KICAD: yes")
    print(f"LIVE_PCB_HASH: {live_state['source_files']['kicad_pcb']['sha256']}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Canonical live-state-aware KiCad phase gate checker.")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--project", required=True, help="Active project path.")
    parser.add_argument("--phase", required=True, help="Requested phase number or alias.")
    parser.add_argument("--task-contract", help="Optional task contract JSON to validate before gate output.")
    parser.add_argument("--lj-approval", action="store_true", help="Retained for CLI compatibility.")
    parser.add_argument("--jlc-feedback-provided", action="store_true", help="Retained for CLI compatibility.")
    args = parser.parse_args()

    repo_root = repo_root_from(args.repo_root)
    project = resolve_project_path(repo_root, args.project)
    phase = parse_phase(args.phase)
    bundle = build_live_state_authority_bundle(
        project,
        repo_root,
        write_supporting=True,
        task_contract_path=args.task_contract,
    )
    phase_result = resolve_phase_result(phase, bundle)
    emit_phase_gate_output(project, phase, phase_result, bundle)
    return 0 if phase_result["result"] == "ALLOWED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
