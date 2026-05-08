"""Shared passive KiCad window classification helpers.

High-confidence KiCad classification requires a confirmed KiCad process name.
Title-only matches are kept for review/reporting but are never eligible for
inspection, screenshots, or control.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

ROOT = Path(r"C:\Users\LJ\KICAD_ENGINE")
DEFAULT_LOG_DIR = ROOT / "03_TOOLS" / "windows" / "logs"

KICAD_PROCESS_NAMES = {"kicad.exe", "eeschema.exe", "pcbnew.exe"}
TITLE_HINTS = ("kicad", ".kicad", "pcb editor", "schematic editor", "footprint editor")

CONF_HIGH = "HIGH_CONFIDENCE_KICAD_PROCESS"
CONF_LOW_TITLE = "LOW_CONFIDENCE_TITLE_ONLY"
CONF_EXCLUDED = "EXCLUDED_NON_KICAD"
CONF_EXCLUDED_TARGET = "EXCLUDED_NON_TARGET_PID"


def safe_text(value: Any) -> str:
    text = "" if value is None else str(value)
    return text.replace("|", "\\|").replace("\r", " ").replace("\n", " ").strip()


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def process_name(process_id: int | None) -> str:
    if process_id is None:
        return "UNKNOWN"
    try:
        import psutil

        return psutil.Process(process_id).name()
    except Exception:
        return "UNKNOWN"


def title_has_kicad_hint(window_title: str) -> bool:
    lowered = window_title.lower()
    return any(hint in lowered for hint in TITLE_HINTS)


def classify_window(
    *,
    window_title: str,
    proc_name: str,
    pid: int | None,
    target_pid: int | None = None,
) -> dict[str, Any]:
    title = safe_text(window_title)
    process = safe_text(proc_name) or "UNKNOWN"
    process_lower = process.lower()
    pid_text = "UNKNOWN" if pid is None else str(pid)

    if target_pid is not None:
        if pid is None:
            return _candidate(
                title=title,
                process=process,
                pid_text=pid_text,
                confidence=CONF_EXCLUDED_TARGET,
                reason=f"Rejected because --target-pid {target_pid} was set but this window has no readable PID.",
            )
        if int(pid) != int(target_pid):
            return _candidate(
                title=title,
                process=process,
                pid_text=pid_text,
                confidence=CONF_EXCLUDED_TARGET,
                reason=f"Rejected because PID {pid} does not match --target-pid {target_pid}.",
            )

    if process_lower in KICAD_PROCESS_NAMES:
        return _candidate(
            title=title,
            process=process,
            pid_text=pid_text,
            confidence=CONF_HIGH,
            reason=f"Process name {process} is an allowed KiCad process.",
            eligible_for_inspection=True,
            eligible_for_screenshot=True,
        )

    if title_has_kicad_hint(title):
        target_note = ""
        if target_pid is not None:
            target_note = f" --target-pid {target_pid} matched this PID, but"
        return _candidate(
            title=title,
            process=process,
            pid_text=pid_text,
            confidence=CONF_LOW_TITLE,
            reason=(
                f"{target_note} title contains KiCad-related text while process {process} "
                "is not an allowed KiCad process."
            ).strip(),
        )

    return _candidate(
        title=title,
        process=process,
        pid_text=pid_text,
        confidence=CONF_EXCLUDED,
        reason=f"Process {process} is not an allowed KiCad process and title has no KiCad-specific hint.",
    )


def _candidate(
    *,
    title: str,
    process: str,
    pid_text: str,
    confidence: str,
    reason: str,
    eligible_for_inspection: bool = False,
    eligible_for_screenshot: bool = False,
) -> dict[str, Any]:
    return {
        "process_name": process,
        "pid": pid_text,
        "window_title": title,
        "confidence": confidence,
        "reason": safe_text(reason),
        "eligible_for_inspection": eligible_for_inspection,
        "eligible_for_screenshot": eligible_for_screenshot,
        "eligible_for_control": False,
    }


def candidate_from_pywinauto_window(window: Any, *, source: str, target_pid: int | None = None) -> dict[str, Any]:
    try:
        title = safe_text(window.window_text())
    except Exception:
        title = ""

    try:
        pid = int(window.process_id())
    except Exception:
        pid = None

    candidate = classify_window(
        window_title=title,
        proc_name=process_name(pid),
        pid=pid,
        target_pid=target_pid,
    )
    candidate["source"] = source

    try:
        candidate["handle"] = safe_text(getattr(window, "handle", "UNKNOWN"))
    except Exception:
        candidate["handle"] = "UNKNOWN"

    try:
        rect = window.rectangle()
        left, top, right, bottom = int(rect.left), int(rect.top), int(rect.right), int(rect.bottom)
        width = max(0, right - left)
        height = max(0, bottom - top)
        candidate.update(
            {
                "left": left,
                "top": top,
                "right": right,
                "bottom": bottom,
                "width": width,
                "height": height,
                "bounds": f"{left},{top},{right},{bottom}",
                "size": f"{width}x{height}",
            }
        )
    except Exception:
        candidate.update(
            {
                "left": None,
                "top": None,
                "right": None,
                "bottom": None,
                "width": 0,
                "height": 0,
                "bounds": "UNKNOWN",
                "size": "UNKNOWN",
            }
        )

    return candidate


def collect_pywinauto_candidates(
    *,
    backend: str,
    target_pid: int | None = None,
) -> tuple[list[tuple[Any, dict[str, Any]]], list[str]]:
    rows: list[tuple[Any, dict[str, Any]]] = []
    notes: list[str] = []
    try:
        from pywinauto import Desktop

        desktop = Desktop(backend=backend)
        for window in desktop.windows(visible_only=True):
            candidate = candidate_from_pywinauto_window(
                window,
                source=f"pywinauto-{backend}",
                target_pid=target_pid,
            )
            rows.append((window, candidate))
    except Exception as exc:
        notes.append(f"pywinauto {backend} discovery failed: {safe_text(exc)}")
    return rows, notes


def candidate_groups(candidates: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    groups = {
        CONF_HIGH: [],
        CONF_LOW_TITLE: [],
        CONF_EXCLUDED: [],
        CONF_EXCLUDED_TARGET: [],
    }
    for candidate in candidates:
        groups.setdefault(str(candidate["confidence"]), []).append(candidate)
    return groups


def candidate_table_header() -> list[str]:
    return [
        "| Process Name | PID | Window Title | Confidence | Reason | Inspect | Screenshot | Control | Handle | Bounds | Size | Source |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]


def candidate_table_row(candidate: dict[str, Any]) -> str:
    return (
        f"| {safe_text(candidate.get('process_name'))} "
        f"| {safe_text(candidate.get('pid'))} "
        f"| {safe_text(candidate.get('window_title'))} "
        f"| {safe_text(candidate.get('confidence'))} "
        f"| {safe_text(candidate.get('reason'))} "
        f"| {bool_text(bool(candidate.get('eligible_for_inspection')))} "
        f"| {bool_text(bool(candidate.get('eligible_for_screenshot')))} "
        f"| {bool_text(bool(candidate.get('eligible_for_control')))} "
        f"| {safe_text(candidate.get('handle', 'UNKNOWN'))} "
        f"| {safe_text(candidate.get('bounds', 'UNKNOWN'))} "
        f"| {safe_text(candidate.get('size', 'UNKNOWN'))} "
        f"| {safe_text(candidate.get('source', 'UNKNOWN'))} |"
    )


def append_candidate_sections(lines: list[str], candidates: list[dict[str, Any]]) -> None:
    groups = candidate_groups(candidates)

    lines.extend(["## High-Confidence KiCad Windows", ""])
    lines.extend(candidate_table_header())
    if groups[CONF_HIGH]:
        lines.extend(candidate_table_row(candidate) for candidate in groups[CONF_HIGH])
    else:
        lines.append("| NONE_FOUND | UNKNOWN | NONE | NONE | No high-confidence KiCad process was found. KiCad is not running, not visible, or not exposed to this desktop session. | false | false | false | UNKNOWN | UNKNOWN | UNKNOWN | none |")
    lines.append("")

    lines.extend(["## Low-Confidence Title-Only Candidates", ""])
    lines.extend(candidate_table_header())
    if groups[CONF_LOW_TITLE]:
        lines.extend(candidate_table_row(candidate) for candidate in groups[CONF_LOW_TITLE])
    else:
        lines.append("| NONE_FOUND | UNKNOWN | NONE | NONE | No title-only KiCad candidates were found. | false | false | false | UNKNOWN | UNKNOWN | UNKNOWN | none |")
    lines.append("")

    lines.extend(["## Excluded Non-KiCad Windows", ""])
    lines.extend(candidate_table_header())
    excluded = groups[CONF_EXCLUDED] + groups[CONF_EXCLUDED_TARGET]
    if excluded:
        lines.extend(candidate_table_row(candidate) for candidate in excluded)
    else:
        lines.append("| NONE_FOUND | UNKNOWN | NONE | NONE | No excluded non-KiCad windows were recorded. | false | false | false | UNKNOWN | UNKNOWN | UNKNOWN | none |")
    lines.append("")


def print_classification_summary(candidates: list[dict[str, Any]]) -> None:
    groups = candidate_groups(candidates)
    excluded = groups[CONF_EXCLUDED] + groups[CONF_EXCLUDED_TARGET]
    print(f"HIGH_CONFIDENCE_KICAD_WINDOW_COUNT={len(groups[CONF_HIGH])}")
    for candidate in groups[CONF_HIGH]:
        _print_candidate("HIGH_CONFIDENCE_KICAD_WINDOW", candidate)

    print(f"LOW_CONFIDENCE_TITLE_ONLY_COUNT={len(groups[CONF_LOW_TITLE])}")
    for candidate in groups[CONF_LOW_TITLE]:
        _print_candidate("LOW_CONFIDENCE_TITLE_ONLY", candidate)

    print(f"EXCLUDED_NON_KICAD_WINDOW_COUNT={len(excluded)}")
    for candidate in excluded:
        _print_candidate("EXCLUDED_NON_KICAD_WINDOW", candidate)


def _print_candidate(prefix: str, candidate: dict[str, Any]) -> None:
    print(
        f"{prefix} pid={safe_text(candidate.get('pid'))} "
        f"process={safe_text(candidate.get('process_name'))} "
        f"title={safe_text(candidate.get('window_title'))} "
        f"confidence={safe_text(candidate.get('confidence'))} "
        f"inspect={bool_text(bool(candidate.get('eligible_for_inspection')))} "
        f"screenshot={bool_text(bool(candidate.get('eligible_for_screenshot')))} "
        f"control={bool_text(bool(candidate.get('eligible_for_control')))} "
        f"reason={safe_text(candidate.get('reason'))}"
    )


def add_common_arguments(parser: Any) -> None:
    parser.add_argument(
        "--allow-title-only-review",
        action="store_true",
        help="Include low-confidence title-only candidates in the report. They remain ineligible for control.",
    )
    parser.add_argument(
        "--target-pid",
        type=int,
        default=None,
        help="Limit inspection to this PID. The PID is still rejected unless the process name is a confirmed KiCad process.",
    )
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_LOG_DIR),
        help=f"Directory for markdown reports. Default: {DEFAULT_LOG_DIR}",
    )


def resolve_output_dir(output_dir: str | None) -> Path:
    path = Path(output_dir) if output_dir else DEFAULT_LOG_DIR
    path.mkdir(parents=True, exist_ok=True)
    return path
