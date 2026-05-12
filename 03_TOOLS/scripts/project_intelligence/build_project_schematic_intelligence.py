#!/usr/bin/env python3
"""Build a project-specific schematic intelligence layer from a KiCad schematic.

This script is read-only with respect to KiCad design artifacts. It parses the
saved schematic, collects current gate evidence, exports a fresh netlist, and
writes human-readable + machine-readable intelligence files under the target
project's ``schematic_intelligence`` folder.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT / "03_TOOLS" / "scripts" / "schematic_quality") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "03_TOOLS" / "scripts" / "schematic_quality"))

from schematic_quality_common import (  # type: ignore
    BLOCK_DEFINITIONS,
    assign_blocks,
    extract_symbols,
    extract_text_items,
    extract_wire_segments,
    heading_positions,
    is_physical_symbol,
    is_power_symbol,
    load_schematic,
)


TIMESTAMP = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

BLOCK_ORDER = [
    "input_power_protection",
    "buck_regulator",
    "esp32_module",
    "usb_c_data",
    "reset_boot",
    "leds",
    "test_debug",
    "mechanical_notes",
    "power_symbols_flags",
]

BLOCK_TITLE_MAP = {
    item["id"]: item["title"] for item in BLOCK_DEFINITIONS
}
BLOCK_TITLE_MAP["power_symbols_flags"] = "Power Symbols / Flags"

PLACEHOLDER_TOKENS = ("NEEDS_REVIEW", "BLOCKED", "TODO", "TBD", "UNVERIFIED", "?")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def save_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT.resolve())).replace("/", "\\")
    except ValueError:
        return str(path.resolve())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build project-specific schematic intelligence files.")
    parser.add_argument("--project", required=True, help="Absolute or repo-relative active project path.")
    return parser.parse_args()


def run_netlist_export(schematic: Path) -> Path:
    temp_dir = Path(tempfile.mkdtemp(prefix="schematic_intelligence_"))
    netlist_path = temp_dir / f"{schematic.stem}.net.xml"
    command = [
        "kicad-cli",
        "sch",
        "export",
        "netlist",
        "--format",
        "kicadxml",
        "--output",
        str(netlist_path),
        str(schematic),
    ]
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if completed.returncode != 0:
        raise RuntimeError(
            "kicad-cli netlist export failed:\n"
            f"stdout:\n{completed.stdout}\n"
            f"stderr:\n{completed.stderr}"
        )
    return netlist_path


def parse_netlist(path: Path) -> list[dict[str, Any]]:
    tree = ET.parse(path)
    root = tree.getroot()
    nets: list[dict[str, Any]] = []
    for net in root.findall("./nets/net"):
        code = net.get("code", "")
        name = net.get("name", "")
        nodes = []
        for node in net.findall("./node"):
            nodes.append(
                {
                    "reference": node.get("ref", ""),
                    "pin": node.get("pin", ""),
                    "pinfunction": node.get("pinfunction", ""),
                    "pintype": node.get("pintype", ""),
                }
            )
        refs = sorted({item["reference"] for item in nodes if item["reference"]})
        categories: list[str] = []
        lowered = name.lower()
        if "unconnected" in lowered:
            categories.append("unconnected")
        if name.upper() in {"GND", "+3V3", "+5V", "+5V_IN", "+5V_FUSED", "+5V_PROTECTED"} or lowered.startswith("/+"):
            categories.append("power")
        if any(token in lowered for token in ("usb", "dp", "dm", "cc1", "cc2", "shield")):
            categories.append("usb")
        if any(token in lowered for token in ("boot", "en", "u0rxd", "u0txd")):
            categories.append("control")
        nets.append(
            {
                "code": code,
                "name": name,
                "node_count": len(nodes),
                "references": refs,
                "nodes": nodes,
                "categories": categories,
            }
        )
    return sorted(nets, key=lambda item: (item["name"].lower(), item["code"]))


def symbol_sort_key(symbol: dict[str, Any]) -> tuple[str, str]:
    return (str(symbol.get("reference", "")), str(symbol.get("value", "")))


def sanitize_symbols(symbols: list[dict[str, Any]]) -> list[dict[str, Any]]:
    clean = []
    for symbol in symbols:
        clean.append(
            {
                "reference": symbol.get("reference", ""),
                "value": symbol.get("value", ""),
                "lib_id": symbol.get("lib_id", ""),
                "footprint": symbol.get("footprint", ""),
                "datasheet": symbol.get("datasheet", ""),
                "description": symbol.get("description", ""),
                "in_bom": symbol.get("in_bom", True),
                "on_board": symbol.get("on_board", True),
                "is_power_symbol": is_power_symbol(symbol),
                "is_physical_symbol": is_physical_symbol(symbol),
                "block_id": symbol.get("block_id", ""),
                "block_title": BLOCK_TITLE_MAP.get(symbol.get("block_id", ""), ""),
                "at": symbol.get("at", {}),
                "bbox": symbol.get("bbox", {}),
                "mirror": symbol.get("mirror", ""),
                "unit": symbol.get("unit", ""),
                "fields": {
                    field_name: field_meta.get("value", "")
                    for field_name, field_meta in symbol.get("properties", {}).items()
                },
            }
        )
    return sorted(clean, key=symbol_sort_key)


def classify_review_status(text: str) -> str:
    upper = str(text or "").upper()
    if any(token in upper for token in PLACEHOLDER_TOKENS):
        return "NEEDS_REVIEW"
    return "CLEAR"


def collect_block_members(symbols: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    members: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for symbol in symbols:
        block_id = symbol.get("block_id") or ""
        if is_power_symbol(symbol):
            members["power_symbols_flags"].append(symbol)
        elif block_id:
            members[block_id].append(symbol)
        else:
            members["unassigned"].append(symbol)
    return members


def compute_power_symbol_summary(symbols: list[dict[str, Any]]) -> dict[str, Any]:
    power_symbols = [symbol for symbol in symbols if is_power_symbol(symbol)]
    counts = Counter()
    refs: list[str] = []
    for symbol in power_symbols:
        reference = str(symbol.get("reference", ""))
        refs.append(reference)
        if reference.upper().startswith("#PWR"):
            counts["power_symbols"] += 1
        elif reference.upper().startswith("#FLG"):
            counts["power_flags"] += 1
        else:
            counts["other"] += 1
    return {
        "count": len(power_symbols),
        "counts_by_type": dict(counts),
        "references": sorted(refs),
    }


def build_review_items(
    symbols: list[dict[str, Any]],
    footprints_report: dict[str, Any],
    annotation_report: dict[str, Any],
    wire_report: dict[str, Any],
    block_report: dict[str, Any],
    text_overlap_report: dict[str, Any],
    footprint_gate_report_md: str,
    schematic_quality_report_md: str,
) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    seen_keys: set[tuple[str, str, str]] = set()

    def add_item(
        category: str,
        title: str,
        status: str,
        references: list[str] | None,
        evidence: str,
        auto_fix: str,
        next_action: str,
        source: str,
    ) -> None:
        refs = sorted({ref for ref in (references or []) if ref})
        key = (category, title, "|".join(refs))
        if key in seen_keys:
            return
        seen_keys.add(key)
        items.append(
            {
                "category": category,
                "title": title,
                "status": status,
                "references": refs,
                "evidence": evidence,
                "auto_fix": auto_fix,
                "next_action": next_action,
                "source": source,
            }
        )

    for symbol in symbols:
        reference = str(symbol.get("reference", ""))
        value = str(symbol.get("value", ""))
        footprint = str(symbol.get("footprint", ""))
        if is_physical_symbol(symbol) and not footprint:
            add_item(
                "footprint",
                "Blank footprint field",
                "FAIL",
                [reference],
                f"{reference} has no footprint field value in the saved schematic.",
                "AUTO_SAFE_AFTER_HUMAN_APPROVAL",
                "Assign an evidence-backed footprint and record it in the footprint lock.",
                "saved_schematic",
            )
        if classify_review_status(value) == "NEEDS_REVIEW":
            add_item(
                "needs_review",
                "Visible value contains review marker",
                "FAIL",
                [reference],
                f"{reference} value is `{value}`.",
                "TEXT_ONLY_SAFE_IF_EVIDENCE_ALREADY_EXISTS",
                "Resolve the underlying part/policy decision before cleaning the visible value.",
                "saved_schematic",
            )
        if "?" in reference:
            add_item(
                "annotation",
                "Unresolved annotation reference",
                "FAIL",
                [reference],
                f"{reference} still contains a question-mark placeholder.",
                "NATIVE_GUI_ONLY",
                "Use native KiCad GUI annotation, save in GUI, rerun ERC, then rescan.",
                "saved_schematic",
            )

    duplicate_refs = annotation_report.get("duplicate_references", [])
    for ref in duplicate_refs:
        add_item(
            "annotation",
            "Duplicate reference",
            "FAIL",
            [ref],
            f"Duplicate reference `{ref}` was reported by the annotation audit.",
            "NATIVE_GUI_ONLY",
            "Resolve with native KiCad annotation and verify the saved schematic.",
            "annotation.json",
        )

    annotation_status = annotation_report.get("native_annotation_status", {})
    if annotation_status.get("status") != "PASS":
        add_item(
            "annotation",
            "Native KiCad annotation not yet proven",
            "FAIL",
            [],
            annotation_status.get("reason", "Native GUI annotation evidence is missing."),
            "HUMAN_OR_GUI_AUTOMATION_REQUIRED",
            "Run the native annotation workflow, save through KiCad GUI, run GUI/ERC verification, and capture screenshots.",
            "annotation.json",
        )

    for finding in footprints_report.get("findings", []):
        if finding.get("status") == "FAIL":
            add_item(
                "footprint",
                finding.get("code", "FOOTPRINT_FAIL"),
                "FAIL",
                [finding.get("reference", "")] if finding.get("reference") else [],
                finding.get("message", ""),
                "EVIDENCE_FIRST",
                "Clear review markers, then populate the footprint lock with source and package proof.",
                "footprints.json",
            )

    for finding in wire_report.get("findings", []):
        if finding.get("status") == "WARN":
            add_item(
                "readability",
                finding.get("code", "WIRE_LABEL_WARN"),
                "WARN",
                [],
                finding.get("evidence", finding.get("message", "")),
                "AUTO_SAFE_PLANNING_ONLY",
                "Convert repeated local labels into direct local wiring during a controlled schematic cleanup pass.",
                "wire_vs_label.json",
            )

    for finding in block_report.get("findings", []):
        if finding.get("status") == "WARN":
            add_item(
                "layout",
                finding.get("code", "BLOCK_LAYOUT_WARN"),
                "WARN",
                [finding.get("reference", "")] if finding.get("reference") else [],
                finding.get("message", ""),
                "AUTO_SAFE_LAYOUT_PLAN_ONLY",
                "Use the schematic layout engine to re-block the page before further repair work.",
                "block_layout.json",
            )

    for finding in text_overlap_report.get("findings", []):
        if finding.get("status") in {"FAIL", "WARN"}:
            refs = []
            if finding.get("reference"):
                refs = re.split(r"[\s,/]+", str(finding["reference"]))
            add_item(
                "visual_overlap",
                finding.get("code", "TEXT_OVERLAP"),
                finding.get("status", "WARN"),
                refs,
                finding.get("message", ""),
                "AUTO_SAFE_IF_LAYOUT_ENGINE_REPOSITIONS_TEXT_ONLY",
                "Reposition text/value/reference fields after the block layout is stabilized.",
                "text_overlaps.json",
            )

    if "FOOTPRINT_LOCK.csv missing" in footprint_gate_report_md:
        add_item(
            "footprint_lock",
            "Footprint lock missing",
            "FAIL",
            [],
            "The footprint package gate report says `FOOTPRINT_LOCK.csv` is missing.",
            "DOCS_ONLY_SAFE",
            "Create a footprint lock file from actual selected parts and package evidence.",
            "FOOTPRINT_PACKAGE_GATE_REPORT.md",
        )

    if "Human visual proof: `FAIL`" in schematic_quality_report_md or "Human visual proof: FAIL" in schematic_quality_report_md:
        add_item(
            "visual_review",
            "Human visual readability gate failed",
            "FAIL",
            [],
            "The schematic quality gate still classifies human visual proof as failed.",
            "HUMAN_REVIEW_REQUIRED",
            "Inspect rendered pages/crops and then clean overlaps and block flow in a controlled edit pass.",
            "schematic_quality_report.md",
        )

    return sorted(items, key=lambda item: (item["status"], item["category"], ",".join(item["references"]), item["title"]))


def build_footprint_status(
    project_root: Path,
    physical_symbols: list[dict[str, Any]],
    footprint_report: dict[str, Any],
    footprint_gate_report_md: str,
) -> dict[str, Any]:
    blank_refs = []
    review_marker_refs = []
    for finding in footprint_report.get("findings", []):
        code = finding.get("code")
        reference = finding.get("reference", "")
        if code == "FOOTPRINT_BLANK":
            blank_refs.append(reference)
        if code == "VISIBLE_REVIEW_MARKER_IN_VALUE":
            review_marker_refs.append(reference)
    lock_path = project_root / "FOOTPRINT_LOCK.csv"
    lock_present = lock_path.exists()
    high_risk = [item["reference"] for item in physical_symbols if item.get("high_risk")]
    missing_source_link_refs = [item["reference"] for item in physical_symbols]
    return {
        "physical_symbol_count": len(physical_symbols),
        "blank_footprint_count": len(blank_refs),
        "blank_footprint_references": sorted(blank_refs),
        "visible_review_marker_count": len(review_marker_refs),
        "visible_review_marker_references": sorted(review_marker_refs),
        "high_risk_count": len(high_risk),
        "high_risk_references": sorted(high_risk),
        "footprint_lock_present": lock_present,
        "footprint_lock_path": relative(lock_path),
        "source_link_required_references": sorted(missing_source_link_refs),
        "status": "FAIL" if blank_refs or not lock_present or review_marker_refs else "PASS",
    }


def build_gate_inputs(
    schematic: Path,
    nets: list[dict[str, Any]],
    symbols: list[dict[str, Any]],
    quality_report: dict[str, Any],
    annotation_report: dict[str, Any],
    footprint_status: dict[str, Any],
    block_report: dict[str, Any],
    wire_report: dict[str, Any],
    text_overlap_report: dict[str, Any],
    footprint_gate_report_md: str,
) -> dict[str, Any]:
    unconnected_nets = [net["name"] for net in nets if "unconnected" in [c.lower() for c in net.get("categories", [])]]
    placeholder_refs = [symbol["reference"] for symbol in symbols if classify_review_status(symbol.get("value", "")) == "NEEDS_REVIEW"]
    return {
        "generated_at": TIMESTAMP,
        "schematic": relative(schematic),
        "symbol_count": len(symbols),
        "physical_symbol_count": len([item for item in symbols if is_physical_symbol(item)]),
        "power_symbol_count": len([item for item in symbols if is_power_symbol(item)]),
        "net_count": len(nets),
        "unconnected_net_count": len(unconnected_nets),
        "unconnected_nets": unconnected_nets,
        "placeholder_value_references": placeholder_refs,
        "annotation_saved_file_status": annotation_report.get("summary", {}).get("status"),
        "annotation_native_gui_status": annotation_report.get("native_annotation_status", {}).get("status", "FAIL"),
        "visual_readability_status": quality_report.get("human_visual", {}).get("status", "FAIL"),
        "erc_status": quality_report.get("erc", {}).get("status", "UNKNOWN"),
        "footprint_status": footprint_status["status"],
        "footprint_lock_present": footprint_status["footprint_lock_present"],
        "block_layout_status": block_report.get("summary", {}).get("status"),
        "wire_vs_label_status": wire_report.get("summary", {}).get("status"),
        "text_overlap_status": text_overlap_report.get("summary", {}).get("status"),
        "pcb_update_allowed": False,
        "schematic_repair_may_resume": True,
        "blocking_reasons": [
            "Native KiCad annotation not yet proven.",
            "Human visual readability gate has not passed.",
            "Footprint lock and package/source evidence are incomplete.",
            "High-risk review markers remain visible in the saved schematic.",
            "Schematic-to-PCB gate remains failed/blocked.",
        ],
        "footprint_gate_note": "FOOTPRINT_LOCK.csv missing" if not footprint_status["footprint_lock_present"] else "Footprint lock detected",
    }


def md_table(rows: list[list[str]]) -> str:
    if not rows:
        return "_None._"
    header = "| " + " | ".join(rows[0]) + " |"
    divider = "| " + " | ".join("---" for _ in rows[0]) + " |"
    body = ["| " + " | ".join(row) + " |" for row in rows[1:]]
    return "\n".join([header, divider, *body])


def build_human_docs(
    project_root: Path,
    output_root: Path,
    schematic: Path,
    symbols: list[dict[str, Any]],
    block_members: dict[str, list[dict[str, Any]]],
    nets: list[dict[str, Any]],
    power_summary: dict[str, Any],
    review_items: list[dict[str, Any]],
    footprint_status: dict[str, Any],
    gate_inputs: dict[str, Any],
    reports: dict[str, dict[str, Any]],
) -> dict[str, str]:
    physical_symbols = [item for item in symbols if is_physical_symbol(item)]
    placeholder_symbols = [item for item in physical_symbols if classify_review_status(item.get("value", "")) == "NEEDS_REVIEW"]
    top_nets = sorted(nets, key=lambda item: (-item["node_count"], item["name"].lower()))[:12]

    block_rows = [["Block", "Refs", "Count", "Notes"]]
    for block_id in BLOCK_ORDER:
        members = block_members.get(block_id, [])
        refs = ", ".join(item["reference"] for item in sorted(members, key=symbol_sort_key)) or "-"
        notes = ""
        if block_id == "power_symbols_flags":
            notes = f"{power_summary['count']} power symbols/flags"
        elif block_id == "usb_c_data":
            notes = "Contains connector, CC resistors, ESD, and USB series resistors."
        elif block_id == "test_debug":
            notes = "Includes UART/test pads and service access points."
        block_rows.append([BLOCK_TITLE_MAP[block_id], refs, str(len(members)), notes])

    review_rows = [["Category", "Title", "Status", "Refs", "Auto-fix", "Next action"]]
    for item in review_items:
        review_rows.append([
            item["category"],
            item["title"],
            item["status"],
            ", ".join(item["references"]) or "-",
            item["auto_fix"],
            item["next_action"],
        ])

    net_rows = [["Net", "Nodes", "Refs", "Category"]]
    for net in top_nets:
        net_rows.append([
            net["name"],
            str(net["node_count"]),
            ", ".join(net["references"][:6]) + (" ..." if len(net["references"]) > 6 else ""),
            ", ".join(net["categories"]) or "-",
        ])

    footprint_rows = [["Metric", "Value"]]
    for key in (
        "physical_symbol_count",
        "blank_footprint_count",
        "visible_review_marker_count",
        "high_risk_count",
    ):
        footprint_rows.append([key, str(footprint_status[key])])
    footprint_rows.append(["footprint_lock_present", "YES" if footprint_status["footprint_lock_present"] else "NO"])
    footprint_rows.append(["footprint_lock_path", footprint_status["footprint_lock_path"]])

    annotation_findings = reports["annotation"].get("native_annotation_status", {})
    docs: dict[str, str] = {}
    docs["README.md"] = f"""# ESP32_CSI_WIFI_NODE Schematic Intelligence

Status: `READ_ONLY_PROJECT_INTELLIGENCE`

This folder records project-specific schematic knowledge for `ESP32_CSI_WIFI_NODE` before any further schematic repair or schematic-to-PCB work. It is generated from the saved schematic plus current gate evidence and does not modify KiCad design files.

## Inputs

- Project root: `{relative(project_root)}`
- Schematic: `{relative(schematic)}`
- Schematic quality report: `{relative(project_root / "reports" / "schematic_quality" / "20260510_104847" / "schematic_quality_report.json")}`
- Footprint package gate report: `{relative(project_root / "reports" / "footprint_package" / "20260510_115257" / "FOOTPRINT_PACKAGE_GATE_REPORT.md")}`
- Generated at: `{TIMESTAMP}`

## Current Summary

- Physical components documented: `{len(physical_symbols)}`
- Power symbols / flags documented: `{power_summary['count']}`
- Nets documented: `{len(nets)}`
- Functional blocks documented: `{len([block for block in BLOCK_ORDER if block_members.get(block)])}`
- Placeholder or `NEEDS_REVIEW` values still visible: `{len(placeholder_symbols)}`
- Annotation native GUI proof: `{annotation_findings.get('status', 'FAIL')}`
- Footprint lock present: `{"YES" if footprint_status["footprint_lock_present"] else "NO"}`
- Schematic-to-PCB update allowed: `NO`

Use [INDEX.md](INDEX.md) as the entry point for the detailed human-readable and machine-readable artifacts.
"""

    docs["INDEX.md"] = f"""# Schematic Intelligence Index

## Human-Readable Files

- [FUNCTIONAL_BLOCK_MAP.md](FUNCTIONAL_BLOCK_MAP.md)
- [SCHEMATIC_FLOW_PLAN.md](SCHEMATIC_FLOW_PLAN.md)
- [WIRE_VS_LABEL_PLAN.md](WIRE_VS_LABEL_PLAN.md)
- [ANNOTATION_STATUS.md](ANNOTATION_STATUS.md)
- [FOOTPRINT_ASSIGNMENT_STATUS.md](FOOTPRINT_ASSIGNMENT_STATUS.md)
- [ELECTRICAL_POLICY_DECISIONS.md](ELECTRICAL_POLICY_DECISIONS.md)
- [SOURCE_LINK_REQUIREMENTS.md](SOURCE_LINK_REQUIREMENTS.md)
- [NEEDS_REVIEW_REGISTER.md](NEEDS_REVIEW_REGISTER.md)
- [SCHEMATIC_VISUAL_CLEANUP_PLAN.md](SCHEMATIC_VISUAL_CLEANUP_PLAN.md)
- [SCHEMATIC_TO_PCB_GATE_INPUTS.md](SCHEMATIC_TO_PCB_GATE_INPUTS.md)
- [SCHEMATIC_REPAIR_SEQUENCE.md](SCHEMATIC_REPAIR_SEQUENCE.md)

## Machine-Readable Files

- [machine_readable/symbols.json](machine_readable/symbols.json)
- [machine_readable/nets.json](machine_readable/nets.json)
- [machine_readable/blocks.json](machine_readable/blocks.json)
- [machine_readable/review_items.json](machine_readable/review_items.json)
- [machine_readable/footprint_status.json](machine_readable/footprint_status.json)
- [machine_readable/schematic_gate_inputs.json](machine_readable/schematic_gate_inputs.json)
"""

    docs["FUNCTIONAL_BLOCK_MAP.md"] = f"""# Functional Block Map

{md_table(block_rows)}

## Power Symbol / Flag Count

- Total power symbols / flags: `{power_summary['count']}`
- `#PWR*`: `{power_summary['counts_by_type'].get('power_symbols', 0)}`
- `#FLG*`: `{power_summary['counts_by_type'].get('power_flags', 0)}`
"""

    docs["SCHEMATIC_FLOW_PLAN.md"] = """# Schematic Flow Plan

## Current Read Order

1. Input power / protection at the left.
2. Buck regulator near upper center-left.
3. ESP32 module in the center.
4. USB-C / ESD / CC / data block at the upper-right.
5. Reset / boot below the power / module region.
6. LEDs at lower-left.
7. Test / debug pads at the right edge.
8. Mechanical / mounting notes at lower-center.

## Current Problems

- The block-layout audit reports `BLOCK_FLOW_DISORDERED`.
- The USB-C block is visually separated from the module enough to require several label hops.
- Test/debug content is label-heavy and competes with the main signal path.

## Target Flow

1. Keep input power and protection on the far left.
2. Keep the buck regulator immediately downstream of input power.
3. Keep the ESP32 module as the page anchor in the center/right.
4. Keep USB-C data, ESD, and CC clustered as one local-wired block feeding the ESP32 USB pins.
5. Keep reset / boot adjacent to the relevant ESP32 pins, with short local wiring.
6. Keep LEDs grouped and visually subordinate to the main power/data path.
7. Keep test pads in one service/debug block off the main signal path.
8. Keep mechanical notes and mounting holes separated from active circuitry.
"""

    docs["WIRE_VS_LABEL_PLAN.md"] = f"""# Wire Vs Label Plan

## Current Audit Status

- Audit status: `{reports["wire"].get("summary", {}).get("status", "WARN")}`

## Current Readability Warnings

{md_table([["Finding", "Evidence"]] + [[item.get("code", ""), item.get("evidence", item.get("message", ""))] for item in reports["wire"].get("findings", []) if item.get("status") == "WARN"])}

## Safe Automatic Cleanup Candidates

- Replace repeated local labels inside the ESP32, USB-C, reset/boot, and test/debug blocks with direct wires where the connection stays within the same block.
- Preserve power-rail labels and true cross-block labels.
- Delay any semantic net renames until source evidence and project review are complete.

## Human / Evidence Required

- USB power and shield policy labels.
- Any connector or module net naming tied to datasheet/package proof.
- Any cleanup that changes block membership or signal intent rather than only readability.
"""

    docs["ANNOTATION_STATUS.md"] = f"""# Annotation Status

## Saved Schematic Scan

- Annotation audit status: `{reports["annotation"].get("summary", {}).get("status", "UNKNOWN")}`
- Duplicate references: `{len(reports["annotation"].get("duplicate_references", []))}`
- Unresolved `?` references in saved schematic: `{len(reports["annotation"].get("question_mark_references", []))}`

## Native KiCad GUI Proof

- Native GUI status: `{annotation_findings.get("status", "FAIL")}`
- Reason: `{annotation_findings.get("reason", "Missing native GUI annotation proof.")}`

## Decision

Saved-file parsing is not enough to declare annotation complete. Future repair work may continue, but schematic-to-PCB update remains blocked until the native KiCad annotation workflow is executed and saved through the GUI.
"""

    docs["FOOTPRINT_ASSIGNMENT_STATUS.md"] = f"""# Footprint Assignment Status

{md_table(footprint_rows)}

## Current Footprint Findings

- Blank footprints in saved schematic: `{footprint_status["blank_footprint_count"]}`
- Visible review-marker values tied to footprint verification: `{", ".join(footprint_status["visible_review_marker_references"]) or "none"}`
- High-risk footprint references: `{", ".join(footprint_status["high_risk_references"])}`.
- Footprint lock file present: `{"YES" if footprint_status["footprint_lock_present"] else "NO"}`

## Decision

Do not move to PCB update. The saved schematic has populated footprint fields, but the footprint proof system is incomplete because the lock file, source links, package drawing proof, and high-risk review evidence are still missing.
"""

    docs["ELECTRICAL_POLICY_DECISIONS.md"] = """# Electrical Policy Decisions

## Current Accepted Planning Decisions

- External 5 V DC barrel supply remains the main power input.
- Reverse-polarity protection remains required before the 3.3 V regulator.
- The board uses a buck regulator for the 3.3 V rail.
- Native ESP32-S3 USB remains the intended USB data path.
- The project keeps external-antenna ESP32-S3-WROOM-1U class requirements.

## Unresolved Policy Decisions

- USB VBUS backfeed / sense policy is still unresolved.
- USB shield / EMC strategy is still unresolved.
- Exact PMOS orientation and protection policy still need proof.
- Final connector mechanical assumptions still need proof.

## Engineering Consequence

These are not cosmetic issues. They affect connector choice, net naming, orientation proof, footprint lock content, and the schematic-to-PCB gate.
"""

    docs["SOURCE_LINK_REQUIREMENTS.md"] = f"""# Source Link Requirements

Every physical symbol needs a source link or datasheet reference in the future footprint lock and parts review evidence.

## Immediate Priority References

- High-risk parts first: `{", ".join(footprint_status["high_risk_references"])}`
- All physical parts still require source-link capture in the new proof engine.

## Minimum Evidence Per Part

1. Manufacturer part number or approved generic package decision.
2. Datasheet or authoritative source URL.
3. Package drawing review status.
4. Pin mapping review status for polarity-sensitive or functional devices.
5. Connector orientation proof where relevant.
"""

    docs["NEEDS_REVIEW_REGISTER.md"] = f"""# Needs Review Register

{md_table(review_rows)}
"""

    docs["SCHEMATIC_VISUAL_CLEANUP_PLAN.md"] = f"""# Schematic Visual Cleanup Plan

## Current Visual Status

- Schematic readability status: `{reports["quality"].get("readability_status", "UNKNOWN")}`
- Human visual gate: `{reports["quality"].get("human_visual", {}).get("status", "FAIL")}`
- Text-overlap audit: `{reports["text_overlaps"].get("summary", {}).get("status", "FAIL")}`

## Known Visual Defects

{md_table([["Finding", "Refs", "Status"]] + [[item.get("code", ""), item.get("reference", ""), item.get("status", "")] for item in reports["text_overlaps"].get("findings", [])])}

## Safe Automatic Cleanup

- Reposition reference/value text that overlaps wires, symbols, or labels.
- Rebuild local wiring inside a block without changing net meaning.
- Regroup symbols inside the same functional block to restore whitespace and left-to-right readability.

## Human / Evidence Required

- Any cleanup that changes connector orientation assumptions.
- Any part substitution, value decision, or net-policy change.
- Any action that depends on unresolved USB, PMOS, shield, or mechanical policy.
"""

    docs["SCHEMATIC_TO_PCB_GATE_INPUTS.md"] = f"""# Schematic To PCB Gate Inputs

## Current Gate Summary

- ERC status: `{gate_inputs["erc_status"]}`
- Native annotation status: `{gate_inputs["annotation_native_gui_status"]}`
- Visual readability status: `{gate_inputs["visual_readability_status"]}`
- Footprint proof status: `{gate_inputs["footprint_status"]}`
- Block-layout status: `{gate_inputs["block_layout_status"]}`
- Wire-vs-label status: `{gate_inputs["wire_vs_label_status"]}`
- Text-overlap status: `{gate_inputs["text_overlap_status"]}`
- Unconnected nets in saved schematic export: `{gate_inputs["unconnected_net_count"]}`

## Current Decision

- Schematic repair may resume: `YES`
- PCB update allowed: `NO`

## Blocking Reasons

{chr(10).join(f"- {reason}" for reason in gate_inputs["blocking_reasons"])}
"""

    docs["SCHEMATIC_REPAIR_SEQUENCE.md"] = """# Schematic Repair Sequence

## Recommended Next Sequence

1. Lock project-specific schematic intelligence as the working context for future repairs.
2. Resolve source-link / MPN / package proof for high-risk parts and create the footprint lock.
3. Run the native KiCad annotation workflow and save through the GUI.
4. Use the schematic layout / cleanup engine to fix block flow, local wire usage, and text overlaps.
5. Clear visible `NEEDS_REVIEW` markers only after the underlying evidence exists.
6. Rerun schematic quality, footprint package, and annotation gates.
7. Re-evaluate schematic-to-PCB readiness.

## Stop Conditions

- Stop before any PCB update while the footprint lock is missing.
- Stop before any PCB update while native annotation is not proven.
- Stop before any PCB update while visual readability still fails.
"""

    return docs


def main() -> int:
    args = parse_args()
    project_root = (Path(args.project) if Path(args.project).is_absolute() else (REPO_ROOT / args.project)).resolve()
    if not project_root.exists():
        raise SystemExit(f"Project path not found: {project_root}")

    schematic = project_root / "kicad" / "ESP32_CSI_WIFI_NODE.kicad_sch"
    output_root = project_root / "schematic_intelligence"
    machine_root = output_root / "machine_readable"

    quality_report_dir = project_root / "reports" / "schematic_quality" / "20260510_104847"
    footprint_report_dir = project_root / "reports" / "footprint_package" / "20260510_115257"

    root = load_schematic(schematic)
    raw_symbols = extract_symbols(root)
    text_items = extract_text_items(root, raw_symbols)
    headings = heading_positions(text_items)
    blocks, _unassigned = assign_blocks(raw_symbols, headings)
    wire_segments = extract_wire_segments(root)

    symbols = sanitize_symbols(raw_symbols)
    block_members = collect_block_members(raw_symbols)
    power_summary = compute_power_symbol_summary(raw_symbols)

    netlist_path = run_netlist_export(schematic)
    nets = parse_netlist(netlist_path)

    reports = {
        "quality": load_json(quality_report_dir / "schematic_quality_report.json"),
        "annotation": load_json(quality_report_dir / "annotation.json"),
        "footprints": load_json(quality_report_dir / "footprints.json"),
        "text_overlaps": load_json(quality_report_dir / "text_overlaps.json"),
        "block": load_json(quality_report_dir / "block_layout.json"),
        "wire": load_json(quality_report_dir / "wire_vs_label.json"),
        "physical_symbols": load_json(footprint_report_dir / "physical_symbols.json"),
    }

    footprint_gate_report_md = (footprint_report_dir / "FOOTPRINT_PACKAGE_GATE_REPORT.md").read_text(encoding="utf-8")
    schematic_quality_report_md = (quality_report_dir / "schematic_quality_report.md").read_text(encoding="utf-8")

    physical_symbols = reports["physical_symbols"]["symbols"]
    review_items = build_review_items(
        raw_symbols,
        reports["footprints"],
        reports["annotation"],
        reports["wire"],
        reports["block"],
        reports["text_overlaps"],
        footprint_gate_report_md,
        schematic_quality_report_md,
    )
    footprint_status = build_footprint_status(project_root, physical_symbols, reports["footprints"], footprint_gate_report_md)
    gate_inputs = build_gate_inputs(
        schematic,
        nets,
        raw_symbols,
        reports["quality"],
        reports["annotation"],
        footprint_status,
        reports["block"],
        reports["wire"],
        reports["text_overlaps"],
        footprint_gate_report_md,
    )

    machine_blocks = {}
    for block_id in BLOCK_ORDER:
        if block_id == "power_symbols_flags":
            members = block_members.get(block_id, [])
            machine_blocks[block_id] = {
                "block_id": block_id,
                "title": BLOCK_TITLE_MAP[block_id],
                "symbol_count": len(members),
                "references": [item.get("reference", "") for item in sorted(members, key=symbol_sort_key)],
                "audit_bbox": {},
                "audit_centroid": {},
            }
            continue
        audit_meta = reports["block"].get("blocks", {}).get(block_id, {})
        members = block_members.get(block_id, [])
        machine_blocks[block_id] = {
            "block_id": block_id,
            "title": BLOCK_TITLE_MAP[block_id],
            "symbol_count": len(members),
            "references": [item.get("reference", "") for item in sorted(members, key=symbol_sort_key)],
            "audit_bbox": audit_meta.get("bbox", {}),
            "audit_centroid": audit_meta.get("centroid", {}),
            "heading_text": audit_meta.get("heading_text", ""),
        }

    docs = build_human_docs(
        project_root=project_root,
        output_root=output_root,
        schematic=schematic,
        symbols=raw_symbols,
        block_members=block_members,
        nets=nets,
        power_summary=power_summary,
        review_items=review_items,
        footprint_status=footprint_status,
        gate_inputs=gate_inputs,
        reports=reports,
    )

    for relative_name, contents in docs.items():
        save_text(output_root / relative_name, contents)

    save_json(machine_root / "symbols.json", {
        "generated_at": TIMESTAMP,
        "schematic": relative(schematic),
        "symbol_count": len(symbols),
        "symbols": symbols,
    })
    save_json(machine_root / "nets.json", {
        "generated_at": TIMESTAMP,
        "schematic": relative(schematic),
        "net_count": len(nets),
        "nets": nets,
    })
    save_json(machine_root / "blocks.json", {
        "generated_at": TIMESTAMP,
        "schematic": relative(schematic),
        "blocks": machine_blocks,
    })
    save_json(machine_root / "review_items.json", {
        "generated_at": TIMESTAMP,
        "review_item_count": len(review_items),
        "review_items": review_items,
    })
    save_json(machine_root / "footprint_status.json", footprint_status)
    save_json(machine_root / "schematic_gate_inputs.json", gate_inputs)

    print(f"SCHEMATIC_INTELLIGENCE_WRITTEN: {output_root}")
    print(f"SYMBOL_COUNT: {len(symbols)}")
    print(f"PHYSICAL_SYMBOL_COUNT: {footprint_status['physical_symbol_count']}")
    print(f"NET_COUNT: {len(nets)}")
    print(f"REVIEW_ITEM_COUNT: {len(review_items)}")
    print(f"UNCONNECTED_NET_COUNT: {gate_inputs['unconnected_net_count']}")
    print(f"FOOTPRINT_LOCK_PRESENT: {footprint_status['footprint_lock_present']}")
    print(f"PCB_UPDATE_ALLOWED: {gate_inputs['pcb_update_allowed']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
