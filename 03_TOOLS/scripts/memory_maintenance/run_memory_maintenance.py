#!/usr/bin/env python3
"""Compatibility wrapper plus compatibility helpers for the new maintenance cycle."""

from __future__ import annotations

import argparse
import subprocess
import sys
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = next((path for path in [SCRIPT_DIR, *SCRIPT_DIR.parents] if (path / "AGENTS.md").exists()), SCRIPT_DIR).resolve()
PROJECT_STATE_DIR = REPO_ROOT / "03_TOOLS" / "scripts" / "project_state"
if str(PROJECT_STATE_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_STATE_DIR))

from project_state_common import (  # type: ignore  # noqa: E402
    build_live_state_outputs,
    current_state_markdown,
    detect_stale_reports_data,
    reconcile_gate_data,
)


RELATIVE_DATE_TERMS = [
    "yesterday",
    "today",
    "tomorrow",
    "recently",
    "current",
    "latest",
    "last run",
    "previous run",
    "now",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def repo_rel(path: Path, root: Path) -> str:
    return str(path.resolve().relative_to(root.resolve())).replace("/", "\\")


def title_for(path: Path) -> str:
    try:
        for line in read_text(path).splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    except OSError:
        pass
    return path.stem.replace("_", " ").title()


def md_files(root: Path, *parts: str) -> list[Path]:
    base = root.joinpath(*parts)
    if not base.exists():
        return []
    return sorted(base.rglob("*.md"), key=lambda p: str(p).lower())


def detect_duplicate_history(root: Path, project: Path) -> dict[str, list[str]]:
    paths = md_files(root, "02_HISTORY") + md_files(project, "history")
    topic_words = [
        "no_pcb",
        "pcb_update",
        "pcb_sync",
        "routing",
        "placement",
        "jlcpcb",
        "not_final",
        "schematic_gate",
        "footprint",
    ]
    buckets: dict[str, list[str]] = defaultdict(list)
    for path in paths:
        name = path.stem.lower().replace("-", "_")
        text = read_text(path).lower()[:4000]
        for topic in topic_words:
            if topic in name or topic.replace("_", " ") in text:
                buckets[topic].append(repo_rel(path, root))
    return {topic: files for topic, files in buckets.items() if len(files) > 1}


def detect_relative_dates(root: Path, scan_dirs: list[Path]) -> list[dict[str, str]]:
    hits: list[dict[str, str]] = []
    term_re = re.compile(r"\b(" + "|".join(re.escape(term) for term in RELATIVE_DATE_TERMS) + r")\b", re.I)
    for base in scan_dirs:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md"), key=lambda p: str(p).lower()):
            text = read_text(path)
            for match in term_re.finditer(text):
                hits.append({"file": repo_rel(path, root), "term": match.group(1), "status": "DATE_UNRESOLVED_NEEDS_HUMAN_REVIEW"})
                break
    return hits


def current_project_state(root: Path, project: Path) -> dict[str, object]:
    live_state = build_live_state_outputs(project, root, write_supporting=False)
    stale = detect_stale_reports_data(project, root, live_state)
    reconciliation = reconcile_gate_data(project, root, live_state, stale)
    return {"live_state": live_state, "reconciliation": reconciliation}


def state_markdown(state: dict[str, object]) -> str:
    live_state = state["live_state"]  # type: ignore[index]
    reconciliation = state["reconciliation"]  # type: ignore[index]
    return current_state_markdown(live_state, reconciliation, REPO_ROOT)


def detect_stale_reports(root: Path, project: Path) -> list[dict[str, str]]:
    live_state = build_live_state_outputs(project, root, write_supporting=False)
    audit = detect_stale_reports_data(project, root, live_state)
    rows: list[dict[str, str]] = []
    for row in audit["stale_rows"]:
        rows.append(
            {
                "file": row["file"],
                "status": "STALE",
                "reason": "; ".join(row["reasons"]),
                "superseded_by": "reports/LIVE_PROJECT_STATE.json and reports/GATE_RECONCILIATION_REPORT.md",
            }
        )
    return rows


def list_markdown(title: str, status: str, rows: list[dict[str, str]], generated: str, project: str) -> str:
    lines = [
        f"# {title}",
        "",
        f"Status: `{status}`",
        "",
        f"Generated date/time: `{generated}`",
        "",
        f"Project: `{project}`",
        "",
    ]
    if not rows:
        lines.extend(["No records detected.", ""])
        return "\n".join(lines)
    keys = sorted({key for row in rows for key in row})
    lines.append("| " + " | ".join(keys) + " |")
    lines.append("|" + "|".join("---" for _ in keys) + "|")
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(key, "")).replace("|", "\\|") for key in keys) + " |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Compatibility wrapper for run_maintenance_cycle.py")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--project", required=True)
    parser.add_argument("--apply", action="store_true", help="Retained for compatibility. The new cycle applies by default.")
    parser.add_argument("--json-output", default="", help="Deprecated compatibility argument.")
    args = parser.parse_args()

    command = [
        sys.executable,
        str(REPO_ROOT / "03_TOOLS" / "scripts" / "maintenance" / "run_maintenance_cycle.py"),
        "--repo-root",
        str(Path(args.repo_root).resolve()),
        "--project",
        args.project,
    ]
    return subprocess.call(command)


if __name__ == "__main__":
    raise SystemExit(main())
