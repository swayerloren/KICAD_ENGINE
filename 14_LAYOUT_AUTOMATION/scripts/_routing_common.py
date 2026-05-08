#!/usr/bin/env python3
"""Shared helpers for routing-planning, routing-audit, and fixture tests."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROUTING_ORDER = [
    "POWER_INPUT_PROTECTION",
    "REGULATOR_CRITICAL_LOOP",
    "RAIL_3V3",
    "USB_DP_DM",
    "ESD_PROTECTION",
    "ESP32_EN_BOOT",
    "DECOUPLING",
    "LEDS_BUTTONS",
    "TEST_PADS",
    "LOW_RISK_REMAINING",
]

ROLE_TO_STAGE = {
    "POWER_INPUT": "POWER_INPUT_PROTECTION",
    "POWER_PROTECTION": "POWER_INPUT_PROTECTION",
    "REGULATOR_LOOP": "REGULATOR_CRITICAL_LOOP",
    "BUCK_SW": "REGULATOR_CRITICAL_LOOP",
    "BUCK_BST": "REGULATOR_CRITICAL_LOOP",
    "REG_SW": "REGULATOR_CRITICAL_LOOP",
    "RAIL_3V3": "RAIL_3V3",
    "USB_DP_DM": "USB_DP_DM",
    "USB_D+": "USB_DP_DM",
    "USB_D-": "USB_DP_DM",
    "ESD": "ESD_PROTECTION",
    "PROTECTION": "ESD_PROTECTION",
    "EN_BOOT": "ESP32_EN_BOOT",
    "DECOUPLING": "DECOUPLING",
    "LEDS_BUTTONS": "LEDS_BUTTONS",
    "TEST_PADS": "TEST_PADS",
    "LOW_RISK": "LOW_RISK_REMAINING",
}

STAGE_INDEX = {name: index for index, name in enumerate(ROUTING_ORDER)}
CRITICAL_STAGE_LIMIT = STAGE_INDEX["DECOUPLING"]


def load_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def dump_json(path: str | Path, payload: dict[str, Any]) -> None:
    Path(path).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def dump_markdown(path: str | Path, text: str) -> None:
    Path(path).write_text(text.rstrip() + "\n", encoding="utf-8")


def parse_args_markdown(parser) -> None:
    parser.add_argument("--markdown", help="Optional Markdown output path")


def routing_stage_for_role(role: str) -> str:
    return ROLE_TO_STAGE.get(role.strip().upper(), "LOW_RISK_REMAINING")


def net_is_critical(stage_name: str) -> bool:
    return STAGE_INDEX.get(stage_name, 99) <= CRITICAL_STAGE_LIMIT


def get_net_class_map(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    raw = payload.get("net_classes", {})
    if isinstance(raw, dict):
        return {str(name): value for name, value in raw.items()}
    if isinstance(raw, list):
        return {str(item.get("name", "")): item for item in raw if item.get("name")}
    return {}


def get_keepouts(payload: dict[str, Any], types: set[str] | None = None) -> list[dict[str, Any]]:
    keepouts = payload.get("keepouts", [])
    if not types:
        return keepouts
    return [item for item in keepouts if str(item.get("type", "")).upper() in types]


def get_traces(payload: dict[str, Any]) -> list[dict[str, Any]]:
    return payload.get("traces", [])


def get_trace_for_net(payload: dict[str, Any], net_name: str) -> list[dict[str, Any]]:
    return [trace for trace in get_traces(payload) if str(trace.get("net", "")).strip() == net_name]


def angle_degrees(seg_a: dict[str, Any], seg_b: dict[str, Any]) -> float:
    ax = float(seg_a["x2"]) - float(seg_a["x1"])
    ay = float(seg_a["y2"]) - float(seg_a["y1"])
    bx = float(seg_b["x2"]) - float(seg_b["x1"])
    by = float(seg_b["y2"]) - float(seg_b["y1"])
    amag = math.hypot(ax, ay)
    bmag = math.hypot(bx, by)
    if amag == 0 or bmag == 0:
        return 0.0
    cosang = max(-1.0, min(1.0, (ax * bx + ay * by) / (amag * bmag)))
    return math.degrees(math.acos(cosang))


def trace_length_mm(segments: list[dict[str, Any]]) -> float:
    total = 0.0
    for seg in segments:
        total += math.hypot(float(seg["x2"]) - float(seg["x1"]), float(seg["y2"]) - float(seg["y1"]))
    return round(total, 3)


def point_in_rect(x: float, y: float, rect: dict[str, Any]) -> bool:
    return float(rect["xmin"]) <= x <= float(rect["xmax"]) and float(rect["ymin"]) <= y <= float(rect["ymax"])


def point_in_polygon(x: float, y: float, points: list[dict[str, Any]]) -> bool:
    inside = False
    count = len(points)
    if count < 3:
        return False
    j = count - 1
    for i in range(count):
        xi = float(points[i]["x_mm"])
        yi = float(points[i]["y_mm"])
        xj = float(points[j]["x_mm"])
        yj = float(points[j]["y_mm"])
        intersects = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / ((yj - yi) or 1e-12) + xi)
        if intersects:
            inside = not inside
        j = i
    return inside


def ccw(ax: float, ay: float, bx: float, by: float, cx: float, cy: float) -> bool:
    return (cy - ay) * (bx - ax) > (by - ay) * (cx - ax)


def segments_intersect(seg1: tuple[float, float, float, float], seg2: tuple[float, float, float, float]) -> bool:
    ax, ay, bx, by = seg1
    cx, cy, dx, dy = seg2
    return ccw(ax, ay, cx, cy, dx, dy) != ccw(bx, by, cx, cy, dx, dy) and ccw(ax, ay, bx, by, cx, cy) != ccw(ax, ay, bx, by, dx, dy)


def segment_crosses_rect(segment: dict[str, Any], rect: dict[str, Any]) -> bool:
    x1 = float(segment["x1"])
    y1 = float(segment["y1"])
    x2 = float(segment["x2"])
    y2 = float(segment["y2"])
    if point_in_rect(x1, y1, rect) or point_in_rect(x2, y2, rect):
        return True
    edges = [
        (float(rect["xmin"]), float(rect["ymin"]), float(rect["xmax"]), float(rect["ymin"])),
        (float(rect["xmax"]), float(rect["ymin"]), float(rect["xmax"]), float(rect["ymax"])),
        (float(rect["xmax"]), float(rect["ymax"]), float(rect["xmin"]), float(rect["ymax"])),
        (float(rect["xmin"]), float(rect["ymax"]), float(rect["xmin"]), float(rect["ymin"])),
    ]
    current = (x1, y1, x2, y2)
    return any(segments_intersect(current, edge) for edge in edges)


def segment_crosses_polygon(segment: dict[str, Any], points: list[dict[str, Any]]) -> bool:
    if len(points) < 3:
        return False
    x1 = float(segment["x1"])
    y1 = float(segment["y1"])
    x2 = float(segment["x2"])
    y2 = float(segment["y2"])
    if point_in_polygon(x1, y1, points) or point_in_polygon(x2, y2, points):
        return True
    current = (x1, y1, x2, y2)
    for left, right in zip(points, points[1:] + points[:1]):
        edge = (
            float(left["x_mm"]),
            float(left["y_mm"]),
            float(right["x_mm"]),
            float(right["y_mm"]),
        )
        if segments_intersect(current, edge):
            return True
    return False


def segment_crosses_keepout(segment: dict[str, Any], keepout: dict[str, Any]) -> bool:
    geometry = str(keepout.get("geometry", "")).upper()
    if geometry == "POLYGON" and keepout.get("points"):
        return segment_crosses_polygon(segment, keepout["points"])
    return segment_crosses_rect(segment, keepout)


def payload_errors(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not str(payload.get("project", "")).strip():
        errors.append("project is missing")
    board = payload.get("board_outline", {})
    if not board:
        errors.append("board_outline is missing")
    else:
        for field in ("shape", "width_mm", "height_mm", "allowed_signal_layers"):
            if field not in board:
                errors.append(f"board_outline missing {field}")
    net_classes = get_net_class_map(payload)
    if not net_classes:
        errors.append("net_classes is missing or empty")
    nets = payload.get("nets", [])
    if not nets:
        errors.append("nets is missing or empty")
    for net in nets:
        name = str(net.get("name", "")).strip()
        if not name:
            errors.append("net missing name")
            continue
        role = str(net.get("role", "")).strip()
        if not role:
            errors.append(f"{name}: missing role")
        net_class = str(net.get("net_class", "")).strip()
        if not net_class:
            errors.append(f"{name}: missing net_class")
        elif net_class not in net_classes:
            errors.append(f"{name}: unknown net_class {net_class}")
        if "routing_status" not in net:
            errors.append(f"{name}: missing routing_status")
    for keepout in payload.get("keepouts", []):
        for field in ("name", "type", "xmin", "ymin", "xmax", "ymax"):
            if field not in keepout:
                errors.append(f"keepout missing {field}")
    for trace in get_traces(payload):
        if not str(trace.get("net", "")).strip():
            errors.append("trace missing net")
        for segment in trace.get("segments", []):
            for field in ("x1", "y1", "x2", "y2", "layer", "width_mm"):
                if field not in segment:
                    errors.append(f"trace segment missing {field}")
    return sorted(set(errors))


def payload_warnings(payload: dict[str, Any]) -> list[str]:
    warnings: list[str] = []
    if not payload.get("ground_strategy", {}).get("present", False):
        warnings.append("ground strategy missing")
    for net in payload.get("nets", []):
        name = str(net.get("name", "")).strip()
        role = str(net.get("role", "")).strip().upper()
        if role in {"USB_D+", "USB_D-"} and not str(net.get("paired_with", "")).strip():
            warnings.append(f"{name}: USB pair mate missing")
        if net.get("critical") and "routing_priority" not in net:
            warnings.append(f"{name}: critical net missing explicit routing_priority")
    return sorted(set(warnings))


def normalized_nets(payload: dict[str, Any]) -> list[dict[str, Any]]:
    net_classes = get_net_class_map(payload)
    keepout_names = {str(item.get("name", "")) for item in payload.get("keepouts", [])}
    normalized: list[dict[str, Any]] = []
    for net in payload.get("nets", []):
        name = str(net.get("name", "")).strip()
        role = str(net.get("role", "")).strip().upper()
        stage_name = routing_stage_for_role(role)
        net_class_name = str(net.get("net_class", "")).strip()
        class_data = net_classes.get(net_class_name, {})
        critical = bool(net.get("critical", net_is_critical(stage_name)))
        power = bool(net.get("power", "POWER" in role or name.startswith("+")))
        usb = bool(net.get("usb", role in {"USB_D+", "USB_D-", "USB_DP_DM"}))
        ground = bool(net.get("ground", name.upper() == "GND"))
        via_rule = net.get("via_rule", {})
        layer_rule = net.get("layer_rule", {})
        trace_width_rule = net.get("trace_width_rule", {})
        clearance_rule = net.get("clearance_rule", {})
        must_avoid = [item for item in net.get("must_avoid_keepouts", []) if item in keepout_names]
        traces = get_trace_for_net(payload, name)
        routing_status = str(net.get("routing_status", "UNROUTED")).upper()
        entry = {
            "name": name,
            "role": role,
            "stage_name": stage_name,
            "stage_index": STAGE_INDEX[stage_name],
            "routing_priority": int(net.get("routing_priority", 0)),
            "critical": critical,
            "power": power,
            "usb": usb,
            "ground": ground,
            "net_class": net_class_name,
            "width_mm": float(trace_width_rule.get("target_mm", class_data.get("width_mm", payload.get("trace_rules", {}).get("default_width_mm", 0.2)))),
            "clearance_mm": float(clearance_rule.get("mm", class_data.get("clearance_mm", payload.get("trace_rules", {}).get("default_clearance_mm", 0.15)))),
            "preferred_layers": layer_rule.get("preferred", payload.get("layer_rules", {}).get("power_preferred_layers" if power else "usb_preferred_layers" if usb else "default_signal_layer", ["F.Cu"])),
            "allowed_layers": layer_rule.get("allowed", class_data.get("allowed_layers", payload.get("layer_rules", {}).get("available_layers", ["F.Cu", "B.Cu"]))),
            "vias_allowed": bool(via_rule.get("allowed", class_data.get("via_allowed", payload.get("via_rules", {}).get("default_allowed", True)))),
            "via_reason_required": bool(via_rule.get("reason_required", payload.get("via_rules", {}).get("critical_reason_required", False) if critical else False)),
            "max_vias": int(via_rule.get("max_count", class_data.get("max_vias", payload.get("via_rules", {}).get("max_default_vias", 2)))),
            "paired_with": str(net.get("paired_with", "")).strip(),
            "must_avoid_keepouts": must_avoid,
            "routing_status": routing_status,
            "review_required": bool(net.get("review_required", usb or role in {"BUCK_SW", "BUCK_BST", "REGULATOR_LOOP", "REG_SW"})),
            "trace_count": len(traces),
            "trace_length_mm": round(sum(trace_length_mm(trace.get("segments", [])) for trace in traces), 3),
            "notes": net.get("notes", ""),
        }
        normalized.append(entry)
    normalized.sort(key=lambda item: (item["stage_index"], -item["routing_priority"], item["name"]))
    return normalized


def usb_pair_names(payload: dict[str, Any]) -> set[str]:
    names = set()
    for net in payload.get("nets", []):
        role = str(net.get("role", "")).strip().upper()
        if role in {"USB_D+", "USB_D-", "USB_DP_DM"} or bool(net.get("usb", False)):
            if net.get("name"):
                names.add(str(net["name"]))
    return names


def critical_net_names(payload: dict[str, Any]) -> set[str]:
    return {item["name"] for item in normalized_nets(payload) if item["critical"]}


def power_net_names(payload: dict[str, Any]) -> set[str]:
    return {item["name"] for item in normalized_nets(payload) if item["power"]}


def regulator_loop_present(payload: dict[str, Any]) -> bool:
    for net in payload.get("nets", []):
        role = str(net.get("role", "")).strip().upper()
        if role in {"REGULATOR_LOOP", "BUCK_SW", "BUCK_BST", "REG_SW"}:
            return True
    return False


def make_markdown(title: str, summary: dict[str, Any], sections: list[tuple[str, str]]) -> str:
    lines = [f"# {title}", ""]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.append("")
    for heading, body in sections:
        lines.append(f"## {heading}")
        lines.append("")
        lines.append(body.rstrip())
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    if not rows:
        return "_none_"
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return "\n".join(lines)
