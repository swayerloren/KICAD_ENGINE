#!/usr/bin/env python3
"""Score a routing plan and routing-state audit outputs with hard-fail rules."""

from __future__ import annotations

import argparse

from _routing_common import dump_json, dump_markdown, make_markdown, markdown_table, normalized_nets, parse_args_markdown, regulator_loop_present, usb_pair_names, load_json


def capped(value: int, low: int = 0, high: int = 100) -> int:
    return max(low, min(high, value))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture_json")
    parser.add_argument("routing_plan_json")
    parser.add_argument("critical_plan_json")
    parser.add_argument("unrouted_report_json")
    parser.add_argument("keepout_report_json")
    parser.add_argument("trace_audit_json")
    parser.add_argument("output_json")
    parse_args_markdown(parser)
    args = parser.parse_args()

    fixture = load_json(args.fixture_json)
    plan = load_json(args.routing_plan_json)
    critical_plan = load_json(args.critical_plan_json)
    unrouted = load_json(args.unrouted_report_json)
    keepouts = load_json(args.keepout_report_json)
    trace_audit = load_json(args.trace_audit_json)
    normalized = normalized_nets(fixture)

    hard_fails: list[str] = []
    blocked_reasons: list[str] = []

    power_nets = [item for item in normalized if item["power"]]
    critical_nets = [item for item in normalized if item["critical"]]
    usb_nets = usb_pair_names(fixture)
    audit_lookup = {item["net"]: item for item in trace_audit.get("traces", [])}

    if any(item["name"] in unrouted.get("unrouted_power_nets", []) for item in power_nets if item["critical"]):
        hard_fails.append("critical power net missing")
    if ("USB_D+" in usb_nets) ^ ("USB_D-" in usb_nets):
        hard_fails.append("USB D+/D- incomplete")
    if keepouts.get("rf_or_antenna_violation_count", 0):
        if any(str(item.get("keepout_type", "")).upper() == "RF_KEEPOUT" for item in keepouts.get("violations", [])):
            hard_fails.append("trace crosses RF keepout")
        if any(str(item.get("keepout_type", "")).upper() == "ANTENNA_KEEPOUT" for item in keepouts.get("violations", [])):
            hard_fails.append("trace crosses antenna keepout")
    if unrouted.get("unrouted_critical_nets"):
        hard_fails.append("unrouted critical net")
    if not fixture.get("ground_strategy", {}).get("present", False):
        hard_fails.append("GND strategy missing")
    if not regulator_loop_present(fixture):
        hard_fails.append("regulator critical loop not planned")
    if any("vias_without_reason" in item.get("issues", []) for item in trace_audit.get("traces", []) if item.get("critical")):
        hard_fails.append("via used without reason on critical net")
    if not trace_audit.get("audit_complete", False):
        hard_fails.append("trace-by-trace audit missing")

    if plan.get("status") != "PASS":
        blocked_reasons.append("routing plan did not pass")
    if critical_plan.get("status") != "PASS":
        blocked_reasons.append("critical-net routing plan did not pass")
    if unrouted.get("unrouted_count", 0):
        blocked_reasons.append(f"{unrouted.get('unrouted_count', 0)} unrouted nets remain")
    if keepouts.get("violation_count", 0):
        blocked_reasons.append(f"{keepouts.get('violation_count', 0)} keepout violations detected")
    if trace_audit.get("flagged_count", 0):
        blocked_reasons.append(f"{trace_audit.get('flagged_count', 0)} trace audit entries flagged")
    blocked_reasons.extend(hard_fails)
    blocked_reasons = sorted(dict.fromkeys(blocked_reasons))

    routed_critical_count = sum(1 for item in critical_nets if item["routing_status"] == "ROUTED")
    critical_score = capped(int(round(20 * routed_critical_count / max(1, len(critical_nets)))))

    power_score = 15
    for item in power_nets:
        audit = audit_lookup.get(item["name"])
        if not audit and item["routing_status"] == "ROUTED":
            power_score -= 4
            continue
        if audit and "power_trace_too_narrow" in audit.get("issues", []):
            power_score -= 5
        if audit and "vias_without_reason" in audit.get("issues", []):
            power_score -= 3
    power_score = capped(power_score, 0, 15)

    usb_score = 10
    if usb_nets:
        if not {"USB_D+", "USB_D-"}.issubset(usb_nets):
            usb_score = 0
        else:
            plus = audit_lookup.get("USB_D+")
            minus = audit_lookup.get("USB_D-")
            if not plus or not minus:
                usb_score -= 5
            elif plus.get("via_count", 0) != minus.get("via_count", 0):
                usb_score -= 2
            if keepouts.get("rf_or_antenna_violation_count", 0):
                usb_score = 0
    usb_score = capped(usb_score, 0, 10)

    rf_score = 15 if keepouts.get("rf_or_antenna_violation_count", 0) == 0 else 0

    via_score = 10
    for audit in trace_audit.get("traces", []):
        if "vias_without_reason" in audit.get("issues", []):
            via_score -= 4
        net_info = next((item for item in normalized if item["name"] == audit["net"]), None)
        if net_info and audit.get("via_count", 0) > net_info.get("max_vias", 99):
            via_score -= 3
    via_score = capped(via_score, 0, 10)

    unrouted_score = capped(10 - (2 * int(unrouted.get("unrouted_count", 0))) - (4 * len(unrouted.get("unrouted_critical_nets", []))), 0, 10)
    drc_risk_score = 10
    drc_risk = str(fixture.get("routing_status", {}).get("drc_risk", "LOW")).upper()
    if drc_risk == "MEDIUM":
        drc_risk_score -= 3
    elif drc_risk == "HIGH":
        drc_risk_score -= 6
    if keepouts.get("violation_count", 0):
        drc_risk_score = 0
    drc_risk_score = capped(drc_risk_score, 0, 10)

    expected_trace_count = len([item for item in normalized if item["routing_status"] == "ROUTED"])
    actual_trace_count = int(trace_audit.get("trace_count", 0))
    trace_audit_score = 5 if trace_audit.get("audit_complete", False) and actual_trace_count >= expected_trace_count else 0

    human_review_penalty = 0
    review_required_count = sum(1 for item in normalized if item.get("review_required"))
    if review_required_count >= 4:
        human_review_penalty = 5
    elif review_required_count >= 2:
        human_review_penalty = 3
    elif review_required_count >= 1:
        human_review_penalty = 1

    total_score = capped(
        critical_score
        + power_score
        + usb_score
        + rf_score
        + via_score
        + unrouted_score
        + drc_risk_score
        + trace_audit_score
        - human_review_penalty
    )

    status = "PASS"
    if hard_fails:
        status = "AUTO_BLOCKED_BAD_LAYOUT"
    elif plan.get("status") == "AUTO_BLOCKED_MISSING_DATA":
        status = "AUTO_BLOCKED_MISSING_DATA"
    elif blocked_reasons:
        status = "AUTO_BLOCKED_BAD_LAYOUT"

    readiness = {
        "ready_for_real_kicad_test": status == "PASS",
        "exact_blockers": blocked_reasons,
    }

    result = {
        "schema_version": "1.0",
        "tool": "score_routing_plan",
        "project": fixture.get("project", ""),
        "status": status,
        "summary": {"total_score": total_score, "hard_fail_count": len(hard_fails)},
        "total_score": total_score,
        "scores": {
            "critical_net_completeness": critical_score,
            "power_path_quality": power_score,
            "usb_path_quality": usb_score,
            "rf_keepout_compliance": rf_score,
            "via_count_reasonableness": via_score,
            "unrouted_net_count": unrouted_score,
            "drc_risk": drc_risk_score,
            "trace_audit_completeness": trace_audit_score,
            "human_review_risk": human_review_penalty,
        },
        "hard_fails": sorted(dict.fromkeys(hard_fails)),
        "blocked_reasons": blocked_reasons,
        "readiness": readiness,
    }
    dump_json(args.output_json, result)

    if args.markdown:
        rows = [[name, score] for name, score in result["scores"].items()]
        text = make_markdown(
            "Routing Scorecard",
            {"project": fixture.get("project", ""), "status": status, "total_score": total_score},
            [
                ("Scores", markdown_table(["category", "value"], rows)),
                ("Hard Fails", "\n".join(f"- {item}" for item in result["hard_fails"]) if result["hard_fails"] else "_none_"),
                ("Blocked Reasons", "\n".join(f"- {item}" for item in blocked_reasons) if blocked_reasons else "_none_"),
            ],
        )
        dump_markdown(args.markdown, text)

    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
