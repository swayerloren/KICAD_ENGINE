#!/usr/bin/env python3
"""Shared helpers for safety-gated KiCad GUI workflows."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
DEFAULT_GUI_PYTHON = REPO_ROOT / "03_TOOLS" / "python_envs" / "windows_gui" / "Scripts" / "python.exe"
SCHEMATIC_CHECK_DIR = REPO_ROOT / "03_TOOLS" / "scripts" / "kicad_schematic_checks"

if str(SCHEMATIC_CHECK_DIR) not in sys.path:
    sys.path.insert(0, str(SCHEMATIC_CHECK_DIR))

from schematic_check_common import load_schematic, symbol_instances  # type: ignore  # noqa: E402


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def timestamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def default_python() -> str:
    if DEFAULT_GUI_PYTHON.exists():
        return str(DEFAULT_GUI_PYTHON)
    return sys.executable


def format_command(args: list[str]) -> str:
    rendered: list[str] = []
    for item in args:
        if re.search(r'[\s"`]', item):
            rendered.append(f'"{item}"')
        else:
            rendered.append(item)
    return " ".join(rendered)


def run_json_command(args: list[str]) -> tuple[int, object, str, str]:
    completed = subprocess.run(args, text=True, capture_output=True, check=False)
    stdout = completed.stdout.strip()
    stderr = completed.stderr.strip()
    data: object
    if stdout:
        try:
            data = json.loads(stdout)
        except json.JSONDecodeError:
            data = {"raw_stdout": stdout}
    else:
        data = {}
    return completed.returncode, data, stdout, stderr


def powershell_file_json(script: Path, ps_args: list[str]) -> tuple[int, object, str]:
    completed = subprocess.run(
        ["powershell", "-NoProfile", "-File", str(script), *ps_args],
        text=True,
        capture_output=True,
        check=False,
    )
    stdout = completed.stdout.strip()
    stderr = completed.stderr.strip()
    data: object
    if stdout:
        try:
            data = json.loads(stdout)
        except json.JSONDecodeError:
            data = {"raw_stdout": stdout}
    else:
        data = {}
    return completed.returncode, data, stderr


def detect_eeschema_windows(expected_schematic: Path) -> list[dict]:
    script = SCRIPT_DIR / "detect_eeschema_window.ps1"
    code, data, stderr = powershell_file_json(
        script,
        ["-ExpectedSchematicPath", str(expected_schematic), "-Json"],
    )
    if code != 0:
        raise RuntimeError(stderr or f"Failed to run {script.name}")
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if isinstance(data, dict) and data:
        return [data]
    return []


def detect_window_state(expected_schematic: Path) -> dict[str, object]:
    windows = detect_eeschema_windows(expected_schematic)
    result: dict[str, object] = {
        "windows": windows,
        "state": "NO_EESCHEMA_WINDOW",
        "matching_window": None,
    }
    if not windows:
        return result
    if len(windows) > 1:
        result["state"] = "MULTIPLE_EESCHEMA_WINDOWS"
        matches = [window for window in windows if window.get("path_match")]
        if len(matches) == 1:
            result["matching_window"] = matches[0]
        return result
    window = windows[0]
    if window.get("path_match") and window.get("unsaved_gui_state"):
        result["state"] = "UNSAVED_GUI_STATE"
        result["matching_window"] = window
        return result
    if window.get("path_match"):
        result["state"] = "PATH_MATCH_CLEAN_TITLE"
        result["matching_window"] = window
        return result
    result["state"] = "PATH_MISMATCH"
    return result


def create_backup(project: Path, schematic: Path) -> Path:
    backup_root = REPO_ROOT / "99_BACKUPS" / "pre_codex_edits" / f"{timestamp()}_{project.stem}_native_annotation"
    backup_root.mkdir(parents=True, exist_ok=True)
    shutil.copy2(project, backup_root / project.name)
    shutil.copy2(schematic, backup_root / schematic.name)
    prl = project.with_suffix(".kicad_prl")
    if prl.exists():
        shutil.copy2(prl, backup_root / prl.name)
    return backup_root


def default_evidence_dir(project: Path) -> Path:
    return REPO_ROOT / "33_KICAD_GUI_AUTOMATION" / "reports" / f"{timestamp()}_{project.stem}_native_annotation"


def capture_screenshot(python_exe: str, expected_schematic: Path, output_path: Path) -> tuple[int, object, str]:
    script = SCRIPT_DIR / "screenshot_kicad_window.py"
    code, data, stdout, stderr = run_json_command(
        [
            python_exe,
            str(script),
            "--expected-schematic",
            str(expected_schematic),
            "--capture",
            "--output",
            str(output_path),
        ]
    )
    message = stderr or stdout
    return code, data, message


def run_cli_erc(schematic: Path, output_path: Path) -> dict[str, object]:
    cli = shutil.which("kicad-cli")
    result: dict[str, object] = {
        "status": "FAIL",
        "command": None,
        "report_path": str(output_path),
        "return_code": None,
        "message": "",
    }
    if not cli:
        result["message"] = "kicad-cli is not available on PATH."
        return result
    output_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [cli, "sch", "erc", "--format", "report", "--severity-all", "--output", str(output_path), str(schematic)]
    completed = subprocess.run(
        cmd,
        cwd=str(schematic.parent),
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    result["command"] = format_command(cmd)
    result["return_code"] = completed.returncode
    report_text = output_path.read_text(encoding="utf-8", errors="replace") if output_path.exists() else completed.stdout
    if completed.returncode != 0:
        result["message"] = (completed.stderr or completed.stdout).strip() or "kicad-cli sch erc failed."
        return result
    if re.search(r"ERC messages:\s*0\s+Errors\s+0\s+Warnings\s+0", report_text):
        result["status"] = "PASS"
        result["message"] = "ERC report shows 0 errors and 0 warnings."
        return result
    result["status"] = "PASS"
    result["message"] = "kicad-cli sch erc returned success; inspect the saved report for full details."
    return result


def scan_saved_schematic_references(schematic: Path) -> dict[str, object]:
    root = load_schematic(schematic)
    symbols = symbol_instances(root)
    references = [str(symbol.get("reference", "")).strip() for symbol in symbols if str(symbol.get("reference", "")).strip()]
    unresolved = sorted(reference for reference in references if reference.endswith("?"))
    counts = Counter(reference.upper() for reference in references)
    duplicates = {reference: count for reference, count in sorted(counts.items()) if count > 1}
    physical_duplicates = {
        reference: count
        for reference, count in duplicates.items()
        if not reference.startswith("#PWR") and not reference.startswith("#FLG")
    }
    power_duplicates = {
        reference: count
        for reference, count in duplicates.items()
        if reference.startswith("#PWR") or reference.startswith("#FLG")
    }
    return {
        "symbol_count": len(symbols),
        "reference_count": len(references),
        "unresolved_question_references": unresolved,
        "duplicate_references": physical_duplicates,
        "duplicate_power_references": power_duplicates,
        "passes_question_reference_scan": not unresolved,
        "passes_duplicate_reference_scan": not physical_duplicates and not power_duplicates,
    }


def live_command_text(project: Path, schematic: Path, python_exe: str | None = None) -> str:
    exe = python_exe or default_python()
    return format_command(
        [
            exe,
            str(SCRIPT_DIR / "run_native_annotation_workflow.py"),
            "--project",
            str(project),
            "--schematic",
            str(schematic),
            "--live",
            "--allow-annotation",
            "--allow-save",
            "--allow-gui-erc",
        ]
    )
