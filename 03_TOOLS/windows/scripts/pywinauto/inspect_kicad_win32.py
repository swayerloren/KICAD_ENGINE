"""Read-only Win32 inspection for confirmed KiCad process windows.

Passive only: no clicks, typing, hotkeys, focus changes, window moves, window
closes, or file saves.
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


def describe_control(control: Any) -> dict[str, str]:
    try:
        title = safe_text(control.window_text())
    except Exception:
        title = "UNKNOWN"
    try:
        class_name = safe_text(control.class_name())
    except Exception:
        class_name = "UNKNOWN"
    try:
        handle = safe_text(getattr(control, "handle", "UNKNOWN"))
    except Exception:
        handle = "UNKNOWN"
    try:
        rect = control.rectangle()
        bounds = f"{rect.left},{rect.top},{rect.right},{rect.bottom}"
    except Exception:
        bounds = "UNKNOWN"
    return {
        "title": title,
        "class_name": class_name,
        "handle": handle,
        "bounds": bounds,
    }


def walk_controls(control: Any, depth: int, max_depth: int, rows: list[dict[str, str]], limit: int) -> None:
    if depth > max_depth or len(rows) >= limit:
        return
    item = describe_control(control)
    item["depth"] = str(depth)
    rows.append(item)
    try:
        children = control.children()
    except Exception:
        return
    for child in children:
        if len(rows) >= limit:
            return
        walk_controls(child, depth + 1, max_depth, rows, limit)


def inspect(max_depth: int, limit: int, target_pid: int | None) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[str]]:
    inspected_windows: list[dict[str, Any]] = []
    rows, notes = collect_pywinauto_candidates(backend="win32", target_pid=target_pid)
    all_candidates = [candidate for _, candidate in rows]

    for window, candidate in rows:
        if not candidate["eligible_for_inspection"]:
            continue
        controls: list[dict[str, str]] = []
        walk_controls(window, 0, max_depth, controls, limit)
        inspected_windows.append({"candidate": candidate, "controls": controls})

    return inspected_windows, all_candidates, notes


def write_report(
    *,
    inspected_windows: list[dict[str, Any]],
    all_candidates: list[dict[str, Any]],
    notes: list[str],
    max_depth: int,
    limit: int,
    output_dir: Path,
    allow_title_only_review: bool,
    target_pid: int | None,
) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = output_dir / f"kicad_win32_inspection_{timestamp}.md"

    lines = [
        "# KiCad Win32 Inspection",
        "",
        f"Timestamp: {timestamp}",
        f"Max depth: {max_depth}",
        f"Per-window node limit: {limit}",
        f"Allow title-only review: `{str(allow_title_only_review).lower()}`",
        f"Target PID: `{target_pid if target_pid is not None else 'NONE'}`",
        "",
        "Safety: read-only Win32 inspection. No clicks, typing, hotkeys, focusing, window movement, window closing, or file saves were performed.",
        "",
        "Only high-confidence KiCad process windows are inspected. Low-confidence title-only candidates are reported but never inspected or controlled.",
        "",
    ]
    if notes:
        lines.extend(["## Notes", ""])
        lines.extend(f"- {safe_text(note)}" for note in notes)
        lines.append("")

    append_candidate_sections(lines, all_candidates)

    if not inspected_windows:
        lines.extend(
            [
                "## Win32 Inspection Result",
                "",
                "No high-confidence KiCad process windows were found. No Win32 tree inspection was performed.",
                "",
            ]
        )

    for window in inspected_windows:
        candidate = window["candidate"]
        controls = window["controls"]
        lines.extend(
            [
                f"## Inspected Window: {safe_text(candidate['window_title'])}",
                "",
                f"- Process ID: `{safe_text(candidate['pid'])}`",
                f"- Process name: `{safe_text(candidate['process_name'])}`",
                f"- Confidence: `{safe_text(candidate['confidence'])}`",
                f"- Reason: {safe_text(candidate['reason'])}",
                f"- Handle: `{safe_text(candidate.get('handle', 'UNKNOWN'))}`",
                f"- Controls recorded: `{len(controls)}`",
                "",
                "| Depth | Title | Class | Handle | Bounds |",
                "| ---: | --- | --- | --- | --- |",
            ]
        )
        for control in controls:
            lines.append(
                f"| {control['depth']} | {control['title']} | {control['class_name']} | {control['handle']} | {control['bounds']} |"
            )
        lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only KiCad Win32 inspection.")
    parser.add_argument("--max-depth", type=int, default=4)
    parser.add_argument("--limit", type=int, default=500)
    add_common_arguments(parser)
    args = parser.parse_args()

    output_dir = resolve_output_dir(args.output_dir)
    inspected_windows, all_candidates, notes = inspect(
        max_depth=args.max_depth,
        limit=args.limit,
        target_pid=args.target_pid,
    )
    report_path = write_report(
        inspected_windows=inspected_windows,
        all_candidates=all_candidates,
        notes=notes,
        max_depth=args.max_depth,
        limit=args.limit,
        output_dir=output_dir,
        allow_title_only_review=args.allow_title_only_review,
        target_pid=args.target_pid,
    )
    print(f"KICAD_WIN32_INSPECTION_REPORT={report_path}")
    print(f"INSPECTED_KICAD_WINDOW_COUNT={len(inspected_windows)}")
    print_classification_summary(all_candidates)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
