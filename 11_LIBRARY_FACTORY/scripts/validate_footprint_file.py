#!/usr/bin/env python3
"""Read-only KiCad footprint file validator.

This script performs basic structural checks only. It does not prove that a
footprint matches a package drawing; human/source review is still required.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class Finding:
    severity: str
    code: str
    message: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def extract_pad_numbers(text: str) -> list[str]:
    return re.findall(r'\(pad\s+"?([^"\s()]+)"?', text)


def validate_footprint(path: Path) -> dict:
    findings: list[Finding] = []
    text = read_text(path)
    pads = extract_pad_numbers(text)
    layers = set(re.findall(r'\(layer\s+"?([^"\s()]+)"?', text))

    if path.suffix.lower() != ".kicad_mod":
        findings.append(Finding("WARN", "FOOTPRINT_EXTENSION", "File extension is not .kicad_mod."))
    if "(footprint " not in text:
        findings.append(Finding("FAIL", "FOOTPRINT_HEADER", "Missing KiCad footprint block."))
    if not pads:
        findings.append(Finding("WARN", "NO_PADS", "No pads found. Mechanical-only footprints may be exceptions."))
    if "1" not in pads and pads:
        findings.append(Finding("WARN", "PIN1_PAD_NOT_FOUND", "No pad numbered `1` found. Verify pin 1 convention."))

    if "F.CrtYd" not in text and "B.CrtYd" not in text:
        findings.append(Finding("WARN", "NO_COURTYARD", "No courtyard layer geometry detected."))
    if "F.Fab" not in text and "B.Fab" not in text:
        findings.append(Finding("WARN", "NO_FAB_LAYER", "No fab layer geometry detected."))
    if "F.SilkS" not in text and "B.SilkS" not in text:
        findings.append(Finding("WARN", "NO_SILKSCREEN", "No silkscreen layer geometry detected."))
    if "(model " not in text:
        findings.append(Finding("INFO", "NO_3D_MODEL", "No 3D model reference detected. This may be acceptable if documented."))
    if "pin 1" not in text.lower() and "pin1" not in text.lower():
        findings.append(Finding("INFO", "PIN1_MARKER_NOT_TEXT_DETECTED", "No text-based pin 1 marker detected by basic scan."))

    duplicate_pads = sorted({pad for pad in pads if pads.count(pad) > 1})
    for pad in duplicate_pads:
        findings.append(Finding("INFO", "DUPLICATE_PAD_NUMBER", f"Pad number `{pad}` appears multiple times. This may be normal for tied pads."))

    drill_count = text.count("(drill")
    smd_count = len(re.findall(r'\(pad\s+"?[^"\s()]+"?\s+smd\b', text))
    thru_hole_count = len(re.findall(r'\(pad\s+"?[^"\s()]+"?\s+thru_hole\b', text))

    summary = {
        "path": str(path),
        "checked_at": datetime.now().isoformat(timespec="seconds"),
        "script_scope": "basic structural checks only; not engineering approval",
        "pad_count": len(pads),
        "unique_pad_count": len(set(pads)),
        "pad_numbers": pads,
        "smd_pad_count": smd_count,
        "through_hole_pad_count": thru_hole_count,
        "drill_statement_count": drill_count,
        "layers_detected": sorted(layers),
        "status": "FAIL" if any(f.severity == "FAIL" for f in findings) else ("WARN" if any(f.severity == "WARN" for f in findings) else "PASS"),
        "findings": [asdict(f) for f in findings],
    }
    return summary


def write_reports(summary: dict, markdown_report: Path | None, json_report: Path | None) -> None:
    if json_report:
        json_report.parent.mkdir(parents=True, exist_ok=True)
        json_report.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    if markdown_report:
        markdown_report.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "# Footprint Validation Report",
            "",
            f"- Path: `{summary['path']}`",
            f"- Status: `{summary['status']}`",
            f"- Scope: {summary['script_scope']}",
            f"- Pad count: {summary['pad_count']}",
            f"- Unique pad count: {summary['unique_pad_count']}",
            f"- SMD pads: {summary['smd_pad_count']}",
            f"- Through-hole pads: {summary['through_hole_pad_count']}",
            f"- Drill statements: {summary['drill_statement_count']}",
            "",
            "## Findings",
            "",
        ]
        if summary["findings"]:
            for finding in summary["findings"]:
                lines.append(f"- `{finding['severity']}` `{finding['code']}`: {finding['message']}")
        else:
            lines.append("- No basic structural findings.")
        lines.extend(
            [
                "",
                "## Review Note",
                "",
                "This script does not verify package fit. Compare pads, drills, courtyard, fab outline, origin, and pin 1 orientation to the exact package drawing before approval.",
            ]
        )
        markdown_report.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a KiCad .kicad_mod file with basic read-only checks.")
    parser.add_argument("--footprint", required=True, help="Path to .kicad_mod file.")
    parser.add_argument("--markdown-report", help="Optional markdown report path.")
    parser.add_argument("--json-report", help="Optional JSON report path.")
    args = parser.parse_args()

    path = Path(args.footprint)
    if not path.exists():
        raise SystemExit(f"Footprint file not found: {path}")
    summary = validate_footprint(path)
    write_reports(
        summary,
        Path(args.markdown_report) if args.markdown_report else None,
        Path(args.json_report) if args.json_report else None,
    )
    print(json.dumps({"status": summary["status"], "findings": len(summary["findings"]), "path": summary["path"]}))
    return 1 if summary["status"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())

