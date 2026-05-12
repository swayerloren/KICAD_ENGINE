#!/usr/bin/env python3
"""Repair local ERC regressions introduced by the ESP32 schematic visual cleanup pass."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]
KICAD_SCH_API_SITE = REPO_ROOT / "03_TOOLS" / "python_envs" / "kicad-mcp-pro" / "Lib" / "site-packages"
if str(KICAD_SCH_API_SITE) not in sys.path and KICAD_SCH_API_SITE.exists():
    sys.path.insert(0, str(KICAD_SCH_API_SITE))

from kicad_sch_api import load_schematic
from kicad_sch_api.core.types import Point


DEFAULT_SCHEMATIC = REPO_ROOT / "04_KICAD_PROJECTS" / "active" / "ESP32_CSI_WIFI_NODE" / "kicad" / "ESP32_CSI_WIFI_NODE.kicad_sch"


def point(x: float, y: float) -> Point:
    return Point(round(x, 3), round(y, 3))


def get_component(sch, ref: str):
    component = sch.components.get(ref)
    if component is None:
        raise RuntimeError(f"Component not found: {ref}")
    return component


def shift_visible_properties(comp, dx: float, dy: float) -> None:
    for prop_name in ("Reference", "Value", "Description"):
        if prop_name not in comp.properties:
            continue
        effects = comp.get_property_effects(prop_name)
        pos_x, pos_y = effects["position"]
        effects["position"] = (round(pos_x + dx, 3), round(pos_y + dy, 3))
        comp.set_property_effects(prop_name, effects)


def move_component(comp, new_x: float, new_y: float) -> None:
    old_x = comp.position.x
    old_y = comp.position.y
    comp.move(new_x, new_y)
    shift_visible_properties(comp, new_x - old_x, new_y - old_y)


def set_property_position(comp, prop_name: str, x: float, y: float) -> None:
    effects = comp.get_property_effects(prop_name)
    effects["position"] = (round(x, 3), round(y, 3))
    comp.set_property_effects(prop_name, effects)


def wire_exists(sch, start: tuple[float, float], end: tuple[float, float], tol: float = 0.01) -> bool:
    wanted = sorted([start, end])
    for wire in sch.wires:
        points = [(round(p.x, 3), round(p.y, 3)) for p in wire.points]
        if len(points) != 2:
            continue
        got = sorted(points)
        if all(abs(a - b) <= tol for a, b in zip(got[0], wanted[0])) and all(abs(a - b) <= tol for a, b in zip(got[1], wanted[1])):
            return True
    return False


def add_wire_if_missing(sch, start: tuple[float, float], end: tuple[float, float]) -> None:
    if not wire_exists(sch, start, end):
        sch.add_wire(start, end)


def main() -> int:
    parser = argparse.ArgumentParser(description="Repair ERC regressions after schematic visual cleanup.")
    parser.add_argument("--schematic", default=str(DEFAULT_SCHEMATIC), help="Target .kicad_sch file.")
    args = parser.parse_args()

    schematic_path = Path(args.schematic).resolve()
    sch = load_schematic(schematic_path)

    # Restore the TVS onto its original wired net span.
    d3 = get_component(sch, "D3")
    move_component(d3, 86.36, 71.12)
    set_property_position(d3, "Reference", 91.44, 66.74)
    set_property_position(d3, "Value", 88.646, 73.914)

    # Restore the optional shield jumper wire so the SHIELD label is not dangling.
    add_wire_if_missing(sch, (207.01, 31.75), (208.28, 31.75))

    # Restore the short USB D+/D- connector stubs that were removed during label cleanup.
    for segment in (
        ((232.41, 52.07), (237.49, 52.07)),
        ((232.41, 54.61), (237.49, 54.61)),
        ((232.41, 57.15), (237.49, 57.15)),
        ((232.41, 59.69), (237.49, 59.69)),
    ):
        add_wire_if_missing(sch, *segment)

    # Separate the buck output capacitor text so C7 no longer collides with C8.
    c7 = get_component(sch, "C7")
    set_property_position(c7, "Reference", 166.37, 56.388)
    set_property_position(c7, "Value", 163.322, 60.452)

    sch.save(schematic_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
