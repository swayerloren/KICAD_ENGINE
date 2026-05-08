#!/usr/bin/env python
"""Safety-gated GUI save helper for Eeschema."""

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


def save_live(process_id: int) -> dict:
    from pywinauto import Application, keyboard  # type: ignore

    app = Application(backend="uia").connect(process=process_id)
    win = app.top_window()
    win.set_focus()
    keyboard.send_keys("^s")
    time.sleep(2)
    title = app.top_window().window_text()
    return {"title_after_save": title, "unsaved_after_save": title.startswith("*")}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected-schematic", required=True)
    parser.add_argument("--execute", action="store_true", help="Actually send GUI save. Default is DRY_RUN.")
    parser.add_argument("--backup-path", default="")
    parser.add_argument("--backup-confirmed", action="store_true")
    parser.add_argument("--confirm-overwrite-disk", action="store_true")
    parser.add_argument("--allow-gui-control", action="store_true")
    args = parser.parse_args()

    windows = ps_json(Path(__file__).with_name("detect_eeschema_window.ps1"), args.expected_schematic)
    blockers = []
    if len(windows) != 1:
        blockers.append("Expected exactly one Eeschema window.")
    else:
        if not windows[0].get("path_match"):
            blockers.append("Open Eeschema path does not match expected schematic.")
    if args.execute:
        if not (args.backup_confirmed or args.backup_path):
            blockers.append("--backup-confirmed or --backup-path is required before any GUI save.")
        if not (args.confirm_overwrite_disk or args.backup_confirmed):
            blockers.append("--confirm-overwrite-disk is required unless --backup-confirmed is used.")
        if not args.allow_gui_control and not args.backup_confirmed:
            blockers.append("--allow-gui-control is required unless called from a backup-confirmed workflow.")

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
            "Confirm the GUI window path matches the intended schematic.",
            "Confirm a backup exists.",
            "Use File -> Save or Ctrl+S in KiCad.",
            "Re-run GUI and CLI ERC after saving.",
        ],
    }
    if not args.execute:
        print(json.dumps(result, indent=2))
        return 0 if not blockers else 2
    if blockers:
        result["status"] = "BLOCKED_PRECHECK_FAILED"
        print(json.dumps(result, indent=2))
        return 2
    live = save_live(int(windows[0]["process_id"]))
    result["live_result"] = live
    result["status"] = "GUI_SAVE_COMPLETED" if not live.get("unsaved_after_save") else "GUI_SAVE_SENT_BUT_STILL_DIRTY"
    result["did_edit_kicad_files"] = True
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "GUI_SAVE_COMPLETED" else 2


if __name__ == "__main__":
    raise SystemExit(main())

