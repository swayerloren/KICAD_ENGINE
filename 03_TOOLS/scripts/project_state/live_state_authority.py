#!/usr/bin/env python3
"""Canonical live-state authority helpers for project gates."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = next((path for path in [SCRIPT_DIR, *SCRIPT_DIR.parents] if (path / "AGENTS.md").exists()), SCRIPT_DIR).resolve()
EXECUTION_CONTRACT_DIR = REPO_ROOT / "03_TOOLS" / "scripts" / "execution_contract"
if str(EXECUTION_CONTRACT_DIR) not in sys.path:
    sys.path.insert(0, str(EXECUTION_CONTRACT_DIR))

from project_state_common import (  # type: ignore  # noqa: E402
    build_live_state_outputs,
    detect_stale_reports_data,
    file_metadata,
    find_one,
    load_json,
    preferred_project_file,
    reconcile_gate_data,
    repo_root_from,
    resolve_project_path,
    write_gate_reconciliation_outputs,
    write_stale_reports_outputs,
)
from validate_task_contract import evaluate_contract, load_contract  # type: ignore  # noqa: E402


BLOCKER_SOURCES = [
    "LIVE_FILE_EVIDENCE",
    "FRESH_GATE_REPORT",
    "STALE_REPORT_IGNORED",
    "TASK_CONTRACT_FAILURE",
    "HUMAN_REVIEW_REQUIRED",
]

AUTHORITY_RULES = [
    "Every phase and gate check must build or read fresh LIVE_PROJECT_STATE first.",
    "Operational reports without source hashes are weak context and cannot overrule live file evidence.",
    "Operational reports older than the current KiCad source hashes or timestamps are stale blockers.",
    "Stale NO_PCB, 0-footprint, or no-routing claims cannot override live PCB existence, footprint count, or track/via evidence.",
    "Gates may still block on real live-state failures such as DRC FAIL, unrouted nets, incomplete placement, or human-review requirements.",
]


def live_project_state_path(project: Path) -> Path:
    return project / "reports" / "LIVE_PROJECT_STATE.json"


def current_source_files(project: Path, repo_root: Path) -> dict[str, Any]:
    kicad_pro = preferred_project_file(project, ".kicad_pro") or find_one(project, ["kicad/*.kicad_pro", "*.kicad_pro"])
    kicad_sch = preferred_project_file(project, ".kicad_sch") or find_one(project, ["kicad/*.kicad_sch", "*.kicad_sch"])
    kicad_pcb = preferred_project_file(project, ".kicad_pcb") or find_one(project, ["kicad/*.kicad_pcb", "*.kicad_pcb"])
    return {
        "kicad_pro": file_metadata(kicad_pro, repo_root),
        "kicad_sch": file_metadata(kicad_sch, repo_root),
        "kicad_pcb": file_metadata(kicad_pcb, repo_root),
    }


def source_files_match(cached: Any, current: dict[str, Any]) -> bool:
    if not isinstance(cached, dict):
        return False
    for key in ("kicad_pro", "kicad_sch", "kicad_pcb"):
        cached_row = cached.get(key)
        current_row = current.get(key)
        if not isinstance(cached_row, dict) or not isinstance(current_row, dict):
            return False
        for field in ("exists", "sha256", "timestamp"):
            if cached_row.get(field) != current_row.get(field):
                return False
    return True


def load_fresh_live_project_state(project: Path, repo_root: Path, write_supporting: bool) -> tuple[dict[str, Any], dict[str, str]]:
    current_files = current_source_files(project, repo_root)
    state_path = live_project_state_path(project)
    if state_path.exists():
        try:
            cached = load_json(state_path)
        except Exception:
            cached = None
        if isinstance(cached, dict) and source_files_match(cached.get("source_files"), current_files):
            return cached, {
                "mode": "READ_FRESH_LIVE_PROJECT_STATE",
                "reason": "LIVE_PROJECT_STATE_SOURCE_HASHES_MATCH_CURRENT_FILES",
                "path": str(state_path.resolve()),
            }

    live_state = build_live_state_outputs(project, repo_root, write_supporting=write_supporting)
    return live_state, {
        "mode": "REBUILT_FROM_LIVE_FILES",
        "reason": "LIVE_PROJECT_STATE_MISSING_OR_OUTDATED",
        "path": str(state_path.resolve()),
    }


def evaluate_task_contract_result(task_contract_path: Path | None) -> dict[str, Any] | None:
    if task_contract_path is None:
        return None
    contract = load_contract(task_contract_path)
    result = evaluate_contract(contract, str(task_contract_path))
    result["contract_path"] = str(task_contract_path.resolve())
    return result


def build_live_state_authority_bundle(
    project: Path,
    repo_root: Path,
    write_supporting: bool = True,
    task_contract_path: str | Path | None = None,
) -> dict[str, Any]:
    task_contract = Path(task_contract_path).resolve() if task_contract_path else None
    live_state, live_state_source = load_fresh_live_project_state(project, repo_root, write_supporting)
    stale_audit = detect_stale_reports_data(project, repo_root, live_state)
    reconciliation = reconcile_gate_data(project, repo_root, live_state, stale_audit)

    if write_supporting:
        write_stale_reports_outputs(project, repo_root, stale_audit)
        write_gate_reconciliation_outputs(project, reconciliation)

    return {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "project": project.name,
        "project_path": str(project.resolve()),
        "authority_rules": AUTHORITY_RULES,
        "blocker_sources": BLOCKER_SOURCES,
        "live_state_source": live_state_source,
        "live_state": live_state,
        "stale_audit": stale_audit,
        "reconciliation": reconciliation,
        "task_contract_validation": evaluate_task_contract_result(task_contract),
    }


def authority_summary(bundle: dict[str, Any]) -> dict[str, Any]:
    live_state = bundle["live_state"]
    stale_audit = bundle["stale_audit"]
    reconciliation = bundle["reconciliation"]
    task_contract = bundle["task_contract_validation"]
    summary = {
        "generated_at": bundle["generated_at"],
        "project": bundle["project"],
        "project_path": bundle["project_path"],
        "live_state_source": bundle["live_state_source"],
        "live_pcb_hash": live_state["source_files"]["kicad_pcb"]["sha256"],
        "classification": live_state["classification"],
        "stale_report_count": len(stale_audit["stale_rows"]),
        "stale_reports_ignored": [row["file"] for row in stale_audit["stale_rows"]],
        "phase_results": reconciliation["phase_results"],
        "authority_rules": bundle["authority_rules"],
        "blocker_sources": bundle["blocker_sources"],
    }
    if task_contract is not None:
        summary["task_contract_validation"] = {
            "contract_path": task_contract["contract_path"],
            "valid": task_contract["valid"],
            "recommended_final_status": task_contract["recommended_final_status"],
            "error_count": len(task_contract["errors"]),
            "warning_count": len(task_contract["warnings"]),
        }
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Build or read the canonical live-state authority bundle.")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--project", required=True)
    parser.add_argument("--task-contract", help="Optional task contract JSON to validate alongside live state.")
    parser.add_argument("--dry-run", action="store_true", help="Do not rewrite supporting authority reports.")
    args = parser.parse_args()

    repo_root = repo_root_from(args.repo_root)
    project = resolve_project_path(repo_root, args.project)
    bundle = build_live_state_authority_bundle(
        project,
        repo_root,
        write_supporting=not args.dry_run,
        task_contract_path=args.task_contract,
    )
    print(json.dumps(authority_summary(bundle), indent=2))

    task_contract = bundle["task_contract_validation"]
    return 0 if task_contract is None or task_contract["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
