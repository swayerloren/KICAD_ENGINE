#!/usr/bin/env python3
"""Write a Markdown execution-contract report."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from validate_task_contract import EDIT_REQUIRED_TASK_TYPES, evaluate_contract, load_contract  # type: ignore  # noqa: E402


def markdown_report(contract: dict, result: dict, contract_path: Path) -> str:
    changed_files = contract.get("changed_files", [])
    evidence = contract.get("evidence", {})
    lines = [
        "# Task Contract Report",
        "",
        f"Generated: `{datetime.now().isoformat(timespec='seconds')}`",
        "",
        f"Contract path: `{contract_path}`",
        f"Task type: `{contract.get('task_type', 'UNKNOWN')}`",
        f"Task summary: `{contract.get('task_summary', '')}`",
        f"Validation result: `{'PASS' if result['valid'] else 'FAIL'}`",
        f"Recommended final status: `{result['recommended_final_status']}`",
        "",
        "## Scope",
        "",
        f"- Project path: `{contract.get('project_path', 'N/A')}`",
        f"- Target PCB: `{contract.get('target_pcb', 'N/A')}`",
        f"- Changed file count: `{len(changed_files)}`",
        "",
        "## Changed Files",
        "",
    ]
    if changed_files:
        for path in changed_files:
            lines.append(f"- `{path}`")
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Evidence",
            "",
            f"- backup_created: `{evidence.get('backup_created')}`",
            f"- backup_path: `{evidence.get('backup_path', 'N/A')}`",
            f"- pcb_hash_before: `{evidence.get('pcb_hash_before', 'N/A')}`",
            f"- pcb_hash_after: `{evidence.get('pcb_hash_after', 'N/A')}`",
            f"- no_design_change_needed: `{evidence.get('no_design_change_needed', False)}`",
            f"- drc_run: `{evidence.get('drc_run')}`",
            f"- visual_export_attempted: `{evidence.get('visual_export_attempted')}`",
        ]
    )

    if contract.get("task_type") == "ROUTING_EDIT_REQUIRED":
        lines.extend(
            [
                f"- unrouted_before: `{evidence.get('unrouted_before', 'N/A')}`",
                f"- unrouted_after: `{evidence.get('unrouted_after', 'N/A')}`",
                f"- unconnected_before: `{evidence.get('unconnected_before', 'N/A')}`",
                f"- unconnected_after: `{evidence.get('unconnected_after', 'N/A')}`",
                f"- trace_change_log_updated: `{evidence.get('trace_change_log_updated')}`",
            ]
        )

    if contract.get("task_type") == "PLACEMENT_EDIT_REQUIRED":
        lines.append(f"- placement_report_updated: `{evidence.get('placement_report_updated')}`")

    lines.extend(
        [
            "",
            "## Enforcement Summary",
            "",
            f"- Edit-required task: `{'YES' if contract.get('task_type') in EDIT_REQUIRED_TASK_TYPES else 'NO'}`",
            f"- Engineering artifact changed: `{'YES' if result['engineering_artifact_changed'] else 'NO'}`",
            "",
            "## Errors",
            "",
        ]
    )
    if result["errors"]:
        for error in result["errors"]:
            lines.append(f"- {error}")
    else:
        lines.append("- none")

    lines.extend(["", "## Warnings", ""])
    if result["warnings"]:
        for warning in result["warnings"]:
            lines.append(f"- {warning}")
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Raw Validation JSON",
            "",
            "```json",
            json.dumps(result, indent=2),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Write a Markdown report for a KiCad Engine task contract.")
    parser.add_argument("--contract", required=True, help="Path to the contract JSON file.")
    parser.add_argument("--output", required=True, help="Path to the Markdown report output.")
    args = parser.parse_args()

    contract_path = Path(args.contract).resolve()
    output_path = Path(args.output).resolve()
    contract = load_contract(contract_path)
    result = evaluate_contract(contract, str(contract_path))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown_report(contract, result, contract_path), encoding="utf-8", newline="\n")
    print(f"WROTE: {output_path}")
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
