#!/usr/bin/env python3
"""Prepare a safe schematic layout rewrite plan without editing by default."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from plan_schematic_block_layout import build_plan
from schematic_layout_common import (
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    common_parser,
    ensure_report_dir,
    infer_project_root,
    resolve_project_and_schematic,
    write_markdown_and_json,
)


def build_result(schematic: Path, apply_requested: bool) -> dict[str, Any]:
    plan = build_plan(schematic)
    operations: list[dict[str, Any]] = []
    for item in plan["plan_items"]:
        if item["status"] == CHECK_STATUS_PASS:
            continue
        operations.append(
            {
                "operation": "move_block",
                "block_id": item["block_id"],
                "title": item["title"],
                "target_centroid": item["target_centroid"],
                "movement_delta_mm": item["movement_delta_mm"],
                "reason": item["action"],
            }
        )
    result_status = "DRY_RUN_ONLY_NO_SCHEMATIC_WRITE"
    message = "No schematic file was written. This wrapper only prepares a rewrite plan unless a future structured writer is approved."
    if apply_requested:
        result_status = "APPLY_BLOCKED_NO_STRUCTURED_WRITER"
        message = "Apply mode was requested, but active schematic rewrite remains intentionally blocked until a structured KiCad schematic writer is approved."
    return {
        "generated_at": plan["generated_at"],
        "schematic": plan["schematic"],
        "status": result_status,
        "apply_requested": apply_requested,
        "write_performed": False,
        "message": message,
        "operation_count": len(operations),
        "operations": operations,
        "planner_id": plan["planner_id"],
    }


def build_markdown(result: dict[str, Any]) -> str:
    lines = [
        "# Safe Schematic Layout Rewrite Probe",
        "",
        f"Status: `{result['status']}`",
        f"Apply requested: `{result['apply_requested']}`",
        f"Write performed: `{result['write_performed']}`",
        "",
        f"Schematic: `{result['schematic']}`",
        "",
        f"- Planned operations: `{result['operation_count']}`",
        f"- Message: {result['message']}",
        "",
    ]
    if result["operations"]:
        lines.extend(
            [
                "## Planned Operations",
                "",
                "| Operation | Block | Move (dx, dy mm) |",
                "| --- | --- | --- |",
            ]
        )
        for item in result["operations"]:
            move = f"{item['movement_delta_mm']['dx']}, {item['movement_delta_mm']['dy']}"
            lines.append(f"| {item['operation']} | {item['title']} | `{move}` |")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = common_parser("Prepare a safe schematic layout rewrite plan.", allow_apply=True)
    args = parser.parse_args()
    project_root, schematic = resolve_project_and_schematic(args.project, args.schematic)
    project_root = project_root or infer_project_root(schematic)
    report_dir = ensure_report_dir(project_root, schematic, args.report_dir)
    report_dir.mkdir(parents=True, exist_ok=True)
    result = build_result(schematic, args.apply)
    output = Path(args.output) if args.output else report_dir / "rewrite_schematic_layout_safe.md"
    json_output = Path(args.json_output) if args.json_output else report_dir / "rewrite_schematic_layout_safe.json"
    write_markdown_and_json(build_markdown(result), result, output, json_output)
    print(str(json_output))
    return 0 if not args.apply else 1


if __name__ == "__main__":
    raise SystemExit(main())
