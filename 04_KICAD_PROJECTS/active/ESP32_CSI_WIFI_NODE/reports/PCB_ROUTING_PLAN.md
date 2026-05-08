# PCB_ROUTING_PLAN

Status: `ROUTING_PLAN_BLOCKED`

Final result: `ROUTING_PLAN_BLOCKED`

Project: `ESP32_CSI_WIFI_NODE`

Date: 2026-05-03

## Result

This is a planning-only routing report. No PCB file was edited, no traces were routed, no vias were placed, no zones were modified, and no manufacturing outputs were generated.

Routing is blocked because required PCB preconditions are not met:

- `.kicad_pcb` exists: `NO`
- Schematic-to-PCB gate result: `FAIL`
- PCB update allowed: `NO`
- Placement pass 2 final result: `PLACEMENT_ORIENTATION_FAIL`
- Hole/test-pad/via strategy final result: `HOLE_PAD_VIA_FAIL`
- Copper zone strategy final result: `ZONE_SETUP_FAIL`
- Board outline exists: `NO`
- Stackup/layer constraints verified: `NO`
- Footprints assigned and verified: `NO`

Do not route traces until `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` is `PASS`, a PCB exists, the board outline and constraints exist, placement passes, hole/test-pad/via strategy passes, copper-zone strategy passes, and high-risk human-review items are resolved.

## Evidence Read

- `reports/PCB_PLACEMENT_PASS_2_ORIENTATION_REPORT.md`
- `reports/COPPER_ZONE_STRATEGY_REPORT.md`
- `reports/THROUGH_HOLE_TEST_PAD_VIA_STRATEGY.md`
- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
- `09_ACCURACY_ENGINE/workflows/SCHEMATIC_TO_PCB_GATE_WORKFLOW.md`
- `09_ACCURACY_ENGINE/verification_rules/SCHEMATIC_TO_PCB_BLOCKERS.md`
- `09_ACCURACY_ENGINE/verification_rules/NEEDS_REVIEW_BLOCKER_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/USB_LAYOUT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/CAN_LAYOUT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/POWER_LAYOUT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/RF_LAYOUT_RULES.md`
- `memory/DESIGN_RULES.md`
- `memory/OPEN_DESIGN_RISKS.md`

## 1. Net Classes

Final net classes are `NOT_DEFINED_BLOCKED`.

Future candidate net classes may include:

| Net class | Intended use | Current status | Evidence required before use |
|---|---|---|---|
| `GND` | Ground return and zone connection. | `BLOCKED_NO_PCB` | Board outline, stackup, zone strategy, DRC rules, return-path review. |
| `POWER_INPUT` | Barrel/input connector, fuse, PMOS, TVS, and input capacitor path. | `BLOCKED_NO_PCB` | Current estimate, copper thickness, fab profile, placement, source-backed protection path. |
| `+5V_PROTECTED` | Protected 5 V rail after input protection. | `BLOCKED_NO_PCB` | Power tree current budget, trace width calculation, placement, DRC constraints. |
| `+3V3` | Regulated 3.3 V rail. | `BLOCKED_NO_PCB` | Regulator source data, load estimate, copper/current strategy, decoupling placement. |
| `USB_DIFF` | USB D+/D- pair. | `BLOCKED_NO_PCB` | USB connector footprint/orientation, ESD placement, stackup, impedance/geometry target, route constraints. |
| `RF_KEEP_OUT` | ESP32 antenna and any RF connector/antenna keepout. | `BLOCKED_NO_PCB` | Exact module footprint and official/module layout keepout evidence. |
| `GPIO_LOW_SPEED` | LEDs, buttons, boot/reset, and low-speed control signals. | `BLOCKED_NO_PCB` | Placement, schematic net review, access requirements. |
| `TEST` | Test pad access routes. | `BLOCKED_NO_PCB` | Test pad list, placement, fixture/access strategy. |
| `MECHANICAL` | Mounting holes and mechanical pads if modeled as nets. | `BLOCKED_NO_PCB` | User-confirmed plated/non-plated and GND/isolation policy. |

Do not assign final trace widths, clearances, or differential-pair settings from this plan alone.

## 2. Trace Width Strategy

Trace widths are `NOT_DEFINED_BLOCKED`.

Future strategy:

- Define minimum signal width from the selected fab profile and KiCad DRC constraints.
- Define power trace widths from current, copper thickness, temperature-rise target, route length, and conservative engineering review.
- Define USB D+/D- geometry from board stackup and impedance/spacing review.
- Define any RF feedline geometry only from source-backed RF layout guidance.
- Keep switcher and high-current power paths short and wide enough for current/thermal needs after source-backed review.

Exact values are intentionally not provided because the project lacks a PCB, stackup, selected verified fab limits, current budget, and placement.

## 3. Clearance Strategy

Clearances are `NOT_DEFINED_BLOCKED`.

Future strategy:

- Use the selected fabrication profile as the lower bound.
- Increase clearance for external connectors, power input, board edge, mounting holes, and mechanical stress areas when required by the design.
- Keep USB and RF clearances compatible with the selected route geometry and return-path requirements.
- Apply additional spacing around the switcher SW node and noisy loops to reduce coupling into USB, RF, reset/boot, and sensitive control nets.

Do not set final clearances without fab evidence, voltage/current review, and board constraints.

## 4. Via Strategy

Via strategy is `BLOCKED`.

Evidence: `reports/THROUGH_HOLE_TEST_PAD_VIA_STRATEGY.md` reports `HOLE_PAD_VIA_FAIL`.

Future strategy must define:

- signal via drill, annular ring, and clearance;
- power via size and count based on current/thermal review;
- stitching via purpose, spacing, and keepouts;
- thermal via policy for thermal pads if used;
- via tent/fill/plug rules only if supported by selected fab profile.

No via dimensions or via placement are approved by this plan.

## 5. Power Path Priority

Power routing must be planned before low-priority signals, but actual routing is blocked.

Future route order for power:

1. Input connector or barrel jack.
2. Fuse or resettable protection.
3. Reverse-polarity PMOS or selected input-protection circuit.
4. TVS and input bulk capacitor at the protected entry point.
5. Buck/regulator input loop.
6. Regulator output capacitor and 3.3 V distribution.
7. ESP32 module power pins and local decoupling.
8. USB VBUS sense/protection path only after VBUS policy is resolved.

High-current and switcher loops must remain short. Exact copper geometry remains blocked until placement, source documents, and fab constraints exist.

## 6. GND Strategy

Ground strategy is `BLOCKED`.

Evidence: `reports/COPPER_ZONE_STRATEGY_REPORT.md` reports `ZONE_SETUP_FAIL`.

Future strategy:

- Prefer continuous GND return where compatible with USB, RF, ESD, and power requirements.
- Avoid split ground unless there is source-backed reason and a human review accepts it.
- Place ESD return close to connector entry paths.
- Preserve return continuity under USB D+/D- where allowed by the final layout.
- Keep switcher power-loop return compact.
- Respect ESP32 antenna keepout and any no-copper regions required by the exact module layout guide.

Do not add, refill, split, or tune copper zones until zone setup is allowed.

## 7. USB D+/D- Routing Strategy

USB routing is `BLOCKED_NEEDS_REVIEW`.

Future USB strategy:

- Verify exact USB-C connector footprint, pin numbering, shell pins, and orientation.
- Place USB ESD protection close to the connector before route planning.
- Place USB series resistors only as source/project design requires and review their placement.
- Route D+/D- as a clean pair with minimal stubs and minimal vias.
- Keep D+/D- away from switcher SW nodes, noisy power loops, RF keepouts, board-edge hazards, and connector mechanical features.
- Preserve a suitable return path under the pair.
- Set final differential-pair geometry only after stackup and impedance review.

Do not claim USB impedance, pair length, or routing quality without PCB evidence and post-route review.

## 8. ESP32 RF/Antenna Keepout

ESP32 RF and antenna handling is `BLOCKED_NEEDS_SOURCE_AND_PCB`.

Future strategy:

- Verify the exact ESP32 module footprint and antenna side.
- Import or draw the antenna keepout from the official module land pattern/layout guidance.
- Keep copper, traces, vias, planes, mounting hardware, connectors, and tall components out of prohibited regions.
- Keep any U.FL/SMA/pigtail/antenna mechanical path source-backed and human-reviewed.
- Do not route RF feedlines or antenna paths from generic assumptions.

No antenna keepout is approved in a PCB file because no PCB exists.

## 9. Regulator Switching Node Constraints

Regulator routing is `BLOCKED_NEEDS_DATASHEET_AND_PLACEMENT`.

Future switcher strategy:

- Place input capacitor, regulator, inductor, diode or synchronous path, and output capacitor according to the regulator datasheet/layout guidance.
- Keep the SW node compact.
- Keep the hot loop small.
- Keep noisy switching copper away from USB D+/D-, RF/antenna areas, EN/BOOT/reset nets, and connector sense nets.
- Use copper/thermal relief only after source-backed thermal and fab review.

No switcher copper, SW-node shape, or power route geometry is approved by this plan.

## 10. Short Decoupling Loops

Decoupling routing is `BLOCKED_UNTIL_PLACEMENT`.

Future strategy:

- Place decoupling capacitors close to the IC/module power pins they support.
- Route power pin -> capacitor -> local GND return as a compact loop.
- Avoid long thin traces between power pins and required capacitors.
- Keep ESP32, regulator, USB protection, and other IC local decoupling source-backed.

Exact capacitor placement and loops must be verified visually and by DRC after placement/routing.

## 11. Test Pad Routes

Test pad routing is `BLOCKED`.

Future strategy:

- Define required test nets before routing.
- Keep test pads accessible according to the intended programming/debug/test method.
- Avoid stubs on USB, RF, or high-speed/high-risk nets unless the design explicitly requires and reviews them.
- Group low-speed test pads in a readable, serviceable area.
- Label test pads clearly without creating assembly ambiguity.

No test pad routing is approved until the test-pad list and access strategy are defined.

## 12. LED/Button Routes

LED/button routing is `LOW_PRIORITY_BLOCKED`.

Future strategy:

- Route LEDs, buttons, boot, reset, and other low-speed controls after power, USB, RF/antenna, and critical return paths.
- Keep boot and reset nets away from noisy switcher areas where practical.
- Preserve access and readability for buttons and LEDs.
- Do not let indicator routing compromise USB, power, RF, or connector keepouts.

## 13. No-Go Areas

Final no-go areas are `NOT_DEFINED_BLOCKED`.

Future no-go areas must include or consider:

- ESP32 antenna keepout and module keepout.
- USB-C connector shell/mechanical tabs and insertion area.
- Barrel jack insertion/mechanical area.
- Mounting-hole copper/hardware keepouts.
- Board edge clearance.
- Switcher SW node and noisy copper area.
- Test-pad access area.
- Connector mating direction and cable bend/strain-relief areas.
- Any RF pigtail/SMA/U.FL mechanical path if present.

No no-go area is approved until exact board outline, footprints, placement, and mechanical evidence exist.

## 14. Route Order

Routing must not start now. When all blockers are cleared, use this route order:

1. Confirm schematic-to-PCB gate is `PASS`.
2. Confirm PCB update from schematic is complete and board/netlist sync passes.
3. Confirm board outline, stackup, mechanical constraints, and fab constraints.
4. Confirm placement pass 1 and pass 2 pass.
5. Confirm hole/test-pad/via strategy passes.
6. Confirm copper-zone strategy passes or is intentionally deferred with written rationale.
7. Route power input/protection/regulator critical loops.
8. Route USB D+/D- with verified constraints.
9. Route ESP32 power, EN, BOOT, programming/debug, and critical control nets.
10. Route any RF/antenna-related paths only with source-backed geometry and keepouts.
11. Route test pads.
12. Route LEDs/buttons/low-speed signals.
13. Add or refill allowed GND zones.
14. Run DRC.
15. Export routed top/bottom visuals.
16. Perform close-up visual review.
17. Record unresolved human-review items.

## 15. Expected DRC Checks

DRC result: `NOT_RUN_NO_PCB`

Expected future checks after routing:

- unconnected items;
- clearance violations;
- trace width violations;
- via and drill violations;
- differential-pair constraint violations if configured;
- zone connection, thermal relief, and island/orphan issues;
- board edge clearance;
- courtyard and mechanical overlap issues;
- silk/fab/reference readability issues where supported by tooling;
- footprint-to-net and stale-footprint issues after schematic sync;
- USB/RF/power no-go and keepout violations where modeled.

Do not report DRC pass until `kicad-cli pcb drc` or equivalent evidence exists for the current routed board.

## 16. Visual Close-Up Checks Required After Routing

Required post-routing close-up review zones:

- input power connector, fuse, PMOS, TVS, and input capacitor;
- regulator, inductor, input/output capacitors, SW node, and thermal copper;
- ESP32 module, antenna keepout, EN/BOOT, decoupling, and any antenna connector path;
- USB-C connector, shell pins, VBUS policy implementation, ESD, CC resistors, series resistors, and D+/D- pair;
- mounting holes and board edge;
- test pads and programming/debug access;
- LEDs/buttons/user-access parts;
- GND zone continuity, islands/orphans, and stitching;
- connector orientation and mating direction;
- polarity-sensitive parts.

Every close-up review must link to image evidence. Any unclear high-risk item remains `NEEDS_HUMAN_REVIEW`.

## Remaining Blockers Before Routing

1. `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` must become `PASS`.
2. All footprints must be assigned and verified to exact package drawings.
3. Connector orientation and polarity-sensitive part review must be complete.
4. PCB must be created or updated from schematic only after the gate passes.
5. Board outline, stackup, and design constraints must be defined.
6. Placement pass 1 and placement pass 2 must pass.
7. Hole/test-pad/via strategy must pass.
8. Copper-zone strategy must pass or be intentionally deferred with evidence.
9. Fab profile and drill/via limits must be selected or user-confirmed.
10. USB, RF/antenna, power, and regulator layout evidence must be source-backed.

## Forbidden Until Blockers Clear

Do not:

- route traces;
- place vias;
- tune USB or RF routes;
- create or modify copper zones;
- define final net classes, trace widths, clearances, or differential-pair settings;
- generate Gerbers, drill files, pick-and-place, STEP, assembly, or fab outputs;
- claim routing is ready to begin.

