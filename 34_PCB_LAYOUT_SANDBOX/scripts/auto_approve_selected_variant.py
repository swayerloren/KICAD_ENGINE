#!/usr/bin/env python3
"""Approve or block the selected PCB layout variant from objective evidence."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


JSON_BLOCK_RE = re.compile(r"```json\s*(\{.*?\})\s*```", re.DOTALL | re.IGNORECASE)

REQUIRED_CONTEXT_FIELDS = (
    "schematic_gate_pass",
    "erc_pass",
    "kicad_native_annotation_verified",
    "all_physical_components_have_footprints",
    "high_risk_footprints_exact_or_safe_candidate",
    "connector_orientation_known",
    "board_shape_and_dimensions_defined",
    "antenna_keepout_defined_if_required",
    "variant_count_at_least_three",
    "variant_scorecard_exists",
    "routing_feasibility_pass",
    "no_drc_precheck_blocker",
)


def load_payload(path: str | Path) -> dict[str, Any]:
    payload_path = Path(path)
    text = payload_path.read_text(encoding="utf-8")
    if payload_path.suffix.lower() == ".json":
        return json.loads(text)
    match = JSON_BLOCK_RE.search(text)
    if match:
        return json.loads(match.group(1))
    stripped = text.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        return json.loads(stripped)
    raise ValueError(f"No JSON payload found in {payload_path}")


def _text_report(payload: dict[str, Any]) -> str:
    lines = [
        f"Project: {payload['project']}",
        f"Selected variant: {payload['selected_variant_id']}",
        f"Selection status: {payload['selection_status']}",
        f"Auto approval status: {payload['auto_approval_status']}",
    ]
    if payload["blocking_reasons"]:
        lines.append("")
        lines.append("Blocking Reasons:")
        lines.extend(f"- {item}" for item in payload["blocking_reasons"])
    else:
        lines.append("")
        lines.append("Blocking Reasons: none")
    return "\n".join(lines)


def auto_approve(selection: dict[str, Any], context: dict[str, Any]) -> dict[str, Any]:
    missing_fields: list[str] = []
    invalid_fields: list[str] = []

    project = context.get("project")
    if not isinstance(project, str) or not project.strip():
        raise ValueError("Context field 'project' must be a non-empty string.")

    selected_variant_id = selection.get("selected_variant_id")
    selection_status = selection.get("selection_status")
    selected_variant_status = selection.get("selected_variant_status")

    if selection_status != "AUTO_SELECTED":
        auto_status = "AUTO_BLOCKED_BAD_LAYOUT"
        reasons = ["No non-failed variant was auto-selected."]
    else:
        def read_bool(name: str) -> bool | None:
            value = context.get(name)
            if value is None:
                missing_fields.append(name)
                return None
            if not isinstance(value, bool):
                invalid_fields.append(name)
                return None
            return value

        flags = {name: read_bool(name) for name in REQUIRED_CONTEXT_FIELDS}

        mechanical_conflict_present = context.get("mechanical_conflict_present")
        if mechanical_conflict_present is None:
            mechanical_conflict_present = False
        elif not isinstance(mechanical_conflict_present, bool):
            invalid_fields.append("mechanical_conflict_present")
            mechanical_conflict_present = False

        antenna_keepout_violation = context.get("antenna_keepout_violation")
        if antenna_keepout_violation is None:
            antenna_keepout_violation = False
        elif not isinstance(antenna_keepout_violation, bool):
            invalid_fields.append("antenna_keepout_violation")
            antenna_keepout_violation = False

        reasons = []
        if missing_fields or invalid_fields:
            auto_status = "AUTO_BLOCKED_MISSING_DATA"
            if missing_fields:
                reasons.append("Missing context fields: " + ", ".join(sorted(set(missing_fields))))
            if invalid_fields:
                reasons.append("Invalid context fields: " + ", ".join(sorted(set(invalid_fields))))
        elif not flags["schematic_gate_pass"] or not flags["erc_pass"] or not flags[
            "kicad_native_annotation_verified"
        ] or not flags["no_drc_precheck_blocker"]:
            auto_status = "AUTO_BLOCKED_DRC_PRECHECK_FAIL"
            reasons.append("Upstream schematic/ERC/precheck evidence is not ready.")
        elif not flags["high_risk_footprints_exact_or_safe_candidate"]:
            auto_status = "AUTO_BLOCKED_HIGH_RISK_FOOTPRINT_UNVERIFIED"
            reasons.append("High-risk footprints are not exact-verified or safe-candidate documented.")
        elif antenna_keepout_violation:
            auto_status = "AUTO_BLOCKED_ANTENNA_KEEPOUT_VIOLATION"
            reasons.append("Selected variant violates the antenna keepout.")
        elif not flags["connector_orientation_known"]:
            auto_status = "AUTO_BLOCKED_CONNECTOR_ORIENTATION_UNKNOWN"
            reasons.append("Connector orientation is still unknown.")
        elif mechanical_conflict_present or not flags["board_shape_and_dimensions_defined"]:
            auto_status = "AUTO_BLOCKED_MECHANICAL_CONFLICT"
            reasons.append("Mechanical shape or dimension evidence is not resolved.")
        elif not flags["routing_feasibility_pass"]:
            auto_status = "AUTO_BLOCKED_ROUTING_FEASIBILITY_FAIL"
            reasons.append("Routing-feasibility evidence does not pass.")
        elif (
            not flags["all_physical_components_have_footprints"]
            or not flags["antenna_keepout_defined_if_required"]
            or not flags["variant_count_at_least_three"]
            or not flags["variant_scorecard_exists"]
        ):
            auto_status = "AUTO_BLOCKED_MISSING_DATA"
            reasons.append("Required sandbox evidence is incomplete.")
        elif selected_variant_status != "PASS":
            auto_status = "AUTO_BLOCKED_BAD_LAYOUT"
            reasons.append(
                f"Selected variant status is {selected_variant_status}, not PASS."
            )
        else:
            auto_status = "AUTO_APPROVED_FOR_PCB_WORK"

    return {
        "project": project,
        "selected_variant_id": selected_variant_id,
        "selection_status": selection_status,
        "selected_variant_status": selected_variant_status,
        "auto_approval_status": auto_status,
        "blocking_reasons": reasons,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "selection_file",
        help="JSON or Markdown file produced by auto_select_best_variant.py or compare_layout_variants.py.",
    )
    parser.add_argument(
        "approval_context_file",
        help="JSON or Markdown file with approval-context booleans.",
    )
    parser.add_argument(
        "--format",
        choices=("json", "text"),
        default="text",
        help="Output format.",
    )
    parser.add_argument("--output", help="Optional output file path.")
    args = parser.parse_args()

    try:
        selection = load_payload(args.selection_file)
        context = load_payload(args.approval_context_file)
        payload = auto_approve(selection, context)
    except Exception as exc:  # pragma: no cover
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    rendered = (
        json.dumps(payload, indent=2, sort_keys=True)
        if args.format == "json"
        else _text_report(payload)
    )

    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
