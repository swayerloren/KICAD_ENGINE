#!/usr/bin/env python3
"""Safety-gated Eeschema save helper, dry-run by default."""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from gui_workflow_common import detect_window_state, now_iso


def save_live(process_id: int) -> dict[str, object]:
    from pywinauto import Application, keyboard  # type: ignore

    app = Application(backend="uia").connect(process=process_id)
    window = app.top_window()
    window.set_focus()
    keyboard.send_keys("^s")
    time.sleep(2)
    title = app.top_window().window_text()
    return {"title_after_save": title, "unsaved_after_save": title.startswith("*")}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected-schematic", required=True)
    parser.add_argument("--live", action="store_true", help="Actually save from the KiCad GUI. Default is dry-run.")
    parser.add_argument("--execute", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--allow-save", action="store_true")
    parser.add_argument("--backup-path", default="")
    parser.add_argument("--backup-confirmed", action="store_true")
    parser.add_argument("--confirm-overwrite-disk", action="store_true")
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
        "manual_steps": [
            "Confirm the exact Eeschema path matches the intended schematic.",
            "Confirm a backup exists.",
            "Save from KiCad GUI.",
            "Run GUI ERC and post-save kicad-cli ERC.",
        ],
        "live_result": None,
        "did_edit_kicad_files": False,
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
        result["blockers"].append("Target Eeschema window is dirty with '*' and was not explicitly allowed for save.")

    if live:
        if not args.allow_save:
            result["blockers"].append("--allow-save is required for live GUI save.")
        if not (args.backup_confirmed or args.backup_path):
            result["blockers"].append("--backup-confirmed or --backup-path is required before GUI save.")
        if not args.confirm_overwrite_disk:
            result["blockers"].append("--confirm-overwrite-disk is required for live GUI save.")
        if not args.allow_gui_control:
            result["blockers"].append("--allow-gui-control is required for live GUI save.")

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

    live_result = save_live(process_id)
    result["live_result"] = live_result
    result["status"] = "GUI_SAVE_COMPLETED" if not live_result.get("unsaved_after_save") else "GUI_SAVE_SENT_BUT_STILL_DIRTY"
    result["did_edit_kicad_files"] = result["status"] == "GUI_SAVE_COMPLETED"
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "GUI_SAVE_COMPLETED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
