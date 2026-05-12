#!/usr/bin/env python3
"""Run the full read-only PCB prelayout gate for one active project."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from _prelayout_common import (
    dump_json,
    dump_markdown,
    iso_now,
    load_json,
    locate_project,
    repo_rel,
    timestamp_slug,
)
from compare_variants import compare_variant_scores
from extract_board_digital_twin import extract_board_digital_twin, twin_markdown
from generate_placement_variants import generate_placement_variants, variants_markdown
from project_routes_45deg import project_variant_routes, projection_markdown
from render_variant_preview import render_svg
from score_placement_variant import score_markdown, score_variant


def evaluate_prelayout_gate(
    twin: dict[str, Any],
    variants: list[dict[str, Any]],
    scores: list[dict[str, Any]],
    comparison: dict[str, Any],
    artifact_paths: dict[str, Any],
) -> dict[str, Any]:
    placement_blocking_codes: list[str] = []
    placement_blocking_reasons: list[str] = []
    variant_map = {variant["variant_id"]: variant for variant in variants}
    selected_variant_id = comparison.get("selected_variant_id")
    selected_variant = variant_map.get(selected_variant_id) if selected_variant_id else None
    selected_score = next((score for score in scores if score["variant_id"] == selected_variant_id), None)
    live = twin["live_board_context"]

    if len(variants) < 3:
        placement_blocking_codes.append("BLOCKED_NEEDS_THREE_VARIANTS")
        placement_blocking_reasons.append("At least three variants are required.")
    if int(comparison["passing_variant_count"]) < 1:
        placement_blocking_codes.append("BLOCKED_NO_PASSING_VARIANT")
        placement_blocking_reasons.append("No variant achieved PASS status.")
    if selected_variant and any(truth["truth_status"] != "PASS" for truth in selected_variant.get("connector_truths", [])):
        placement_blocking_codes.append("BLOCKED_CONNECTOR_DIRECTION")
        placement_blocking_reasons.append("The selected variant still has connector truth failures or unknowns.")
    if selected_variant and int(selected_variant.get("projected_open_nets_count", 0)) > 0:
        placement_blocking_codes.append("BLOCKED_PROJECTED_OPEN_NETS")
        placement_blocking_reasons.append("The selected variant still has projected open nets.")
    if selected_variant and any(route.get("crosses_keepout") for route in selected_variant.get("projected_routes", [])):
        placement_blocking_codes.append("BLOCKED_PROJECTED_KEEP_OUT_CROSSING")
        placement_blocking_reasons.append("The selected variant projects one or more keepout crossings.")
    if selected_score and selected_score["status"] != "PASS":
        placement_blocking_codes.append("BLOCKED_SELECTED_VARIANT_NOT_PASS")
        placement_blocking_reasons.append(f"The selected variant status is {selected_score['status']}, not PASS.")

    routing_blocking_codes = list(placement_blocking_codes)
    routing_blocking_reasons = list(placement_blocking_reasons)
    if int(live["unconnected_count"]) > 0 or int(live["detectable_unrouted_net_count"]) > 0:
        routing_blocking_codes.append("BLOCKED_LIVE_OPEN_NETS")
        routing_blocking_reasons.append(
            "The live board already proves open-net work remains: "
            f"{live['unconnected_count']} unconnected items and {live['detectable_unrouted_net_count']} detectable unrouted nets."
        )

    placement_gate_status = "PASS" if not placement_blocking_codes else "BLOCKED"
    routing_gate_status = "PASS" if not routing_blocking_codes else "BLOCKED"
    gate_status = routing_gate_status
    return {
        "project": twin["project"],
        "generated_at": iso_now(),
        "placement_gate_status": placement_gate_status,
        "placement_blocking_codes": placement_blocking_codes,
        "placement_blocking_reasons": placement_blocking_reasons,
        "routing_gate_status": routing_gate_status,
        "routing_blocking_codes": routing_blocking_codes,
        "routing_blocking_reasons": routing_blocking_reasons,
        "gate_status": gate_status,
        "blocking_codes": routing_blocking_codes,
        "blocking_reasons": routing_blocking_reasons,
        "variant_count": len(variants),
        "passing_variant_count": int(comparison["passing_variant_count"]),
        "selected_variant_id": selected_variant_id,
        "selected_variant_status": selected_score["status"] if selected_score else None,
        "live_board_context": twin["live_board_context"],
        "artifacts": artifact_paths,
    }


def gate_markdown(result: dict[str, Any], comparison: dict[str, Any]) -> str:
    lines = [
        "# PCB Prelayout Gate Result",
        "",
        f"Generated: `{result['generated_at']}`",
        "",
        f"Project: `{result['project']}`",
        f"Placement start gate: `{result['placement_gate_status']}`",
        f"Routing continuation gate: `{result['routing_gate_status']}`",
        f"Overall gate status: `{result['gate_status']}`",
        f"Variant count: `{result['variant_count']}`",
        f"Passing variant count: `{result['passing_variant_count']}`",
        f"Selected variant: `{result['selected_variant_id']}`",
        f"Selected status: `{result['selected_variant_status']}`",
        "",
        "## Live Board Context",
        "",
        f"- DRC result: `{result['live_board_context']['drc_result']}`",
        f"- Violations: `{result['live_board_context']['violation_count']}`",
        f"- Unconnected items: `{result['live_board_context']['unconnected_count']}`",
        f"- Detectable unrouted nets: `{result['live_board_context']['detectable_unrouted_net_count']}`",
        "",
        "## Ranking",
        "",
        "| Variant | Status | Total Score | Projected Open Nets |",
        "| --- | --- | --- | --- |",
    ]
    for score in comparison["ranked_scores"]:
        lines.append(
            f"| `{score['variant_id']}` | `{score['status']}` | `{score['total_score']}` | "
            f"`{score['projected_open_nets_count']}` |"
        )
    lines.extend(["", "## Placement Gate Blocking Reasons", ""])
    if result["placement_blocking_reasons"]:
        for reason in result["placement_blocking_reasons"]:
            lines.append(f"- {reason}")
    else:
        lines.append("- None.")
    lines.extend(["", "## Routing Gate Blocking Reasons", ""])
    if result["routing_blocking_reasons"]:
        for reason in result["routing_blocking_reasons"]:
            lines.append(f"- {reason}")
    else:
        lines.append("- None.")
    lines.append("")
    return "\n".join(lines)


def run_gate(project_path: str | Path, output_dir: str | Path) -> dict[str, Any]:
    project = locate_project(project_path)
    output_root = Path(output_dir)
    output_root.mkdir(parents=True, exist_ok=True)

    twin = extract_board_digital_twin(project)
    twin_json = output_root / "digital_twin.json"
    twin_md = output_root / "digital_twin.md"
    dump_json(twin_json, twin)
    dump_markdown(twin_md, twin_markdown(twin))

    variants_dir = output_root / "variants"
    variants_dir.mkdir(parents=True, exist_ok=True)
    scores_dir = output_root / "scores"
    scores_dir.mkdir(parents=True, exist_ok=True)
    previews_dir = output_root / "previews"
    previews_dir.mkdir(parents=True, exist_ok=True)

    variants = generate_placement_variants(twin)
    dump_markdown(output_root / "variants.md", variants_markdown(variants))
    final_variants: list[dict[str, Any]] = []
    score_payloads: list[dict[str, Any]] = []
    variant_files: list[str] = []
    score_files: list[str] = []

    for variant in variants:
        projected = project_variant_routes(twin, variant)
        variant_json = variants_dir / f"{variant['variant_id'].lower()}.json"
        variant_md = variants_dir / f"{variant['variant_id'].lower()}.md"
        dump_json(variant_json, projected)
        dump_markdown(variant_md, projection_markdown(projected))
        final_variants.append(projected)
        variant_files.append(repo_rel(variant_json))

        score = score_variant(projected)
        score_json = scores_dir / f"{variant['variant_id'].lower()}.score.json"
        score_md = scores_dir / f"{variant['variant_id'].lower()}.score.md"
        dump_json(score_json, score)
        dump_markdown(score_md, score_markdown(score))
        score_payloads.append(score)
        score_files.append(repo_rel(score_json))

        preview_svg = previews_dir / f"{variant['variant_id'].lower()}.svg"
        preview_md = previews_dir / f"{variant['variant_id'].lower()}.md"
        preview_svg.write_text(render_svg(projected) + "\n", encoding="utf-8")
        dump_markdown(preview_md, f"# {variant['variant_id']} Preview\n\nSVG: `{repo_rel(preview_svg)}`\n")

    comparison = compare_variant_scores(score_payloads)
    comparison_json = output_root / "variant_comparison.json"
    comparison_md = output_root / "variant_comparison.md"
    dump_json(comparison_json, comparison)
    dump_markdown(comparison_md, gate_markdown(
        evaluate_prelayout_gate(
            twin,
            final_variants,
            score_payloads,
            comparison,
            {
                "digital_twin_json": repo_rel(twin_json),
                "variant_files": variant_files,
                "score_files": score_files,
                "comparison_json": repo_rel(comparison_json),
            },
        ),
        comparison,
    ))

    artifact_paths = {
        "digital_twin_json": repo_rel(twin_json),
        "variant_files": variant_files,
        "score_files": score_files,
        "comparison_json": repo_rel(comparison_json),
    }
    result = evaluate_prelayout_gate(twin, final_variants, score_payloads, comparison, artifact_paths)
    result_json = output_root / "prelayout_gate_result.json"
    result_md = output_root / "prelayout_gate_result.md"
    dump_json(result_json, result)
    dump_markdown(result_md, gate_markdown(result, comparison))
    return result


def default_output_dir(project_path: str | Path) -> Path:
    project = locate_project(project_path)
    return project / "reports" / "prelayout_engine" / timestamp_slug()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, help="Active project path.")
    parser.add_argument("--output-dir", help="Optional output directory.")
    parser.add_argument(
        "--fail-on-blocked",
        action="store_true",
        help="Return non-zero when the gate result is BLOCKED.",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir) if args.output_dir else default_output_dir(args.project)
    result = run_gate(args.project, output_dir)
    print(f"PRELAYOUT_GATE_STATUS: {result['gate_status']}")
    print(f"PRELAYOUT_PLACEMENT_GATE_STATUS: {result['placement_gate_status']}")
    print(f"PRELAYOUT_ROUTING_GATE_STATUS: {result['routing_gate_status']}")
    print(f"PRELAYOUT_VARIANT_COUNT: {result['variant_count']}")
    print(f"PRELAYOUT_PASSING_VARIANTS: {result['passing_variant_count']}")
    print(f"PRELAYOUT_SELECTED_VARIANT: {result['selected_variant_id']}")
    print(f"PRELAYOUT_RESULT_JSON: {repo_rel(output_dir / 'prelayout_gate_result.json')}")
    if args.fail_on_blocked and result["gate_status"] != "PASS":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
