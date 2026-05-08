#!/usr/bin/env python3
"""Shared routing geometry quality helpers."""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any, Callable

from _routing_common import (
    angle_degrees,
    dump_json,
    dump_markdown,
    get_keepouts,
    get_traces,
    load_json,
    make_markdown,
    markdown_table,
    normalized_nets,
    segment_crosses_keepout,
    trace_length_mm,
)


RIGHT_ANGLE_FOUND = "RIGHT_ANGLE_FOUND"
ACUTE_JOG_FOUND = "ACUTE_JOG_FOUND"
PAD_ENTRY_GEOMETRY_POOR = "PAD_ENTRY_GEOMETRY_POOR"
UNNECESSARY_ZIGZAG_FOUND = "UNNECESSARY_ZIGZAG_FOUND"
CRITICAL_LOOP_DETOUR_FOUND = "CRITICAL_LOOP_DETOUR_FOUND"
KEEP_OUT_CROSSING_FOUND = "KEEP_OUT_CROSSING_FOUND"
UNJUSTIFIED_VIA_FOUND = "UNJUSTIFIED_VIA_FOUND"
TRACE_WIDTH_MISMATCH_FOUND = "TRACE_WIDTH_MISMATCH_FOUND"

HARD_FAIL_STATUSES = [
    RIGHT_ANGLE_FOUND,
    ACUTE_JOG_FOUND,
    PAD_ENTRY_GEOMETRY_POOR,
    UNNECESSARY_ZIGZAG_FOUND,
    CRITICAL_LOOP_DETOUR_FOUND,
    KEEP_OUT_CROSSING_FOUND,
    UNJUSTIFIED_VIA_FOUND,
    TRACE_WIDTH_MISMATCH_FOUND,
]

STATUS_TO_ISSUE = {
    RIGHT_ANGLE_FOUND: "right_angle_turn",
    ACUTE_JOG_FOUND: "acute_jog_found",
    PAD_ENTRY_GEOMETRY_POOR: "poor_pad_entry_geometry",
    UNNECESSARY_ZIGZAG_FOUND: "unnecessary_zigzag_found",
    CRITICAL_LOOP_DETOUR_FOUND: "critical_loop_detour",
    KEEP_OUT_CROSSING_FOUND: "trace_crosses_keepout",
    UNJUSTIFIED_VIA_FOUND: "vias_without_reason",
    TRACE_WIDTH_MISMATCH_FOUND: "trace_width_mismatch",
}

RIGHT_ANGLE_TOLERANCE_DEG = 0.75
FORTY_FIVE_TOLERANCE_DEG = 0.75
PAD_ENTRY_MIN_RUNOUT_MM = 0.75
ZIGZAG_LENGTH_RATIO = 1.20
CRITICAL_DETOUR_RATIO = 1.50


def round_mm(value: Any) -> float:
    return round(float(value), 3)


def same_point(ax: float, ay: float, bx: float, by: float, tol: float = 1e-6) -> bool:
    return abs(ax - bx) <= tol and abs(ay - by) <= tol


def segment_start(segment: dict[str, Any]) -> tuple[float, float]:
    return float(segment["x1"]), float(segment["y1"])


def segment_end(segment: dict[str, Any]) -> tuple[float, float]:
    return float(segment["x2"]), float(segment["y2"])


def segment_length(segment: dict[str, Any]) -> float:
    x1, y1 = segment_start(segment)
    x2, y2 = segment_end(segment)
    return math.hypot(x2 - x1, y2 - y1)


def segment_vector(segment: dict[str, Any]) -> tuple[float, float]:
    x1, y1 = segment_start(segment)
    x2, y2 = segment_end(segment)
    return x2 - x1, y2 - y1


def trace_endpoints(trace: dict[str, Any]) -> tuple[tuple[float, float], tuple[float, float]] | None:
    segments = trace.get("segments", [])
    if not segments:
        return None
    return segment_start(segments[0]), segment_end(segments[-1])


def direct_length(trace: dict[str, Any]) -> float:
    endpoints = trace_endpoints(trace)
    if not endpoints:
        return 0.0
    (x1, y1), (x2, y2) = endpoints
    return math.hypot(x2 - x1, y2 - y1)


def normalized_heading(segment: dict[str, Any]) -> tuple[int, int]:
    dx, dy = segment_vector(segment)

    def norm(value: float) -> int:
        if value > 1e-6:
            return 1
        if value < -1e-6:
            return -1
        return 0

    return norm(dx), norm(dy)


def segment_coordinates(segment: dict[str, Any]) -> dict[str, float]:
    return {
        "x1_mm": round_mm(segment["x1"]),
        "y1_mm": round_mm(segment["y1"]),
        "x2_mm": round_mm(segment["x2"]),
        "y2_mm": round_mm(segment["y2"]),
    }


def coordinates_text(payload: Any) -> str:
    if isinstance(payload, dict):
        return f"({payload['x1_mm']}, {payload['y1_mm']}) -> ({payload['x2_mm']}, {payload['y2_mm']})"
    if isinstance(payload, list):
        parts = []
        for item in payload:
            coords = item if isinstance(item, dict) else {}
            if coords:
                parts.append(f"({coords['x1_mm']}, {coords['y1_mm']}) -> ({coords['x2_mm']}, {coords['y2_mm']})")
        return " ; ".join(parts)
    return ""


def build_finding(
    trace: dict[str, Any],
    net_info: dict[str, Any],
    status: str,
    segment_payload: dict[str, Any] | list[dict[str, Any]],
    layer: str,
    reason: str,
    recommended_fix: str,
) -> dict[str, Any]:
    return {
        "trace_id": str(trace.get("id", "")),
        "net": str(trace.get("net", "<unnamed_net>")),
        "status": status,
        "issue_code": STATUS_TO_ISSUE[status],
        "layer": layer,
        "segment_coordinates": segment_payload,
        "reason": reason,
        "recommended_fix": recommended_fix,
        "critical": bool(trace.get("critical", net_info.get("critical", False))),
    }


def good_45_angle(angle_deg: float) -> bool:
    return abs(angle_deg - 45.0) <= FORTY_FIVE_TOLERANCE_DEG


def right_angle(angle_deg: float) -> bool:
    return abs(angle_deg - 90.0) <= RIGHT_ANGLE_TOLERANCE_DEG


def acute_non_45(angle_deg: float) -> bool:
    return 0.0 < angle_deg < (90.0 - RIGHT_ANGLE_TOLERANCE_DEG) and not good_45_angle(angle_deg)


def detect_right_angle_findings(trace: dict[str, Any], net_info: dict[str, Any]) -> list[dict[str, Any]]:
    segments = trace.get("segments", [])
    findings: list[dict[str, Any]] = []
    for left, right in zip(segments, segments[1:]):
        angle = angle_degrees(left, right)
        if right_angle(angle):
            findings.append(
                build_finding(
                    trace,
                    net_info,
                    RIGHT_ANGLE_FOUND,
                    [segment_coordinates(left), segment_coordinates(right)],
                    str(right.get("layer", left.get("layer", ""))),
                    f"Found a {round(angle, 3)} degree bend. Routing requires 45-degree or smoother geometry.",
                    "Replace the 90-degree corner with a 45-degree bend or a smoother critical-net path.",
                )
            )
    return findings


def detect_acute_jog_findings(trace: dict[str, Any], net_info: dict[str, Any]) -> list[dict[str, Any]]:
    segments = trace.get("segments", [])
    findings: list[dict[str, Any]] = []
    for left, right in zip(segments, segments[1:]):
        angle = angle_degrees(left, right)
        if acute_non_45(angle):
            findings.append(
                build_finding(
                    trace,
                    net_info,
                    ACUTE_JOG_FOUND,
                    [segment_coordinates(left), segment_coordinates(right)],
                    str(right.get("layer", left.get("layer", ""))),
                    f"Found a non-45 acute jog of {round(angle, 3)} degrees.",
                    "Rebuild this bend as a 45-degree transition or a straight continuation without an acute jog.",
                )
            )
    return findings


def detect_bad_pad_entry_findings(trace: dict[str, Any], net_info: dict[str, Any]) -> list[dict[str, Any]]:
    if not bool(trace.get("critical", net_info.get("critical", False))):
        return []
    segments = trace.get("segments", [])
    if len(segments) < 2:
        return []

    min_runout = max(
        PAD_ENTRY_MIN_RUNOUT_MM,
        float(trace.get("pad_entry_min_runout_mm", 0.0) or 0.0),
        float(net_info.get("width_mm", 0.2)) * 3.0,
    )
    findings: list[dict[str, Any]] = []

    first_angle = angle_degrees(segments[0], segments[1])
    if segment_length(segments[0]) + 1e-9 < min_runout and first_angle > RIGHT_ANGLE_TOLERANCE_DEG:
        findings.append(
            build_finding(
                trace,
                net_info,
                PAD_ENTRY_GEOMETRY_POOR,
                [segment_coordinates(segments[0]), segment_coordinates(segments[1])],
                str(segments[0].get("layer", "")),
                f"Critical net bends after only {round(segment_length(segments[0]), 3)} mm of pad runout.",
                f"Extend a straight pad exit to at least {round(min_runout, 3)} mm before the first bend.",
            )
        )

    last_angle = angle_degrees(segments[-2], segments[-1])
    if segment_length(segments[-1]) + 1e-9 < min_runout and last_angle > RIGHT_ANGLE_TOLERANCE_DEG:
        findings.append(
            build_finding(
                trace,
                net_info,
                PAD_ENTRY_GEOMETRY_POOR,
                [segment_coordinates(segments[-2]), segment_coordinates(segments[-1])],
                str(segments[-1].get("layer", "")),
                f"Critical net enters the destination pad with only {round(segment_length(segments[-1]), 3)} mm of straight runout.",
                f"Add at least {round(min_runout, 3)} mm of straight run before the destination pad.",
            )
        )

    return findings


def detect_unnecessary_zigzag_findings(trace: dict[str, Any], net_info: dict[str, Any]) -> list[dict[str, Any]]:
    segments = trace.get("segments", [])
    if len(segments) < 4:
        return []

    path_length = trace_length_mm(segments)
    direct = direct_length(trace)
    if direct <= 0:
        return []

    direction_reversals = 0
    bend_count = 0
    headings = [normalized_heading(segment) for segment in segments]
    for previous, current in zip(headings, headings[1:]):
        if previous != current:
            bend_count += 1
        if previous[0] != 0 and current[0] != 0 and previous[0] != current[0]:
            direction_reversals += 1
        if previous[1] != 0 and current[1] != 0 and previous[1] != current[1]:
            direction_reversals += 1

    if bend_count < 3:
        return []
    if path_length / direct <= ZIGZAG_LENGTH_RATIO and direction_reversals == 0:
        return []

    return [
        build_finding(
            trace,
            net_info,
            UNNECESSARY_ZIGZAG_FOUND,
            [segment_coordinates(item) for item in segments],
            str(segments[0].get("layer", "")),
            f"Trace length is {round(path_length, 3)} mm versus {round(direct, 3)} mm direct with repeated geometry reversals.",
            "Collapse the jog sequence into a simpler 45-degree path with fewer bends and no unnecessary reversals.",
        )
    ]


def detect_critical_detour_findings(trace: dict[str, Any], net_info: dict[str, Any]) -> list[dict[str, Any]]:
    if not bool(trace.get("critical", net_info.get("critical", False))):
        return []
    segments = trace.get("segments", [])
    if len(segments) < 3:
        return []
    path_length = trace_length_mm(segments)
    direct = direct_length(trace)
    if direct <= 0:
        return []
    if path_length / direct <= CRITICAL_DETOUR_RATIO and path_length <= direct + 2.5:
        return []
    return [
        build_finding(
            trace,
            net_info,
            CRITICAL_LOOP_DETOUR_FOUND,
            [segment_coordinates(item) for item in segments],
            str(segments[0].get("layer", "")),
            f"Critical trace detours to {round(path_length, 3)} mm for a {round(direct, 3)} mm point-to-point span.",
            "Shorten this critical route, reduce detours, or repair placement so the path stays compact and direct.",
        )
    ]


def detect_keepout_crossing_findings(trace: dict[str, Any], net_info: dict[str, Any], keepouts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for segment in trace.get("segments", []):
        for keepout in keepouts:
            if segment_crosses_keepout(segment, keepout):
                keepout_type = str(keepout.get("type", "")).upper()
                findings.append(
                    build_finding(
                        trace,
                        net_info,
                        KEEP_OUT_CROSSING_FOUND,
                        segment_coordinates(segment),
                        str(segment.get("layer", "")),
                        f"Trace crosses keepout `{keepout.get('name', '')}` of type `{keepout_type}`.",
                        "Reroute the segment completely outside the RF or antenna keepout boundary.",
                    )
                )
    return findings


def detect_unjustified_via_findings(trace: dict[str, Any], net_info: dict[str, Any]) -> list[dict[str, Any]]:
    if int(trace.get("via_count", 0)) <= 0:
        return []
    if not bool(trace.get("critical", net_info.get("critical", False))):
        return []
    if str(trace.get("via_reason", "")).strip():
        return []
    segments = trace.get("segments", [])
    payload = [segment_coordinates(item) for item in segments] if segments else []
    return [
        build_finding(
            trace,
            net_info,
            UNJUSTIFIED_VIA_FOUND,
            payload,
            "MULTI_LAYER",
            f"Critical trace uses {int(trace.get('via_count', 0))} vias without a recorded reason.",
            "Either remove the via usage or record a specific engineering reason for each critical-net layer change.",
        )
    ]


def detect_width_mismatch_findings(trace: dict[str, Any], net_info: dict[str, Any]) -> list[dict[str, Any]]:
    segments = trace.get("segments", [])
    if not segments:
        return []
    target = float(net_info.get("width_mm", 0.0))
    widths = [float(segment.get("width_mm", target or 0.0)) for segment in segments]
    unique = sorted({round(width, 4) for width in widths})
    findings: list[dict[str, Any]] = []
    for segment, width in zip(segments, widths):
        if target > 0 and width + 1e-9 < target:
            findings.append(
                build_finding(
                    trace,
                    net_info,
                    TRACE_WIDTH_MISMATCH_FOUND,
                    segment_coordinates(segment),
                    str(segment.get("layer", "")),
                    f"Segment width {round(width, 4)} mm is below the target width {round(target, 4)} mm.",
                    "Increase the segment width to the assigned net target or document a justified neckdown.",
                )
            )
    if len(unique) > 1 and bool(trace.get("critical", net_info.get("critical", False))):
        findings.append(
            build_finding(
                trace,
                net_info,
                TRACE_WIDTH_MISMATCH_FOUND,
                [segment_coordinates(item) for item in segments],
                str(segments[0].get("layer", "")),
                f"Critical trace mixes widths {', '.join(str(item) for item in unique)} mm without a recorded justification.",
                "Use one consistent critical-net width unless the neckdown is explicitly justified and documented.",
            )
        )
    return findings


GEOMETRY_DETECTORS: dict[str, tuple[str, Callable[..., list[dict[str, Any]]]]] = {
    "right_angles": (RIGHT_ANGLE_FOUND, detect_right_angle_findings),
    "acute_jogs": (ACUTE_JOG_FOUND, detect_acute_jog_findings),
    "bad_pad_entry": (PAD_ENTRY_GEOMETRY_POOR, detect_bad_pad_entry_findings),
    "unnecessary_zigzags": (UNNECESSARY_ZIGZAG_FOUND, detect_unnecessary_zigzag_findings),
    "critical_detours": (CRITICAL_LOOP_DETOUR_FOUND, detect_critical_detour_findings),
    "keepout_crossings": (KEEP_OUT_CROSSING_FOUND, detect_keepout_crossing_findings),
    "unjustified_vias": (UNJUSTIFIED_VIA_FOUND, detect_unjustified_via_findings),
    "width_mismatches": (TRACE_WIDTH_MISMATCH_FOUND, detect_width_mismatch_findings),
}


def analyze_trace_geometry(trace: dict[str, Any], net_info: dict[str, Any], keepouts: list[dict[str, Any]]) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    findings.extend(detect_right_angle_findings(trace, net_info))
    findings.extend(detect_acute_jog_findings(trace, net_info))
    findings.extend(detect_bad_pad_entry_findings(trace, net_info))
    findings.extend(detect_unnecessary_zigzag_findings(trace, net_info))
    findings.extend(detect_critical_detour_findings(trace, net_info))
    findings.extend(detect_keepout_crossing_findings(trace, net_info, keepouts))
    findings.extend(detect_unjustified_via_findings(trace, net_info))
    findings.extend(detect_width_mismatch_findings(trace, net_info))

    segments = trace.get("segments", [])
    direct = direct_length(trace)
    path_length = trace_length_mm(segments) if segments else 0.0
    return {
        "findings": findings,
        "hard_fail_statuses": sorted({finding["status"] for finding in findings}),
        "issue_codes": sorted({finding["issue_code"] for finding in findings}),
        "trace_length_mm": round(path_length, 3),
        "direct_length_mm": round(direct, 3),
        "length_ratio": round(path_length / direct, 3) if direct > 0 else None,
    }


def analyze_payload_geometry(payload: dict[str, Any]) -> dict[str, Any]:
    net_lookup = {item["name"]: item for item in normalized_nets(payload)}
    keepouts = get_keepouts(payload, {"RF_KEEPOUT", "ANTENNA_KEEPOUT"})
    trace_reports: list[dict[str, Any]] = []
    all_findings: list[dict[str, Any]] = []

    for trace in get_traces(payload):
        net_info = net_lookup.get(str(trace.get("net", "")), {})
        geometry = analyze_trace_geometry(trace, net_info, keepouts)
        report = {
            "trace_id": str(trace.get("id", "")),
            "net": str(trace.get("net", "")),
            "hard_fail_statuses": geometry["hard_fail_statuses"],
            "issue_codes": geometry["issue_codes"],
            "trace_length_mm": geometry["trace_length_mm"],
            "direct_length_mm": geometry["direct_length_mm"],
            "length_ratio": geometry["length_ratio"],
            "findings": geometry["findings"],
        }
        trace_reports.append(report)
        all_findings.extend(geometry["findings"])

    finding_counts: dict[str, int] = {}
    for status in HARD_FAIL_STATUSES:
        count = sum(1 for item in all_findings if item["status"] == status)
        if count:
            finding_counts[status] = count

    return {
        "trace_count": len(trace_reports),
        "trace_reports": trace_reports,
        "findings": all_findings,
        "hard_fail_statuses": sorted({item["status"] for item in all_findings}),
        "finding_counts": finding_counts,
    }


def detector_findings(payload: dict[str, Any], detector_key: str) -> list[dict[str, Any]]:
    net_lookup = {item["name"]: item for item in normalized_nets(payload)}
    keepouts = get_keepouts(payload, {"RF_KEEPOUT", "ANTENNA_KEEPOUT"})
    findings: list[dict[str, Any]] = []
    _, detector = GEOMETRY_DETECTORS[detector_key]
    for trace in get_traces(payload):
        net_info = net_lookup.get(str(trace.get("net", "")), {})
        if detector_key == "keepout_crossings":
            findings.extend(detector(trace, net_info, keepouts))
        else:
            findings.extend(detector(trace, net_info))
    return findings


def detector_result(payload: dict[str, Any], tool_name: str, findings: list[dict[str, Any]], status: str | None = None) -> dict[str, Any]:
    hard_fail_statuses = sorted({finding["status"] for finding in findings})
    result_status = status if status is not None else ("PASS" if not findings else "AUTO_BLOCKED_BAD_LAYOUT")
    return {
        "schema_version": "1.0",
        "tool": tool_name,
        "project": payload.get("project", ""),
        "status": result_status,
        "summary": {
            "trace_count": len(get_traces(payload)),
            "finding_count": len(findings),
            "hard_fail_status_count": len(hard_fail_statuses),
        },
        "hard_fail_statuses": hard_fail_statuses,
        "findings": findings,
    }


def markdown_for_result(title: str, result: dict[str, Any]) -> str:
    finding_rows = [
        [
            item["net"],
            item["status"],
            item["layer"],
            coordinates_text(item["segment_coordinates"]),
            item["reason"],
            item["recommended_fix"],
        ]
        for item in result.get("findings", [])
    ]
    return make_markdown(
        title,
        {
            "project": result.get("project", ""),
            "status": result.get("status", ""),
            "trace_count": result.get("summary", {}).get("trace_count", 0),
            "finding_count": result.get("summary", {}).get("finding_count", 0),
        },
        [
            (
                "Hard Fail Statuses",
                "\n".join(f"- {item}" for item in result.get("hard_fail_statuses", [])) if result.get("hard_fail_statuses") else "_none_",
            ),
            (
                "Findings",
                markdown_table(
                    ["net", "status", "layer", "segment_coordinates", "reason", "recommended_fix"],
                    finding_rows,
                ),
            ),
        ],
    )


def write_result(output_json: str | Path, result: dict[str, Any], markdown_path: str | Path | None = None, title: str | None = None) -> None:
    dump_json(output_json, result)
    if markdown_path:
        dump_markdown(markdown_path, markdown_for_result(title or result.get("tool", "Routing Geometry Quality"), result))
