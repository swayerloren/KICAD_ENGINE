#!/usr/bin/env python3
"""Audit every trace in a routing fixture JSON."""

from __future__ import annotations

import argparse

from _routing_common import angle_degrees, dump_json, dump_markdown, get_keepouts, get_traces, make_markdown, markdown_table, normalized_nets, parse_args_markdown, segment_crosses_keepout, load_json


def classify_trace(trace: dict, net_info: dict, keepouts: list[dict]) -> dict:
    issues: list[str] = []
    segments = trace.get("segments", [])
    via_count = int(trace.get("via_count", 0))
    via_reason = str(trace.get("via_reason", "")).strip()
    net = trace.get("net", "<unnamed_net>")
    critical = bool(trace.get("critical", net_info.get("critical", False)))
    routing_status = str(trace.get("routing_status", net_info.get("routing_status", "UNROUTED"))).upper()

    if not segments:
        issues.append("no_segments")
    if critical and routing_status != "ROUTED":
        issues.append("critical_trace_unrouted")
    if via_count > 0 and critical and not via_reason:
        issues.append("vias_without_reason")

    widths = sorted({round(float(seg.get("width_mm", 0.0)), 4) for seg in segments})
    if net_info.get("power") and widths and min(widths) + 1e-9 < float(net_info.get("width_mm", 0.2)):
        issues.append("power_trace_too_narrow")

    angles: list[float] = []
    for left, right in zip(segments, segments[1:]):
        ang = round(angle_degrees(left, right), 3)
        angles.append(ang)
        if abs(ang - 90.0) < 0.01:
            issues.append("right_angle_turn")
        elif 0.0 < ang < 90.0 and abs(ang - 45.0) > 0.01:
            issues.append("acute_or_nonstandard_angle")

    for segment in segments:
        for keepout in keepouts:
            if segment_crosses_keepout(segment, keepout):
                keepout_type = str(keepout.get("type", "")).upper()
                if keepout_type == "RF_KEEPOUT":
                    issues.append("trace_crosses_rf_keepout")
                if keepout_type == "ANTENNA_KEEPOUT":
                    issues.append("trace_crosses_antenna_keepout")

    return {
        "net": net,
        "critical": critical,
        "routing_status": routing_status,
        "segment_count": len(segments),
        "via_count": via_count,
        "via_reason": via_reason,
        "widths_mm": widths,
        "angles_deg": angles,
        "issues": sorted(set(issues)),
        "review_required": bool(trace.get("review_required", net_info.get("review_required", False))),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("routing_state_json")
    parser.add_argument("output_json")
    parse_args_markdown(parser)
    args = parser.parse_args()

    payload = load_json(args.routing_state_json)
    net_lookup = {item["name"]: item for item in normalized_nets(payload)}
    traces = get_traces(payload)
    keepouts = get_keepouts(payload, {"RF_KEEPOUT", "ANTENNA_KEEPOUT"})
    audits = [classify_trace(trace, net_lookup.get(str(trace.get("net", "")), {}), keepouts) for trace in traces]

    routed_trace_nets = {str(trace.get("net", "")) for trace in traces if str(trace.get("routing_status", "")).upper() == "ROUTED"}
    audited_nets = {item["net"] for item in audits}
    missing_trace_nets = sorted(routed_trace_nets - audited_nets)

    flagged = [item for item in audits if item["issues"]]
    hard_fails: list[str] = []
    if missing_trace_nets:
        hard_fails.append("trace-by-trace audit missing")
    if any("vias_without_reason" in item["issues"] for item in audits if item["critical"]):
        hard_fails.append("via used without reason on critical net")
    if any("trace_crosses_rf_keepout" in item["issues"] for item in audits):
        hard_fails.append("trace crosses RF keepout")
    if any("trace_crosses_antenna_keepout" in item["issues"] for item in audits):
        hard_fails.append("trace crosses antenna keepout")

    status = "PASS" if not flagged and not missing_trace_nets and audits else "AUTO_BLOCKED_BAD_LAYOUT"
    result = {
        "schema_version": "1.0",
        "tool": "trace_by_trace_audit",
        "project": payload.get("project", ""),
        "status": status,
        "summary": {
            "trace_count": len(audits),
            "flagged_count": len(flagged),
            "critical_trace_count": sum(1 for item in audits if item["critical"]),
        },
        "trace_count": len(audits),
        "flagged_count": len(flagged),
        "critical_trace_count": sum(1 for item in audits if item["critical"]),
        "audit_complete": not missing_trace_nets,
        "missing_trace_nets": missing_trace_nets,
        "traces": audits,
        "hard_fails": sorted(set(hard_fails)),
    }
    dump_json(args.output_json, result)

    if args.markdown:
        rows = [
            [item["net"], item["critical"], item["segment_count"], item["via_count"], ",".join(item["issues"]) or "_none_"]
            for item in audits
        ]
        text = make_markdown(
            "Trace By Trace Audit",
            {"project": payload.get("project", ""), "status": status},
            [
                ("Trace Audit", markdown_table(["net", "critical", "segments", "vias", "issues"], rows)),
                ("Hard Fails", "\n".join(f"- {item}" for item in sorted(set(hard_fails))) if hard_fails else "_none_"),
            ],
        )
        dump_markdown(args.markdown, text)

    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
