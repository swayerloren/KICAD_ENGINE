#!/usr/bin/env python3
"""Shared helpers for the enforceable read-only PCB quality gate."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = next((path for path in [SCRIPT_DIR, *SCRIPT_DIR.parents] if (path / "AGENTS.md").exists()), SCRIPT_DIR)
PCB_GEOMETRY_DIR = REPO_ROOT / "03_TOOLS" / "scripts" / "pcb_geometry"
MECH_DIR = REPO_ROOT / "03_TOOLS" / "scripts" / "mechanical_orientation"
PROJECT_STATE_DIR = REPO_ROOT / "03_TOOLS" / "scripts" / "project_state"
LAYOUT_SCRIPTS = REPO_ROOT / "14_LAYOUT_AUTOMATION" / "scripts"
for item in (SCRIPT_DIR, PCB_GEOMETRY_DIR, MECH_DIR, PROJECT_STATE_DIR, LAYOUT_SCRIPTS):
    if str(item) not in sys.path:
        sys.path.insert(0, str(item))

from _kicad_pcb_bridge_common import bbox_to_mm, require_pcbnew_for_cli  # type: ignore  # noqa: E402
from _pcb_geometry_common import (  # type: ignore  # noqa: E402
    ACUTE_JOG_FOUND,
    BOARD_EDGE_CROSSING,
    EXCESSIVE_DETOUR_RATIO,
    KEEP_OUT_CROSSING_FOUND,
    PERIMETER_BOX_ROUTE_FOUND,
    RECTANGULAR_LOOP_FOUND,
    RETURN_PATH_SPLIT_RISK,
    RIGHT_ANGLE_FOUND,
    TEST_POINT_STUB_TOO_LONG,
    UNNECESSARY_ZIGZAG_FOUND,
    aggregate_trace_quality_findings,
    build_geometry_payload,
    usb_pair_findings,
)
from _mechanical_orientation_common import (  # type: ignore  # noqa: E402
    audit_connector_state,
    audit_esp32_antenna_state,
    build_live_placement_state,
    load_truth_catalog,
)
from project_state_common import (  # type: ignore  # noqa: E402
    build_live_project_state_data,
    preferred_project_file,
    repo_rel as project_state_repo_rel,
    resolve_project_path,
)


PASS = "PASS"
PASS_FINAL_ROUTING = "PASS_FINAL_ROUTING"
FAIL_DRC = "FAIL_DRC"
FAIL_OPEN_NETS = "FAIL_OPEN_NETS"
FAIL_TRACE_GEOMETRY = "FAIL_TRACE_GEOMETRY"
FAIL_TESTPOINT_TOPOLOGY = "FAIL_TESTPOINT_TOPOLOGY"
FAIL_POWER_WIDTHS = "FAIL_POWER_WIDTHS"
FAIL_USB_ROUTING = "FAIL_USB_ROUTING"
FAIL_CONNECTOR_ORIENTATION = "FAIL_CONNECTOR_ORIENTATION"
FAIL_RF_KEEPOUT = "FAIL_RF_KEEPOUT"
FAIL_ZONE_GND = "FAIL_ZONE_GND"
NEEDS_HUMAN_REVIEW = "NEEDS_HUMAN_REVIEW"

FAIL_PRIORITY = [
    FAIL_DRC,
    FAIL_OPEN_NETS,
    FAIL_TRACE_GEOMETRY,
    FAIL_TESTPOINT_TOPOLOGY,
    FAIL_POWER_WIDTHS,
    FAIL_USB_ROUTING,
    FAIL_CONNECTOR_ORIENTATION,
    FAIL_RF_KEEPOUT,
    FAIL_ZONE_GND,
]


DEFAULT_CONSTRAINTS = {
    "schema_version": "1.0",
    "board_profile": "GENERIC_DEV_BOARD",
    "geometry": {
        "max_detour_ratio": 2.0,
        "max_board_edge_parallel_mm": 20.0,
    },
    "power_nets": [],
    "usb_pairs": [],
    "test_points": {
        "max_stub_mm": 5.0,
        "require_leaf_topology": True,
    },
    "gnd": {
        "required_zone_nets": ["GND"],
        "min_stitching_via_count": 0,
        "require_filled_zones": True,
    },
    "orientation": {
        "connector_refs": [],
        "rf_refs": [],
    },
    "silkscreen": {
        "check_reference_text": True,
        "check_value_text": True,
        "allow_over_pad": False,
        "allow_over_hole": False,
    },
}


def repo_rel(path: str | Path) -> str:
    return project_state_repo_rel(path, REPO_ROOT)


def locate_project(target: str | Path) -> Path:
    path = resolve_project_path(REPO_ROOT, target)
    if path.is_file() and path.suffix.lower() == ".kicad_pcb":
        if path.parent.name.lower() == "kicad":
            return path.parent.parent.resolve()
        return path.parent.resolve()
    return path.resolve()


def locate_pcb(target: str | Path) -> Path:
    project = locate_project(target)
    preferred = preferred_project_file(project, ".kicad_pcb")
    if preferred and preferred.exists():
        return preferred.resolve()
    candidates = sorted(project.glob("kicad/*.kicad_pcb")) + sorted(project.glob("*.kicad_pcb"))
    if candidates:
        return candidates[0].resolve()
    raise FileNotFoundError(f"No .kicad_pcb found under {project}")


def timestamp_slug() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def default_output_dir(project: Path) -> Path:
    return project / "reports" / "pcb_quality_gate" / timestamp_slug()


def write_json(path: str | Path, payload: Any) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def write_markdown(path: str | Path, text: str) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text.rstrip() + "\n", encoding="utf-8")


def load_json(path: str | Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged: dict[str, Any] = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(dict(merged[key]), value)
        else:
            merged[key] = value
    return merged


def default_constraints_path(project: Path) -> Path:
    return project / "config" / "pcb_routing_constraints.yaml"


def template_constraints_path() -> Path:
    return REPO_ROOT / "04_KICAD_PROJECTS" / "_templates" / "pcb_routing_constraints.template.yaml"


def load_constraints(project: Path, config_path: str | Path | None = None) -> tuple[dict[str, Any], Path | None]:
    candidate: Path | None = None
    if config_path:
        candidate = Path(config_path).resolve()
    elif default_constraints_path(project).exists():
        candidate = default_constraints_path(project).resolve()
    elif template_constraints_path().exists():
        candidate = template_constraints_path().resolve()

    payload = dict(DEFAULT_CONSTRAINTS)
    if candidate and candidate.exists():
        text = candidate.read_text(encoding="utf-8")
        try:
            loaded = json.loads(text)
        except json.JSONDecodeError as exc:
            raise SystemExit(
                f"{candidate}: expected JSON-compatible YAML so the repo can parse constraints without extra dependencies. {exc}"
            ) from exc
        if not isinstance(loaded, dict):
            raise SystemExit(f"{candidate}: constraint file must contain a JSON/YAML object at the top level.")
        payload = deep_merge(payload, loaded)
    return payload, candidate


def run_drc_text_report(pcb_path: Path, output_path: Path | None = None) -> dict[str, Any]:
    if output_path is None:
        temp = tempfile.NamedTemporaryFile(prefix="pcb_quality_drc_", suffix=".rpt", delete=False)
        temp_path = Path(temp.name)
        temp.close()
        cleanup = True
    else:
        temp_path = Path(output_path).resolve()
        temp_path.parent.mkdir(parents=True, exist_ok=True)
        cleanup = False

    command = [
        "kicad-cli",
        "pcb",
        "drc",
        "--schematic-parity",
        "--severity-all",
        "--format",
        "report",
        "--output",
        str(temp_path),
        str(pcb_path),
    ]
    try:
        completed = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
    except FileNotFoundError:
        return {
            "runnable": False,
            "returncode": 127,
            "stdout": "",
            "stderr": "kicad-cli not found on PATH",
            "report_path": repo_rel(temp_path),
            "report_text": "",
            "violations": None,
            "unconnected_pads": None,
            "footprint_errors": None,
        }

    report_text = temp_path.read_text(encoding="utf-8", errors="replace") if temp_path.exists() else ""
    violations = parse_count(report_text, r"Found\s+(\d+)\s+DRC violations")
    unconnected_pads = parse_count(report_text, r"Found\s+(\d+)\s+unconnected pads")
    footprint_errors = parse_count(report_text, r"Found\s+(\d+)\s+Footprint errors")
    schematic_parity_issues = parse_count(completed.stdout, r"Found\s+(\d+)\s+schematic parity issues")
    result = {
        "runnable": completed.returncode == 0 and temp_path.exists(),
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "report_path": repo_rel(temp_path),
        "report_text": report_text,
        "violations": violations,
        "unconnected_pads": unconnected_pads,
        "footprint_errors": footprint_errors,
        "schematic_parity_issues": schematic_parity_issues,
    }
    if cleanup:
        try:
            temp_path.unlink(missing_ok=True)
        except OSError:
            pass
    return result


def parse_count(text: str, pattern: str) -> int:
    match = re.search(pattern, text, re.I)
    return int(match.group(1)) if match else 0


def build_context(
    project_or_pcb: str | Path,
    config_path: str | Path | None = None,
    drc_report_path: str | Path | None = None,
) -> dict[str, Any]:
    project = locate_project(project_or_pcb)
    pcb_path = locate_pcb(project_or_pcb)
    constraints, resolved_constraints_path = load_constraints(project, config_path)
    live_state = build_live_project_state_data(project, REPO_ROOT, write_supporting=False)
    geometry_payload = build_geometry_payload(project)
    context = {
        "repo_root": REPO_ROOT,
        "project": project,
        "project_name": project.name,
        "pcb_path": pcb_path,
        "constraints": constraints,
        "constraints_path": resolved_constraints_path,
        "live_state": live_state,
        "geometry_payload": geometry_payload,
        "placement_state": None,
        "connector_audit": None,
        "antenna_audit": None,
        "silkscreen_audit": None,
        "drc_text": None,
        "drc_report_path": Path(drc_report_path).resolve() if drc_report_path else None,
    }
    return context


def ensure_drc_text(context: dict[str, Any]) -> dict[str, Any]:
    if context.get("drc_text") is None:
        context["drc_text"] = run_drc_text_report(context["pcb_path"], context.get("drc_report_path"))
    return context["drc_text"]


def ensure_placement_state(context: dict[str, Any]) -> dict[str, Any]:
    if context.get("placement_state") is None:
        context["placement_state"] = build_live_placement_state(context["pcb_path"])
    return context["placement_state"]


def ensure_orientation_audits(context: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    if context.get("connector_audit") is None or context.get("antenna_audit") is None:
        state = ensure_placement_state(context)
        catalog = load_truth_catalog()
        context["connector_audit"] = audit_connector_state(state, catalog)
        context["antenna_audit"] = audit_esp32_antenna_state(state, catalog)
    return context["connector_audit"], context["antenna_audit"]


def make_result(
    tool: str,
    check_id: str,
    status: str,
    summary: str,
    context: dict[str, Any],
    details: dict[str, Any] | None = None,
    artifacts: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "tool": tool,
        "check_id": check_id,
        "status": status,
        "summary": summary,
        "project": context["project_name"],
        "project_path": repo_rel(context["project"]),
        "board_path": repo_rel(context["pcb_path"]),
        "read_only_mode": True,
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "details": details or {},
        "artifacts": artifacts or {},
    }


def result_to_markdown(title: str, result: dict[str, Any]) -> str:
    lines = [
        f"# {title}",
        "",
        f"- project: `{result.get('project', '')}`",
        f"- status: `{result.get('status', '')}`",
        f"- summary: {result.get('summary', '')}",
        "",
        "## Details",
        "",
        "```json",
        json.dumps(result.get("details", {}), indent=2),
        "```",
    ]
    artifacts = result.get("artifacts", {})
    if artifacts:
        lines.extend(
            [
                "",
                "## Artifacts",
                "",
                "```json",
                json.dumps(artifacts, indent=2),
                "```",
            ]
        )
    return "\n".join(lines) + "\n"


def min_trace_width_for_net(payload: dict[str, Any], net_name: str) -> float | None:
    widths = [
        float(segment.get("width_mm", 0.0))
        for path in payload.get("traces", [])
        if str(path.get("net", "")).strip() == net_name
        for segment in path.get("segments", [])
    ]
    return round(min(widths), 6) if widths else None


def total_trace_length_for_net(payload: dict[str, Any], net_name: str) -> float:
    return round(
        sum(float(path.get("path_length_mm", 0.0) or 0.0) for path in payload.get("traces", []) if str(path.get("net", "")).strip() == net_name),
        6,
    )


def trace_paths_for_net(payload: dict[str, Any], net_name: str) -> list[dict[str, Any]]:
    return [path for path in payload.get("traces", []) if str(path.get("net", "")).strip() == net_name]


def find_trace_quality_findings(payload: dict[str, Any]) -> list[dict[str, Any]]:
    return aggregate_trace_quality_findings(payload)


def evaluate_pcb_drc(context: dict[str, Any]) -> dict[str, Any]:
    drc_text = ensure_drc_text(context)
    live_drc = context["live_state"]["drc"]
    violations = int(drc_text.get("violations") or 0)
    parity_errors = max(
        int(drc_text.get("schematic_parity_issues") or 0),
        int(drc_text.get("footprint_errors") or 0),
    )
    if violations > 0 or parity_errors > 0:
        status = FAIL_DRC
        summary = f"DRC/parity check failed with {violations} DRC violation(s) and {parity_errors} schematic-parity issue(s)."
    else:
        status = PASS
        summary = "DRC and schematic parity checks found no DRC violations or parity mismatches."
    return make_result(
        "check_pcb_drc",
        "PCB_DRC_AND_PARITY",
        status,
        summary,
        context,
        details={
            "drc_violations": violations,
            "schematic_parity_or_footprint_errors": parity_errors,
            "schematic_parity_issues_cli": drc_text.get("schematic_parity_issues"),
            "footprint_errors_report": drc_text.get("footprint_errors"),
            "json_unconnected_items": live_drc.get("unconnected_count"),
            "json_drc_result": live_drc.get("result"),
            "text_report_returncode": drc_text.get("returncode"),
        },
        artifacts={"drc_report_path": drc_text.get("report_path", "")},
    )


def evaluate_open_nets(context: dict[str, Any]) -> dict[str, Any]:
    live = context["live_state"]
    drc_text = ensure_drc_text(context)
    unconnected_items = int(live["drc"].get("unconnected_count") or 0)
    unrouted_nets = [str(item) for item in live["pcb"].get("unrouted_nets", [])]
    if unconnected_items > 0 or unrouted_nets:
        status = FAIL_OPEN_NETS
        summary = f"Open-net gate failed with {unconnected_items} unconnected item(s) and {len(unrouted_nets)} detectable unrouted net(s)."
    else:
        status = PASS
        summary = "Open-net gate found no unconnected items or detectable unrouted nets."
    return make_result(
        "check_open_nets",
        "OPEN_NETS_AND_SCHEMATIC_PARITY_CONNECTIVITY",
        status,
        summary,
        context,
        details={
            "unconnected_items": unconnected_items,
            "detectable_unrouted_net_count": len(unrouted_nets),
            "detectable_unrouted_nets": unrouted_nets,
            "drc_text_unconnected_pads": drc_text.get("unconnected_pads"),
        },
    )


def evaluate_trace_geometry(context: dict[str, Any]) -> dict[str, Any]:
    payload = context["geometry_payload"]
    findings = find_trace_quality_findings(payload)
    filtered = [item for item in findings if item.get("status") != TEST_POINT_STUB_TOO_LONG]
    counts = Counter(str(item.get("status", "")) for item in filtered)
    if counts.get(KEEP_OUT_CROSSING_FOUND, 0) > 0:
        status = FAIL_RF_KEEPOUT
        summary = f"Trace geometry failed because {counts.get(KEEP_OUT_CROSSING_FOUND, 0)} RF/antenna keepout crossing(s) were detected."
    elif filtered:
        status = FAIL_TRACE_GEOMETRY
        summary = f"Trace geometry failed with {len(filtered)} non-testpoint geometry finding(s)."
    else:
        status = PASS
        summary = "Trace geometry check found no right angles, acute angles, detours, perimeter boxes, board-edge crossings, or return-path split risks."
    return make_result(
        "check_trace_geometry",
        "TRACE_GEOMETRY",
        status,
        summary,
        context,
        details={
            "finding_count": len(filtered),
            "finding_counts": dict(counts),
            "representative_nets": sorted({str(item.get("net", "")) for item in filtered if item.get("net")})[:20],
            "findings": filtered[:50],
        },
    )


def evaluate_testpoint_topology(context: dict[str, Any]) -> dict[str, Any]:
    payload = context["geometry_payload"]
    findings = [item for item in find_trace_quality_findings(payload) if item.get("status") == TEST_POINT_STUB_TOO_LONG]
    non_leaf_paths: list[dict[str, Any]] = []
    if bool(context["constraints"].get("test_points", {}).get("require_leaf_topology", True)):
        for path in payload.get("traces", []):
            if not path.get("touches_test_point", False):
                continue
            start_tp = bool(path.get("start_testpoint_refs"))
            end_tp = bool(path.get("end_testpoint_refs"))
            if start_tp and end_tp:
                non_leaf_paths.append(
                    {
                        "trace_id": path.get("id", ""),
                        "net": path.get("net", ""),
                        "reason": "Path terminates in test points at both ends instead of a single leaf test branch.",
                    }
                )
    if findings or non_leaf_paths:
        status = FAIL_TESTPOINT_TOPOLOGY
        summary = f"Test-point topology failed with {len(findings)} long stub finding(s) and {len(non_leaf_paths)} non-leaf test-point path(s)."
    else:
        status = PASS
        summary = "Test-point topology found no long stubs or non-leaf TP branches."
    return make_result(
        "check_testpoint_stubs",
        "TESTPOINT_TOPOLOGY",
        status,
        summary,
        context,
        details={
            "long_stub_count": len(findings),
            "long_stub_findings": findings,
            "non_leaf_path_count": len(non_leaf_paths),
            "non_leaf_paths": non_leaf_paths,
            "max_stub_mm": float(context["constraints"].get("test_points", {}).get("max_stub_mm", 5.0)),
        },
    )


def evaluate_power_widths(context: dict[str, Any]) -> dict[str, Any]:
    payload = context["geometry_payload"]
    issues: list[dict[str, Any]] = []
    checked: list[dict[str, Any]] = []
    for item in context["constraints"].get("power_nets", []):
        net_name = str(item.get("name", "")).strip()
        if not net_name:
            continue
        min_width_mm = float(item.get("min_width_mm", 0.0))
        actual = min_trace_width_for_net(payload, net_name)
        checked.append({"net": net_name, "min_width_mm": min_width_mm, "actual_min_width_mm": actual})
        if actual is not None and actual + 1e-9 < min_width_mm:
            issues.append({"net": net_name, "min_width_mm": min_width_mm, "actual_min_width_mm": actual})
    if issues:
        status = FAIL_POWER_WIDTHS
        summary = f"Power-width check failed on {len(issues)} configured power net(s)."
    else:
        status = PASS
        summary = "Power-width check found no configured power nets narrower than their required minimum widths."
    return make_result(
        "check_power_widths",
        "POWER_WIDTHS",
        status,
        summary,
        context,
        details={
            "configured_power_nets": checked,
            "narrow_power_nets": issues,
        },
    )


def evaluate_usb_routing(context: dict[str, Any]) -> dict[str, Any]:
    payload = context["geometry_payload"]
    findings = usb_pair_findings(payload)
    pair_issues: list[dict[str, Any]] = []
    checked_pairs: list[dict[str, Any]] = []
    for pair in context["constraints"].get("usb_pairs", []):
        pos = str(pair.get("positive_net", "")).strip()
        neg = str(pair.get("negative_net", "")).strip()
        if not pos or not neg:
            continue
        pos_paths = trace_paths_for_net(payload, pos)
        neg_paths = trace_paths_for_net(payload, neg)
        pos_len = total_trace_length_for_net(payload, pos)
        neg_len = total_trace_length_for_net(payload, neg)
        delta = round(abs(pos_len - neg_len), 6)
        min_width = float(pair.get("min_width_mm", 0.0))
        pos_min = min_trace_width_for_net(payload, pos)
        neg_min = min_trace_width_for_net(payload, neg)
        max_delta = float(pair.get("max_length_delta_mm", 999.0))
        pair_record = {
            "name": str(pair.get("name", f"{pos}:{neg}")),
            "positive_net": pos,
            "negative_net": neg,
            "positive_length_mm": pos_len,
            "negative_length_mm": neg_len,
            "length_delta_mm": delta,
            "max_length_delta_mm": max_delta,
            "positive_min_width_mm": pos_min,
            "negative_min_width_mm": neg_min,
            "min_width_mm": min_width,
        }
        checked_pairs.append(pair_record)
        if not pos_paths or not neg_paths:
            pair_issues.append(dict(pair_record, reason="One or both USB nets have no routed path."))
            continue
        if delta > max_delta:
            pair_issues.append(dict(pair_record, reason="USB pair length delta exceeds configured maximum."))
        if (pos_min is not None and pos_min + 1e-9 < min_width) or (neg_min is not None and neg_min + 1e-9 < min_width):
            pair_issues.append(dict(pair_record, reason="USB pair width is narrower than the configured minimum."))
    filtered_findings = [
        item
        for item in findings
        if any(str(item.get("net", "")).strip() in {str(pair.get("positive_net", "")).strip(), str(pair.get("negative_net", "")).strip()} for pair in context["constraints"].get("usb_pairs", []))
    ]
    if filtered_findings or pair_issues:
        status = FAIL_USB_ROUTING
        summary = f"USB routing check failed with {len(filtered_findings)} geometry finding(s) and {len(pair_issues)} pair-sanitary issue(s)."
    else:
        status = PASS
        summary = "USB routing check found no pair-geometry or pair-sanitary issues."
    return make_result(
        "check_usb_pair_routing",
        "USB_PAIR_ROUTING",
        status,
        summary,
        context,
        details={
            "checked_pairs": checked_pairs,
            "pair_issues": pair_issues,
            "geometry_findings": filtered_findings,
        },
    )


def silkscreen_overlap_audit(context: dict[str, Any]) -> dict[str, Any]:
    if context.get("silkscreen_audit") is not None:
        return context["silkscreen_audit"]
    try:
        pcbnew = require_pcbnew_for_cli()
        board = pcbnew.LoadBoard(str(context["pcb_path"]))
    except Exception as exc:  # noqa: BLE001
        result = {
            "status": NEEDS_HUMAN_REVIEW,
            "summary": "Silkscreen overlap check could not load pcbnew safely.",
            "pad_overlap_count": None,
            "hole_overlap_count": None,
            "overlaps": [],
            "error": str(exc),
        }
        context["silkscreen_audit"] = result
        return result

    pad_boxes: list[dict[str, Any]] = []
    hole_boxes: list[dict[str, Any]] = []
    text_boxes: list[dict[str, Any]] = []

    for footprint in board.GetFootprints():
        ref = str(footprint.GetReference())
        footprint_name = str(footprint.GetFPID().GetLibItemName() or "")
        value = str(footprint.GetValue() or "")
        hole_like = ref.upper().startswith("MH") or "MOUNTINGHOLE" in footprint_name.upper() or "NPTH" in value.upper()
        for pad in footprint.Pads():
            record = {
                "ref": ref,
                "pad": str(pad.GetNumber()),
                "bbox_mm": bbox_to_mm(pcbnew, pad.GetBoundingBox()),
            }
            if hole_like:
                hole_boxes.append(record)
            else:
                pad_boxes.append(record)
        for label, getter, enabled in (
            ("reference", footprint.Reference, bool(context["constraints"].get("silkscreen", {}).get("check_reference_text", True))),
            ("value", footprint.Value, bool(context["constraints"].get("silkscreen", {}).get("check_value_text", True))),
        ):
            if not enabled:
                continue
            text_item = getter()
            try:
                visible = bool(text_item and text_item.IsVisible())
                layer_name = str(text_item.GetLayerName()) if text_item else ""
            except Exception:  # noqa: BLE001
                visible = False
                layer_name = ""
            if not visible or "SilkS" not in layer_name:
                continue
            text_boxes.append(
                {
                    "ref": ref,
                    "text_kind": label,
                    "layer": layer_name,
                    "bbox_mm": bbox_to_mm(pcbnew, text_item.GetBoundingBox()),
                }
            )

    overlaps: list[dict[str, Any]] = []
    pad_overlap_count = 0
    hole_overlap_count = 0
    for text in text_boxes:
        tb = text["bbox_mm"]
        for pad in pad_boxes:
            if not _bbox_overlap(tb, pad["bbox_mm"]):
                continue
            pad_overlap_count += 1
            overlaps.append(
                {
                    "text_ref": text["ref"],
                    "text_kind": text["text_kind"],
                    "layer": text["layer"],
                    "overlap_type": "PAD",
                    "target_ref": pad["ref"],
                    "target_pad": pad["pad"],
                }
            )
        for hole in hole_boxes:
            if not _bbox_overlap(tb, hole["bbox_mm"]):
                continue
            hole_overlap_count += 1
            overlaps.append(
                {
                    "text_ref": text["ref"],
                    "text_kind": text["text_kind"],
                    "layer": text["layer"],
                    "overlap_type": "HOLE",
                    "target_ref": hole["ref"],
                    "target_pad": hole["pad"],
                }
            )

    status = PASS if pad_overlap_count == 0 and hole_overlap_count == 0 else NEEDS_HUMAN_REVIEW
    summary = "No reference/value silkscreen overlap with pads or holes was detected." if status == PASS else "Reference/value silkscreen overlaps pads or holes and needs human cleanup."
    result = {
        "status": status,
        "summary": summary,
        "pad_overlap_count": pad_overlap_count,
        "hole_overlap_count": hole_overlap_count,
        "overlaps": overlaps[:50],
    }
    context["silkscreen_audit"] = result
    return result


def _bbox_overlap(a: dict[str, float], b: dict[str, float]) -> bool:
    return not (
        float(a["xmax"]) <= float(b["xmin"])
        or float(a["xmin"]) >= float(b["xmax"])
        or float(a["ymax"]) <= float(b["ymin"])
        or float(a["ymin"]) >= float(b["ymax"])
    )


def copper_zone_fill_status(context: dict[str, Any]) -> dict[str, Any]:
    try:
        pcbnew = require_pcbnew_for_cli()
        board = pcbnew.LoadBoard(str(context["pcb_path"]))
    except Exception as exc:  # noqa: BLE001
        return {
            "available": False,
            "zones": [],
            "error": str(exc),
        }
    zones: list[dict[str, Any]] = []
    for index, zone in enumerate(board.Zones()):
        name = str(zone.GetNetname() or f"ZONE_{index}")
        is_rule_area = bool(getattr(zone, "GetIsRuleArea", lambda: False)())
        if is_rule_area:
            continue
        filled: bool | None = None
        if hasattr(zone, "IsFilled"):
            try:
                filled = bool(zone.IsFilled())
            except Exception:  # noqa: BLE001
                filled = None
        zones.append(
            {
                "name": name,
                "layer": str(zone.GetLayerName()),
                "filled": filled,
            }
        )
    return {"available": True, "zones": zones}


def evaluate_zone_and_gnd(context: dict[str, Any]) -> dict[str, Any]:
    payload = context["geometry_payload"]
    gnd_constraints = context["constraints"].get("gnd", {})
    required_zone_nets = [str(item).strip().upper() for item in gnd_constraints.get("required_zone_nets", ["GND"]) if str(item).strip()]
    zones = payload.get("zones", [])
    zone_nets_present = {str(zone.get("net", "")).strip().upper() for zone in zones}
    missing_zone_nets = [net for net in required_zone_nets if net not in zone_nets_present]
    gnd_via_count = sum(1 for via in payload.get("vias", []) if str(via.get("net", "")).strip().upper() == "GND")
    min_stitch_vias = int(gnd_constraints.get("min_stitching_via_count", 0))
    fill_info = copper_zone_fill_status(context)
    unfilled = [zone for zone in fill_info.get("zones", []) if zone.get("filled") is False]
    fill_unknown = [zone for zone in fill_info.get("zones", []) if zone.get("filled") is None]
    silk = silkscreen_overlap_audit(context)

    if missing_zone_nets or gnd_via_count < min_stitch_vias or (bool(gnd_constraints.get("require_filled_zones", True)) and unfilled):
        status = FAIL_ZONE_GND
        summary = "Zone/GND gate failed because required GND zones, fill state, or stitching-via thresholds are not satisfied."
    elif fill_unknown or silk["status"] == NEEDS_HUMAN_REVIEW:
        status = NEEDS_HUMAN_REVIEW
        summary = "Zone/GND gate needs human review because zone-fill proof or silkscreen clearance proof is incomplete."
    else:
        status = PASS
        summary = "Zone/GND gate found required GND zones, acceptable stitching-via count, and no detected silkscreen overlap issue."

    return make_result(
        "check_zone_and_gnd_stitching",
        "ZONE_AND_GND",
        status,
        summary,
        context,
        details={
            "ground_strategy": payload.get("ground_strategy", {}),
            "required_zone_nets": required_zone_nets,
            "missing_zone_nets": missing_zone_nets,
            "gnd_zone_count": sum(1 for zone in zones if str(zone.get("net", "")).strip().upper() == "GND"),
            "gnd_via_count": gnd_via_count,
            "minimum_required_gnd_vias": min_stitch_vias,
            "unfilled_zones": unfilled,
            "fill_state_unknown_zones": fill_unknown,
            "silkscreen_audit": silk,
        },
    )


def evaluate_connector_orientation(context: dict[str, Any]) -> dict[str, Any]:
    connector_audit, antenna_audit = ensure_orientation_audits(context)
    connector_status = str(connector_audit.get("status", PASS))
    antenna_status = str(antenna_audit.get("status", PASS))
    if connector_status == "FAIL":
        status = FAIL_CONNECTOR_ORIENTATION
        summary = "Connector-orientation audit found a proven wrong-facing connector condition."
    elif antenna_status == "FAIL":
        status = FAIL_RF_KEEPOUT
        summary = "RF/antenna keepout direction failed."
    elif connector_status == "NEEDS_HUMAN_REVIEW" or antenna_status == "NEEDS_HUMAN_REVIEW":
        status = NEEDS_HUMAN_REVIEW
        summary = "Connector/RF orientation still requires human proof."
    else:
        status = PASS
        summary = "Connector and RF orientation checks passed."
    return make_result(
        "check_connector_orientation",
        "CONNECTOR_ORIENTATION_AND_RF_DIRECTION",
        status,
        summary,
        context,
        details={
            "connector_status": connector_status,
            "connector_records": connector_audit.get("records", []),
            "antenna_status": antenna_status,
            "antenna_records": antenna_audit.get("records", []),
        },
    )


def evaluate_all_checks(context: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        "drc": evaluate_pcb_drc(context),
        "open_nets": evaluate_open_nets(context),
        "trace_geometry": evaluate_trace_geometry(context),
        "testpoint_topology": evaluate_testpoint_topology(context),
        "power_widths": evaluate_power_widths(context),
        "usb_routing": evaluate_usb_routing(context),
        "connector_orientation": evaluate_connector_orientation(context),
        "zone_and_gnd": evaluate_zone_and_gnd(context),
    }


def build_gate_result(context: dict[str, Any], checks: dict[str, dict[str, Any]]) -> dict[str, Any]:
    statuses = {name: result["status"] for name, result in checks.items()}
    overall = PASS_FINAL_ROUTING
    for candidate in FAIL_PRIORITY:
        if candidate in statuses.values():
            overall = candidate
            break
    else:
        if NEEDS_HUMAN_REVIEW in statuses.values():
            overall = NEEDS_HUMAN_REVIEW

    fail_codes = sorted({status for status in statuses.values() if status not in {PASS}})
    live = context["live_state"]
    return {
        "schema_version": "1.0",
        "tool": "run_pcb_quality_gate",
        "project": context["project_name"],
        "project_path": repo_rel(context["project"]),
        "board_path": repo_rel(context["pcb_path"]),
        "read_only_mode": True,
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "status": overall,
        "summary": {
            "drc_result": live["drc"].get("result"),
            "drc_violation_count": live["drc"].get("violation_count"),
            "unconnected_item_count": live["drc"].get("unconnected_count"),
            "detectable_unrouted_net_count": live["pcb"].get("unrouted_net_count"),
            "board_size_mm": {
                "width_mm": live["pcb"].get("board_width_mm"),
                "height_mm": live["pcb"].get("board_height_mm"),
            },
        },
        "fail_codes": fail_codes,
        "checks": checks,
        "check_statuses": statuses,
        "source_hashes": {
            "kicad_pro": live["source_files"]["kicad_pro"].get("sha256"),
            "kicad_sch": live["source_files"]["kicad_sch"].get("sha256"),
            "kicad_pcb": live["source_files"]["kicad_pcb"].get("sha256"),
        },
        "constraints_path": repo_rel(context["constraints_path"]) if context.get("constraints_path") else "",
        "constraints": context["constraints"],
    }


def gate_markdown(result: dict[str, Any]) -> str:
    lines = [
        "# PCB Quality Gate Report",
        "",
        f"Project: `{result.get('project', '')}`",
        f"Status: `{result.get('status', '')}`",
        "",
        "## Summary",
        "",
        f"- DRC result: `{result.get('summary', {}).get('drc_result')}`",
        f"- DRC violations: `{result.get('summary', {}).get('drc_violation_count')}`",
        f"- Unconnected items: `{result.get('summary', {}).get('unconnected_item_count')}`",
        f"- Detectable unrouted nets: `{result.get('summary', {}).get('detectable_unrouted_net_count')}`",
        f"- Constraints: `{result.get('constraints_path', '') or 'DEFAULTS_ONLY'}`",
        "",
        "## Check Statuses",
        "",
        "| Check | Status | Summary |",
        "| --- | --- | --- |",
    ]
    for name, payload in result.get("checks", {}).items():
        lines.append(f"| `{name}` | `{payload.get('status', '')}` | {payload.get('summary', '')} |")
    lines.extend(
        [
            "",
            "## Fail Codes",
            "",
        ]
    )
    for code in result.get("fail_codes", []):
        lines.append(f"- `{code}`")
    if not result.get("fail_codes"):
        lines.append("- none")
    return "\n".join(lines) + "\n"
