#!/usr/bin/env python3
"""Audit USB-C mechanical orientation truth from a live or copied KiCad PCB."""

from __future__ import annotations

import argparse

from _mechanical_orientation_common import (
    audit_connector_state,
    build_live_placement_state,
    connector_markdown,
    dump_json,
    dump_markdown,
    load_truth_catalog,
    locate_pcb,
    repo_rel,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, help="Active project path or .kicad_pcb path.")
    parser.add_argument("--output-json", help="Optional JSON output path.")
    parser.add_argument("--markdown", help="Optional Markdown output path.")
    parser.add_argument("--fail-on-non-pass", action="store_true", help="Return non-zero when status is not PASS.")
    args = parser.parse_args()

    pcb_path = locate_pcb(args.project)
    state = build_live_placement_state(pcb_path)
    catalog = load_truth_catalog()
    result = audit_connector_state(state, catalog, family_filter="USB_C")
    if args.output_json:
        dump_json(args.output_json, result)
    if args.markdown:
        dump_markdown(args.markdown, connector_markdown(result))
    print(f"USB_C_AUDIT_STATUS: {result['status']}")
    print(f"USB_C_ROUTING_BLOCKED: {result['routing_blocked']}")
    print(f"USB_C_SOURCE_PCB: {repo_rel(pcb_path)}")
    print(f"USB_C_COUNT: {len(result['records'])}")
    if args.fail_on_non_pass and result["status"] != "PASS":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
