#!/usr/bin/env python3
"""Generate ESP32_CSI_WIFI_NODE PCB intelligence docs from KiCad source files.

Read-only for KiCad design files. Writes documentation and JSON only under the
active project's pcb_intelligence folder.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PROJECT = ROOT / "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE"
PCB = PROJECT / "kicad/ESP32_CSI_WIFI_NODE.kicad_pcb"
SCH = PROJECT / "kicad/ESP32_CSI_WIFI_NODE.kicad_sch"
OUT = PROJECT / "pcb_intelligence"
MR = OUT / "machine_readable"
DATE = "2026-05-07"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def blocks(text: str, start_pattern: str):
    for match in re.finditer(start_pattern, text):
        start = match.start()
        depth = 0
        in_string = False
        escape = False
        for idx in range(start, len(text)):
            ch = text[idx]
            if in_string:
                if escape:
                    escape = False
                elif ch == "\\":
                    escape = True
                elif ch == '"':
                    in_string = False
            else:
                if ch == '"':
                    in_string = True
                elif ch == "(":
                    depth += 1
                elif ch == ")":
                    depth -= 1
                    if depth == 0:
                        yield text[start : idx + 1]
                        break


def q(pattern: str, text: str, default: str = "") -> str:
    match = re.search(pattern, text, re.S)
    return match.group(1) if match else default


def natural_key(ref: str):
    match = re.match(r"([A-Za-z#]+)(\d+)", ref or "")
    return (match.group(1), int(match.group(2)), ref) if match else (ref, 0, ref)


def parse_components(pcb_text: str) -> list[dict]:
    components: list[dict] = []
    for block in blocks(pcb_text, r"\(footprint\s+"):
        footprint = q(r'\(footprint\s+"([^"]+)"', block)
        ref = q(r'\(property\s+"Reference"\s+"([^"]+)"', block) or q(
            r'\(fp_text\s+reference\s+"([^"]+)"', block
        )
        value = q(r'\(property\s+"Value"\s+"([^"]*)"', block) or q(
            r'\(fp_text\s+value\s+"([^"]*)"', block
        )
        at_match = re.search(r"\(at\s+([\-\d.]+)\s+([\-\d.]+)(?:\s+([\-\d.]+))?", block)
        at = None
        if at_match:
            at = {
                "x_mm": float(at_match.group(1)),
                "y_mm": float(at_match.group(2)),
                "rotation_deg": float(at_match.group(3) or 0),
            }
        pads: list[dict] = []
        for pad_block in blocks(block, r"\(pad\s+"):
            pad = q(r'\(pad\s+"?([^"\s\)]+)"?', pad_block)
            pad_type = q(r'\(pad\s+"?[^"\s\)]+"?\s+([^\s\)]+)', pad_block)
            pinfunction = q(r'\(pinfunction\s+"([^"]*)"', pad_block)
            net_match = re.search(r'\(net\s+(\d+)\s+"([^"]*)"\)', pad_block)
            pads.append(
                {
                    "pad": pad,
                    "type": pad_type,
                    "pinfunction": pinfunction,
                    "net_id": int(net_match.group(1)) if net_match else None,
                    "net": net_match.group(2) if net_match else "",
                }
            )
        components.append({"ref": ref, "value": value, "footprint": footprint, "at": at, "pads": pads})
    return sorted(components, key=lambda item: natural_key(item["ref"]))


POWER_NETS = {"+3V3", "/+5V_IN", "/+5V_FUSED", "/+5V_PROTECTED", "/BUCK_SW", "/BUCK_BST"}
USB_NETS = {"/DP_C", "/DM_C", "/DP_E", "/DM_E", "/CC1", "/CC2", "/SHIELD"}
CONTROL_NETS = {"/BOOT0", "/ESP_EN", "/STATUS_LED", "/PLED", "/SLED"}
DEBUG_NETS = {"/U0RXD", "/U0TXD"}


def net_criticality(net: str) -> str:
    if net == "GND":
        return "GROUND"
    if net in POWER_NETS:
        return "CRITICAL_POWER"
    if net in USB_NETS:
        return "CRITICAL_USB"
    if net in DEBUG_NETS:
        return "DEBUG_TEST"
    if net in CONTROL_NETS:
        return "CONTROL_SIGNAL"
    if net.startswith("unconnected-"):
        return "LOW_SPEED"
    return "LOW_SPEED"


def route_priority(net: str) -> int:
    if net in {"/BUCK_SW", "/BUCK_BST"}:
        return 1
    if net in {"/+5V_IN", "/+5V_FUSED", "/+5V_PROTECTED", "+3V3", "GND"}:
        return 2
    if net in {"/DP_C", "/DM_C", "/DP_E", "/DM_E"}:
        return 3
    if net in {"/CC1", "/CC2", "/SHIELD"}:
        return 4
    if net_criticality(net) == "CONTROL_SIGNAL":
        return 5
    if net_criticality(net) == "DEBUG_TEST":
        return 6
    return 9


def width(net: str):
    if net in {"/+5V_IN", "/+5V_FUSED", "/+5V_PROTECTED"}:
        return 0.75
    if net == "+3V3":
        return 0.50
    if net == "GND":
        return None
    if net in {"/DP_C", "/DM_C", "/DP_E", "/DM_E", "/CC1", "/CC2"}:
        return 0.25
    if net == "/BUCK_SW":
        return 0.50
    return 0.20


def via_policy(net: str) -> str:
    if net == "GND":
        return "Use ground vias for low-impedance returns/stitching; avoid ESP32 RF keepout."
    if net in {"/BUCK_SW", "/BUCK_BST"}:
        return "Avoid vias; keep local to U1/L1/C6."
    if net in {"/DP_C", "/DM_C", "/DP_E", "/DM_E"}:
        return "Avoid vias/stubs; if unavoidable, use symmetric treatment on D+/D- pair."
    if net in {"/+5V_IN", "/+5V_FUSED", "/+5V_PROTECTED", "+3V3"}:
        return "Vias acceptable only when current path and return path remain low impedance."
    return "Vias acceptable when useful; keep away from RF keepout and connector mechanical areas."


def length_sensitivity(net: str) -> str:
    if net in {"/BUCK_SW", "/BUCK_BST"}:
        return "very short/local"
    if net in {"/DP_C", "/DM_C", "/DP_E", "/DM_E"}:
        return "short/paired/minimal stubs"
    if net in {"/+5V_IN", "/+5V_FUSED", "/+5V_PROTECTED", "+3V3", "GND"}:
        return "short for high-current loops; distribution can branch after decoupling"
    if net in {"/BOOT0", "/ESP_EN"}:
        return "low-speed, but pull/timing parts should stay near the relevant pins"
    return "low-speed/no strict length match"


def net_purpose(net: str) -> str:
    mapping = {
        "GND": "Common return path, ESD return, regulator return, and module ground.",
        "+3V3": "Buck-regulated 3.3 V rail feeding ESP32 and low-voltage peripherals.",
        "/+5V_IN": "Raw external 5 V input from barrel jack.",
        "/+5V_FUSED": "Input after PTC fuse and before PMOS reverse-polarity stage.",
        "/+5V_PROTECTED": "Protected 5 V after Q1; feeds TVS/input caps/buck and test point.",
        "/BUCK_SW": "Switching node between U1 SW pin and L1.",
        "/BUCK_BST": "Bootstrap node for U1, local to U1/C6/SW.",
        "/DP_C": "USB D+ at connector/ESD side.",
        "/DM_C": "USB D- at connector/ESD side.",
        "/DP_E": "USB D+ at ESP32 side after series resistor.",
        "/DM_E": "USB D- at ESP32 side after series resistor.",
        "/CC1": "USB-C CC1 pull-down path.",
        "/CC2": "USB-C CC2 pull-down path.",
        "/SHIELD": "USB connector shield policy net.",
        "/ESP_EN": "ESP32 enable/reset net.",
        "/BOOT0": "ESP32 boot-mode net.",
        "/U0RXD": "ESP32 UART receive/debug test net.",
        "/U0TXD": "ESP32 UART transmit/debug test net.",
        "/STATUS_LED": "ESP32 status LED drive net.",
        "/PLED": "Power LED resistor/LED net.",
        "/SLED": "Status LED resistor/LED net.",
    }
    if net.startswith("unconnected-"):
        return "Explicit no-connect imported from schematic/PCB for unused module or connector pad."
    return mapping.get(net, "Low-speed or support net imported from schematic/PCB.")


def placement_dependency(net: str) -> str:
    if net in {"/+5V_IN", "/+5V_FUSED", "/+5V_PROTECTED"}:
        return "J1/F1/Q1/D3/C2/C5/U1 must remain close in source-to-load order."
    if net in {"/BUCK_SW", "/BUCK_BST"}:
        return "U1/C6/L1 must be adjacent with compact loop."
    if net == "+3V3":
        return "U1/L1/C7/C8 near regulator output; C3/C4 close to U2 3V3/GND pins."
    if net in {"/DP_C", "/DM_C", "/DP_E", "/DM_E"}:
        return "J2/U3/R8/R9/U2 must form short direct USB path; test pads are stub-risk."
    if net in {"/CC1", "/CC2"}:
        return "R6/R7 close to J2 CC pins."
    if net in {"/ESP_EN", "/BOOT0"}:
        return "SW1/SW2 and R1/R2/C1/C3 close enough for clean routing while edge-accessible."
    if net in {"/PLED", "/SLED", "/STATUS_LED"}:
        return "LEDs at visible edge; resistors near LEDs."
    if net == "GND":
        return "Continuous return plane required; avoid splitting USB/power returns; no copper in RF keepout."
    return "No special placement beyond clean routing and service access."


def net_risk(net: str) -> str:
    if net in {"/BUCK_SW", "/BUCK_BST"}:
        return "Switching noise and loop-area risk; keep away from USB/RF."
    if net in {"/DP_C", "/DM_C", "/DP_E", "/DM_E"}:
        return "USB signal integrity/stub risk."
    if net == "/SHIELD":
        return "USB shield policy remains human-review required."
    if net in {"/+5V_IN", "/+5V_FUSED", "/+5V_PROTECTED"}:
        return "Power input/protection path and barrel jack mechanical decision affect route."
    if net == "+3V3":
        return "Brownout/voltage-drop risk if distribution or return is poor."
    if net.startswith("unconnected-"):
        return "No route expected; verify no unintended connection."
    return "Low to medium; route after critical nets."


def cluster(ref: str) -> str:
    if ref in {"J1", "F1", "Q1", "D3", "C2", "C5", "U1", "C6", "L1", "C7", "C8"}:
        return "POWER_INPUT_BUCK"
    if ref in {"J2", "U3", "R6", "R7", "R8", "R9"}:
        return "USB"
    if ref in {"U2", "C3", "C4"}:
        return "ESP32_MODULE_RF"
    if ref in {"SW1", "SW2", "R1", "R2", "C1"}:
        return "RESET_BOOT"
    if ref in {"D1", "D2", "R3", "R4"}:
        return "LED"
    if ref.startswith("TP"):
        return "TEST_PAD"
    if ref.startswith("MH"):
        return "MECHANICAL"
    if ref == "R5":
        return "USB_SHIELD_POLICY"
    return "MISC"


MUST_NEAR = {
    "J1": ["F1", "Q1"],
    "F1": ["J1", "Q1"],
    "Q1": ["F1", "D3", "C2", "C5", "U1"],
    "D3": ["Q1", "C2", "C5"],
    "C2": ["U1", "Q1", "D3"],
    "C5": ["U1", "Q1", "D3"],
    "U1": ["C2", "C5", "C6", "L1", "C7", "C8"],
    "C6": ["U1"],
    "L1": ["U1", "C7", "C8"],
    "C7": ["L1", "U1"],
    "C8": ["L1", "U1"],
    "J2": ["U3", "R6", "R7"],
    "U3": ["J2", "R8", "R9"],
    "R6": ["J2"],
    "R7": ["J2"],
    "R8": ["U3", "U2"],
    "R9": ["U3", "U2"],
    "U2": ["C3", "C4", "R8", "R9", "SW1", "SW2"],
    "C3": ["U2"],
    "C4": ["U2"],
    "SW1": ["U2", "R2"],
    "SW2": ["U2", "R1", "C1"],
    "R1": ["U2", "SW2"],
    "R2": ["U2", "SW1"],
    "C1": ["U2", "SW2"],
    "D1": ["R3"],
    "D2": ["R4"],
    "R3": ["D1"],
    "R4": ["D2"],
    "R5": ["J2", "GND"],
}


def component_function(ref: str) -> str:
    mapping = {
        "J1": "External barrel-jack 5 V input connector; mechanical fit risk on pill board.",
        "J2": "USB-C connector for USB data and connector shield; bottom-edge orientation required.",
        "F1": "PTC fuse in input power path.",
        "Q1": "AO3401A PMOS reverse-polarity/protection stage; pin mapping repaired.",
        "D3": "Input TVS/protection diode; polarity/package human-review required.",
        "U1": "AP63203 buck regulator candidate; converts protected input to +3V3.",
        "L1": "Buck regulator inductor.",
        "U2": "ESP32-S3-WROOM-1U value on ESP32-S3-WROOM-1 footprint; RF/footprint review required.",
        "U3": "USB ESD protection device near connector.",
        "SW1": "BOOT button/control switch.",
        "SW2": "RESET/EN button/control switch.",
        "D1": "Power/status LED indicator.",
        "D2": "Status LED indicator.",
    }
    if ref in mapping:
        return mapping[ref]
    c = cluster(ref)
    if ref.startswith("C"):
        return {
            "POWER_INPUT_BUCK": "Buck/input/output capacitor in power cluster.",
            "ESP32_MODULE_RF": "ESP32 module decoupling capacitor.",
            "RESET_BOOT": "EN/reset timing capacitor.",
        }.get(c, "Capacitor/support passive.")
    if ref.startswith("R"):
        if ref in {"R6", "R7"}:
            return "USB-C CC pull-down resistor."
        if ref in {"R8", "R9"}:
            return "USB D+/D- series resistor between connector/ESD and ESP32 side."
        if ref in {"R1", "R2"}:
            return "Reset/boot pull resistor."
        if ref in {"R3", "R4"}:
            return "LED current-limiting resistor."
        if ref == "R5":
            return "USB shield-to-ground policy resistor/link; DNI/review item."
        return "Resistor/support passive."
    if ref.startswith("TP"):
        return "Test pad/service access point."
    if ref.startswith("MH"):
        return "M2.5 NPTH mounting hole footprint."
    return "Component role not fully inferred; needs human review."


def orientation_risk(ref: str) -> str:
    if ref in {"J1", "J2"}:
        return "HIGH: connector mouth/edge orientation and plug envelope must be verified."
    if ref == "Q1":
        return "MEDIUM: AO3401A pin mapping repaired; verify orientation before production."
    if ref in {"D1", "D2", "D3"}:
        return "HIGH: diode/LED polarity must be verified."
    if ref == "U3":
        return "HIGH: USB ESD pinout/orientation must be verified."
    if ref == "U1":
        return "MEDIUM: regulator pin 1/orientation must be verified."
    if ref == "U2":
        return "HIGH: ESP32 module antenna/U.FL orientation and footprint width must be reviewed."
    if ref.startswith("SW"):
        return "MEDIUM: switch orientation must match intended access/action."
    return "LOW unless footprint/package source review says otherwise."


def production_risk(ref: str) -> str:
    if ref in {"J1", "J2", "U2", "U3", "Q1", "U1", "L1", "D3"}:
        return "HIGH: exact footprint/package/orientation/mechanical review required."
    if ref.startswith("MH"):
        return "HIGH: mounting strategy not resolved for compact board."
    if ref.startswith("TP"):
        return "MEDIUM: service access and USB stub risks need LJ review."
    if ref.startswith("D"):
        return "MEDIUM: polarity and visibility review required."
    return "MEDIUM: candidate footprint/package not production-verified unless separately documented."


def make_data(components: list[dict], sch_text: str):
    net_pads: dict[str, list[dict]] = defaultdict(list)
    for comp in components:
        for pad in comp["pads"]:
            if pad["net"]:
                net_pads[pad["net"]].append(
                    {
                        "ref": comp["ref"],
                        "pad": pad["pad"],
                        "pinfunction": pad["pinfunction"],
                        "value": comp["value"],
                        "footprint": comp["footprint"],
                    }
                )

    nets = []
    for net in sorted(net_pads, key=lambda item: (route_priority(item), item)):
        nets.append(
            {
                "net": net,
                "criticality": net_criticality(net),
                "connected_pads": [
                    {"ref": pad["ref"], "pad": pad["pad"], "role": pad["pinfunction"] or pad["value"] or ""}
                    for pad in sorted(net_pads[net], key=lambda item: natural_key(item["ref"]))
                ],
                "route_priority": route_priority(net),
                "recommended_width_mm": width(net),
                "via_policy": via_policy(net),
                "length_sensitivity": length_sensitivity(net),
                "return_path_concern": (
                    "Primary return net; requires continuous zones and short ESD/regulator returns."
                    if net == "GND"
                    else "Use adjacent/continuous GND return; important for USB, buck, ESD, and +3V3."
                ),
                "placement_notes": placement_dependency(net),
                "risk": net_risk(net),
                "human_review_required": (
                    net in {"/SHIELD", "/DP_C", "/DM_C", "/DP_E", "/DM_E", "/+5V_IN", "/+5V_FUSED", "/+5V_PROTECTED", "/BUCK_SW", "/BUCK_BST"}
                    or net.startswith("unconnected-")
                ),
            }
        )

    comp_rows = []
    for comp in components:
        connected_nets = sorted({pad["net"] for pad in comp["pads"] if pad["net"]})
        risk = production_risk(comp["ref"])
        comp_rows.append(
            {
                "ref": comp["ref"],
                "value": comp["value"],
                "footprint": comp["footprint"],
                "package": comp["footprint"].split(":")[-1] if ":" in comp["footprint"] else "UNKNOWN",
                "function": component_function(comp["ref"]),
                "cluster": cluster(comp["ref"]),
                "connected_nets": connected_nets,
                "must_be_near": MUST_NEAR.get(comp["ref"], []),
                "placement_priority": 1 if cluster(comp["ref"]) in {"POWER_INPUT_BUCK", "USB", "ESP32_MODULE_RF"} else 2,
                "orientation_risk": orientation_risk(comp["ref"]),
                "routing_notes": "; ".join(sorted({placement_dependency(net) for net in connected_nets}))[:1000],
                "production_risk": risk,
                "human_review": risk.startswith("HIGH") or "verify" in orientation_risk(comp["ref"]).lower(),
            }
        )

    return nets, comp_rows, len(set(re.findall(r'\(property\s+"Reference"\s+"([A-Z]+\d+)"', sch_text)))


def comp_table(rows: list[dict]) -> str:
    lines = [
        "| Ref | Value | Footprint | Cluster | Connected nets | Must be near | Human review |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['ref']}` | `{row['value']}` | `{row['footprint']}` | `{row['cluster']}` | "
            + ", ".join(f"`{net}`" for net in row["connected_nets"])
            + " | "
            + ", ".join(f"`{item}`" for item in row["must_be_near"])
            + f" | `{str(row['human_review']).upper()}` |"
        )
    return "\n".join(lines)


def net_table(rows: list[dict]) -> str:
    lines = ["| Net | Criticality | Pads | Priority | Width mm | Via policy | Risk |", "|---|---|---:|---:|---:|---|---|"]
    for row in rows:
        lines.append(
            f"| `{row['net']}` | `{row['criticality']}` | {len(row['connected_pads'])} | {row['route_priority']} | "
            f"`{row['recommended_width_mm']}` | {row['via_policy']} | {row['risk']} |"
        )
    return "\n".join(lines)


def write(path: Path, text: str):
    path.write_text(text.strip() + "\n", encoding="utf-8")


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    MR.mkdir(parents=True, exist_ok=True)
    pcb_text = read(PCB)
    sch_text = read(SCH)
    components = parse_components(pcb_text)
    nets, comp_rows, schematic_ref_count = make_data(components, sch_text)

    routing_rules = {
        "net_classes": [
            {"name": "POWER_5V_INPUT", "nets": ["/+5V_IN", "/+5V_FUSED", "/+5V_PROTECTED"], "width_mm": 0.75, "clearance_mm": 0.20, "notes": "Use wider than signal where space allows."},
            {"name": "POWER_3V3", "nets": ["+3V3"], "width_mm": 0.50, "clearance_mm": 0.20, "notes": "Wider than low-speed signals; distribute after output caps."},
            {"name": "USB_FS", "nets": ["/DP_C", "/DM_C", "/DP_E", "/DM_E"], "width_mm": 0.25, "clearance_mm": 0.20, "notes": "Short and parallel as practical; not an impedance-verified claim."},
            {"name": "BUCK_LOCAL", "nets": ["/BUCK_SW", "/BUCK_BST"], "width_mm": 0.50, "clearance_mm": 0.20, "notes": "Shortest possible local routing; avoid USB/RF."},
            {"name": "SIGNAL", "nets": ["/BOOT0", "/ESP_EN", "/STATUS_LED", "/PLED", "/SLED", "/U0RXD", "/U0TXD", "/CC1", "/CC2"], "width_mm": 0.20, "clearance_mm": 0.20, "notes": "Low-speed/control/debug/CC routing."},
            {"name": "GND", "nets": ["GND"], "width_mm": None, "clearance_mm": 0.20, "notes": "Use zones and low-impedance returns."},
        ],
        "route_order": ["repair_placement", "confirm_connector_orientation", "confirm_J1_strategy", "confirm_mounting_holes", "confirm_U2_keepout", "power_input", "buck_loop", "3V3_distribution", "USB_DP_DM", "USB_CC", "reset_boot", "LEDs", "test_pads_debug", "GND_zones", "DRC", "visual_trace_audit"],
        "via_policy": {"power": "Allowed when current/return path remains low impedance.", "usb": "Avoid; symmetric if unavoidable.", "buck_switch": "Avoid.", "gnd": "Allowed for stitching and returns outside RF keepout.", "rf_keepout": "No vias."},
        "keepout_zones": ["ESP32 antenna/U.FL/RF keepout", "USB-C shell/plug envelope", "barrel jack plug envelope", "mounting-hole clearance zones"],
        "no_route_zones": ["ESP32 RF keepout", "connector mechanical overhang areas", "mounting-hole clearance areas"],
        "drc_expectations": "Current board is unrouted; unconnected items are expected, but placement/courtyard/silkscreen/clearance issues block routing.",
    }
    placement_dependencies = {
        "clusters": {
            "POWER_INPUT_BUCK": ["J1", "F1", "Q1", "D3", "C2", "C5", "U1", "C6", "L1", "C7", "C8"],
            "USB": ["J2", "U3", "R6", "R7", "R8", "R9"],
            "ESP32_MODULE_RF": ["U2", "C3", "C4"],
            "RESET_BOOT": ["SW1", "SW2", "R1", "R2", "C1"],
            "LED": ["D1", "D2", "R3", "R4"],
            "TEST_PAD": [f"TP{i}" for i in range(1, 10)],
            "MECHANICAL": [f"MH{i}" for i in range(1, 5)],
        },
        "must_be_near": MUST_NEAR,
        "hard_blocks": [
            "Current placement audit is BLOCKED_BY_MECHANICAL_OR_FOOTPRINT_RISK.",
            "J1 barrel jack strategy unresolved.",
            "U2 footprint/keepout width risk unresolved.",
            "Four-hole compact mounting unresolved.",
            "Test pads crowded near USB/support parts.",
            "DRC has courtyard/clearance/silkscreen blockers.",
        ],
    }
    unresolved = [
        {"risk": "Placement repair not applied; latest repaired-placement audit says no repaired placement exists.", "severity": "HIGH", "status": "OPEN"},
        {"risk": "J1 barrel jack is bulky and not pill-board-friendly.", "severity": "HIGH", "status": "NEEDS_HUMAN_DECISION"},
        {"risk": "U2 footprint/keepout bbox reported wider than 38 mm board.", "severity": "HIGH", "status": "NEEDS_FOOTPRINT_OR_BOARD_DECISION"},
        {"risk": "Four M2.5 holes not practical on compact 38 mm board with current U2/J1 constraints.", "severity": "HIGH", "status": "NEEDS_MOUNTING_DECISION"},
        {"risk": "USB D+/D- test pads create stub risk and are crowded near USB area.", "severity": "MEDIUM", "status": "OPEN"},
        {"risk": "USB shield policy remains human-review required.", "severity": "MEDIUM", "status": "OPEN"},
        {"risk": "U2 pad 41 drill-size violation needs footprint/rule/fab review.", "severity": "HIGH", "status": "OPEN"},
        {"risk": "Silkscreen/courtyard/clearance DRC blockers remain.", "severity": "HIGH", "status": "OPEN"},
    ]

    write(MR / "nets.json", json.dumps(nets, indent=2))
    write(MR / "components.json", json.dumps(comp_rows, indent=2))
    write(MR / "routing_rules.json", json.dumps(routing_rules, indent=2))
    write(MR / "placement_dependencies.json", json.dumps(placement_dependencies, indent=2))
    write(MR / "unresolved_risks.json", json.dumps(unresolved, indent=2))
    write(MR / "_summary.json", json.dumps({"component_count": len(components), "net_count": len(nets), "critical_nets": [n["net"] for n in nets if n["criticality"] in {"CRITICAL_POWER", "CRITICAL_USB", "GROUND"}], "schematic_ref_count": schematic_ref_count}, indent=2))

    write(OUT / "README.md", f"""
# ESP32_CSI_WIFI_NODE PCB Intelligence Layer

Created: {DATE}

Scope: read-only PCB net intelligence, routing, placement, and dependency documentation.

## Source Files Parsed

- `kicad/ESP32_CSI_WIFI_NODE.kicad_sch`
- `kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

## Safety Scope

No schematic or PCB design files were edited. No routing, zones, Gerbers, drills, BOM/CPL, STEP, or production outputs were generated.

## Current Board Status

- PCB footprints documented: `{len(components)}`.
- Nets connected to pads documented: `{len(nets)}`.
- Current placement status: `BLOCKED_BY_MECHANICAL_OR_FOOTPRINT_RISK`.
- Routing status: `BLOCKED`.

Use this folder before any future placement repair or routing task so component movement is driven by actual net topology and placement dependencies, not by ratsnest appearance alone.
""")
    write(OUT / "INDEX.md", """
# PCB Intelligence Index

## Human-Readable Files

- `NET_TOPOLOGY_MAP.md`
- `PART_TO_PART_CONNECTION_MAP.md`
- `PLACEMENT_DEPENDENCY_MAP.md`
- `CRITICAL_NET_ROUTING_RULES.md`
- `POWER_TREE_AND_RETURN_PATHS.md`
- `USB_ROUTING_PLAN.md`
- `ESP32_RF_KEEP_OUT_PLAN.md`
- `TEST_PAD_ACCESS_PLAN.md`
- `MOUNTING_AND_CONNECTOR_MECHANICAL_PLAN.md`
- `VIA_AND_LAYER_STRATEGY.md`
- `COPPER_ZONE_STRATEGY.md`
- `ROUTING_SEQUENCE_PLAN.md`
- `TRACE_WIDTH_AND_NET_CLASS_PLAN.md`
- `COMPONENT_CLUSTER_PLAN.md`
- `ROUTING_RISK_REGISTER.md`
- `HUMAN_REVIEW_DECISIONS_REQUIRED.md`

## Machine-Readable Files

- `machine_readable/nets.json`
- `machine_readable/components.json`
- `machine_readable/routing_rules.json`
- `machine_readable/placement_dependencies.json`
- `machine_readable/unresolved_risks.json`

## Use Rule

Read this folder before placement repair, zone setup, or routing. Routing remains blocked until placement is repaired and LJ visually approves.
""")
    write(OUT / "NET_TOPOLOGY_MAP.md", f"""
# Net Topology Map

Source: parsed PCB pad-net assignments from `ESP32_CSI_WIFI_NODE.kicad_pcb`.

Documented nets: `{len(nets)}`

{net_table(nets)}

## Detailed Connected Pads

""" + "\n\n".join([f"### `{n['net']}`\n\nPurpose: {net_purpose(n['net'])}\n\n" + "\n".join(f"- `{p['ref']}` pad `{p['pad']}` {('('+p['role']+')') if p['role'] else ''}" for p in n["connected_pads"]) for n in nets]))
    write(OUT / "PART_TO_PART_CONNECTION_MAP.md", f"""
# Part-To-Part Connection Map

{net_table(nets)}

## Net-Based Part Groups

""" + "\n\n".join([f"### `{n['net']}`\n\nConnected references: " + ", ".join(f"`{p['ref']}`" for p in n["connected_pads"]) + f"\n\nPlacement dependency: {n['placement_notes']}" for n in nets]))
    write(OUT / "PLACEMENT_DEPENDENCY_MAP.md", f"""
# Placement Dependency Map

Current placement is not ready for routing. Future movement must preserve these electrical dependencies.

{comp_table(comp_rows)}

## Hard Placement Blocks

""" + "\n".join(f"- {item}" for item in placement_dependencies["hard_blocks"]))
    write(OUT / "CRITICAL_NET_ROUTING_RULES.md", f"""
# Critical Net Routing Rules

## Critical Power Nets

{net_table([n for n in nets if n['criticality'] == 'CRITICAL_POWER'])}

## Critical USB Nets

{net_table([n for n in nets if n['criticality'] == 'CRITICAL_USB'])}

## Ground

{net_table([n for n in nets if n['criticality'] == 'GROUND'])}

## Rules

- Route power input and buck regulator loop before low-speed/debug nets.
- Keep `/BUCK_SW` and `/BUCK_BST` very short and local to `U1/C6/L1`.
- Keep USB D+/D- short and paired as practical; avoid stubs and unnecessary vias.
- Do not route under ESP32 RF keepout.
- Do not route until placement is repaired and LJ visually approves.
""")
    write(OUT / "POWER_TREE_AND_RETURN_PATHS.md", f"""
# Power Tree And Return Paths

## Actual Power Nets

- `/+5V_IN`: raw input from `J1` to `F1`.
- `/+5V_FUSED`: fused input from `F1` to `Q1`.
- `/+5V_PROTECTED`: protected input from `Q1` to `D3/C2/C5/U1/TP1`.
- `/BUCK_BST`: bootstrap local net for `U1/C6`.
- `/BUCK_SW`: switch node between `U1`, `C6`, and `L1`.
- `+3V3`: regulator output rail feeding `U2`, decoupling, LEDs/control pullups, and `TP3`.
- `GND`: common return path.

## Power Cluster Components

{comp_table([c for c in comp_rows if c['cluster'] == 'POWER_INPUT_BUCK'])}

## Return Path Rules

- `J1/F1/Q1/D3/C2/C5` must stay close.
- `U1/C6/L1/C7/C8` must be compact; `/BUCK_SW` must be short.
- `GND` must provide low-impedance return for input protection, buck regulator, ESD, and ESP32 decoupling.
- Do not run buck switching copper near USB D+/D- or ESP32 RF keepout.
""")
    write(OUT / "USB_ROUTING_PLAN.md", f"""
# USB Routing Plan

## USB Cluster Components

{comp_table([c for c in comp_rows if c['cluster'] == 'USB' or c['ref'] == 'R5'])}

## USB Nets

{net_table([n for n in nets if n['criticality'] == 'CRITICAL_USB'])}

## Routing Rules

- `J2` must be at board edge with mouth off-board.
- `U3` ESD must be close to `J2`.
- `R6/R7` CC resistors must be close to `J2`.
- `R8/R9` series resistors must sit between `U3` and `U2`.
- `/DP_C` and `/DM_C` are connector/ESD-side USB data nets.
- `/DP_E` and `/DM_E` are ESP32-side USB data nets after series resistors.
- USB test pads are stub-risk and need LJ decision before routing.
- `/SHIELD` and `R5` remain USB shield policy review items.
""")
    write(OUT / "ESP32_RF_KEEP_OUT_PLAN.md", f"""
# ESP32 RF Keepout Plan

## ESP32 Cluster

{comp_table([c for c in comp_rows if c['cluster'] == 'ESP32_MODULE_RF'])}

## Rules

- `U2` must remain near the top edge with antenna/U.FL/RF keepout facing the top edge.
- No copper, traces, vias, test pads, mounting holes, or components are allowed in the RF keepout.
- Reports state `RF_Module:ESP32-S3-WROOM-1` footprint/keepout bbox is approximately 48 mm wide, wider than the 38 mm board.
- This is `REQUIRES_LJ_EXPLICIT_ACCEPTANCE` or board/footprint repair before routing.
- Keep buck regulator switching copper away from `U2` RF area.
""")
    write(OUT / "TEST_PAD_ACCESS_PLAN.md", f"""
# Test Pad Access Plan

## Test Pad Components

{comp_table([c for c in comp_rows if c['cluster'] == 'TEST_PAD'])}

## Rules

- Move `TP1-TP9` into a clean accessible row before routing.
- Do not crowd test pads behind USB-C shell or cable path.
- Do not mix test pads with `R6/R7/R8/R9`, LEDs, LED resistors, ESD, or switches.
- USB data test pads (`TP8/TP9` on `/DP_E` and `/DM_E`) are `USB_TEST_PAD_STUB_RISK`.
- Test pads must not block routing corridors from `J2` to `U3/R8/R9/U2`.
""")
    write(OUT / "MOUNTING_AND_CONNECTOR_MECHANICAL_PLAN.md", f"""
# Mounting And Connector Mechanical Plan

## Connector Components

{comp_table([c for c in comp_rows if c['ref'] in ['J1', 'J2']])}

## Mounting Holes

{comp_table([c for c in comp_rows if c['cluster'] == 'MECHANICAL'])}

## Rules

- `J2` USB-C should be bottom-edge, mouth downward/off-board, edge-line aligned.
- `J1` barrel jack is not pill-board-friendly and requires LJ mechanical decision.
- Connector plug/cable envelopes must not block test pads, buttons, LEDs, or mounting holes.
- Four M2.5 holes are not proven practical on the 38 mm board.
- Top holes must not violate ESP32 RF keepout.
- Current status: `MOUNTING_HOLE_STRATEGY_REQUIRES_LJ_DECISION`.
""")
    write(OUT / "VIA_AND_LAYER_STRATEGY.md", """
# Via And Layer Strategy

Layer assumption from current project planning: 2-layer board.

## Via Policy By Net Type

- GND: use stitching/return vias near USB ESD, regulator ground, and board perimeter only where they do not clutter or enter RF keepout.
- `/BUCK_SW` and `/BUCK_BST`: avoid vias; keep on same layer and very short.
- USB D+/D-: avoid vias; if unavoidable, use symmetric pair treatment and keep stubs minimal.
- +5 V and +3V3: vias acceptable when current path and return path remain low impedance.
- Low-speed/debug/test nets: vias acceptable after critical routing.

## No-Via Areas

- ESP32 RF keepout.
- Connector mechanical overhang/cable path areas.
- Mounting-hole clearance areas.
""")
    write(OUT / "COPPER_ZONE_STRATEGY.md", """
# Copper Zone Strategy

No zones should be created until placement is repaired and approved.

## Planned Strategy

- `B.Cu`: solid `GND` plane after placement approval.
- `F.Cu`: local `GND` pours where helpful after critical placement and routing decisions.
- No copper in ESP32 antenna/U.FL/RF keepout.
- Prioritize low-impedance return near USB ESD and buck regulator ground.
- Use thermal relief policy later; direct/solid GND may be appropriate for ESD/high-current returns where constraints allow.

## Current Gate

Zone creation remains blocked because placement is not repaired and LJ has not visually approved placement.
""")
    write(OUT / "ROUTING_SEQUENCE_PLAN.md", """
# Routing Sequence Plan

Routing is not allowed yet.

## Strict Sequence

1. Repair placement before routing.
2. Confirm connector orientation.
3. Confirm `J1` barrel jack strategy.
4. Confirm mounting-hole strategy.
5. Confirm `U2` keepout.
6. Route power input: `J1 -> F1 -> Q1 -> D3/C2/C5 -> U1`.
7. Route buck regulator loop: `U1/C6/L1/C7/C8`.
8. Route `+3V3` distribution.
9. Route USB D+/D-: `J2 -> U3 -> R8/R9 -> U2`.
10. Route CC resistors `R6/R7`.
11. Route reset/boot.
12. Route LEDs.
13. Route test pads/debug.
14. Add/refill GND zones.
15. Run DRC.
16. Perform visual trace audit.

## Gate

Do not start step 6 until steps 1-5 are complete and LJ approves placement.
""")
    write(OUT / "TRACE_WIDTH_AND_NET_CLASS_PLAN.md", "# Trace Width And Net Class Plan\n\nThese are first-pass layout planning values, not manufacturing capability claims.\n\n" + "\n".join(f"- `{cls['name']}`: nets {', '.join('`'+net+'`' for net in cls['nets'])}; width `{cls['width_mm']}` mm; clearance `{cls['clearance_mm']}` mm. {cls['notes']}" for cls in routing_rules["net_classes"]))
    write(OUT / "COMPONENT_CLUSTER_PLAN.md", f"""
# Component Cluster Plan

{comp_table(comp_rows)}

## Cluster Rules

- `POWER_INPUT_BUCK`: compact source-to-load chain, with short buck switch loop.
- `USB`: compact behind bottom-edge USB-C, not mixed into test pad row.
- `ESP32_MODULE_RF`: top-edge module placement, clear RF keepout.
- `RESET_BOOT`: edge-accessible switches with nearby pull/timing parts.
- `LED`: visible indicators, resistors close to LEDs.
- `TEST_PAD`: clean service row, not behind USB-C.
- `MECHANICAL`: holes only where clearance is proven.
""")
    write(OUT / "ROUTING_RISK_REGISTER.md", "# Routing Risk Register\n\n" + "\n".join(f"## {idx}. {risk['risk']}\n\n- Severity: `{risk['severity']}`\n- Status: `{risk['status']}`\n" for idx, risk in enumerate(unresolved, 1)))
    write(OUT / "HUMAN_REVIEW_DECISIONS_REQUIRED.md", """
# Human Review Decisions Required

Routing remains blocked until these decisions are resolved or explicitly accepted.

## Decisions

- Repair phase-gate/status inconsistency before more placement edits, or approve logged exception.
- Choose compact board size after U2 footprint width and J1 barrel jack constraints are reviewed.
- Decide whether to keep, replace, DNP, or move `J1` barrel input.
- Confirm `J2` bottom-edge alignment and acceptable overhang.
- Choose two-hole, shifted-hole, or wider-board mounting strategy.
- Confirm current `U2` footprint/keepout or replace with verified WROOM-1U footprint.
- Resolve U2 pad 41 drill-size rule/footprint/fab issue.
- Decide whether USB D+/D- test pads stay, move, or are removed/DNP in future revision.
- Confirm USB shield policy for `/SHIELD` and `R5`.
- Approve placement visually before routing.
""")

    print(json.dumps({"component_count": len(components), "net_count": len(nets), "critical_net_count": len([n for n in nets if n["criticality"] in {"CRITICAL_POWER", "CRITICAL_USB", "GROUND"}])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
