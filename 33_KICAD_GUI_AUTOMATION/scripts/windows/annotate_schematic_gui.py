#!/usr/bin/env python3
"""Safety-gated KiCad native schematic annotation helper."""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from gui_workflow_common import detect_window_state, now_iso


MANUAL_STEPS = [
    "Focus the exact Eeschema window for the active schematic.",
    "Run Tools -> Annotate Schematic...",
    "Choose Re-annotate all symbols.",
    "Confirm the annotation dialog.",
    "Save from KiCad GUI through the approved save gate.",
    "Run GUI ERC when safely automatable.",
    "Confirm the GUI no longer shows question-mark references.",
]


def click_named_button(root, name: str) -> bool:
    for control in root.descendants(depth=8):
        if control.window_text() == name and control.friendly_class_name() == "Button":
            control.click_input()
            return True
    return False


def click_named_option(root, text: str) -> bool:
    for control in root.descendants(depth=8):
        if control.window_text() == text and control.friendly_class_name() in {"RadioButton", "CheckBox"}:
            control.click_input()
            return True
    return False


def run_live_annotation(process_id: int) -> dict[str, object]:
    from pywinauto import Application  # type: ignore

    app = Application(backend="uia").connect(process=process_id)
    window = app.top_window()
    window.set_focus()
    menu_errors: list[str] = []
    opened = False
    for route in ("Tools->Annotate Schematic...", "Tools->Annotate Schematic"):
        try:
            window.menu_select(route)
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
        "entire_schematic": click_named_option(dialog, "Entire schematic"),
        "reset_existing_annotations": click_named_option(dialog, "Reset existing annotations"),
        "sort_by_x": click_named_option(dialog, "Sort symbols by X position"),
    }
    if not click_named_button(dialog, "Annotate"):
        return {"status": "ANNOTATE_BUTTON_NOT_FOUND", "dialog_found": True, "options": options}
    time.sleep(1)
    click_named_button(dialog, "Close")
    return {"status": "ANNOTATION_APPLIED", "dialog_found": True, "options": options}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected-schematic", required=True)
    parser.add_argument("--live", action="store_true", help="Run live GUI annotation. Default is dry-run.")
    parser.add_argument("--execute", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--allow-annotation", action="store_true")
    parser.add_argument("--backup-confirmed", action="store_true")
    parser.add_argument("--backup-path", default="")
    parser.add_argument("--allow-gui-control", action="store_true")
    parser.add_argument("--allow-unsaved-existing", action="store_true")
    args = parser.parse_args()

    live = args.live or args.execute
    schematic = Path(args.expected_schematic).resolve()
    window_state = detect_window_state(schematic) if schematic.exists() else {"state": "MISSING_SCHEMATIC", "windows": []}

    result = {
        "checked_at": now_iso(),
        "mode": "LIVE" if live else "DRY_RUN",
        "expected_schematic": str(schematic),
        "window_state": window_state.get("state"),
        "windows": window_state.get("windows", []),
        "status": "UNKNOWN",
        "blockers": [],
        "manual_steps": MANUAL_STEPS,
        "live_result": None,
        "did_edit_kicad_files": False,
        "did_modify_pcb": False,
    }

    if not schematic.exists() or schematic.suffix != ".kicad_sch":
        result["blockers"].append("Expected schematic path is missing or is not a .kicad_sch file.")

    state = str(window_state.get("state"))
    if state == "NO_EESCHEMA_WINDOW":
        result["blockers"].append("No Eeschema window is open for the target schematic.")
    elif state == "PATH_MISMATCH":
        result["blockers"].append("The open Eeschema window does not match the expected schematic.")
    elif state == "MULTIPLE_EESCHEMA_WINDOWS":
        result["blockers"].append("Multiple Eeschema windows are open; target is ambiguous.")
    elif state == "UNSAVED_GUI_STATE" and not args.allow_unsaved_existing:
        result["blockers"].append("Target Eeschema window is dirty with '*' and was not explicitly allowed.")

    if live:
        if not args.allow_annotation:
            result["blockers"].append("--allow-annotation is required for live native annotation.")
        if not args.allow_gui_control:
            result["blockers"].append("--allow-gui-control is required for live GUI annotation.")
        if not (args.backup_confirmed or args.backup_path):
            result["blockers"].append("--backup-confirmed or --backup-path is required for live native annotation.")

    result["status"] = "DRY_RUN_READY" if not result["blockers"] else "DRY_RUN_BLOCKED"
    if not live:
        print(json.dumps(result, indent=2))
        return 0 if not result["blockers"] else 2
    if result["blockers"]:
        result["status"] = "BLOCKED_PRECHECK_FAILED"
        print(json.dumps(result, indent=2))
        return 2

    matching_window = window_state.get("matching_window")
    process_id = int(matching_window["process_id"]) if isinstance(matching_window, dict) and "process_id" in matching_window else None
    if process_id is None:
        result["status"] = "BLOCKED_PROCESS_ID_NOT_FOUND"
        result["blockers"].append("Matching Eeschema process_id was not available.")
        print(json.dumps(result, indent=2))
        return 2

    live_result = run_live_annotation(process_id)
    result["live_result"] = live_result
    result["status"] = str(live_result.get("status", "UNKNOWN"))
    result["did_edit_kicad_files"] = result["status"] == "ANNOTATION_APPLIED"
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "ANNOTATION_APPLIED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
