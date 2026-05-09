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


SUMMARY_NETS = ["+3V3", "/+5V_IN", "/+5V_FUSED", "/+5V_PROTECTED", "/BUCK_SW", "/BUCK_BST"]
REROUTE_NETS = ["/+5V_IN", "/+5V_FUSED", "/+5V_PROTECTED"]


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


def find_net(board, name):
    net = board.FindNet(name)
    if net is None:
        raise RuntimeError(f"missing net: {name}")
    return net


def iter_tracks(board):
    for item in board.GetTracks():
        yield item


def same_point(a, b, tol=0.01):
    return abs(a[0] - b[0]) <= tol and abs(a[1] - b[1]) <= tol


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
        if same_point(existing_start, start, tol) and same_point(existing_end, end, tol):
            return True
        if same_point(existing_start, end, tol) and same_point(existing_end, start, tol):
            return True
    return False


def add_track(board, net_name, start, end, width, layer):
    if same_point(start, end):
        return False
    track = pcbnew.PCB_TRACK(board)
    track.SetStart(v(*start))
    track.SetEnd(v(*end))
    track.SetWidth(nm(width))
    track.SetLayer(layer)
    track.SetNet(find_net(board, net_name))
    board.Add(track)
    return True


def route_path(board, net_name, points, width, layer=F):
    added = 0
    for start, end in zip(points, points[1:]):
        if add_track(board, net_name, start, end, width, layer):
            added += 1
    return added


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


def remove_tracks_for_nets(board, net_names):
    target_nets = set(net_names)
    removed = {net_name: {"segments": 0, "vias": 0} for net_name in net_names}
    items_to_remove = [track for track in board.GetTracks() if track.GetNetname() in target_nets]
    for item in items_to_remove:
        net_name = item.GetNetname()
        if isinstance(item, pcbnew.PCB_VIA):
            removed[net_name]["vias"] += 1
        else:
            removed[net_name]["segments"] += 1
        board.Remove(item)
    return removed


def apply_batch_02(board):
    removed = remove_tracks_for_nets(board, REROUTE_NETS)

    added = {}
    added["/+5V_IN"] = route_path(board, "/+5V_IN", [(14.000, 86.800), (14.000, 77.900), (13.600, 77.500)], 0.75, F)
    added["/+5V_FUSED"] = route_path(board, "/+5V_FUSED", [(16.400, 77.500), (21.562, 77.500), (22.062, 78.000)], 0.75, F)

    protected_added = 0
    protected_added += route_path(board, "/+5V_PROTECTED", [(14.000, 67.500), (16.000, 69.500), (21.950, 69.500)], 0.75, F)
    protected_added += route_path(board, "/+5V_PROTECTED", [(21.950, 69.500), (22.475, 70.025), (22.475, 74.000), (23.938, 75.463), (23.938, 77.050)], 0.75, F)
    protected_added += route_path(board, "/+5V_PROTECTED", [(21.950, 69.500), (26.600, 69.500)], 0.75, F)
    protected_added += route_path(board, "/+5V_PROTECTED", [(26.600, 69.500), (27.863, 69.500), (27.863, 70.450)], 0.50, F)
    added["/+5V_PROTECTED"] = protected_added

    fill_existing_zones(board)
    return {"removed": removed, "added_segments": added}


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

    result = apply_batch_02(board)
    pcbnew.SaveBoard(str(board_path), board)
    result["after"] = collect_summary(board)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
