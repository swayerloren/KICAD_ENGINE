#!/usr/bin/env python3
"""Build LIVE_PROJECT_STATE from actual KiCad project files."""

from __future__ import annotations

import argparse
import json

from project_state_common import build_live_state_outputs, repo_root_from, resolve_project_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Build live KiCad project state from actual project files.")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--project", required=True)
    parser.add_argument("--apply", action="store_true", help="Write LIVE_PROJECT_STATE.json and .md")
    args = parser.parse_args()

    repo_root = repo_root_from(args.repo_root)
    project = resolve_project_path(repo_root, args.project)
    live_state = build_live_state_outputs(project, repo_root, write_supporting=args.apply)
    print(json.dumps(live_state, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
