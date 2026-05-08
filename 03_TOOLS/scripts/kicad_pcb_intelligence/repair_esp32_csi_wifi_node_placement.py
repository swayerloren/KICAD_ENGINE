#!/usr/bin/env python3
"""Repair ESP32_CSI_WIFI_NODE PCB placement using pcb_intelligence constraints.

This script edits placement, board outline, and text visibility/positions only.
It does not route tracks, create zones, or generate fabrication outputs.
"""

from __future__ import annotations

from pathlib import Path

import pcbnew


ROOT = Path(__file__).resolve().parents[3]
PCB = ROOT / "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb"


BOARD_W = 55.0
BOARD_H = 90.0


PLACEMENT = {
    # ESP32/RF at top
    "U2": (27.5, 28.0, 0.0),
    "C3": (19.0, 44.0, 90.0),
    "C4": (24.0, 44.0, 90.0),
    # USB bottom cluster
    "J2": (27.5, 84.5, 90.0),
    "U3": (27.5, 75.0, 0.0),
    "R6": (21.0, 80.0, 0.0),
    "R7": (34.0, 80.0, 0.0),
    "R8": (24.0, 68.0, 0.0),
    "R9": (31.0, 68.0, 0.0),
    "R5": (42.0, 77.0, 0.0),
    # Power path, compact left-to-center
    "J1": (7.5, 64.0, 180.0),
    "F1": (17.0, 64.0, 0.0),
    "Q1": (24.0, 64.0, 0.0),
    "D3": (16.0, 55.0, 90.0),
    "C2": (22.0, 55.0, 90.0),
    "C5": (22.0, 60.0, 90.0),
    "U1": (30.0, 56.0, 0.0),
    "C6": (28.0, 51.0, 0.0),
    "L1": (38.0, 56.0, 0.0),
    "C7": (42.0, 51.0, 90.0),
    "C8": (48.0, 51.0, 90.0),
    # Reset/boot controls accessible from edge
    "SW2": (6.0, 38.0, 90.0),
    "R1": (13.0, 37.0, 0.0),
    "C1": (13.0, 41.0, 0.0),
    "SW1": (6.0, 74.0, 90.0),
    "R2": (13.0, 74.0, 0.0),
    # LEDs visible, resistors nearby
    "D1": (42.0, 64.0, 0.0),
    "R3": (42.0, 67.0, 0.0),
    "D2": (47.0, 64.0, 0.0),
    "R4": (47.0, 67.0, 0.0),
    # Right-side service row, clear of USB support cluster
    "TP1": (52.0, 42.0, 90.0),
    "TP2": (52.0, 46.0, 90.0),
    "TP3": (52.0, 50.0, 90.0),
    "TP4": (52.0, 54.0, 90.0),
    "TP5": (52.0, 58.0, 90.0),
    "TP6": (52.0, 62.0, 90.0),
    "TP7": (52.0, 66.0, 90.0),
    "TP8": (52.0, 70.0, 90.0),
    "TP9": (52.0, 74.0, 90.0),
    # Mechanical holes, compact-board shifted four-hole review strategy
    "MH1": (4.0, 86.0, 0.0),
    "MH2": (51.0, 86.0, 0.0),
    "MH3": (4.0, 46.0, 0.0),
    "MH4": (51.0, 36.0, 0.0),
}


REF_OFFSETS = {
    "U2": (0, 13),
    "J2": (0, -8),
    "J1": (0, -9),
}


def mm(value: float) -> int:
    return pcbnew.FromMM(value)


def point(x: float, y: float) -> pcbnew.VECTOR2I:
    return pcbnew.VECTOR2I(mm(x), mm(y))


def angle(deg: float):
    return pcbnew.EDA_ANGLE(deg, pcbnew.DEGREES_T)


def set_footprint(fp: pcbnew.FOOTPRINT, x: float, y: float, rot: float):
    fp.SetPosition(point(x, y))
    fp.SetOrientation(angle(rot))


def draw_outline(board: pcbnew.BOARD):
    for drawing in list(board.GetDrawings()):
        if drawing.GetLayer() == pcbnew.Edge_Cuts:
            board.Remove(drawing)
    corners = [(0, 0), (BOARD_W, 0), (BOARD_W, BOARD_H), (0, BOARD_H), (0, 0)]
    for start, end in zip(corners, corners[1:]):
        segment = pcbnew.PCB_SHAPE(board)
        segment.SetShape(pcbnew.SHAPE_T_SEGMENT)
        segment.SetStart(point(*start))
        segment.SetEnd(point(*end))
        segment.SetLayer(pcbnew.Edge_Cuts)
        segment.SetWidth(mm(0.10))
        board.Add(segment)


def cleanup_text(fp: pcbnew.FOOTPRINT):
    ref = fp.GetReference()
    ref_text = fp.Reference()
    val_text = fp.Value()
    ref_text.SetVisible(True)
    val_text.SetVisible(False)
    ref_text.SetTextSize(pcbnew.VECTOR2I(mm(0.8), mm(0.8)))
    ref_text.SetTextThickness(mm(0.12))
    pos = fp.GetPosition()
    dx, dy = REF_OFFSETS.get(ref, (0.0, -2.2))
    if ref.startswith("TP"):
        dx, dy = -5.2, 0.0
    elif ref.startswith("MH"):
        dx, dy = 0.0, -2.8
    elif ref in {"R6", "R7", "R8", "R9", "R3", "R4", "R1", "R2", "R5"}:
        dx, dy = 0.0, -1.6
    elif ref in {"C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"}:
        dx, dy = 0.0, -1.8
    elif ref in {"D1", "D2", "D3"}:
        dx, dy = 0.0, -2.0
    elif ref in {"SW1", "SW2"}:
        dx, dy = 0.0, -4.2
    ref_text.SetPosition(pcbnew.VECTOR2I(pos.x + mm(dx), pos.y + mm(dy)))
    ref_text.SetTextAngle(angle(0))
    if ref.startswith(("R", "C")) or ref == "D3":
        ref_text.SetVisible(False)


def main() -> int:
    board = pcbnew.LoadBoard(str(PCB))
    missing = []
    for ref, placement in PLACEMENT.items():
        fp_raw = board.FindFootprintByReference(ref)
        if fp_raw is None:
            missing.append(ref)
            continue
        set_footprint(fp_raw, *placement)
        cleanup_text(fp_raw)
    if missing:
        raise SystemExit(f"Missing footprints: {', '.join(missing)}")
    draw_outline(board)
    pcbnew.SaveBoard(str(PCB), board)
    print(f"Saved placement repair to {PCB}")
    print(f"Board outline: {BOARD_W:.1f} x {BOARD_H:.1f} mm")
    print(f"Footprints placed: {len(PLACEMENT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
