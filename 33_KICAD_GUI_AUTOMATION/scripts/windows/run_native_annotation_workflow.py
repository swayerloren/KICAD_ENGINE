#!/usr/bin/env python3
"""Run the full native KiCad annotation workflow, dry-run by default."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from gui_workflow_common import (
    create_backup,
    default_evidence_dir,
    default_python,
    detect_window_state,
    format_command,
    live_command_text,
    now_iso,
    run_cli_erc,
    run_json_command,
    scan_saved_schematic_references,
    capture_screenshot,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--schematic", required=True)
    parser.add_argument("--live", action="store_true", help="Allow live GUI opening/control. Default is dry-run.")
    parser.add_argument("--allow-annotation", action="store_true")
    parser.add_argument("--allow-save", action="store_true")
    parser.add_argument("--allow-gui-erc", action="store_true")
    parser.add_argument("--allow-unsaved-existing", action="store_true")
    parser.add_argument("--python", default=default_python())
    parser.add_argument("--evidence-dir", default="", help="Optional evidence directory for live screenshots and CLI ERC output.")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    schematic = Path(args.schematic).resolve()
    window_state = detect_window_state(schematic) if schematic.exists() else {"state": "MISSING_SCHEMATIC", "windows": []}

    result = {
        "checked_at": now_iso(),
        "mode": "LIVE" if args.live else "DRY_RUN",
        "project": str(project),
        "schematic": str(schematic),
        "python": args.python,
        "window_state_before": window_state.get("state"),
        "windows_before": window_state.get("windows", []),
        "status": "UNKNOWN",
        "blockers": [],
        "actions": [],
        "future_live_command": live_command_text(project, schematic, args.python),
        "ensure_eeschema_result": None,
        "backup_path": None,
        "evidence_dir": None,
        "before_screenshot": None,
        "annotation_result": None,
        "save_result": None,
        "gui_erc_result": None,
        "after_screenshot": None,
        "cli_erc_result": None,
        "saved_reference_scan": None,
        "did_edit_kicad_files": False,
        "did_modify_pcb": False,
        "did_generate_manufacturing_outputs": False,
    }

    if not project.exists() or project.suffix != ".kicad_pro":
        result["blockers"].append("Project path is missing or is not a .kicad_pro file.")
    if not schematic.exists() or schematic.suffix != ".kicad_sch":
        result["blockers"].append("Schematic path is missing or is not a .kicad_sch file.")

    state = str(window_state.get("state"))
    if state == "PATH_MISMATCH":
        result["blockers"].append("An Eeschema window is already open for a different project; stop.")
    elif state == "MULTIPLE_EESCHEMA_WINDOWS":
        result["blockers"].append("Multiple Eeschema windows are open; target is ambiguous.")
    elif state == "UNSAVED_GUI_STATE" and not args.allow_unsaved_existing:
        result["blockers"].append("Target Eeschema window is already open with unsaved '*' state and was not explicitly allowed.")

    if not args.live:
        result["status"] = "DRY_RUN_READY_NATIVE_ANNOTATION_WORKFLOW" if not result["blockers"] else "DRY_RUN_BLOCKED"
        result["actions"].extend(
            [
                "Would ensure Eeschema is open for the exact target schematic.",
                "Would create a backup before native annotation or GUI save.",
                "Would capture before and after screenshots.",
                "Would run native annotation only with --allow-annotation.",
                "Would save only with --allow-save.",
                "Would run GUI ERC only with --allow-gui-erc.",
                "Would run post-save kicad-cli ERC and saved-schematic reference scans.",
            ]
        )
        print(json.dumps(result, indent=2))
        return 0 if not result["blockers"] else 2

    if not args.allow_annotation:
        result["blockers"].append("--allow-annotation is required for live native annotation.")
    if not args.allow_save:
        result["blockers"].append("--allow-save is required for live GUI save.")
    if not args.allow_gui_erc:
        result["blockers"].append("--allow-gui-erc is required for the full authoritative live annotation workflow.")
    if result["blockers"]:
        result["status"] = "BLOCKED_LIVE_FLAGS_OR_PRECHECKS_FAILED"
        print(json.dumps(result, indent=2))
        return 2

    ensure_script = Path(__file__).with_name("ensure_eeschema_open.py")
    ensure_cmd = [args.python, str(ensure_script), "--project", str(project), "--schematic", str(schematic), "--live", "--python", args.python]
    if args.allow_unsaved_existing:
        ensure_cmd.append("--allow-unsaved-existing")
    code, data, stdout, stderr = run_json_command(ensure_cmd)
    result["ensure_eeschema_result"] = data or {"stdout": stdout, "stderr": stderr, "exit_code": code}
    if code != 0:
        result["status"] = "BLOCKED_EESCHEMA_NOT_READY"
        print(json.dumps(result, indent=2))
        return 2

    backup = create_backup(project, schematic)
    result["backup_path"] = str(backup)
    evidence_dir = Path(args.evidence_dir).resolve() if args.evidence_dir else default_evidence_dir(project)
    evidence_dir.mkdir(parents=True, exist_ok=True)
    result["evidence_dir"] = str(evidence_dir)

    before_path = evidence_dir / "before_eeschema.png"
    code, data, message = capture_screenshot(args.python, schematic, before_path)
    result["before_screenshot"] = data or {"message": message, "exit_code": code}
    if code != 0:
        result["status"] = "BLOCKED_BEFORE_SCREENSHOT_FAILED"
        print(json.dumps(result, indent=2))
        return 2

    annotate_script = Path(__file__).with_name("annotate_schematic_gui.py")
    annotate_cmd = [
        args.python,
        str(annotate_script),
        "--expected-schematic",
        str(schematic),
        "--live",
        "--allow-annotation",
        "--backup-path",
        str(backup),
        "--allow-gui-control",
    ]
    if args.allow_unsaved_existing:
        annotate_cmd.append("--allow-unsaved-existing")
    code, data, stdout, stderr = run_json_command(annotate_cmd)
    result["annotation_result"] = data or {"stdout": stdout, "stderr": stderr, "exit_code": code}
    if code != 0:
        result["status"] = "BLOCKED_NATIVE_ANNOTATION_FAILED"
        print(json.dumps(result, indent=2))
        return 2

    save_script = Path(__file__).with_name("save_schematic_gui.py")
    save_cmd = [
        args.python,
        str(save_script),
        "--expected-schematic",
        str(schematic),
        "--live",
        "--allow-save",
        "--backup-path",
        str(backup),
        "--confirm-overwrite-disk",
        "--allow-gui-control",
        "--allow-unsaved-existing",
    ]
    code, data, stdout, stderr = run_json_command(save_cmd)
    result["save_result"] = data or {"stdout": stdout, "stderr": stderr, "exit_code": code}
    if code != 0:
        result["status"] = "BLOCKED_GUI_SAVE_FAILED"
        print(json.dumps(result, indent=2))
        return 2

    erc_script = Path(__file__).with_name("run_erc_gui.py")
    erc_cmd = [args.python, str(erc_script), "--expected-schematic", str(schematic), "--live", "--allow-gui-erc"]
    code, data, stdout, stderr = run_json_command(erc_cmd)
    result["gui_erc_result"] = data or {"stdout": stdout, "stderr": stderr, "exit_code": code}
    if code != 0:
        result["status"] = "BLOCKED_GUI_ERC_FAILED"
        print(json.dumps(result, indent=2))
        return 2

    after_path = evidence_dir / "after_eeschema.png"
    code, data, message = capture_screenshot(args.python, schematic, after_path)
    result["after_screenshot"] = data or {"message": message, "exit_code": code}
    if code != 0:
        result["status"] = "BLOCKED_AFTER_SCREENSHOT_FAILED"
        print(json.dumps(result, indent=2))
        return 2

    cli_erc = run_cli_erc(schematic, evidence_dir / "post_save_cli_erc.rpt")
    result["cli_erc_result"] = cli_erc
    if cli_erc.get("status") != "PASS":
        result["status"] = "BLOCKED_POST_SAVE_CLI_ERC_FAILED"
        print(json.dumps(result, indent=2))
        return 2

    saved_scan = scan_saved_schematic_references(schematic)
    result["saved_reference_scan"] = saved_scan
    if not saved_scan.get("passes_question_reference_scan"):
        result["status"] = "BLOCKED_UNRESOLVED_QUESTION_REFS_REMAIN"
        print(json.dumps(result, indent=2))
        return 2
    if not saved_scan.get("passes_duplicate_reference_scan"):
        result["status"] = "BLOCKED_DUPLICATE_REFERENCES_REMAIN"
        print(json.dumps(result, indent=2))
        return 2

    result["status"] = "LIVE_NATIVE_ANNOTATION_WORKFLOW_PASS"
    result["did_edit_kicad_files"] = True
    result["actions"].append("Native annotation, GUI save, GUI ERC, post-save CLI ERC, and saved-schematic reference scans all passed.")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
