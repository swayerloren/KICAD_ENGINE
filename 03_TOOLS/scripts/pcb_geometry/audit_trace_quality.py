#!/usr/bin/env python3
"""Run the full read-only PCB trace geometry audit pipeline."""

from __future__ import annotations

import argparse
from pathlib import Path

from _pcb_geometry_common import (
    aggregate_trace_quality_findings,
    audit_markdown,
    audit_result,
    build_geometry_payload,
    default_output_dir,
    default_overlay_paths,
    default_report_paths,
    default_tracks_paths,
    extraction_markdown,
    load_payload,
    power_loop_findings,
    render_svg_overlay,
    repo_rel,
    trace_angle_findings,
    usb_pair_findings,
    write_json_and_markdown,
    write_svg,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--project", help="Active project directory")
    source.add_argument("--pcb", help="Direct .kicad_pcb path")
    source.add_argument("--tracks-json", help="Existing extracted geometry JSON path")
    parser.add_argument("--output-dir", help="Optional output directory")
    args = parser.parse_args()

    if args.tracks_json:
        tracks_json_path = Path(args.tracks_json).resolve()
        output_dir = Path(args.output_dir).resolve() if args.output_dir else tracks_json_path.parent
        payload = load_payload(tracks_json_path)
        tracks_json = tracks_json_path
        tracks_md = output_dir / "tracks.md"
    else:
        target = args.project or args.pcb
        output_dir = Path(args.output_dir).resolve() if args.output_dir else default_output_dir(str(target))
        output_dir.mkdir(parents=True, exist_ok=True)
        tracks_json, tracks_md = default_tracks_paths(output_dir)
        payload = build_geometry_payload(str(target))
        write_json_and_markdown(tracks_json, payload, tracks_md, "PCB Geometry Track Extraction", extraction_markdown(payload))

    angle_json, angle_md = default_report_paths(output_dir, "trace_angles")
    power_json, power_md = default_report_paths(output_dir, "power_loop_geometry")
    usb_json, usb_md = default_report_paths(output_dir, "usb_pair_geometry")
    quality_json, quality_md = default_report_paths(output_dir, "trace_quality")
    overlay_svg, overlay_md = default_overlay_paths(output_dir)

    angle_result = audit_result(payload, "audit_trace_angles", trace_angle_findings(payload), "TRACE_ANGLES")
    power_result = audit_result(payload, "audit_power_loop_geometry", power_loop_findings(payload), "POWER_LOOP_GEOMETRY")
    usb_result = audit_result(payload, "audit_usb_pair_geometry", usb_pair_findings(payload), "USB_PAIR_GEOMETRY")
    usb_result["summary"]["usb_path_count"] = sum(1 for item in payload.get("traces", []) if item.get("usb", False))

    write_json_and_markdown(angle_json, angle_result, angle_md, "Trace Angle Audit")
    write_json_and_markdown(power_json, power_result, power_md, "Power Loop Geometry Audit")
    write_json_and_markdown(usb_json, usb_result, usb_md, "USB Pair Geometry Audit")

    quality_result = audit_result(payload, "audit_trace_quality", aggregate_trace_quality_findings(payload), "FULL_TRACE_GEOMETRY")
    quality_result["artifacts"] = {
        "tracks_json": repo_rel(tracks_json),
        "trace_angles_json": repo_rel(angle_json),
        "power_loop_geometry_json": repo_rel(power_json),
        "usb_pair_geometry_json": repo_rel(usb_json),
        "overlay_svg": repo_rel(overlay_svg),
    }
    quality_result["sub_audit_statuses"] = {
        "trace_angles": angle_result["status"],
        "power_loop_geometry": power_result["status"],
        "usb_pair_geometry": usb_result["status"],
    }
    write_json_and_markdown(quality_json, quality_result, quality_md, "Trace Quality Audit", audit_markdown("Trace Quality Audit", quality_result))

    write_svg(overlay_svg, render_svg_overlay(payload, quality_result))
    overlay_text = (
        "# Trace Quality Overlay\n\n"
        f"- project: `{quality_result.get('project', '')}`\n"
        f"- status: `{quality_result.get('status', '')}`\n"
        f"- finding_count: `{quality_result.get('summary', {}).get('finding_count', 0)}`\n"
        f"- overlay_svg: `{repo_rel(overlay_svg)}`\n"
    )
    overlay_md.parent.mkdir(parents=True, exist_ok=True)
    overlay_md.write_text(overlay_text, encoding="utf-8")

    print(f"TRACE_QUALITY_AUDIT_STATUS: {quality_result['status']}")
    print(f"TRACE_QUALITY_FINDING_COUNT: {quality_result.get('summary', {}).get('finding_count', 0)}")
    print(f"TRACE_QUALITY_REPORT_JSON: {quality_json.resolve()}")
    print(f"TRACE_QUALITY_REPORT_MD: {quality_md.resolve()}")
    return 0 if quality_result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
