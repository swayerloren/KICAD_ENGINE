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

TARGET_NETS = ["/CC1", "/CC2", "/SHIELD", "/DM_C", "/DP_C", "/DM_E", "/DP_E", "/BOOT0", "/ESP_EN", "/U0RXD", "/U0TXD"]


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


def find_net(board, name):
    net = board.FindNet(name)
    if net is None:
        raise RuntimeError(f"missing net: {name}")
    return net


def iter_tracks(board):
    for item in board.GetTracks():
        yield item


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
    if track_exists(board, net_name, start, end, layer):
        return False
    track = pcbnew.PCB_TRACK(board)
    track.SetStart(v(*start))
    track.SetEnd(v(*end))
    track.SetWidth(nm(width))
    track.SetLayer(layer)
    track.SetNet(find_net(board, net_name))
    board.Add(track)
    return True


def add_via(board, net_name, point, drill=0.20, diameter=0.50):
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


def via_diameter_mm(via):
    for getter_name in ("TopLayer", "BottomLayer"):
        getter = getattr(via, getter_name, None)
        if getter is None:
            continue
        try:
            return mm(via.GetWidth(getter()))
        except Exception:
            continue
    for layer in (F, B):
        try:
            return mm(via.GetWidth(layer))
        except Exception:
            continue
    return None


def route_path(board, net_name, points, width, layer=F, via_points=None):
    added_tracks = 0
    added_vias = 0
    added_track_rows = []
    via_points = via_points or []
    for point in via_points:
        if add_via(board, net_name, point):
            added_vias += 1
    for start, end in zip(points, points[1:]):
        if add_track(board, net_name, start, end, width, layer):
            added_tracks += 1
            added_track_rows.append(
                {
                    "layer": layer_name(layer),
                    "start": [start[0], start[1]],
                    "end": [end[0], end[1]],
                    "width_mm": width,
                }
            )
    return {
        "tracks_added": added_tracks,
        "vias_added": added_vias,
        "tracks": added_track_rows,
        "vias": [{"x": point[0], "y": point[1]} for point in via_points],
    }


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
    return {net_name: collect_net_geometry(board, net_name) for net_name in TARGET_NETS}


def apply_batch_03(board):
    summary = {}

    summary["/CC1"] = route_path(
        board,
        "/CC1",
        [(37.750, 87.645), (37.750, 84.800), (32.325, 81.500)],
        0.20,
        F,
    )
    summary["/CC2"] = route_path(
        board,
        "/CC2",
        [(40.750, 87.645), (40.750, 84.000), (46.825, 84.000), (46.825, 81.500)],
        0.20,
        F,
    )
    summary["/SHIELD"] = {"tracks_added": 0, "vias_added": 0, "tracks": [], "vias": []}
    first = route_path(
        board,
        "/SHIELD",
        [(34.680, 88.220), (34.680, 92.400), (43.320, 92.400), (43.320, 88.220)],
        0.20,
        B,
        via_points=[(34.680, 88.220), (43.320, 88.220)],
    )
    second = route_path(
        board,
        "/SHIELD",
        [(43.320, 88.220), (51.825, 78.000)],
        0.20,
        B,
        via_points=[(51.825, 78.000)],
    )
    for part in (first, second):
        summary["/SHIELD"]["tracks_added"] += part["tracks_added"]
        summary["/SHIELD"]["vias_added"] += part["vias_added"]
        summary["/SHIELD"]["tracks"].extend(part["tracks"])
        summary["/SHIELD"]["vias"].extend(part["vias"])

    fill_existing_zones(board)
    return summary


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

    result = apply_batch_03(board)
    pcbnew.SaveBoard(str(board_path), board)
    output = {
        "applied": result,
        "after": collect_summary(board),
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
