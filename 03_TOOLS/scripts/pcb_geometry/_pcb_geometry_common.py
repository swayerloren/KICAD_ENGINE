#!/usr/bin/env python3
"""Shared helpers for read-only PCB trace geometry extraction and audits."""

from __future__ import annotations

import json
import math
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
LAYOUT_SCRIPTS = REPO_ROOT / "14_LAYOUT_AUTOMATION" / "scripts"
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))
if str(LAYOUT_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(LAYOUT_SCRIPTS))

from _kicad_pcb_bridge_common import dump_json, dump_markdown, ensure_parent, require_pcbnew_for_cli  # type: ignore  # noqa: E402
from _kicad_pcb_bridge_extract import build_routing_schema  # type: ignore  # noqa: E402
from _routing_common import (  # type: ignore  # noqa: E402
    get_keepouts,
    load_json,
    make_markdown,
    markdown_table,
    normalized_nets,
    point_in_polygon,
    segment_crosses_keepout,
    trace_length_mm,
)
from route_quality_common import (  # type: ignore  # noqa: E402
    ACUTE_JOG_FOUND,
    KEEP_OUT_CROSSING_FOUND,
    RIGHT_ANGLE_FOUND,
    UNNECESSARY_ZIGZAG_FOUND,
    coordinates_text,
    detect_acute_jog_findings,
    detect_right_angle_findings,
    detect_unnecessary_zigzag_findings,
)


POINT_TOL_MM = 0.001
PAD_ATTACH_TOL_MM = 1.6
PERIMETER_MARGIN_MM = 2.0
TEST_POINT_STUB_LIMIT_MM = 5.0
DETOUR_RATIO_LIMIT = 2.0

RECTANGULAR_LOOP_FOUND = "RECTANGULAR_LOOP_FOUND"
PERIMETER_BOX_ROUTE_FOUND = "PERIMETER_BOX_ROUTE_FOUND"
EXCESSIVE_DETOUR_RATIO = "EXCESSIVE_DETOUR_RATIO"
TEST_POINT_STUB_TOO_LONG = "TEST_POINT_STUB_TOO_LONG"
BOARD_EDGE_CROSSING = "BOARD_EDGE_CROSSING"
RETURN_PATH_SPLIT_RISK = "RETURN_PATH_SPLIT_RISK"

FAIL_STATUSES = [
    RIGHT_ANGLE_FOUND,
    ACUTE_JOG_FOUND,
    UNNECESSARY_ZIGZAG_FOUND,
    RECTANGULAR_LOOP_FOUND,
    PERIMETER_BOX_ROUTE_FOUND,
    EXCESSIVE_DETOUR_RATIO,
    TEST_POINT_STUB_TOO_LONG,
    BOARD_EDGE_CROSSING,
    KEEP_OUT_CROSSING_FOUND,
    RETURN_PATH_SPLIT_RISK,
]


def repo_rel(path: Path) -> str:
    return str(path.resolve().relative_to(REPO_ROOT)).replace("\\", "/")


def timestamp_slug() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def locate_project(target: str | Path) -> Path:
    path = Path(target).resolve()
    if path.is_file() and path.suffix.lower() == ".kicad_pcb":
        if path.parent.name.lower() == "kicad":
            return path.parent.parent
        return path.parent
    return path


def locate_pcb(target: str | Path) -> Path:
    path = Path(target).resolve()
    if path.is_file() and path.suffix.lower() == ".kicad_pcb":
        return path
    search_root = path / "kicad" if (path / "kicad").exists() else path
    candidates = sorted(item for item in search_root.glob("*.kicad_pcb") if item.is_file())
    if not candidates:
        raise FileNotFoundError(f"No .kicad_pcb file found under {search_root}")
    return candidates[0]


def quantized(value: float, tol: float = POINT_TOL_MM) -> float:
    return round(round(float(value) / tol) * tol, 6)


def point_key_xy(x_mm: float, y_mm: float) -> str:
    return f"{quantized(x_mm):.3f},{quantized(y_mm):.3f}"


def point_key(point: dict[str, float]) -> str:
    return point_key_xy(float(point["x_mm"]), float(point["y_mm"]))


def key_to_point(key: str) -> dict[str, float]:
    x_text, y_text = key.split(",", 1)
    return {"x_mm": float(x_text), "y_mm": float(y_text)}


def same_point(a: dict[str, float], b: dict[str, float], tol: float = POINT_TOL_MM) -> bool:
    return abs(float(a["x_mm"]) - float(b["x_mm"])) <= tol and abs(float(a["y_mm"]) - float(b["y_mm"])) <= tol


def point_distance(a: dict[str, float], b: dict[str, float]) -> float:
    return math.hypot(float(a["x_mm"]) - float(b["x_mm"]), float(a["y_mm"]) - float(b["y_mm"]))


def segment_points(segment: dict[str, Any]) -> tuple[dict[str, float], dict[str, float]]:
    return (
        {"x_mm": float(segment["x1"]), "y_mm": float(segment["y1"])},
        {"x_mm": float(segment["x2"]), "y_mm": float(segment["y2"])},
    )


def segment_length(segment: dict[str, Any]) -> float:
    start, end = segment_points(segment)
    return point_distance(start, end)


def segment_midpoint(segment: dict[str, Any]) -> dict[str, float]:
    return {
        "x_mm": round((float(segment["x1"]) + float(segment["x2"])) / 2.0, 6),
        "y_mm": round((float(segment["y1"]) + float(segment["y2"])) / 2.0, 6),
    }


def orthogonal_segment(segment: dict[str, Any]) -> bool:
    return abs(float(segment["x1"]) - float(segment["x2"])) <= POINT_TOL_MM or abs(float(segment["y1"]) - float(segment["y2"])) <= POINT_TOL_MM


def bbox_for_segments(segments: list[dict[str, Any]]) -> dict[str, float]:
    xs = [float(item["x1"]) for item in segments] + [float(item["x2"]) for item in segments]
    ys = [float(item["y1"]) for item in segments] + [float(item["y2"]) for item in segments]
    xmin = min(xs)
    xmax = max(xs)
    ymin = min(ys)
    ymax = max(ys)
    return {
        "xmin": round(xmin, 6),
        "xmax": round(xmax, 6),
        "ymin": round(ymin, 6),
        "ymax": round(ymax, 6),
        "width_mm": round(xmax - xmin, 6),
        "height_mm": round(ymax - ymin, 6),
    }


def near_board_perimeter_fraction(path: dict[str, Any], outline: dict[str, Any], margin_mm: float = PERIMETER_MARGIN_MM) -> float:
    total = 0.0
    near = 0.0
    for segment in path.get("segments", []):
        length = segment_length(segment)
        total += length
        midpoint = segment_midpoint(segment)
        distances = [
            abs(midpoint["x_mm"] - float(outline["xmin"])),
            abs(float(outline["xmax"]) - midpoint["x_mm"]),
            abs(midpoint["y_mm"] - float(outline["ymin"])),
            abs(float(outline["ymax"]) - midpoint["y_mm"]),
        ]
        if min(distances) <= margin_mm:
            near += length
    if total <= 0:
        return 0.0
    return round(near / total, 3)


def segment_crosses_board_edge(segment: dict[str, Any], outline: dict[str, Any]) -> bool:
    x1 = float(segment["x1"])
    y1 = float(segment["y1"])
    x2 = float(segment["x2"])
    y2 = float(segment["y2"])
    xmin = float(outline["xmin"])
    xmax = float(outline["xmax"])
    ymin = float(outline["ymin"])
    ymax = float(outline["ymax"])

    inside_1 = xmin <= x1 <= xmax and ymin <= y1 <= ymax
    inside_2 = xmin <= x2 <= xmax and ymin <= y2 <= ymax
    if not inside_1 or not inside_2:
        return True

    edges = outline.get("segments", [])
    current = (x1, y1, x2, y2)
    for edge in edges:
        start = edge.get("start_mm")
        end = edge.get("end_mm")
        if not start or not end:
            continue
        edge_tuple = (
            float(start["x_mm"]),
            float(start["y_mm"]),
            float(end["x_mm"]),
            float(end["y_mm"]),
        )
        if segments_intersect_strict(current, edge_tuple):
            return True
    return False


def ccw(ax: float, ay: float, bx: float, by: float, cx: float, cy: float) -> bool:
    return (cy - ay) * (bx - ax) > (by - ay) * (cx - ax)


def segments_intersect_strict(seg1: tuple[float, float, float, float], seg2: tuple[float, float, float, float]) -> bool:
    ax, ay, bx, by = seg1
    cx, cy, dx, dy = seg2
    if max(ax, bx) + POINT_TOL_MM < min(cx, dx) or max(cx, dx) + POINT_TOL_MM < min(ax, bx):
        return False
    if max(ay, by) + POINT_TOL_MM < min(cy, dy) or max(cy, dy) + POINT_TOL_MM < min(ay, by):
        return False
    return ccw(ax, ay, cx, cy, dx, dy) != ccw(bx, by, cx, cy, dx, dy) and ccw(ax, ay, bx, by, cx, cy) != ccw(ax, ay, bx, by, dx, dy)


def point_in_zone(point: dict[str, float], zone: dict[str, Any]) -> bool:
    points = zone.get("outline_points_mm") or zone.get("points") or []
    if len(points) < 3:
        bbox = zone.get("bbox_mm")
        if not bbox:
            return False
        return (
            float(bbox["xmin"]) <= float(point["x_mm"]) <= float(bbox["xmax"])
            and float(bbox["ymin"]) <= float(point["y_mm"]) <= float(bbox["ymax"])
        )
    return point_in_polygon(float(point["x_mm"]), float(point["y_mm"]), points)


def segment_crosses_zone(segment: dict[str, Any], zone: dict[str, Any]) -> bool:
    points = zone.get("outline_points_mm") or zone.get("points") or []
    if points:
        keepout_like = {
            "geometry": "POLYGON",
            "points": points,
            "xmin": zone.get("bbox_mm", {}).get("xmin", 0.0),
            "ymin": zone.get("bbox_mm", {}).get("ymin", 0.0),
            "xmax": zone.get("bbox_mm", {}).get("xmax", 0.0),
            "ymax": zone.get("bbox_mm", {}).get("ymax", 0.0),
        }
        return segment_crosses_keepout(segment, keepout_like)
    bbox = zone.get("bbox_mm")
    if not bbox:
        return False
    keepout_like = {
        "geometry": "RECT",
        "xmin": bbox["xmin"],
        "ymin": bbox["ymin"],
        "xmax": bbox["xmax"],
        "ymax": bbox["ymax"],
    }
    return segment_crosses_keepout(segment, keepout_like)


def net_lookup(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["name"]: item for item in normalized_nets(payload)}


def pads_by_net(payload: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for pad in payload.get("pads", []):
        grouped[str(pad.get("net", ""))].append(pad)
    return grouped


def vias_by_net(payload: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for via in payload.get("vias", []):
        grouped[str(via.get("net", ""))].append(via)
    return grouped


def tracks_by_net(payload: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for index, track in enumerate(payload.get("tracks", [])):
        net_name = str(track.get("net", ""))
        segment = dict(track.get("segment", {}))
        if not segment:
            continue
        segment["_track_index"] = index
        grouped[net_name].append(segment)
    return grouped


def nearby_pads(net_pads: list[dict[str, Any]], point: dict[str, float], tol_mm: float = PAD_ATTACH_TOL_MM) -> list[dict[str, Any]]:
    return [
        pad
        for pad in net_pads
        if point_distance(point, {"x_mm": float(pad["x_mm"]), "y_mm": float(pad["y_mm"])}) <= tol_mm
    ]


def oriented_segment(segment: dict[str, Any], current_key: str) -> tuple[dict[str, Any], str]:
    start_key = point_key_xy(float(segment["x1"]), float(segment["y1"]))
    end_key = point_key_xy(float(segment["x2"]), float(segment["y2"]))
    if start_key == current_key:
        return dict(segment), end_key
    return (
        {
            "x1": float(segment["x2"]),
            "y1": float(segment["y2"]),
            "x2": float(segment["x1"]),
            "y2": float(segment["y1"]),
            "layer": segment["layer"],
            "width_mm": segment["width_mm"],
            "_track_index": segment.get("_track_index"),
        },
        start_key,
    )


def build_path_record(
    net_name: str,
    path_index: int,
    node_sequence: list[str],
    segments: list[dict[str, Any]],
    node_adjacency: dict[str, list[int]],
    via_node_keys: set[str],
    net_info: dict[str, Any],
    net_pads: list[dict[str, Any]],
    outline: dict[str, Any],
) -> dict[str, Any]:
    start_point = key_to_point(node_sequence[0])
    end_point = key_to_point(node_sequence[-1])
    closed_loop = same_point(start_point, end_point) and len(node_sequence) > 2
    path_length = round(trace_length_mm(segments), 3)
    direct = 0.0 if closed_loop else round(point_distance(start_point, end_point), 3)
    ratio = round(path_length / direct, 3) if direct > 0 else None
    bbox = bbox_for_segments(segments)
    layers = sorted({str(item["layer"]) for item in segments})
    start_pads = nearby_pads(net_pads, start_point)
    end_pads = nearby_pads(net_pads, end_point)
    start_tp = sorted({str(item["component"]) for item in start_pads if str(item["component"]).upper().startswith("TP")})
    end_tp = sorted({str(item["component"]) for item in end_pads if str(item["component"]).upper().startswith("TP")})
    touched_vias = sorted({node for node in node_sequence if node in via_node_keys})
    path_kind = "LOOP" if closed_loop else "CHAIN"
    if not closed_loop and (start_tp or end_tp):
        path_kind = "TP_BRANCH"
    junction_count = sum(1 for node in node_sequence[1:-1] if len(node_adjacency.get(node, [])) > 2)
    return {
        "id": f"path:{net_name or 'NO_NET'}:{path_index}",
        "net": net_name,
        "role": str(net_info.get("role", "")),
        "net_class": str(net_info.get("net_class", "")),
        "critical": bool(net_info.get("critical", False)),
        "power": bool(net_info.get("power", False)),
        "usb": bool(net_info.get("usb", False)),
        "ground": bool(net_info.get("ground", False)),
        "routing_status": str(net_info.get("routing_status", "ROUTED")),
        "paired_with": str(net_info.get("paired_with", "")),
        "path_kind": path_kind,
        "closed_loop": closed_loop,
        "path_length_mm": path_length,
        "direct_length_mm": direct,
        "length_ratio": ratio,
        "segment_count": len(segments),
        "segments": segments,
        "bbox_mm": bbox,
        "layers": layers,
        "start_point_mm": start_point,
        "end_point_mm": end_point,
        "node_points_mm": [key_to_point(item) for item in node_sequence],
        "start_pad_ids": sorted({str(item["id"]) for item in start_pads}),
        "end_pad_ids": sorted({str(item["id"]) for item in end_pads}),
        "start_components": sorted({str(item["component"]) for item in start_pads}),
        "end_components": sorted({str(item["component"]) for item in end_pads}),
        "start_testpoint_refs": start_tp,
        "end_testpoint_refs": end_tp,
        "test_point_refs": sorted(set(start_tp + end_tp)),
        "touches_test_point": bool(start_tp or end_tp),
        "junction_count": junction_count,
        "via_count": len(touched_vias),
        "via_nodes": [key_to_point(item) for item in touched_vias],
        "perimeter_fraction": near_board_perimeter_fraction({"segments": segments}, outline),
        "review_required": bool(net_info.get("review_required", False)),
        "notes": "Path segments are extracted read-only from connected same-net track branches.",
    }


def trace_paths_from_schema(payload: dict[str, Any]) -> list[dict[str, Any]]:
    nets = net_lookup(payload)
    pads = pads_by_net(payload)
    vias = vias_by_net(payload)
    track_segments = tracks_by_net(payload)
    outline = payload.get("board_outline", {})

    path_records: list[dict[str, Any]] = []
    for net_name in sorted(set(track_segments) | set(vias)):
        segments = track_segments.get(net_name, [])
        if not segments:
            continue
        node_adjacency: dict[str, list[int]] = defaultdict(list)
        entries: list[dict[str, Any]] = []
        for index, segment in enumerate(segments):
            start_key = point_key_xy(float(segment["x1"]), float(segment["y1"]))
            end_key = point_key_xy(float(segment["x2"]), float(segment["y2"]))
            entries.append({"segment": segment, "start_key": start_key, "end_key": end_key})
            node_adjacency[start_key].append(index)
            node_adjacency[end_key].append(index)
        via_keys = {point_key_xy(float(item["x_mm"]), float(item["y_mm"])) for item in vias.get(net_name, [])}
        special_nodes = {node for node, attached in node_adjacency.items() if len(attached) != 2 or node in via_keys}
        visited: set[int] = set()
        path_index = 0

        def walk(start_node: str, start_segment_index: int) -> tuple[list[str], list[dict[str, Any]]]:
            node_sequence = [start_node]
            ordered_segments: list[dict[str, Any]] = []
            current_node = start_node
            current_segment_index = start_segment_index
            while True:
                visited.add(current_segment_index)
                ordered_segment, next_node = oriented_segment(entries[current_segment_index]["segment"], current_node)
                ordered_segments.append(ordered_segment)
                node_sequence.append(next_node)
                if next_node in special_nodes and next_node != start_node:
                    break
                candidates = [item for item in node_adjacency[next_node] if item != current_segment_index and item not in visited]
                if not candidates:
                    break
                current_node = next_node
                current_segment_index = candidates[0]
            return node_sequence, ordered_segments

        for node in sorted(special_nodes):
            for segment_index in list(node_adjacency[node]):
                if segment_index in visited:
                    continue
                node_sequence, ordered_segments = walk(node, segment_index)
                path_records.append(
                    build_path_record(
                        net_name,
                        path_index,
                        node_sequence,
                        ordered_segments,
                        node_adjacency,
                        via_keys,
                        nets.get(net_name, {}),
                        pads.get(net_name, []),
                        outline,
                    )
                )
                path_index += 1

        for segment_index in range(len(entries)):
            if segment_index in visited:
                continue
            start_node = entries[segment_index]["start_key"]
            node_sequence, ordered_segments = walk(start_node, segment_index)
            path_records.append(
                build_path_record(
                    net_name,
                    path_index,
                    node_sequence,
                    ordered_segments,
                    node_adjacency,
                    via_keys,
                    nets.get(net_name, {}),
                    pads.get(net_name, []),
                    outline,
                )
            )
            path_index += 1

    path_records.sort(key=lambda item: (item["net"], item["id"]))
    return path_records


def build_geometry_payload(target: str | Path) -> dict[str, Any]:
    pcb_path = locate_pcb(target)
    pcbnew = require_pcbnew_for_cli()
    board = pcbnew.LoadBoard(str(pcb_path))
    routing_schema = build_routing_schema(pcb_path.stem, pcb_path, board, pcbnew)
    traces = trace_paths_from_schema(routing_schema)
    return {
        "schema_version": "1.0",
        "tool": "extract_tracks",
        "read_only_mode": True,
        "project": routing_schema.get("project", pcb_path.stem),
        "board_path": routing_schema.get("board_path", str(pcb_path)),
        "board_outline": routing_schema.get("board_outline", {}),
        "edge_cuts": routing_schema.get("edge_cuts", []),
        "components": routing_schema.get("components", []),
        "pads": routing_schema.get("pads", []),
        "nets": routing_schema.get("nets", []),
        "net_classes": routing_schema.get("net_classes", {}),
        "keepouts": routing_schema.get("keepouts", []),
        "zones": routing_schema.get("zones", []),
        "tracks": routing_schema.get("tracks", []),
        "vias": routing_schema.get("vias", []),
        "traces": traces,
        "ground_strategy": routing_schema.get("ground_strategy", {}),
        "routing_status": routing_schema.get("routing_status", {}),
        "not_extracted": routing_schema.get("not_extracted", []),
        "summary": {
            "track_item_count": len(routing_schema.get("tracks", [])),
            "via_count": len(routing_schema.get("vias", [])),
            "path_count": len(traces),
            "net_count": len(routing_schema.get("nets", [])),
            "keepout_count": len(routing_schema.get("keepouts", [])),
            "zone_count": len(routing_schema.get("zones", [])),
        },
    }


def extraction_markdown(payload: dict[str, Any]) -> str:
    sample_rows = [
        [
            item["net"],
            item["path_kind"],
            item["segment_count"],
            item["path_length_mm"],
            item["direct_length_mm"],
            item["length_ratio"],
        ]
        for item in payload.get("traces", [])[:40]
    ]
    return make_markdown(
        "PCB Geometry Track Extraction",
        {
            "project": payload.get("project", ""),
            "board_path": payload.get("board_path", ""),
            "read_only_mode": payload.get("read_only_mode", False),
            "path_count": payload.get("summary", {}).get("path_count", 0),
            "track_item_count": payload.get("summary", {}).get("track_item_count", 0),
            "keepout_count": payload.get("summary", {}).get("keepout_count", 0),
            "zone_count": payload.get("summary", {}).get("zone_count", 0),
        },
        [
            (
                "Trace Paths",
                markdown_table(
                    ["net", "path_kind", "segments", "path_length_mm", "direct_length_mm", "length_ratio"],
                    sample_rows,
                ),
            ),
            (
                "Not Extracted",
                "\n".join(f"- {item}" for item in payload.get("not_extracted", [])) if payload.get("not_extracted") else "_none_",
            ),
        ],
    )


def make_finding(
    path: dict[str, Any],
    status: str,
    reason: str,
    recommended_fix: str,
    segment_payload: dict[str, Any] | list[dict[str, Any]],
    layer: str | None = None,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    payload = {
        "trace_id": path["id"],
        "net": path["net"],
        "role": path.get("role", ""),
        "status": status,
        "layer": layer or ",".join(path.get("layers", [])),
        "segment_coordinates": segment_payload,
        "reason": reason,
        "recommended_fix": recommended_fix,
        "path_length_mm": path.get("path_length_mm"),
        "direct_length_mm": path.get("direct_length_mm"),
        "length_ratio": path.get("length_ratio"),
        "path_kind": path.get("path_kind", ""),
    }
    if extra:
        payload.update(extra)
    return payload


def rectangular_loop_findings(payload: dict[str, Any], power_only: bool = False) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    outline = payload.get("board_outline", {})
    for path in payload.get("traces", []):
        if power_only and not path.get("power", False):
            continue
        segments = path.get("segments", [])
        if len(segments) < 4:
            continue
        orthogonal = sum(1 for item in segments if orthogonal_segment(item))
        if orthogonal < len(segments) - 1:
            continue
        bbox = path.get("bbox_mm", {})
        perimeter = 2.0 * (float(bbox.get("width_mm", 0.0)) + float(bbox.get("height_mm", 0.0)))
        path_length = float(path.get("path_length_mm", 0.0))
        if path.get("closed_loop", False) and perimeter >= 10.0 and abs(path_length - perimeter) <= max(1.0, perimeter * 0.25):
            findings.append(
                make_finding(
                    path,
                    RECTANGULAR_LOOP_FOUND,
                    f"Path forms an orthogonal closed loop of about {round(path_length, 3)} mm perimeter.",
                    "Remove the rectangular loop and reroute as a compact direct path without a box-like copper ring.",
                    [segment_coords(item) for item in segments],
                )
            )
            continue
        ratio = path.get("length_ratio")
        if ratio is None:
            continue
        if float(ratio) > 1.8 and near_board_perimeter_fraction(path, outline) >= 0.5 and perimeter >= 15.0:
            findings.append(
                make_finding(
                    path,
                    PERIMETER_BOX_ROUTE_FOUND,
                    f"Path detours around the perimeter with orthogonal box-like routing and length ratio {ratio}.",
                    "Shorten this route, reduce perimeter hugging, and rebuild the branch with a more direct geometry.",
                    [segment_coords(item) for item in segments],
                )
            )
    return findings


def detour_ratio_findings(payload: dict[str, Any], power_only: bool = False) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for path in payload.get("traces", []):
        if power_only and not path.get("power", False):
            continue
        direct = float(path.get("direct_length_mm", 0.0) or 0.0)
        path_length = float(path.get("path_length_mm", 0.0) or 0.0)
        ratio = path.get("length_ratio")
        if direct <= 0.0 or ratio is None:
            continue
        if path_length > 6.0 and float(ratio) > DETOUR_RATIO_LIMIT:
            findings.append(
                make_finding(
                    path,
                    EXCESSIVE_DETOUR_RATIO,
                    f"Routed length {round(path_length, 3)} mm exceeds {DETOUR_RATIO_LIMIT}x the direct span {round(direct, 3)} mm.",
                    "Shorten the route, remove decorative detours, or repair placement so the path stays compact.",
                    [segment_coords(item) for item in path.get("segments", [])],
                )
            )
    return findings


def test_point_stub_findings(payload: dict[str, Any]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for path in payload.get("traces", []):
        if path.get("closed_loop", False):
            continue
        path_length = float(path.get("path_length_mm", 0.0) or 0.0)
        if path_length <= TEST_POINT_STUB_LIMIT_MM:
            continue
        start_tp = path.get("start_testpoint_refs", [])
        end_tp = path.get("end_testpoint_refs", [])
        if bool(start_tp) ^ bool(end_tp):
            tp_refs = start_tp or end_tp
            findings.append(
                make_finding(
                    path,
                    TEST_POINT_STUB_TOO_LONG,
                    f"Test-point branch `{', '.join(tp_refs)}` is {round(path_length, 3)} mm long.",
                    f"Keep TP stubs at or under {TEST_POINT_STUB_LIMIT_MM} mm, or move the TP closer to the main trunk.",
                    [segment_coords(item) for item in path.get("segments", [])],
                    extra={"test_point_refs": tp_refs},
                )
            )
    return findings


def board_edge_crossing_findings(payload: dict[str, Any]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    outline = payload.get("board_outline", {})
    for path in payload.get("traces", []):
        for segment in path.get("segments", []):
            if segment_crosses_board_edge(segment, outline):
                findings.append(
                    make_finding(
                        path,
                        BOARD_EDGE_CROSSING,
                        "Trace geometry crosses or extends beyond the board edge.",
                        "Pull this segment fully inside the board outline and keep copper clear of Edge.Cuts.",
                        segment_coords(segment),
                        layer=str(segment.get("layer", "")),
                    )
                )
    return findings


def rf_keepout_crossing_findings(payload: dict[str, Any]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    keepouts = get_keepouts(payload, {"RF_KEEPOUT", "ANTENNA_KEEPOUT"})
    for path in payload.get("traces", []):
        for segment in path.get("segments", []):
            for keepout in keepouts:
                if segment_crosses_keepout(segment, keepout):
                    findings.append(
                        make_finding(
                            path,
                            KEEP_OUT_CROSSING_FOUND,
                            f"Trace crosses keepout `{keepout.get('name', '')}` of type `{keepout.get('type', '')}`.",
                            "Reroute the trace completely outside the RF or antenna keepout boundary.",
                            segment_coords(segment),
                            layer=str(segment.get("layer", "")),
                        )
                    )
    return findings


def return_path_split_findings(payload: dict[str, Any], power_only: bool = False) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    gnd_zones = [zone for zone in payload.get("zones", []) if str(zone.get("net", "")).upper() == "GND"]
    if not gnd_zones:
        return findings
    for path in payload.get("traces", []):
        if path.get("ground", False):
            continue
        if power_only and not path.get("power", False):
            continue
        for zone in gnd_zones:
            zone_layer = str(zone.get("layer", ""))
            zone_bbox = zone.get("bbox_mm", {})
            inside_segments: list[dict[str, Any]] = []
            xs: list[float] = []
            ys: list[float] = []
            for segment in path.get("segments", []):
                if str(segment.get("layer", "")) != zone_layer:
                    continue
                midpoint = segment_midpoint(segment)
                if point_in_zone(midpoint, zone) or segment_crosses_zone(segment, zone):
                    inside_segments.append(segment)
                    xs.extend([float(segment["x1"]), float(segment["x2"])])
                    ys.extend([float(segment["y1"]), float(segment["y2"])])
            if not inside_segments:
                continue
            total_in_zone = float(trace_length_mm(inside_segments))
            if total_in_zone <= 10.0:
                continue
            x_span = max(xs) - min(xs) if xs else 0.0
            y_span = max(ys) - min(ys) if ys else 0.0
            zone_width = float(zone_bbox.get("width_mm", 0.0) or 0.0)
            zone_height = float(zone_bbox.get("height_mm", 0.0) or 0.0)
            if (zone_width > 0.0 and x_span > zone_width * 0.6) or (zone_height > 0.0 and y_span > zone_height * 0.6):
                findings.append(
                    make_finding(
                        path,
                        RETURN_PATH_SPLIT_RISK,
                        f"Trace cuts through a large fraction of GND zone `{zone.get('name', '')}`, risking a return-path split.",
                        "Rebuild this route so it does not carve a long slot through the reference plane, or add a safer local return strategy.",
                        [segment_coords(item) for item in inside_segments],
                        layer=zone_layer,
                    )
                )
                break
    return findings


def segment_coords(segment: dict[str, Any]) -> dict[str, float]:
    return {
        "x1_mm": round(float(segment["x1"]), 3),
        "y1_mm": round(float(segment["y1"]), 3),
        "x2_mm": round(float(segment["x2"]), 3),
        "y2_mm": round(float(segment["y2"]), 3),
    }


def trace_angle_findings(payload: dict[str, Any]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for path in payload.get("traces", []):
        net_info = {"critical": path.get("critical", False), "width_mm": 0.0}
        findings.extend(detect_right_angle_findings(path, net_info))
        findings.extend(detect_acute_jog_findings(path, net_info))
    return findings


def zigzag_findings(payload: dict[str, Any]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for path in payload.get("traces", []):
        net_info = {"critical": path.get("critical", False), "width_mm": 0.0}
        findings.extend(detect_unnecessary_zigzag_findings(path, net_info))
    return findings


def power_loop_findings(payload: dict[str, Any]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    findings.extend(detour_ratio_findings(payload, power_only=True))
    findings.extend(rectangular_loop_findings(payload, power_only=True))
    findings.extend(return_path_split_findings(payload, power_only=True))
    return findings


def usb_pair_findings(payload: dict[str, Any]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for path in payload.get("traces", []):
        if not path.get("usb", False):
            continue
        net_info = {"critical": True, "width_mm": 0.0}
        findings.extend(detect_right_angle_findings(path, net_info))
        findings.extend(detect_acute_jog_findings(path, net_info))
        findings.extend(detect_unnecessary_zigzag_findings(path, net_info))
        direct = float(path.get("direct_length_mm", 0.0) or 0.0)
        ratio = path.get("length_ratio")
        if direct > 0.0 and ratio is not None and float(ratio) > DETOUR_RATIO_LIMIT:
            findings.append(
                make_finding(
                    path,
                    EXCESSIVE_DETOUR_RATIO,
                    f"USB route length ratio {ratio} exceeds the {DETOUR_RATIO_LIMIT}x direct-path limit.",
                    "Shorten the USB route and remove avoidable detours before treating the pair geometry as acceptable.",
                    [segment_coords(item) for item in path.get("segments", [])],
                )
            )
    return findings


def aggregate_trace_quality_findings(payload: dict[str, Any]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    findings.extend(trace_angle_findings(payload))
    findings.extend(zigzag_findings(payload))
    findings.extend(rectangular_loop_findings(payload))
    findings.extend(detour_ratio_findings(payload))
    findings.extend(test_point_stub_findings(payload))
    findings.extend(board_edge_crossing_findings(payload))
    findings.extend(rf_keepout_crossing_findings(payload))
    findings.extend(return_path_split_findings(payload))
    return findings


def audit_result(payload: dict[str, Any], tool_name: str, findings: list[dict[str, Any]], scope: str) -> dict[str, Any]:
    counts: dict[str, int] = {}
    for status in FAIL_STATUSES:
        count = sum(1 for item in findings if item["status"] == status)
        if count:
            counts[status] = count
    return {
        "schema_version": "1.0",
        "tool": tool_name,
        "scope": scope,
        "project": payload.get("project", ""),
        "read_only_mode": True,
        "status": "PASS" if not findings else "FAIL",
        "summary": {
            "path_count": len(payload.get("traces", [])),
            "finding_count": len(findings),
            "track_item_count": payload.get("summary", {}).get("track_item_count", 0),
        },
        "finding_counts": counts,
        "findings": findings,
        "board_path": payload.get("board_path", ""),
    }


def audit_markdown(title: str, result: dict[str, Any]) -> str:
    rows = [
        [
            item.get("net", ""),
            item.get("status", ""),
            item.get("layer", ""),
            coordinates_text(item.get("segment_coordinates")),
            item.get("reason", ""),
            item.get("recommended_fix", ""),
        ]
        for item in result.get("findings", [])
    ]
    return make_markdown(
        title,
        {
            "project": result.get("project", ""),
            "status": result.get("status", ""),
            "scope": result.get("scope", ""),
            "path_count": result.get("summary", {}).get("path_count", 0),
            "finding_count": result.get("summary", {}).get("finding_count", 0),
        },
        [
            (
                "Finding Counts",
                markdown_table(
                    ["status", "count"],
                    [[status, count] for status, count in sorted(result.get("finding_counts", {}).items())],
                ),
            ),
            (
                "Findings",
                markdown_table(
                    ["net", "status", "layer", "segment_coordinates", "reason", "recommended_fix"],
                    rows,
                ),
            ),
        ],
    )


def overlay_color(status: str) -> str:
    mapping = {
        RIGHT_ANGLE_FOUND: "#d62728",
        ACUTE_JOG_FOUND: "#ff7f0e",
        UNNECESSARY_ZIGZAG_FOUND: "#9467bd",
        RECTANGULAR_LOOP_FOUND: "#8c564b",
        PERIMETER_BOX_ROUTE_FOUND: "#e377c2",
        EXCESSIVE_DETOUR_RATIO: "#bcbd22",
        TEST_POINT_STUB_TOO_LONG: "#17becf",
        BOARD_EDGE_CROSSING: "#1f77b4",
        KEEP_OUT_CROSSING_FOUND: "#ff1493",
        RETURN_PATH_SPLIT_RISK: "#7f7f7f",
    }
    return mapping.get(status, "#d62728")


def render_svg_overlay(payload: dict[str, Any], result: dict[str, Any]) -> str:
    outline = payload.get("board_outline", {})
    xmin = float(outline.get("xmin", 0.0))
    xmax = float(outline.get("xmax", 100.0))
    ymin = float(outline.get("ymin", 0.0))
    ymax = float(outline.get("ymax", 100.0))
    width = max(1.0, xmax - xmin)
    height = max(1.0, ymax - ymin)
    scale = 8.0
    margin = 20.0
    svg_width = width * scale + margin * 2.0
    svg_height = height * scale + margin * 2.0

    def sx(x_mm: float) -> float:
        return margin + (x_mm - xmin) * scale

    def sy(y_mm: float) -> float:
        return margin + (ymax - y_mm) * scale

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_width:.1f}" height="{svg_height:.1f}" viewBox="0 0 {svg_width:.1f} {svg_height:.1f}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<rect x="{sx(xmin):.1f}" y="{sy(ymax):.1f}" width="{width * scale:.1f}" height="{height * scale:.1f}" fill="#f8f8f8" stroke="#222222" stroke-width="1.5"/>',
    ]

    for keepout in payload.get("keepouts", []):
        points = keepout.get("points", [])
        if points:
            svg_points = " ".join(f"{sx(float(item['x_mm'])):.1f},{sy(float(item['y_mm'])):.1f}" for item in points)
            lines.append(
                f'<polygon points="{svg_points}" fill="rgba(255,165,0,0.18)" stroke="#ff8c00" stroke-width="1.0" stroke-dasharray="4 3"/>'
            )

    for path in payload.get("traces", []):
        for segment in path.get("segments", []):
            lines.append(
                f'<line x1="{sx(float(segment["x1"])):.1f}" y1="{sy(float(segment["y1"])):.1f}" x2="{sx(float(segment["x2"])):.1f}" y2="{sy(float(segment["y2"])):.1f}" stroke="#bdbdbd" stroke-width="1.8" stroke-linecap="round"/>'
            )

    labeled: set[str] = set()
    for finding in result.get("findings", []):
        color = overlay_color(str(finding.get("status", "")))
        coords = finding.get("segment_coordinates")
        segments = coords if isinstance(coords, list) else [coords]
        valid_segments = [item for item in segments if isinstance(item, dict)]
        for segment in valid_segments:
            lines.append(
                f'<line x1="{sx(float(segment["x1_mm"])):.1f}" y1="{sy(float(segment["y1_mm"])):.1f}" x2="{sx(float(segment["x2_mm"])):.1f}" y2="{sy(float(segment["y2_mm"])):.1f}" stroke="{color}" stroke-width="3.4" stroke-linecap="round"/>'
            )
        if valid_segments:
            first = valid_segments[0]
            label_key = f'{finding.get("net","")}::{finding.get("status","")}'
            if label_key not in labeled:
                labeled.add(label_key)
                lines.append(
                    f'<text x="{sx(float(first["x1_mm"])) + 4.0:.1f}" y="{sy(float(first["y1_mm"])) - 4.0:.1f}" fill="{color}" font-size="10" font-family="Consolas, monospace">{finding.get("net","")} {finding.get("status","")}</text>'
                )

    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def write_json_and_markdown(output_json: str | Path, payload: dict[str, Any], markdown_path: str | Path | None, title: str, markdown_text: str | None = None) -> None:
    ensure_parent(output_json)
    dump_json(output_json, payload)
    if markdown_path:
        ensure_parent(markdown_path)
        dump_markdown(markdown_path, markdown_text or audit_markdown(title, payload))


def load_payload(path: str | Path) -> dict[str, Any]:
    return load_json(path)


def write_svg(path: str | Path, text: str) -> None:
    ensure_parent(path)
    Path(path).write_text(text, encoding="utf-8")


def default_output_dir(project_or_pcb: str | Path) -> Path:
    project = locate_project(project_or_pcb)
    return project / "reports" / "pcb_geometry" / timestamp_slug()


def default_tracks_paths(output_dir: Path) -> tuple[Path, Path]:
    return output_dir / "tracks.json", output_dir / "tracks.md"


def default_report_paths(output_dir: Path, stem: str) -> tuple[Path, Path]:
    return output_dir / f"{stem}.json", output_dir / f"{stem}.md"


def default_overlay_paths(output_dir: Path) -> tuple[Path, Path]:
    return output_dir / "trace_quality_overlay.svg", output_dir / "trace_quality_overlay.md"
