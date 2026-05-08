#!/usr/bin/env python3
"""Detect unrouted nets from a routing fixture JSON."""

from __future__ import annotations

import argparse

from _routing_common import dump_json, dump_markdown, make_markdown, markdown_table, normalized_nets, parse_args_markdown, load_json


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("routing_state_json")
    parser.add_argument("output_json")
    parse_args_markdown(parser)
    args = parser.parse_args()

    payload = load_json(args.routing_state_json)
    nets = normalized_nets(payload)
    unrouted = [item for item in nets if item["routing_status"] not in {"ROUTED", "PLANNED"}]
    unrouted_critical = [item["name"] for item in unrouted if item["critical"]]
    unrouted_power = [item["name"] for item in unrouted if item["power"]]

    hard_fails: list[str] = []
    if unrouted_critical:
        hard_fails.append("unrouted critical net")
    if unrouted_power:
        hard_fails.append("critical power net missing")

    status = "PASS" if not unrouted else "AUTO_BLOCKED_BAD_LAYOUT"
    result = {
        "schema_version": "1.0",
        "tool": "detect_unrouted_nets",
        "project": payload.get("project", ""),
        "status": status,
        "summary": {
            "unrouted_count": len(unrouted),
            "unrouted_critical_count": len(unrouted_critical),
        },
        "unrouted_nets": [item["name"] for item in unrouted],
        "unrouted_count": len(unrouted),
        "unrouted_critical_nets": unrouted_critical,
        "unrouted_power_nets": unrouted_power,
        "hard_fails": hard_fails,
    }
    dump_json(args.output_json, result)

    if args.markdown:
        rows = [[item["name"], item["critical"], item["power"], item["routing_status"]] for item in unrouted]
        text = make_markdown(
            "Unrouted Nets",
            {"project": payload.get("project", ""), "status": status},
            [
                ("Unrouted Nets", markdown_table(["net", "critical", "power", "status"], rows)),
                ("Hard Fails", "\n".join(f"- {item}" for item in hard_fails) if hard_fails else "_none_"),
            ],
        )
        dump_markdown(args.markdown, text)

    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
