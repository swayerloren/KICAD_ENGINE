#!/usr/bin/env python3
"""Bottom-edge connector placement repair for ESP32_CSI_WIFI_NODE.

Placement-only edit:
- updates board outline
- moves footprints and silkscreen references
- does not create tracks, vias, zones, or fabrication outputs
"""

from __future__ import annotations

from pathlib import Path

import pcbnew


ROOT = Path(__file__).resolve().parents[3]
PCB = ROOT / "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb"

BOARD_W = 60.0
BOARD_H = 95.0


PLACEMENT = {
    # ESP32 module at top; antenna/keepout remains toward top board edge.
    "U2": (30.0, 28.0, 0.0),
    "C3": (21.5, 44.0, 90.0),
    "C4": (26.5, 44.0, 90.0),
    # Bottom-edge connectors and USB support.
    "J1": (13.0, 89.0, 90.0),
    "J2": (39.0, 89.5, 90.0),
    "U3": (39.0, 78.0, 0.0),
    "R6": (31.5, 81.5, 0.0),
    "R7": (46.0, 81.5, 0.0),
    "R8": (33.0, 75.0, 0.0),
    "R9": (45.0, 75.0, 0.0),
    "R5": (51.0, 78.0, 0.0),
    # Compact power chain above J1.
    "F1": (15.0, 78.0, 0.0),
    "Q1": (23.0, 78.0, 0.0),
    "D3": (14.0, 69.5, 90.0),
    "C2": (21.0, 69.5, 90.0),
    "C5": (21.0, 74.0, 90.0),
    "U1": (29.0, 69.5, 0.0),
    "C6": (27.0, 64.5, 0.0),
    "L1": (37.0, 69.5, 0.0),
    "C7": (42.0, 64.5, 90.0),
    "C8": (48.0, 64.5, 90.0),
    # Accessible controls and indicators.
    "SW2": (6.0, 54.0, 90.0),
    "R1": (13.0, 53.0, 0.0),
    "C1": (13.0, 57.0, 0.0),
    "SW1": (6.0, 64.0, 90.0),
    "R2": (13.0, 64.0, 0.0),
    "D1": (39.0, 55.0, 0.0),
    "R3": (39.0, 58.0, 0.0),
    "D2": (45.0, 55.0, 0.0),
    "R4": (45.0, 58.0, 0.0),
    # Right-side vertical service row, away from USB connector/passives.
    "TP1": (57.0, 40.0, 90.0),
    "TP2": (57.0, 44.0, 90.0),
    "TP3": (57.0, 48.0, 90.0),
    "TP4": (57.0, 52.0, 90.0),
    "TP5": (57.0, 56.0, 90.0),
    "TP6": (57.0, 60.0, 90.0),
    "TP7": (57.0, 64.0, 90.0),
    "TP8": (57.0, 68.0, 90.0),
    "TP9": (57.0, 72.0, 90.0),
    # Four-hole attempt outside RF keepout and connector mechanical areas.
    "MH1": (4.0, 91.0, 0.0),
    "MH2": (56.0, 91.0, 0.0),
    "MH3": (4.0, 45.0, 0.0),
    "MH4": (56.0, 35.0, 0.0),
}


REF_OFFSETS = {
    "U2": (0.0, 17.0),
    "J1": (-7.0, -12.0),
    "J2": (0.0, -8.5),
    "U3": (0.0, -3.5),
    "L1": (0.0, -5.5),
}


def mm(value: float) -> int:
    return pcbnew.FromMM(value)


def point(x: float, y: float) -> pcbnew.VECTOR2I:
    return pcbnew.VECTOR2I(mm(x), mm(y))


def angle(deg: float) -> pcbnew.EDA_ANGLE:
    return pcbnew.EDA_ANGLE(deg, pcbnew.DEGREES_T)


def set_footprint(fp: pcbnew.FOOTPRINT, x: float, y: float, rot: float) -> None:
    fp.SetPosition(point(x, y))
    fp.SetOrientation(angle(rot))


def draw_outline(board: pcbnew.BOARD) -> None:
    for drawing in list(board.GetDrawings()):
        if drawing.GetLayer() == pcbnew.Edge_Cuts:
            board.Remove(drawing)
    corners = [(0.0, 0.0), (BOARD_W, 0.0), (BOARD_W, BOARD_H), (0.0, BOARD_H), (0.0, 0.0)]
    for start, end in zip(corners, corners[1:]):
        segment = pcbnew.PCB_SHAPE(board)
        segment.SetShape(pcbnew.SHAPE_T_SEGMENT)
        segment.SetStart(point(*start))
        segment.SetEnd(point(*end))
        segment.SetLayer(pcbnew.Edge_Cuts)
        segment.SetWidth(mm(0.10))
        board.Add(segment)


def cleanup_text(fp: pcbnew.FOOTPRINT) -> None:
    ref = fp.GetReference()
    ref_text = fp.Reference()
    val_text = fp.Value()

    val_text.SetVisible(False)
    ref_text.SetVisible(True)
    ref_text.SetTextSize(pcbnew.VECTOR2I(mm(0.8), mm(0.8)))
    ref_text.SetTextThickness(mm(0.12))
    ref_text.SetTextAngle(angle(0.0))

    dx, dy = REF_OFFSETS.get(ref, (0.0, -2.2))
    if ref.startswith("TP"):
        dx, dy = -5.2, 0.0
    elif ref.startswith("MH"):
        dx, dy = 0.0, -2.9
    elif ref in {"SW1", "SW2"}:
        dx, dy = 0.0, -4.2
    elif ref.startswith(("R", "C")) or ref == "D3":
        ref_text.SetVisible(False)
    elif ref in {"D1", "D2"}:
        dx, dy = 0.0, -2.0

    pos = fp.GetPosition()
    ref_text.SetPosition(pcbnew.VECTOR2I(pos.x + mm(dx), pos.y + mm(dy)))


def main() -> int:
    board = pcbnew.LoadBoard(str(PCB))

    missing = []
    for ref, placement in PLACEMENT.items():
        fp = board.FindFootprintByReference(ref)
        if fp is None:
            missing.append(ref)
            continue
        set_footprint(fp, *placement)
        cleanup_text(fp)
    if missing:
        raise SystemExit(f"Missing footprints: {', '.join(missing)}")

    draw_outline(board)
    pcbnew.SaveBoard(str(PCB), board)

    print(f"Saved bottom-edge connector placement repair to {PCB}")
    print(f"Board outline: {BOARD_W:.1f} x {BOARD_H:.1f} mm")
    print(f"Footprints placed: {len(PLACEMENT)}")
    print(f"Zone count preserved: {board.GetAreaCount()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
