#!/usr/bin/env python3
"""Render a simple SVG preview for one placement variant."""

from __future__ import annotations

import argparse

from _prelayout_common import dump_markdown, load_json


def render_svg(variant: dict, view: str = "top") -> str:
    board = variant["board_profile"]
    width = float(board["board_width_mm"])
    height = float(board["board_height_mm"])
    is_bottom = str(view).lower() == "bottom"
    scale = 6.0
    margin = 24.0
    svg_width = width * scale + margin * 2
    svg_height = height * scale + margin * 2

    def sx(x: float) -> float:
        x_mm = width - x if is_bottom else x
        return round(margin + x_mm * scale, 3)

    def sy(y: float) -> float:
        return round(margin + y * scale, 3)

    pieces = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}">',
        '<rect width="100%" height="100%" fill="#fffdf7"/>',
        f'<rect x="{sx(0)}" y="{sy(0)}" width="{width * scale}" height="{height * scale}" fill="#fcfcfb" stroke="#1f2933" stroke-width="2"/>',
        f'<text x="{svg_width - margin}" y="{margin - 6}" font-size="11" text-anchor="end" fill="#334155">{view.title()} preview</text>',
    ]

    for component in variant.get("components", []):
        bbox = component.get("courtyard_bbox") or component.get("body_bbox")
        if not bbox:
            continue
        fill = "#d9e7ff" if component.get("fixed_mechanical") else "#dff5e1"
        pieces.append(
            f'<rect x="{sx(float(bbox["xmin"]))}" y="{sy(float(bbox["ymin"]))}" '
            f'width="{(float(bbox["xmax"]) - float(bbox["xmin"])) * scale}" '
            f'height="{(float(bbox["ymax"]) - float(bbox["ymin"])) * scale}" '
            f'fill="{fill}" stroke="#334e68" stroke-width="1"/>'
        )
        pieces.append(
            f'<text x="{sx(float(component["x_mm"]))}" y="{sy(float(component["y_mm"]))}" '
            'font-size="9" text-anchor="middle" fill="#102a43">'
            f'{component["ref"]}</text>'
        )
        keepout = component.get("antenna_keepout")
        if isinstance(keepout, dict) and isinstance(keepout.get("bbox"), dict):
            box = keepout["bbox"]
            pieces.append(
                f'<rect x="{sx(float(box["xmin"]))}" y="{sy(float(box["ymin"]))}" '
                f'width="{(float(box["xmax"]) - float(box["xmin"])) * scale}" '
                f'height="{(float(box["ymax"]) - float(box["ymin"])) * scale}" '
                'fill="rgba(255, 183, 77, 0.25)" stroke="#d97706" stroke-dasharray="4 3" stroke-width="1"/>'
            )

    truth_map = {item["ref"]: item for item in variant.get("connector_truths", [])}
    for component in variant.get("components", []):
        truth = truth_map.get(component["ref"])
        if not truth:
            continue
        color = {"PASS": "#0f766e", "FAIL": "#b91c1c", "UNKNOWN": "#92400e"}.get(truth["truth_status"], "#334155")
        x = sx(float(component["x_mm"]))
        y = sy(float(component["y_mm"]))
        delta = 16
        dx = 0
        dy = 0
        direction = truth["mating_direction"]
        if direction == "bottom":
            dy = delta
        elif direction == "top":
            dy = -delta
        elif direction == "left":
            dx = -delta
        else:
            dx = delta
        pieces.append(f'<line x1="{x}" y1="{y}" x2="{x + dx}" y2="{y + dy}" stroke="{color}" stroke-width="2"/>')

    for route in variant.get("projected_routes", []):
        color = {
            "PROJECTED_OK": "#15803d",
            "PROJECTED_WARNING_LONG_PATH": "#b45309",
            "BLOCKED_CONNECTOR_DIRECTION": "#b91c1c",
            "BLOCKED_RF_KEEPOUT": "#b91c1c",
            "BLOCKED_NO_CHANNEL": "#b91c1c",
            "OPEN_REQUIRED": "#b91c1c",
        }.get(route["status"], "#475569")
        for segment in route.get("segments", []):
            pieces.append(
                f'<line x1="{sx(float(segment["start"]["x_mm"]))}" y1="{sy(float(segment["start"]["y_mm"]))}" '
                f'x2="{sx(float(segment["end"]["x_mm"]))}" y2="{sy(float(segment["end"]["y_mm"]))}" '
                f'stroke="{color}" stroke-width="1.6"/>'
            )

    pieces.append("</svg>")
    return "\n".join(pieces)


def preview_markdown(variant: dict, svg_path: str, view: str) -> str:
    return "\n".join(
        [
            f"# {variant['variant_id']} Preview",
            "",
            f"Strategy: `{variant['strategy_id']}`",
            f"View: `{view}`",
            f"Projected open nets: `{variant['projected_open_nets_count']}`",
            f"SVG: `{svg_path}`",
            "",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("variant_json", help="Input variant JSON file.")
    parser.add_argument("output_svg", help="Output SVG preview path.")
    parser.add_argument("--markdown", help="Optional Markdown sidecar path.")
    parser.add_argument("--view", choices=("top", "bottom"), default="top", help="Preview side to render.")
    args = parser.parse_args()

    variant = load_json(args.variant_json)
    svg = render_svg(variant, args.view)
    with open(args.output_svg, "w", encoding="utf-8") as handle:
        handle.write(svg + "\n")
    if args.markdown:
        dump_markdown(args.markdown, preview_markdown(variant, args.output_svg, args.view))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
