#!/usr/bin/env python3
"""Audit functional-block flow against the schematic layout template."""

from __future__ import annotations

from pathlib import Path

from schematic_layout_common import (
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    CHECK_STATUS_WARN,
    LAYOUT_TEMPLATE_ESP32_DEV_BOARD,
    common_parser,
    load_layout_context,
    rect_distance,
    resolve_project_and_schematic,
    write_markdown_and_json,
)


def finding(status: str, code: str, message: str, evidence: str = "") -> dict[str, str]:
    return {"status": status, "code": code, "message": message, "evidence": evidence}


def run_audit(schematic: Path) -> dict:
    context = load_layout_context(schematic)
    template = LAYOUT_TEMPLATE_ESP32_DEV_BOARD
    findings: list[dict[str, str]] = []

    for block_id, rules in template["blocks"].items():
        block = context["blocks"][block_id]
        region = context["block_regions"][block_id]
        if block["symbol_count"] == 0:
            severity = CHECK_STATUS_FAIL if block_id in {"input_power_protection", "buck_regulator", "esp32_module", "usb_c_data", "reset_boot"} else CHECK_STATUS_WARN
            findings.append(finding(severity, "BLOCK_MISSING", f"Functional block is missing or empty: {block['title']}.", block_id))
            continue
        if region["horizontal"] in rules["allowed_horizontal"] and region["vertical"] in rules["allowed_vertical"]:
            findings.append(finding(CHECK_STATUS_PASS, "BLOCK_REGION_OK", f"Block is in an acceptable region: {block['title']}.", region["region"]))
        else:
            findings.append(
                finding(
                    CHECK_STATUS_WARN,
                    "BLOCK_REGION_OFF_TEMPLATE",
                    f"Block is present but not in the preferred template region: {block['title']}.",
                    f"current={region['region']} desired={rules['desired_region']}",
                )
            )

    input_block = context["blocks"]["input_power_protection"]
    buck_block = context["blocks"]["buck_regulator"]
    esp_block = context["blocks"]["esp32_module"]
    if input_block["symbol_count"] and buck_block["symbol_count"] and esp_block["symbol_count"]:
        input_x = input_block["centroid"]["x"]
        buck_x = buck_block["centroid"]["x"]
        esp_x = esp_block["centroid"]["x"]
        if input_x <= buck_x <= esp_x:
            findings.append(finding(CHECK_STATUS_PASS, "POWER_FLOW_LEFT_TO_RIGHT", "Power flow reads left-to-right from input to regulator to ESP32."))
        else:
            findings.append(
                finding(
                    CHECK_STATUS_FAIL,
                    "POWER_FLOW_DISORDERED",
                    "Input, buck, and ESP32 blocks do not read in a clean left-to-right order.",
                    f"input_x={input_x:.2f}, buck_x={buck_x:.2f}, esp_x={esp_x:.2f}",
                )
            )
        spacing = rect_distance(input_block["bbox"], buck_block["bbox"])
        if spacing <= 25.0:
            findings.append(finding(CHECK_STATUS_PASS, "BUCK_NEAR_INPUT", "Buck regulator block is near the input power block.", f"{spacing:.2f} mm"))
        elif spacing <= 40.0:
            findings.append(finding(CHECK_STATUS_WARN, "BUCK_NEAR_INPUT_WARN", "Buck regulator block is farther from the input block than preferred.", f"{spacing:.2f} mm"))
        else:
            findings.append(finding(CHECK_STATUS_FAIL, "BUCK_TOO_FAR_FROM_INPUT", "Buck regulator block is too far from the input power block.", f"{spacing:.2f} mm"))

    usb_block = context["blocks"]["usb_c_data"]
    reset_block = context["blocks"]["reset_boot"]
    if usb_block["symbol_count"]:
        usb_region = context["block_regions"]["usb_c_data"]
        if usb_region["vertical"] == "lower":
            findings.append(finding(CHECK_STATUS_PASS, "USB_BLOCK_LOW_ENOUGH", "USB block is in a lower review-friendly region.", usb_region["region"]))
        else:
            findings.append(finding(CHECK_STATUS_WARN, "USB_BLOCK_NOT_LOW", "USB block is not in the preferred lower region.", usb_region["region"]))
    if reset_block["symbol_count"] and esp_block["symbol_count"]:
        spacing = rect_distance(reset_block["bbox"], esp_block["bbox"])
        if spacing <= 25.0:
            findings.append(finding(CHECK_STATUS_PASS, "RESET_BOOT_NEAR_ESP32", "Reset/boot block is near the ESP32 block.", f"{spacing:.2f} mm"))
        elif spacing <= 40.0:
            findings.append(finding(CHECK_STATUS_WARN, "RESET_BOOT_NEAR_ESP32_WARN", "Reset/boot block is a little far from the ESP32 block.", f"{spacing:.2f} mm"))
        else:
            findings.append(finding(CHECK_STATUS_FAIL, "RESET_BOOT_TOO_FAR", "Reset/boot block is too far from the ESP32 block.", f"{spacing:.2f} mm"))

    unassigned = [symbol.get("reference", "") for symbol in context["unassigned_symbols"] if symbol.get("reference")]
    if not unassigned:
        findings.append(finding(CHECK_STATUS_PASS, "NO_SYMBOL_EXPLOSION", "Symbols are assigned into recognizable blocks."))
    elif len(unassigned) <= 4:
        findings.append(finding(CHECK_STATUS_WARN, "UNASSIGNED_SYMBOLS_WARN", "Some symbols are not cleanly grouped into blocks.", ", ".join(unassigned)))
    else:
        findings.append(finding(CHECK_STATUS_FAIL, "SYMBOL_EXPLOSION", "Too many symbols are visually detached from functional blocks.", ", ".join(unassigned)))

    pass_count = sum(1 for item in findings if item["status"] == CHECK_STATUS_PASS)
    warn_count = sum(1 for item in findings if item["status"] == CHECK_STATUS_WARN)
    fail_count = sum(1 for item in findings if item["status"] == CHECK_STATUS_FAIL)
    status = CHECK_STATUS_FAIL if fail_count else CHECK_STATUS_WARN if warn_count else CHECK_STATUS_PASS
    return {
        "generated_at": context["generated_at"],
        "schematic": context["schematic"],
        "audit_id": "visual_flow",
        "title": "Schematic Visual Flow Audit",
        "status": status,
        "counts": {"PASS": pass_count, "WARN": warn_count, "FAIL": fail_count},
        "findings": findings,
        "block_regions": context["block_regions"],
    }


def markdown(result: dict) -> str:
    lines = [
        "# Schematic Visual Flow Audit",
        "",
        f"Status: `{result['status']}`",
        "",
        f"Generated: `{result['generated_at']}`",
        f"Schematic: `{result['schematic']}`",
        "",
        "## Findings",
        "",
        "| Status | Code | Message | Evidence |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["findings"]:
        lines.append(f"| `{item['status']}` | `{item['code']}` | {item['message'].replace('|', '\\|')} | `{item.get('evidence', '')}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = common_parser("Audit schematic visual flow against the functional-block template.")
    args = parser.parse_args()
    _, schematic = resolve_project_and_schematic(args.project, args.schematic)
    result = run_audit(schematic)
    write_markdown_and_json(markdown(result), result, Path(args.output) if args.output else None, Path(args.json_output) if args.json_output else None)
    return 0 if args.no_fail or result["status"] != CHECK_STATUS_FAIL else 1


if __name__ == "__main__":
    raise SystemExit(main())
