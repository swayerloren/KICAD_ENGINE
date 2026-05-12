#!/usr/bin/env python3
"""Shared read-only helpers for mechanical orientation truth audits."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = next(
    (path for path in [SCRIPT_DIR, *SCRIPT_DIR.parents] if (path / "AGENTS.md").exists()),
    SCRIPT_DIR,
)
PLACEMENT_SCRIPTS = REPO_ROOT / "14_LAYOUT_AUTOMATION" / "scripts"
if str(PLACEMENT_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(PLACEMENT_SCRIPTS))

from _placement_common import (  # type: ignore  # noqa: E402
    EDGE_CONNECTOR_MAX_EDGE_DISTANCE_MM,
    build_live_placement_state,
    nearest_board_edge,
)


ORIENTATION_DB = REPO_ROOT / "08_COMPONENT_DATABASE" / "mechanical_orientation" / "connector_orientation_truth.json"
ROTATION_ORDER = ["bottom", "left", "top", "right"]
CONNECTOR_FAMILIES = {"USB_C", "BARREL_JACK", "EDGE_CONNECTOR"}


def load_json(path: str | Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def dump_json(path: str | Path, payload: Any) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def dump_markdown(path: str | Path, text: str) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text.rstrip() + "\n", encoding="utf-8")


def repo_rel(path: str | Path) -> str:
    candidate = Path(path).resolve()
    try:
        return str(candidate.relative_to(REPO_ROOT.resolve())).replace("\\", "/")
    except ValueError:
        return str(candidate).replace("\\", "/")


def locate_project(project_or_pcb: str | Path) -> Path:
    candidate = Path(project_or_pcb)
    if candidate.is_absolute():
        return candidate.resolve()
    return (REPO_ROOT / candidate).resolve()


def locate_pcb(project_or_pcb: str | Path) -> Path:
    candidate = locate_project(project_or_pcb)
    if candidate.is_file() and candidate.suffix == ".kicad_pcb":
        return candidate
    candidates = [
        candidate / "kicad" / f"{candidate.name}.kicad_pcb",
        candidate / f"{candidate.name}.kicad_pcb",
    ]
    for path in candidates:
        if path.exists():
            return path.resolve()
    matches = sorted(candidate.glob("**/*.kicad_pcb"))
    if matches:
        return matches[0].resolve()
    raise FileNotFoundError(f"No .kicad_pcb found under {candidate}")


def load_truth_catalog() -> dict[str, Any]:
    return load_json(ORIENTATION_DB)


def normalize_direction(value: str | None) -> str:
    if value is None:
        return "off_board_unknown"
    lowered = str(value).strip().lower()
    return lowered if lowered in {"top", "bottom", "left", "right"} else "off_board_unknown"


def rotate_direction(zero_direction: str | None, rotation_deg: float) -> str:
    base = normalize_direction(zero_direction)
    if base == "off_board_unknown":
        return base
    steps = (int(round(float(rotation_deg))) % 360) // 90
    index = ROTATION_ORDER.index(base)
    return ROTATION_ORDER[(index + steps) % len(ROTATION_ORDER)]


def inward_direction(edge: str | None) -> str:
    mapping = {
        "top": "bottom",
        "bottom": "top",
        "left": "right",
        "right": "left",
    }
    return mapping.get(normalize_direction(edge), "off_board_unknown")


def truth_status_rank(status: str) -> int:
    order = {"PASS": 0, "NEEDS_HUMAN_REVIEW": 1, "FAIL": 2, "NOT_APPLICABLE": 3}
    return order.get(status, 99)


def connector_family(component: dict[str, Any]) -> str | None:
    role = str(component.get("role") or "").upper()
    if role in CONNECTOR_FAMILIES:
        return role
    footprint = str(component.get("footprint_name") or "").upper()
    value = str(component.get("value") or "").upper()
    ref = str(component.get("ref") or "").upper()
    if "USB_C" in footprint or "USB-C" in value:
        return "USB_C"
    if "BARREL" in footprint or "JACK_5V" in value:
        return "BARREL_JACK"
    if ref.startswith("J"):
        return "EDGE_CONNECTOR"
    return None


def matched_family_rule(component: dict[str, Any], catalog: dict[str, Any]) -> tuple[str | None, dict[str, Any] | None]:
    family = connector_family(component)
    if not family:
        return None, None
    config = (catalog.get("rule_families") or {}).get(family)
    if not isinstance(config, dict):
        return family, None
    footprint_name = str(component.get("footprint_name") or "")
    value = str(component.get("value") or "")
    ref = str(component.get("ref") or "")
    haystacks = [footprint_name.lower(), value.lower(), ref.lower()]
    for rule in config.get("specific_footprints", []):
        tokens = [str(token).lower() for token in rule.get("match_any", [])]
        if tokens and any(token in haystack for haystack in haystacks for token in tokens):
            return family, rule
    return family, config.get("default_rule")


def build_connector_truth_record(
    component: dict[str, Any],
    catalog: dict[str, Any],
    intended_edge: str | None = None,
) -> dict[str, Any]:
    family, rule = matched_family_rule(component, catalog)
    edge = normalize_direction(intended_edge or component.get("edge_proximity", {}).get("edge"))
    distance_mm = round(float(component.get("edge_proximity", {}).get("distance_mm", 999.0)), 6)
    edge_alignment_verified = distance_mm <= EDGE_CONNECTOR_MAX_EDGE_DISTANCE_MM
    rotation_deg = float(component.get("rotation_deg", 0.0))
    proof_sources: list[str] = []
    missing_evidence: list[str] = []
    conflicts: list[str] = []

    if component.get("body_bbox") or component.get("courtyard_bbox"):
        proof_sources.append("component_geometry")
    if component.get("model_paths"):
        proof_sources.append("3d_model_reference")
    if component.get("has_resolved_3d_model"):
        proof_sources.append("3d_model_resolved")
    if rule:
        proof_sources.append("mechanical_truth_catalog")

    port_opening_direction = "off_board_unknown"
    pin_side_direction = "off_board_unknown"
    body_side_direction = "off_board_unknown"
    pcb_edge_marker_direction = "off_board_unknown"
    off_board_facing = False

    if not rule:
        missing_evidence.append("No matched orientation rule exists for this connector footprint.")
    else:
        zero = rule.get("zero_deg", {})
        port_opening_direction = rotate_direction(zero.get("port_opening_direction"), rotation_deg)
        pin_side_direction = rotate_direction(zero.get("pin_side_direction"), rotation_deg)
        body_side_direction = rotate_direction(zero.get("body_side_direction"), rotation_deg)
        pcb_edge_marker_direction = rotate_direction(zero.get("pcb_edge_marker_direction"), rotation_deg)
        off_board_facing = port_opening_direction == edge

        if port_opening_direction != edge:
            conflicts.append("Port opening does not face the intended board edge.")
        if pin_side_direction == edge:
            conflicts.append("Pin/solder side is facing the board edge instead of the port opening.")
        if pcb_edge_marker_direction != "off_board_unknown" and pcb_edge_marker_direction != edge:
            conflicts.append("Footprint PCB-edge direction does not align with the board edge.")
        if not edge_alignment_verified:
            conflicts.append("Connector body is not aligned tightly enough to the intended board edge.")

    if not component.get("has_3d_model_reference"):
        missing_evidence.append("No 3D model reference is present in the live PCB footprint.")
    elif not component.get("has_resolved_3d_model"):
        missing_evidence.append("3D model reference exists but the model file is missing or unresolved.")

    hard_rule_hits: list[str] = []
    if conflicts:
        hard_rule_hits.append("CONNECTOR_DIRECTION_FAIL")
    if missing_evidence:
        hard_rule_hits.append("CONNECTOR_ORIENTATION_NEEDS_HUMAN_REVIEW")

    if conflicts:
        truth_status = "FAIL"
    elif missing_evidence:
        truth_status = "NEEDS_HUMAN_REVIEW"
    else:
        truth_status = "PASS"

    notes = rule.get("notes", "") if isinstance(rule, dict) else ""
    return {
        "ref": str(component.get("ref", "")),
        "connector_type": family or "CONNECTOR",
        "intended_edge": edge,
        "mating_direction": port_opening_direction,
        "rotation_deg": rotation_deg,
        "truth_status": truth_status,
        "off_board_facing": off_board_facing,
        "edge_alignment_required": True,
        "edge_alignment_verified": edge_alignment_verified,
        "distance_to_edge_mm": distance_mm,
        "mechanical_conflicts": conflicts,
        "proof_sources": proof_sources,
        "notes": notes,
        "port_opening_direction": port_opening_direction,
        "pin_side_direction": pin_side_direction,
        "body_side_direction": body_side_direction,
        "pcb_edge_marker_direction": pcb_edge_marker_direction,
        "three_d_model_status": (
            "MODEL_PRESENT"
            if component.get("has_resolved_3d_model")
            else "MODEL_REFERENCE_MISSING"
            if not component.get("has_3d_model_reference")
            else "MODEL_FILE_MISSING_OR_UNRESOLVED"
        ),
        "missing_evidence": missing_evidence,
        "routing_blocked": truth_status != "PASS",
        "hard_rule_hits": hard_rule_hits,
        "footprint_rule_id": str((rule or {}).get("rule_id", "")),
    }


def audit_connector_state(
    state: dict[str, Any],
    catalog: dict[str, Any],
    family_filter: str | None = None,
) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    for component in state.get("components", []):
        family = connector_family(component)
        if not family:
            continue
        if family_filter and family != family_filter:
            continue
        records.append(build_connector_truth_record(component, catalog))

    statuses = [record["truth_status"] for record in records]
    if any(status == "FAIL" for status in statuses):
        overall = "FAIL"
    elif any(status == "NEEDS_HUMAN_REVIEW" for status in statuses):
        overall = "NEEDS_HUMAN_REVIEW"
    else:
        overall = "PASS" if records else "NOT_APPLICABLE"

    return {
        "project": state["project"],
        "source_pcb": state["source_pcb"],
        "audit_scope": family_filter or "ALL_CONNECTORS",
        "status": overall,
        "routing_blocked": overall != "PASS",
        "records": sorted(records, key=lambda item: (truth_status_rank(item["truth_status"]), item["ref"])),
    }


def audit_esp32_antenna_state(state: dict[str, Any], catalog: dict[str, Any]) -> dict[str, Any]:
    rf_modules = [
        component
        for component in state.get("components", [])
        if str(component.get("role") or "").upper() == "RF_MODULE"
        and "ESP32" in str(component.get("value") or "").upper() + " " + str(component.get("footprint_name") or "").upper()
    ]
    board_bbox = state.get("board", {}).get("bbox", {})
    records: list[dict[str, Any]] = []
    for component in rf_modules:
        antenna = component.get("antenna_keepout")
        proof_sources = ["component_geometry"]
        missing_evidence: list[str] = []
        conflicts: list[str] = []
        if component.get("has_resolved_3d_model"):
            proof_sources.append("3d_model_resolved")
        family_config = (catalog.get("rule_families") or {}).get("ESP32_MODULE_ANTENNA", {})
        if family_config:
            proof_sources.append("mechanical_truth_catalog")
        if not antenna or antenna.get("status") != "INFERRED" or not isinstance(antenna.get("bbox"), dict):
            missing_evidence.append("ESP32 antenna keepout could not be inferred from live footprint geometry.")
            actual_direction = "off_board_unknown"
            outward_edge = "off_board_unknown"
            keepout_edge_distance = 999.0
        else:
            actual_direction = normalize_direction(antenna.get("side"))
            keepout_edge = nearest_board_edge(board_bbox, antenna["bbox"])
            outward_edge = normalize_direction(keepout_edge.get("edge"))
            keepout_edge_distance = round(float(keepout_edge.get("distance_mm", 999.0)), 6)
            if actual_direction != outward_edge:
                conflicts.append("ESP32 antenna keepout does not face outward toward the board edge.")
            if keepout_edge_distance > EDGE_CONNECTOR_MAX_EDGE_DISTANCE_MM:
                conflicts.append("ESP32 antenna keepout is too far from the board edge to be treated as outward-facing.")

        if conflicts:
            status = "FAIL"
        elif missing_evidence:
            status = "NEEDS_HUMAN_REVIEW"
        else:
            status = "PASS"

        records.append(
            {
                "ref": str(component.get("ref", "")),
                "component_type": "ESP32_MODULE_ANTENNA",
                "truth_status": status,
                "keepout_direction": actual_direction,
                "outward_edge": outward_edge,
                "keepout_edge_distance_mm": keepout_edge_distance,
                "proof_sources": proof_sources,
                "missing_evidence": missing_evidence,
                "mechanical_conflicts": conflicts,
                "routing_blocked": status != "PASS",
            }
        )

    statuses = [record["truth_status"] for record in records]
    if any(status == "FAIL" for status in statuses):
        overall = "FAIL"
    elif any(status == "NEEDS_HUMAN_REVIEW" for status in statuses):
        overall = "NEEDS_HUMAN_REVIEW"
    else:
        overall = "PASS" if records else "NOT_APPLICABLE"

    return {
        "project": state["project"],
        "source_pcb": state["source_pcb"],
        "audit_scope": "ESP32_MODULE_ANTENNA",
        "status": overall,
        "routing_blocked": overall != "PASS",
        "records": records,
    }


def connector_markdown(result: dict[str, Any]) -> str:
    lines = [
        "# Connector Orientation Audit",
        "",
        f"Project: `{result['project']}`",
        f"Source PCB: `{repo_rel(result['source_pcb'])}`",
        f"Scope: `{result['audit_scope']}`",
        f"Status: `{result['status']}`",
        f"Routing blocked: `{result['routing_blocked']}`",
        "",
        "| Ref | Type | Edge | Port Opening | Pin Side | 3D Model | Status |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    if not result["records"]:
        lines.append("| `_none_` | `_n/a_` | `_n/a_` | `_n/a_` | `_n/a_` | `_n/a_` | `NOT_APPLICABLE` |")
    for record in result["records"]:
        lines.append(
            f"| `{record['ref']}` | `{record['connector_type']}` | `{record['intended_edge']}` | "
            f"`{record['port_opening_direction']}` | `{record['pin_side_direction']}` | "
            f"`{record['three_d_model_status']}` | `{record['truth_status']}` |"
        )
    lines.extend(["", "## Findings", ""])
    for record in result["records"]:
        if not record["mechanical_conflicts"] and not record["missing_evidence"]:
            continue
        lines.append(f"- `{record['ref']}` `{record['truth_status']}`")
        for reason in record["mechanical_conflicts"]:
            lines.append(f"  - Conflict: {reason}")
        for reason in record["missing_evidence"]:
            lines.append(f"  - Missing evidence: {reason}")
    if not any(record["mechanical_conflicts"] or record["missing_evidence"] for record in result["records"]):
        lines.append("- None.")
    lines.append("")
    return "\n".join(lines)


def antenna_markdown(result: dict[str, Any]) -> str:
    lines = [
        "# ESP32 Antenna Orientation Audit",
        "",
        f"Project: `{result['project']}`",
        f"Source PCB: `{repo_rel(result['source_pcb'])}`",
        f"Status: `{result['status']}`",
        f"Routing blocked: `{result['routing_blocked']}`",
        "",
        "| Ref | Keepout Direction | Outward Edge | Distance | Status |",
        "| --- | --- | --- | --- | --- |",
    ]
    if not result["records"]:
        lines.append("| `_none_` | `_n/a_` | `_n/a_` | `_n/a_` | `NOT_APPLICABLE` |")
    for record in result["records"]:
        lines.append(
            f"| `{record['ref']}` | `{record['keepout_direction']}` | `{record['outward_edge']}` | "
            f"`{record['keepout_edge_distance_mm']}` | `{record['truth_status']}` |"
        )
    lines.extend(["", "## Findings", ""])
    for record in result["records"]:
        if not record["mechanical_conflicts"] and not record["missing_evidence"]:
            continue
        lines.append(f"- `{record['ref']}` `{record['truth_status']}`")
        for reason in record["mechanical_conflicts"]:
            lines.append(f"  - Conflict: {reason}")
        for reason in record["missing_evidence"]:
            lines.append(f"  - Missing evidence: {reason}")
    if not any(record["mechanical_conflicts"] or record["missing_evidence"] for record in result["records"]):
        lines.append("- None.")
    lines.append("")
    return "\n".join(lines)
