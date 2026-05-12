#!/usr/bin/env python3
"""Ensure Eeschema is open for the exact target schematic, dry-run by default."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from gui_workflow_common import default_python, detect_window_state, now_iso, run_json_command


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--schematic", required=True)
    parser.add_argument("--live", action="store_true", help="Actually open KiCad/project/schematic if needed. Default is dry-run.")
    parser.add_argument("--allow-unsaved-existing", action="store_true", help="Allow a matching target Eeschema window that is already dirty with '*'.")
    parser.add_argument("--python", default=default_python(), help="Python executable for child GUI scripts.")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    schematic = Path(args.schematic).resolve()
    window_state = detect_window_state(schematic) if schematic.exists() else {"state": "MISSING_SCHEMATIC", "windows": []}

    result = {
        "checked_at": now_iso(),
        "mode": "LIVE" if args.live else "DRY_RUN",
        "project": str(project),
        "schematic": str(schematic),
        "python": args.python,
        "window_state": window_state.get("state"),
        "windows": window_state.get("windows", []),
        "status": "UNKNOWN",
        "blockers": [],
        "actions": [],
        "open_project_result": None,
        "open_schematic_result": None,
        "final_window_state": None,
        "final_windows": [],
        "did_edit_kicad_files": False,
    }

    if not project.exists() or project.suffix != ".kicad_pro":
        result["blockers"].append("Project path is missing or is not a .kicad_pro file.")
    if not schematic.exists() or schematic.suffix != ".kicad_sch":
        result["blockers"].append("Schematic path is missing or is not a .kicad_sch file.")

    state = str(window_state.get("state"))
    if state == "PATH_MATCH_CLEAN_TITLE":
        result["status"] = "EESCHEMA_READY_FOR_TARGET"
        result["actions"].append("Exact target Eeschema window is already open and clean.")
        print(json.dumps(result, indent=2))
        return 0
    if state == "UNSAVED_GUI_STATE":
        if args.allow_unsaved_existing:
            result["status"] = "EESCHEMA_READY_FOR_TARGET_UNSAVED_ALLOWED"
            result["actions"].append("Exact target Eeschema window is already open with '*' and was explicitly allowed.")
            print(json.dumps(result, indent=2))
            return 0
        result["blockers"].append("Exact target Eeschema window is open but has unsaved '*' state.")
    elif state == "PATH_MISMATCH":
        result["blockers"].append("An Eeschema window is open for a different project; stop.")
    elif state == "MULTIPLE_EESCHEMA_WINDOWS":
        result["blockers"].append("Multiple Eeschema windows are open; target is ambiguous.")

    if not args.live:
        result["status"] = "DRY_RUN_READY_TO_OPEN_PROJECT_AND_EESCHEMA" if not result["blockers"] else "DRY_RUN_BLOCKED"
        result["actions"].append("Would launch the exact .kicad_pro, then open or focus the schematic editor, then verify the exact .kicad_sch path.")
        print(json.dumps(result, indent=2))
        return 0 if not result["blockers"] else 2

    if result["blockers"]:
        result["status"] = "BLOCKED_PRECHECK_FAILED"
        print(json.dumps(result, indent=2))
        return 2

    open_project = Path(__file__).with_name("open_kicad_project.py")
    code, data, stdout, stderr = run_json_command(
        [args.python, str(open_project), "--project", str(project), "--schematic", str(schematic), "--live"]
    )
    result["open_project_result"] = data or {"stdout": stdout, "stderr": stderr, "exit_code": code}
    if code != 0:
        result["status"] = "BLOCKED_OPEN_PROJECT_FAILED"
        print(json.dumps(result, indent=2))
        return 2

    open_schematic = Path(__file__).with_name("open_schematic_editor_gui.py")
    code, data, stdout, stderr = run_json_command(
        [args.python, str(open_schematic), "--project", str(project), "--schematic", str(schematic), "--live"]
    )
    result["open_schematic_result"] = data or {"stdout": stdout, "stderr": stderr, "exit_code": code}
    final_state = detect_window_state(schematic)
    result["final_window_state"] = final_state.get("state")
    result["final_windows"] = final_state.get("windows", [])
    if code == 0 and final_state.get("state") == "PATH_MATCH_CLEAN_TITLE":
        result["status"] = "EESCHEMA_READY_FOR_TARGET"
        print(json.dumps(result, indent=2))
        return 0
    result["status"] = "BLOCKED_EESCHEMA_NOT_READY"
    if final_state.get("state") == "UNSAVED_GUI_STATE" and args.allow_unsaved_existing:
        result["status"] = "EESCHEMA_READY_FOR_TARGET_UNSAVED_ALLOWED"
        print(json.dumps(result, indent=2))
        return 0
    print(json.dumps(result, indent=2))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
