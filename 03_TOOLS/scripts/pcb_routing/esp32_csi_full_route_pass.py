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


def find_net(board, name):
    net = board.FindNet(name)
    if net is None:
        raise RuntimeError(f"missing net: {name}")
    return net


def add_track(board, net, start, end, width, layer):
    if start == end:
        return
    track = pcbnew.PCB_TRACK(board)
    track.SetStart(v(*start))
    track.SetEnd(v(*end))
    track.SetWidth(nm(width))
    track.SetLayer(layer)
    track.SetNet(net)
    board.Add(track)


def add_via(board, net, point, drill=0.3, diameter=0.6):
    via = pcbnew.PCB_VIA(board)
    via.SetPosition(v(*point))
    via.SetDrill(nm(drill))
    via.SetWidth(nm(diameter))
    via.SetLayerPair(F, B)
    via.SetNet(net)
    board.Add(via)


def route_path(board, net_name, points, width, layer=B, endpoint_vias=True, all_vias=False):
    net = find_net(board, net_name)
    if endpoint_vias or all_vias:
        via_points = points if all_vias else [points[0], points[-1]]
        for point in via_points:
            add_via(board, net, point)
    for start, end in zip(points, points[1:]):
        add_track(board, net, start, end, width, layer)


def route_tree(board, net_name, paths, width, layer=B):
    for path in paths:
        route_path(board, net_name, path, width, layer=layer, endpoint_vias=True)


def add_gnd_vias(board):
    net = find_net(board, "GND")
    points = [
        (12.225, 57.000), (21.000, 70.450), (21.500, 44.950), (26.500, 44.775),
        (21.000, 75.475), (42.000, 65.975), (48.000, 65.975), (38.212, 55.000),
        (44.212, 55.000), (14.000, 71.500), (22.062, 77.050), (30.675, 81.500),
        (45.175, 81.500), (37.862, 78.950), (50.175, 78.000), (57.000, 56.000),
        (30.137, 70.450), (21.250, 22.740), (38.750, 22.740), (14.000, 80.800),
        (35.800, 87.645), (42.200, 87.645), (34.680, 88.220), (43.320, 88.220),
        (34.680, 92.400), (43.320, 92.400), (6.850, 51.375), (6.850, 56.625),
        (6.850, 61.375), (6.850, 66.625)
    ]
    for point in points:
        if point[1] > 21.25:
            add_via(board, net, point, drill=0.3, diameter=0.65)


def add_stitching_vias(board):
    net = find_net(board, "GND")
    points = [
        (10, 30), (50, 30), (10, 50), (50, 50), (10, 75), (50, 75),
        (31, 73), (39, 81), (45, 84), (20, 80)
    ]
    for point in points:
        add_via(board, net, point, drill=0.3, diameter=0.65)


def add_zone(board, net_name, layer, name):
    net = find_net(board, net_name)
    zone = pcbnew.ZONE(board)
    zone.SetNet(net)
    zone.SetNetCode(net.GetNetCode())
    zone.SetLayer(layer)
    zone.SetZoneName(name)
    zone.SetMinThickness(nm(0.254))
    zone.SetLocalClearance(nm(0.2))
    zone.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL)
    zone.SetThermalReliefGap(nm(0.508))
    zone.SetThermalReliefSpokeWidth(nm(0.508))
    polygon = pcbnew.SHAPE_LINE_CHAIN()
    for point in [(0.5, 94.5), (59.5, 94.5), (59.5, 21.5), (0.5, 21.5)]:
        polygon.Append(v(*point))
    polygon.SetClosed(True)
    zone.AddPolygon(polygon)
    board.Add(zone)


def main():
    board_path = Path(sys.argv[1])
    board = pcbnew.LoadBoard(str(board_path))

    # Stage 1 - 5 V input/protected path.
    route_path(board, "/+5V_IN", [(14.000, 86.800), (13.600, 86.800), (13.600, 77.500)], 0.75, B)
    route_path(board, "/+5V_FUSED", [(16.400, 77.500), (23.938, 78.000)], 0.75, B)
    route_tree(board, "/+5V_PROTECTED", [
        [(22.062, 78.950), (21.000, 78.950), (21.000, 72.525), (21.000, 68.550)],
        [(14.000, 67.500), (21.000, 67.500), (21.000, 68.550)],
        [(21.000, 68.550), (27.863, 68.550), (27.863, 69.500)],
        [(27.863, 69.500), (27.863, 70.450)],
        [(21.000, 68.550), (57.000, 68.550), (57.000, 40.000)]
    ], 0.75, B)

    # Stage 2 - buck loop and local output.
    route_tree(board, "/BUCK_SW", [
        [(30.137, 69.500), (35.525, 69.500)],
        [(30.137, 69.500), (30.137, 64.500), (26.225, 64.500)]
    ], 0.50, F)
    route_path(board, "/BUCK_BST", [(30.137, 68.550), (27.775, 68.550), (27.775, 64.500)], 0.25, F, endpoint_vias=False)
    route_tree(board, "+3V3", [
        [(27.863, 68.550), (38.475, 68.550), (38.475, 69.500)],
        [(38.475, 69.500), (38.475, 63.025), (42.000, 63.025), (48.000, 63.025), (57.000, 63.025), (57.000, 48.000)],
        [(39.825, 58.000), (39.825, 63.025), (42.000, 63.025)],
        [(21.250, 24.010), (21.250, 43.050), (21.500, 43.050), (26.500, 43.225)],
        [(21.500, 43.050), (13.825, 43.050), (13.825, 53.000), (13.825, 64.000), (38.475, 64.000), (38.475, 63.025)]
    ], 0.50, B)

    # Stage 3 - USB-C, ESD, series resistors, and shield policy net.
    route_tree(board, "/DM_C", [
        [(39.250, 87.645), (38.250, 87.645), (37.862, 78.000)],
        [(37.862, 78.000), (32.175, 75.000)]
    ], 0.25, B)
    route_tree(board, "/DP_C", [
        [(38.750, 87.645), (39.750, 87.645), (37.862, 77.050)],
        [(37.862, 77.050), (44.175, 75.000)]
    ], 0.25, B)
    route_tree(board, "/DM_E", [
        [(33.825, 75.000), (33.825, 50.000), (21.250, 50.000), (21.250, 37.980)],
        [(33.825, 75.000), (57.000, 75.000), (57.000, 72.000)]
    ], 0.25, B)
    route_tree(board, "/DP_E", [
        [(45.825, 75.000), (45.825, 51.500), (21.250, 51.500), (21.250, 39.250)],
        [(45.825, 75.000), (57.000, 75.000), (57.000, 68.000)]
    ], 0.25, B)
    route_path(board, "/CC1", [(37.750, 87.645), (32.325, 81.500)], 0.25, B)
    route_path(board, "/CC2", [(40.750, 87.645), (46.825, 81.500)], 0.25, B)
    route_tree(board, "/SHIELD", [
        [(34.680, 88.220), (34.680, 92.400), (43.320, 92.400), (43.320, 88.220)],
        [(43.320, 88.220), (51.825, 78.000)]
    ], 0.25, B)

    # Join USB-C VBUS pads that are intentionally not connected to the power tree.
    route_tree(board, "unconnected-(J2-VBUS-PadA4)", [
        [(36.600, 87.645), (41.400, 87.645)],
        [(36.600, 87.645), (36.600, 86.800), (41.400, 86.800), (41.400, 87.645)]
    ], 0.20, B)

    # Stage 4 - low speed, debug, LEDs, and test pads.
    route_tree(board, "/ESP_EN", [
        [(21.250, 25.280), (21.250, 53.000), (12.175, 53.000)],
        [(12.175, 53.000), (13.775, 57.000)],
        [(12.175, 53.000), (5.150, 53.000), (5.150, 51.375)],
        [(5.150, 51.375), (5.150, 56.625)],
        [(21.250, 25.280), (57.000, 25.280), (57.000, 44.000)]
    ], 0.20, B)
    route_tree(board, "/BOOT0", [
        [(38.750, 39.250), (38.750, 64.000), (12.175, 64.000)],
        [(12.175, 64.000), (5.150, 64.000), (5.150, 61.375)],
        [(5.150, 61.375), (5.150, 66.625)],
        [(38.750, 39.250), (57.000, 39.250), (57.000, 52.000)]
    ], 0.20, B)
    route_path(board, "/PLED", [(38.175, 58.000), (39.788, 55.000)], 0.20, B)
    route_path(board, "/SLED", [(44.175, 58.000), (45.788, 55.000)], 0.20, B)
    route_path(board, "/STATUS_LED", [(38.750, 25.280), (45.825, 25.280), (45.825, 58.000)], 0.20, B)
    route_path(board, "/U0RXD", [(38.750, 27.820), (57.000, 27.820), (57.000, 64.000)], 0.20, B)
    route_path(board, "/U0TXD", [(38.750, 26.550), (55.000, 26.550), (55.000, 60.000), (57.000, 60.000)], 0.20, B)

    # Ground connections and zones.
    add_gnd_vias(board)
    add_stitching_vias(board)
    add_zone(board, "GND", B, "GND_B_Cu_first_pass")
    add_zone(board, "GND", F, "GND_F_Cu_first_pass")

    filler = pcbnew.ZONE_FILLER(board)
    filler.Fill(board.Zones())
    pcbnew.SaveBoard(str(board_path), board)


if __name__ == "__main__":
    main()
