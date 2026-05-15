#!/usr/bin/env python3
"""Read-only human-drafting checker for KiCad schematics.

This checker complements ERC and basic overlap audits by combining:

- .kicad_sch object parsing for geometry and object-type truth
- read-only netlist export for saved electrical truth
- heuristic checks for label shortcuts, local MCU support wiring, reset/boot
  topology, text ownership, and local wire-path quality
"""

from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

from schematic_quality_common import (
    assign_blocks,
    bbox_center,
    default_output_dir,
    extract_symbols,
    extract_text_items,
    find_project_schematic,
    heading_positions,
    load_schematic,
    parse_pts,
    points_bbox,
    rect_distance,
    rects_overlap,
    symbol_search_text,
    walk_lists,
)


STATUS_INFO = "INFO"
STATUS_WARN = "WARN"
STATUS_FAIL = "FAIL"

POWER_LABELS = {
    "GND",
    "AGND",
    "PGND",
    "DGND",
    "VCC",
    "VDD",
    "VBUS",
    "+3V3",
    "+5V",
    "+5V_IN",
    "+5V_FUSED",
    "+5V_PROTECTED",
}
DEBUG_LABELS = {
    "U0RXD",
    "U0TXD",
    "RX",
    "TX",
    "UART_RX",
    "UART_TX",
    "SWDIO",
    "SWCLK",
}
FOCUS_NETS = {
    "ESP_EN": ("/ESP_EN", "ESP_EN"),
    "BOOT0": ("/BOOT0", "BOOT0", "/IO0", "IO0"),
    "STATUS_LED": ("STATUS_LED", "/STATUS_LED"),
    "+3V3": ("+3V3", "/+3V3"),
    "GND": ("GND", "/GND"),
}
SUPPORT_NAME_TOKENS = ("EN", "ESP_EN", "RESET", "RST", "BOOT", "BOOT0", "IO0", "STATUS_LED")
GRAPHIC_ITEM_NAMES = {"polyline", "rectangle", "arc", "circle", "bezier"}


def point_in_bbox(x: float, y: float, bbox: dict[str, float], margin: float = 0.0) -> bool:
    return (bbox["x1"] - margin) <= x <= (bbox["x2"] + margin) and (bbox["y1"] - margin) <= y <= (bbox["y2"] + margin)


def distance_points(first: tuple[float, float], second: tuple[float, float]) -> float:
    return math.hypot(first[0] - second[0], first[1] - second[1])


def rect_center(rect: dict[str, float]) -> tuple[float, float]:
    return bbox_center(rect)


def line_length(points: list[tuple[float, float]]) -> float:
    return sum(distance_points(points[index], points[index + 1]) for index in range(len(points) - 1))


def bbox_width(bbox: dict[str, float]) -> float:
    return abs(bbox["x2"] - bbox["x1"])


def bbox_height(bbox: dict[str, float]) -> float:
    return abs(bbox["y2"] - bbox["y1"])


def looks_like_power_label(text: str) -> bool:
    upper = text.strip().upper()
    return upper in POWER_LABELS or upper.startswith("+")


def looks_like_debug_label(text: str) -> bool:
    upper = text.strip().upper()
    return upper in DEBUG_LABELS or upper.startswith("TP_") or upper.endswith("_DBG")


def label_net_candidates(text: str) -> list[str]:
    stripped = text.strip()
    if not stripped:
        return []
    if stripped.startswith("/"):
        return [stripped, stripped[1:]]
    candidates = [f"/{stripped}", stripped]
    if stripped.startswith("+"):
        candidates = [stripped, f"/{stripped}"]
    return candidates


def build_symbol_lookup(symbols: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {str(symbol.get("reference", "")): symbol for symbol in symbols if symbol.get("reference")}


def nearest_block_id(point: tuple[float, float], blocks: dict[str, dict[str, Any]]) -> str:
    for block_id, block in blocks.items():
        if point_in_bbox(point[0], point[1], block["bbox"], margin=3.0):
            return block_id
    nearest = ""
    nearest_distance = float("inf")
    for block_id, block in blocks.items():
        center = (block["centroid"]["x"], block["centroid"]["y"])
        current_distance = distance_points(point, center)
        if current_distance < nearest_distance:
            nearest = block_id
            nearest_distance = current_distance
    return nearest


def nearby_symbols(point: tuple[float, float], symbols: list[dict[str, Any]], radius_mm: float = 25.0) -> list[dict[str, Any]]:
    nearby: list[dict[str, Any]] = []
    for symbol in symbols:
        current_distance = rect_distance(
            {"x1": point[0], "y1": point[1], "x2": point[0], "y2": point[1]},
            symbol["bbox"],
        )
        if current_distance <= radius_mm:
            nearby.append(symbol)
    return nearby


def maybe_write_report(output_dir: Path, stem: str, data: str) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / stem
    path.write_text(data, encoding="utf-8")
    return path


def choose_output_dir(project_root: Path | None, schematic: Path, output_dir_value: str) -> Path | None:
    if output_dir_value:
        return Path(output_dir_value)
    if project_root is not None:
        return default_output_dir(project_root)
    return None


def export_netlist_xml(schematic: Path) -> dict[str, Any]:
    cli = shutil.which("kicad-cli")
    if not cli:
        return {
            "available": False,
            "error": "kicad-cli is not available on PATH.",
            "nets": {},
            "components": {},
            "node_to_net": {},
        }

    with tempfile.TemporaryDirectory(prefix="kicad_human_drafting_") as temp_dir:
        xml_path = Path(temp_dir) / "netlist.xml"
        command = [
            cli,
            "sch",
            "export",
            "netlist",
            "--format",
            "kicadxml",
            "--output",
            str(xml_path),
            str(schematic),
        ]
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        if completed.returncode != 0 or not xml_path.exists():
            return {
                "available": False,
                "error": (completed.stderr or completed.stdout).strip() or f"netlist export failed with {completed.returncode}",
                "nets": {},
                "components": {},
                "node_to_net": {},
            }

        xml_root = ET.parse(xml_path).getroot()
        components: dict[str, dict[str, Any]] = {}
        for comp in xml_root.findall("./components/comp"):
            ref = comp.attrib.get("ref", "")
            if not ref:
                continue
            components[ref] = {
                "value": comp.findtext("value", default=""),
                "footprint": comp.findtext("footprint", default=""),
                "datasheet": comp.findtext("datasheet", default=""),
                "fields": {field.attrib.get("name", ""): field.text or "" for field in comp.findall("./fields/field")},
            }

        nets: dict[str, list[dict[str, str]]] = {}
        node_to_net: dict[tuple[str, str], str] = {}
        for net in xml_root.findall("./nets/net"):
            net_name = net.attrib.get("name", "")
            nodes: list[dict[str, str]] = []
            for node in net.findall("./node"):
                ref = node.attrib.get("ref", "")
                pin = node.attrib.get("pin", "")
                node_data = {
                    "ref": ref,
                    "pin": pin,
                    "pinfunction": node.attrib.get("pinfunction", ""),
                    "pintype": node.attrib.get("pintype", ""),
                }
                nodes.append(node_data)
                if ref and pin:
                    node_to_net[(ref, pin)] = net_name
            nets[net_name] = nodes

        return {
            "available": True,
            "error": "",
            "nets": nets,
            "components": components,
            "node_to_net": node_to_net,
        }


def extract_wire_paths(root: list[Any]) -> list[dict[str, Any]]:
    paths: list[dict[str, Any]] = []
    for node in walk_lists(root):
        if not node or node[0] != "wire":
            continue
        points = parse_pts(node)
        if len(points) < 2:
            continue
        path_length = line_length(points)
        direct = distance_points(points[0], points[-1])
        directions: list[str] = []
        orientation_changes = 0
        last_direction = ""
        uturn = False
        for index in range(len(points) - 1):
            start = points[index]
            end = points[index + 1]
            dx = end[0] - start[0]
            dy = end[1] - start[1]
            if abs(dx) > abs(dy):
                direction = "H"
            elif abs(dy) > abs(dx):
                direction = "V"
            else:
                direction = "D"
            directions.append(direction)
            if last_direction and direction != last_direction:
                orientation_changes += 1
            last_direction = direction
        for index in range(len(points) - 2):
            first = points[index]
            second = points[index + 1]
            third = points[index + 2]
            if first[0] == second[0] == third[0]:
                if (second[1] - first[1]) * (third[1] - second[1]) < 0:
                    uturn = True
            if first[1] == second[1] == third[1]:
                if (second[0] - first[0]) * (third[0] - second[0]) < 0:
                    uturn = True
        paths.append(
            {
                "points": points,
                "bbox": points_bbox(points),
                "path_length": path_length,
                "direct_length": direct,
                "orientation_changes": orientation_changes,
                "directions": directions,
                "uturn": uturn,
            }
        )
    return paths


def extract_top_level_graphic_items(root: list[Any]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for child in root:
        if not isinstance(child, list) or not child:
            continue
        kind = str(child[0])
        if kind not in GRAPHIC_ITEM_NAMES:
            continue
        points: list[tuple[float, float]] = []
        if kind == "polyline":
            points = parse_pts(child)
        elif kind == "rectangle":
            start = next((item for item in child if isinstance(item, list) and item and item[0] == "start"), None)
            end = next((item for item in child if isinstance(item, list) and item and item[0] == "end"), None)
            if start and end and len(start) >= 3 and len(end) >= 3:
                points = [
                    (float(start[1]), float(start[2])),
                    (float(end[1]), float(end[2])),
                ]
        elif kind == "arc":
            for name in ("start", "mid", "end"):
                point = next((item for item in child if isinstance(item, list) and item and item[0] == name), None)
                if point and len(point) >= 3:
                    points.append((float(point[1]), float(point[2])))
        elif kind == "circle":
            center = next((item for item in child if isinstance(item, list) and item and item[0] == "center"), None)
            radius = next((item for item in child if isinstance(item, list) and item and item[0] == "radius"), None)
            if center and radius and len(center) >= 3 and len(radius) >= 3:
                cx = float(center[1])
                cy = float(center[2])
                rx = abs(float(radius[1]) - cx)
                ry = abs(float(radius[2]) - cy)
                points = [(cx - rx, cy - ry), (cx + rx, cy + ry)]
        if not points:
            continue
        bbox = points_bbox(points)
        items.append(
            {
                "kind": kind,
                "bbox": bbox,
                "width": bbox_width(bbox),
                "height": bbox_height(bbox),
                "point_count": len(points),
            }
        )
    return items


def lookup_net(netlist: dict[str, Any], label_text: str) -> tuple[str, list[dict[str, str]]]:
    for candidate in label_net_candidates(label_text):
        if candidate in netlist["nets"]:
            return candidate, netlist["nets"][candidate]
    return "", []


def is_support_net_name(label_text: str, nodes: list[dict[str, str]]) -> bool:
    upper = label_text.strip().upper()
    if upper in SUPPORT_NAME_TOKENS:
        return True
    for node in nodes:
        pinfunction = str(node.get("pinfunction", "")).upper()
        if pinfunction in {"EN", "IO0"}:
            return True
    return False


def focus_net_summary(netlist: dict[str, Any], components: dict[str, dict[str, Any]]) -> dict[str, Any]:
    summary: dict[str, Any] = {}
    for key, candidates in FOCUS_NETS.items():
        resolved_name = ""
        nodes: list[dict[str, str]] = []
        for candidate in candidates:
            if candidate in netlist["nets"]:
                resolved_name = candidate
                nodes = netlist["nets"][candidate]
                break
        summary[key] = {
            "resolved_name": resolved_name,
            "present": bool(resolved_name),
            "nodes": [
                {
                    "ref": node["ref"],
                    "pin": node["pin"],
                    "pinfunction": node.get("pinfunction", ""),
                    "value": components.get(node["ref"], {}).get("value", ""),
                }
                for node in nodes
            ],
        }
    return summary


def classify_label_items(
    labels: list[dict[str, Any]],
    blocks: dict[str, dict[str, Any]],
    symbols: list[dict[str, Any]],
    netlist: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for label in labels:
        grouped[label["text"]].append(label)

    classifications: list[dict[str, Any]] = []
    findings: list[dict[str, Any]] = []

    for text, items in grouped.items():
        resolved_net, nodes = lookup_net(netlist, text)
        point_blocks = [nearest_block_id((item["at"]["x"], item["at"]["y"]), blocks) for item in items]
        block_count = len({block_id for block_id in point_blocks if block_id})
        max_distance = 0.0
        for index, first in enumerate(items):
            for second in items[index + 1 :]:
                max_distance = max(
                    max_distance,
                    distance_points((first["at"]["x"], first["at"]["y"]), (second["at"]["x"], second["at"]["y"])),
                )

        if looks_like_power_label(text):
            classification = "KEEP_POWER_RAIL"
            status = STATUS_INFO
            message = "Power or ground rail label is acceptable."
        elif looks_like_debug_label(text):
            classification = "KEEP_DEBUG_LABEL"
            status = STATUS_INFO
            message = "Debug or review anchor label is acceptable."
        elif is_support_net_name(text, nodes):
            if len(items) >= 2 or len(nodes) <= 5:
                classification = "POSSIBLE_REPLACE_WITH_WIRE"
                status = STATUS_WARN
                message = "Local MCU support net still relies on labels; review physical wiring before keeping it."
            else:
                classification = "REVIEW_LOCAL_LABEL"
                status = STATUS_WARN
                message = "Local MCU support label needs justification because the support circuit is compact."
        elif any(node["ref"].startswith("TP") for node in nodes) and any(node["ref"].startswith("U") for node in nodes):
            classification = "KEEP_CROSS_BLOCK_SIGNAL"
            status = STATUS_INFO
            message = "Label appears to be a compact module-to-test-anchor signal and is acceptable."
        elif len(items) >= 2 and block_count <= 2 and len(nodes) <= 6 and max_distance <= 120.0:
            classification = "POSSIBLE_REPLACE_WITH_WIRE"
            status = STATUS_WARN
            message = "Repeated local labels appear close enough to review as a wire-first drafting problem."
        elif len(items) >= 2:
            classification = "KEEP_CROSS_BLOCK_SIGNAL"
            status = STATUS_INFO
            message = "Repeated label looks like an intentional cross-block signal."
        else:
            classification = "REVIEW_LOCAL_LABEL"
            status = STATUS_WARN
            message = "Single local label should be justified against a short physical wire."

        classifications.append(
            {
                "label": text,
                "count": len(items),
                "resolved_net": resolved_net,
                "classification": classification,
                "blocks": point_blocks,
                "node_count": len(nodes),
                "max_pair_distance_mm": round(max_distance, 2),
            }
        )
        findings.append(
            {
                "status": status,
                "code": classification,
                "category": "local_label_usage",
                "reference": text,
                "message": message,
                "evidence": f"count={len(items)}, blocks={','.join(point_blocks)}, net={resolved_net or 'UNRESOLVED'}",
            }
        )

    return classifications, findings


def audit_graphic_items(
    graphics: list[dict[str, Any]],
    wires: list[dict[str, Any]],
    power_symbols: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    if not graphics:
        return [
            {
                "status": STATUS_INFO,
                "code": "NO_TOP_LEVEL_GRAPHIC_LINES",
                "category": "graphic_line_risk",
                "reference": "",
                "message": "No top-level graphic line objects were found in the sheet body.",
                "evidence": "graphic_count=0",
            }
        ]

    for index, item in enumerate(graphics, start=1):
        looks_like_rail = (item["width"] >= 8.0 and item["height"] <= 1.5) or (item["height"] >= 8.0 and item["width"] <= 1.5)
        near_wire = any(rect_distance(item["bbox"], wire["bbox"]) <= 1.2 for wire in wires)
        near_power = any(rect_distance(item["bbox"], symbol["bbox"]) <= 2.0 for symbol in power_symbols)
        if looks_like_rail and (near_wire or near_power):
            findings.append(
                {
                    "status": STATUS_WARN,
                    "code": "GRAPHIC_RAIL_NEAR_ELECTRICAL_NET",
                    "category": "graphic_line_risk",
                    "reference": f"graphic_{index}",
                    "message": "Graphic item looks like a rail near electrical content; do not treat it as electrical proof.",
                    "evidence": f"kind={item['kind']}, width={item['width']:.2f}, height={item['height']:.2f}",
                }
            )
        else:
            findings.append(
                {
                    "status": STATUS_INFO,
                    "code": "GRAPHIC_ITEM_PRESENT",
                    "category": "graphic_line_risk",
                    "reference": f"graphic_{index}",
                    "message": "Graphic item found, but it does not currently look like a suspicious electrical rail.",
                    "evidence": f"kind={item['kind']}, width={item['width']:.2f}, height={item['height']:.2f}",
                }
            )
    return findings


def audit_orientation_before_label(
    classifications: list[dict[str, Any]],
    netlist: dict[str, Any],
) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for item in classifications:
        if item["classification"] not in {"POSSIBLE_REPLACE_WITH_WIRE", "REVIEW_LOCAL_LABEL"}:
            continue
        if item["count"] >= 2 and item["node_count"] <= 6:
            findings.append(
                {
                    "status": STATUS_WARN,
                    "code": "ORIENT_SYMBOLS_BEFORE_LABELS_REVIEW",
                    "category": "orientation_before_label",
                    "reference": item["label"],
                    "message": "Repeated local labels suggest symbol orientation or positioning should be reviewed before keeping label shortcuts.",
                    "evidence": f"count={item['count']}, node_count={item['node_count']}, blocks={','.join(item['blocks'])}",
                }
            )
    if not findings:
        findings.append(
            {
                "status": STATUS_INFO,
                "code": "NO_OBVIOUS_ORIENTATION_LABEL_SHORTCUTS",
                "category": "orientation_before_label",
                "reference": "",
                "message": "No repeated local-label pattern clearly indicated an orientation-before-label drafting shortcut.",
                "evidence": "",
            }
        )
    return findings


def audit_mcu_local_support(
    classifications: list[dict[str, Any]],
    focus_summary: dict[str, Any],
) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for item in classifications:
        upper = item["label"].strip().upper()
        if upper not in {"ESP_EN", "BOOT0", "STATUS_LED"}:
            continue
        if item["classification"] in {"POSSIBLE_REPLACE_WITH_WIRE", "REVIEW_LOCAL_LABEL"}:
            findings.append(
                {
                    "status": STATUS_WARN,
                    "code": "MCU_LOCAL_SUPPORT_PHYSICAL_WIRING_REVIEW",
                    "category": "mcu_local_support",
                    "reference": item["label"],
                    "message": "MCU local support net still relies on labels and should be justified against a direct physical wire.",
                    "evidence": f"classification={item['classification']}, resolved_net={item['resolved_net'] or 'UNRESOLVED'}",
                }
            )

    status_led = focus_summary.get("STATUS_LED", {})
    if not status_led.get("present", False):
        findings.append(
            {
                "status": STATUS_WARN,
                "code": "STATUS_LED_NET_NAME_MISSING",
                "category": "mcu_local_support",
                "reference": "STATUS_LED",
                "message": "A named STATUS_LED net was not preserved in the saved netlist.",
                "evidence": "focus_net_missing",
            }
        )
    if not findings:
        findings.append(
            {
                "status": STATUS_INFO,
                "code": "MCU_LOCAL_SUPPORT_LABELS_ACCEPTABLE",
                "category": "mcu_local_support",
                "reference": "",
                "message": "No obvious local MCU support label shortcuts were detected.",
                "evidence": "",
            }
        )
    return findings


def nets_for_ref(netlist: dict[str, Any], ref: str) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for (node_ref, pin), net_name in netlist["node_to_net"].items():
        if node_ref == ref:
            mapping[pin] = net_name
    return mapping


def classify_switch_role(symbol: dict[str, Any], nets: dict[str, str]) -> str:
    text = symbol_search_text(symbol)
    joined_nets = " ".join(nets.values()).lower()
    if "reset" in text or "esp_en" in joined_nets or " /esp_en " in f" {joined_nets} ":
        return "reset"
    if "boot" in text or "io0" in joined_nets or "boot0" in joined_nets:
        return "boot"
    return "unknown"


def audit_reset_boot_topology(
    symbols_by_ref: dict[str, dict[str, Any]],
    netlist: dict[str, Any],
) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []

    for ref, symbol in symbols_by_ref.items():
        if not ref.startswith("SW"):
            continue
        switch_nets = nets_for_ref(netlist, ref)
        if len(switch_nets) < 2:
            findings.append(
                {
                    "status": STATUS_WARN,
                    "code": "SWITCH_NETS_INCOMPLETE",
                    "category": "reset_boot_topology",
                    "reference": ref,
                    "message": "Switch net mapping is incomplete; topology review is ambiguous.",
                    "evidence": f"nets={switch_nets}",
                }
            )
            continue
        net_set = set(switch_nets.values())
        role = classify_switch_role(symbol, switch_nets)
        if net_set == {"+3V3", "GND"}:
            findings.append(
                {
                    "status": STATUS_FAIL,
                    "code": "SWITCH_DIRECT_3V3_TO_GND_SHORT",
                    "category": "reset_boot_topology",
                    "reference": ref,
                    "message": "Switch directly shorts +3V3 to GND when pressed.",
                    "evidence": f"role={role}, nets={sorted(net_set)}",
                }
            )
        elif role == "reset" and net_set != {"/ESP_EN", "GND"}:
            findings.append(
                {
                    "status": STATUS_FAIL,
                    "code": "RESET_SWITCH_TOPOLOGY_REVIEW",
                    "category": "reset_boot_topology",
                    "reference": ref,
                    "message": "Reset switch does not resolve to the expected ESP_EN-to-GND topology.",
                    "evidence": f"nets={sorted(net_set)}",
                }
            )
        elif role == "boot" and net_set != {"/BOOT0", "GND"}:
            findings.append(
                {
                    "status": STATUS_FAIL,
                    "code": "BOOT_SWITCH_TOPOLOGY_REVIEW",
                    "category": "reset_boot_topology",
                    "reference": ref,
                    "message": "Boot switch does not resolve to the expected BOOT0-to-GND topology.",
                    "evidence": f"nets={sorted(net_set)}",
                }
            )

    for ref, symbol in symbols_by_ref.items():
        if not ref.startswith("R"):
            continue
        text = symbol_search_text(symbol).upper()
        resistor_nets = set(nets_for_ref(netlist, ref).values())
        if "10K_EN" in text and resistor_nets and resistor_nets != {"+3V3", "/ESP_EN"}:
            findings.append(
                {
                    "status": STATUS_FAIL,
                    "code": "EN_PULLUP_NET_REVIEW",
                    "category": "reset_boot_topology",
                    "reference": ref,
                    "message": "EN pull-up resistor is not mapped between +3V3 and /ESP_EN.",
                    "evidence": f"nets={sorted(resistor_nets)}",
                }
            )
        if "10K_BOOT" in text and resistor_nets and resistor_nets != {"+3V3", "/BOOT0"}:
            findings.append(
                {
                    "status": STATUS_FAIL,
                    "code": "BOOT_PULLUP_NET_REVIEW",
                    "category": "reset_boot_topology",
                    "reference": ref,
                    "message": "BOOT pull-up resistor is not mapped between +3V3 and /BOOT0.",
                    "evidence": f"nets={sorted(resistor_nets)}",
                }
            )

    for ref, symbol in symbols_by_ref.items():
        if not ref.startswith("C"):
            continue
        text = symbol_search_text(symbol).upper()
        capacitor_nets = set(nets_for_ref(netlist, ref).values())
        if "1UF_EN" in text and capacitor_nets and capacitor_nets != {"/ESP_EN", "GND"}:
            findings.append(
                {
                    "status": STATUS_FAIL,
                    "code": "EN_CAP_RETURN_NOT_GND",
                    "category": "reset_boot_topology",
                    "reference": ref,
                    "message": "EN support capacitor is not mapped between /ESP_EN and GND.",
                    "evidence": f"nets={sorted(capacitor_nets)}",
                }
            )
        if "+3V3" in capacitor_nets and "GND" not in capacitor_nets and any(token in text for token in ("_MOD", "10UF", "100NF", "100N")):
            findings.append(
                {
                    "status": STATUS_WARN,
                    "code": "LOCAL_3V3_DECOUPLING_RETURN_NOT_GND",
                    "category": "reset_boot_topology",
                    "reference": ref,
                    "message": "Local +3V3 decoupling capacitor does not return to GND in the saved netlist.",
                    "evidence": f"nets={sorted(capacitor_nets)}",
                }
            )

    if not findings:
        findings.append(
            {
                "status": STATUS_INFO,
                "code": "RESET_BOOT_TOPOLOGY_NO_HARD_HEURISTIC_FAILURE",
                "category": "reset_boot_topology",
                "reference": "",
                "message": "No hard reset/boot topology failure was detected by the current heuristics.",
                "evidence": "",
            }
        )
    return findings


def audit_text_ownership(
    texts: list[dict[str, Any]],
    symbols_by_ref: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    physical_symbols = [symbol for symbol in symbols_by_ref.values() if not str(symbol.get("reference", "")).startswith("#")]
    for text in texts:
        owner_reference = str(text.get("owner_reference", ""))
        if not owner_reference:
            continue
        if not str(text["kind"]).startswith("property:"):
            continue
        owner = symbols_by_ref.get(owner_reference)
        if owner is None:
            continue
        owner_gap = rect_distance(text["bbox"], owner["bbox"])
        nearest_other_ref = ""
        nearest_other_gap = float("inf")
        for symbol in physical_symbols:
            if symbol.get("reference") == owner_reference:
                continue
            current_gap = rect_distance(text["bbox"], symbol["bbox"])
            if current_gap < nearest_other_gap:
                nearest_other_gap = current_gap
                nearest_other_ref = str(symbol.get("reference", ""))

        if owner_gap > 4.0 and nearest_other_ref and nearest_other_gap + 1.0 < owner_gap and nearest_other_gap <= 3.0:
            findings.append(
                {
                    "status": STATUS_WARN,
                    "code": "TEXT_CLOSER_TO_OTHER_SYMBOL",
                    "category": "text_ownership",
                    "reference": owner_reference,
                    "message": "Visible reference/value appears closer to a different symbol than its owner.",
                    "evidence": f"text={text['kind']}:{text['text']}, nearest_other={nearest_other_ref}",
                }
            )
        elif owner_gap > 8.0:
            findings.append(
                {
                    "status": STATUS_WARN,
                    "code": "TEXT_DETACHED_FROM_OWNER",
                    "category": "text_ownership",
                    "reference": owner_reference,
                    "message": "Visible reference/value is far enough from its symbol to risk weak ownership.",
                    "evidence": f"text={text['kind']}:{text['text']}, owner_gap_mm={owner_gap:.2f}",
                }
            )

    if not findings:
        findings.append(
            {
                "status": STATUS_INFO,
                "code": "NO_OBVIOUS_TEXT_OWNERSHIP_HEURISTIC_FAILURE",
                "category": "text_ownership",
                "reference": "",
                "message": "No obvious detached reference/value ownership problem was detected by the current heuristics.",
                "evidence": "",
            }
        )
    return findings


def audit_wire_paths(paths: list[dict[str, Any]], blocks: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    suspicious_count = 0
    for index, path in enumerate(paths, start=1):
        direct = path["direct_length"]
        if direct <= 0.0:
            continue
        ratio = path["path_length"] / direct if direct else 0.0
        span = max(bbox_width(path["bbox"]), bbox_height(path["bbox"]))
        start_block = nearest_block_id(path["points"][0], blocks)
        end_block = nearest_block_id(path["points"][-1], blocks)
        if span <= 35.0 and (path["uturn"] or (path["orientation_changes"] >= 3 and ratio >= 1.8)):
            suspicious_count += 1
            findings.append(
                {
                    "status": STATUS_WARN,
                    "code": "LOCAL_LOOPBACK_OR_S_PATH",
                    "category": "wire_path_quality",
                    "reference": f"path_{index}",
                    "message": "Local wire path looks like a loopback or S-shaped route that may be simplified by orientation or direct wiring.",
                    "evidence": f"ratio={ratio:.2f}, blocks={start_block}->{end_block}, points={len(path['points'])}",
                }
            )
    if suspicious_count == 0:
        findings.append(
            {
                "status": STATUS_INFO,
                "code": "NO_OBVIOUS_LOCAL_LOOPBACK_PATHS",
                "category": "wire_path_quality",
                "reference": "",
                "message": "No obvious local loopback or S-shaped wire path was detected by the current heuristics.",
                "evidence": "",
            }
        )
    return findings


def audit_ground_power_presentation(
    netlist: dict[str, Any],
    symbols_by_ref: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for net_name, nodes in netlist["nets"].items():
        if not net_name or net_name == "GND" or net_name.startswith("unconnected-"):
            continue
        refs = {node["ref"] for node in nodes}
        if len(refs) < 4:
            continue
        local_symbols = [symbols_by_ref.get(ref) for ref in refs if ref in symbols_by_ref]
        block_ids = {symbol.get("block_id", "") for symbol in local_symbols if symbol}
        search_text = " ".join(symbol_search_text(symbol or {}) for symbol in local_symbols if symbol)
        if block_ids - {"reset_boot", "leds", "esp32_module"}:
            continue
        if "led" in search_text and "switch" in search_text and "device:c" in search_text:
            findings.append(
                {
                    "status": STATUS_FAIL,
                    "code": "LOCAL_RETURN_CLUSTER_NOT_GND",
                    "category": "ground_power_presentation",
                    "reference": net_name,
                    "message": "A local common-return-style cluster around LEDs/reset support is not actually on GND.",
                    "evidence": f"refs={','.join(sorted(refs))}",
                }
            )

    if not findings:
        findings.append(
            {
                "status": STATUS_INFO,
                "code": "NO_SUSPICIOUS_LOCAL_RETURN_CLUSTERS",
                "category": "ground_power_presentation",
                "reference": "",
                "message": "No suspicious unnamed local return cluster was detected by the current heuristics.",
                "evidence": "",
            }
        )
    return findings


def summarize_findings(findings: list[dict[str, Any]]) -> dict[str, Any]:
    counts = Counter(item["status"] for item in findings)
    overall = STATUS_INFO
    if counts.get(STATUS_FAIL, 0):
        overall = STATUS_FAIL
    elif counts.get(STATUS_WARN, 0):
        overall = STATUS_WARN
    return {
        "overall_status": overall,
        "counts": {
            STATUS_FAIL: counts.get(STATUS_FAIL, 0),
            STATUS_WARN: counts.get(STATUS_WARN, 0),
            STATUS_INFO: counts.get(STATUS_INFO, 0),
        },
    }


def markdown_report(result: dict[str, Any]) -> str:
    lines = [
        "# Schematic Human Drafting Quality Check",
        "",
        f"Status: `{result['summary']['overall_status']}`",
        "",
        f"Generated: `{result['generated_at']}`",
        f"Schematic: `{result['schematic']}`",
    ]
    if result.get("project"):
        lines.append(f"Project: `{result['project']}`")
    lines.extend(
        [
            "",
            "## Summary",
            "",
            f"- Fail: {result['summary']['counts'][STATUS_FAIL]}",
            f"- Warn: {result['summary']['counts'][STATUS_WARN]}",
            f"- Info: {result['summary']['counts'][STATUS_INFO]}",
            "",
            "## Key Checks",
            "",
            f"- Netlist export available: `{result['netlist']['available']}`",
            f"- Top-level graphic items: `{result['object_counts']['graphics']}`",
            f"- Labels reviewed: `{result['object_counts']['labels']}`",
            f"- Wire paths reviewed: `{result['object_counts']['wire_paths']}`",
            "",
            "## Focus Nets",
            "",
            "| Focus | Present | Resolved Net | Nodes |",
            "| --- | --- | --- | --- |",
        ]
    )
    for key, item in result["focus_nets"].items():
        node_summary = ", ".join(f"{node['ref']}.{node['pin']}" for node in item["nodes"]) or "none"
        lines.append(f"| `{key}` | `{item['present']}` | `{item['resolved_name'] or ''}` | {node_summary} |")

    lines.extend(
        [
            "",
            "## Label Classifications",
            "",
            "| Label | Class | Count | Resolved Net | Blocks |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["label_classifications"]:
        lines.append(
            f"| `{item['label']}` | `{item['classification']}` | `{item['count']}` | `{item['resolved_net'] or ''}` | {', '.join(item['blocks'])} |"
        )

    lines.extend(
        [
            "",
            "## Findings",
            "",
            "| Status | Category | Code | Reference | Message | Evidence |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for finding in result["findings"]:
        lines.append(
            "| `{status}` | `{category}` | `{code}` | `{reference}` | {message} | `{evidence}` |".format(
                status=finding["status"],
                category=finding["category"],
                code=finding["code"],
                reference=finding.get("reference", ""),
                message=str(finding["message"]).replace("|", "\\|"),
                evidence=str(finding.get("evidence", "")).replace("|", "\\|"),
            )
        )

    lines.extend(
        [
            "",
            "## What This Checker Catches",
            "",
            "- top-level graphic items that may be mistaken for electrical rails",
            "- local net labels that look avoidable or weakly justified",
            "- repeated local labels that suggest orientation-before-label problems",
            "- local MCU support nets that still rely on labels",
            "- likely reset/boot switch, pull-up, and support-cap topology mistakes",
            "- visible reference/value ownership drift",
            "- suspicious local loopback or S-shaped wire paths",
            "- local return-style clusters that are not actually on GND",
            "",
            "## Limits",
            "",
            "- This is still a heuristic read-only checker and may produce false positives.",
            "- It does not replace human image review, ERC, datasheet review, or KiCad-native annotation proof.",
            "- Net truth depends on read-only netlist export when `kicad-cli` is available.",
            "- Some drafting issues remain easier for a human to judge from rendered pages than from raw geometry.",
            "",
        ]
    )
    return "\n".join(lines)


def run_checker(project_root: Path | None, schematic: Path) -> dict[str, Any]:
    root = load_schematic(schematic)
    symbols = extract_symbols(root)
    texts = extract_text_items(root, symbols)
    headings = heading_positions(texts)
    blocks, _ = assign_blocks(symbols, headings)
    for block_id, block in blocks.items():
        for symbol in block["symbols"]:
            symbol["block_id"] = block_id
    labels = [item for item in texts if item["kind"] in {"label", "global_label", "hierarchical_label"}]
    graphics = extract_top_level_graphic_items(root)
    wire_paths = extract_wire_paths(root)
    netlist = export_netlist_xml(schematic)
    symbols_by_ref = build_symbol_lookup(symbols)
    power_symbols = [symbol for symbol in symbols if str(symbol.get("lib_id", "")).lower().startswith("power:")]
    focus = focus_net_summary(netlist, netlist.get("components", {}))

    findings: list[dict[str, Any]] = []

    if not netlist["available"]:
        findings.append(
            {
                "status": STATUS_WARN,
                "code": "NETLIST_EXPORT_UNAVAILABLE",
                "category": "net_truth",
                "reference": "",
                "message": "Netlist export was unavailable; some electrical-topology checks were skipped.",
                "evidence": netlist["error"],
            }
        )
    else:
        findings.append(
            {
                "status": STATUS_INFO,
                "code": "NETLIST_EXPORT_AVAILABLE",
                "category": "net_truth",
                "reference": "",
                "message": "Read-only netlist export succeeded and was used for saved-net truth checks.",
                "evidence": "",
            }
        )

    label_classifications, label_findings = classify_label_items(labels, blocks, symbols, netlist)
    findings.extend(audit_graphic_items(graphics, wire_paths, power_symbols))
    findings.extend(label_findings)
    findings.extend(audit_orientation_before_label(label_classifications, netlist))
    findings.extend(audit_mcu_local_support(label_classifications, focus))
    if netlist["available"]:
        findings.extend(audit_reset_boot_topology(symbols_by_ref, netlist))
        findings.extend(audit_ground_power_presentation(netlist, symbols_by_ref))
    findings.extend(audit_text_ownership(texts, symbols_by_ref))
    findings.extend(audit_wire_paths(wire_paths, blocks))

    result = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "project": str(project_root) if project_root is not None else "",
        "schematic": str(schematic),
        "summary": summarize_findings(findings),
        "netlist": {
            "available": netlist["available"],
            "error": netlist["error"],
        },
        "object_counts": {
            "graphics": len(graphics),
            "labels": len(labels),
            "wire_paths": len(wire_paths),
            "symbols": len(symbols),
        },
        "focus_nets": focus,
        "label_classifications": label_classifications,
        "findings": findings,
    }
    return result


def resolve_paths(args: argparse.Namespace) -> tuple[Path | None, Path]:
    if args.project:
        project_root = Path(args.project)
        schematic = find_project_schematic(project_root)
        return project_root, schematic
    if not args.schematic:
        raise ValueError("either --project or --schematic is required")
    return None, Path(args.schematic)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the read-only schematic human-drafting quality checker.")
    parser.add_argument("--project", default="", help="Active project root. If set, the checker auto-finds the schematic.")
    parser.add_argument("--schematic", default="", help="Path to a .kicad_sch file.")
    parser.add_argument("--output-dir", default="", help="Optional output directory for JSON and Markdown reports.")
    parser.add_argument("--warn-only", action="store_true", help="Return exit code 0 even when FAIL findings exist.")
    args = parser.parse_args()

    project_root, schematic = resolve_paths(args)
    output_dir = choose_output_dir(project_root, schematic, args.output_dir)
    result = run_checker(project_root, schematic)

    if output_dir is not None:
        json_path = maybe_write_report(output_dir, "human_drafting_quality.json", json.dumps(result, indent=2, sort_keys=True))
        markdown_path = maybe_write_report(output_dir, "human_drafting_quality.md", markdown_report(result))
        print(str(json_path))
        print(str(markdown_path))
    else:
        print(markdown_report(result))

    if args.warn_only:
        return 0
    return 1 if result["summary"]["overall_status"] == STATUS_FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
