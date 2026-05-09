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

SUMMARY_NETS = ["+3V3", "/+5V_IN", "/+5V_FUSED", "/+5V_PROTECTED", "/BUCK_SW", "/BUCK_BST", "GND"]
FULL_REROUTE_NETS = ["/+5V_PROTECTED", "/BUCK_SW", "/BUCK_BST"]
LOCAL_3V3_VIAS_TO_REMOVE = [
    (26.113, 66.800),
    (38.475, 69.500),
]
OLD_GND_VIAS_TO_REMOVE = [
    (18.200, 71.800),
]
LOCAL_3V3_TRACKS_TO_REMOVE = [
    ("+3V3", F, (38.475, 66.550), (42.000, 63.025)),
    ("+3V3", F, (27.863, 68.550), (26.113, 66.800)),
    ("+3V3", F, (38.475, 66.550), (38.475, 69.500)),
    ("+3V3", F, (42.000, 63.025), (48.000, 63.025)),
    ("+3V3", B, (26.113, 66.800), (38.475, 66.550)),
    ("+3V3", B, (38.475, 69.500), (38.475, 63.025)),
    ("+3V3", B, (38.475, 64.000), (38.475, 63.025)),
    ("+3V3", B, (38.475, 63.025), (42.000, 63.025)),
    ("+3V3", B, (13.825, 53.000), (13.825, 64.000)),
    ("+3V3", B, (13.825, 64.000), (38.475, 64.000)),
]
NEW_GND_VIAS = [
    (19.000, 72.600),
    (43.500, 65.975),
]


def nm(mm_value):
    return pcbnew.FromMM(mm_value)


def mm(nm_value):
    return round(pcbnew.ToMM(nm_value), 3)


def v(x, y):
    return pcbnew.VECTOR2I(nm(x), nm(y))


def layer_name(layer_id):
    return {
        pcbnew.F_Cu: "F.Cu",
        pcbnew.B_Cu: "B.Cu",
    }.get(layer_id, str(layer_id))


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


def via_diameter_mm(via):
    for layer in (F, B):
        try:
            return mm(via.GetWidth(layer))
        except Exception:
            continue
    return None


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


def route_path(board, net_name, points, width, layer=F):
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


def collect_net_geometry(board, net_name):
    segments = []
    vias = []
    for item in iter_tracks(board):
        if item.GetNetname() != net_name:
            continue
        if isinstance(item, pcbnew.PCB_VIA):
            pos = item.GetPosition()
            vias.append(
                {
                    "x": mm(pos.x),
                    "y": mm(pos.y),
                    "diameter_mm": via_diameter_mm(item),
                    "drill_mm": mm(item.GetDrillValue()),
                }
            )
            continue
        start = item.GetStart()
        end = item.GetEnd()
        segments.append(
            {
                "layer": layer_name(item.GetLayer()),
                "start": [mm(start.x), mm(start.y)],
                "end": [mm(end.x), mm(end.y)],
                "width_mm": mm(item.GetWidth()),
            }
        )
    return {
        "segment_count": len(segments),
        "via_count": len(vias),
        "segments": sorted(segments, key=lambda s: (s["layer"], s["start"][1], s["start"][0], s["end"][1], s["end"][0])),
        "vias": sorted(vias, key=lambda x: (x["y"], x["x"])),
    }


def collect_summary(board):
    return {net_name: collect_net_geometry(board, net_name) for net_name in SUMMARY_NETS}


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
    result = {
        "removed_full_net_geometry": {},
        "removed_local_3v3_tracks": [],
        "removed_local_3v3_vias": [],
        "added": {},
        "added_gnd_vias": [],
    }
    existing_items = list(iter_tracks(board))
    result["removed_full_net_geometry"] = remove_tracks_for_nets(board, FULL_REROUTE_NETS, existing_items)

    for net_name, layer, start, end in LOCAL_3V3_TRACKS_TO_REMOVE:
        if remove_matching_track(board, net_name, layer, start, end, existing_items=existing_items):
            result["removed_local_3v3_tracks"].append(
                {
                    "net": net_name,
                    "layer": layer_name(layer),
                    "start": [start[0], start[1]],
                    "end": [end[0], end[1]],
                }
            )

    for point in LOCAL_3V3_VIAS_TO_REMOVE:
        if remove_matching_via(board, "+3V3", point, existing_items=existing_items):
            result["removed_local_3v3_vias"].append({"net": "+3V3", "point": [point[0], point[1]]})

    for point in OLD_GND_VIAS_TO_REMOVE:
        remove_matching_via(board, "GND", point, existing_items=existing_items)

    board = save_and_reload(board_path, board)

    result["added"]["/+5V_PROTECTED"] = []
    result["added"]["/+5V_PROTECTED"].append(
        route_path(
            board,
            "/+5V_PROTECTED",
            [(14.000, 67.500), (17.500, 71.000), (21.425, 71.000), (21.950, 70.475), (21.950, 69.500)],
            0.75,
            F,
        )
    )
    result["added"]["/+5V_PROTECTED"].append(
        route_path(board, "/+5V_PROTECTED", [(21.950, 69.500), (22.475, 70.025), (22.475, 74.000), (23.938, 75.463), (23.938, 77.050)], 0.75, F)
    )
    result["added"]["/+5V_PROTECTED"].append(
        route_path(board, "/+5V_PROTECTED", [(21.950, 69.500), (26.800, 69.500)], 0.75, F)
    )
    result["added"]["/+5V_PROTECTED"].append(
        route_path(board, "/+5V_PROTECTED", [(26.800, 69.500), (27.863, 69.500), (27.863, 70.450)], 0.50, F)
    )

    result["added"]["/BUCK_SW"] = [
        route_path(board, "/BUCK_SW", [(30.137, 69.500), (32.400, 69.500), (35.525, 69.500)], 0.60, F)
    ]
    result["added"]["/BUCK_BST"] = [
        route_path(board, "/BUCK_BST", [(30.137, 68.550), (30.737, 67.950), (32.400, 67.950)], 0.25, F)
    ]
    result["added"]["+3V3"] = []
    result["added"]["+3V3"].append(
        route_path(board, "+3V3", [(27.863, 68.550), (29.863, 66.550), (38.475, 66.550)], 0.25, F)
    )
    result["added"]["+3V3"].append(
        route_path(board, "+3V3", [(38.475, 69.500), (38.475, 66.550), (42.000, 63.025)], 0.60, F)
    )
    result["added"]["+3V3"].append(
        route_path(board, "+3V3", [(42.000, 63.025), (48.000, 63.025)], 0.60, F)
    )
    result["added"]["+3V3"].append(
        route_path(board, "+3V3", [(38.475, 66.550), (38.475, 63.025), (42.000, 63.025)], 0.60, B)
    )
    result["added"]["+3V3"].append(
        route_path(board, "+3V3", [(13.825, 53.000), (13.825, 64.000), (38.475, 64.000)], 0.50, B)
    )

    for point in NEW_GND_VIAS:
        if add_via(board, "GND", point):
            result["added_gnd_vias"].append({"x": point[0], "y": point[1], "diameter_mm": 0.65, "drill_mm": 0.30})

    fill_existing_zones(board)
    board = save_and_reload(board_path, board)
    return result, board


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("board_path")
    parser.add_argument("mode", choices=["summary", "apply"])
    args = parser.parse_args()

    board_path = Path(args.board_path)
    board = pcbnew.LoadBoard(str(board_path))

    if args.mode == "summary":
        print(json.dumps(collect_summary(board), indent=2))
        return

    result, _board = apply_repair(board_path)
    output = {
        "applied": result,
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
