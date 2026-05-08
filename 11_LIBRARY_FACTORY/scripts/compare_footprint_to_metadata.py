#!/usr/bin/env python3
"""Compare a KiCad footprint against simple package metadata.

This script is read-only and checks only machine-readable metadata fields. It
does not replace comparison to the manufacturer package drawing.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass
class Finding:
    severity: str
    code: str
    message: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def extract_pad_numbers(text: str) -> list[str]:
    return re.findall(r'\(pad\s+"?([^"\s()]+)"?', text)


def as_str_set(value: Any) -> set[str]:
    if value is None:
        return set()
    if isinstance(value, list):
        return {str(item) for item in value}
    return {str(value)}


def compare(footprint_path: Path, metadata_path: Path) -> dict:
    text = read_text(footprint_path)
    metadata = json.loads(read_text(metadata_path))
    pads = extract_pad_numbers(text)
    pad_set = set(pads)
    findings: list[Finding] = []

    expected_pad_count = metadata.get("expected_pad_count")
    if expected_pad_count is not None and int(expected_pad_count) != len(pads):
        findings.append(
            Finding(
                "WARN",
                "PAD_COUNT_MISMATCH",
                f"Expected {expected_pad_count} pads from metadata, found {len(pads)} pads in footprint.",
            )
        )

    expected_pad_numbers = as_str_set(metadata.get("expected_pad_numbers"))
    if expected_pad_numbers:
        missing = sorted(expected_pad_numbers - pad_set)
        extra = sorted(pad_set - expected_pad_numbers)
        if missing:
            findings.append(Finding("WARN", "MISSING_EXPECTED_PADS", f"Missing expected pads: {', '.join(missing)}."))
        if extra:
            findings.append(Finding("INFO", "EXTRA_PADS", f"Extra pads not listed in metadata: {', '.join(extra)}."))

    if metadata.get("pin1_required", True) and "1" not in pad_set:
        findings.append(Finding("WARN", "PIN1_MISSING", "Metadata requires pin 1, but pad `1` was not found."))

    layer_requirements = [
        ("requires_courtyard", ("F.CrtYd", "B.CrtYd"), "COURTYARD_REQUIRED", "Metadata requires courtyard geometry."),
        ("requires_fab", ("F.Fab", "B.Fab"), "FAB_REQUIRED", "Metadata requires fab-layer geometry."),
        ("requires_silkscreen", ("F.SilkS", "B.SilkS"), "SILKSCREEN_REQUIRED", "Metadata requires silkscreen geometry."),
    ]
    for key, tokens, code, message in layer_requirements:
        if metadata.get(key) and not any(token in text for token in tokens):
            findings.append(Finding("WARN", code, message))

    if metadata.get("requires_3d_model") and "(model " not in text:
        findings.append(Finding("WARN", "MODEL_REQUIRED", "Metadata requires a 3D model, but none was detected."))

    if metadata.get("connector_requires_exact_drawing") and not metadata.get("source_document"):
        findings.append(Finding("WARN", "CONNECTOR_SOURCE_MISSING", "Connector metadata requires exact drawing source, but source_document is blank."))

    if not metadata.get("source_document"):
        findings.append(Finding("WARN", "SOURCE_DOCUMENT_MISSING", "Metadata has no source_document."))

    summary = {
        "footprint_path": str(footprint_path),
        "metadata_path": str(metadata_path),
        "checked_at": datetime.now().isoformat(timespec="seconds"),
        "script_scope": "metadata comparison only; not package drawing approval",
        "metadata": metadata,
        "pad_count": len(pads),
        "pad_numbers": pads,
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
            "# Footprint Metadata Comparison Report",
            "",
            f"- Footprint: `{summary['footprint_path']}`",
            f"- Metadata: `{summary['metadata_path']}`",
            f"- Status: `{summary['status']}`",
            f"- Scope: {summary['script_scope']}",
            f"- Pad count: {summary['pad_count']}",
            "",
            "## Findings",
            "",
        ]
        if summary["findings"]:
            for finding in summary["findings"]:
                lines.append(f"- `{finding['severity']}` `{finding['code']}`: {finding['message']}")
        else:
            lines.append("- No metadata comparison findings.")
        lines.extend(
            [
                "",
                "## Review Note",
                "",
                "This script does not approve the footprint. Compare against the exact manufacturer package or connector drawing before use.",
            ]
        )
        markdown_report.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare a KiCad footprint to simple JSON package metadata.")
    parser.add_argument("--footprint", required=True, help="Path to .kicad_mod file.")
    parser.add_argument("--metadata", required=True, help="Path to package metadata JSON.")
    parser.add_argument("--markdown-report", help="Optional markdown report path.")
    parser.add_argument("--json-report", help="Optional JSON report path.")
    args = parser.parse_args()

    footprint_path = Path(args.footprint)
    metadata_path = Path(args.metadata)
    if not footprint_path.exists():
        raise SystemExit(f"Footprint file not found: {footprint_path}")
    if not metadata_path.exists():
        raise SystemExit(f"Metadata file not found: {metadata_path}")
    summary = compare(footprint_path, metadata_path)
    write_reports(
        summary,
        Path(args.markdown_report) if args.markdown_report else None,
        Path(args.json_report) if args.json_report else None,
    )
    print(json.dumps({"status": summary["status"], "findings": len(summary["findings"]), "footprint": summary["footprint_path"]}))
    return 1 if summary["status"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())

