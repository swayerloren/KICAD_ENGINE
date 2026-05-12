import argparse
import json
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
LAYER_BY_NAME = {"F.Cu": F, "B.Cu": B}


TRIALS = {
    "usb_top": [
        {
            "net": "/DM_C",
            "kind": "track",
            "width": 0.15,
            "layer": "F.Cu",
            "points": [
                (38.25, 87.645),
                (38.25, 78.3875),
                (37.8625, 78.0),
            ],
        },
        {
            "net": "/DM_C",
            "kind": "track",
            "width": 0.15,
            "layer": "F.Cu",
            "points": [
                (39.25, 87.645),
                (39.25, 86.645),
                (38.25, 85.645),
            ],
        },
        {
            "net": "/DM_C",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (37.8625, 78.0),
                (35.175, 78.0),
                (32.175, 75.0),
            ],
        },
        {
            "net": "/DP_C",
            "kind": "track",
            "width": 0.15,
            "layer": "F.Cu",
            "points": [
                (38.75, 87.645),
                (38.75, 77.9375),
                (37.8625, 77.05),
            ],
        },
        {
            "net": "/DP_C",
            "kind": "track",
            "width": 0.15,
            "layer": "F.Cu",
            "points": [
                (39.75, 87.645),
                (39.75, 86.645),
                (38.75, 85.645),
            ],
        },
        {
            "net": "/DP_C",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (37.8625, 77.05),
                (42.125, 77.05),
                (44.175, 75.0),
            ],
        },
    ],
    "controls_rework": [
        {
            "kind": "remove_net_copper",
            "nets": ["/STATUS_LED", "/U0RXD", "/U0TXD"],
        },
        {
            "net": "/STATUS_LED",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (38.75, 25.28),
                (40.0, 25.28),
            ],
        },
        {
            "net": "/STATUS_LED",
            "kind": "via",
            "point": (40.0, 25.28),
            "drill": 0.30,
            "diameter": 0.65,
        },
        {
            "net": "/STATUS_LED",
            "kind": "track",
            "width": 0.20,
            "layer": "B.Cu",
            "points": [
                (40.0, 25.28),
                (40.0, 52.175),
                (45.825, 58.0),
            ],
        },
        {
            "net": "/U0TXD",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (38.75, 26.55),
                (41.0, 26.55),
            ],
        },
        {
            "net": "/U0TXD",
            "kind": "via",
            "point": (41.0, 26.55),
            "drill": 0.30,
            "diameter": 0.65,
        },
        {
            "net": "/U0TXD",
            "kind": "track",
            "width": 0.20,
            "layer": "B.Cu",
            "points": [
                (41.0, 26.55),
                (41.0, 44.0),
                (57.0, 60.0),
            ],
        },
        {
            "net": "/U0RXD",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (38.75, 27.82),
                (42.0, 27.82),
            ],
        },
        {
            "net": "/U0RXD",
            "kind": "via",
            "point": (42.0, 27.82),
            "drill": 0.30,
            "diameter": 0.65,
        },
        {
            "net": "/U0RXD",
            "kind": "track",
            "width": 0.20,
            "layer": "B.Cu",
            "points": [
                (42.0, 27.82),
                (42.0, 49.0),
                (57.0, 64.0),
            ],
        },
        {
            "net": "/BOOT0",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (38.75, 39.25),
                (40.25, 39.25),
                (53.0, 52.0),
                (57.0, 52.0),
            ],
        },
        {
            "net": "/BOOT0",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (38.75, 39.25),
                (39.75, 40.25),
                (39.75, 41.5),
                (17.25, 64.0),
                (12.175, 64.0),
            ],
        },
        {
            "net": "/ESP_EN",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (21.25, 25.28),
                (22.5, 25.28),
                (41.22, 44.0),
                (57.0, 44.0),
            ],
        },
        {
            "net": "/ESP_EN",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (21.25, 25.28),
                (20.25, 25.28),
                (20.25, 49.525),
                (13.775, 56.0),
            ],
        },
        {
            "net": "/+5V_PROTECTED",
            "kind": "track",
            "width": 0.50,
            "layer": "F.Cu",
            "points": [
                (26.8, 69.5),
                (27.8, 69.5),
                (57.0, 40.3),
                (57.0, 40.0),
            ],
        },
        {
            "net": "/DP_E",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (21.25, 39.25),
                (18.0, 39.25),
            ],
        },
        {
            "net": "/DP_E",
            "kind": "via",
            "point": (18.0, 39.25),
            "drill": 0.30,
            "diameter": 0.65,
        },
        {
            "net": "/DP_E",
            "kind": "track",
            "width": 0.20,
            "layer": "B.Cu",
            "points": [
                (18.0, 39.25),
                (18.0, 44.175),
                (46.825, 73.0),
            ],
        },
        {
            "net": "/DP_E",
            "kind": "via",
            "point": (46.825, 73.0),
            "drill": 0.30,
            "diameter": 0.65,
        },
        {
            "net": "/DP_E",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (46.825, 73.0),
                (46.825, 74.0),
                (45.825, 75.0),
            ],
        },
        {
            "net": "/DP_E",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (46.825, 73.0),
                (52.0, 73.0),
                (57.0, 68.0),
            ],
        },
    ],
    "tp1_diag": [
        {
            "net": "/+5V_PROTECTED",
            "kind": "track",
            "width": 0.50,
            "layer": "F.Cu",
            "points": [
                (26.8, 69.5),
                (27.8, 69.5),
                (57.0, 40.3),
                (57.0, 40.0),
            ],
        },
    ],
    "tp1_alt": [
        {
            "net": "/+5V_PROTECTED",
            "kind": "track",
            "width": 0.50,
            "layer": "F.Cu",
            "points": [
                (26.8, 69.5),
                (31.5, 69.5),
                (38.0, 63.0),
                (40.5, 63.0),
                (57.0, 46.5),
                (57.0, 40.0),
            ],
        },
    ],
    "dp_e_manual": [
        {
            "net": "/DP_E",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (21.25, 39.25),
                (18.0, 39.25),
            ],
        },
        {
            "net": "/DP_E",
            "kind": "via",
            "point": (18.0, 39.25),
            "drill": 0.30,
            "diameter": 0.65,
        },
        {
            "net": "/DP_E",
            "kind": "track",
            "width": 0.20,
            "layer": "B.Cu",
            "points": [
                (18.0, 39.25),
                (18.0, 44.175),
                (46.825, 73.0),
            ],
        },
        {
            "net": "/DP_E",
            "kind": "via",
            "point": (46.825, 73.0),
            "drill": 0.30,
            "diameter": 0.65,
        },
        {
            "net": "/DP_E",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (46.825, 73.0),
                (46.825, 74.0),
                (45.825, 75.0),
            ],
        },
        {
            "net": "/DP_E",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (46.825, 73.0),
                (52.0, 73.0),
                (57.0, 68.0),
            ],
        },
    ],
    "boot0_manual": [
        {
            "net": "/BOOT0",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (38.75, 39.25),
                (40.25, 39.25),
                (53.0, 52.0),
                (57.0, 52.0),
            ],
        },
        {
            "net": "/BOOT0",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (38.75, 39.25),
                (39.75, 40.25),
                (39.75, 41.5),
                (17.25, 64.0),
                (12.175, 64.0),
            ],
        },
    ],
    "esp_en_manual": [
        {
            "net": "/ESP_EN",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (21.25, 25.28),
                (22.5, 25.28),
                (41.22, 44.0),
                (57.0, 44.0),
            ],
        },
        {
            "net": "/ESP_EN",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (21.25, 25.28),
                (20.25, 25.28),
                (20.25, 49.525),
                (13.775, 56.0),
            ],
        },
    ],
    "right_fanout_rework": [
        {
            "kind": "remove_net_copper",
            "nets": ["/STATUS_LED", "/U0RXD", "/U0TXD"],
        },
        {
            "net": "/STATUS_LED",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (38.75, 25.28),
                (44.0, 25.28),
            ],
        },
        {
            "net": "/STATUS_LED",
            "kind": "via",
            "point": (44.0, 25.28),
            "drill": 0.30,
            "diameter": 0.65,
        },
        {
            "net": "/STATUS_LED",
            "kind": "track",
            "width": 0.20,
            "layer": "B.Cu",
            "points": [
                (44.0, 25.28),
                (44.0, 56.175),
                (45.825, 58.0),
            ],
        },
        {
            "net": "/U0TXD",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (38.75, 26.55),
                (46.0, 26.55),
            ],
        },
        {
            "net": "/U0TXD",
            "kind": "via",
            "point": (46.0, 26.55),
            "drill": 0.30,
            "diameter": 0.65,
        },
        {
            "net": "/U0TXD",
            "kind": "track",
            "width": 0.20,
            "layer": "B.Cu",
            "points": [
                (46.0, 26.55),
                (46.0, 49.0),
                (57.0, 60.0),
            ],
        },
        {
            "net": "/U0RXD",
            "kind": "track",
            "width": 0.20,
            "layer": "F.Cu",
            "points": [
                (38.75, 27.82),
                (48.0, 27.82),
            ],
        },
        {
            "net": "/U0RXD",
            "kind": "via",
            "point": (48.0, 27.82),
            "drill": 0.30,
            "diameter": 0.65,
        },
        {
            "net": "/U0RXD",
            "kind": "track",
            "width": 0.20,
            "layer": "B.Cu",
            "points": [
                (48.0, 27.82),
                (48.0, 55.0),
                (57.0, 64.0),
            ],
        },
    ],
}


def nm(mm_value):
    return pcbnew.FromMM(mm_value)


def v(x_mm, y_mm):
    return pcbnew.VECTOR2I(nm(x_mm), nm(y_mm))


def add_track(board, net_name, layer_name, width_mm, points_mm):
    net = board.FindNet(net_name)
    if net is None:
        raise RuntimeError(f"missing net {net_name}")
    layer = LAYER_BY_NAME[layer_name]
    for start, end in zip(points_mm, points_mm[1:]):
        track = pcbnew.PCB_TRACK(board)
        track.SetStart(v(*start))
        track.SetEnd(v(*end))
        track.SetWidth(nm(width_mm))
        track.SetLayer(layer)
        track.SetNet(net)
        board.Add(track)


def add_via(board, net_name, point_mm, drill_mm, diameter_mm):
    net = board.FindNet(net_name)
    if net is None:
        raise RuntimeError(f"missing net {net_name}")
    via = pcbnew.PCB_VIA(board)
    via.SetPosition(v(*point_mm))
    via.SetDrill(nm(drill_mm))
    via.SetWidth(nm(diameter_mm))
    via.SetLayerPair(F, B)
    via.SetNet(net)
    board.Add(via)


def remove_net_copper(board, net_names):
    wanted = set(net_names)
    to_remove = [item for item in board.GetTracks() if item.GetNetname() in wanted]
    for item in to_remove:
        board.Remove(item)


def fill_zones(board):
    pcbnew.ZONE_FILLER(board).Fill(board.Zones())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("board_path")
    parser.add_argument("mode", choices=["apply"])
    parser.add_argument("--trial", choices=sorted(TRIALS.keys()), required=True)
    parser.add_argument("--fill", action="store_true")
    args = parser.parse_args()

    board = pcbnew.LoadBoard(args.board_path)
    applied = []
    for action in TRIALS[args.trial]:
        if action["kind"] == "remove_net_copper":
            remove_net_copper(board, action["nets"])
            applied.append(action)
        elif action["kind"] == "track":
            add_track(board, action["net"], action["layer"], action["width"], action["points"])
            applied.append(action)
        elif action["kind"] == "via":
            add_via(board, action["net"], action["point"], action["drill"], action["diameter"])
            applied.append(action)
        else:
            raise RuntimeError(f"unsupported action kind {action['kind']}")

    if args.fill:
        fill_zones(board)
    pcbnew.SaveBoard(args.board_path, board)
    print(json.dumps({"trial": args.trial, "applied": applied}, indent=2))


if __name__ == "__main__":
    main()
