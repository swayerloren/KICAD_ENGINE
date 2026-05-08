#!/usr/bin/env python3
"""Generate a schema-aware routing priority plan from a routing fixture JSON."""

from __future__ import annotations

import argparse

from _routing_common import (
    critical_net_names,
    dump_json,
    dump_markdown,
    make_markdown,
    markdown_table,
    normalized_nets,
    parse_args_markdown,
    payload_errors,
    payload_warnings,
    power_net_names,
    regulator_loop_present,
    usb_pair_names,
    load_json,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_json")
    parser.add_argument("output_json")
    parse_args_markdown(parser)
    args = parser.parse_args()

    payload = load_json(args.input_json)
    errors = payload_errors(payload)
    warnings = payload_warnings(payload)
    routing_order = normalized_nets(payload)

    hard_fails: list[str] = []
    if not payload.get("ground_strategy", {}).get("present", False):
        hard_fails.append("GND strategy missing")
    if not regulator_loop_present(payload):
        hard_fails.append("regulator critical loop not planned")
    usb_names = usb_pair_names(payload)
    if ("USB_D+" in usb_names) ^ ("USB_D-" in usb_names):
        hard_fails.append("USB D+/D- incomplete")

    status = "PASS"
    if errors:
        status = "AUTO_BLOCKED_MISSING_DATA"
    elif hard_fails:
        status = "AUTO_BLOCKED_BAD_LAYOUT"

    result = {
        "schema_version": "1.0",
        "tool": "generate_routing_plan",
        "project": payload.get("project", ""),
        "status": status,
        "summary": {
            "net_count": len(routing_order),
            "critical_net_count": len(critical_net_names(payload)),
            "power_net_count": len(power_net_names(payload)),
            "usb_net_count": len(usb_names),
        },
        "routing_order": routing_order,
        "critical_net_names": sorted(critical_net_names(payload)),
        "power_net_names": sorted(power_net_names(payload)),
        "usb_net_names": sorted(usb_names),
        "rf_keepout_risk_nets": sorted({item["name"] for item in routing_order if item["must_avoid_keepouts"]}),
        "antenna_keepout_risk_nets": sorted({item["name"] for item in routing_order if item["must_avoid_keepouts"]}),
        "errors": errors,
        "warnings": warnings,
        "hard_fails": hard_fails,
        "autorouting_policy": "REVIEW_ONLY",
    }
    dump_json(args.output_json, result)

    if args.markdown:
        rows = [
            [
                item["name"],
                item["stage_name"],
                item["routing_priority"],
                item["critical"],
                item["power"],
                item["usb"],
                item["routing_status"],
            ]
            for item in routing_order
        ]
        text = make_markdown(
            "Routing Plan",
            {
                "project": payload.get("project", ""),
                "status": status,
                "hard_fail_count": len(hard_fails),
            },
            [
                ("Routing Order", markdown_table(["net", "stage", "priority", "critical", "power", "usb", "status"], rows)),
                ("Errors", "\n".join(f"- {item}" for item in errors) if errors else "_none_"),
                ("Warnings", "\n".join(f"- {item}" for item in warnings) if warnings else "_none_"),
                ("Hard Fails", "\n".join(f"- {item}" for item in hard_fails) if hard_fails else "_none_"),
            ],
        )
        dump_markdown(args.markdown, text)

    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
