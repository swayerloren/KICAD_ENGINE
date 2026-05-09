import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = next((path for path in [SCRIPT_DIR, *SCRIPT_DIR.parents] if (path / "AGENTS.md").exists()), SCRIPT_DIR)
LAYOUT_SCRIPTS = REPO_ROOT / "14_LAYOUT_AUTOMATION" / "scripts"
if str(LAYOUT_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(LAYOUT_SCRIPTS))

from _kicad_pcb_bridge_common import require_pcbnew_for_cli  # type: ignore  # noqa: E402


pcbnew = require_pcbnew_for_cli()


F = pcbnew.F_Cu
B = pcbnew.B_Cu


def nm(mm):
    return pcbnew.FromMM(mm)


def v(x, y):
    return pcbnew.VECTOR2I(nm(x), nm(y))


def add_track(board, net_name, points, width, layer=F):
    net = board.FindNet(net_name)
    if net is None:
        raise RuntimeError(f"missing net {net_name}")
    for start, end in zip(points, points[1:]):
        if start == end:
            continue
        track = pcbnew.PCB_TRACK(board)
        track.SetStart(v(*start))
        track.SetEnd(v(*end))
        track.SetWidth(nm(width))
        track.SetLayer(layer)
        track.SetNet(net)
        board.Add(track)


def add_via(board, net_name, point, drill=0.3, diameter=0.6):
    net = board.FindNet(net_name)
    via = pcbnew.PCB_VIA(board)
    via.SetPosition(v(*point))
    via.SetDrill(nm(drill))
    via.SetWidth(nm(diameter))
    via.SetLayerPair(F, B)
    via.SetNet(net)
    board.Add(via)


def main():
    board_path = Path(sys.argv[1])
    board = pcbnew.LoadBoard(str(board_path))

    # Conservative local Stage 1 power routes. Keep J1 +5V_IN away from J1 GND pad.
    add_track(board, "/+5V_IN", [(14.0, 86.8), (11.25, 86.8), (11.25, 77.5), (13.6, 77.5)], 0.50)
    add_track(board, "/+5V_PROTECTED", [(22.062, 78.95), (19.5, 78.95), (19.5, 72.525), (21.0, 72.525)], 0.40)
    add_track(board, "/+5V_PROTECTED", [(21.0, 72.525), (19.5, 72.525), (19.5, 68.55), (21.0, 68.55)], 0.40)
    add_track(board, "/+5V_PROTECTED", [(21.0, 68.55), (14.0, 67.5)], 0.30)
    add_track(board, "/+5V_PROTECTED", [(21.0, 68.55), (27.863, 69.5), (27.863, 70.45)], 0.30)

    # Conservative local Stage 2 buck routes. Widths are reduced around TSOT/SMD pads to avoid shorts.
    add_track(board, "/BUCK_SW", [(30.137, 69.5), (35.525, 69.5)], 0.30)
    add_via(board, "/BUCK_SW", (26.225, 64.5))
    add_via(board, "/BUCK_SW", (30.137, 69.5))
    add_track(board, "/BUCK_SW", [(26.225, 64.5), (26.225, 66.25), (30.137, 66.25), (30.137, 69.5)], 0.25, B)
    add_track(board, "/BUCK_BST", [(30.137, 68.55), (31.25, 68.55), (31.25, 63.5), (27.775, 63.5), (27.775, 64.5)], 0.15)
    add_track(board, "+3V3", [(38.475, 69.5), (40.0, 69.5), (40.0, 63.025), (42.0, 63.025), (48.0, 63.025)], 0.40)

    pcbnew.SaveBoard(str(board_path), board)


if __name__ == "__main__":
    main()
