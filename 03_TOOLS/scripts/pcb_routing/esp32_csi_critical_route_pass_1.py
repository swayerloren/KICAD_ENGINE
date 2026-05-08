import math
import sys
from pathlib import Path

import pcbnew


F = pcbnew.F_Cu
B = pcbnew.B_Cu


def nm(mm_value):
    return pcbnew.FromMM(mm_value)


def mm(nm_value):
    return pcbnew.ToMM(nm_value)


def v(x, y):
    return pcbnew.VECTOR2I(nm(x), nm(y))


def close_mm(a, b, tol=0.01):
    return abs(a - b) <= tol


def same_point(a, b, tol=0.01):
    return close_mm(a[0], b[0], tol) and close_mm(a[1], b[1], tol)


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
        existing = (mm(pos.x), mm(pos.y))
        if same_point(existing, point, tol):
            return True
    return False


def track_exists(board, net_name, start, end, layer, tol=0.01):
    for item in iter_tracks(board):
        if isinstance(item, pcbnew.PCB_VIA):
            continue
        if item.GetNetname() != net_name:
            continue
        if item.GetLayer() != layer:
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


def route_path(board, net_name, points, width, layer=B, via_points=None):
    added_tracks = 0
    added_vias = 0
    via_points = via_points or []
    for point in via_points:
        if add_via(board, net_name, point):
            added_vias += 1
    for start, end in zip(points, points[1:]):
        if add_track(board, net_name, start, end, width, layer):
            added_tracks += 1
    return added_tracks, added_vias


def add_gnd_vias(board):
    added = 0
    pad_center_points = [
        (12.225, 57.000), (21.500, 44.950), (26.500, 44.775),
        (21.250, 22.740), (38.750, 22.740),
        (6.850, 51.375), (6.850, 56.625), (6.850, 61.375), (6.850, 66.625),
    ]
    for point in pad_center_points:
        if add_via(board, "GND", point, drill=0.20, diameter=0.50):
            added += 1

    stitching_points = [
        (10.0, 30.0), (50.0, 30.0), (10.0, 50.0), (50.0, 50.0), (10.0, 75.0),
        (50.0, 75.0),
    ]
    for point in stitching_points:
        if add_via(board, "GND", point, drill=0.30, diameter=0.65):
            added += 1
    return added


def fill_existing_zones(board):
    filler = pcbnew.ZONE_FILLER(board)
    filler.Fill(board.Zones())


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: esp32_csi_critical_route_pass_1.py <board_path>")

    board_path = Path(sys.argv[1])
    board = pcbnew.LoadBoard(str(board_path))

    summary = {
        "tracks": 0,
        "vias": 0,
        "nets": {},
    }

    critical_routes = [
        ("+3V3", [(38.475, 69.500), (38.475, 63.025), (42.000, 63.025), (48.000, 63.025), (48.000, 46.000), (57.000, 46.000), (57.000, 48.000)], 0.45, B, [(38.475, 69.500), (57.000, 48.000)]),
        ("+3V3", [(39.825, 58.000), (39.825, 63.025), (42.000, 63.025)], 0.35, B, [(39.825, 58.000)]),
        ("+3V3", [(21.250, 24.010), (21.250, 43.050), (21.500, 43.050), (26.500, 43.225)], 0.35, B, [(21.250, 24.010), (21.500, 43.050), (26.500, 43.225)]),
        ("+3V3", [(21.500, 43.050), (13.825, 43.050), (13.825, 53.000), (13.825, 64.000), (38.475, 64.000), (38.475, 63.025)], 0.35, B, [(13.825, 53.000), (13.825, 64.000)]),
    ]

    for net_name, points, width, layer, via_points in critical_routes:
        added_tracks, added_vias = route_path(board, net_name, points, width, layer=layer, via_points=via_points)
        summary["tracks"] += added_tracks
        summary["vias"] += added_vias
        per_net = summary["nets"].setdefault(net_name, {"tracks": 0, "vias": 0})
        per_net["tracks"] += added_tracks
        per_net["vias"] += added_vias

    gnd_vias_added = add_gnd_vias(board)
    summary["vias"] += gnd_vias_added
    summary["nets"]["GND"] = {"tracks": 0, "vias": gnd_vias_added}

    fill_existing_zones(board)
    pcbnew.SaveBoard(str(board_path), board)

    print(f"TRACKS_ADDED={summary['tracks']}")
    print(f"VIAS_ADDED={summary['vias']}")
    for net_name in sorted(summary["nets"]):
        per_net = summary["nets"][net_name]
        print(f"NET {net_name} TRACKS={per_net['tracks']} VIAS={per_net['vias']}")


if __name__ == "__main__":
    main()
