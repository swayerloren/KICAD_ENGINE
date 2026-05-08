#!/usr/bin/env python
"""Safety-gated GUI ERC workflow helper."""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from datetime import datetime
from pathlib import Path


def ps_json(script: Path, expected: str):
    cmd = f"& '{script}' -Json -ExpectedSchematicPath '{expected}'"
    completed = subprocess.run(["powershell", "-NoProfile", "-Command", cmd], text=True, capture_output=True)
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or completed.stdout.strip())
    text = completed.stdout.strip()
    if not text:
        return []
    data = json.loads(text)
    return data if isinstance(data, list) else [data]


def click_button(root, name: str) -> bool:
    for control in root.descendants(depth=8):
        if control.window_text() == name and control.friendly_class_name() == "Button":
            control.click_input()
            return True
    return False


def run_live_erc(process_id: int) -> dict:
    from pywinauto import Application  # type: ignore

    app = Application(backend="uia").connect(process=process_id)
    win = app.top_window()
    win.set_focus()
    menu_errors = []
    for route in ("Inspect->Electrical Rules Checker...", "Inspect->Electrical Rules Checker"):
        try:
            win.menu_select(route)
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
    texts = [c.window_text() for c in dialog.descendants(depth=8) if c.window_text()]
    violations_zero = any("Violations (0)" in t for t in texts)
    click_button(dialog, "Close")
    return {"status": "GUI_ERC_RAN", "violations_zero": violations_zero, "observed_text": texts[:80]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected-schematic", required=True)
    parser.add_argument("--execute", action="store_true", help="Actually run GUI ERC. Default is DRY_RUN.")
    args = parser.parse_args()

    windows = ps_json(Path(__file__).with_name("detect_eeschema_window.ps1"), args.expected_schematic)
    blockers = []
    if len(windows) != 1:
        blockers.append("Expected exactly one Eeschema window.")
    else:
        if not windows[0].get("path_match"):
            blockers.append("Open Eeschema path does not match expected schematic.")
        if windows[0].get("unsaved_gui_state"):
            blockers.append("Eeschema title begins with '*'; save/resolve GUI state before GUI ERC.")
    result = {
        "checked_at": datetime.now().isoformat(timespec="seconds"),
        "mode": "LIVE" if args.execute else "DRY_RUN",
        "status": "DRY_RUN_READY" if not blockers else "DRY_RUN_BLOCKED",
        "expected_schematic": args.expected_schematic,
        "windows": windows,
        "blockers": blockers,
        "live_result": None,
        "did_edit_kicad_files": False,
        "manual_steps": [
            "Focus the matching Eeschema window.",
            "Run Inspect -> Electrical Rules Checker.",
            "Run ERC from the KiCad dialog.",
            "Capture a screenshot of the ERC result.",
        ],
        "note": "Use kicad-cli ERC for saved-file evidence, but GUI ERC is required when validating what LJ sees in an open modified GUI state.",
    }
    if not args.execute:
        print(json.dumps(result, indent=2))
        return 0 if not blockers else 2
    if blockers:
        result["status"] = "BLOCKED_PRECHECK_FAILED"
        print(json.dumps(result, indent=2))
        return 2
    live = run_live_erc(int(windows[0]["process_id"]))
    result["live_result"] = live
    result["status"] = "GUI_ERC_ZERO_VIOLATIONS" if live.get("violations_zero") else live.get("status", "UNKNOWN")
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "GUI_ERC_ZERO_VIOLATIONS" else 2


if __name__ == "__main__":
    raise SystemExit(main())

