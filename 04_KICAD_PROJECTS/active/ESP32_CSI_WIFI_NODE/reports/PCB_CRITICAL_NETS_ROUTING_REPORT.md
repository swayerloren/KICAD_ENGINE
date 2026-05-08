# ESP32_CSI_WIFI_NODE PCB Critical Nets Routing Report

Date: 2026-05-06

Status: `BLOCKED`

PCB edits made: `NO`

Final classification: `BLOCKED`

## Requested Scope

Route critical nets only:

1. Input power path
2. Protection path
3. Buck regulator loop
4. `+3V3` output
5. Regulator decoupling
6. ESP32 decoupling
7. USB `D+` / `D-`
8. CC resistors
9. USB ESD
10. Reset/boot critical nets

Do not route all remaining nets.

## Gate Checks

| Check | Result | Evidence |
|---|---:|---|
| Active project identified | `PASS` | `00_CODEX_START/CURRENT_PROJECT.md` |
| PCB file exists | `FAIL` | `Test-Path kicad/ESP32_CSI_WIFI_NODE.kicad_pcb` returned `False` |
| Schematic-to-PCB gate | `FAIL` | `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` has `Gate result: FAIL` |
| PCB update allowed | `FAIL` | `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` has `PCB update allowed: NO` |
| Placement ready | `FAIL` | `reports/PCB_PLACEMENT_STRICT_AUDIT.md` final classification is `BLOCKED_BY_FOOTPRINT_ORIENTATION_RISK` |
| Routing allowed by placement audit | `FAIL` | `reports/PCB_PLACEMENT_STRICT_AUDIT.md` has `Routing allowed: NO` |
| Zones/ground plane ready | `FAIL` | `reports/PCB_COPPER_ZONE_GROUND_PLANE_REPORT.md` has `Status: NOT_RUN_BLOCKED_NO_PCB_OR_PLACEMENT_APPROVAL` |
| Critical routing may begin | `FAIL` | `reports/PCB_COPPER_ZONE_GROUND_PLANE_REPORT.md` has `Critical routing may begin: NO` |

## Routing Result

Critical nets routed: `0`

No traces were routed.

No vias were added.

No zones were refilled.

No KiCad PCB design files were edited.

## Critical Net Status

| Critical net group | Result | Reason |
|---|---:|---|
| Input power path | `NOT_ROUTED_BLOCKED` | No PCB, placement, outline, or approved power path exists |
| Protection path | `NOT_ROUTED_BLOCKED` | Protection components are not placed |
| Buck regulator loop | `NOT_ROUTED_BLOCKED` | Regulator, inductor, and capacitors are not placed |
| `+3V3` output | `NOT_ROUTED_BLOCKED` | No PCB copper or placed rail endpoints exist |
| Regulator decoupling | `NOT_ROUTED_BLOCKED` | No `U1`/capacitor placement exists |
| ESP32 decoupling | `NOT_ROUTED_BLOCKED` | No `U2`/decoupling capacitor placement exists |
| USB `D+` / `D-` | `NOT_ROUTED_BLOCKED` | No USB-C, ESD, series resistor, or ESP32 placement exists |
| CC resistors | `NOT_ROUTED_BLOCKED` | No USB-C/CC resistor placement exists |
| USB ESD | `NOT_ROUTED_BLOCKED` | No `U3` placement exists |
| Reset/boot critical nets | `NOT_ROUTED_BLOCKED` | No ESP32/switch placement exists |

## Rule Review

| Rule | Status |
|---|---:|
| Keep switching loop short | `NOT_VERIFIED_NO_PLACEMENT` |
| Keep USB pair short and clean | `NOT_VERIFIED_NO_PLACEMENT` |
| Avoid antenna keepout | `NOT_VERIFIED_NO_KEEP_OUT` |
| Use proper widths for power | `NOT_APPLIED_NO_ROUTING` |
| Use vias only when justified | `NOT_APPLIED_NO_ROUTING` |
| Refill zones after routing | `NOT_RUN_NO_ZONES_OR_ROUTING` |
| Run DRC | `NOT_RUN_NO_PCB` |
| Export visual crops | `NOT_RUN_NO_PCB` |

## DRC

DRC result: `NOT_RUN_NO_PCB`

Reason: no `.kicad_pcb` exists and no routing was performed.

## Visual Review

Visual result: `NOT_RUN_NO_PCB`

Review file: `_verification/pcb_visual/CRITICAL_NETS_ROUTING_REVIEW.md`

## Final Classification

`BLOCKED`

Reason: critical routing cannot begin until the schematic-to-PCB gate passes, the PCB exists, mechanical setup and placement are complete, copper/ground setup is applied, and routing is explicitly allowed.
