# ESP32_CSI_WIFI_NODE Production Risk Register

Date: 2026-05-07

Mode: `READ_ONLY`

Production decision: `DO_NOT_SUBMIT_TO_JLCPCB`

Final classification: `BLOCKED_HIGH_RISK`

## Register Summary

| Metric | Count |
|---|---:|
| Critical open risks | 5 |
| High open risks | 9 |
| Medium open risks | 2 |
| Closed risks | 0 |
| Production release allowed | `NO` |

## Risk Register

| ID | Risk | Severity | Status | Evidence | Closure requirement |
|---|---|---:|---:|---|---|
| RISK-001 | No PCB exists for production review | `CRITICAL` | `OPEN` | `Test-Path kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`: `False`; final PCB audit is `BLOCKED_BY_DRC_OR_REVIEW_RISK`. | Create PCB only after schematic-to-PCB gate passes; run DRC, routing audit, visual review, and final PCB audit. |
| RISK-002 | Schematic-to-PCB gate blocks layout progression | `CRITICAL` | `OPEN` | `SCHEMATIC_TO_PCB_GATE_STATUS.md`: `Gate result: FAIL`; `PCB update allowed: NO`. | Resolve gate blockers and update gate report to exact `PASS` before PCB update. |
| RISK-003 | No exact footprint/package drawing verified | `CRITICAL` | `OPEN` | `PRE_SCHEMATIC_BOM_LOCK.md`: exact verified footprints `0`; schematic footprint assignment safe now `NO`. | Verify exact manufacturer drawings, pin numbering, package dimensions, and orientation for all physical parts. |
| RISK-004 | Power-entry protection may not survive wrong polarity/wrong voltage | `CRITICAL` | `OPEN` | J1 exact MPN missing; Q1 PMOS pin mapping review required; D1 TVS polarity/package review required; C1 package missing. | Close barrel jack, PMOS, fuse, TVS, and input capacitor reviews with datasheet evidence and schematic/PCB verification. |
| RISK-005 | USB-C and barrel power coexistence/backfeed policy unresolved | `CRITICAL` | `OPEN` | J2 review requires USB VBUS policy and shield/EMC strategy; no PCB/routing exists. | Define and implement USB VBUS isolation/backfeed policy; verify with netlist, layout, and DRC. |
| RISK-006 | Buck regulator stability and thermal risk | `HIGH` | `OPEN` | U1 high-risk regulator review; L1 exact MPN missing; C2/C3/C4 packages missing; no switching-loop layout exists. | Select compliant inductor/capacitors, verify AP63203 package/pinout, lay out tight loop and thermal copper, run DRC. |
| RISK-007 | ESP32 brownout during WiFi transmit | `HIGH` | `OPEN` | C6 package missing; C7 human review; regulator output network unresolved; no 3V3 layout exists. | Verify 3V3 current margin, output capacitance after derating, local decoupling, and power-plane/routing impedance. |
| RISK-008 | ESP32 boot/reset reliability unresolved | `HIGH` | `OPEN` | C8 package missing; SW1/SW2 exact MPNs missing; EN/GPIO0 layout not present. | Verify strap/reset values and EN timing; select switches; place controls accessibly and confirm bootloader behavior. |
| RISK-009 | PMOS source/drain or gate mapping error | `HIGH` | `OPEN` | Q1 value includes `PINMAP_BLOCKED_NEEDS_REVIEW`; SOT-23 pad numbering not verified. | Compare AO3401A datasheet, schematic symbol, and footprint pad map; document orientation before PCB update. |
| RISK-010 | TVS orientation/package error | `HIGH` | `OPEN` | D1 requires unidirectional/bidirectional, polarity, standoff/clamp, and placement review. | Select exact TVS and verify polarity/footprint against package drawing. |
| RISK-011 | USB ESD package/pinout error | `HIGH` | `OPEN` | U3 exact orderable/package is `BLOCKED_NO_EXACT_PART`; pinout review required. | Select exact ESD device; verify symbol and footprint pad mapping; place close to USB connector. |
| RISK-012 | USB D+/D- swapped or degraded by stubs | `HIGH` | `OPEN` | No USB routing exists; TP8/TP9 are optional stub review items. | Verify connector-to-ESD-to-resistor-to-ESP32 D+/D- continuity; remove or tightly control USB test stubs. |
| RISK-013 | ESP32-S3-WROOM-1U RF/mechanical keepout blocked | `HIGH` | `OPEN` | U2 WROOM-1U land-pattern equivalence and U.FL/pigtail clearance require review; no keepout exists. | Verify module footprint and RF connector clearance; add and visually inspect antenna/pigtail keepouts. |
| RISK-014 | Mounting holes may short or collide mechanically | `HIGH` | `OPEN` | MH1-MH4 screw size, NPTH/plated intent, copper keepout, standoff/washer clearance require review. | Define mounting hardware and enclosure; create holes/keepouts; inspect DRC and mechanical visuals. |
| RISK-015 | Connector edge alignment/overhang collision | `HIGH` | `OPEN` | J1/J2 exact drawings and edge direction are unresolved; no board outline exists. | Verify connector drawings, board-edge placement, enclosure openings, and cable insertion clearance. |
| RISK-016 | LEDs polarity/brightness not production-verified | `MEDIUM` | `OPEN` | D2/D3 exact LED color/package/MPN missing; resistors are planning values. | Select LEDs, verify polarity footprint and current/visibility against enclosure requirements. |
| RISK-017 | Test pads may be inaccessible or harmful to USB SI | `MEDIUM` | `OPEN` | TP1-TP9 probe access requires review; TP8/TP9 are USB stub risks; no placement exists. | Define enclosure probe access; remove or minimize high-speed stubs; verify final placement. |

## Release Gate

JLCPCB production release is blocked until all `CRITICAL` and `HIGH` risks are closed with evidence. Current disposition remains:

`BLOCKED_HIGH_RISK`
