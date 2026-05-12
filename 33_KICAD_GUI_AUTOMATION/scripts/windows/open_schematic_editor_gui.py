#!/usr/bin/env python3
"""Open or focus Eeschema from the KiCad project manager, dry-run by default."""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from gui_workflow_common import detect_window_state, now_iso


def find_kicad_project_window(project_stem: str):
    try:
        from pywinauto import Desktop  # type: ignore
    except Exception as exc:
        raise RuntimeError(f"pywinauto is required for live GUI navigation: {exc}") from exc
    matches = []
    for win in Desktop(backend="uia").windows():
        title = win.window_text() or ""
        if project_stem.lower() in title.lower() and "KiCad" in title:
            matches.append(win)
    return matches


def click_schematic_control(window) -> str:
    candidates = []
    for control in window.descendants(depth=8):
        text = control.window_text() or ""
        control_class = control.friendly_class_name()
        if "schematic" in text.lower() and control_class in {"Button", "MenuItem", "Hyperlink", "ListItem"}:
            candidates.append(control)
    if not candidates:
        raise RuntimeError("Could not find a detectable schematic-editor control in KiCad project manager.")
    preferred = [control for control in candidates if "open" in (control.window_text() or "").lower() or "editor" in (control.window_text() or "").lower()]
    if len(preferred) == 1:
        candidates = preferred
    if len(candidates) != 1:
        names = [control.window_text() for control in candidates]
        raise RuntimeError(f"Multiple schematic-like controls were found; refusing to choose blindly: {names}")
    candidates[0].click_input()
    return candidates[0].window_text()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--schematic", required=True)
    parser.add_argument("--live", action="store_true", help="Actually click the schematic-editor control. Default is dry-run.")
    parser.add_argument("--wait-seconds", type=int, default=8)
    args = parser.parse_args()

    project = Path(args.project).resolve()
    schematic = Path(args.schematic).resolve()
    window_state = detect_window_state(schematic) if schematic.exists() else {"state": "MISSING_SCHEMATIC", "windows": []}

    result = {
        "checked_at": now_iso(),
        "mode": "LIVE" if args.live else "DRY_RUN",
        "project": str(project),
        "schematic": str(schematic),
        "window_state": window_state.get("state"),
        "windows": window_state.get("windows", []),
        "status": "UNKNOWN",
        "blockers": [],
        "actions": [],
        "did_click": False,
        "did_edit_kicad_files": False,
    }

    if not project.exists() or project.suffix != ".kicad_pro":
        result["blockers"].append("Target project is missing or is not a .kicad_pro file.")
    if not schematic.exists() or schematic.suffix != ".kicad_sch":
        result["blockers"].append("Target schematic is missing or is not a .kicad_sch file.")

    state = str(window_state.get("state"))
    if state == "PATH_MATCH_CLEAN_TITLE":
        result["status"] = "EESCHEMA_ALREADY_OPEN_FOR_TARGET"
        result["actions"].append("Did not click any GUI control because the exact target schematic is already open.")
        print(json.dumps(result, indent=2))
        return 0
    if state == "PATH_MISMATCH":
        result["blockers"].append("A different-project Eeschema window is already open; stop.")
    elif state == "MULTIPLE_EESCHEMA_WINDOWS":
        result["blockers"].append("Multiple Eeschema windows are open; target is ambiguous.")
    elif state == "UNSAVED_GUI_STATE":
        result["blockers"].append("Target Eeschema window is open with unsaved '*' state; stop unless a higher-level workflow explicitly allows it.")

    if not args.live:
        result["status"] = "DRY_RUN_READY_TO_OPEN_SCHEMATIC_EDITOR" if not result["blockers"] else "DRY_RUN_BLOCKED"
        result["actions"].append("Would find the exact KiCad project-manager window and click the detectable schematic-editor control if --live is provided.")
        print(json.dumps(result, indent=2))
        return 0 if not result["blockers"] else 2

    if result["blockers"]:
        result["status"] = "BLOCKED_PRECHECK_FAILED"
        print(json.dumps(result, indent=2))
        return 2

    windows = find_kicad_project_window(project.stem)
    if len(windows) != 1:
        result["status"] = "BLOCKED_PROJECT_MANAGER_WINDOW_NOT_UNAMBIGUOUS"
        result["blockers"].append(f"Expected one KiCad project-manager window for {project.stem}, found {len(windows)}.")
        print(json.dumps(result, indent=2))
        return 2

    windows[0].set_focus()
    clicked = click_schematic_control(windows[0])
    result["did_click"] = True
    result["actions"].append(f"Clicked schematic control: {clicked!r}")
    time.sleep(max(1, args.wait_seconds))
    after_state = detect_window_state(schematic)
    result["window_state_after"] = after_state.get("state")
    result["windows_after"] = after_state.get("windows", [])
    if after_state.get("state") == "PATH_MATCH_CLEAN_TITLE":
        result["status"] = "EESCHEMA_OPENED_FOR_TARGET"
        print(json.dumps(result, indent=2))
        return 0
    result["status"] = "BLOCKED_EESCHEMA_NOT_CONFIRMED_AFTER_CLICK"
    result["blockers"].append("Schematic editor did not reopen on the exact expected target schematic.")
    print(json.dumps(result, indent=2))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
