#!/usr/bin/env python
"""Run the KiCad native annotation workflow, dry-run by default.

Live mode is intentionally heavily gated. This wrapper can ensure Eeschema is
open, create a backup, then delegate to native annotation/save/ERC steps only
when --live, --allow-annotation, and --allow-save are all present.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from datetime import datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_PYTHON = REPO_ROOT / "03_TOOLS" / "python_envs" / "windows_gui" / "Scripts" / "python.exe"


def run_json(args: list[str]):
    completed = subprocess.run(args, text=True, capture_output=True, check=False)
    output = completed.stdout.strip()
    data = json.loads(output) if output else {}
    return completed.returncode, data, completed.stderr.strip()


def create_backup(project: Path, schematic: Path) -> Path:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    root = REPO_ROOT / "99_BACKUPS" / "pre_codex_edits" / f"{stamp}_{project.stem}_before_native_annotation_workflow"
    root.mkdir(parents=True, exist_ok=True)
    shutil.copy2(project, root / project.name)
    shutil.copy2(schematic, root / schematic.name)
    return root


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--schematic", required=True)
    parser.add_argument("--live", action="store_true", help="Allow live GUI opening/control. Default is DRY_RUN.")
    parser.add_argument("--allow-annotation", action="store_true")
    parser.add_argument("--allow-save", action="store_true")
    parser.add_argument("--allow-gui-erc", action="store_true")
    parser.add_argument("--allow-unsaved-existing", action="store_true", help="Reserved for future use; current workflow still blocks dirty windows.")
    parser.add_argument("--python", default=str(DEFAULT_PYTHON))
    args = parser.parse_args()

    project = Path(args.project).resolve()
    schematic = Path(args.schematic).resolve()
    python_exe = args.python
    result = {
        "checked_at": datetime.now().isoformat(timespec="seconds"),
        "mode": "LIVE" if args.live else "DRY_RUN",
        "project": str(project),
        "schematic": str(schematic),
        "status": "UNKNOWN",
        "blockers": [],
        "actions": [],
        "backup_path": None,
        "ensure_eeschema_result": None,
        "annotation_result": None,
        "save_result": None,
        "gui_erc_result": None,
        "did_edit_kicad_files": False,
        "did_modify_pcb": False,
        "did_generate_manufacturing_outputs": False,
    }

    if not project.exists() or project.suffix != ".kicad_pro":
        result["blockers"].append("Project path missing or not .kicad_pro.")
    if not schematic.exists() or schematic.suffix != ".kicad_sch":
        result["blockers"].append("Schematic path missing or not .kicad_sch.")

    if not args.live:
        result["status"] = "DRY_RUN_READY_NATIVE_ANNOTATION_FROM_CLOSED_STATE" if not result["blockers"] else "DRY_RUN_BLOCKED"
        result["actions"].extend([
            "Would ensure Eeschema is open for the exact target schematic.",
            "Would create backup before annotation/save.",
            "Would require --allow-annotation before native annotation.",
            "Would require --allow-save before GUI save.",
            "Would run GUI ERC only when --allow-gui-erc is present and safe.",
            "Would run post-save CLI ERC/reference validation in the caller workflow.",
        ])
        print(json.dumps(result, indent=2))
        return 0 if not result["blockers"] else 2

    if not args.allow_annotation:
        result["blockers"].append("--allow-annotation is required for live native annotation.")
    if not args.allow_save:
        result["blockers"].append("--allow-save is required for live GUI save after annotation.")
    if result["blockers"]:
        result["status"] = "BLOCKED_LIVE_FLAGS_OR_PATHS_MISSING"
        print(json.dumps(result, indent=2))
        return 2

    ensure = Path(__file__).with_name("ensure_eeschema_open.py")
    code, data, err = run_json([python_exe, str(ensure), "--project", str(project), "--schematic", str(schematic), "--live", "--python", python_exe])
    result["ensure_eeschema_result"] = data or {"stderr": err, "exit_code": code}
    if code != 0:
        result["status"] = "BLOCKED_EESCHEMA_NOT_READY"
        print(json.dumps(result, indent=2))
        return 2

    backup = create_backup(project, schematic)
    result["backup_path"] = str(backup)

    annotate = Path(__file__).with_name("annotate_schematic_gui.py")
    code, data, err = run_json([
        python_exe,
        str(annotate),
        "--expected-schematic",
        str(schematic),
        "--execute",
        "--backup-confirmed",
        "--allow-gui-control",
        "--confirm-native-annotation-risk",
    ])
    result["annotation_result"] = data or {"stderr": err, "exit_code": code}
    result["did_edit_kicad_files"] = code == 0
    if code != 0:
        result["status"] = "BLOCKED_NATIVE_ANNOTATION_STEP_FAILED"
        print(json.dumps(result, indent=2))
        return 2

    save = Path(__file__).with_name("save_schematic_gui.py")
    code, data, err = run_json([python_exe, str(save), "--expected-schematic", str(schematic), "--execute", "--backup-confirmed"])
    result["save_result"] = data or {"stderr": err, "exit_code": code}
    if code != 0:
        result["status"] = "BLOCKED_GUI_SAVE_FAILED"
        print(json.dumps(result, indent=2))
        return 2

    if args.allow_gui_erc:
        erc = Path(__file__).with_name("run_erc_gui.py")
        code, data, err = run_json([python_exe, str(erc), "--expected-schematic", str(schematic), "--execute"])
        result["gui_erc_result"] = data or {"stderr": err, "exit_code": code}
        if code != 0:
            result["status"] = "BLOCKED_GUI_ERC_FAILED"
            print(json.dumps(result, indent=2))
            return 2

    result["status"] = "LIVE_NATIVE_ANNOTATION_WORKFLOW_COMPLETED_RUN_POST_SAVE_VALIDATION"
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

