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

FULL_REROUTE_NETS = []
LOCAL_5V_TRACKS_TO_REMOVE = []
LOCAL_5V_VIAS_TO_REMOVE = []
NEW_GND_VIAS = [
    (31.5, 44.775),
    (36.5, 44.775),
]


def nm(mm_value):
    return pcbnew.FromMM(mm_value)


def mm(nm_value):
    return round(pcbnew.ToMM(nm_value), 3)


def v(x, y):
    return pcbnew.VECTOR2I(nm(x), nm(y))


def layer_name(layer_id):
    return {pcbnew.F_Cu: "F.Cu", pcbnew.B_Cu: "B.Cu"}.get(layer_id, str(layer_id))


def same_point(a, b, tol=0.01):
    return abs(a[0] - b[0]) <= tol and abs(a[1] - b[1]) <= tol


def same_segment(a_start, a_end, b_start, b_end, tol=0.01):
    return (
        same_point(a_start, b_start, tol) and same_point(a_end, b_end, tol)
    ) or (
        same_point(a_start, b_end, tol) and same_point(a_end, b_start, tol)
    )


def find_net(board, name):
    net = board.FindNet(name)
    if net is None:
        raise RuntimeError(f"missing net: {name}")
    return net


def iter_tracks(board):
    for item in board.Tracks():
        yield item


def save_and_reload(board_path, board):
    pcbnew.SaveBoard(str(board_path), board)
    return pcbnew.LoadBoard(str(board_path))


def track_exists(board, net_name, start, end, layer, tol=0.01):
    for item in iter_tracks(board):
        if isinstance(item, pcbnew.PCB_VIA):
            continue
        if item.GetNetname() != net_name or item.GetLayer() != layer:
            continue
        s = item.GetStart()
        e = item.GetEnd()
        existing_start = (mm(s.x), mm(s.y))
        existing_end = (mm(e.x), mm(e.y))
        if same_segment(existing_start, existing_end, start, end, tol):
            return True
    return False


def via_exists(board, net_name, point, tol=0.01):
    for item in iter_tracks(board):
        if not isinstance(item, pcbnew.PCB_VIA):
            continue
        if item.GetNetname() != net_name:
            continue
        pos = item.GetPosition()
        if same_point((mm(pos.x), mm(pos.y)), point, tol):
            return True
    return False


def add_track(board, net_name, start, end, width, layer):
    if same_point(start, end) or track_exists(board, net_name, start, end, layer):
        return False
    track = pcbnew.PCB_TRACK(board)
    track.SetStart(v(*start))
    track.SetEnd(v(*end))
    track.SetWidth(nm(width))
    track.SetLayer(layer)
    track.SetNet(find_net(board, net_name))
    board.Add(track)
    return True


def add_via(board, net_name, point, drill=0.30, diameter=0.65):
    if via_exists(board, net_name, point):
        return False
    via = pcbnew.PCB_VIA(board)
    via.SetPosition(v(*point))
    via.SetDrill(nm(drill))
    via.SetWidth(nm(diameter))
    via.SetLayerPair(F, B)
    via.SetNet(find_net(board, net_name))
    board.Add(via)
    return True


def route_path(board, net_name, points, width, layer):
    added = 0
    rows = []
    for start, end in zip(points, points[1:]):
        if add_track(board, net_name, start, end, width, layer):
            added += 1
            rows.append(
                {
                    "layer": layer_name(layer),
                    "start": [start[0], start[1]],
                    "end": [end[0], end[1]],
                    "width_mm": width,
                }
            )
    return {"tracks_added": added, "tracks": rows}


def fill_existing_zones(board):
    filler = pcbnew.ZONE_FILLER(board)
    filler.Fill(board.Zones())


def remove_tracks_for_nets(board, net_names, existing_items=None):
    target_nets = set(net_names)
    removed = {net_name: {"segments": 0, "vias": 0} for net_name in net_names}
    source_items = existing_items if existing_items is not None else list(iter_tracks(board))
    for item in source_items:
        if item.GetNetname() not in target_nets:
            continue
        net_name = item.GetNetname()
        if isinstance(item, pcbnew.PCB_VIA):
            removed[net_name]["vias"] += 1
        else:
            removed[net_name]["segments"] += 1
        board.Remove(item)
    return removed


def remove_matching_track(board, net_name, layer, start, end, tol=0.01, existing_items=None):
    source_items = existing_items if existing_items is not None else list(iter_tracks(board))
    for item in source_items:
        if isinstance(item, pcbnew.PCB_VIA):
            continue
        if item.GetNetname() != net_name or item.GetLayer() != layer:
            continue
        item_start = (mm(item.GetStartX()), mm(item.GetStartY()))
        item_end = (mm(item.GetEndX()), mm(item.GetEndY()))
        if same_segment(item_start, item_end, start, end, tol):
            board.Remove(item)
            return True
    return False


def remove_matching_via(board, net_name, point, tol=0.01, existing_items=None):
    source_items = existing_items if existing_items is not None else list(iter_tracks(board))
    for item in source_items:
        if not isinstance(item, pcbnew.PCB_VIA):
            continue
        if item.GetNetname() != net_name:
            continue
        pos = item.GetPosition()
        if same_point((mm(pos.x), mm(pos.y)), point, tol):
            board.Remove(item)
            return True
    return False


def apply_repair(board_path):
    board = pcbnew.LoadBoard(str(board_path))
    existing_items = list(iter_tracks(board))
    result = {
        "removed_full_net_geometry": remove_tracks_for_nets(board, FULL_REROUTE_NETS, existing_items),
        "removed_local_5v_tracks": [],
        "removed_local_5v_vias": [],
        "added": {},
        "added_gnd_vias": [],
    }

    for net_name, layer, start, end in LOCAL_5V_TRACKS_TO_REMOVE:
        if remove_matching_track(board, net_name, layer, start, end, existing_items=existing_items):
            result["removed_local_5v_tracks"].append(
                {"net": net_name, "layer": layer_name(layer), "start": [start[0], start[1]], "end": [end[0], end[1]]}
            )

    for net_name, point in LOCAL_5V_VIAS_TO_REMOVE:
        if remove_matching_via(board, net_name, point, existing_items=existing_items):
            result["removed_local_5v_vias"].append({"net": net_name, "point": [point[0], point[1]]})

    board = save_and_reload(board_path, board)

    result["added"]["/BOOT0"] = [
        route_path(board, "/BOOT0", [(5.15, 66.625), (5.15, 61.375)], 0.20, F)
    ]

    result["added"]["/ESP_EN"] = [
        route_path(board, "/ESP_EN", [(5.15, 56.625), (5.15, 51.375)], 0.20, F)
    ]

    result["added"]["/DM_E"] = []
    if add_via(board, "/DM_E", (18.0, 37.98)):
        result["added"]["/DM_E"].append({"via": [18.0, 37.98], "drill_mm": 0.30, "diameter_mm": 0.65})
    if add_via(board, "/DM_E", (34.825, 74.0)):
        result["added"]["/DM_E"].append({"via": [34.825, 74.0], "drill_mm": 0.30, "diameter_mm": 0.65})
    if add_via(board, "/DM_E", (55.0, 72.0)):
        result["added"]["/DM_E"].append({"via": [55.0, 72.0], "drill_mm": 0.30, "diameter_mm": 0.65})
    result["added"]["/DM_E"].append(route_path(board, "/DM_E", [(21.25, 37.98), (18.0, 37.98)], 0.20, F))
    result["added"]["/DM_E"].append(route_path(board, "/DM_E", [(18.0, 37.98), (18.0, 41.0), (11.0, 41.0), (11.0, 74.0), (34.825, 74.0)], 0.20, B))
    result["added"]["/DM_E"].append(route_path(board, "/DM_E", [(34.825, 74.0), (33.825, 75.0)], 0.20, F))
    result["added"]["/DM_E"].append(route_path(board, "/DM_E", [(34.825, 74.0), (55.0, 74.0), (55.0, 72.0)], 0.20, B))
    result["added"]["/DM_E"].append(route_path(board, "/DM_E", [(55.0, 72.0), (57.0, 72.0)], 0.20, F))

    result["added"]["/DP_E"] = []

    for point in NEW_GND_VIAS:
        if add_via(board, "GND", point):
            result["added_gnd_vias"].append({"x": point[0], "y": point[1], "diameter_mm": 0.65, "drill_mm": 0.30})

    fill_existing_zones(board)
    board = save_and_reload(board_path, board)
    return result, board


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("board_path")
    parser.add_argument("mode", choices=["apply"])
    args = parser.parse_args()

    board_path = Path(args.board_path)
    result, _board = apply_repair(board_path)
    print(json.dumps({"applied": result}, indent=2))


if __name__ == "__main__":
    main()
