#!/usr/bin/env python3
"""Compile current project state into project memory."""

from __future__ import annotations

import argparse
from pathlib import Path

from run_memory_maintenance import current_project_state, state_markdown


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--project", default="04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    project = (root / args.project).resolve()
    text = state_markdown(current_project_state(root, project))
    target = project / "memory" / "CURRENT_PROJECT_STATE.md"
    if args.apply:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8", newline="\n")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
