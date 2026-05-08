#!/usr/bin/env python3
"""Update current project state and blocker summaries from live state."""

from __future__ import annotations

import argparse
import json

from project_state_common import (
    build_live_state_outputs,
    detect_stale_reports_data,
    reconcile_gate_data,
    repo_root_from,
    resolve_project_path,
    update_phase_status_outputs,
    write_gate_reconciliation_outputs,
    write_stale_reports_outputs,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Update current-state memory files from live project state.")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--project", required=True)
    parser.add_argument("--apply", action="store_true", help="Write project memory state files.")
    args = parser.parse_args()

    repo_root = repo_root_from(args.repo_root)
    project = resolve_project_path(repo_root, args.project)
    live_state = build_live_state_outputs(project, repo_root, write_supporting=args.apply)
    stale_audit = detect_stale_reports_data(project, repo_root, live_state)
    reconciliation = reconcile_gate_data(project, repo_root, live_state, stale_audit)
    if args.apply:
        write_stale_reports_outputs(project, repo_root, stale_audit)
        write_gate_reconciliation_outputs(project, reconciliation)
        update_phase_status_outputs(project, repo_root, live_state, reconciliation)
    print(
        json.dumps(
            {
                "live_state_classification": live_state["classification"],
                "phase_results": reconciliation["phase_results"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
