#!/usr/bin/env python3
"""Enforce edit-required task contracts for KiCad Engine."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from validate_task_contract import EDIT_REQUIRED_TASK_TYPES, evaluate_contract, load_contract  # type: ignore  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Hard-fail edit-required contracts that do not prove engineering artifact change.")
    parser.add_argument("--contract", required=True, help="Path to the contract JSON file.")
    args = parser.parse_args()

    contract_path = Path(args.contract).resolve()
    contract = load_contract(contract_path)
    result = evaluate_contract(contract, str(contract_path))

    task_type = result.get("task_type")
    outcome = {
        "contract_path": str(contract_path),
        "task_type": task_type,
        "edit_required": task_type in EDIT_REQUIRED_TASK_TYPES,
        "valid": result["valid"],
        "engineering_artifact_changed": result["engineering_artifact_changed"],
        "recommended_final_status": result["recommended_final_status"],
        "errors": result["errors"],
        "warnings": result["warnings"],
    }
    print(json.dumps(outcome, indent=2))

    if task_type in EDIT_REQUIRED_TASK_TYPES and result["recommended_final_status"] == "EDIT_REQUIRED_FAILED_NO_ENGINEERING_ARTIFACT_CHANGE":
        return 1
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
