#!/usr/bin/env python3
"""Render a complete schematic layout review packet in read-only mode."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from audit_local_wire_usage import markdown as local_wire_markdown
from audit_local_wire_usage import run_audit as run_local_wire_audit
from audit_visual_flow import markdown as visual_flow_markdown
from audit_visual_flow import run_audit as run_visual_flow_audit
from extract_schematic_layout import build_markdown as extract_markdown
from extract_schematic_layout import build_payload
from plan_schematic_block_layout import build_markdown as plan_markdown
from plan_schematic_block_layout import build_plan
from rewrite_schematic_layout_safe import build_markdown as rewrite_markdown
from rewrite_schematic_layout_safe import build_result as build_rewrite_result
from schematic_layout_common import (
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    common_parser,
    ensure_report_dir,
    infer_project_root,
    resolve_project_and_schematic,
)
from score_schematic_readability import build_markdown as score_markdown
from score_schematic_readability import build_result as build_score_result


def write_pair(markdown_text: str, payload: dict[str, Any], md_path: Path, json_path: Path) -> None:
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(markdown_text, encoding="utf-8")
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def summary_markdown(summary: dict[str, Any]) -> str:
    lines = [
        "# Schematic Layout Review Packet",
        "",
        f"Generated: `{summary['generated_at']}`",
        f"Schematic: `{summary['schematic']}`",
        "",
        f"- Overall status: `{summary['overall_status']}`",
        f"- Readability score: `{summary['readability_score']}/100`",
        f"- Visual flow: `{summary['visual_flow_status']}`",
        f"- Local wire usage: `{summary['local_wire_status']}`",
        "",
        "## Outputs",
        "",
    ]
    for name, path in summary["outputs"].items():
        lines.append(f"- `{name}`: `{path}`")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = common_parser("Render schematic review pages without editing the schematic.")
    args = parser.parse_args()
    project_root, schematic = resolve_project_and_schematic(args.project, args.schematic)
    project_root = project_root or infer_project_root(schematic)
    report_dir = ensure_report_dir(project_root, schematic, args.report_dir)
    report_dir.mkdir(parents=True, exist_ok=True)

    extract_result = build_payload(schematic)
    visual_flow_result = run_visual_flow_audit(schematic)
    local_wire_result = run_local_wire_audit(schematic)
    score_result = build_score_result(project_root, schematic, report_dir)
    plan_result = build_plan(schematic)
    rewrite_result = build_rewrite_result(schematic, apply_requested=False)

    outputs = {
        "layout_extract_md": str(report_dir / "layout_extract.md"),
        "layout_extract_json": str(report_dir / "layout_extract.json"),
        "visual_flow_md": str(report_dir / "visual_flow.md"),
        "visual_flow_json": str(report_dir / "visual_flow.json"),
        "local_wire_usage_md": str(report_dir / "local_wire_usage.md"),
        "local_wire_usage_json": str(report_dir / "local_wire_usage.json"),
        "schematic_readability_score_md": str(report_dir / "schematic_readability_score.md"),
        "schematic_readability_score_json": str(report_dir / "schematic_readability_score.json"),
        "schematic_block_layout_plan_md": str(report_dir / "schematic_block_layout_plan.md"),
        "schematic_block_layout_plan_json": str(report_dir / "schematic_block_layout_plan.json"),
        "rewrite_schematic_layout_safe_md": str(report_dir / "rewrite_schematic_layout_safe.md"),
        "rewrite_schematic_layout_safe_json": str(report_dir / "rewrite_schematic_layout_safe.json"),
    }

    write_pair(extract_markdown(extract_result), extract_result, report_dir / "layout_extract.md", report_dir / "layout_extract.json")
    write_pair(visual_flow_markdown(visual_flow_result), visual_flow_result, report_dir / "visual_flow.md", report_dir / "visual_flow.json")
    write_pair(local_wire_markdown(local_wire_result), local_wire_result, report_dir / "local_wire_usage.md", report_dir / "local_wire_usage.json")
    write_pair(score_markdown(score_result), score_result, report_dir / "schematic_readability_score.md", report_dir / "schematic_readability_score.json")
    write_pair(plan_markdown(plan_result), plan_result, report_dir / "schematic_block_layout_plan.md", report_dir / "schematic_block_layout_plan.json")
    write_pair(rewrite_markdown(rewrite_result), rewrite_result, report_dir / "rewrite_schematic_layout_safe.md", report_dir / "rewrite_schematic_layout_safe.json")

    summary = {
        "generated_at": score_result["generated_at"],
        "schematic": str(schematic),
        "overall_status": score_result["overall_status"],
        "readability_score": score_result["total_score"],
        "visual_flow_status": visual_flow_result["status"],
        "local_wire_status": local_wire_result["status"],
        "outputs": outputs,
    }
    write_pair(summary_markdown(summary), summary, report_dir / "SCHEMATIC_LAYOUT_REVIEW.md", report_dir / "SCHEMATIC_LAYOUT_REVIEW.json")
    print(str(report_dir / "SCHEMATIC_LAYOUT_REVIEW.json"))
    return 0 if args.no_fail or score_result["overall_status"] != CHECK_STATUS_FAIL else 1


if __name__ == "__main__":
    raise SystemExit(main())
