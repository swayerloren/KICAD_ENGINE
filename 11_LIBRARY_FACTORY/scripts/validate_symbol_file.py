#!/usr/bin/env python3
"""Read-only KiCad symbol file validator.

This script performs basic structural checks only. It does not prove that a
symbol pinout is correct; datasheet/source review is still required.
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


def extract_properties(text: str) -> dict[str, str]:
    props: dict[str, str] = {}
    for name, value in re.findall(r'\(property\s+"([^"]+)"\s+"([^"]*)"', text):
        props[name] = value
    return props


def extract_pin_numbers(text: str) -> list[str]:
    return re.findall(r'\(number\s+"([^"]*)"', text)


def extract_pin_names(text: str) -> list[str]:
    return re.findall(r'\(name\s+"([^"]*)"', text)


def validate_symbol(path: Path) -> dict:
    findings: list[Finding] = []
    text = read_text(path)
    props = extract_properties(text)
    pin_numbers = extract_pin_numbers(text)
    pin_names = extract_pin_names(text)

    if path.suffix.lower() != ".kicad_sym":
        findings.append(Finding("WARN", "SYMBOL_EXTENSION", "File extension is not .kicad_sym."))
    if "(kicad_symbol_lib" not in text:
        findings.append(Finding("FAIL", "SYMBOL_LIB_HEADER", "Missing KiCad symbol library header."))
    if "(symbol " not in text:
        findings.append(Finding("FAIL", "SYMBOL_BLOCK", "No symbol block found."))
    if "(pin " not in text:
        findings.append(Finding("WARN", "NO_PINS", "No pin blocks found. Power symbols may be exceptions."))

    for required in ("Reference", "Value"):
        if required not in props:
            findings.append(Finding("WARN", f"MISSING_{required.upper()}_FIELD", f"Missing `{required}` property."))

    if "Datasheet" not in props or not props.get("Datasheet", "").strip():
        findings.append(Finding("WARN", "MISSING_DATASHEET_FIELD", "Missing or blank `Datasheet` property."))

    verification_fields = {"VerificationStatus", "SourceDocument", "SourceURL", "MPN", "Manufacturer"}
    if not verification_fields.intersection(props):
        findings.append(
            Finding(
                "WARN",
                "MISSING_VERIFICATION_FIELDS",
                "No verification/source fields found. Add source evidence before approval.",
            )
        )

    duplicates = sorted({pin for pin in pin_numbers if pin and pin_numbers.count(pin) > 1})
    for pin in duplicates:
        findings.append(Finding("WARN", "DUPLICATE_PIN_NUMBER", f"Pin number `{pin}` appears multiple times."))

    unnamed_count = sum(1 for name in pin_names if not name.strip())
    if unnamed_count:
        findings.append(Finding("WARN", "BLANK_PIN_NAME", f"{unnamed_count} pin name entries are blank."))

    if not any("power" in match.lower() for match in re.findall(r'\(pin\s+([a-zA-Z_]+)', text)):
        findings.append(Finding("INFO", "POWER_PIN_TYPE_NOT_DETECTED", "No explicit power pin type detected by basic scan."))

    summary = {
        "path": str(path),
        "checked_at": datetime.now().isoformat(timespec="seconds"),
        "script_scope": "basic structural checks only; not engineering approval",
        "symbol_count_estimate": text.count("(symbol "),
        "pin_number_count": len(pin_numbers),
        "unique_pin_number_count": len(set(pin_numbers)),
        "property_count": len(props),
        "properties": sorted(props.keys()),
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
            "# Symbol Validation Report",
            "",
            f"- Path: `{summary['path']}`",
            f"- Status: `{summary['status']}`",
            f"- Scope: {summary['script_scope']}",
            f"- Symbol count estimate: {summary['symbol_count_estimate']}",
            f"- Pin number count: {summary['pin_number_count']}",
            f"- Unique pin number count: {summary['unique_pin_number_count']}",
            f"- Property count: {summary['property_count']}",
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
                "This script does not verify pinout correctness. Compare every pin to the exact datasheet before approval.",
            ]
        )
        markdown_report.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a KiCad .kicad_sym file with basic read-only checks.")
    parser.add_argument("--symbol", required=True, help="Path to .kicad_sym file.")
    parser.add_argument("--markdown-report", help="Optional markdown report path.")
    parser.add_argument("--json-report", help="Optional JSON report path.")
    args = parser.parse_args()

    path = Path(args.symbol)
    if not path.exists():
        raise SystemExit(f"Symbol file not found: {path}")
    summary = validate_symbol(path)
    write_reports(
        summary,
        Path(args.markdown_report) if args.markdown_report else None,
        Path(args.json_report) if args.json_report else None,
    )
    print(json.dumps({"status": summary["status"], "findings": len(summary["findings"]), "path": summary["path"]}))
    return 1 if summary["status"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())

