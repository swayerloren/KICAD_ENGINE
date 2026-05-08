# Needs Review Marker Check

Status: `FAIL`

Generated: `2026-05-03T14:56:58`
Schematic: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\attiny85.kicad_sch`

## Summary

- Pass: 0
- Warn: 1
- Fail: 3

## Findings

| Status | Code | Reference | Message | Evidence |
| --- | --- | --- | --- | --- |
| `FAIL` | `UNRESOLVED_REVIEW_MARKER_ON_SYMBOL` | `J2` | Unresolved review marker present: BLOCKED. | `Conn_02x05_Odd_Even` |
| `FAIL` | `UNRESOLVED_REVIEW_MARKER_ON_SYMBOL` | `U2` | Unresolved review marker present: BLOCKED. | `AMS1117-3.3` |
| `FAIL` | `UNRESOLVED_REVIEW_MARKER_ON_SYMBOL` | `J1` | Unresolved review marker present: BLOCKED. | `USB_A` |
| `WARN` | `REVIEW_MARKERS_REQUIRE_GATE_BLOCKER` | `` | Any unresolved review marker must block schematic-to-PCB gate until resolved or explicitly accepted by human review. | `3` |

## Safe Use

- This is an automated screening report, not final engineering approval.
- Failures or warnings must be resolved or explicitly carried as schematic-to-PCB gate blockers.
- Do not update PCB from schematic unless the active project's schematic-to-PCB gate is `PASS`.
