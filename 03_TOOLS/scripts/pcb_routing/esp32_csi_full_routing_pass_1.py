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


def route_path(board, net_name, points, width, layer=F, via_points=None):
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


def fill_existing_zones(board):
    filler = pcbnew.ZONE_FILLER(board)
    filler.Fill(board.Zones())


def main():
    if len(sys.argv) < 2:
        raise SystemExit(
            "usage: esp32_csi_full_routing_pass_1.py <board_path> [scenario ...]\n"
            "scenarios: leds status uart uart_tx uart_rx esp_en boot0 p5v_tp usb_low usb_vbus gnd_cleanup"
        )

    board_path = Path(sys.argv[1])
    requested = set(sys.argv[2:])
    board = pcbnew.LoadBoard(str(board_path))

    summary = {"tracks": 0, "vias": 0, "nets": {}}

    def apply(net_name, points, width, layer=F, via_points=None):
        added_tracks, added_vias = route_path(board, net_name, points, width, layer=layer, via_points=via_points)
        summary["tracks"] += added_tracks
        summary["vias"] += added_vias
        net_summary = summary["nets"].setdefault(net_name, {"tracks": 0, "vias": 0})
        net_summary["tracks"] += added_tracks
        net_summary["vias"] += added_vias

    def want(name):
        return not requested or name in requested

    if want("leds"):
        apply("/PLED", [(38.175, 58.000), (39.788, 55.000)], 0.20, F)
        apply("/SLED", [(44.175, 58.000), (45.788, 55.000)], 0.20, F)

    if want("status"):
        apply("/STATUS_LED", [(38.750, 25.280), (40.800, 25.280)], 0.20, F)
        apply("/STATUS_LED", [(40.800, 25.280), (41.000, 25.280), (41.000, 59.000), (46.800, 59.000)], 0.20, B, via_points=[(40.800, 25.280), (46.800, 59.000)])
        apply("/STATUS_LED", [(46.800, 59.000), (45.825, 58.000)], 0.20, F)

    if want("uart") or want("uart_tx"):
        apply("/U0TXD", [(38.750, 26.550), (49.000, 26.550), (49.000, 60.000), (57.000, 60.000)], 0.20, F)

    if want("uart") or want("uart_rx"):
        apply("/U0RXD", [(38.750, 27.820), (43.500, 27.820)], 0.20, F)
        apply("/U0RXD", [(43.500, 27.820), (43.500, 72.000), (55.000, 72.000), (55.000, 64.000)], 0.20, B, via_points=[(43.500, 27.820), (55.000, 64.000)])
        apply("/U0RXD", [(55.000, 64.000), (57.000, 64.000)], 0.20, F)

    if want("esp_en"):
        apply("/ESP_EN", [(21.250, 25.280), (17.000, 25.280), (17.000, 53.000), (12.175, 53.000)], 0.20, F)
        apply("/ESP_EN", [(12.175, 53.000), (13.775, 53.000), (13.775, 57.000)], 0.20, F)
        apply("/ESP_EN", [(12.175, 53.000), (5.150, 53.000), (5.150, 51.375)], 0.20, F)
        apply("/ESP_EN", [(5.150, 51.375), (5.150, 56.625)], 0.20, F)
        apply("/ESP_EN", [(21.250, 25.280), (17.000, 25.280), (17.000, 42.000), (57.000, 42.000), (57.000, 44.000)], 0.20, F)

    if want("boot0"):
        apply("/BOOT0", [(38.750, 39.250), (40.000, 39.250), (40.000, 46.500), (12.175, 46.500), (12.175, 64.000)], 0.20, F)
        apply("/BOOT0", [(12.175, 64.000), (5.150, 64.000), (5.150, 61.375)], 0.20, F)
        apply("/BOOT0", [(5.150, 61.375), (5.150, 66.625)], 0.20, F)
        apply("/BOOT0", [(40.000, 46.500), (57.000, 46.500), (57.000, 52.000)], 0.20, F)

    if want("p5v_tp"):
        apply("/+5V_PROTECTED", [(27.863, 70.450), (53.000, 70.450), (53.000, 40.000), (57.000, 40.000)], 0.30, F)

    if want("usb_low"):
        apply("/CC1", [(37.750, 87.645), (32.325, 81.500)], 0.20, F)
        apply("/CC2", [(40.750, 87.645), (46.825, 81.500)], 0.20, F)
        apply("/SHIELD", [(34.680, 88.220), (34.680, 92.400), (43.320, 92.400), (43.320, 88.220), (51.825, 78.000)], 0.20, B, via_points=[(34.680, 88.220), (43.320, 88.220), (51.825, 78.000)])

    if want("usb_vbus"):
        apply("unconnected-(J2-VBUS-PadA4)", [(36.600, 87.645), (36.600, 86.800), (41.400, 86.800), (41.400, 87.645)], 0.20, B, via_points=[(36.600, 87.645), (41.400, 87.645)])

    if want("gnd_cleanup"):
        gnd_vias = [
            (14.000, 71.500),
            (19.525, 74.000),
            (20.050, 69.500),
            (23.938, 78.950),
            (30.137, 70.450),
            (30.675, 81.500),
            (37.862, 78.950),
            (45.175, 81.500),
            (50.175, 78.000),
            (42.000, 65.975),
            (48.000, 65.975),
            (38.212, 55.000),
            (44.212, 55.000),
            (57.000, 56.000),
        ]
        gnd_added = 0
        for point in gnd_vias:
            if add_via(board, "GND", point):
                gnd_added += 1
        summary["vias"] += gnd_added
        summary["nets"]["GND"] = {"tracks": 0, "vias": gnd_added}
        apply("GND", [(35.800, 86.800), (42.200, 86.800)], 0.25, F)

    fill_existing_zones(board)
    pcbnew.SaveBoard(str(board_path), board)

    print(f"TRACKS_ADDED={summary['tracks']}")
    print(f"VIAS_ADDED={summary['vias']}")
    for net_name in sorted(summary["nets"]):
        per_net = summary["nets"][net_name]
        print(f"NET {net_name} TRACKS={per_net['tracks']} VIAS={per_net['vias']}")


if __name__ == "__main__":
    main()
