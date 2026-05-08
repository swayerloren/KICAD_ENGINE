#!/usr/bin/env python
"""Capture or dry-run a screenshot of the active KiCad/Eeschema window.

Default mode is dry-run. Use --capture to save a screenshot. This script never
clicks, types, saves, annotates, or edits KiCad files.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def powershell_json(command: str):
    completed = subprocess.run(
        ["powershell", "-NoProfile", "-Command", command],
        check=False,
        text=True,
        capture_output=True,
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or completed.stdout.strip())
    text = completed.stdout.strip()
    return json.loads(text) if text else None


def find_eeschema_windows(expected: str | None):
    script = Path(__file__).with_name("detect_eeschema_window.ps1")
    cmd = f"& '{script}' -Json"
    if expected:
        cmd += f" -ExpectedSchematicPath '{expected}'"
    data = powershell_json(cmd)
    if data is None:
        return []
    return data if isinstance(data, list) else [data]


def capture_window(process_id: int, output: Path) -> str:
    try:
        from pywinauto import Application  # type: ignore
    except Exception as exc:  # pragma: no cover - environment dependent
        raise RuntimeError(f"pywinauto is required for live screenshot capture: {exc}") from exc

    app = Application(backend="uia").connect(process=process_id)
    win = app.top_window()
    image = win.capture_as_image()
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output)
    return str(output)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected-schematic", default="")
    parser.add_argument("--output", default="")
    parser.add_argument("--capture", action="store_true", help="Actually capture screenshot. Default is dry-run.")
    args = parser.parse_args()

    windows = find_eeschema_windows(args.expected_schematic or None)
    result = {
        "checked_at": datetime.now().isoformat(timespec="seconds"),
        "mode": "CAPTURE" if args.capture else "DRY_RUN",
        "windows": windows,
        "screenshot_path": None,
        "status": "NO_EESCHEMA_WINDOW" if not windows else "DRY_RUN_ONLY",
    }

    if not args.capture:
        print(json.dumps(result, indent=2))
        return 0

    if len(windows) != 1:
        result["status"] = "BLOCKED_EXPECTED_EXACTLY_ONE_EESCHEMA_WINDOW"
        print(json.dumps(result, indent=2))
        return 2
    window = windows[0]
    if args.expected_schematic and not window.get("path_match"):
        result["status"] = "BLOCKED_PATH_MISMATCH"
        print(json.dumps(result, indent=2))
        return 2

    out = Path(args.output) if args.output else Path("33_KICAD_GUI_AUTOMATION/reports") / f"eeschema_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    result["screenshot_path"] = capture_window(int(window["process_id"]), out)
    result["status"] = "SCREENSHOT_CAPTURED"
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
