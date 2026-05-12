#!/usr/bin/env python3
"""Generate at least three placement variants from a board digital twin."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from _prelayout_common import (
    build_connector_truth,
    dump_json,
    dump_markdown,
    first_ref_by_role,
    get_component,
    load_json,
    refs_by_role,
    set_component,
)


VARIANT_DEFS = [
    {
        "variant_id": "VARIANT_A",
        "variant_name": "Compact dev-board",
        "strategy_id": "compact_dev_board",
        "risk_tags": ["compact_io_cluster", "short_power_path"],
        "notes": "A compact pill-style layout that keeps both edge connectors low, the power cluster tight, and test access on the right edge.",
    },
    {
        "variant_id": "VARIANT_B",
        "variant_name": "Routing-first",
        "strategy_id": "routing_first",
        "risk_tags": ["preferred_candidate", "channel_margin"],
        "notes": "This variant opens the bottom-edge corridor and gives USB, control, LED, and test-pad escape paths the most routing room.",
    },
    {
        "variant_id": "VARIANT_C",
        "variant_name": "Mechanical-safe",
        "strategy_id": "mechanical_safe",
        "risk_tags": ["connector_clearance_bias", "service_envelope_margin"],
        "notes": "This variant biases connector service-envelope clearance and hand-access margin, even if that makes some low-risk routing channels longer.",
    },
]


def apply_strategy(base_twin: dict[str, Any], variant_def: dict[str, Any]) -> dict[str, Any]:
    board_profile = base_twin["board_profile"]
    width = float(board_profile["board_width_mm"])
    height = float(board_profile["board_height_mm"])
    components = [dict(component) for component in base_twin["components"]]
    components = [component.copy() for component in components]

    usb_ref = first_ref_by_role(components, "USB_C") or "J2"
    barrel_ref = first_ref_by_role(components, "BARREL_JACK") or "J1"
    rf_ref = first_ref_by_role(components, "RF_MODULE") or "U2"
    regulator_ref = first_ref_by_role(components, "REGULATOR") or "U1"
    inductor_ref = first_ref_by_role(components, "INDUCTOR") or "L1"
    testpad_refs = refs_by_role(components, "TEST_PAD")[:3]

    set_component(components, usb_ref, 39.0, round(height - 3.75, 3), board_profile, 0.0)
    set_component(components, barrel_ref, 11.5, round(height - 6.0, 3), board_profile, 0.0)
    set_component(components, rf_ref, round(width / 2.0, 3), 28.0, board_profile, None)
    set_component(components, regulator_ref, 17.0, 56.0, board_profile, None)
    set_component(components, inductor_ref, 23.0, 56.0, board_profile, None)

    if len(testpad_refs) >= 3:
        base_y = 38.0
        for index, ref in enumerate(testpad_refs):
            set_component(components, ref, round(width - 3.0, 3), round(base_y + index * 5.0, 3), board_profile, 90.0)

    if variant_def["strategy_id"] == "routing_first":
        set_component(components, usb_ref, 42.0, round(height - 3.75, 3), board_profile, 0.0)
        set_component(components, barrel_ref, 10.5, round(height - 6.0, 3), board_profile, 0.0)
        set_component(components, rf_ref, round(width / 2.0, 3), 28.0, board_profile, None)
        set_component(components, regulator_ref, 18.0, 52.0, board_profile, None)
        set_component(components, inductor_ref, 25.0, 52.0, board_profile, None)
        if len(testpad_refs) >= 3:
            base_y = 32.0
            for index, ref in enumerate(testpad_refs):
                set_component(components, ref, round(width - 3.0, 3), round(base_y + index * 6.0, 3), board_profile, 90.0)
    elif variant_def["strategy_id"] == "mechanical_safe":
        set_component(components, usb_ref, 40.5, round(height - 4.5, 3), board_profile, 0.0)
        set_component(components, barrel_ref, 13.0, round(height - 7.5, 3), board_profile, 0.0)
        set_component(components, rf_ref, round(width / 2.0, 3), 29.0, board_profile, None)
        set_component(components, regulator_ref, 20.0, 60.0, board_profile, None)
        set_component(components, inductor_ref, 27.0, 60.0, board_profile, None)
        if len(testpad_refs) >= 3:
            base_y = 42.0
            for index, ref in enumerate(testpad_refs):
                set_component(components, ref, round(width - 8.0, 3), round(base_y + index * 6.0, 3), board_profile, 90.0)

    connector_truths = []
    for component in components:
        ref = str(component.get("ref", ""))
        intended_edge = component.get("edge_proximity", {}).get("edge")
        if ref == usb_ref:
            intended_edge = "bottom"
        if ref == barrel_ref:
            intended_edge = "bottom"
        if ref.startswith("J"):
            connector_truths.append(build_connector_truth(component, board_profile, intended_edge))

    return {
        "schema_version": "1.0",
        "project": base_twin["project"],
        "variant_id": variant_def["variant_id"],
        "variant_name": variant_def["variant_name"],
        "strategy_id": variant_def["strategy_id"],
        "board_profile": board_profile,
        "components": components,
        "connector_truths": connector_truths,
        "projected_routes": [],
        "projected_open_nets_count": 0,
        "notes": variant_def["notes"],
        "risk_tags": list(variant_def["risk_tags"]),
    }


def generate_placement_variants(twin: dict[str, Any]) -> list[dict[str, Any]]:
    return [apply_strategy(twin, variant_def) for variant_def in VARIANT_DEFS]


def variants_markdown(variants: list[dict[str, Any]]) -> str:
    lines = [
        "# Placement Variants",
        "",
        "| Variant | Strategy | Notes |",
        "| --- | --- | --- |",
    ]
    for variant in variants:
        lines.append(
            f"| `{variant['variant_id']}` | `{variant['strategy_id']}` | {variant['notes']} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("digital_twin_json", help="Input digital twin JSON file.")
    parser.add_argument("output_dir", help="Output directory for per-variant JSON.")
    parser.add_argument("--markdown", help="Optional Markdown summary path.")
    args = parser.parse_args()

    twin = load_json(args.digital_twin_json)
    variants = generate_placement_variants(twin)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    for variant in variants:
        path = output_dir / f"{variant['variant_id'].lower()}.json"
        dump_json(path, variant)
    if args.markdown:
        dump_markdown(args.markdown, variants_markdown(variants))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
