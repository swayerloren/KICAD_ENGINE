#!/usr/bin/env python3
"""Shared prompt-counter helpers for the maintenance supervisor."""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent


def repo_root_from(repo_root: str | Path | None = None) -> Path:
    if repo_root:
        return Path(repo_root).resolve()
    return next((path for path in [SCRIPT_DIR, *SCRIPT_DIR.parents] if (path / "AGENTS.md").exists()), SCRIPT_DIR).resolve()


def config_path(repo_root: Path) -> Path:
    return repo_root / "03_TOOLS" / "scripts" / "maintenance" / "maintenance_config.json"


def load_config(repo_root: Path) -> dict[str, Any]:
    with config_path(repo_root).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def threshold(repo_root: Path) -> int:
    return int(load_config(repo_root).get("prompt_threshold", 5))


def counter_path(project: Path) -> Path:
    return project / "memory" / "PROMPT_COUNTER.md"


def read_count(path: Path) -> int:
    if not path.exists():
        return 0
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"Prompt count:\s*`?(\d+)`?", text)
    if match:
        return int(match.group(1))
    match = re.search(r"\bcount\b\s*[:=]\s*(\d+)", text, re.I)
    return int(match.group(1)) if match else 0


def render(project: Path, count: int, reason: str, threshold_value: int) -> str:
    status = "MAINTENANCE_DUE" if count >= threshold_value else "ACTIVE_EVIDENCE"
    generated = datetime.now().isoformat(timespec="seconds")
    return "\n".join(
        [
            "# Prompt Counter",
            "",
            f"Status: `{status}`",
            "",
            f"Generated date/time: `{generated}`",
            "",
            f"Project: `{project.name}`",
            "",
            "Supersedes: prior prompt counter state",
            "",
            "Superseded by: `None`",
            "",
            "Evidence files: `00_CODEX_START/PROMPT_COUNTER_RULES.md`",
            "",
            "Current relevance: project-specific trigger for maintenance and live-state rebuilds.",
            "",
            f"Prompt count: `{count}`",
            "",
            f"Maintenance threshold: `{threshold_value}`",
            "",
            f"Maintenance due: `{'YES' if count >= threshold_value else 'NO'}`",
            "",
            f"Last increment reason: `{reason}`",
            "",
            "Maintenance command:",
            "",
            "```powershell",
            f"python 03_TOOLS\\scripts\\maintenance\\run_maintenance_cycle.py --project {project}",
            "```",
            "",
        ]
    )


def write_counter(project: Path, count: int, reason: str, repo_root: Path) -> Path:
    path = counter_path(project)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render(project, count, reason, threshold(repo_root)), encoding="utf-8", newline="\n")
    return path
