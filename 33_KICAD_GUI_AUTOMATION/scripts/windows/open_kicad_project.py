#!/usr/bin/env python3
"""Open the exact KiCad project manager window, dry-run by default."""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from pathlib import Path

from gui_workflow_common import DEFAULT_GUI_PYTHON, detect_window_state, now_iso


DEFAULT_KICAD = Path(r"C:\Program Files\KiCad\9.0\bin\kicad.exe")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True, help="Exact target .kicad_pro path.")
    parser.add_argument("--schematic", required=True, help="Exact target .kicad_sch path.")
    parser.add_argument("--kicad-exe", default=str(DEFAULT_KICAD))
    parser.add_argument("--live", action="store_true", help="Actually launch KiCad. Default is dry-run.")
    parser.add_argument("--wait-seconds", type=int, default=8)
    args = parser.parse_args()

    project = Path(args.project).resolve()
    schematic = Path(args.schematic).resolve()
    kicad_exe = Path(args.kicad_exe)
    window_state = detect_window_state(schematic) if schematic.exists() else {"state": "MISSING_SCHEMATIC", "windows": []}

    result = {
        "checked_at": now_iso(),
        "mode": "LIVE" if args.live else "DRY_RUN",
        "project": str(project),
        "schematic": str(schematic),
        "kicad_exe": str(kicad_exe),
        "window_state": window_state.get("state"),
        "windows": window_state.get("windows", []),
        "status": "UNKNOWN",
        "blockers": [],
        "actions": [],
        "did_launch": False,
        "did_edit_kicad_files": False,
    }

    if not project.exists() or project.suffix != ".kicad_pro":
        result["blockers"].append("Target project is missing or is not a .kicad_pro file.")
    if not schematic.exists() or schematic.suffix != ".kicad_sch":
        result["blockers"].append("Target schematic is missing or is not a .kicad_sch file.")
    if not kicad_exe.exists():
        result["blockers"].append("KiCad executable was not found at the requested path.")

    state = str(window_state.get("state"))
    if state == "PATH_MISMATCH":
        result["blockers"].append("An Eeschema window is already open for a different project; stop.")
    elif state == "MULTIPLE_EESCHEMA_WINDOWS":
        result["blockers"].append("Multiple Eeschema windows are open; target is ambiguous.")
    elif state == "UNSAVED_GUI_STATE":
        result["blockers"].append("Target Eeschema window is already open but has unsaved '*' state.")

    if state == "PATH_MATCH_CLEAN_TITLE":
        result["status"] = "TARGET_EESCHEMA_ALREADY_OPEN"
        result["actions"].append("Did not launch KiCad because the exact target schematic is already open and clean.")
        print(json.dumps(result, indent=2))
        return 0

    if not args.live:
        result["status"] = "DRY_RUN_READY_TO_OPEN_PROJECT" if not result["blockers"] else "DRY_RUN_BLOCKED"
        result["actions"].append("Would launch the exact target .kicad_pro in KiCad project manager if --live is provided.")
        print(json.dumps(result, indent=2))
        return 0 if not result["blockers"] else 2

    if result["blockers"]:
        result["status"] = "BLOCKED_PRECHECK_FAILED"
        print(json.dumps(result, indent=2))
        return 2

    subprocess.Popen([str(kicad_exe), str(project)], cwd=str(project.parent))
    result["did_launch"] = True
    result["actions"].append("Launched the exact target KiCad project manager window.")
    time.sleep(max(1, args.wait_seconds))
    result["status"] = "KICAD_PROJECT_LAUNCHED_VERIFY_SCHEMATIC_EDITOR_NEXT"
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
