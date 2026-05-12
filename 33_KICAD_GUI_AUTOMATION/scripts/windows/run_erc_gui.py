#!/usr/bin/env python3
"""Safety-gated KiCad GUI ERC helper, dry-run by default."""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from gui_workflow_common import detect_window_state, now_iso


def click_button(root, name: str) -> bool:
    for control in root.descendants(depth=8):
        if control.window_text() == name and control.friendly_class_name() == "Button":
            control.click_input()
            return True
    return False


def run_live_erc(process_id: int) -> dict[str, object]:
    from pywinauto import Application  # type: ignore

    app = Application(backend="uia").connect(process=process_id)
    window = app.top_window()
    window.set_focus()
    menu_errors: list[str] = []
    for route in ("Inspect->Electrical Rules Checker...", "Inspect->Electrical Rules Checker"):
        try:
            window.menu_select(route)
            break
        except Exception as exc:
            menu_errors.append(f"{route}: {exc!r}")
    time.sleep(1)
    dialog = None
    for candidate in app.windows():
        if "Electrical Rules Checker" in (candidate.window_text() or ""):
            dialog = candidate
            break
    if dialog is None:
        return {"status": "ERC_DIALOG_NOT_FOUND", "menu_errors": menu_errors}
    if not click_button(dialog, "Run ERC"):
        return {"status": "RUN_ERC_BUTTON_NOT_FOUND", "dialog_found": True}
    time.sleep(2)
    texts = [control.window_text() for control in dialog.descendants(depth=8) if control.window_text()]
    violations_zero = any("Violations (0)" in text for text in texts)
    click_button(dialog, "Close")
    return {"status": "GUI_ERC_RAN", "violations_zero": violations_zero, "observed_text": texts[:80]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected-schematic", required=True)
    parser.add_argument("--live", action="store_true", help="Actually run KiCad GUI ERC. Default is dry-run.")
    parser.add_argument("--execute", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--allow-gui-erc", action="store_true")
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
            "Focus the exact matching Eeschema window.",
            "Open Inspect -> Electrical Rules Checker.",
            "Run ERC from the KiCad dialog.",
            "Capture the GUI ERC result.",
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
    elif state == "UNSAVED_GUI_STATE":
        result["blockers"].append("Target Eeschema window is dirty with '*' and should be saved before GUI ERC.")

    if live and not args.allow_gui_erc:
        result["blockers"].append("--allow-gui-erc is required for live GUI ERC.")

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

    live_result = run_live_erc(process_id)
    result["live_result"] = live_result
    result["status"] = "GUI_ERC_ZERO_VIOLATIONS" if live_result.get("violations_zero") else str(live_result.get("status", "UNKNOWN"))
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "GUI_ERC_ZERO_VIOLATIONS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
