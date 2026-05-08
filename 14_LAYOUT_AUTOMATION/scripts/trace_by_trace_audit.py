#!/usr/bin/env python3
"""Audit every trace in a routing fixture JSON."""

from __future__ import annotations

import argparse

from _routing_common import dump_json, dump_markdown, get_keepouts, get_traces, load_json, make_markdown, markdown_table, normalized_nets, parse_args_markdown
from route_quality_common import analyze_trace_geometry, coordinates_text


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
    geometry = analyze_trace_geometry(trace, net_info, keepouts)
    issues.extend(geometry["issue_codes"])

    widths = sorted({round(float(seg.get("width_mm", 0.0)), 4) for seg in segments})

    return {
        "net": net,
        "critical": critical,
        "routing_status": routing_status,
        "segment_count": len(segments),
        "via_count": via_count,
        "via_reason": via_reason,
        "widths_mm": widths,
        "trace_length_mm": geometry["trace_length_mm"],
        "direct_length_mm": geometry["direct_length_mm"],
        "length_ratio": geometry["length_ratio"],
        "issues": sorted(set(issues)),
        "hard_fail_statuses": geometry["hard_fail_statuses"],
        "findings": geometry["findings"],
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
    hard_fail_statuses = sorted({status for item in audits for status in item["hard_fail_statuses"]})
    hard_fails: list[str] = list(hard_fail_statuses)
    if missing_trace_nets:
        hard_fails.append("trace-by-trace audit missing")

    status = "PASS" if not flagged and not missing_trace_nets and audits else "AUTO_BLOCKED_BAD_LAYOUT"
    detailed_findings = [finding for item in audits for finding in item["findings"]]
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
        "detailed_findings": detailed_findings,
        "hard_fail_statuses": hard_fail_statuses,
        "hard_fails": sorted(set(hard_fails)),
    }
    dump_json(args.output_json, result)

    if args.markdown:
        rows = [
            [
                item["net"],
                item["critical"],
                item["segment_count"],
                item["via_count"],
                ",".join(item["hard_fail_statuses"]) or "_none_",
            ]
            for item in audits
        ]
        finding_rows = [
            [
                finding["net"],
                finding["status"],
                finding["layer"],
                coordinates_text(finding["segment_coordinates"]),
                finding["reason"],
                finding["recommended_fix"],
            ]
            for finding in detailed_findings
        ]
        text = make_markdown(
            "Trace By Trace Audit",
            {"project": payload.get("project", ""), "status": status},
            [
                ("Trace Audit", markdown_table(["net", "critical", "segments", "vias", "hard_fail_statuses"], rows)),
                ("Hard Fails", "\n".join(f"- {item}" for item in sorted(set(hard_fails))) if hard_fails else "_none_"),
                (
                    "Detailed Findings",
                    markdown_table(
                        ["net", "status", "layer", "segment_coordinates", "reason", "recommended_fix"],
                        finding_rows,
                    ),
                ),
            ],
        )
        dump_markdown(args.markdown, text)

    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
