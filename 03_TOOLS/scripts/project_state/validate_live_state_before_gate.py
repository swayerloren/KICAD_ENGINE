#!/usr/bin/env python3
"""Validate fresh live-state authority before any gate decision."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from live_state_authority import (  # type: ignore  # noqa: E402
    authority_summary,
    build_live_state_authority_bundle,
    repo_root_from,
    resolve_project_path,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate fresh live-state authority before running a project gate.")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--project", required=True)
    parser.add_argument("--task-contract", help="Optional task contract JSON to validate.")
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
    summary = authority_summary(bundle)
    summary["live_state_authority_valid"] = True
    print(json.dumps(summary, indent=2))

    task_contract = bundle["task_contract_validation"]
    return 0 if task_contract is None or task_contract["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
