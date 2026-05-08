#!/usr/bin/env python3
"""Shared helpers for read-only KiCad PCB extraction into routing-engine JSON."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
DISCOVERY_DIR = SCRIPT_DIR.parents[1] / "03_TOOLS" / "scripts" / "kicad_discovery"
if str(DISCOVERY_DIR) not in sys.path:
    sys.path.insert(0, str(DISCOVERY_DIR))

try:
    from find_kicad import detect_kicad_environment  # type: ignore
except Exception:  # noqa: BLE001
    detect_kicad_environment = None


REEXEC_ENV = "KICAD_ENGINE_PCB_BRIDGE_ACTIVE"
KICAD_PYTHON_CANDIDATES = [
    Path(r"C:\Program Files\KiCad\9.0\bin\python.exe"),
    Path(r"C:\Program Files\KiCad\8.0\bin\python.exe"),
]


def dump_json(path: str | Path, payload: dict[str, Any]) -> None:
    Path(path).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def dump_markdown(path: str | Path, text: str) -> None:
    Path(path).write_text(text.rstrip() + "\n", encoding="utf-8")


def parse_common_args(parser) -> None:
    parser.add_argument("pcb_file", help="Input .kicad_pcb file")
    parser.add_argument("output_json", help="Output JSON path")
    parser.add_argument("--markdown", help="Optional Markdown output path")


def ensure_parent(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def find_kicad_python() -> Path | None:
    if detect_kicad_environment is not None:
        try:
            payload = detect_kicad_environment(probe_pcbnew=False)
            root = payload.get("kicad_root", {}).get("path")
            if root:
                candidate = Path(root) / "bin" / "python.exe"
                if candidate.exists():
                    return candidate.resolve()
        except Exception:
            pass
    for candidate in KICAD_PYTHON_CANDIDATES:
        if candidate.exists():
            return candidate
    return None


def require_pcbnew_for_cli() -> Any:
    try:
        import pcbnew  # type: ignore

        return pcbnew
    except Exception:
        if os.environ.get(REEXEC_ENV) == "1":
            raise
        kicad_python = find_kicad_python()
        if not kicad_python:
            raise RuntimeError("KiCad python.exe not found; cannot import pcbnew")
        env = os.environ.copy()
        env[REEXEC_ENV] = "1"
        completed = subprocess.run([str(kicad_python), *sys.argv], env=env)
        raise SystemExit(completed.returncode)


def mm(pcbnew: Any, value: int | float) -> float:
    return round(float(pcbnew.ToMM(value)), 6)


def point_to_mm(pcbnew: Any, point: Any) -> dict[str, float]:
    return {"x_mm": mm(pcbnew, point.x), "y_mm": mm(pcbnew, point.y)}


def bbox_to_mm(pcbnew: Any, bbox: Any) -> dict[str, float]:
    x = mm(pcbnew, bbox.GetX())
    y = mm(pcbnew, bbox.GetY())
    width = mm(pcbnew, bbox.GetWidth())
    height = mm(pcbnew, bbox.GetHeight())
    return {
        "xmin": x,
        "ymin": y,
        "xmax": round(x + width, 6),
        "ymax": round(y + height, 6),
        "width_mm": width,
        "height_mm": height,
    }


def copper_layer_names(board: Any) -> list[str]:
    names: list[str] = []
    for layer_id in list(board.GetEnabledLayers().Seq()):
        name = str(board.GetLayerName(layer_id))
        if name.endswith(".Cu"):
            names.append(name)
    return names


def layer_names_from_set(board: Any, layer_set: Any) -> list[str]:
    names: list[str] = []
    for layer_id in list(layer_set.Seq()):
        names.append(str(board.GetLayerName(layer_id)))
    return names


def is_mounting_hole(ref: str, value: str, footprint_name: str) -> bool:
    haystack = " ".join([ref.upper(), value.upper(), footprint_name.upper()])
    return any(token in haystack for token in ("MOUNT", "MNT", "HOLE", "MH", "SCREW"))


def is_fixed_mechanical(ref: str, value: str, footprint_name: str) -> bool:
    haystack = " ".join([ref.upper(), value.upper(), footprint_name.upper()])
    if is_mounting_hole(ref, value, footprint_name):
        return True
    return ref.upper().startswith("J")


def infer_keepout_type(name: str) -> str:
    upper = name.upper()
    if "ANT" in upper:
        return "ANTENNA_KEEPOUT"
    if "RF" in upper:
        return "RF_KEEPOUT"
    if "USB" in upper or "CONN" in upper or "J" in upper:
        return "CONNECTOR_KEEPOUT"
    return "MECHANICAL_KEEPOUT"


def infer_net_role(name: str) -> str:
    upper = name.upper()
    if upper in {"GND", "PGND", "AGND"}:
        return "GROUND"
    if any(token in upper for token in ("VBUS", "+5V", "VIN", "VCC", "BAT", "12V", "24V")):
        return "POWER_INPUT"
    if any(token in upper for token in ("3V3", "VDD", "VDD33", "3.3V")):
        return "RAIL_3V3"
    if upper in {"D+", "USB_D+", "USB_DP", "DP"} or upper.endswith("D+"):
        return "USB_D+"
    if upper in {"D-", "USB_D-", "USB_DM", "DM"} or upper.endswith("D-"):
        return "USB_D-"
    if any(token in upper for token in ("BUCK_SW", "_SW", " SW", "LX")):
        return "BUCK_SW"
    if any(token in upper for token in ("BUCK_BST", "_BST", "BST")):
        return "BUCK_BST"
    if any(token in upper for token in ("EN", "ENABLE", "BOOT", "IO0")):
        return "EN_BOOT"
    if any(token in upper for token in ("ESD", "TVS", "PROT")):
        return "PROTECTION"
    if any(token in upper for token in ("LED", "BTN", "SWITCH", "KEY", "BUTTON")):
        return "LEDS_BUTTONS"
    if upper.startswith("TP") or "TEST" in upper:
        return "TEST_PADS"
    return "LOW_RISK"


def infer_routing_priority(role: str, power: bool, usb: bool, critical: bool) -> int:
    if role == "POWER_INPUT":
        return 100
    if role in {"BUCK_SW", "BUCK_BST"}:
        return 95
    if role == "RAIL_3V3":
        return 90
    if usb:
        return 85
    if role == "PROTECTION":
        return 80
    if role == "EN_BOOT":
        return 70
    if power:
        return 65
    if critical:
        return 60
    if role == "TEST_PADS":
        return 20
    if role == "LEDS_BUTTONS":
        return 15
    return 10


def infer_pair_name(name: str) -> str:
    upper = name.upper()
    if upper.endswith("D+") or upper in {"USB_D+", "USB_DP", "D+", "DP"}:
        return "USB_D-"
    if upper.endswith("D-") or upper in {"USB_D-", "USB_DM", "D-", "DM"}:
        return "USB_D+"
    return ""
