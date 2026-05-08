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


SUMMARY_NETS = ["/BOOT0", "/ESP_EN", "/DP_C", "/DP_E", "/DM_C", "/DM_E"]


def mm(nm_value):
    return round(pcbnew.ToMM(nm_value), 3)


def layer_name(layer_id):
    return {
        pcbnew.F_Cu: "F.Cu",
        pcbnew.B_Cu: "B.Cu",
    }.get(layer_id, str(layer_id))


def iter_tracks(board):
    for item in board.GetTracks():
        yield item


def collect_net_geometry(board, net_name):
    segments = []
    vias = []
    for item in iter_tracks(board):
        if item.GetNetname() != net_name:
            continue
        if isinstance(item, pcbnew.PCB_VIA):
            pos = item.GetPosition()
            vias.append({"x": mm(pos.x), "y": mm(pos.y), "drill_mm": mm(item.GetDrillValue())})
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
        "segments": segments,
        "vias": vias,
    }


def collect_summary(board):
    return {net_name: collect_net_geometry(board, net_name) for net_name in SUMMARY_NETS}


def ensure_control_net_preconditions(board):
    blockers = []
    for net_name in ("/BOOT0", "/ESP_EN"):
        if collect_net_geometry(board, net_name)["segment_count"] == 0:
            blockers.append(net_name)
    if blockers:
        raise SystemExit(
            "BATCH_05_BLOCKED_PRECONDITION_NOT_MET: "
            + ", ".join(blockers)
            + " still unrouted; resolve control nets before USB D+/D- routing."
        )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("board_path")
    parser.add_argument("mode", choices=["summary", "apply"])
    args = parser.parse_args()

    board = pcbnew.LoadBoard(str(Path(args.board_path)))

    if args.mode == "summary":
        print(json.dumps({"summary": collect_summary(board)}, indent=2))
        return

    ensure_control_net_preconditions(board)
    raise SystemExit(
        "BATCH_05_ROUTE_GEOMETRY_NOT_IMPLEMENTED: precondition passed, but no copied-board-proven USB data route has been authored yet."
    )


if __name__ == "__main__":
    main()
