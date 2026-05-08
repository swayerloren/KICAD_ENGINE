#!/usr/bin/env python3
"""Shared helpers for placement-planning scripts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


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


def load_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def dump_json(path: str | Path, payload: dict[str, Any]) -> None:
    Path(path).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


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
        "xmin": x_mm - half_w,
        "xmax": x_mm + half_w,
        "ymin": y_mm - half_h,
        "ymax": y_mm + half_h,
    }


def bboxes_overlap(a: dict[str, float], b: dict[str, float]) -> bool:
    return not (
        a["xmax"] <= b["xmin"]
        or a["xmin"] >= b["xmax"]
        or a["ymax"] <= b["ymin"]
        or a["ymin"] >= b["ymax"]
    )


def bbox_inside_board(
    bbox: dict[str, float],
    board_width_mm: float,
    board_height_mm: float,
    edge_clearance_mm: float,
) -> bool:
    return (
        bbox["xmin"] >= edge_clearance_mm
        and bbox["ymin"] >= edge_clearance_mm
        and bbox["xmax"] <= board_width_mm - edge_clearance_mm
        and bbox["ymax"] <= board_height_mm - edge_clearance_mm
    )
