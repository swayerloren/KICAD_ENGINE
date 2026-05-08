#!/usr/bin/env python3
"""Score one PCB layout variant from JSON or Markdown with fenced JSON."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


CATEGORY_LIMITS = {
    "mechanical_correctness": 20,
    "connector_orientation_correctness": 20,
    "antenna_rf_keepout_correctness": 15,
    "power_path_quality": 15,
    "usb_data_routing_quality": 10,
    "component_grouping_quality": 10,
    "routing_feasibility": 10,
}

DCR_PRECHECK_RISK_PENALTIES = {
    "NONE": 0,
    "LOW": 3,
    "MEDIUM": 6,
    "HIGH": 10,
    "BLOCKER": 15,
}

HUMAN_UNCERTAINTY_RISK_PENALTIES = {
    "NONE": 0,
    "LOW": 2,
    "MEDIUM": 5,
    "HIGH": 10,
    "BLOCKER": 15,
}

PASS_THRESHOLD = 80
JSON_BLOCK_RE = re.compile(r"```json\s*(\{.*?\})\s*```", re.DOTALL | re.IGNORECASE)

BOOL_FIELDS = (
    "required_connectors_present",
    "connector_orientation_known",
    "usb_c_required",
    "usb_c_on_intended_edge",
    "usb_c_facing_correctly",
    "input_connector_required",
    "input_connector_present",
    "input_connector_facing_correctly",
    "barrel_jack_required",
    "barrel_jack_placed",
    "barrel_jack_facing_correctly",
    "esp32_rf_module_present",
    "antenna_keepout_defined_if_required",
    "esp32_antenna_keepout_blocked",
    "mounting_holes_required",
    "mounting_holes_present",
    "board_shape_defined",
    "board_dimensions_known",
    "board_dimensions_guessed_without_source",
    "all_footprints_assigned",
    "high_risk_footprint_exact_package_evidence",
    "high_risk_footprint_safe_candidate_documented",
    "routing_projection_crosses_antenna_keepout",
    "power_path_order_sensible",
    "routing_feasibility_impossible",
    "drc_precheck_pass",
)

STRING_FIELDS = (
    "project",
    "variant_id",
    "drc_precheck_risk_level",
    "human_uncertainty_risk_level",
)


def _is_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def load_variant_file(path: str | Path) -> dict[str, Any]:
    variant_path = Path(path)
    text = variant_path.read_text(encoding="utf-8")
    if variant_path.suffix.lower() == ".json":
        return json.loads(text)
    match = JSON_BLOCK_RE.search(text)
    if match:
        return json.loads(match.group(1))
    stripped = text.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        return json.loads(stripped)
    raise ValueError(f"No JSON payload found in {variant_path}")


def _get_required_string(
    data: dict[str, Any],
    key: str,
    missing_fields: list[str],
    invalid_fields: list[str],
) -> str:
    value = data.get(key)
    if value is None:
        missing_fields.append(key)
        return ""
    if not isinstance(value, str) or not value.strip():
        invalid_fields.append(key)
        return ""
    return value.strip()


def _get_required_bool(
    data: dict[str, Any],
    key: str,
    missing_fields: list[str],
    invalid_fields: list[str],
) -> bool | None:
    value = data.get(key)
    if value is None:
        missing_fields.append(key)
        return None
    if not isinstance(value, bool):
        invalid_fields.append(key)
        return None
    return value


def _get_required_score(
    data: dict[str, Any],
    key: str,
    maximum: int,
    missing_fields: list[str],
    invalid_fields: list[str],
) -> int:
    value = data.get(key)
    if value is None:
        missing_fields.append(key)
        return 0
    if not _is_int(value) or value < 0 or value > maximum:
        invalid_fields.append(key)
        return 0
    return value


def _get_risk_level(
    data: dict[str, Any],
    key: str,
    allowed: dict[str, int],
    missing_fields: list[str],
    invalid_fields: list[str],
) -> str:
    value = data.get(key)
    if value is None:
        missing_fields.append(key)
        return "BLOCKER"
    if not isinstance(value, str):
        invalid_fields.append(key)
        return "BLOCKER"
    normalized = value.strip().upper()
    if normalized not in allowed:
        invalid_fields.append(key)
        return "BLOCKER"
    return normalized


def score_variant(data: dict[str, Any], source: str = "") -> dict[str, Any]:
    missing_fields: list[str] = []
    invalid_fields: list[str] = []

    project = _get_required_string(data, "project", missing_fields, invalid_fields)
    variant_id = _get_required_string(data, "variant_id", missing_fields, invalid_fields)

    category_scores = {
        key: _get_required_score(data, key, maximum, missing_fields, invalid_fields)
        for key, maximum in CATEGORY_LIMITS.items()
    }

    bools = {
        key: _get_required_bool(data, key, missing_fields, invalid_fields)
        for key in BOOL_FIELDS
    }

    drc_precheck_risk_level = _get_risk_level(
        data,
        "drc_precheck_risk_level",
        DCR_PRECHECK_RISK_PENALTIES,
        missing_fields,
        invalid_fields,
    )
    human_uncertainty_risk_level = _get_risk_level(
        data,
        "human_uncertainty_risk_level",
        HUMAN_UNCERTAINTY_RISK_PENALTIES,
        missing_fields,
        invalid_fields,
    )

    notes = str(data.get("notes", "")).strip()
    uncertainty_notes = str(data.get("uncertainty_notes", "")).strip()

    category_subtotal = sum(category_scores.values())
    drc_precheck_risk_penalty = DCR_PRECHECK_RISK_PENALTIES[drc_precheck_risk_level]
    human_uncertainty_risk_penalty = HUMAN_UNCERTAINTY_RISK_PENALTIES[
        human_uncertainty_risk_level
    ]
    total_penalty = drc_precheck_risk_penalty + human_uncertainty_risk_penalty
    total_score = max(0, min(100, category_subtotal - total_penalty))

    hard_fails: list[str] = []
    blocked_reasons: list[str] = []

    if missing_fields or invalid_fields:
        if missing_fields:
            blocked_reasons.append(
                "Missing required fields: " + ", ".join(sorted(set(missing_fields)))
            )
        if invalid_fields:
            blocked_reasons.append(
                "Invalid required fields: " + ", ".join(sorted(set(invalid_fields)))
            )

    def flag(name: str) -> bool:
        return bools[name] is True

    def false_or_missing(name: str) -> bool:
        return bools[name] is not True

    if flag("required_connectors_present") is False:
        hard_fails.append("Required connector missing.")
    if flag("usb_c_required") and false_or_missing("usb_c_on_intended_edge"):
        hard_fails.append("USB-C is not edge-facing when required.")
    if flag("usb_c_required") and false_or_missing("usb_c_facing_correctly"):
        hard_fails.append("USB-C facing direction is wrong.")
    if flag("input_connector_required") and false_or_missing("input_connector_present"):
        hard_fails.append("Input connector is missing.")
    if flag("input_connector_required") and false_or_missing("input_connector_facing_correctly"):
        hard_fails.append("Input connector facing direction is wrong.")
    if flag("barrel_jack_required") and false_or_missing("barrel_jack_placed"):
        hard_fails.append("Barrel jack is missing when required.")
    if flag("barrel_jack_required") and false_or_missing("barrel_jack_facing_correctly"):
        hard_fails.append("Barrel jack facing direction is wrong.")
    if flag("esp32_rf_module_present") and false_or_missing("antenna_keepout_defined_if_required"):
        blocked_reasons.append("RF module exists but antenna keepout definition is missing.")
    if flag("esp32_antenna_keepout_blocked"):
        hard_fails.append("ESP32 antenna keepout is blocked.")
    if flag("mounting_holes_required") and false_or_missing("mounting_holes_present"):
        hard_fails.append("Mounting holes are missing when required.")
    if false_or_missing("board_shape_defined"):
        blocked_reasons.append("Board shape is not defined.")
    if flag("board_dimensions_guessed_without_source"):
        hard_fails.append("Board dimensions were guessed without source.")
    elif false_or_missing("board_dimensions_known"):
        blocked_reasons.append("Board dimensions are not source-defined.")
    if false_or_missing("all_footprints_assigned"):
        hard_fails.append("A required footprint is missing.")
    if false_or_missing("high_risk_footprint_exact_package_evidence") and false_or_missing(
        "high_risk_footprint_safe_candidate_documented"
    ):
        hard_fails.append(
            "High-risk footprint has no exact package evidence or documented safe candidate."
        )
    if flag("routing_projection_crosses_antenna_keepout"):
        hard_fails.append("Projected traces cross the antenna keepout.")
    if false_or_missing("power_path_order_sensible"):
        hard_fails.append("Power path order is nonsensical.")
    if flag("routing_feasibility_impossible"):
        hard_fails.append("Routing feasibility is impossible.")
    if false_or_missing("drc_precheck_pass"):
        hard_fails.append("DRC/precheck fail.")
    if false_or_missing("connector_orientation_known"):
        blocked_reasons.append("Connector orientation is not fully known.")

    if hard_fails:
        status = "FAIL"
    elif missing_fields or invalid_fields or blocked_reasons:
        status = "AUTO_BLOCKED_MISSING_DATA"
    elif total_score < PASS_THRESHOLD:
        status = "AUTO_BLOCKED_BAD_LAYOUT"
        blocked_reasons.append(
            f"Total score {total_score} is below the PASS threshold {PASS_THRESHOLD}."
        )
    else:
        status = "PASS"

    return {
        "project": project,
        "variant_id": variant_id,
        "source": source,
        "category_scores": category_scores,
        "category_subtotal": category_subtotal,
        "drc_precheck_risk_level": drc_precheck_risk_level,
        "drc_precheck_risk_penalty": drc_precheck_risk_penalty,
        "human_uncertainty_risk_level": human_uncertainty_risk_level,
        "human_uncertainty_risk_penalty": human_uncertainty_risk_penalty,
        "total_penalty": total_penalty,
        "total_score": total_score,
        "status": status,
        "hard_fails": hard_fails,
        "blocked_reasons": blocked_reasons,
        "missing_fields": sorted(set(missing_fields)),
        "invalid_fields": sorted(set(invalid_fields)),
        "eligible_for_selection": status != "FAIL",
        "notes": notes,
        "uncertainty_notes": uncertainty_notes,
    }


def _text_report(result: dict[str, Any]) -> str:
    lines = [
        f"Project: {result['project']}",
        f"Variant: {result['variant_id']}",
    ]
    if result.get("source"):
        lines.append(f"Source: {result['source']}")
    lines.extend(["", "Category Scores:"])
    for key, value in result["category_scores"].items():
        lines.append(f"- {key}: {value}/{CATEGORY_LIMITS[key]}")
    lines.extend(
        [
            "",
            f"Category subtotal: {result['category_subtotal']}",
            f"DRC/precheck risk: {result['drc_precheck_risk_level']} (-{result['drc_precheck_risk_penalty']})",
            f"Human uncertainty risk: {result['human_uncertainty_risk_level']} (-{result['human_uncertainty_risk_penalty']})",
            f"Total penalty: {result['total_penalty']}",
            f"Total score: {result['total_score']}",
            f"Status: {result['status']}",
            f"Eligible for selection: {'YES' if result['eligible_for_selection'] else 'NO'}",
        ]
    )
    if result["hard_fails"]:
        lines.append("")
        lines.append("Hard Fails:")
        lines.extend(f"- {item}" for item in result["hard_fails"])
    if result["blocked_reasons"]:
        lines.append("")
        lines.append("Blocked Reasons:")
        lines.extend(f"- {item}" for item in result["blocked_reasons"])
    if result["missing_fields"]:
        lines.append("")
        lines.append("Missing Fields:")
        lines.extend(f"- {item}" for item in result["missing_fields"])
    if result["invalid_fields"]:
        lines.append("")
        lines.append("Invalid Fields:")
        lines.extend(f"- {item}" for item in result["invalid_fields"])
    if result["notes"]:
        lines.append("")
        lines.append(f"Notes: {result['notes']}")
    if result["uncertainty_notes"]:
        lines.append(f"Uncertainty notes: {result['uncertainty_notes']}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("variant_file", help="JSON file or Markdown file with fenced JSON.")
    parser.add_argument(
        "--format",
        choices=("json", "text"),
        default="text",
        help="Output format.",
    )
    parser.add_argument("--output", help="Optional output file path.")
    args = parser.parse_args()

    try:
        data = load_variant_file(args.variant_file)
        result = score_variant(data, source=str(Path(args.variant_file)))
    except Exception as exc:  # pragma: no cover - CLI error path
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    rendered = (
        json.dumps(result, indent=2, sort_keys=True)
        if args.format == "json"
        else _text_report(result)
    )

    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
