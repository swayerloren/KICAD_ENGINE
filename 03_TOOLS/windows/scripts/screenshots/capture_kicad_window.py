"""Capture screenshots of confirmed KiCad process windows only.

Passive only: no clicks, typing, hotkeys, focus changes, window moves, window
closes, or file saves inside KiCad.
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(SCRIPT_ROOT))

from kicad_window_filter import (  # noqa: E402
    append_candidate_sections,
    add_common_arguments,
    collect_pywinauto_candidates,
    print_classification_summary,
    resolve_output_dir,
    safe_text,
)


def safe_filename(value: str) -> str:
    cleaned = "".join(ch if ch.isalnum() or ch in ("-", "_") else "_" for ch in value)
    cleaned = "_".join(part for part in cleaned.split("_") if part)
    return cleaned[:80] or "kicad_window"


def capture(window: dict[str, Any], timestamp: str, screenshot_dir: Path) -> Path:
    from PIL import ImageGrab

    screenshot_dir.mkdir(parents=True, exist_ok=True)
    filename = f"kicad_window_{timestamp}_{safe_filename(str(window['window_title']))}_{window['pid']}.png"
    output_path = screenshot_dir / filename

    bbox = (window["left"], window["top"], window["right"], window["bottom"])
    image = ImageGrab.grab(bbox=bbox, all_screens=True)
    image.save(output_path)
    return output_path


def write_report(
    *,
    all_candidates: list[dict[str, Any]],
    notes: list[str],
    captures: list[dict[str, str]],
    output_dir: Path,
    timestamp: str,
    allow_title_only_review: bool,
    target_pid: int | None,
) -> Path:
    report_path = output_dir / f"kicad_window_screenshot_{timestamp}.md"
    lines = [
        "# KiCad Window Screenshot Capture",
        "",
        f"Timestamp: {timestamp}",
        f"Allow title-only review: `{str(allow_title_only_review).lower()}`",
        f"Target PID: `{target_pid if target_pid is not None else 'NONE'}`",
        "",
        "Safety: screenshot capture only. No clicks, typing, hotkeys, focusing, window movement, window closing, or file saves inside KiCad were performed.",
        "",
        "Only high-confidence KiCad process windows are eligible for screenshots. Low-confidence title-only candidates are reported but never captured or controlled.",
        "",
    ]
    if notes:
        lines.extend(["## Notes", ""])
        lines.extend(f"- {safe_text(note)}" for note in notes)
        lines.append("")

    append_candidate_sections(lines, all_candidates)

    lines.extend(
        [
            "## Screenshot Result",
            "",
            "| Process Name | PID | Window Title | Screenshot |",
            "| --- | --- | --- | --- |",
        ]
    )
    if captures:
        for item in captures:
            lines.append(
                f"| {safe_text(item['process_name'])} | {safe_text(item['pid'])} | {safe_text(item['window_title'])} | {safe_text(item['path'])} |"
            )
    else:
        lines.append("| NONE_FOUND | UNKNOWN | No high-confidence KiCad process windows were found. | NOT_CAPTURED |")

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture screenshots of confirmed KiCad process windows only.")
    add_common_arguments(parser)
    args = parser.parse_args()

    output_dir = resolve_output_dir(args.output_dir)
    screenshot_dir = output_dir / "screenshots"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    rows, notes = collect_pywinauto_candidates(backend="uia", target_pid=args.target_pid)
    all_candidates = [candidate for _, candidate in rows]

    captures: list[dict[str, str]] = []
    for candidate in all_candidates:
        if not candidate["eligible_for_screenshot"]:
            continue
        if not all(candidate.get(key) is not None for key in ("left", "top", "right", "bottom")):
            notes.append(f"Skipped screenshot for {candidate['window_title']}: bounds were unavailable.")
            continue
        if int(candidate.get("width", 0)) <= 0 or int(candidate.get("height", 0)) <= 0:
            notes.append(f"Skipped screenshot for {candidate['window_title']}: window size was zero.")
            continue
        try:
            screenshot_path = capture(candidate, timestamp, screenshot_dir)
            captures.append(
                {
                    "process_name": str(candidate["process_name"]),
                    "pid": str(candidate["pid"]),
                    "window_title": str(candidate["window_title"]),
                    "path": str(screenshot_path),
                }
            )
        except Exception as exc:
            notes.append(f"Screenshot failed for {candidate['window_title']}: {safe_text(exc)}")

    report_path = write_report(
        all_candidates=all_candidates,
        notes=notes,
        captures=captures,
        output_dir=output_dir,
        timestamp=timestamp,
        allow_title_only_review=args.allow_title_only_review,
        target_pid=args.target_pid,
    )
    print(f"KICAD_WINDOW_SCREENSHOT_REPORT={report_path}")
    print(f"SCREENSHOT_COUNT={len(captures)}")
    print_classification_summary(all_candidates)
    for item in captures:
        print(f"SCREENSHOT={item['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
