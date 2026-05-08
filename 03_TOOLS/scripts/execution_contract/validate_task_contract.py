#!/usr/bin/env python3
"""Validate KiCad Engine task execution contracts."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
SCHEMA_PATH = SCRIPT_DIR / "task_contract.schema.json"

TASK_TYPES = {
    "DOCS_ONLY",
    "AUDIT_ONLY",
    "LIVE_STATE_RECONCILE",
    "PLACEMENT_EDIT_REQUIRED",
    "ROUTING_EDIT_REQUIRED",
    "PCB_EDIT_REQUIRED",
    "GITHUB_DOCS_ONLY",
}

NON_EDIT_TASK_TYPES = {
    "DOCS_ONLY",
    "AUDIT_ONLY",
    "LIVE_STATE_RECONCILE",
    "GITHUB_DOCS_ONLY",
}

EDIT_REQUIRED_TASK_TYPES = {
    "PLACEMENT_EDIT_REQUIRED",
    "ROUTING_EDIT_REQUIRED",
    "PCB_EDIT_REQUIRED",
}

KICAD_DESIGN_SUFFIXES = {
    ".kicad_pcb",
    ".kicad_sch",
    ".kicad_pro",
    ".kicad_prl",
    ".kicad_sym",
    ".kicad_mod",
}


def load_contract(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_schema() -> dict[str, Any]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def is_sha256(value: Any) -> bool:
    return isinstance(value, str) and bool(re.fullmatch(r"[0-9a-fA-F]{64}", value))


def is_kicad_design_file(path_text: str) -> bool:
    return Path(path_text).suffix.lower() in KICAD_DESIGN_SUFFIXES


def require_bool_true(evidence: dict[str, Any], key: str, errors: list[str], reason: str) -> None:
    if evidence.get(key) is not True:
        errors.append(reason)


def require_int(evidence: dict[str, Any], key: str, errors: list[str], reason: str) -> None:
    if not isinstance(evidence.get(key), int):
        errors.append(reason)


def evaluate_contract(contract: dict[str, Any], contract_path: str = "<memory>") -> dict[str, Any]:
    schema = load_schema()
    errors: list[str] = []
    warnings: list[str] = []

    task_type = contract.get("task_type")
    if task_type not in TASK_TYPES:
        errors.append(
            "task_type must be exactly one supported value: "
            + ", ".join(sorted(TASK_TYPES))
        )

    if not isinstance(contract.get("task_summary"), str) or not contract.get("task_summary", "").strip():
        errors.append("task_summary must be a non-empty string.")

    changed_files_raw = contract.get("changed_files")
    if not isinstance(changed_files_raw, list) or not all(isinstance(item, str) for item in changed_files_raw):
        errors.append("changed_files must be a list of file-path strings.")
        changed_files: list[str] = []
    else:
        changed_files = changed_files_raw

    evidence_raw = contract.get("evidence")
    if not isinstance(evidence_raw, dict):
        errors.append("evidence must be a JSON object.")
        evidence: dict[str, Any] = {}
    else:
        evidence = evidence_raw

    unknown_keys = set(contract.keys()) - set(schema["properties"].keys())
    if unknown_keys:
        errors.append(
            "contract contains unsupported top-level keys: "
            + ", ".join(sorted(unknown_keys))
        )

    changed_kicad_files = [path for path in changed_files if is_kicad_design_file(path)]
    target_pcb = contract.get("target_pcb")
    target_pcb_valid = isinstance(target_pcb, str) and target_pcb.lower().endswith(".kicad_pcb")

    hash_before = evidence.get("pcb_hash_before")
    hash_after = evidence.get("pcb_hash_after")
    hash_before_valid = is_sha256(hash_before)
    hash_after_valid = is_sha256(hash_after)
    hash_changed = hash_before_valid and hash_after_valid and hash_before != hash_after
    no_design_change_needed = evidence.get("no_design_change_needed") is True
    pcb_file_listed = any(Path(path).suffix.lower() == ".kicad_pcb" for path in changed_files)

    if task_type in NON_EDIT_TASK_TYPES and changed_kicad_files:
        errors.append(
            f"{task_type} cannot edit KiCad design files, but changed_files includes: "
            + ", ".join(changed_kicad_files)
        )

    if task_type in EDIT_REQUIRED_TASK_TYPES:
        if not target_pcb_valid:
            errors.append("target_pcb must be a .kicad_pcb path for edit-required tasks.")
        require_bool_true(
            evidence,
            "backup_created",
            errors,
            f"{task_type} must prove backup_created=true.",
        )
        if not isinstance(evidence.get("backup_path"), str) or not evidence.get("backup_path", "").strip():
            errors.append(f"{task_type} must record backup_path.")
        if not hash_before_valid:
            errors.append(f"{task_type} must record a valid 64-hex pcb_hash_before.")
        if not hash_after_valid:
            errors.append(f"{task_type} must record a valid 64-hex pcb_hash_after.")
        require_bool_true(
            evidence,
            "drc_run",
            errors,
            f"{task_type} must prove drc_run=true.",
        )
        require_bool_true(
            evidence,
            "visual_export_attempted",
            errors,
            f"{task_type} must prove visual_export_attempted=true.",
        )

        if task_type == "PCB_EDIT_REQUIRED":
            if not hash_changed and not no_design_change_needed:
                errors.append(
                    "PCB_EDIT_REQUIRED must prove pcb_hash_before != pcb_hash_after or explicit no_design_change_needed=true."
                )
            if no_design_change_needed and hash_changed:
                warnings.append(
                    "no_design_change_needed=true was declared, but pcb_hash_before and pcb_hash_after differ."
                )
        else:
            if not hash_changed:
                errors.append(
                    f"{task_type} must prove pcb_hash_before != pcb_hash_after."
                )

        if hash_changed and not pcb_file_listed:
            errors.append(
                f"{task_type} changed the PCB hash but changed_files does not include a .kicad_pcb path."
            )

        if task_type == "ROUTING_EDIT_REQUIRED":
            require_int(
                evidence,
                "unrouted_before",
                errors,
                "ROUTING_EDIT_REQUIRED must record unrouted_before as an integer.",
            )
            require_int(
                evidence,
                "unrouted_after",
                errors,
                "ROUTING_EDIT_REQUIRED must record unrouted_after as an integer.",
            )
            require_int(
                evidence,
                "unconnected_before",
                errors,
                "ROUTING_EDIT_REQUIRED must record unconnected_before as an integer.",
            )
            require_int(
                evidence,
                "unconnected_after",
                errors,
                "ROUTING_EDIT_REQUIRED must record unconnected_after as an integer.",
            )
            require_bool_true(
                evidence,
                "trace_change_log_updated",
                errors,
                "ROUTING_EDIT_REQUIRED must prove trace_change_log_updated=true.",
            )

        if task_type == "PLACEMENT_EDIT_REQUIRED":
            require_bool_true(
                evidence,
                "placement_report_updated",
                errors,
                "PLACEMENT_EDIT_REQUIRED must prove placement_report_updated=true.",
            )

    engineering_artifact_changed = task_type in EDIT_REQUIRED_TASK_TYPES and hash_changed and pcb_file_listed

    recommended_final_status = "VALID_TASK_CONTRACT"
    if task_type in EDIT_REQUIRED_TASK_TYPES:
        if task_type == "PCB_EDIT_REQUIRED" and no_design_change_needed and not hash_changed:
            recommended_final_status = "NO_DESIGN_CHANGE_NEEDED"
        elif not engineering_artifact_changed:
            recommended_final_status = "EDIT_REQUIRED_FAILED_NO_ENGINEERING_ARTIFACT_CHANGE"
        else:
            recommended_final_status = "ENGINEERING_ARTIFACT_CHANGE_PROVEN"
    elif errors:
        recommended_final_status = "INVALID_TASK_CONTRACT"

    declared_final_status = contract.get("declared_final_status")
    if isinstance(declared_final_status, str) and declared_final_status.strip():
        if declared_final_status != recommended_final_status:
            warnings.append(
                "declared_final_status does not match the validator recommendation: "
                f"declared={declared_final_status}, recommended={recommended_final_status}"
            )

    return {
        "contract_path": contract_path,
        "task_type": task_type,
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "recommended_final_status": recommended_final_status,
        "engineering_artifact_changed": engineering_artifact_changed,
        "hash_changed": hash_changed,
        "changed_kicad_files": changed_kicad_files,
        "changed_file_count": len(changed_files),
        "schema_path": str(SCHEMA_PATH),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a KiCad Engine task execution contract.")
    parser.add_argument("--contract", required=True, help="Path to the contract JSON file.")
    args = parser.parse_args()

    contract_path = Path(args.contract).resolve()
    contract = load_contract(contract_path)
    result = evaluate_contract(contract, str(contract_path))
    print(json.dumps(result, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
