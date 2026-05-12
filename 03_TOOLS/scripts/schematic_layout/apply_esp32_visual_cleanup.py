#!/usr/bin/env python3
"""Apply a structured visual cleanup pass to the ESP32_CSI_WIFI_NODE schematic."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[3]
KICAD_SCH_API_SITE = REPO_ROOT / "03_TOOLS" / "python_envs" / "kicad-mcp-pro" / "Lib" / "site-packages"
if str(KICAD_SCH_API_SITE) not in sys.path and KICAD_SCH_API_SITE.exists():
    sys.path.insert(0, str(KICAD_SCH_API_SITE))

from kicad_sch_api import load_schematic
from kicad_sch_api.core.types import Point

ACTIVE_SCHEMATIC = REPO_ROOT / "04_KICAD_PROJECTS" / "active" / "ESP32_CSI_WIFI_NODE" / "kicad" / "ESP32_CSI_WIFI_NODE.kicad_sch"


def point(x: float, y: float) -> Point:
    return Point(round(x, 3), round(y, 3))


def load(path: Path):
    return load_schematic(path)


def get_component(sch, ref: str):
    comp = sch.components.get(ref)
    if comp is None:
        raise RuntimeError(f"Component not found: {ref}")
    return comp


def find_label(sch, text: str, x: float, y: float, tol: float = 0.01):
    for label in sch.labels:
        if label.text != text:
            continue
        if abs(label.position.x - x) <= tol and abs(label.position.y - y) <= tol:
            return label
    raise RuntimeError(f"Label not found: {text} @ ({x}, {y})")


def find_text(sch, text_value: str):
    for item in sch.texts:
        if item.text == text_value:
            return item
    raise RuntimeError(f"Text not found: {text_value}")


def find_wire(sch, start: tuple[float, float], end: tuple[float, float], tol: float = 0.01):
    wanted = sorted([start, end])
    for wire in sch.wires:
        points = [(round(p.x, 3), round(p.y, 3)) for p in wire.points]
        if len(points) != 2:
            continue
        got = sorted(points)
        if all(abs(a - b) <= tol for a, b in zip(got[0], wanted[0])) and all(abs(a - b) <= tol for a, b in zip(got[1], wanted[1])):
            return wire
    raise RuntimeError(f"Wire not found: {start} -> {end}")


def find_no_connect(sch, x: float, y: float, tol: float = 0.01):
    for item in sch.no_connects:
        if abs(item.position.x - x) <= tol and abs(item.position.y - y) <= tol:
            return item
    raise RuntimeError(f"No-connect not found: ({x}, {y})")


def shift_visible_properties(comp, dx: float, dy: float):
    for prop_name in ("Reference", "Value", "Description"):
        if prop_name not in comp.properties:
            continue
        effects = comp.get_property_effects(prop_name)
        pos_x, pos_y = effects["position"]
        effects["position"] = (round(pos_x + dx, 3), round(pos_y + dy, 3))
        comp.set_property_effects(prop_name, effects)


def move_component(comp, new_x: float, new_y: float, rotation: int | None = None):
    old_x = comp.position.x
    old_y = comp.position.y
    if rotation is not None and int(comp.rotation) != rotation:
        comp.rotation = rotation
    comp.move(new_x, new_y)
    shift_visible_properties(comp, new_x - old_x, new_y - old_y)


def move_label(label, new_x: float, new_y: float):
    label.move(new_x, new_y)


def move_text(item, new_x: float, new_y: float):
    item.position = point(new_x, new_y)


def move_no_connect(item, new_x: float, new_y: float):
    item.position = point(new_x, new_y)


def set_value(comp, value: str):
    comp.value = value


def set_property_position(comp, prop_name: str, x: float, y: float):
    effects = comp.get_property_effects(prop_name)
    effects["position"] = (round(x, 3), round(y, 3))
    comp.set_property_effects(prop_name, effects)


def remove_labels(sch, labels: Iterable):
    for label in labels:
        sch.remove_label(label.uuid)


def remove_wires(sch, wires: Iterable):
    for wire in wires:
        sch.remove_wire(wire.uuid)


def add_wire(sch, start: tuple[float, float], end: tuple[float, float]):
    sch.add_wire(start, end)


def add_label(sch, text: str, x: float, y: float, rotation: float = 0.0):
    sch.add_label(text, position=(x, y), rotation=rotation)


def cleanup_values(sch):
    replacements = {
        "Q1": "AO3401A",
        "D3": "5V_TVS",
        "U1": "AP63203WU",
        "L1": "3.9uH",
        "SW2": "RESET_SW",
        "SW1": "BOOT_SW",
        "J2": "USB_C_USB2",
        "U3": "USB_ESD",
        "TP8": "TP_D+",
        "TP9": "TP_D-",
    }
    for ref, value in replacements.items():
        set_value(get_component(sch, ref), value)


def move_c2_block(sch):
    c2 = get_component(sch, "C2")
    pwr = get_component(sch, "#PWR011")
    label = find_label(sch, "+5V_PROTECTED", 91.44, 95.25)
    wire = find_wire(sch, (91.44, 95.25), (91.44, 90.17))
    move_component(c2, 88.9, 57.15)
    move_component(pwr, 88.9, 53.34)
    move_label(label, 93.98, 60.96)
    wire.points = [point(88.9, 60.96), point(93.98, 60.96)]


def move_power_support_parts(sch):
    move_component(get_component(sch, "D3"), 82.55, 62.23)
    move_component(get_component(sch, "C7"), 167.64, 58.42)
    move_component(get_component(sch, "#PWR023"), 167.64, 54.61)
    move_component(get_component(sch, "#PWR024"), 167.64, 62.23)
    move_component(get_component(sch, "C8"), 180.34, 58.42)
    move_component(get_component(sch, "#PWR025"), 180.34, 54.61)
    move_component(get_component(sch, "#PWR026"), 180.34, 62.23)


def rebuild_reset_block(sch):
    reset_text = find_text(sch, "RESET / BOOT")
    move_text(reset_text, 91.44, 76.2)

    move_component(get_component(sch, "R1"), 107.95, 88.9, rotation=270)
    move_component(get_component(sch, "C1"), 104.14, 85.09, rotation=0)
    move_component(get_component(sch, "SW2"), 121.92, 88.9, rotation=0)
    move_component(get_component(sch, "R2"), 107.95, 101.6, rotation=270)
    move_component(get_component(sch, "SW1"), 121.92, 101.6, rotation=0)

    move_component(get_component(sch, "#PWR02"), 115.57, 88.9)
    move_component(get_component(sch, "#PWR03"), 115.57, 101.6)
    move_component(get_component(sch, "#PWR06"), 104.14, 81.28)
    move_component(get_component(sch, "#PWR012"), 130.81, 88.9)
    move_component(get_component(sch, "#PWR010"), 130.81, 101.6)

    old_labels = [
        find_label(sch, "ESP_EN", 41.91, 85.09),
        find_label(sch, "ESP_EN", 62.23, 93.98),
        find_label(sch, "ESP_EN", 107.95, 91.44),
        find_label(sch, "BOOT0", 41.91, 104.14),
        find_label(sch, "BOOT0", 67.31, 109.22),
    ]
    remove_labels(sch, old_labels)

    old_wires = [
        find_wire(sch, (41.91, 85.09), (41.91, 86.36)),
        find_wire(sch, (62.23, 93.98), (62.23, 92.71)),
        find_wire(sch, (107.95, 92.71), (107.95, 91.44)),
        find_wire(sch, (41.91, 104.14), (41.91, 105.41)),
        find_wire(sch, (67.31, 107.95), (69.85, 107.95)),
        find_wire(sch, (67.31, 109.22), (67.31, 107.95)),
        find_wire(sch, (82.55, 107.95), (80.01, 107.95)),
        find_wire(sch, (119.38, 92.71), (118.11, 92.71)),
    ]
    remove_wires(sch, old_wires)

    add_label(sch, "ESP_EN", 99.06, 88.9, rotation=0.0)
    add_wire(sch, (99.06, 88.9), (104.14, 88.9))
    add_wire(sch, (104.14, 88.9), (116.84, 88.9))
    add_wire(sch, (111.76, 88.9), (115.57, 88.9))
    add_wire(sch, (127.0, 88.9), (130.81, 88.9))

    add_label(sch, "BOOT0", 99.06, 101.6, rotation=0.0)
    add_wire(sch, (99.06, 101.6), (104.14, 101.6))
    add_wire(sch, (104.14, 101.6), (116.84, 101.6))
    add_wire(sch, (111.76, 101.6), (115.57, 101.6))
    add_wire(sch, (127.0, 101.6), (130.81, 101.6))


def rebuild_usb_block(sch):
    labels_to_remove = [
        find_label(sch, "CC1", 237.49, 44.45),
        find_label(sch, "CC2", 237.49, 46.99),
        find_label(sch, "CC1", 245.11, 81.28),
        find_label(sch, "CC2", 266.7, 81.28),
        find_label(sch, "DM_C", 237.49, 52.07),
        find_label(sch, "DM_C", 237.49, 54.61),
        find_label(sch, "DP_C", 237.49, 57.15),
        find_label(sch, "DP_C", 237.49, 59.69),
    ]
    remove_labels(sch, labels_to_remove)

    wires_to_remove = [
        find_wire(sch, (245.11, 81.28), (245.11, 78.74)),
        find_wire(sch, (266.7, 81.28), (266.7, 78.74)),
        find_wire(sch, (208.28, 31.75), (207.01, 31.75)),
        find_wire(sch, (232.41, 44.45), (237.49, 44.45)),
        find_wire(sch, (232.41, 46.99), (237.49, 46.99)),
        find_wire(sch, (232.41, 52.07), (237.49, 52.07)),
        find_wire(sch, (232.41, 54.61), (237.49, 54.61)),
        find_wire(sch, (232.41, 57.15), (237.49, 57.15)),
        find_wire(sch, (232.41, 59.69), (237.49, 59.69)),
    ]
    remove_wires(sch, wires_to_remove)

    # Rebuild CC wiring locally.
    add_wire(sch, (232.41, 44.45), (245.11, 44.45))
    add_wire(sch, (245.11, 44.45), (245.11, 78.74))
    add_wire(sch, (232.41, 46.99), (266.7, 46.99))
    add_wire(sch, (266.7, 46.99), (266.7, 78.74))

    # Keep one DM_C / DP_C label at the connector pair and one at the U3 side.
    add_wire(sch, (237.49, 52.07), (237.49, 54.61))
    add_wire(sch, (237.49, 57.15), (237.49, 59.69))
    add_wire(sch, (237.49, 54.61), (242.57, 54.61))
    add_wire(sch, (237.49, 59.69), (242.57, 59.69))
    add_label(sch, "DM_C", 242.57, 54.61, rotation=0.0)
    add_label(sch, "DP_C", 242.57, 59.69, rotation=0.0)
    add_label(sch, "DM_C", 280.67, 49.53, rotation=0.0)
    add_label(sch, "DP_C", 250.19, 49.53, rotation=180.0)
    add_wire(sch, (275.59, 49.53), (280.67, 49.53))
    add_wire(sch, (255.27, 49.53), (250.19, 49.53))


def move_r8_r9_and_rewire_u2(sch):
    move_component(get_component(sch, "R8"), 186.69, 90.17, rotation=90)
    move_component(get_component(sch, "R9"), 186.69, 92.71, rotation=90)

    old_labels = [
        find_label(sch, "DM_C", 246.38, 95.25),
        find_label(sch, "DM_E", 254.0, 95.25),
        find_label(sch, "DP_C", 269.24, 95.25),
        find_label(sch, "DP_E", 276.86, 95.25),
    ]
    remove_labels(sch, old_labels)

    add_wire(sch, (177.8, 90.17), (182.88, 90.17))
    add_wire(sch, (177.8, 92.71), (182.88, 92.71))
    add_wire(sch, (190.5, 90.17), (195.58, 90.17))
    add_wire(sch, (190.5, 92.71), (195.58, 92.71))
    add_label(sch, "DM_E", 177.8, 90.17, rotation=180.0)
    add_label(sch, "DP_E", 177.8, 92.71, rotation=180.0)
    add_label(sch, "DM_C", 195.58, 90.17, rotation=0.0)
    add_label(sch, "DP_C", 195.58, 92.71, rotation=0.0)


def fix_overlaps(sch):
    # U1 / inductor / LED / ESP32 power text cleanup.
    u1_gnd = get_component(sch, "#PWR015")
    set_property_position(u1_gnd, "Value", 105.41, 55.88)

    led_gnd = get_component(sch, "#PWR07")
    set_property_position(led_gnd, "Value", 55.88, 136.906)

    l1 = get_component(sch, "L1")
    set_property_position(l1, "Value", 161.29, 51.816)

    pwr_3v3 = get_component(sch, "#PWR020")
    set_property_position(pwr_3v3, "Value", 137.16, 67.31)

    r1 = get_component(sch, "R1")
    set_property_position(r1, "Reference", 107.95, 84.582)
    set_property_position(r1, "Value", 107.95, 86.36)

    r2 = get_component(sch, "R2")
    set_property_position(r2, "Reference", 107.95, 97.282)
    set_property_position(r2, "Value", 104.14, 99.568)

    pwr3 = get_component(sch, "#PWR03")
    set_property_position(pwr3, "Value", 113.03, 104.14)

    pwr12 = get_component(sch, "#PWR012")
    set_property_position(pwr12, "Value", 132.08, 91.44)

    r8 = get_component(sch, "R8")
    set_property_position(r8, "Reference", 184.404, 87.63)
    set_property_position(r8, "Value", 191.008, 87.63)

    r9 = get_component(sch, "R9")
    set_property_position(r9, "Reference", 184.404, 95.25)
    set_property_position(r9, "Value", 191.008, 95.25)


def collect_summary() -> dict[str, object]:
    return {
        "script": Path(__file__).name,
        "target": str(ACTIVE_SCHEMATIC),
        "actions": [
            "replace visible review-marker values with readable functional values",
            "move C2 support capacitor back into the power block",
            "rebuild reset/boot as two compact wired local rows",
            "move USB local support closer to the ESP32 and reduce label duplication",
            "move R8/R9 next to the ESP32 USB pins and wire them directly",
            "reposition the worst overlapping text items",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply ESP32 schematic visual cleanup.")
    parser.add_argument("--schematic", default=str(ACTIVE_SCHEMATIC), help="Target .kicad_sch file.")
    parser.add_argument("--summary-json", default="", help="Optional JSON summary output.")
    args = parser.parse_args()

    schematic_path = Path(args.schematic).resolve()
    sch = load(schematic_path)

    cleanup_values(sch)
    move_c2_block(sch)
    move_power_support_parts(sch)
    rebuild_reset_block(sch)
    rebuild_usb_block(sch)
    move_r8_r9_and_rewire_u2(sch)
    fix_overlaps(sch)

    sch.save(schematic_path)

    if args.summary_json:
        Path(args.summary_json).write_text(json.dumps(collect_summary(), indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
