#!/usr/bin/env python3
"""Shared helpers for placement planning and live-board readiness scoring."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from _kicad_pcb_bridge_common import bbox_to_mm, mm, require_pcbnew_for_cli
from _kicad_pcb_bridge_extract import board_outline


STAGE_ORDER = [
    "BOARD_OUTLINE",
    "MOUNTING_HOLES",
    "EDGE_CONNECTORS",
    "RF_AND_KEEPOUT",
    "POWER_INPUT_PATH",
    "POWER_REGULATION",
    "USB_PATH",
    "MCU_SUPPORT",
    "RESET_BOOT",
    "LEDS",
    "TEST_PADS",
    "LOW_RISK_PASSIVES",
]

ROLE_TO_STAGE = {
    "MOUNTING_HOLE": "MOUNTING_HOLES",
    "USB_C": "EDGE_CONNECTORS",
    "BARREL_JACK": "EDGE_CONNECTORS",
    "EDGE_CONNECTOR": "EDGE_CONNECTORS",
    "RF_MODULE": "RF_AND_KEEPOUT",
    "RF_CONNECTOR": "RF_AND_KEEPOUT",
    "FUSE": "POWER_INPUT_PATH",
    "TVS": "POWER_INPUT_PATH",
    "PMOS_PROTECTION": "POWER_INPUT_PATH",
    "INPUT_CAP": "POWER_INPUT_PATH",
    "REGULATOR": "POWER_REGULATION",
    "INDUCTOR": "POWER_REGULATION",
    "OUTPUT_CAP": "POWER_REGULATION",
    "ESD_USB": "USB_PATH",
    "USB_SERIES": "USB_PATH",
    "USB_CC": "USB_PATH",
    "DECOUPLING_CAP": "MCU_SUPPORT",
    "MCU_SUPPORT": "MCU_SUPPORT",
    "RESET_BUTTON": "RESET_BOOT",
    "BOOT_BUTTON": "RESET_BOOT",
    "LED": "LEDS",
    "TEST_PAD": "TEST_PADS",
    "PASSIVE_LOW_RISK": "LOW_RISK_PASSIVES",
}

STAGE_INDEX = {name: index for index, name in enumerate(STAGE_ORDER)}

RIGHT_ANGLE_TOLERANCE_DEG = 5.0
BOARD_EDGE_COMPONENT_MARGIN_MM = 0.25
EDGE_CONNECTOR_MAX_EDGE_DISTANCE_MM = 6.5
TEST_PAD_EDGE_DISTANCE_MM = 5.0
TEST_PAD_ROW_SPACING_MIN_MM = 2.2
HARD_FAIL_STATUSES = {
    "USB_CONNECTOR_ORIENTATION_UNKNOWN",
    "POWER_CONNECTOR_ORIENTATION_UNKNOWN",
    "ESP32_ANTENNA_KEEPOUT_BLOCKED",
    "POWER_PATH_SCATTERED_BEYOND_THRESHOLD",
    "USB_CLUSTER_TOO_SPREAD",
    "TEST_PADS_INACCESSIBLE",
    "FOOTPRINT_OUTSIDE_BOARD",
    "COURTYARD_BODY_OVERLAP",
    "PLACEMENT_CREATES_IMPOSSIBLE_ROUTE",
}


def load_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def dump_json(path: str | Path, payload: dict[str, Any]) -> None:
    Path(path).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def dump_markdown(path: str | Path, text: str) -> None:
    Path(path).write_text(text.rstrip() + "\n", encoding="utf-8")


def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def placement_stage_for_role(role: str) -> str:
    return ROLE_TO_STAGE.get(role.strip().upper(), "LOW_RISK_PASSIVES")


def normalize_edge(edge: str | None) -> str | None:
    if edge is None:
        return None
    value = edge.strip().lower()
    if value in {"top", "bottom", "left", "right"}:
        return value
    return None


def component_size(component: dict[str, Any]) -> tuple[float, float]:
    width = float(component.get("courtyard_width_mm", component.get("width_mm", 0.0)))
    height = float(component.get("courtyard_height_mm", component.get("height_mm", 0.0)))
    return width, height


def bbox_from_center(x_mm: float, y_mm: float, width_mm: float, height_mm: float) -> dict[str, float]:
    half_w = width_mm / 2.0
    half_h = height_mm / 2.0
    return {
        "xmin": round(x_mm - half_w, 6),
        "xmax": round(x_mm + half_w, 6),
        "ymin": round(y_mm - half_h, 6),
        "ymax": round(y_mm + half_h, 6),
    }


def bbox_width(bbox: dict[str, float]) -> float:
    return round(float(bbox["xmax"]) - float(bbox["xmin"]), 6)


def bbox_height(bbox: dict[str, float]) -> float:
    return round(float(bbox["ymax"]) - float(bbox["ymin"]), 6)


def bbox_center(bbox: dict[str, float]) -> dict[str, float]:
    return {
        "x_mm": round((float(bbox["xmin"]) + float(bbox["xmax"])) / 2.0, 6),
        "y_mm": round((float(bbox["ymin"]) + float(bbox["ymax"])) / 2.0, 6),
    }


def bbox_area(bbox: dict[str, float]) -> float:
    return round(max(0.0, bbox_width(bbox)) * max(0.0, bbox_height(bbox)), 6)


def expand_bbox(bbox: dict[str, float], margin_mm: float) -> dict[str, float]:
    return {
        "xmin": round(float(bbox["xmin"]) - margin_mm, 6),
        "xmax": round(float(bbox["xmax"]) + margin_mm, 6),
        "ymin": round(float(bbox["ymin"]) - margin_mm, 6),
        "ymax": round(float(bbox["ymax"]) + margin_mm, 6),
    }


def union_bbox(boxes: list[dict[str, float]]) -> dict[str, float] | None:
    if not boxes:
        return None
    return {
        "xmin": round(min(float(box["xmin"]) for box in boxes), 6),
        "xmax": round(max(float(box["xmax"]) for box in boxes), 6),
        "ymin": round(min(float(box["ymin"]) for box in boxes), 6),
        "ymax": round(max(float(box["ymax"]) for box in boxes), 6),
    }


def bboxes_overlap(a: dict[str, float], b: dict[str, float]) -> bool:
    return not (
        float(a["xmax"]) <= float(b["xmin"])
        or float(a["xmin"]) >= float(b["xmax"])
        or float(a["ymax"]) <= float(b["ymin"])
        or float(a["ymin"]) >= float(b["ymax"])
    )


def bbox_intersection(a: dict[str, float], b: dict[str, float]) -> dict[str, float] | None:
    if not bboxes_overlap(a, b):
        return None
    return {
        "xmin": round(max(float(a["xmin"]), float(b["xmin"])), 6),
        "xmax": round(min(float(a["xmax"]), float(b["xmax"])), 6),
        "ymin": round(max(float(a["ymin"]), float(b["ymin"])), 6),
        "ymax": round(min(float(a["ymax"]), float(b["ymax"])), 6),
    }


def bbox_overlap_area(a: dict[str, float], b: dict[str, float]) -> float:
    overlap = bbox_intersection(a, b)
    return bbox_area(overlap) if overlap else 0.0


def bbox_inside_board(
    bbox: dict[str, float],
    board_width_mm: float,
    board_height_mm: float,
    edge_clearance_mm: float,
) -> bool:
    return (
        float(bbox["xmin"]) >= edge_clearance_mm
        and float(bbox["ymin"]) >= edge_clearance_mm
        and float(bbox["xmax"]) <= board_width_mm - edge_clearance_mm
        and float(bbox["ymax"]) <= board_height_mm - edge_clearance_mm
    )


def bbox_within_bounds(bbox: dict[str, float], board_bbox: dict[str, float], margin_mm: float = 0.0) -> bool:
    return (
        float(bbox["xmin"]) >= float(board_bbox["xmin"]) - margin_mm
        and float(bbox["ymin"]) >= float(board_bbox["ymin"]) - margin_mm
        and float(bbox["xmax"]) <= float(board_bbox["xmax"]) + margin_mm
        and float(bbox["ymax"]) <= float(board_bbox["ymax"]) + margin_mm
    )


def point_distance(a: dict[str, float], b: dict[str, float]) -> float:
    dx = float(a["x_mm"]) - float(b["x_mm"])
    dy = float(a["y_mm"]) - float(b["y_mm"])
    return round((dx * dx + dy * dy) ** 0.5, 6)


def bbox_distance(a: dict[str, float], b: dict[str, float]) -> float:
    if bboxes_overlap(a, b):
        return 0.0
    dx = max(float(b["xmin"]) - float(a["xmax"]), float(a["xmin"]) - float(b["xmax"]), 0.0)
    dy = max(float(b["ymin"]) - float(a["ymax"]), float(a["ymin"]) - float(b["ymax"]), 0.0)
    return round((dx * dx + dy * dy) ** 0.5, 6)


def nearest_board_edge(board_bbox: dict[str, float], bbox: dict[str, float]) -> dict[str, float | str]:
    distances = {
        "left": round(float(bbox["xmin"]) - float(board_bbox["xmin"]), 6),
        "right": round(float(board_bbox["xmax"]) - float(bbox["xmax"]), 6),
        "top": round(float(bbox["ymin"]) - float(board_bbox["ymin"]), 6),
        "bottom": round(float(board_bbox["ymax"]) - float(bbox["ymax"]), 6),
    }
    edge = min(distances, key=distances.get)
    return {"edge": edge, "distance_mm": distances[edge], "distances_mm": distances}


def overhang_amounts(board_bbox: dict[str, float], bbox: dict[str, float]) -> dict[str, float]:
    return {
        "left": round(max(0.0, float(board_bbox["xmin"]) - float(bbox["xmin"])), 6),
        "right": round(max(0.0, float(bbox["xmax"]) - float(board_bbox["xmax"])), 6),
        "top": round(max(0.0, float(board_bbox["ymin"]) - float(bbox["ymin"])), 6),
        "bottom": round(max(0.0, float(bbox["ymax"]) - float(board_bbox["ymax"])), 6),
    }


def segment_bbox(start: dict[str, float], end: dict[str, float]) -> dict[str, float]:
    return {
        "xmin": min(float(start["x_mm"]), float(end["x_mm"])),
        "xmax": max(float(start["x_mm"]), float(end["x_mm"])),
        "ymin": min(float(start["y_mm"]), float(end["y_mm"])),
        "ymax": max(float(start["y_mm"]), float(end["y_mm"])),
    }


def segment_intersects_bbox(start: dict[str, float], end: dict[str, float], bbox: dict[str, float]) -> bool:
    return bboxes_overlap(segment_bbox(start, end), bbox)


def orientation_family(rotation_deg: float) -> str:
    normalized = round(float(rotation_deg)) % 360
    if normalized in {0, 180}:
        return "horizontal"
    if normalized in {90, 270}:
        return "vertical"
    return "angled"


def normalize_net_name(name: str) -> str:
    return str(name or "").strip().upper()


def flatten_unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            ordered.append(item)
    return ordered


def extract_pad_nets(footprint: Any) -> list[str]:
    nets: list[str] = []
    for pad in footprint.Pads():
        name = normalize_net_name(pad.GetNetname())
        if name:
            nets.append(name)
    return flatten_unique(sorted(nets))


def extract_pad_bbox(footprint: Any, pcbnew: Any) -> dict[str, float] | None:
    boxes = [bbox_to_mm(pcbnew, pad.GetBoundingBox()) for pad in footprint.Pads()]
    return union_bbox(boxes)


def extract_courtyard_bbox(footprint: Any, pcbnew: Any) -> dict[str, float] | None:
    boxes: list[dict[str, float]] = []
    if not hasattr(footprint, "GraphicalItems"):
        return None
    for item in footprint.GraphicalItems():
        layer_name = str(getattr(item, "GetLayerName", lambda: "")())
        if layer_name in {"F.Courtyard", "B.Courtyard"}:
            boxes.append(bbox_to_mm(pcbnew, item.GetBoundingBox()))
    return union_bbox(boxes)


def infer_live_component_role(ref: str, value: str, footprint_name: str, pad_nets: list[str]) -> str:
    upper_ref = ref.upper()
    upper_value = value.upper()
    upper_fp = footprint_name.upper()
    haystack = " ".join([upper_ref, upper_value, upper_fp, " ".join(pad_nets)])

    if upper_ref.startswith("MH") or "MOUNTINGHOLE" in upper_fp or "NPTH" in upper_value:
        return "MOUNTING_HOLE"
    if upper_ref.startswith("TP") or "TESTPOINT" in upper_fp:
        return "TEST_PAD"
    if "USB_C" in upper_fp or "USB4105" in upper_fp or "USB-C" in upper_value:
        return "USB_C"
    if "BARREL" in upper_fp or "JACK_5V" in upper_value or "PJ-102" in upper_fp:
        return "BARREL_JACK"
    if upper_ref.startswith("J"):
        return "EDGE_CONNECTOR"
    if "ESP32" in haystack or "WROOM" in haystack:
        return "RF_MODULE"
    if upper_ref.startswith("F") or "FUSE" in haystack or "PTC" in haystack:
        return "FUSE"
    if upper_ref.startswith("Q") and any(net in pad_nets for net in {"/+5V_FUSED", "/+5V_PROTECTED", "/+5V_IN"}):
        return "PMOS_PROTECTION"
    if upper_ref.startswith("D") and "TVS" in haystack:
        return "TVS"
    if upper_ref.startswith("U") and ("USB_ESD" in haystack or any(net in pad_nets for net in {"/DP_C", "/DM_C", "/DP_E", "/DM_E"})):
        return "ESD_USB"
    if upper_ref.startswith("R") and any(token in upper_value for token in {"CC1", "CC2"}):
        return "USB_CC"
    if upper_ref.startswith("R") and any(token in upper_value for token in {"D+", "D-", "DP", "DM"}):
        return "USB_SERIES"
    if upper_ref.startswith("U") and ("AP63203" in haystack or "/BUCK_SW" in pad_nets or "/BUCK_BST" in pad_nets):
        return "REGULATOR"
    if upper_ref.startswith("L") or "INDUCTOR" in haystack:
        return "INDUCTOR"
    if upper_ref.startswith("C"):
        if any(net in pad_nets for net in {"/+5V_IN", "/+5V_FUSED", "/+5V_PROTECTED", "/BUCK_BST"}):
            return "INPUT_CAP"
        if any(net in pad_nets for net in {"+3V3", "3V3"}):
            return "OUTPUT_CAP"
        return "DECOUPLING_CAP"
    if upper_ref.startswith("SW") and ("BOOT" in haystack or "/BOOT0" in pad_nets):
        return "BOOT_BUTTON"
    if upper_ref.startswith("SW") and ("RESET" in haystack or "/ESP_EN" in pad_nets):
        return "RESET_BUTTON"
    if upper_ref.startswith("D") and "LED" in haystack:
        return "LED"
    return "PASSIVE_LOW_RISK"


def infer_antenna_keepout(component: dict[str, Any]) -> dict[str, Any] | None:
    if component.get("role") != "RF_MODULE":
        return None
    body_bbox = component.get("body_bbox")
    courtyard_bbox = component.get("courtyard_bbox")
    if not body_bbox or not courtyard_bbox:
        return None

    extensions = {
        "top": round(float(body_bbox["ymin"]) - float(courtyard_bbox["ymin"]), 6),
        "bottom": round(float(courtyard_bbox["ymax"]) - float(body_bbox["ymax"]), 6),
        "left": round(float(body_bbox["xmin"]) - float(courtyard_bbox["xmin"]), 6),
        "right": round(float(courtyard_bbox["xmax"]) - float(body_bbox["xmax"]), 6),
    }
    side = max(extensions, key=extensions.get)
    depth = float(extensions[side])
    if depth < 3.0:
        return {
            "status": "UNKNOWN",
            "reason": "RF module courtyard does not expose a clear keepout extension.",
            "extensions_mm": extensions,
        }

    if side == "top":
        bbox = {
            "xmin": float(courtyard_bbox["xmin"]),
            "xmax": float(courtyard_bbox["xmax"]),
            "ymin": float(courtyard_bbox["ymin"]),
            "ymax": float(body_bbox["ymin"]),
        }
    elif side == "bottom":
        bbox = {
            "xmin": float(courtyard_bbox["xmin"]),
            "xmax": float(courtyard_bbox["xmax"]),
            "ymin": float(body_bbox["ymax"]),
            "ymax": float(courtyard_bbox["ymax"]),
        }
    elif side == "left":
        bbox = {
            "xmin": float(courtyard_bbox["xmin"]),
            "xmax": float(body_bbox["xmin"]),
            "ymin": float(courtyard_bbox["ymin"]),
            "ymax": float(courtyard_bbox["ymax"]),
        }
    else:
        bbox = {
            "xmin": float(body_bbox["xmax"]),
            "xmax": float(courtyard_bbox["xmax"]),
            "ymin": float(courtyard_bbox["ymin"]),
            "ymax": float(courtyard_bbox["ymax"]),
        }
    return {
        "status": "INFERRED",
        "side": side,
        "depth_mm": round(depth, 6),
        "bbox": {key: round(value, 6) for key, value in bbox.items()},
        "extensions_mm": extensions,
    }


def placement_component_record(board_bbox: dict[str, float], footprint: Any, pcbnew: Any) -> dict[str, Any]:
    ref = str(footprint.GetReference())
    value = str(footprint.GetValue())
    footprint_name = str(footprint.GetFPID().GetLibItemName())
    full_library_name = str(footprint.GetFPID().GetFullLibraryName())
    pos = footprint.GetPosition()
    pad_nets = extract_pad_nets(footprint)
    body_bbox = extract_pad_bbox(footprint, pcbnew) or bbox_to_mm(pcbnew, footprint.GetBoundingBox())
    body_bbox = expand_bbox(body_bbox, 0.05)
    courtyard_bbox = extract_courtyard_bbox(footprint, pcbnew) or expand_bbox(body_bbox, 0.25)
    edge_info = nearest_board_edge(board_bbox, courtyard_bbox)
    role = infer_live_component_role(ref, value, footprint_name, pad_nets)

    component = {
        "ref": ref,
        "value": value,
        "footprint_name": footprint_name,
        "footprint_library": full_library_name,
        "role": role,
        "placement_stage": STAGE_INDEX[placement_stage_for_role(role)],
        "stage_name": placement_stage_for_role(role),
        "x_mm": mm(pcbnew, pos.x),
        "y_mm": mm(pcbnew, pos.y),
        "rotation_deg": round(float(footprint.GetOrientationDegrees()), 6),
        "side": "B" if str(footprint.GetLayerName()) == "B.Cu" else "F",
        "pad_nets": pad_nets,
        "pad_count": len(list(footprint.Pads())),
        "body_bbox": body_bbox,
        "courtyard_bbox": courtyard_bbox,
        "body_center": bbox_center(body_bbox),
        "courtyard_center": bbox_center(courtyard_bbox),
        "edge_proximity": edge_info,
        "fixed_mechanical": role in {"MOUNTING_HOLE", "USB_C", "BARREL_JACK", "EDGE_CONNECTOR"} or ref.upper().startswith("J"),
        "mounting_hole": role == "MOUNTING_HOLE",
    }
    antenna_keepout = infer_antenna_keepout(component)
    if antenna_keepout:
        component["antenna_keepout"] = antenna_keepout
    return component


def track_records(board: Any, pcbnew: Any) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    tracks: list[dict[str, Any]] = []
    vias: list[dict[str, Any]] = []
    for item in board.GetTracks():
        item_type = type(item).__name__
        if item_type == "PCB_TRACK":
            start = item.GetStart()
            end = item.GetEnd()
            tracks.append(
                {
                    "net": str(item.GetNetname()),
                    "layer": str(item.GetLayerName()),
                    "width_mm": mm(pcbnew, item.GetWidth()),
                    "start_mm": {"x_mm": mm(pcbnew, start.x), "y_mm": mm(pcbnew, start.y)},
                    "end_mm": {"x_mm": mm(pcbnew, end.x), "y_mm": mm(pcbnew, end.y)},
                }
            )
        elif item_type == "PCB_VIA":
            position = item.GetPosition()
            vias.append(
                {
                    "net": str(item.GetNetname()),
                    "x_mm": mm(pcbnew, position.x),
                    "y_mm": mm(pcbnew, position.y),
                    "drill_mm": mm(pcbnew, item.GetDrillValue()),
                    "diameter_mm": mm(pcbnew, item.GetFrontWidth()),
                }
            )
    return tracks, vias


def build_live_placement_state(pcb_file: str | Path) -> dict[str, Any]:
    pcbnew = require_pcbnew_for_cli()
    board_path = Path(pcb_file).resolve()
    board = pcbnew.LoadBoard(str(board_path))
    project_name = board_path.stem
    for suffix in ("_copy", "_copied"):
        if project_name.lower().endswith(suffix):
            project_name = project_name[: -len(suffix)]
            break
    outline, _segments, unsupported = board_outline(board, pcbnew)
    board_bbox = {
        "xmin": float(outline["xmin"]),
        "xmax": float(outline["xmax"]),
        "ymin": float(outline["ymin"]),
        "ymax": float(outline["ymax"]),
    }
    components = [
        placement_component_record(board_bbox, footprint, pcbnew)
        for footprint in sorted(board.GetFootprints(), key=lambda item: item.GetReference())
    ]
    tracks, vias = track_records(board, pcbnew)

    return {
        "project": project_name,
        "source_pcb": str(board_path),
        "source_sha256": sha256_file(board_path),
        "source_timestamp": board_path.stat().st_mtime,
        "board": {
            "width_mm": float(outline["width_mm"]),
            "height_mm": float(outline["height_mm"]),
            "bbox": board_bbox,
        },
        "components": components,
        "tracks": tracks,
        "vias": vias,
        "unsupported_extract_notes": unsupported,
    }
