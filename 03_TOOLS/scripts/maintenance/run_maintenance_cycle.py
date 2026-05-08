#!/usr/bin/env python3
"""Run the live-state-aware maintenance cycle."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = next((path for path in [SCRIPT_DIR, *SCRIPT_DIR.parents] if (path / "AGENTS.md").exists()), SCRIPT_DIR).resolve()
PROJECT_STATE_DIR = REPO_ROOT / "03_TOOLS" / "scripts" / "project_state"
if str(PROJECT_STATE_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_STATE_DIR))

from project_state_common import (  # type: ignore  # noqa: E402
    build_live_state_outputs,
    detect_stale_reports_data,
    reconcile_gate_data,
    render_gate_reconciliation_markdown,
    render_live_project_state_markdown,
    render_stale_reports_markdown,
    repo_root_from,
    resolve_project_path,
    update_phase_status_outputs,
    write_gate_reconciliation_outputs,
    write_stale_reports_outputs,
)
from prompt_counter import counter_path, read_count, repo_root_from as prompt_repo_root_from, threshold, write_counter  # type: ignore  # noqa: E402


def run_script(script: Path, repo_root: Path) -> dict[str, object]:
    command = [sys.executable, str(script), "--repo-root", str(repo_root)]
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    return {
        "command": command,
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def maintenance_report(summary: dict[str, object]) -> str:
    lines = [
        "# Maintenance Cycle Report",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        f"Project: `{summary['project']}`",
        "",
        f"Prompt counter before: `{summary['prompt_counter_before']}`",
        f"Prompt counter after reset: `{summary['prompt_counter_after']}`",
        "",
        f"Live classification: `{summary['classification']}`",
        f"Stale report count: `{summary['stale_report_count']}`",
        "",
        "## Phase Snapshot",
        "",
        "| Phase | Result | Status |",
        "| --- | --- | --- |",
    ]
    for key in ("2", "3", "8"):
        phase = summary["phase_results"][key]
        lines.append(f"| `{key}` | `{phase['result']}` | `{phase['phase_status']}` |")
    lines.extend(["", "## Steps", ""])
    for step in summary["steps"]:
        lines.append(f"- `{step['name']}`: returncode `{step['returncode']}`")
    lines.extend(["", "## Next Action", "", summary["next_action"], ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the KiCad Engine maintenance cycle.")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--project", required=True)
    parser.add_argument("--dry-run", action="store_true", help="Build results in memory but do not write files.")
    args = parser.parse_args()

    repo_root = repo_root_from(args.repo_root)
    _ = prompt_repo_root_from(args.repo_root)
    project = resolve_project_path(repo_root, args.project)
    apply = not args.dry_run

    before = read_count(counter_path(project))

    live_state = build_live_state_outputs(project, repo_root, write_supporting=apply)
    stale_audit = detect_stale_reports_data(project, repo_root, live_state)
    reconciliation = reconcile_gate_data(project, repo_root, live_state, stale_audit)

    if apply:
        write_stale_reports_outputs(project, repo_root, stale_audit)
        write_gate_reconciliation_outputs(project, reconciliation)
        update_phase_status_outputs(project, repo_root, live_state, reconciliation)

    steps = [
        {"name": "build_live_project_state", "returncode": 0},
        {"name": "detect_stale_reports", "returncode": 0},
        {"name": "reconcile_project_gates", "returncode": 0},
        {"name": "update_phase_status_from_live_state", "returncode": 0},
    ]

    for script in [
        repo_root / "03_TOOLS" / "scripts" / "indexing" / "build_memory_index.py",
        repo_root / "03_TOOLS" / "scripts" / "indexing" / "build_history_index.py",
        repo_root / "03_TOOLS" / "scripts" / "ai_quality" / "build_ai_quality_index.py",
        repo_root / "03_TOOLS" / "scripts" / "ai_quality" / "build_current_known_problems.py",
    ]:
        result = run_script(script, repo_root)
        steps.append({"name": script.stem, "returncode": result["returncode"], "stdout": result["stdout"], "stderr": result["stderr"]})
        if result["returncode"] != 0:
            print(json.dumps({"error": f"{script.name} failed", "detail": result}, indent=2))
            return 1

    after = before
    if apply:
        write_counter(project, 0, "reset after successful maintenance cycle", repo_root)
        after = read_count(counter_path(project))

        report_path = project / "reports" / "MAINTENANCE_CYCLE_REPORT.md"
        report_json = project / "reports" / "MAINTENANCE_CYCLE_REPORT.json"
        summary = {
            "generated_at": live_state["generated_at"],
            "project": project.name,
            "prompt_counter_before": before,
            "prompt_counter_after": after,
            "classification": live_state["classification"],
            "stale_report_count": len(stale_audit["stale_rows"]),
            "phase_results": reconciliation["phase_results"],
            "next_action": live_state["next_action"],
            "steps": steps,
        }
        report_path.write_text(maintenance_report(summary), encoding="utf-8", newline="\n")
        report_json.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "mode": "DRY_RUN" if args.dry_run else "APPLY",
                "project": project.name,
                "prompt_counter_before": before,
                "prompt_counter_after": after,
                "classification": live_state["classification"],
                "stale_report_count": len(stale_audit["stale_rows"]),
                "phase_results": reconciliation["phase_results"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
