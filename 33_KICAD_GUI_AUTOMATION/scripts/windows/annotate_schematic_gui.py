#!/usr/bin/env python
"""Safety-gated wrapper for KiCad native schematic annotation.

Default mode is DRY_RUN. Live annotation requires explicit execution flags,
exact Eeschema path match, clean title, backup confirmation, and detectable UI
controls. This script does not edit .kicad_sch as text, does not touch PCB, and
does not generate manufacturing outputs.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from datetime import datetime
from pathlib import Path


MANUAL_STEPS = [
    "Focus the Eeschema window for the active schematic.",
    "If the window title starts with *, decide whether to keep or discard the unsaved GUI state.",
    "Create/confirm a backup before saving over disk.",
    "Run Tools -> Annotate Schematic...",
    "Choose Re-annotate all symbols.",
    "Confirm annotation.",
    "Save the schematic.",
    "Run ERC in KiCad.",
    "Confirm the GUI no longer shows question-mark references.",
]


def ps_json(script: Path, expected: str):
    cmd = f"& '{script}' -Json"
    if expected:
        cmd += f" -ExpectedSchematicPath '{expected}'"
    completed = subprocess.run(["powershell", "-NoProfile", "-Command", cmd], text=True, capture_output=True)
    if completed.returncode != 0:
        return {"error": completed.stderr.strip() or completed.stdout.strip()}
    text = completed.stdout.strip()
    if not text:
        return []
    return json.loads(text)


def normalize_windows(data):
    if isinstance(data, dict):
        return [data] if "process_id" in data else []
    return data or []


def click_named_button(root, name: str) -> bool:
    for control in root.descendants(depth=8):
        if control.window_text() == name and control.friendly_class_name() == "Button":
            control.click_input()
            return True
    return False


def click_radio(root, text: str) -> bool:
    for control in root.descendants(depth=8):
        if control.window_text() == text and control.friendly_class_name() in {"RadioButton", "CheckBox"}:
            control.click_input()
            return True
    return False


def run_live_annotation(process_id: int) -> dict:
    from pywinauto import Application  # type: ignore

    app = Application(backend="uia").connect(process=process_id)
    win = app.top_window()
    win.set_focus()
    opened = False
    menu_errors = []
    for route in ("Tools->Annotate Schematic...", "Tools->Annotate Schematic"):
        try:
            win.menu_select(route)
            opened = True
            break
        except Exception as exc:
            menu_errors.append(f"{route}: {exc!r}")
    time.sleep(1)
    dialog = None
    for candidate in app.windows():
        if "Annotate Schematic" in (candidate.window_text() or ""):
            dialog = candidate
            break
    if dialog is None:
        return {"status": "ANNOTATION_DIALOG_NOT_FOUND", "opened_menu": opened, "menu_errors": menu_errors}

    options = {
        "entire_schematic": click_radio(dialog, "Entire schematic"),
        "reset_existing_annotations": click_radio(dialog, "Reset existing annotations"),
        "sort_by_x": click_radio(dialog, "Sort symbols by X position"),
        "use_first_free": click_radio(dialog, "Use first free number after:"),
    }
    if not click_named_button(dialog, "Annotate"):
        return {"status": "ANNOTATE_BUTTON_NOT_FOUND", "dialog_found": True, "options": options}
    time.sleep(1)
    # Keep the dialog open/closed status nonfatal; close if possible.
    closed = click_named_button(dialog, "Close")
    return {"status": "ANNOTATION_APPLIED", "dialog_found": True, "options": options, "closed_dialog": closed}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected-schematic", required=True)
    parser.add_argument("--execute", action="store_true", help="Run live GUI annotation. Default is DRY_RUN.")
    parser.add_argument("--backup-confirmed", action="store_true")
    parser.add_argument("--allow-gui-control", action="store_true")
    parser.add_argument("--confirm-native-annotation-risk", action="store_true")
    args = parser.parse_args()

    script = Path(__file__).with_name("detect_eeschema_window.ps1")
    windows = normalize_windows(ps_json(script, args.expected_schematic))

    blockers = []
    if len(windows) != 1:
        blockers.append("Expected exactly one Eeschema window.")
    else:
        w = windows[0]
        if not w.get("path_match"):
            blockers.append("Open Eeschema path does not match expected schematic.")
        if w.get("unsaved_gui_state"):
            blockers.append("Eeschema title begins with '*': unsaved GUI state requires human decision before automation.")
    if args.execute:
        if not args.backup_confirmed:
            blockers.append("--backup-confirmed is required.")
        if not args.allow_gui_control:
            blockers.append("--allow-gui-control is required.")
        if not args.confirm_native_annotation_risk:
            blockers.append("--confirm-native-annotation-risk is required.")

    result = {
        "checked_at": datetime.now().isoformat(timespec="seconds"),
        "mode": "LIVE" if args.execute else "DRY_RUN",
        "status": "DRY_RUN_READY" if not blockers else "DRY_RUN_BLOCKED",
        "windows": windows,
        "blockers": blockers,
        "manual_steps": MANUAL_STEPS,
        "live_result": None,
        "did_edit_kicad_files": False,
        "did_modify_pcb": False,
    }
    if not args.execute:
        print(json.dumps(result, indent=2))
        return 0 if not blockers else 2
    if blockers:
        result["status"] = "BLOCKED_PRECHECK_FAILED"
        print(json.dumps(result, indent=2))
        return 2
    live = run_live_annotation(int(windows[0]["process_id"]))
    result["live_result"] = live
    result["status"] = live.get("status", "UNKNOWN")
    result["did_edit_kicad_files"] = result["status"] == "ANNOTATION_APPLIED"
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "ANNOTATION_APPLIED" else 2


if __name__ == "__main__":
    raise SystemExit(main())

