"""Take a passive desktop screenshot.

This script does not click, type, move, resize, focus, or close any window.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

ROOT = Path(r"C:\Users\LJ\KICAD_ENGINE")
SCREENSHOT_DIR = ROOT / "03_TOOLS" / "windows" / "logs" / "screenshots"


def main() -> int:
    import pyautogui

    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = SCREENSHOT_DIR / f"screenshot_{timestamp}.png"

    image = pyautogui.screenshot()
    image.save(screenshot_path)

    width, height = image.size
    print(f"SCREENSHOT_PATH={screenshot_path}")
    print(f"SCREENSHOT_SIZE={width}x{height}")
    print("Safety: screenshot only. No clicks, typing, window movement, resizing, focusing, or closing were performed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
