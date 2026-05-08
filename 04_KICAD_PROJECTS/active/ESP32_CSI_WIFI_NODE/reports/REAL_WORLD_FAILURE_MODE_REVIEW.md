# ESP32_CSI_WIFI_NODE Real-World Failure Mode Review

Date: 2026-05-07

Mode: `READ_ONLY`

Schematic edited: `NO`

PCB edited: `NO`

Manufacturing outputs generated: `NO`

Final classification: `BLOCKED_HIGH_RISK`

Production recommendation: `DO_NOT_SUBMIT_TO_JLCPCB`

## Evidence Reviewed

- `reports/FINAL_PCB_AUDIT_BEFORE_FAB.md`: final PCB audit classification is `BLOCKED_BY_DRC_OR_REVIEW_RISK`.
- `reports/PCB_FULL_ROUTING_REPORT.md`: routing status is `BLOCKED`; DRC result is `NOT_RUN_NO_PCB`; unrouted count is `UNKNOWN_NO_PCB`.
- `reports/TRACE_BY_TRACE_AUDIT.md`: status is `NO_TRACES_TO_AUDIT`.
- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`: `Gate result: FAIL`; `PCB update allowed: NO`.
- `PRE_SCHEMATIC_BOM_LOCK.md`: no footprint is `VERIFIED_EXACT_PACKAGE_DRAWING`; 0 exact verified footprints; 30 candidate footprints require human review; 7 parts blocked by missing exact part; 6 parts blocked by missing package.
- `SCHEMATIC_READY_PARTS_LIST.md`: status is `NOT_READY_FOR_AUTOMATIC_FOOTPRINT_ASSIGNMENT`; no current row is ready for exact footprint assignment without human review.
- `NEEDS_REVIEW_BEFORE_SCHEMATIC.md`: connector, PMOS, TVS, regulator, USB ESD, ESP32 module, switches, LEDs, test pads, and mounting holes still require review.
- `Test-Path kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`: `False`.

## Review Basis

This review checks whether the design has enough verified evidence to survive common production and field-use failures. Because no PCB exists, no DRC has passed, no traces exist, and no exact footprint/package drawing has been verified, no scenario is classified as `PASS`.

`FAIL` means the current production state demonstrably fails the requested production-readiness condition. `NEEDS_HUMAN_REVIEW` means the schematic intent may be valid, but the exact part, package, orientation, layout, or mechanical evidence is not sufficient for production release.

## Failure Scenarios

| # | Scenario | Status | Evidence | Likely symptom | Required fix if failed or blocked | Production risk |
|---:|---|---:|---|---|---|---:|
| 1 | User plugs in wrong barrel jack polarity | `NEEDS_HUMAN_REVIEW` | J1 exact MPN is `BLOCKED_NO_EXACT_PART`; Q1 PMOS pin mapping/orientation remains `CANDIDATE_NEEDS_HUMAN_REVIEW`; no PCB exists to verify source/drain placement. | Board dead, PMOS body diode conducts unexpectedly, fuse/TVS overheats, regulator damage. | Select exact barrel jack and AO3401A-class PMOS; verify center-positive marking, jack pinout, PMOS source/gate/drain mapping, and reverse-polarity circuit in schematic and PCB before fab. | `CRITICAL` |
| 2 | User plugs in wrong voltage supply | `NEEDS_HUMAN_REVIEW` | Input TVS D1, fuse F1, bulk cap C1, regulator U1, and inductor L1 all require human review or exact package/MPN selection. | TVS clamps continuously, fuse trips, capacitor vents/fails, regulator overheats or fails short/open. | Define accepted input voltage range and adapter rating; verify TVS standoff/clamp, fuse trip behavior, capacitor voltage derating, and regulator absolute maximum margins. | `CRITICAL` |
| 3 | USB-C cable plugged in while barrel power is present | `NEEDS_HUMAN_REVIEW` | USB VBUS policy is called out as a J2 review item; no PCB exists and no power-path/USB routing exists. | Host port backfeed, board powers from unintended source, enumeration instability, damage to host or board power path. | Define USB VBUS/barrel coexistence policy; add or verify isolation/current limiting/backfeed prevention as required before PCB release. | `CRITICAL` |
| 4 | USB-C VBUS backfeed risk | `NEEDS_HUMAN_REVIEW` | J2 exact suffix and USB VBUS policy are not verified; no traces or net-by-net PCB evidence exist. | PC or hub receives 5 V from barrel input, USB port protection trips, field failures when both cables are connected. | Verify schematic power-domain separation and PCB implementation; add ideal diode/load switch/fuse/isolation if VBUS can be driven upstream. | `CRITICAL` |
| 5 | USB shield/ground noise/ESD behavior | `NEEDS_HUMAN_REVIEW` | R3 is `0R_DNI_SHIELD_BLOCKED_NEEDS_REVIEW`; J2 shell orientation and U3 ESD package are unresolved; no copper zones exist. | ESD resets, noisy ground coupling, poor USB robustness, enclosure/shield surprises. | Decide shield policy, chassis/logic ground connection method, ESD return path, and placement. Verify with layout images and DRC. | `HIGH` |
| 6 | ESP32-S3 boot mode failure | `NEEDS_HUMAN_REVIEW` | R1/R2/C8/SW1/SW2 need package or exact switch review; switch MPNs are `BLOCKED_NO_EXACT_PART`; no placement exists. | Board will not enter bootloader, boots intermittently, requires awkward timing or rework. | Verify EN/GPIO0 strap values, switch orientation, EN delay capacitor value/package, and accessible reset/boot placement. | `HIGH` |
| 7 | EN/reset timing issue | `NEEDS_HUMAN_REVIEW` | C8 package is `BLOCKED_NO_PACKAGE`; R1 and reset switch require human review; no actual RC routing/placement exists. | Random startup failures, brownout reset loops, unreliable programming. | Verify ESP32 EN timing against Espressif guidance, capacitor derating, reset switch topology, and local placement near U2. | `HIGH` |
| 8 | Brownout during WiFi transmit | `NEEDS_HUMAN_REVIEW` | ESP32 module decoupling C6 is `BLOCKED_NO_PACKAGE`; C7 requires human review; regulator output caps C3/C4 are package-blocked; no power routing exists. | WiFi connect resets, CSI capture dropouts, USB disconnects, unstable operation at peak RF current. | Verify AP63203 current/thermal margin, output capacitance after DC bias, ESP32 local decoupling, and low-impedance 3V3 routing/plane. | `HIGH` |
| 9 | Regulator thermal overload | `NEEDS_HUMAN_REVIEW` | U1 is high-risk regulator thermal/pinout/layout; L1 exact MPN is missing; no board copper, placement, or DRC exists. | Regulator enters thermal shutdown, 3V3 droops, board resets, component discoloration. | Calculate worst-case dissipation and temperature rise; choose inductor and capacitors; create layout with short loops and adequate copper; verify DRC and thermal assumptions. | `HIGH` |
| 10 | Regulator unstable due to capacitor/inductor choice | `NEEDS_HUMAN_REVIEW` | L1 exact MPN not selected; C2/C3/C4 packages and derating not selected; AP63203 support parts remain review-blocked. | Oscillation, audible/EMI noise, output ripple, boot failures, hot regulator. | Select AP63203-compliant inductor and capacitors using datasheet limits, saturation current, ESR, and DC-bias derating; update BOM and layout. | `HIGH` |
| 11 | PMOS reverse polarity source/drain wrong | `NEEDS_HUMAN_REVIEW` | Q1 value explicitly says `AO3401A_CLASS_PMOS_PINMAP_BLOCKED_NEEDS_REVIEW`; SOT-23 pad mapping and circuit orientation are not verified. | Reverse-polarity protection ineffective, permanent conduction through body diode, board fails under normal or reversed input. | Verify exact AO3401A datasheet pin numbering, KiCad symbol pins, and SOT-23 footprint pad numbering before PCB update. | `CRITICAL` |
| 12 | TVS diode orientation/package wrong | `NEEDS_HUMAN_REVIEW` | D1 polarity/package is high risk; exact unidirectional/bidirectional choice and cathode marking require review. | TVS shorts normal 5 V input, provides no surge protection, or fails during wrong-voltage events. | Select exact TVS part, verify DO-214AC/SMA footprint, polarity marking, standoff voltage, clamp voltage, and placement after fuse/power entry. | `HIGH` |
| 13 | USB ESD diode pinout wrong | `NEEDS_HUMAN_REVIEW` | U3 exact orderable/package is `BLOCKED_NO_EXACT_PART`; SOT-23-6 candidate must be checked against selected suffix. | USB D+/D- shorted, swapped, over-capacitive, or unprotected; enumeration fails. | Select exact ESD array package, verify schematic symbol pinout and KiCad footprint pad mapping, then place close to J2 with clean return path. | `HIGH` |
| 14 | USB D+/D- swapped | `NEEDS_HUMAN_REVIEW` | No PCB exists; no USB routing exists; J2 and U3 pin mappings are not verified. | USB enumeration fails or is unreliable; device not detected by host. | Verify connector pins, ESD pins, series resistor assignment, ESP32 USB pins, and final D+/D- route continuity before fab. | `HIGH` |
| 15 | USB D+/D- stubs from test pads too long | `NEEDS_HUMAN_REVIEW` | TP8/TP9 are explicitly `USB_D+_OPTIONAL_STUB_REVIEW` and `USB_D-_OPTIONAL_STUB_REVIEW`; no routing exists to measure stub length. | Marginal USB signal integrity, intermittent enumeration, higher EMI. | Remove USB test pads or implement very short, symmetric, near-inline access pads; verify route geometry with PCB images and trace audit. | `HIGH` |
| 16 | ESP32 module antenna/pigtail keepout blocked | `NEEDS_HUMAN_REVIEW` | U2 WROOM-1U footprint equivalence, U.FL/MHF clearance, pigtail bend, and enclosure/SMA routing require review; no keepout exists. | Reduced range, detuned antenna, damaged pigtail, failed enclosure fit. | Verify WROOM-1U land pattern and antenna connector mechanics; create RF/mechanical keepouts and inspect top/bottom visuals. | `HIGH` |
| 17 | Mounting holes short to copper/enclosure | `NEEDS_HUMAN_REVIEW` | MH1-MH4 require final screw/NPTH/copper keepout/standoff review; no PCB outline or holes exist. | Short to enclosure/standoff, cracked board, failed mounting, ground noise through hardware. | Confirm screw/standoff geometry, NPTH/plated intent, copper keepout diameter, and enclosure clearance in actual PCB. | `HIGH` |
| 18 | LEDs reversed or too bright/dim | `NEEDS_HUMAN_REVIEW` | D2/D3 exact LED color/package/MPN are `BLOCKED_NO_EXACT_PART`; resistor values are planning values. | No LED indication, excessive current, barely visible indicators, GPIO stress. | Select LED MPN/color, verify polarity footprint, forward voltage, resistor current, and enclosure visibility. | `MEDIUM` |
| 19 | Test pads inaccessible after enclosure | `NEEDS_HUMAN_REVIEW` | TP1-TP9 require probe access review; no board placement or enclosure geometry exists. | Debug/programming difficult or impossible after assembly; rework required. | Define enclosure/service access and probe direction; place grouped test pads away from connector overhangs and high-speed stubs. | `MEDIUM` |
| 20 | Board connector overhang/mechanical collision | `NEEDS_HUMAN_REVIEW` | J1/J2 exact drawings and board-edge/enclosure alignment are unresolved; no board outline or connector placement exists. | Connectors do not protrude correctly, cable cannot mate, enclosure interference, mechanical stress. | Select exact connector MPNs and drawings; verify edge alignment, insertion clearance, overhang, and enclosure opening before fab. | `HIGH` |

## Blocking Production Findings

1. No PCB source file exists, so DRC, trace inspection, board outline, placement, holes, copper, connector edge alignment, and mechanical clearances cannot be verified.
2. The schematic-to-PCB gate is `FAIL` and PCB update is explicitly forbidden by the project gate report.
3. No exact package drawing is verified for any footprint in the BOM lock.
4. Power-entry, reverse-polarity, USB-C, USB ESD, buck regulator, ESP32 RF, mounting-hole, and connector-orientation risks all remain unresolved.
5. The design must not be submitted to JLCPCB and must not be described as fabrication-ready.

## Final Classification

`BLOCKED_HIGH_RISK`

Reason: multiple critical real-world failure scenarios depend on exact parts, pin mappings, layout, DRC, routing, and mechanical evidence that does not yet exist or remains explicitly review-blocked.
