#!/usr/bin/env python3
"""Shared read-only helpers for the PCB prelayout engine."""

from __future__ import annotations

import copy
import hashlib
import json
import math
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = next(
    (path for path in [SCRIPT_DIR, *SCRIPT_DIR.parents] if (path / "AGENTS.md").exists()),
    SCRIPT_DIR,
)
LAYOUT_SCRIPTS = REPO_ROOT / "14_LAYOUT_AUTOMATION" / "scripts"
PROJECT_STATE_SCRIPTS = REPO_ROOT / "03_TOOLS" / "scripts" / "project_state"
MECHANICAL_ORIENTATION_SCRIPTS = REPO_ROOT / "03_TOOLS" / "scripts" / "mechanical_orientation"

for candidate in (LAYOUT_SCRIPTS, PROJECT_STATE_SCRIPTS, MECHANICAL_ORIENTATION_SCRIPTS):
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))

from _placement_common import (  # type: ignore  # noqa: E402
    bboxes_overlap,
    build_live_placement_state,
    nearest_board_edge,
)
from _mechanical_orientation_common import (  # type: ignore  # noqa: E402
    build_connector_truth_record,
    load_truth_catalog,
)
from project_state_common import build_board_schema, build_live_project_state_data  # type: ignore  # noqa: E402


CONNECTOR_EDGE_THRESHOLD_MM = 7.0
ORIENTATION_TRUTH_CATALOG = load_truth_catalog()


def iso_now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def timestamp_slug() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


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
        return str(candidate)


def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def locate_project(project_path: str | Path) -> Path:
    candidate = Path(project_path)
    if candidate.is_absolute():
        return candidate.resolve()
    return (REPO_ROOT / candidate).resolve()


def locate_pcb(project_path: str | Path) -> Path:
    project = locate_project(project_path)
    candidates = [
        project / "kicad" / f"{project.name}.kicad_pcb",
        project / f"{project.name}.kicad_pcb",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()
    matches = sorted(project.glob("**/*.kicad_pcb"))
    if matches:
        return matches[0].resolve()
    raise FileNotFoundError(f"No .kicad_pcb found under {project}")


def live_state_is_current(live_state: dict[str, Any], pcb_path: Path) -> bool:
    source_files = live_state.get("source_files", {})
    pcb_meta = source_files.get("kicad_pcb", {})
    return pcb_meta.get("sha256") == sha256_file(pcb_path)


def load_live_state(project_path: str | Path) -> dict[str, Any]:
    project = locate_project(project_path)
    pcb_path = locate_pcb(project)
    live_state_path = project / "reports" / "LIVE_PROJECT_STATE.json"
    if live_state_path.exists():
        data = load_json(live_state_path)
        if isinstance(data, dict) and live_state_is_current(data, pcb_path):
            return data
    return build_live_project_state_data(project, REPO_ROOT, False)


def load_routing_schema(project_path: str | Path) -> dict[str, Any]:
    project = locate_project(project_path)
    pcb_path = locate_pcb(project)
    schema_path = project / "reports" / "live_project_state" / "LIVE_PROJECT_STATE_ROUTING_SCHEMA.json"
    if schema_path.exists():
        return load_json(schema_path)
    return build_board_schema(project.name, pcb_path)


def board_bbox(board_profile: dict[str, Any]) -> dict[str, float]:
    bbox = board_profile["outline_bbox"]
    return {
        "xmin": float(bbox["xmin"]),
        "xmax": float(bbox["xmax"]),
        "ymin": float(bbox["ymin"]),
        "ymax": float(bbox["ymax"]),
    }


def shift_bbox(bbox: dict[str, Any] | None, dx: float, dy: float) -> dict[str, float] | None:
    if not bbox:
        return None
    return {
        "xmin": round(float(bbox["xmin"]) + dx, 6),
        "xmax": round(float(bbox["xmax"]) + dx, 6),
        "ymin": round(float(bbox["ymin"]) + dy, 6),
        "ymax": round(float(bbox["ymax"]) + dy, 6),
    }


def component_center(component: dict[str, Any]) -> dict[str, float]:
    bbox = component.get("courtyard_bbox") or component.get("body_bbox")
    if bbox:
        return {
            "x_mm": round((float(bbox["xmin"]) + float(bbox["xmax"])) / 2.0, 6),
            "y_mm": round((float(bbox["ymin"]) + float(bbox["ymax"])) / 2.0, 6),
        }
    return {
        "x_mm": round(float(component["x_mm"]), 6),
        "y_mm": round(float(component["y_mm"]), 6),
    }


def shift_component(
    component: dict[str, Any],
    target_x_mm: float,
    target_y_mm: float,
    rotation_deg: float | None,
    board_profile: dict[str, Any],
) -> dict[str, Any]:
    updated = copy.deepcopy(component)
    dx = float(target_x_mm) - float(component["x_mm"])
    dy = float(target_y_mm) - float(component["y_mm"])
    updated["x_mm"] = round(float(target_x_mm), 6)
    updated["y_mm"] = round(float(target_y_mm), 6)
    if rotation_deg is not None:
        updated["rotation_deg"] = round(float(rotation_deg), 6)
    for key in ("body_bbox", "courtyard_bbox"):
        updated[key] = shift_bbox(updated.get(key), dx, dy)
    antenna_keepout = updated.get("antenna_keepout")
    if isinstance(antenna_keepout, dict) and isinstance(antenna_keepout.get("bbox"), dict):
        antenna_keepout["bbox"] = shift_bbox(antenna_keepout["bbox"], dx, dy)
    bbox = updated.get("courtyard_bbox") or updated.get("body_bbox")
    if bbox:
        updated["edge_proximity"] = nearest_board_edge(board_bbox(board_profile), bbox)
    return updated


def first_ref_by_role(components: list[dict[str, Any]], role: str) -> str | None:
    for component in components:
        if component.get("role") == role:
            return str(component["ref"])
    return None


def refs_by_role(components: list[dict[str, Any]], role: str) -> list[str]:
    return [str(component["ref"]) for component in components if component.get("role") == role]


def get_component(components: list[dict[str, Any]], ref: str) -> dict[str, Any] | None:
    for component in components:
        if str(component.get("ref")) == ref:
            return component
    return None


def set_component(
    components: list[dict[str, Any]],
    ref: str,
    target_x_mm: float,
    target_y_mm: float,
    board_profile: dict[str, Any],
    rotation_deg: float | None = None,
) -> None:
    for index, component in enumerate(components):
        if str(component.get("ref")) == ref:
            components[index] = shift_component(component, target_x_mm, target_y_mm, rotation_deg, board_profile)
            return


def infer_connector_type(component: dict[str, Any]) -> str:
    role = str(component.get("role") or "").upper()
    footprint = str(component.get("footprint_name") or "").upper()
    value = str(component.get("value") or "").upper()
    ref = str(component.get("ref") or "").upper()
    if role == "USB_C" or "USB_C" in footprint or "USB-C" in value:
        return "USB_C"
    if role == "BARREL_JACK" or "BARREL" in footprint or "JACK_5V" in value:
        return "BARREL_JACK"
    if ref.startswith("J"):
        return "EDGE_CONNECTOR"
    return "CONNECTOR"


def normalize_edge(edge: str | None) -> str:
    if edge is None:
        return "bottom"
    value = str(edge).strip().lower()
    if value in {"top", "bottom", "left", "right"}:
        return value
    return "bottom"


def expected_mating_direction(connector_type: str, rotation_deg: float) -> str:
    normalized = int(round(float(rotation_deg))) % 360
    mapping = {
        0: "bottom",
        90: "left",
        180: "top",
        270: "right",
    }
    if connector_type == "CONNECTOR":
        return mapping.get(normalized, "bottom")
    return mapping.get(normalized, "bottom")


def build_connector_truth(
    component: dict[str, Any],
    board_profile_data: dict[str, Any],
    intended_edge: str | None,
) -> dict[str, Any]:
    if not component.get("edge_proximity"):
        bbox = component.get("courtyard_bbox") or component.get("body_bbox")
        if bbox:
            component = copy.deepcopy(component)
            component["edge_proximity"] = nearest_board_edge(board_bbox(board_profile_data), bbox)
    return build_connector_truth_record(component, ORIENTATION_TRUTH_CATALOG, intended_edge)


def build_board_profile(live_state: dict[str, Any]) -> dict[str, Any]:
    pcb = live_state["pcb"]
    return {
        "project": live_state["project"]["name"],
        "source_pcb": live_state["source_files"]["kicad_pcb"]["path"],
        "source_sha256": live_state["source_files"]["kicad_pcb"]["sha256"],
        "board_shape": "RECTANGULAR" if pcb["board_outline_exists"] else "UNKNOWN",
        "board_width_mm": pcb["board_width_mm"],
        "board_height_mm": pcb["board_height_mm"],
        "outline_bbox": pcb["outline_bbox_mm"],
        "mounting_hole_count": pcb["mounting_hole_count"],
        "rf_module_present": False,
        "live_board_context": {
            "drc_result": live_state["drc"]["result"],
            "violation_count": int(live_state["drc"]["violation_count"] or 0),
            "unconnected_count": int(live_state["drc"]["unconnected_count"] or 0),
            "detectable_unrouted_net_count": int(pcb["unrouted_net_count"] or 0),
        },
    }


def summarize_nets(routing_schema: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for net in routing_schema.get("nets", []) or []:
        rows.append(
            {
                "name": net.get("name", ""),
                "role": net.get("role", "LOW_RISK"),
                "power": bool(net.get("power")),
                "usb": bool(net.get("usb")),
                "critical": bool(net.get("critical")),
                "routing_priority": int(net.get("routing_priority", 0)),
                "routing_status": net.get("routing_status", ""),
                "pads": net.get("pads", []),
            }
        )
    return rows


def choose_projection_net_names(twin: dict[str, Any]) -> list[str]:
    preferred_names = {
        "/+5V_IN",
        "/+5V_FUSED",
        "/+5V_PROTECTED",
        "/BUCK_BST",
        "/BUCK_SW",
        "+3V3",
        "/BOOT0",
        "/ESP_EN",
        "/CC1",
        "/CC2",
        "/SHIELD",
        "/DM_C",
        "/DM_E",
        "/DP_C",
        "/DP_E",
        "/PLED",
        "/SLED",
        "/STATUS_LED",
        "/U0RXD",
        "/U0TXD",
    }
    nets: list[str] = []
    for net in twin.get("nets", []):
        name = str(net.get("name") or "")
        if not name:
            continue
        upper_name = name.upper()
        if upper_name.startswith("UNCONNECTED-") or upper_name.startswith("UNCONNECTED("):
            continue
        if name in preferred_names or net.get("power") or net.get("usb") or net.get("critical"):
            nets.append(name)
    ordered: list[str] = []
    seen: set[str] = set()
    for name in nets:
        if name not in seen:
            seen.add(name)
            ordered.append(name)
    return ordered


def components_for_net(components: list[dict[str, Any]], net_name: str) -> list[dict[str, Any]]:
    matches = []
    for component in components:
        if net_name in (component.get("pad_nets") or []):
            matches.append(component)
    return sorted(matches, key=lambda item: (float(item["x_mm"]), float(item["y_mm"]), str(item["ref"])))


def route_class_for_net(net_name: str, twin: dict[str, Any]) -> str:
    for net in twin.get("nets", []):
        if net.get("name") == net_name:
            role = str(net.get("role") or "LOW_RISK")
            if bool(net.get("power")):
                return "POWER"
            if bool(net.get("usb")):
                return "USB_DATA"
            return role
    return "LOW_RISK"


def point_from_component(component: dict[str, Any]) -> dict[str, float]:
    return {
        "x_mm": round(float(component["x_mm"]), 6),
        "y_mm": round(float(component["y_mm"]), 6),
    }


def angle_deg(start: dict[str, float], end: dict[str, float]) -> float:
    dx = float(end["x_mm"]) - float(start["x_mm"])
    dy = float(end["y_mm"]) - float(start["y_mm"])
    value = math.degrees(math.atan2(dy, dx))
    return round(value % 360.0, 3)


def segment_length(start: dict[str, float], end: dict[str, float]) -> float:
    dx = float(end["x_mm"]) - float(start["x_mm"])
    dy = float(end["y_mm"]) - float(start["y_mm"])
    return round(math.hypot(dx, dy), 6)


def make_segment(start: dict[str, float], end: dict[str, float]) -> dict[str, Any]:
    return {
        "start": {"x_mm": round(float(start["x_mm"]), 6), "y_mm": round(float(start["y_mm"]), 6)},
        "end": {"x_mm": round(float(end["x_mm"]), 6), "y_mm": round(float(end["y_mm"]), 6)},
        "angle_deg": angle_deg(start, end),
        "length_mm": segment_length(start, end),
    }


def project_45deg_path(start: dict[str, float], end: dict[str, float]) -> list[dict[str, Any]]:
    dx = float(end["x_mm"]) - float(start["x_mm"])
    dy = float(end["y_mm"]) - float(start["y_mm"])
    if abs(dx) < 1e-6 or abs(dy) < 1e-6:
        return [make_segment(start, end)]
    sx = 1.0 if dx >= 0 else -1.0
    sy = 1.0 if dy >= 0 else -1.0
    diagonal = min(abs(dx), abs(dy))
    midpoint = {
        "x_mm": round(float(start["x_mm"]) + sx * diagonal, 6),
        "y_mm": round(float(start["y_mm"]) + sy * diagonal, 6),
    }
    return [make_segment(start, midpoint), make_segment(midpoint, end)]


def segment_bbox(segment: dict[str, Any]) -> dict[str, float]:
    start = segment["start"]
    end = segment["end"]
    return {
        "xmin": min(float(start["x_mm"]), float(end["x_mm"])),
        "xmax": max(float(start["x_mm"]), float(end["x_mm"])),
        "ymin": min(float(start["y_mm"]), float(end["y_mm"])),
        "ymax": max(float(start["y_mm"]), float(end["y_mm"])),
    }


def route_crosses_keepout(route_segments: list[dict[str, Any]], keepout_boxes: list[dict[str, float]]) -> bool:
    for segment in route_segments:
        bbox = segment_bbox(segment)
        for keepout in keepout_boxes:
            if bboxes_overlap(bbox, keepout):
                return True
    return False


def keepout_boxes_from_variant(variant: dict[str, Any]) -> list[dict[str, float]]:
    keepouts: list[dict[str, float]] = []
    for component in variant.get("components", []):
        antenna_keepout = component.get("antenna_keepout")
        if isinstance(antenna_keepout, dict) and isinstance(antenna_keepout.get("bbox"), dict):
            bbox = antenna_keepout["bbox"]
            keepouts.append(
                {
                    "xmin": float(bbox["xmin"]),
                    "xmax": float(bbox["xmax"]),
                    "ymin": float(bbox["ymin"]),
                    "ymax": float(bbox["ymax"]),
                }
            )
    return keepouts


def mechanical_conflict_pairs(components: list[dict[str, Any]]) -> list[tuple[str, str]]:
    refs: list[tuple[str, str]] = []
    for index, left in enumerate(components):
        left_box = left.get("body_bbox") or left.get("courtyard_bbox")
        if not left_box:
            continue
        for right in components[index + 1 :]:
            right_box = right.get("body_bbox") or right.get("courtyard_bbox")
            if not right_box:
                continue
            if bboxes_overlap(left_box, right_box):
                refs.append((str(left["ref"]), str(right["ref"])))
    return refs


def component_outside_board(component: dict[str, Any], board_profile_data: dict[str, Any]) -> bool:
    bbox = component.get("courtyard_bbox") or component.get("body_bbox")
    if not bbox:
        return False
    board = board_bbox(board_profile_data)
    return (
        float(bbox["xmin"]) < board["xmin"]
        or float(bbox["xmax"]) > board["xmax"]
        or float(bbox["ymin"]) < board["ymin"]
        or float(bbox["ymax"]) > board["ymax"]
    )


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)
