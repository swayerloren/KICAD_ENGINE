"""List visible Windows desktop windows without controlling them.

This script is passive. It does not click, type, move, resize, focus, or close
any window.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any


def _repo_root() -> Path:
    current = Path(__file__).resolve()
    for candidate in [current.parent, *current.parents]:
        if (candidate / "AGENTS.md").exists():
            return candidate
    return current.parents[4]


ROOT = _repo_root()
LOG_DIR = ROOT / "03_TOOLS" / "windows" / "logs"


def _safe_text(value: Any) -> str:
    text = "" if value is None else str(value)
    return text.replace("|", "\\|").replace("\r", " ").replace("\n", " ").strip()


def _collect_with_pywinauto() -> tuple[list[dict[str, str]], str | None]:
    rows: list[dict[str, str]] = []
    try:
        from pywinauto import Desktop

        desktop = Desktop(backend="uia")
        for window in desktop.windows(visible_only=True):
            title = _safe_text(window.window_text())
            if not title:
                continue
            try:
                process_id = str(window.process_id())
            except Exception:
                process_id = "UNKNOWN"
            try:
                rect = window.rectangle()
                bounds = f"{rect.left},{rect.top},{rect.right},{rect.bottom}"
            except Exception:
                bounds = "UNKNOWN"
            rows.append(
                {
                    "title": title,
                    "process_id": process_id,
                    "bounds": bounds,
                    "source": "pywinauto-uia",
                }
            )
        return rows, None
    except Exception as exc:  # Passive fallback only.
        return rows, f"pywinauto discovery failed: {exc}"


def _collect_with_pygetwindow() -> tuple[list[dict[str, str]], str | None]:
    rows: list[dict[str, str]] = []
    try:
        import pygetwindow as gw

        for window in gw.getAllWindows():
            title = _safe_text(getattr(window, "title", ""))
            if not title:
                continue
            width = getattr(window, "width", None)
            height = getattr(window, "height", None)
            if width is not None and height is not None and (width <= 0 or height <= 0):
                continue
            left = getattr(window, "left", "UNKNOWN")
            top = getattr(window, "top", "UNKNOWN")
            right = getattr(window, "right", "UNKNOWN")
            bottom = getattr(window, "bottom", "UNKNOWN")
            rows.append(
                {
                    "title": title,
                    "process_id": "UNAVAILABLE",
                    "bounds": f"{left},{top},{right},{bottom}",
                    "source": "pygetwindow",
                }
            )
        return rows, None
    except Exception as exc:
        return rows, f"pygetwindow discovery failed: {exc}"


def main() -> int:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = LOG_DIR / f"window_discovery_{timestamp}.md"

    rows, primary_error = _collect_with_pywinauto()
    fallback_error = None
    if not rows:
        rows, fallback_error = _collect_with_pygetwindow()

    lines = [
        "# Window Discovery",
        "",
        f"Timestamp: {timestamp}",
        "",
        "Safety: passive discovery only. No clicks, typing, window movement, resizing, focusing, or closing were performed.",
        "",
    ]

    if primary_error:
        lines.extend(["## Notes", "", f"- {primary_error}", ""])
    if fallback_error:
        lines.extend(["## Fallback Notes", "", f"- {fallback_error}", ""])

    lines.extend(
        [
            "## Visible Windows",
            "",
            "| Title | Process ID | Bounds Left,Top,Right,Bottom | Source |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in rows:
        lines.append(
            f"| {row['title']} | {row['process_id']} | {row['bounds']} | {row['source']} |"
        )

    if not rows:
        lines.append("| NONE_FOUND | UNKNOWN | UNKNOWN | none |")

    log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"WINDOW_DISCOVERY_LOG={log_path}")
    print(f"VISIBLE_WINDOW_COUNT={len(rows)}")
    for row in rows:
        print(f"WINDOW title={row['title']} pid={row['process_id']} bounds={row['bounds']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
