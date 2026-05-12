#!/usr/bin/env python3
"""Render a simple SVG overlay for flagged trace-geometry findings."""

from __future__ import annotations

import argparse
from pathlib import Path

from _pcb_geometry_common import load_payload, make_markdown, render_svg_overlay, write_svg
from _routing_common import dump_markdown  # type: ignore


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tracks_json", help="Input geometry JSON path")
    parser.add_argument("quality_json", help="Input aggregate quality JSON path")
    parser.add_argument("output_svg", help="Output SVG path")
    parser.add_argument("--markdown", help="Optional Markdown output path")
    args = parser.parse_args()

    payload = load_payload(args.tracks_json)
    quality = load_payload(args.quality_json)
    svg = render_svg_overlay(payload, quality)
    write_svg(args.output_svg, svg)

    if args.markdown:
        text = make_markdown(
            "Trace Quality Overlay",
            {
                "project": quality.get("project", ""),
                "status": quality.get("status", ""),
                "finding_count": quality.get("summary", {}).get("finding_count", 0),
                "overlay_svg": str(Path(args.output_svg).resolve()),
            },
            [],
        )
        dump_markdown(args.markdown, text)

    print("TRACE_OVERLAY_STATUS: PASS")
    print(f"TRACE_OVERLAY_OUTPUT_SVG: {Path(args.output_svg).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
