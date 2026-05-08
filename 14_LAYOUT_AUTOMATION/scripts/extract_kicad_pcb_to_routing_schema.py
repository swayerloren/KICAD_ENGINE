#!/usr/bin/env python3
"""Extract a read-only .kicad_pcb into the routing-engine input schema JSON."""

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
    ensure_parent(args.output_json)
    dump_json(args.output_json, schema)

    if args.markdown:
        ensure_parent(args.markdown)
        net_rows = [[item["name"], item["role"], item["net_class"], item["routing_status"]] for item in schema["nets"][:40]]
        text = make_markdown(
            "KiCad PCB To Routing Schema",
            {
                "project": schema["project"],
                "components": len(schema["components"]),
                "pads": len(schema["pads"]),
                "nets": len(schema["nets"]),
                "tracks": len(schema["tracks"]),
                "vias": len(schema["vias"]),
                "zones": len(schema["zones"]),
                "keepouts": len(schema["keepouts"]),
            },
            [
                ("Net Sample", markdown_table(["net", "role", "net_class", "routing_status"], net_rows)),
                ("Not Extracted", "\n".join(f"- {item}" for item in schema["not_extracted"]) if schema["not_extracted"] else "_none_"),
            ],
        )
        dump_markdown(args.markdown, text)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
