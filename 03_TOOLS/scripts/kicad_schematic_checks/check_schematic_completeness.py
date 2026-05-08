#!/usr/bin/env python3
"""Check whether required schematic functional blocks are present."""

from __future__ import annotations

from pathlib import Path

from schematic_check_common import (
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    CHECK_STATUS_WARN,
    build_report_data,
    check_record,
    common_parser,
    exit_code_for,
    load_schematic,
    parse_bom_lock,
    schematic_text_items,
    symbol_instances,
    symbol_search_text,
    write_optional_reports,
)


BLOCK_RULES = {
    "POWER_INPUT_PRESENT": ("power input", ("5v_in", "5v input", "vbus", "barrel", "jack", "usb-c", "+5v_in", "5v_raw")),
    "PROTECTION_PRESENT": ("input/protection", ("polyfuse", "ptc", "fuse", "tvs", "esd", "reverse polarity", "pmos", "smaj")),
    "REGULATOR_PRESENT": ("regulator", ("regulator", "buck", "ldo", "+3v3", "3v3", "ap63203", "ams1117", "mp1584")),
    "MCU_OR_MODULE_PRESENT": ("MCU/module", ("esp32", "stm32", "pic", "rp2040", "mcu", "module")),
    "ESD_PRESENT": ("ESD protection", ("esd", "tvs", "tpd", "usblc", "protection diode")),
    "BOOT_RESET_PRESENT": ("boot/reset", ("boot", "reset", "en", "gpio0", "nrst", "mclr")),
    "TEST_PADS_PRESENT": ("test pads", ("testpoint", "test point", "testpad", "tp_")),
    "MOUNTING_HOLES_PRESENT": ("mounting holes", ("mountinghole", "mounting hole", "mh1", "mh2")),
}


def combined_schematic_text(root: list[object]) -> str:
    symbols = symbol_instances(root)
    symbol_text = " ".join(symbol_search_text(symbol) for symbol in symbols)
    note_text = " ".join(schematic_text_items(root))
    return f"{symbol_text} {note_text}".lower()


def project_requires_usb_c(text: str, project_root: Path | None) -> bool:
    if "usb-c" in text or "usb_c" in text or "usbc" in text:
        return True
    if project_root and project_root.exists():
        for name in ("REQUIREMENTS.md", "DESIGN_PLAN.md", "SCHEMATIC_VERIFICATION_PLAN.md"):
            path = project_root / name
            if path.exists() and any(token in path.read_text(encoding="utf-8", errors="replace").lower() for token in ("usb-c", "usb_c", "usbc")):
                return True
    return False


def run_checks(schematic: Path, bom_lock: Path | None, project_root: Path | None) -> list[dict[str, str]]:
    root = load_schematic(schematic)
    text = combined_schematic_text(root)
    symbols = symbol_instances(root)
    symbol_refs = {str(symbol.get("reference", "")).upper() for symbol in symbols}
    checks: list[dict[str, str]] = []

    for code, (label, keywords) in BLOCK_RULES.items():
        if any(keyword in text for keyword in keywords):
            checks.append(check_record(CHECK_STATUS_PASS, code, f"{label} appears present.", "", ", ".join(keywords)))
        else:
            checks.append(check_record(CHECK_STATUS_FAIL, code, f"{label} was not detected by symbol/text scan.", "", ", ".join(keywords)))

    if project_requires_usb_c(text, project_root):
        if any(keyword in text for keyword in ("usb-c", "usb_c", "usbc", "usb4125", "cc1", "cc2", "vbus")):
            checks.append(check_record(CHECK_STATUS_PASS, "USB_C_SECTION_PRESENT", "Project appears to require USB-C and USB-C-related schematic content was found."))
        else:
            checks.append(check_record(CHECK_STATUS_FAIL, "USB_C_SECTION_MISSING", "Project appears to require USB-C but no USB-C section was detected."))
    else:
        checks.append(check_record(CHECK_STATUS_WARN, "USB_C_REQUIREMENT_NOT_DETECTED", "USB-C requirement was not detected from schematic/project notes; verify manually if this project should include USB-C."))

    if any(token in text for token in ("mechanical", "enclosure", "board outline", "mounting", "clearance")):
        checks.append(check_record(CHECK_STATUS_PASS, "PROJECT_MECHANICAL_NOTES_PRESENT", "Mechanical/project notes appear present."))
    else:
        checks.append(check_record(CHECK_STATUS_WARN, "PROJECT_MECHANICAL_NOTES_NOT_DETECTED", "Project notes/mechanical notes were not detected in schematic text."))

    bom = parse_bom_lock(bom_lock)
    if bom_lock and not bom["exists"]:
        checks.append(check_record(CHECK_STATUS_FAIL, "BOM_LOCK_NOT_FOUND", "BOM lock file does not exist.", "", str(bom_lock)))
    elif bom["exists"]:
        missing_refs = sorted(ref for ref in bom["references"] if ref not in symbol_refs)
        if missing_refs:
            checks.append(check_record(CHECK_STATUS_FAIL, "BOM_LOCK_ITEMS_MISSING_FROM_SCHEMATIC", "Expected BOM lock references are not present in schematic.", "", ", ".join(missing_refs)))
        else:
            checks.append(check_record(CHECK_STATUS_PASS, "BOM_LOCK_ITEMS_PRESENT", "All parseable BOM lock references appear in schematic.", "", str(len(bom["references"]))))
    else:
        checks.append(check_record(CHECK_STATUS_WARN, "NO_BOM_LOCK_PROVIDED", "No BOM lock path was provided; expected-items check was skipped."))

    return checks


def main() -> int:
    parser = common_parser("Check required functional blocks and expected BOM lock items in a KiCad schematic.")
    parser.add_argument("--project-root", default="", help="Optional active project root for requirement-note scanning.")
    args = parser.parse_args()
    schematic = Path(args.schematic)
    bom_lock = Path(args.bom_lock) if args.bom_lock else None
    project_root = Path(args.project_root) if args.project_root else None
    checks = run_checks(schematic, bom_lock, project_root)
    data = build_report_data(args, checks, {"project_root": str(project_root) if project_root else ""})
    write_optional_reports(args, "Schematic Completeness Check", data)
    return exit_code_for(data, args.no_fail)


if __name__ == "__main__":
    raise SystemExit(main())
