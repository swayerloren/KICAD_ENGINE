"""Discover running KiCad windows without controlling them.

Passive only: no clicks, typing, hotkeys, focus changes, window moves, window
closes, or file saves.
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

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


def write_report(
    *,
    candidates: list[dict[str, object]],
    notes: list[str],
    output_dir: Path,
    allow_title_only_review: bool,
    target_pid: int | None,
) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = output_dir / f"kicad_window_discovery_{timestamp}.md"

    lines = [
        "# KiCad Window Discovery",
        "",
        f"Timestamp: {timestamp}",
        f"Allow title-only review: `{str(allow_title_only_review).lower()}`",
        f"Target PID: `{target_pid if target_pid is not None else 'NONE'}`",
        "",
        "Safety: passive discovery only. No clicks, typing, hotkeys, focusing, window movement, window closing, or file saves were performed.",
        "",
        "High-confidence KiCad windows require process name `kicad.exe`, `eeschema.exe`, or `pcbnew.exe`.",
        "Title-only matches are low confidence and are not eligible for inspection, screenshots, or control.",
        "",
    ]
    if notes:
        lines.extend(["## Notes", ""])
        lines.extend(f"- {safe_text(note)}" for note in notes)
        lines.append("")

    append_candidate_sections(lines, candidates)
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only KiCad window discovery.")
    add_common_arguments(parser)
    args = parser.parse_args()

    output_dir = resolve_output_dir(args.output_dir)
    rows, notes = collect_pywinauto_candidates(backend="uia", target_pid=args.target_pid)
    candidates = [candidate for _, candidate in rows]

    report_path = write_report(
        candidates=candidates,
        notes=notes,
        output_dir=output_dir,
        allow_title_only_review=args.allow_title_only_review,
        target_pid=args.target_pid,
    )

    print(f"KICAD_WINDOW_DISCOVERY_REPORT={report_path}")
    print(f"TOTAL_VISIBLE_WINDOW_COUNT={len(candidates)}")
    print_classification_summary(candidates)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
