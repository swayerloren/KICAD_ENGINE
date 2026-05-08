#!/usr/bin/env python3
"""Extract the critical-net routing plan from a generated routing plan JSON."""

from __future__ import annotations

import argparse

from _routing_common import dump_json, dump_markdown, make_markdown, markdown_table, parse_args_markdown, load_json


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("routing_plan_json")
    parser.add_argument("output_json")
    parse_args_markdown(parser)
    args = parser.parse_args()

    plan = load_json(args.routing_plan_json)
    critical_nets = [item for item in plan.get("routing_order", []) if item.get("critical")]
    missing_critical = [item for item in critical_nets if item.get("routing_status") not in {"ROUTED", "PLANNED"}]
    hard_fails = []
    if not critical_nets:
        hard_fails.append("critical net set missing from routing plan")

    status = "PASS"
    if plan.get("status") == "AUTO_BLOCKED_MISSING_DATA":
        status = "AUTO_BLOCKED_MISSING_DATA"
    elif hard_fails:
        status = "AUTO_BLOCKED_BAD_LAYOUT"

    result = {
        "schema_version": "1.0",
        "tool": "route_critical_nets_plan",
        "project": plan.get("project", ""),
        "status": status,
        "summary": {
            "critical_net_count": len(critical_nets),
            "missing_critical_count": len(missing_critical),
        },
        "critical_nets": critical_nets,
        "critical_net_count": len(critical_nets),
        "missing_critical_nets": [item["name"] for item in missing_critical],
        "review_required": [
            item["name"]
            for item in critical_nets
            if item.get("review_required") or item.get("usb") or item.get("role") in {"BUCK_SW", "BUCK_BST", "REGULATOR_LOOP", "REG_SW"}
        ],
        "hard_fails": hard_fails,
        "autorouting_policy": "REVIEW_ONLY",
    }
    dump_json(args.output_json, result)

    if args.markdown:
        rows = [
            [item["name"], item["stage_name"], item["routing_priority"], item["routing_status"], item["review_required"]]
            for item in critical_nets
        ]
        text = make_markdown(
            "Critical Net Routing Plan",
            {
                "project": plan.get("project", ""),
                "status": status,
            },
            [
                ("Critical Nets", markdown_table(["net", "stage", "priority", "status", "review_required"], rows)),
                ("Hard Fails", "\n".join(f"- {item}" for item in hard_fails) if hard_fails else "_none_"),
            ],
        )
        dump_markdown(args.markdown, text)

    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
