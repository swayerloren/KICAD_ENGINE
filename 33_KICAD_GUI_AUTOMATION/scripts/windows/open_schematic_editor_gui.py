#!/usr/bin/env python
"""Open/focus Eeschema from KiCad project manager, dry-run by default.

Live mode uses UI Automation only when a KiCad project-manager window for the
expected project is detectable. It never uses blind clicking, never opens PCB,
and never saves or edits files.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from datetime import datetime
from pathlib import Path


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


def click_schematic_button(window) -> str:
    candidates = []
    for control in window.descendants(depth=8):
        text = control.window_text() or ""
        cls = control.friendly_class_name()
        if "schematic" in text.lower() and cls in {"Button", "MenuItem", "Hyperlink", "ListItem"}:
            candidates.append(control)
    if not candidates:
        raise RuntimeError("Could not find a detectable 'Schematic' control in KiCad project manager.")
    if len(candidates) > 1:
        # Prefer explicit editor/open wording, otherwise stop to avoid wrong target.
        preferred = [c for c in candidates if "editor" in (c.window_text() or "").lower() or "open" in (c.window_text() or "").lower()]
        if len(preferred) == 1:
            candidates = preferred
        else:
            names = [c.window_text() for c in candidates]
            raise RuntimeError(f"Multiple schematic-like controls found; refusing to choose blindly: {names}")
    candidates[0].click_input()
    return candidates[0].window_text()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--schematic", required=True)
    parser.add_argument("--live", action="store_true", help="Actually click a detected schematic-editor control.")
    parser.add_argument("--wait-seconds", type=int, default=8)
    args = parser.parse_args()

    project = Path(args.project).resolve()
    schematic = Path(args.schematic).resolve()
    result = {
        "checked_at": datetime.now().isoformat(timespec="seconds"),
        "mode": "LIVE" if args.live else "DRY_RUN",
        "project": str(project),
        "schematic": str(schematic),
        "status": "UNKNOWN",
        "blockers": [],
        "actions": [],
        "eeschema_windows_before": [],
        "eeschema_windows_after": [],
        "did_click": False,
        "did_edit_kicad_files": False,
    }

    if not project.exists() or project.suffix != ".kicad_pro":
        result["blockers"].append("Target project is missing or not a .kicad_pro file.")
    if not schematic.exists() or schematic.suffix != ".kicad_sch":
        result["blockers"].append("Target schematic is missing or not a .kicad_sch file.")

    if schematic.exists():
        before = detect_eeschema(schematic)
        result["eeschema_windows_before"] = before
        if any(w.get("path_match") for w in before):
            result["status"] = "EESCHEMA_ALREADY_OPEN_FOR_TARGET"
            print(json.dumps(result, indent=2))
            return 0
        if before:
            result["blockers"].append("Eeschema is already open but not for the expected target; stop.")

    if not args.live:
        result["status"] = "DRY_RUN_READY_TO_OPEN_SCHEMATIC_EDITOR" if not result["blockers"] else "DRY_RUN_BLOCKED"
        result["actions"].append("Would find KiCad project-manager window and click a detectable schematic editor control if --live is provided.")
        print(json.dumps(result, indent=2))
        return 0 if not result["blockers"] else 2

    if result["blockers"]:
        result["status"] = "BLOCKED_PRECHECK_FAILED"
        print(json.dumps(result, indent=2))
        return 2

    windows = find_kicad_project_window(project.stem)
    if len(windows) != 1:
        result["status"] = "BLOCKED_PROJECT_MANAGER_WINDOW_NOT_UNAMBIGUOUS"
        result["blockers"].append(f"Expected one KiCad project manager window for {project.stem}, found {len(windows)}.")
        print(json.dumps(result, indent=2))
        return 2
    windows[0].set_focus()
    clicked_text = click_schematic_button(windows[0])
    result["did_click"] = True
    result["actions"].append(f"Clicked detected schematic control: {clicked_text!r}")
    time.sleep(max(1, args.wait_seconds))
    result["eeschema_windows_after"] = detect_eeschema(schematic)
    if any(w.get("path_match") for w in result["eeschema_windows_after"]):
        result["status"] = "EESCHEMA_OPENED_FOR_TARGET"
        print(json.dumps(result, indent=2))
        return 0
    result["status"] = "BLOCKED_EESCHEMA_NOT_CONFIRMED_AFTER_CLICK"
    result["blockers"].append("Schematic editor did not open with the expected schematic path.")
    print(json.dumps(result, indent=2))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

