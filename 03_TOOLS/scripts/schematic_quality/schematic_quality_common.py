#!/usr/bin/env python3
"""Shared read-only helpers for the schematic quality engine.

This module parses KiCad schematic S-expressions directly and builds enough
geometry metadata to support annotation, footprint, readability, spacing, and
wire-vs-label audits without editing design files.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import subprocess
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


CHECK_STATUS_PASS = "PASS"
CHECK_STATUS_WARN = "WARN"
CHECK_STATUS_FAIL = "FAIL"
CHECK_STATUS_NEEDS_HUMAN_REVIEW = "NEEDS_HUMAN_REVIEW"

MARKER_TOKENS = ("NEEDS_REVIEW", "BLOCKED", "UNVERIFIED", "TODO", "TBD")

BLOCK_DEFINITIONS = [
    {
        "id": "input_power_protection",
        "title": "Input Power / Protection",
        "heading_keywords": ("INPUT POWER", "POWER INPUT", "POWER / PROTECTION"),
        "seed_keywords": ("barrel", "jack", "polyfuse", "fuse", "pmos", "reverse polarity", "protection", "tvs", "+5v_in", "+5v_fused"),
    },
    {
        "id": "buck_regulator",
        "title": "Buck Regulator",
        "heading_keywords": ("BUCK REGULATOR", "3V3 BUCK", "REGULATOR"),
        "seed_keywords": ("buck", "regulator", "ap63203", "ldo", "inductor", "buck_sw", "buck_bst", "+3v3"),
    },
    {
        "id": "esp32_module",
        "title": "ESP32 Module",
        "heading_keywords": ("ESP32", "ESP32-S3 MODULE"),
        "seed_keywords": ("esp32", "wroom", "rf_module"),
    },
    {
        "id": "usb_c_data",
        "title": "USB-C / ESD / CC / Data",
        "heading_keywords": ("USB-C", "USB C", "USB2", "USB-C USB2"),
        "seed_keywords": ("usb-c", "usb_c", "receptacle", "tpd2eusb", "cc1", "cc2", "usb_d+", "usb_d-", "dp_c", "dm_c", "dp_e", "dm_e"),
    },
    {
        "id": "reset_boot",
        "title": "Reset / Boot",
        "heading_keywords": ("RESET / BOOT", "RESET", "BOOT"),
        "seed_keywords": ("boot", "reset", "gpio0", "esp_en", "en", "switch"),
    },
    {
        "id": "leds",
        "title": "LEDs",
        "heading_keywords": ("LEDS", "LED"),
        "seed_keywords": ("led", "status_led", "power_led", "sled", "pled"),
    },
    {
        "id": "test_debug",
        "title": "Test Pads / Debug",
        "heading_keywords": ("TEST / DEBUG", "TEST PADS", "DEBUG"),
        "seed_keywords": ("testpoint", "test point", "testpad", "uart", "debug", "tp"),
    },
    {
        "id": "mechanical_notes",
        "title": "Mounting / Mechanical Notes",
        "heading_keywords": ("MOUNTING HOLES", "MECHANICAL NOTES", "MECHANICAL"),
        "seed_keywords": ("mountinghole", "mounting hole", "mechanical", "mh"),
    },
]

BLOCK_INDEX = {item["id"]: item for item in BLOCK_DEFINITIONS}
BLOCK_ORDER = [item["id"] for item in BLOCK_DEFINITIONS]


def decode_atom(token: str) -> str:
    if token.startswith('"') and token.endswith('"'):
        try:
            return json.loads(token)
        except json.JSONDecodeError:
            return token[1:-1]
    return token


def tokenize_sexpr(text: str) -> list[str]:
    return re.findall(r'"(?:\\.|[^"\\])*"|[()]|[^\s()]+', text)


def parse_tokens(tokens: list[str]) -> list[Any]:
    index = 0

    def parse_one() -> Any:
        nonlocal index
        if index >= len(tokens):
            raise ValueError("unexpected end of token stream")
        token = tokens[index]
        index += 1
        if token == "(":
            node: list[Any] = []
            while index < len(tokens) and tokens[index] != ")":
                node.append(parse_one())
            if index >= len(tokens):
                raise ValueError("missing closing parenthesis")
            index += 1
            return node
        if token == ")":
            raise ValueError("unexpected closing parenthesis")
        return decode_atom(token)

    parsed: list[Any] = []
    while index < len(tokens):
        parsed.append(parse_one())
    return parsed[0] if len(parsed) == 1 else parsed


def load_schematic(path: Path) -> list[Any]:
    return parse_tokens(tokenize_sexpr(path.read_text(encoding="utf-8", errors="replace")))


def walk_lists(node: Any) -> list[list[Any]]:
    found: list[list[Any]] = []
    if isinstance(node, list):
        found.append(node)
        for child in node:
            found.extend(walk_lists(child))
    return found


def child_lists(node: list[Any], name: str) -> list[list[Any]]:
    return [child for child in node if isinstance(child, list) and child and child[0] == name]


def direct_child(node: list[Any], name: str) -> list[Any] | None:
    for child in child_lists(node, name):
        return child
    return None


def first_child_value(node: list[Any], name: str, index: int = 1, default: str = "") -> str:
    child = direct_child(node, name)
    if child and len(child) > index and isinstance(child[index], str):
        return child[index]
    return default


def float_or(default: float, value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def parse_at(node: list[Any]) -> dict[str, float]:
    at = direct_child(node, "at")
    if not at:
        return {"x": 0.0, "y": 0.0, "rotation": 0.0}
    return {
        "x": float_or(0.0, at[1] if len(at) > 1 else 0.0),
        "y": float_or(0.0, at[2] if len(at) > 2 else 0.0),
        "rotation": float_or(0.0, at[3] if len(at) > 3 else 0.0),
    }


def parse_effects(node: list[Any]) -> dict[str, Any]:
    effects = direct_child(node, "effects")
    result = {
        "hidden": False,
        "font_width": 1.016,
        "font_height": 1.016,
        "justify": "left",
    }
    if not effects:
        return result
    if direct_child(effects, "hide"):
        result["hidden"] = True
    font = direct_child(effects, "font")
    if font:
        size = direct_child(font, "size")
        if size and len(size) >= 3:
            result["font_width"] = float_or(1.016, size[1])
            result["font_height"] = float_or(1.016, size[2])
    justify = direct_child(effects, "justify")
    if justify and len(justify) >= 2 and isinstance(justify[1], str):
        result["justify"] = justify[1]
    return result


def symbol_properties(symbol: list[Any]) -> dict[str, dict[str, Any]]:
    props: dict[str, dict[str, Any]] = {}
    for child in child_lists(symbol, "property"):
        if len(child) < 3 or not isinstance(child[1], str):
            continue
        at = parse_at(child)
        effects = parse_effects(child)
        props[child[1]] = {
            "value": child[2] if isinstance(child[2], str) else "",
            "at": at,
            "effects": effects,
        }
    return props


def normalize_text(*parts: object) -> str:
    return " ".join(str(part or "") for part in parts).lower()


def is_power_symbol(symbol: dict[str, Any]) -> bool:
    ref = str(symbol.get("reference", "")).upper()
    lib_id = str(symbol.get("lib_id", "")).lower()
    return ref.startswith("#PWR") or ref.startswith("#FLG") or lib_id.startswith("power:")


def is_physical_symbol(symbol: dict[str, Any]) -> bool:
    if is_power_symbol(symbol):
        return False
    ref = str(symbol.get("reference", "")).upper()
    if ref.startswith("#"):
        return False
    return True


def reference_prefix(reference: str) -> str:
    match = re.match(r"[A-Z]+", reference.strip().upper())
    return match.group(0) if match else ""


def parse_pts(node: list[Any]) -> list[tuple[float, float]]:
    pts_node = direct_child(node, "pts")
    points: list[tuple[float, float]] = []
    if not pts_node:
        return points
    for child in pts_node:
        if isinstance(child, list) and child and child[0] == "xy" and len(child) >= 3:
            points.append((float_or(0.0, child[1]), float_or(0.0, child[2])))
    return points


def collect_lib_geometry(node: list[Any], points: list[tuple[float, float]], pin_points: list[tuple[float, float]]) -> None:
    if not isinstance(node, list) or not node:
        return
    name = node[0]
    if name == "rectangle":
        start = direct_child(node, "start")
        end = direct_child(node, "end")
        if start and end and len(start) >= 3 and len(end) >= 3:
            points.extend(
                [
                    (float_or(0.0, start[1]), float_or(0.0, start[2])),
                    (float_or(0.0, end[1]), float_or(0.0, end[2])),
                ]
            )
    elif name == "polyline":
        points.extend(parse_pts(node))
    elif name == "arc":
        for child_name in ("start", "mid", "end"):
            child = direct_child(node, child_name)
            if child and len(child) >= 3:
                points.append((float_or(0.0, child[1]), float_or(0.0, child[2])))
    elif name == "circle":
        center = direct_child(node, "center")
        radius = direct_child(node, "radius")
        if center and radius and len(center) >= 3 and len(radius) >= 3:
            cx = float_or(0.0, center[1])
            cy = float_or(0.0, center[2])
            rx = abs(float_or(cx, radius[1]) - cx)
            ry = abs(float_or(cy, radius[2]) - cy)
            points.extend([(cx - rx, cy - ry), (cx + rx, cy + ry)])
    elif name == "pin":
        at = parse_at(node)
        length_node = direct_child(node, "length")
        length = float_or(2.54, length_node[1] if length_node and len(length_node) > 1 else 2.54)
        x = at["x"]
        y = at["y"]
        rotation = int(at["rotation"]) % 360
        deltas = {
            0: (length, 0.0),
            90: (0.0, length),
            180: (-length, 0.0),
            270: (0.0, -length),
        }
        dx, dy = deltas.get(rotation, (0.0, 0.0))
        pin_points.extend([(x, y), (x + dx, y + dy)])
        points.extend([(x, y), (x + dx, y + dy)])

    for child in node:
        if isinstance(child, list):
            collect_lib_geometry(child, points, pin_points)


def points_bbox(points: list[tuple[float, float]]) -> dict[str, float]:
    if not points:
        return {"x1": -2.54, "y1": -2.54, "x2": 2.54, "y2": 2.54}
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    return {"x1": min(xs), "y1": min(ys), "x2": max(xs), "y2": max(ys)}


def build_library_metadata(root: list[Any]) -> dict[str, dict[str, Any]]:
    lib_symbols = direct_child(root, "lib_symbols")
    metadata: dict[str, dict[str, Any]] = {}
    if not lib_symbols:
        return metadata
    for child in lib_symbols:
        if not isinstance(child, list) or not child or child[0] != "symbol":
            continue
        if len(child) < 2 or not isinstance(child[1], str):
            continue
        lib_id = child[1]
        points: list[tuple[float, float]] = []
        pin_points: list[tuple[float, float]] = []
        collect_lib_geometry(child, points, pin_points)
        metadata[lib_id] = {"bbox": points_bbox(points), "pin_points": pin_points}
    return metadata


def transform_point(x: float, y: float, instance_at: dict[str, float], mirror: str = "") -> tuple[float, float]:
    if mirror == "x":
        x = -x
    elif mirror == "y":
        y = -y
    rotation = int(instance_at["rotation"]) % 360
    if rotation == 90:
        x, y = -y, x
    elif rotation == 180:
        x, y = -x, -y
    elif rotation == 270:
        x, y = y, -x
    return (instance_at["x"] + x, instance_at["y"] + y)


def transform_bbox(local_bbox: dict[str, float], instance_at: dict[str, float], mirror: str = "") -> dict[str, float]:
    corners = [
        (local_bbox["x1"], local_bbox["y1"]),
        (local_bbox["x1"], local_bbox["y2"]),
        (local_bbox["x2"], local_bbox["y1"]),
        (local_bbox["x2"], local_bbox["y2"]),
    ]
    transformed = [transform_point(x, y, instance_at, mirror) for x, y in corners]
    return points_bbox(transformed)


def bbox_center(bbox: dict[str, float]) -> tuple[float, float]:
    return ((bbox["x1"] + bbox["x2"]) / 2.0, (bbox["y1"] + bbox["y2"]) / 2.0)


def rect_distance(a: dict[str, float], b: dict[str, float]) -> float:
    dx = max(a["x1"] - b["x2"], b["x1"] - a["x2"], 0.0)
    dy = max(a["y1"] - b["y2"], b["y1"] - a["y2"], 0.0)
    return math.hypot(dx, dy)


def rects_overlap(a: dict[str, float], b: dict[str, float], margin: float = 0.0) -> bool:
    return not (
        a["x2"] < (b["x1"] - margin)
        or a["x1"] > (b["x2"] + margin)
        or a["y2"] < (b["y1"] - margin)
        or a["y1"] > (b["y2"] + margin)
    )


def estimate_text_bbox(text: str, at: dict[str, float], effects: dict[str, Any]) -> dict[str, float]:
    width = max(1.0, len(text) * effects["font_width"] * 0.58)
    height = max(1.0, effects["font_height"] * 1.25)
    x = at["x"]
    y = at["y"]
    justify = effects.get("justify", "left")
    rotation = int(at["rotation"]) % 360
    if justify == "right":
        x1 = x - width
        x2 = x
    elif justify == "center":
        x1 = x - width / 2.0
        x2 = x + width / 2.0
    else:
        x1 = x
        x2 = x + width
    y1 = y - height / 2.0
    y2 = y + height / 2.0
    if rotation in {90, 270}:
        cx = (x1 + x2) / 2.0
        cy = (y1 + y2) / 2.0
        half_w = height / 2.0
        half_h = width / 2.0
        return {"x1": cx - half_w, "y1": cy - half_h, "x2": cx + half_w, "y2": cy + half_h}
    return {"x1": x1, "y1": y1, "x2": x2, "y2": y2}


def extract_symbols(root: list[Any]) -> list[dict[str, Any]]:
    library = build_library_metadata(root)
    symbols: list[dict[str, Any]] = []
    for node in walk_lists(root):
        if not node or node[0] != "symbol":
            continue
        lib_id = first_child_value(node, "lib_id")
        if not lib_id:
            continue
        instance_at = parse_at(node)
        mirror = first_child_value(node, "mirror")
        props = symbol_properties(node)
        metadata = library.get(lib_id, {"bbox": {"x1": -2.54, "y1": -2.54, "x2": 2.54, "y2": 2.54}, "pin_points": []})
        bbox = transform_bbox(metadata["bbox"], instance_at, mirror)
        pin_points = [transform_point(x, y, instance_at, mirror) for x, y in metadata.get("pin_points", [])]
        symbols.append(
            {
                "lib_id": lib_id,
                "reference": str(props.get("Reference", {}).get("value", "")),
                "value": str(props.get("Value", {}).get("value", "")),
                "footprint": str(props.get("Footprint", {}).get("value", "")),
                "properties": props,
                "at": instance_at,
                "mirror": mirror,
                "bbox": bbox,
                "center": {"x": bbox_center(bbox)[0], "y": bbox_center(bbox)[1]},
                "pin_points": [{"x": point[0], "y": point[1]} for point in pin_points],
            }
        )
    return symbols


def symbol_search_text(symbol: dict[str, Any]) -> str:
    prop_text = " ".join(f"{name} {item.get('value', '')}" for name, item in symbol.get("properties", {}).items())
    return normalize_text(symbol.get("reference"), symbol.get("value"), symbol.get("lib_id"), symbol.get("footprint"), prop_text)


def extract_text_items(root: list[Any], symbols: list[dict[str, Any]]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for node in walk_lists(root):
        if not node or node[0] not in {"text", "label", "global_label", "hierarchical_label"}:
            continue
        if len(node) < 2 or not isinstance(node[1], str):
            continue
        at = parse_at(node)
        effects = parse_effects(node)
        items.append(
            {
                "kind": node[0],
                "text": node[1],
                "at": at,
                "effects": effects,
                "bbox": estimate_text_bbox(node[1], at, effects),
            }
        )

    for symbol in symbols:
        for prop_name, prop_data in symbol.get("properties", {}).items():
            effects = prop_data.get("effects", {})
            if effects.get("hidden"):
                continue
            text = str(prop_data.get("value", ""))
            if not text:
                continue
            items.append(
                {
                    "kind": f"property:{prop_name}",
                    "owner_reference": symbol.get("reference", ""),
                    "text": text,
                    "at": prop_data.get("at", {"x": 0.0, "y": 0.0, "rotation": 0.0}),
                    "effects": effects,
                    "bbox": estimate_text_bbox(text, prop_data.get("at", {"x": 0.0, "y": 0.0, "rotation": 0.0}), effects),
                }
            )
    return items


def extract_wire_segments(root: list[Any]) -> list[dict[str, Any]]:
    segments: list[dict[str, Any]] = []
    for node in walk_lists(root):
        if not node or node[0] != "wire":
            continue
        points = parse_pts(node)
        for start, end in zip(points, points[1:]):
            mid_x = (start[0] + end[0]) / 2.0
            mid_y = (start[1] + end[1]) / 2.0
            bbox = points_bbox([start, end])
            segments.append(
                {
                    "start": {"x": start[0], "y": start[1]},
                    "end": {"x": end[0], "y": end[1]},
                    "midpoint": {"x": mid_x, "y": mid_y},
                    "bbox": bbox,
                }
            )
    return segments


def heading_positions(text_items: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    headings: dict[str, dict[str, Any]] = {}
    for item in text_items:
        if item["kind"] != "text":
            continue
        upper = item["text"].upper()
        for block in BLOCK_DEFINITIONS:
            if any(keyword in upper for keyword in block["heading_keywords"]):
                headings[block["id"]] = item
    return headings


def classify_symbol_direct(symbol: dict[str, Any]) -> str:
    text = symbol_search_text(symbol)
    ref = str(symbol.get("reference", "")).upper()
    if "mountinghole" in text or ref.startswith("MH"):
        return "mechanical_notes"
    if ref.startswith("TP") or "testpoint" in text or "test point" in text or "debug" in text:
        return "test_debug"
    if "esp32" in text or "wroom" in text:
        return "esp32_module"
    if "usb-c" in text or "usb_c" in text or "receptacle" in text or "tpd2eusb" in text:
        return "usb_c_data"
    if ref.startswith("SW") or any(token in text for token in ("boot", "reset", "gpio0", "esp_en")):
        return "reset_boot"
    if "led" in text or ref.startswith("D") and "device:led" in text:
        return "leds"
    if any(token in text for token in ("barrel", "polyfuse", "fuse", "reverse polarity", "pmos", "jack", "+5v_in", "+5v_fused", "+5v_protected")):
        return "input_power_protection"
    if any(token in text for token in ("buck", "regulator", "ap63203", "inductor", "+3v3", "buck_sw", "buck_bst")):
        return "buck_regulator"
    return ""


def distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def assign_blocks(symbols: list[dict[str, Any]], headings: dict[str, dict[str, Any]]) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    blocks: dict[str, dict[str, Any]] = {
        block["id"]: {
            "block_id": block["id"],
            "title": block["title"],
            "heading_text": headings.get(block["id"], {}).get("text", ""),
            "heading_at": headings.get(block["id"], {}).get("at", {"x": 0.0, "y": 0.0}),
            "symbols": [],
        }
        for block in BLOCK_DEFINITIONS
    }
    unassigned: list[dict[str, Any]] = []

    for symbol in symbols:
        if is_power_symbol(symbol):
            continue
        direct = classify_symbol_direct(symbol)
        chosen = direct
        if not chosen and headings:
            symbol_point = (symbol["center"]["x"], symbol["center"]["y"])
            nearest_id = ""
            nearest_distance = float("inf")
            for block_id, heading in headings.items():
                heading_point = (heading["at"]["x"], heading["at"]["y"])
                current_distance = distance(symbol_point, heading_point)
                if current_distance < nearest_distance:
                    nearest_id = block_id
                    nearest_distance = current_distance
            if nearest_id:
                chosen = nearest_id
        if chosen and chosen in blocks:
            symbol["block_id"] = chosen
            blocks[chosen]["symbols"].append(symbol)
        else:
            symbol["block_id"] = ""
            unassigned.append(symbol)

    for block_id, block in blocks.items():
        points: list[tuple[float, float]] = []
        for symbol in block["symbols"]:
            bbox = symbol["bbox"]
            points.extend(
                [
                    (bbox["x1"], bbox["y1"]),
                    (bbox["x2"], bbox["y2"]),
                ]
            )
        if points:
            block["bbox"] = points_bbox(points)
        elif block["heading_text"]:
            x = block["heading_at"]["x"]
            y = block["heading_at"]["y"]
            block["bbox"] = {"x1": x - 5.0, "y1": y - 5.0, "x2": x + 5.0, "y2": y + 5.0}
        else:
            block["bbox"] = {"x1": 0.0, "y1": 0.0, "x2": 0.0, "y2": 0.0}
        center = bbox_center(block["bbox"])
        block["centroid"] = {"x": center[0], "y": center[1]}
        block["symbol_count"] = len(block["symbols"])
    return blocks, unassigned


def line_box_with_margin(segment: dict[str, Any], margin: float = 0.4) -> dict[str, float]:
    bbox = segment["bbox"]
    return {
        "x1": bbox["x1"] - margin,
        "y1": bbox["y1"] - margin,
        "x2": bbox["x2"] + margin,
        "y2": bbox["y2"] + margin,
    }


def check_record(status: str, code: str, message: str, reference: str = "", evidence: str = "") -> dict[str, str]:
    return {
        "status": status,
        "code": code,
        "reference": reference,
        "message": message,
        "evidence": evidence,
    }


def summarize_status(findings: list[dict[str, str]]) -> dict[str, Any]:
    counts = Counter(item["status"] for item in findings)
    if counts.get(CHECK_STATUS_FAIL, 0):
        result = CHECK_STATUS_FAIL
    elif counts.get(CHECK_STATUS_WARN, 0):
        result = CHECK_STATUS_WARN
    else:
        result = CHECK_STATUS_PASS
    return {
        "status": result,
        "counts": {
            CHECK_STATUS_PASS: counts.get(CHECK_STATUS_PASS, 0),
            CHECK_STATUS_WARN: counts.get(CHECK_STATUS_WARN, 0),
            CHECK_STATUS_FAIL: counts.get(CHECK_STATUS_FAIL, 0),
        },
    }


def build_audit_result(audit_id: str, title: str, schematic: Path, findings: list[dict[str, str]], extra: dict[str, Any] | None = None) -> dict[str, Any]:
    result: dict[str, Any] = {
        "audit_id": audit_id,
        "title": title,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "schematic": str(schematic),
        "findings": findings,
        "summary": summarize_status(findings),
    }
    if extra:
        result.update(extra)
    return result


def audit_markdown(result: dict[str, Any]) -> str:
    lines = [
        f"# {result['title']}",
        "",
        f"Status: `{result['summary']['status']}`",
        "",
        f"Generated: `{result['generated_at']}`",
        f"Schematic: `{result['schematic']}`",
        "",
        "## Summary",
        "",
        f"- Pass: {result['summary']['counts'][CHECK_STATUS_PASS]}",
        f"- Warn: {result['summary']['counts'][CHECK_STATUS_WARN]}",
        f"- Fail: {result['summary']['counts'][CHECK_STATUS_FAIL]}",
        "",
        "## Findings",
        "",
        "| Status | Code | Reference | Message | Evidence |",
        "| --- | --- | --- | --- | --- |",
    ]
    for finding in result["findings"]:
        lines.append(
            "| `{status}` | `{code}` | `{reference}` | {message} | `{evidence}` |".format(
                status=finding["status"],
                code=finding["code"],
                reference=finding.get("reference", ""),
                message=str(finding["message"]).replace("|", "\\|"),
                evidence=str(finding.get("evidence", "")).replace("|", "\\|"),
            )
        )
    lines.extend(
        [
            "",
            "## Limits",
            "",
            "- This is a read-only automated audit with estimated geometry where needed.",
            "- ERC pass alone is not readability proof.",
            "- Native annotation proof and human visual evidence remain separate gates.",
            "",
        ]
    )
    return "\n".join(lines)


def write_outputs(result: dict[str, Any], output: Path | None, json_output: Path | None) -> None:
    if json_output:
        json_output.parent.mkdir(parents=True, exist_ok=True)
        json_output.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    markdown = audit_markdown(result)
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(markdown, encoding="utf-8")
    else:
        print(markdown)


def common_parser(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--schematic", required=True, help="Path to .kicad_sch file.")
    parser.add_argument("--output", default="", help="Optional markdown output path.")
    parser.add_argument("--json-output", default="", help="Optional JSON output path.")
    parser.add_argument("--no-fail", action="store_true", help="Return exit code 0 even when findings fail.")
    return parser


def exit_code_for(result: dict[str, Any], no_fail: bool) -> int:
    if no_fail:
        return 0
    return 1 if result["summary"]["status"] == CHECK_STATUS_FAIL else 0


def detect_closeup_visual_status(project_root: Path) -> dict[str, str]:
    report_path = project_root / "reports" / "CLOSE_UP_REVIEW.md"
    if not report_path.exists():
        return {"status": CHECK_STATUS_FAIL, "evidence": str(report_path), "message": "Close-up visual review report is missing."}
    text = report_path.read_text(encoding="utf-8", errors="replace")
    status_match = re.search(r"Status:\s*`([^`]+)`", text)
    status = status_match.group(1) if status_match else "UNKNOWN"
    if status != "SCHEMATIC_VISUAL_PASS":
        return {
            "status": CHECK_STATUS_FAIL,
            "evidence": str(report_path),
            "message": f"Human-readable visual review is not passed; current status is {status}.",
        }
    if "Human visual result: `NOT_REVIEWED`" in text:
        return {
            "status": CHECK_STATUS_FAIL,
            "evidence": str(report_path),
            "message": "Close-up review still contains NOT_REVIEWED crop sections.",
        }
    return {"status": CHECK_STATUS_PASS, "evidence": str(report_path), "message": "Close-up visual review shows passed human review."}


def detect_native_annotation_status(project_root: Path) -> dict[str, str]:
    gate_path = project_root / "reports" / "SCHEMATIC_TO_PCB_GATE_STATUS.md"
    gui_report = project_root / "reports" / "KICAD_GUI_NATIVE_ANNOTATION_ERC_REPORT.md"
    if not gate_path.exists():
        return {"status": CHECK_STATUS_FAIL, "evidence": str(gate_path), "message": "Schematic-to-PCB gate report is missing."}
    text = gate_path.read_text(encoding="utf-8", errors="replace")
    gui_match = re.search(r"Current annotation GUI gate:\s*`([^`]+)`", text)
    gui_status = gui_match.group(1) if gui_match else ""
    if gui_status and gui_status != "PASS":
        return {
            "status": CHECK_STATUS_FAIL,
            "evidence": str(gate_path),
            "message": f"Native annotation GUI gate is not passed: {gui_status}.",
        }
    if gui_report.exists():
        return {"status": CHECK_STATUS_PASS, "evidence": str(gui_report), "message": "Native annotation ERC evidence exists."}
    return {
        "status": CHECK_STATUS_WARN,
        "evidence": str(gate_path),
        "message": "No explicit failing GUI annotation gate was found, but direct native annotation evidence file is missing.",
    }


def run_erc(schematic: Path, output_path: Path) -> dict[str, str]:
    cli = shutil.which("kicad-cli")
    if not cli:
        return {"status": CHECK_STATUS_FAIL, "evidence": "", "message": "kicad-cli is not available on PATH."}
    output_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [cli, "sch", "erc", "--format", "report", "--severity-all", "--output", str(output_path), str(schematic)]
    completed = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
    if completed.returncode != 0:
        return {
            "status": CHECK_STATUS_FAIL,
            "evidence": str(output_path),
            "message": f"kicad-cli sch erc returned {completed.returncode}: {(completed.stderr or completed.stdout).strip()}",
        }
    report_text = output_path.read_text(encoding="utf-8", errors="replace") if output_path.exists() else completed.stdout
    if re.search(r"ERC messages:\s*0\s+Errors\s+0\s+Warnings\s+0", report_text):
        return {"status": CHECK_STATUS_PASS, "evidence": str(output_path), "message": "ERC report shows 0 errors and 0 warnings."}
    return {"status": CHECK_STATUS_FAIL, "evidence": str(output_path), "message": "ERC report contains warnings or errors."}


def find_project_schematic(project_root: Path) -> Path:
    kicad_dir = project_root / "kicad"
    candidates = sorted(kicad_dir.glob("*.kicad_sch"))
    if not candidates:
        raise FileNotFoundError(f"No .kicad_sch files found under {kicad_dir}")
    return candidates[0]


def default_output_dir(project_root: Path) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return project_root / "reports" / "schematic_quality" / timestamp

