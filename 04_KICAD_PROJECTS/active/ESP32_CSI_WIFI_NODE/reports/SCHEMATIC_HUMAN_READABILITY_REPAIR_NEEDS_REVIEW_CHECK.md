# Needs Review Marker Check

Status: `FAIL`

Generated: `2026-05-06T17:27:25`
Schematic: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`
BOM lock: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\PRE_SCHEMATIC_BOM_LOCK.md`

## Summary

- Pass: 0
- Warn: 1
- Fail: 14

## Findings

| Status | Code | Reference | Message | Evidence |
| --- | --- | --- | --- | --- |
| `FAIL` | `UNRESOLVED_REVIEW_MARKER_ON_SYMBOL` | `J1` | Unresolved review marker present: BLOCKED. | `JACK_5V` |
| `FAIL` | `UNRESOLVED_REVIEW_MARKER_ON_SYMBOL` | `Q1` | Unresolved review marker present: BLOCKED. | `AO3401A_REV` |
| `FAIL` | `UNRESOLVED_REVIEW_MARKER_ON_SYMBOL` | `D1` | Unresolved review marker present: NEEDS_REVIEW. | `TVS_NEEDS_REVIEW` |
| `FAIL` | `UNRESOLVED_REVIEW_MARKER_ON_SYMBOL` | `U1` | Unresolved review marker present: NEEDS_REVIEW. | `AP63203_NEEDS_REVIEW` |
| `FAIL` | `UNRESOLVED_REVIEW_MARKER_ON_SYMBOL` | `L1` | Unresolved review marker present: BLOCKED. | `3.9uH_REV` |
| `FAIL` | `UNRESOLVED_REVIEW_MARKER_ON_SYMBOL` | `SW1` | Unresolved review marker present: BLOCKED. | `RESET_EN_REVIEW` |
| `FAIL` | `UNRESOLVED_REVIEW_MARKER_ON_SYMBOL` | `SW2` | Unresolved review marker present: BLOCKED. | `BOOT_GPIO0_REVIEW` |
| `FAIL` | `UNRESOLVED_REVIEW_MARKER_ON_SYMBOL` | `J2` | Unresolved review marker present: NEEDS_REVIEW. | `USB-C_NEEDS_REVIEW` |
| `FAIL` | `UNRESOLVED_REVIEW_MARKER_ON_SYMBOL` | `U3` | Unresolved review marker present: BLOCKED. | `USB_ESD_REV` |
| `FAIL` | `UNRESOLVED_REVIEW_MARKER_ON_SYMBOL` | `D2` | Unresolved review marker present: BLOCKED. | `PWR_LED` |
| `FAIL` | `UNRESOLVED_REVIEW_MARKER_ON_SYMBOL` | `D3` | Unresolved review marker present: BLOCKED. | `STATUS_LED` |
| `FAIL` | `UNRESOLVED_REVIEW_MARKER_IN_TEXT` | `` | Unresolved review marker present in schematic note: BLOCKED. | `REVIEW TABLE - unresolved items stay blocked for PCB update` |
| `FAIL` | `UNRESOLVED_REVIEW_MARKER_IN_TEXT` | `` | Unresolved review marker present in schematic note: UNVERIFIED. | `Package review: J1 J2 Q1 U1 U2 U3 L1 D1 and all connectors remain unverified` |
| `FAIL` | `UNRESOLVED_REVIEW_MARKER_IN_TEXT` | `` | Unresolved review marker present in schematic note: BLOCKED. | `PCB update remains blocked until schematic-to-PCB gate is PASS` |
| `WARN` | `REVIEW_MARKERS_REQUIRE_GATE_BLOCKER` | `` | Any unresolved review marker must block schematic-to-PCB gate until resolved or explicitly accepted by human review. | `14` |

## Safe Use

- This is an automated screening report, not final engineering approval.
- Failures or warnings must be resolved or explicitly carried as schematic-to-PCB gate blockers.
- Do not update PCB from schematic unless the active project's schematic-to-PCB gate is `PASS`.
