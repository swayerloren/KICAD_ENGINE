#!/usr/bin/env python
"""Ensure Eeschema is open for the target schematic, dry-run by default."""

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime
from pathlib import Path


def run_json(args: list[str]):
    completed = subprocess.run(args, text=True, capture_output=True, check=False)
    output = completed.stdout.strip()
    data = json.loads(output) if output else {}
    return completed.returncode, data, completed.stderr.strip()


def ps_detect(expected_schematic: Path):
    script = Path(__file__).with_name("detect_eeschema_window.ps1")
    completed = subprocess.run(
        ["powershell", "-NoProfile", "-Command", f"& '{script}' -ExpectedSchematicPath '{expected_schematic}' -Json"],
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or completed.stdout.strip())
    text = completed.stdout.strip()
    if not text:
        return []
    data = json.loads(text)
    return data if isinstance(data, list) else [data]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--schematic", required=True)
    parser.add_argument("--live", action="store_true", help="Open KiCad/project/schematic if needed. Default is DRY_RUN.")
    parser.add_argument("--python", default=None, help="Python executable for child scripts.")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    schematic = Path(args.schematic).resolve()
    python_exe = args.python or "python"
    result = {
        "checked_at": datetime.now().isoformat(timespec="seconds"),
        "mode": "LIVE" if args.live else "DRY_RUN",
        "project": str(project),
        "schematic": str(schematic),
        "status": "UNKNOWN",
        "blockers": [],
        "actions": [],
        "initial_eeschema_windows": [],
        "open_project_result": None,
        "open_schematic_result": None,
        "final_eeschema_windows": [],
        "did_edit_kicad_files": False,
    }

    if not project.exists() or project.suffix != ".kicad_pro":
        result["blockers"].append("Project path missing or not .kicad_pro.")
    if not schematic.exists() or schematic.suffix != ".kicad_sch":
        result["blockers"].append("Schematic path missing or not .kicad_sch.")

    if schematic.exists():
        windows = ps_detect(schematic)
        result["initial_eeschema_windows"] = windows
        if any(w.get("path_match") and not w.get("unsaved_gui_state") for w in windows):
            result["status"] = "EESCHEMA_READY_FOR_TARGET"
            print(json.dumps(result, indent=2))
            return 0
        if any(w.get("path_match") and w.get("unsaved_gui_state") for w in windows):
            result["status"] = "BLOCKED_UNSAVED_TARGET_EESCHEMA"
            result["blockers"].append("Target Eeschema is open but has unsaved '*' state.")
            print(json.dumps(result, indent=2))
            return 2
        if windows:
            result["status"] = "BLOCKED_DIFFERENT_EESCHEMA_OPEN"
            result["blockers"].append("An Eeschema window is open for a different project/schematic.")
            print(json.dumps(result, indent=2))
            return 2

    if result["blockers"]:
        result["status"] = "BLOCKED_PRECHECK_FAILED"
        print(json.dumps(result, indent=2))
        return 2

    if not args.live:
        result["status"] = "DRY_RUN_READY_TO_OPEN_PROJECT_AND_EESCHEMA"
        result["actions"].append("Would launch target .kicad_pro, then open/focus schematic editor, then verify path.")
        print(json.dumps(result, indent=2))
        return 0

    open_project = Path(__file__).with_name("open_kicad_project.py")
    code, data, err = run_json([python_exe, str(open_project), "--project", str(project), "--schematic", str(schematic), "--live"])
    result["open_project_result"] = data or {"stderr": err, "exit_code": code}
    if code != 0:
        result["status"] = "BLOCKED_OPEN_PROJECT_FAILED"
        print(json.dumps(result, indent=2))
        return 2

    open_schematic = Path(__file__).with_name("open_schematic_editor_gui.py")
    code, data, err = run_json([python_exe, str(open_schematic), "--project", str(project), "--schematic", str(schematic), "--live"])
    result["open_schematic_result"] = data or {"stderr": err, "exit_code": code}
    result["final_eeschema_windows"] = ps_detect(schematic)
    if code == 0 and any(w.get("path_match") and not w.get("unsaved_gui_state") for w in result["final_eeschema_windows"]):
        result["status"] = "EESCHEMA_READY_FOR_TARGET"
        print(json.dumps(result, indent=2))
        return 0
    result["status"] = "BLOCKED_EESCHEMA_NOT_READY"
    print(json.dumps(result, indent=2))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

