#!/usr/bin/env python3
"""Detect stale or contradictory operational project reports."""

from __future__ import annotations

import argparse
import json

from project_state_common import (
    build_live_state_outputs,
    detect_stale_reports_data,
    repo_root_from,
    resolve_project_path,
    write_stale_reports_outputs,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Detect stale or contradictory operational reports.")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--project", required=True)
    parser.add_argument("--apply", action="store_true", help="Write STALE_REPORTS_AUDIT.json and .md")
    args = parser.parse_args()

    repo_root = repo_root_from(args.repo_root)
    project = resolve_project_path(repo_root, args.project)
    live_state = build_live_state_outputs(project, repo_root, write_supporting=args.apply)
    audit = detect_stale_reports_data(project, repo_root, live_state)
    if args.apply:
        write_stale_reports_outputs(project, repo_root, audit)
    print(json.dumps(audit, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
