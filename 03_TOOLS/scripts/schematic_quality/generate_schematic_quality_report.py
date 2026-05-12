#!/usr/bin/env python3
"""Render a combined schematic-quality JSON result into Markdown."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def markdown_report(data: dict[str, Any]) -> str:
    lines = [
        "# Schematic Quality Report",
        "",
        f"Gate status: `{data.get('gate_status', 'UNKNOWN')}`",
        "",
        f"Generated: `{data.get('generated_at', '')}`",
        f"Project: `{data.get('project', '')}`",
        f"Schematic: `{data.get('schematic', '')}`",
        "",
        "## Gate Summary",
        "",
        f"- Readability status: `{data.get('readability_status', 'UNKNOWN')}`",
        f"- Native annotation proof: `{data.get('native_annotation', {}).get('status', 'UNKNOWN')}`",
        f"- ERC proof: `{data.get('erc', {}).get('status', 'UNKNOWN')}`",
        f"- Human visual proof: `{data.get('human_visual', {}).get('status', 'UNKNOWN')}`",
        "",
        "## Audit Status Table",
        "",
        "| Audit | Status | Pass | Warn | Fail |",
        "| --- | --- | --- | --- | --- |",
    ]
    for audit_name, audit_data in data.get("audits", {}).items():
        summary = audit_data.get("summary", {})
        counts = summary.get("counts", {})
        lines.append(
            f"| `{audit_name}` | `{summary.get('status', 'UNKNOWN')}` | {counts.get('PASS', 0)} | {counts.get('WARN', 0)} | {counts.get('FAIL', 0)} |"
        )
    lines.extend(["", "## Gate Findings", ""])
    for finding in data.get("gate_findings", []):
        lines.append(
            "- `{status}` `{code}`: {message} `{evidence}`".format(
                status=finding.get("status", ""),
                code=finding.get("code", ""),
                message=finding.get("message", ""),
                evidence=finding.get("evidence", ""),
            )
        )
    lines.extend(
        [
            "",
            "## Output Files",
            "",
        ]
    )
    for label, value in sorted(data.get("output_files", {}).items()):
        lines.append(f"- `{label}`: `{value}`")
    lines.extend(
        [
            "",
            "## Rule",
            "",
            "Do not treat ERC alone as schematic readiness proof. Native annotation, footprint readiness, and human-readable visual flow must all pass before PCB update.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a combined schematic-quality JSON file into Markdown.")
    parser.add_argument("--input-json", required=True, help="Combined schematic-quality JSON path.")
    parser.add_argument("--output", required=True, help="Markdown output path.")
    args = parser.parse_args()

    input_path = Path(args.input_json)
    output_path = Path(args.output)
    data = json.loads(input_path.read_text(encoding="utf-8"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown_report(data), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
