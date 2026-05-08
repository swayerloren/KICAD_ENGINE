#!/usr/bin/env python3
"""Extract read-only KiCad board outline, zones, and keepouts from a .kicad_pcb file."""

from __future__ import annotations

import argparse
from pathlib import Path

from _kicad_pcb_bridge_common import dump_json, dump_markdown, ensure_parent, parse_common_args, require_pcbnew_for_cli
from _kicad_pcb_bridge_extract import build_routing_schema
from _routing_common import make_markdown, markdown_table


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parse_common_args(parser)
    args = parser.parse_args()

    pcbnew = require_pcbnew_for_cli()
    board_path = Path(args.pcb_file).resolve()
    board = pcbnew.LoadBoard(str(board_path))
    schema = build_routing_schema(board_path.stem, board_path, board, pcbnew)
    result = {
        "schema_version": "1.0",
        "tool": "extract_kicad_zones_keepouts",
        "status": "PASS",
        "project": schema["project"],
        "board_path": schema["board_path"],
        "summary": {
            "edge_cut_count": len(schema["edge_cuts"]),
            "zone_count": len(schema["zones"]),
            "keepout_count": len(schema["keepouts"]),
        },
        "board_outline": schema["board_outline"],
        "edge_cuts": schema["edge_cuts"],
        "zones": schema["zones"],
        "keepouts": schema["keepouts"],
        "not_extracted": schema["not_extracted"],
    }
    ensure_parent(args.output_json)
    dump_json(args.output_json, result)

    if args.markdown:
        ensure_parent(args.markdown)
        rows = [[item["name"], item["type"], item["layer"]] for item in schema["keepouts"]]
        text = make_markdown(
            "KiCad Zones And Keepouts Extraction",
            {"project": schema["project"], "status": "PASS"},
            [
                ("Keepouts", markdown_table(["name", "type", "layer"], rows)),
                ("Not Extracted", "\n".join(f"- {item}" for item in schema["not_extracted"]) if schema["not_extracted"] else "_none_"),
            ],
        )
        dump_markdown(args.markdown, text)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
