#!/usr/bin/env python3
"""Detect trace segments that cross routing keepouts in a routing fixture JSON."""

from __future__ import annotations

import argparse

from _routing_common import dump_json, dump_markdown, get_keepouts, get_traces, make_markdown, markdown_table, parse_args_markdown, segment_crosses_keepout, load_json


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("routing_state_json")
    parser.add_argument("output_json")
    parse_args_markdown(parser)
    args = parser.parse_args()

    payload = load_json(args.routing_state_json)
    keepouts = get_keepouts(payload)
    traces = get_traces(payload)
    violations: list[dict] = []

    for trace in traces:
        net = trace.get("net", "<unnamed_net>")
        for segment in trace.get("segments", []):
            for keepout in keepouts:
                if segment_crosses_keepout(segment, keepout):
                    violations.append(
                        {
                            "net": net,
                            "keepout": keepout.get("name", "<unnamed_keepout>"),
                            "keepout_type": keepout.get("type", ""),
                            "segment": segment,
                        }
                    )

    rf_or_antenna = [
        item for item in violations if str(item.get("keepout_type", "")).upper() in {"RF_KEEPOUT", "ANTENNA_KEEPOUT"}
    ]
    hard_fails: list[str] = []
    if any(str(item.get("keepout_type", "")).upper() == "RF_KEEPOUT" for item in rf_or_antenna):
        hard_fails.append("trace crosses RF keepout")
    if any(str(item.get("keepout_type", "")).upper() == "ANTENNA_KEEPOUT" for item in rf_or_antenna):
        hard_fails.append("trace crosses antenna keepout")

    status = "PASS" if not violations else "AUTO_BLOCKED_BAD_LAYOUT"
    result = {
        "schema_version": "1.0",
        "tool": "detect_trace_keepout_violations",
        "project": payload.get("project", ""),
        "status": status,
        "summary": {
            "violation_count": len(violations),
            "rf_or_antenna_violation_count": len(rf_or_antenna),
        },
        "violation_count": len(violations),
        "rf_or_antenna_violation_count": len(rf_or_antenna),
        "violations": violations,
        "hard_fails": hard_fails,
    }
    dump_json(args.output_json, result)

    if args.markdown:
        rows = [[item["net"], item["keepout"], item["keepout_type"]] for item in violations]
        text = make_markdown(
            "Keepout Violations",
            {"project": payload.get("project", ""), "status": status},
            [
                ("Violations", markdown_table(["net", "keepout", "type"], rows)),
                ("Hard Fails", "\n".join(f"- {item}" for item in hard_fails) if hard_fails else "_none_"),
            ],
        )
        dump_markdown(args.markdown, text)

    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
