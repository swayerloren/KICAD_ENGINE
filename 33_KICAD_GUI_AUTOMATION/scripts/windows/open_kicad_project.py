#!/usr/bin/env python
"""Open a KiCad project safely, dry-run by default.

Live mode launches the exact .kicad_pro only when no conflicting Eeschema
window is already open. It does not open the schematic editor, click controls,
save files, annotate, run ERC, edit PCB, or generate outputs.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from datetime import datetime
from pathlib import Path


DEFAULT_KICAD = Path(r"C:\Program Files\KiCad\9.0\bin\kicad.exe")


def norm(path: str | Path) -> str:
    return str(Path(path).resolve()).casefold()


def ps_json(command: str):
    completed = subprocess.run(
        ["powershell", "-NoProfile", "-Command", command],
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or completed.stdout.strip())
    text = completed.stdout.strip()
    return json.loads(text) if text else None


def detect_eeschema(expected_schematic: Path):
    script = Path(__file__).with_name("detect_eeschema_window.ps1")
    data = ps_json(f"& '{script}' -ExpectedSchematicPath '{expected_schematic}' -Json")
    if data is None:
        return []
    return data if isinstance(data, list) else [data]


def detect_kicad_processes():
    command = (
        "Get-CimInstance Win32_Process | "
        "Where-Object { $_.Name -in @('kicad.exe','eeschema.exe') } | "
        "Select-Object ProcessId,Name,CommandLine | ConvertTo-Json -Depth 4"
    )
    data = ps_json(command)
    if data is None:
        return []
    return data if isinstance(data, list) else [data]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True, help="Absolute or repo-relative .kicad_pro path.")
    parser.add_argument("--schematic", required=True, help="Absolute or repo-relative .kicad_sch path.")
    parser.add_argument("--kicad-exe", default=str(DEFAULT_KICAD))
    parser.add_argument("--live", action="store_true", help="Actually launch KiCad. Default is DRY_RUN.")
    parser.add_argument("--wait-seconds", type=int, default=8)
    args = parser.parse_args()

    project = Path(args.project).resolve()
    schematic = Path(args.schematic).resolve()
    kicad_exe = Path(args.kicad_exe)
    result = {
        "checked_at": datetime.now().isoformat(timespec="seconds"),
        "mode": "LIVE" if args.live else "DRY_RUN",
        "project": str(project),
        "schematic": str(schematic),
        "kicad_exe": str(kicad_exe),
        "status": "UNKNOWN",
        "blockers": [],
        "actions": [],
        "eeschema_windows_before": [],
        "processes_after": [],
        "did_launch": False,
        "did_edit_kicad_files": False,
    }

    if project.suffix != ".kicad_pro" or not project.exists():
        result["blockers"].append("Target project path is missing or is not a .kicad_pro file.")
    if schematic.suffix != ".kicad_sch" or not schematic.exists():
        result["blockers"].append("Target schematic path is missing or is not a .kicad_sch file.")
    if not kicad_exe.exists():
        result["blockers"].append("KiCad executable was not found.")

    windows = detect_eeschema(schematic) if schematic.exists() else []
    result["eeschema_windows_before"] = windows
    for win in windows:
        if win.get("open_schematic_path") and not win.get("path_match"):
            result["blockers"].append("Existing Eeschema window is open for a different schematic; stop.")
        if win.get("unsaved_gui_state"):
            result["blockers"].append("Existing Eeschema window has unsaved '*' state; stop unless explicitly handled by a higher-level workflow.")

    if len(windows) > 1:
        result["blockers"].append("More than one Eeschema window is open; target is ambiguous.")

    target_already_open = len(windows) == 1 and windows[0].get("path_match") and not windows[0].get("unsaved_gui_state")

    if not args.live:
        if target_already_open:
            result["status"] = "DRY_RUN_TARGET_EESCHEMA_ALREADY_OPEN"
            result["actions"].append("Would not launch a duplicate project; target Eeschema is already open and clean.")
        else:
            result["status"] = "DRY_RUN_READY_TO_OPEN_PROJECT" if not result["blockers"] else "DRY_RUN_BLOCKED"
            result["actions"].append("Would launch exact KiCad project with kicad.exe if --live is provided.")
        print(json.dumps(result, indent=2))
        return 0 if not result["blockers"] else 2

    if result["blockers"]:
        result["status"] = "BLOCKED_PRECHECK_FAILED"
        print(json.dumps(result, indent=2))
        return 2

    if target_already_open:
        result["status"] = "TARGET_EESCHEMA_ALREADY_OPEN_NO_LAUNCH_NEEDED"
        result["actions"].append("Did not launch a duplicate project; target Eeschema is already open and clean.")
        print(json.dumps(result, indent=2))
        return 0

    subprocess.Popen([str(kicad_exe), str(project)], cwd=str(project.parent))
    result["did_launch"] = True
    result["actions"].append("Launched KiCad project manager for exact target project.")
    time.sleep(max(1, args.wait_seconds))
    result["processes_after"] = detect_kicad_processes()
    result["status"] = "KICAD_PROJECT_LAUNCHED_VERIFY_WINDOW_STATE_NEXT"
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
