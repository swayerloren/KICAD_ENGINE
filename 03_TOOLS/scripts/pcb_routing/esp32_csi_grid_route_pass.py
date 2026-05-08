import heapq
import math
import sys
from pathlib import Path

import pcbnew


GRID = 0.25
F = pcbnew.F_Cu
B = pcbnew.B_Cu
LAYER_NAMES = {F: "F.Cu", B: "B.Cu"}


def nm(mm):
    return pcbnew.FromMM(mm)


def mm(nm_value):
    return pcbnew.ToMM(nm_value)


def v(x, y):
    return pcbnew.VECTOR2I(nm(x), nm(y))


def grid_point(point):
    return (round(point[0] / GRID), round(point[1] / GRID))


def real_point(node):
    return (node[0] * GRID, node[1] * GRID)


def dist_point_segment(px, py, ax, ay, bx, by):
    dx = bx - ax
    dy = by - ay
    if dx == 0 and dy == 0:
        return math.hypot(px - ax, py - ay)
    t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
    cx = ax + t * dx
    cy = ay + t * dy
    return math.hypot(px - cx, py - cy)


class Router:
    def __init__(self, board):
        self.board = board
        self.static_pads = []
        self.dynamic_tracks = []
        self.dynamic_vias = []
        self.rf_keepout = (6.0, 0.25, 54.0, 21.25)
        self.min_x = int(round(0.75 / GRID))
        self.max_x = int(round(59.25 / GRID))
        self.min_y = int(round(21.50 / GRID))
        self.max_y = int(round(94.25 / GRID))
        self._load_pads()

    def _load_pads(self):
        for fp in self.board.GetFootprints():
            for pad in fp.Pads():
                box = pad.GetBoundingBox()
                net = pad.GetNetname()
                layers = []
                layer_set = pad.GetLayerSet()
                if layer_set.Contains(F):
                    layers.append(F)
                if layer_set.Contains(B):
                    layers.append(B)
                if not layers:
                    layers = [F, B]
                x1, y1 = mm(box.GetX()), mm(box.GetY())
                x2, y2 = mm(box.GetRight()), mm(box.GetBottom())
                self.static_pads.append((net, layers, x1, y1, x2, y2))

    def net(self, name):
        net = self.board.FindNet(name)
        if net is None:
            raise RuntimeError(f"missing net {name}")
        return net

    def _blocked_grid(self, net_name, width, forced_open):
        blocked = {F: set(), B: set()}
        clearance = 0.20 + width / 2

        def mark_rect(layer, x1, y1, x2, y2, inflate):
            gx1 = math.floor((x1 - inflate) / GRID)
            gx2 = math.ceil((x2 + inflate) / GRID)
            gy1 = math.floor((y1 - inflate) / GRID)
            gy2 = math.ceil((y2 + inflate) / GRID)
            for gx in range(gx1, gx2 + 1):
                if gx < self.min_x or gx > self.max_x:
                    continue
                for gy in range(gy1, gy2 + 1):
                    if gy < self.min_y or gy > self.max_y:
                        continue
                    blocked[layer].add((gx, gy))

        for layer in (F, B):
            x1, y1, x2, y2 = self.rf_keepout
            mark_rect(layer, x1, y1, x2, y2, 0.0)

        for pad_net, layers, x1, y1, x2, y2 in self.static_pads:
            if pad_net == net_name:
                continue
            for layer in layers:
                mark_rect(layer, x1, y1, x2, y2, clearance)

        for tr_net, layer, start, end, tr_width in self.dynamic_tracks:
            if tr_net == net_name:
                continue
            ax, ay = start
            bx, by = end
            inflate = clearance + tr_width / 2
            gx1 = math.floor((min(ax, bx) - inflate) / GRID)
            gx2 = math.ceil((max(ax, bx) + inflate) / GRID)
            gy1 = math.floor((min(ay, by) - inflate) / GRID)
            gy2 = math.ceil((max(ay, by) + inflate) / GRID)
            for gx in range(gx1, gx2 + 1):
                if gx < self.min_x or gx > self.max_x:
                    continue
                for gy in range(gy1, gy2 + 1):
                    if gy < self.min_y or gy > self.max_y:
                        continue
                    px, py = real_point((gx, gy))
                    if dist_point_segment(px, py, ax, ay, bx, by) <= inflate:
                        blocked[layer].add((gx, gy))

        for via_net, point, diameter in self.dynamic_vias:
            if via_net == net_name:
                continue
            inflate = clearance + diameter / 2
            px, py = point
            for layer in (F, B):
                mark_rect(layer, px, py, px, py, inflate)

        for layer, point in forced_open:
            gx, gy = grid_point(point)
            for dx in range(-2, 3):
                for dy in range(-2, 3):
                    blocked[layer].discard((gx + dx, gy + dy))
        return blocked

    def _is_inside(self, gx, gy):
        return self.min_x <= gx <= self.max_x and self.min_y <= gy <= self.max_y

    def route_pair(self, net_name, start, end, width, allowed_layers=(F, B), via_allowed=True):
        forced = [(layer, start) for layer in allowed_layers] + [(layer, end) for layer in allowed_layers]
        blocked = self._blocked_grid(net_name, width, forced)
        starts = [(grid_point(start)[0], grid_point(start)[1], layer) for layer in allowed_layers]
        goals = {(grid_point(end)[0], grid_point(end)[1], layer) for layer in allowed_layers}

        def heuristic(state):
            gx, gy, _layer = state
            ex, ey, _ = next(iter(goals))
            return math.hypot(gx - ex, gy - ey)

        heap = []
        came = {}
        cost = {}
        for s in starts:
            if s[:2] in blocked[s[2]]:
                continue
            cost[s] = 0.0
            heapq.heappush(heap, (heuristic(s), 0.0, s))

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        found = None
        while heap:
            _prio, cur_cost, state = heapq.heappop(heap)
            if cur_cost != cost.get(state):
                continue
            if state in goals:
                found = state
                break
            gx, gy, layer = state
            for dx, dy in moves:
                nx, ny = gx + dx, gy + dy
                if not self._is_inside(nx, ny) or (nx, ny) in blocked[layer]:
                    continue
                step = math.hypot(dx, dy)
                nxt = (nx, ny, layer)
                ncost = cur_cost + step
                if ncost < cost.get(nxt, 1e18):
                    cost[nxt] = ncost
                    came[nxt] = state
                    heapq.heappush(heap, (ncost + heuristic(nxt), ncost, nxt))
            if via_allowed and len(allowed_layers) > 1:
                other = B if layer == F else F
                if other in allowed_layers and (gx, gy) not in blocked[other]:
                    nxt = (gx, gy, other)
                    ncost = cur_cost + 16.0
                    if ncost < cost.get(nxt, 1e18):
                        cost[nxt] = ncost
                        came[nxt] = state
                        heapq.heappush(heap, (ncost + heuristic(nxt), ncost, nxt))

        if found is None:
            raise RuntimeError(f"route failed: {net_name} {start} -> {end}")

        path = [found]
        while path[-1] not in starts:
            path.append(came[path[-1]])
        path.reverse()
        self._commit_path(net_name, path, width)
        for point, state in [(start, path[0]), (end, path[-1])]:
            if state[2] == B and self._endpoint_needs_b_via(net_name, point):
                net = self.net(net_name)
                add_via(self.board, net, point)
                self.dynamic_vias.append((net_name, point, 0.6))

    def _endpoint_needs_b_via(self, net_name, point):
        px, py = point
        found_same_net_pad = False
        pad_has_b = False
        for pad_net, layers, x1, y1, x2, y2 in self.static_pads:
            if pad_net != net_name:
                continue
            if (x1 - 0.05) <= px <= (x2 + 0.05) and (y1 - 0.05) <= py <= (y2 + 0.05):
                found_same_net_pad = True
                if B in layers:
                    pad_has_b = True
        return found_same_net_pad and not pad_has_b

    def _commit_path(self, net_name, path, width):
        net = self.net(net_name)
        current_layer = path[0][2]
        segment_points = [(path[0][0], path[0][1])]
        last_dir = None

        def flush(points, layer):
            if len(points) < 2:
                return
            simplified = [points[0]]
            direction = None
            for a, b in zip(points, points[1:]):
                d = (b[0] - a[0], b[1] - a[1])
                d = (0 if d[0] == 0 else int(d[0] / abs(d[0])), 0 if d[1] == 0 else int(d[1] / abs(d[1])))
                if direction is None:
                    direction = d
                elif d != direction:
                    simplified.append(a)
                    direction = d
            simplified.append(points[-1])
            for a, b in zip(simplified, simplified[1:]):
                start = real_point(a)
                end = real_point(b)
                add_track(self.board, net, start, end, width, layer)
                self.dynamic_tracks.append((net_name, layer, start, end, width))

        for prev, cur in zip(path, path[1:]):
            if cur[2] != current_layer:
                flush(segment_points, current_layer)
                point = real_point((prev[0], prev[1]))
                add_via(self.board, net, point)
                self.dynamic_vias.append((net_name, point, 0.6))
                current_layer = cur[2]
                segment_points = [(cur[0], cur[1])]
                last_dir = None
                continue
            d = (cur[0] - prev[0], cur[1] - prev[1])
            d = (0 if d[0] == 0 else int(d[0] / abs(d[0])), 0 if d[1] == 0 else int(d[1] / abs(d[1])))
            if last_dir is not None and d != last_dir:
                segment_points.append((prev[0], prev[1]))
            segment_points.append((cur[0], cur[1]))
            last_dir = d
        flush(segment_points, current_layer)

    def add_zones(self):
        add_zone(self.board, self.net("GND"), B, "GND_B_Cu_first_pass")
        add_zone(self.board, self.net("GND"), F, "GND_F_Cu_first_pass")
        for point in [(10, 30), (50, 30), (10, 50), (50, 50), (10, 75), (50, 75), (31, 73), (39, 81), (45, 84), (20, 80)]:
            add_via(self.board, self.net("GND"), point, drill=0.3, diameter=0.65)
        filler = pcbnew.ZONE_FILLER(self.board)
        filler.Fill(self.board.Zones())


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


def add_zone(board, net, layer, name):
    zone = pcbnew.ZONE(board)
    zone.SetNet(net)
    zone.SetNetCode(net.GetNetCode())
    zone.SetLayer(layer)
    layer_set = pcbnew.LSET()
    layer_set.AddLayer(layer)
    zone.SetLayerSet(layer_set)
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
    r = Router(board)

    routes = [
        # Stage 1 power input
        ("/+5V_IN", (14.0, 86.8), (13.6, 77.5), 0.75, (B,)),
        ("/+5V_FUSED", (16.4, 77.5), (23.938, 78.0), 0.75, (B,)),
        ("/+5V_PROTECTED", (22.062, 78.95), (21.0, 72.525), 0.75, (B,)),
        ("/+5V_PROTECTED", (21.0, 72.525), (21.0, 68.55), 0.75, (B,)),
        ("/+5V_PROTECTED", (21.0, 68.55), (14.0, 67.5), 0.75, (B,)),
        ("/+5V_PROTECTED", (21.0, 68.55), (27.863, 69.5), 0.75, (B,)),
        ("/+5V_PROTECTED", (27.863, 69.5), (27.863, 70.45), 0.75, (B,)),
        ("/+5V_PROTECTED", (27.863, 69.5), (57.0, 40.0), 0.5, (B,)),
        # Stage 2 buck
        ("/BUCK_SW", (30.137, 69.5), (35.525, 69.5), 0.45, (F,)),
        ("/BUCK_SW", (30.137, 69.5), (26.225, 64.5), 0.30, (F,)),
        ("/BUCK_BST", (30.137, 68.55), (27.775, 64.5), 0.20, (F,)),
        ("+3V3", (27.863, 68.55), (38.475, 69.5), 0.50, (B,)),
        ("+3V3", (38.475, 69.5), (42.0, 63.025), 0.50, (B,)),
        ("+3V3", (42.0, 63.025), (48.0, 63.025), 0.50, (B,)),
        ("+3V3", (48.0, 63.025), (57.0, 48.0), 0.45, (B,)),
        ("+3V3", (42.0, 63.025), (39.825, 58.0), 0.35, (B,)),
        ("+3V3", (21.25, 24.01), (21.5, 43.05), 0.35, (B,)),
        ("+3V3", (21.5, 43.05), (26.5, 43.225), 0.35, (B,)),
        ("+3V3", (21.5, 43.05), (13.825, 53.0), 0.35, (B,)),
        ("+3V3", (13.825, 53.0), (13.825, 64.0), 0.35, (B,)),
        ("+3V3", (13.825, 64.0), (42.0, 63.025), 0.35, (B,)),
        # Stage 3 USB
        ("/DM_C", (39.25, 87.645), (38.25, 87.645), 0.15, (F,)),
        ("/DM_C", (38.25, 87.645), (37.862, 78.0), 0.15, (F,)),
        ("/DM_C", (37.862, 78.0), (32.175, 75.0), 0.20, (F,)),
        ("/DP_C", (38.75, 87.645), (39.75, 87.645), 0.15, (F,)),
        ("/DP_C", (38.75, 87.645), (37.862, 77.05), 0.15, (F,)),
        ("/DP_C", (37.862, 77.05), (44.175, 75.0), 0.20, (F,)),
        ("/DM_E", (33.825, 75.0), (21.25, 37.98), 0.20, (B,)),
        ("/DM_E", (33.825, 75.0), (57.0, 72.0), 0.20, (B,)),
        ("/DP_E", (45.825, 75.0), (21.25, 39.25), 0.20, (B,)),
        ("/DP_E", (45.825, 75.0), (57.0, 68.0), 0.20, (B,)),
        ("/CC1", (37.75, 87.645), (32.325, 81.5), 0.20, (F,)),
        ("/CC2", (40.75, 87.645), (46.825, 81.5), 0.20, (F,)),
        ("/SHIELD", (34.68, 88.22), (34.68, 92.4), 0.25, (B,)),
        ("/SHIELD", (34.68, 92.4), (43.32, 92.4), 0.25, (B,)),
        ("/SHIELD", (43.32, 92.4), (43.32, 88.22), 0.25, (B,)),
        ("/SHIELD", (43.32, 88.22), (51.825, 78.0), 0.20, (B,)),
        ("unconnected-(J2-VBUS-PadA4)", (36.6, 87.645), (41.4, 87.645), 0.15, (F,)),
        ("unconnected-(J2-VBUS-PadA4)", (36.6, 87.645), (36.6, 86.85), 0.15, (F,)),
        ("unconnected-(J2-VBUS-PadA4)", (41.4, 87.645), (41.4, 86.85), 0.15, (F,)),
        # Stage 4 low speed/control
        ("/ESP_EN", (21.25, 25.28), (12.175, 53.0), 0.18, (B,)),
        ("/ESP_EN", (12.175, 53.0), (13.775, 57.0), 0.18, (B,)),
        ("/ESP_EN", (12.175, 53.0), (5.15, 51.375), 0.18, (B,)),
        ("/ESP_EN", (5.15, 51.375), (5.15, 56.625), 0.18, (B,)),
        ("/ESP_EN", (21.25, 25.28), (57.0, 44.0), 0.18, (B,)),
        ("/BOOT0", (38.75, 39.25), (12.175, 64.0), 0.18, (B,)),
        ("/BOOT0", (12.175, 64.0), (5.15, 61.375), 0.18, (B,)),
        ("/BOOT0", (5.15, 61.375), (5.15, 66.625), 0.18, (B,)),
        ("/BOOT0", (38.75, 39.25), (57.0, 52.0), 0.18, (B,)),
        ("/PLED", (38.175, 58.0), (39.788, 55.0), 0.18, (F,)),
        ("/SLED", (44.175, 58.0), (45.788, 55.0), 0.18, (F,)),
        ("/STATUS_LED", (38.75, 25.28), (45.825, 58.0), 0.18, (B,)),
        ("/U0RXD", (38.75, 27.82), (57.0, 64.0), 0.18, (B,)),
        ("/U0TXD", (38.75, 26.55), (57.0, 60.0), 0.18, (B,)),
    ]

    routed = []
    failed = []
    for net, start, end, width, layers in routes:
        try:
            r.route_pair(net, start, end, width, allowed_layers=layers, via_allowed=len(layers) > 1)
            routed.append((net, start, end))
        except Exception as exc:
            failed.append((net, start, end, str(exc)))
            print(f"ROUTE_FAIL {net} {start}->{end}: {exc}")

    r.add_zones()
    pcbnew.SaveBoard(str(board_path), board)
    print(f"ROUTED={len(routed)} FAILED={len(failed)}")
    if failed:
        for item in failed:
            print("FAILED_DETAIL", item)


if __name__ == "__main__":
    main()
