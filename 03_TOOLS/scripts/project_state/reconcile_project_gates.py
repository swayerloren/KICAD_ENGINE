#!/usr/bin/env python3
"""Reconcile operational gate decisions against live project state."""

from __future__ import annotations

import argparse
import json

from project_state_common import (
    build_live_state_outputs,
    detect_stale_reports_data,
    reconcile_gate_data,
    repo_root_from,
    resolve_project_path,
    write_gate_reconciliation_outputs,
    write_stale_reports_outputs,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Reconcile project gates against live file evidence.")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--project", required=True)
    parser.add_argument("--apply", action="store_true", help="Write stale-report and gate-reconciliation outputs.")
    args = parser.parse_args()

    repo_root = repo_root_from(args.repo_root)
    project = resolve_project_path(repo_root, args.project)
    live_state = build_live_state_outputs(project, repo_root, write_supporting=args.apply)
    stale_audit = detect_stale_reports_data(project, repo_root, live_state)
    reconciliation = reconcile_gate_data(project, repo_root, live_state, stale_audit)
    if args.apply:
        write_stale_reports_outputs(project, repo_root, stale_audit)
        write_gate_reconciliation_outputs(project, reconciliation)
    print(json.dumps(reconciliation, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
