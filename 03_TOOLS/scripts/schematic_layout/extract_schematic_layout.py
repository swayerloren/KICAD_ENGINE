#!/usr/bin/env python3
"""Extract schematic block/layout metadata without editing the schematic."""

from __future__ import annotations

from pathlib import Path

from schematic_layout_common import (
    common_parser,
    layout_summary_markdown,
    load_layout_context,
    resolve_project_and_schematic,
    serializable_blocks,
    write_markdown_and_json,
)


def build_payload(schematic: Path) -> dict:
    context = load_layout_context(schematic)
    return {
        "generated_at": context["generated_at"],
        "schematic": context["schematic"],
        "template_id": context["template_id"],
        "diagram_bbox": context["diagram_bbox"],
        "symbol_count": len(context["symbols"]),
        "wire_count": len(context["wires"]),
        "label_count": sum(1 for item in context["text_items"] if item["kind"] in {"label", "global_label", "hierarchical_label"}),
        "blocks": serializable_blocks(context),
        "unassigned_symbols": [symbol.get("reference", "") for symbol in context["unassigned_symbols"]],
        "reference_metrics": context["reference_metrics"],
        "esp32_metrics": context["esp32_metrics"],
    }


def build_markdown(payload: dict) -> str:
    sections = [
        "## Summary",
        "",
        f"- Template: `{payload['template_id']}`",
        f"- Symbols: `{payload['symbol_count']}`",
        f"- Wires: `{payload['wire_count']}`",
        f"- Labels: `{payload['label_count']}`",
        f"- Unassigned symbols: `{len(payload['unassigned_symbols'])}`",
        "",
        "## Blocks",
        "",
        "| Block | Symbols | Region | Wires | Labels | Repeated labels |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for block_id, block in payload["blocks"].items():
        repeated = ", ".join(f"{name} x{count}" for name, count in block["stats"]["repeated_labels"].items()) or "-"
        sections.append(
            f"| {block['title']} | `{block['symbol_count']}` | `{block['region']['region']}` | `{block['stats']['wire_count']}` | `{block['stats']['label_count']}` | {repeated} |"
        )
    return layout_summary_markdown("Schematic Layout Extract", Path(payload["schematic"]), sections)


def main() -> int:
    parser = common_parser("Extract current schematic layout and block metadata.")
    args = parser.parse_args()
    _, schematic = resolve_project_and_schematic(args.project, args.schematic)
    payload = build_payload(schematic)
    markdown = build_markdown(payload)
    write_markdown_and_json(markdown, payload, Path(args.output) if args.output else None, Path(args.json_output) if args.json_output else None)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
