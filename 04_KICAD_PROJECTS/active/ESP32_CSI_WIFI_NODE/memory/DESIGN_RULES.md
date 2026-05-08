# Project Design Rules

Status: `UNVERIFIED_PROJECT_MEMORY`

Project-specific rules for `ESP32_CSI_WIFI_NODE`.

## Rules

- Generated manufacturing-style outputs remain `NOT_FINAL`.
- USB-C, RF antenna, connector, polarity, and power-protection choices require explicit review.
- ERC is required after schematic edits.
- DRC is required after PCB creation or PCB edits.

## Current Records

No new design rules were added by this learning-system setup.

## 2026-05-03 PCB Mechanical Setup Blocker

Status: `BLOCKED_NEEDS_USER_REVIEW`

Durable project rule:

- Do not create or edit the PCB mechanical outline from assumptions.
- Board size, layer count, board thickness, mounting-hole geometry, connector edge placement, enclosure dimensions, and antenna/SMA/pigtail constraints must be user-confirmed or source-backed before PCB mechanical setup.
- A PCB mechanical setup request on 2026-05-03 was stopped because no `.kicad_pcb` existed, the schematic-to-PCB gate was `FAIL`, and board size was unknown.

Evidence:

- `reports/PCB_UPDATE_FROM_SCHEMATIC_REPORT.md`
- `reports/PCB_MECHANICAL_SETUP_REPORT.md`
- `reports/BOARD_SIZE_NEEDS_USER_REVIEW.md`

## 2026-05-03 PCB Placement Pass 1 Blocker

Status: `BLOCKED_UNTIL_PCB_EXISTS`

Durable project rule:

- Do not perform placement until a `.kicad_pcb` exists, the board outline exists, mechanical constraints are set, and the schematic-to-PCB gate allows PCB work.
- Placement pass 1 was requested on 2026-05-03 and stopped because no PCB file exists and the mechanical setup report is `NOT_RUN_BLOCKED`.

Evidence:

- `reports/PCB_PLACEMENT_PASS_1_REPORT.md`
- `_verification/pcb_visual/PLACEMENT_PASS_1_CLOSEUP_REVIEW.md`

## 2026-05-03 PCB Placement Pass 2 Orientation Blocker

Status: `BLOCKED_UNTIL_PCB_EXISTS`

Durable project rule:

- Do not perform placement pass 2 orientation, courtyard, mechanical, or readability review until a `.kicad_pcb` exists and placement pass 1 has produced placed footprints.
- Connector orientation, polarity orientation, courtyard clearance, board-edge clearance, and reference/value readability cannot be verified from schematic-only evidence.
- A placement pass 2 request on 2026-05-03 was stopped because no PCB file exists, pass 1 failed, and the schematic-to-PCB gate remains `FAIL`.

Evidence:

- `reports/PCB_PLACEMENT_PASS_2_ORIENTATION_REPORT.md`
- `_verification/pcb_visual/PLACEMENT_PASS_2_CLOSEUP_REVIEW.md`

## 2026-05-03 Hole, Test-Pad, And Via Strategy Blocker

Status: `BLOCKED_UNTIL_PCB_AND_FAB_EVIDENCE_EXIST`

Durable project rule:

- Do not define final via sizes, stitching spacing, thermal via arrays, mounting-hole plated status, mounting-hole GND/isolation policy, or test-pad geometry from assumptions.
- Hole, pad, and via strategy requires an existing PCB, board outline, stackup, selected fab limits, placement context, and mechanical/test requirements.
- A hole/test-pad/via strategy request on 2026-05-03 was stopped because no PCB file exists, placement pass 2 failed, and fab drill/via limits are not selected or verified.

Evidence:

- `reports/THROUGH_HOLE_TEST_PAD_VIA_STRATEGY.md`
- `_verification/pcb_visual/HOLE_PAD_VIA_CLOSEUP_REVIEW.md`

## 2026-05-03 Copper Zone Strategy Blocker

Status: `BLOCKED_UNTIL_PCB_PLACEMENT_AND_RETURN_PATH_EVIDENCE_EXIST`

Durable project rule:

- Do not create copper zones, split ground, define final zone priorities, define final thermal relief policy, or define final power copper from assumptions.
- Zone strategy requires an existing PCB, board outline, stackup, placed footprints, via strategy, antenna keepout, USB/ESD return-path plan, regulator layout evidence, and DRC constraints.
- A copper zone strategy request on 2026-05-03 was stopped because no PCB file exists, the schematic-to-PCB gate is `FAIL`, placement pass 2 failed, and hole/test-pad/via strategy failed.

Evidence:

- `reports/COPPER_ZONE_STRATEGY_REPORT.md`
- `_verification/pcb_visual/ZONE_CLOSEUP_REVIEW.md`

## 2026-05-03 PCB Routing Plan Blocker

Status: `BLOCKED_UNTIL_PCB_GATE_PLACEMENT_ZONES_AND_ROUTE_CONSTRAINTS_EXIST`

Durable project rule:

- Do not route traces, place routing vias, tune USB/RF routes, or define final routing constraints until the schematic-to-PCB gate is `PASS`, a `.kicad_pcb` exists, board outline/stackup constraints exist, placement passes, hole/test-pad/via strategy passes, copper-zone strategy passes, and high-risk routing constraints are source-backed or user-confirmed.
- Exact trace widths, clearances, via sizes, USB geometry, RF keepouts/feedlines, regulator switch-node copper, and power copper must not be guessed.
- A routing plan request on 2026-05-03 produced a blocked planning report only. No KiCad design files were edited and no routing was performed.

Evidence:

- `reports/PCB_ROUTING_PLAN.md`

## 2026-05-03 Critical Nets Routing Blocker

Status: `BLOCKED_UNTIL_ROUTING_PRECONDITIONS_PASS`

Durable project rule:

- Do not route even critical nets until the routing plan is ready, the schematic-to-PCB gate is `PASS`, a `.kicad_pcb` exists, placement and zone setup pass, and source-backed USB/RF/power constraints are available.
- A critical-net routing request on 2026-05-03 was stopped before PCB edits because `reports/PCB_ROUTING_PLAN.md` is `ROUTING_PLAN_BLOCKED`, no `.kicad_pcb` exists, placement pass 2 is `PLACEMENT_ORIENTATION_FAIL`, and zone setup is `ZONE_SETUP_FAIL`.

Evidence:

- `reports/PCB_CRITICAL_NETS_ROUTING_REPORT.md`
- `_verification/pcb_visual/CRITICAL_NETS_CLOSEUP_REVIEW.md`

## 2026-05-03 Full Routing Blocker

Status: `BLOCKED_UNTIL_CRITICAL_ROUTING_PASS_OR_ACCEPTED`

Durable project rule:

- Do not route remaining signal, LED/button, test-pad, or miscellaneous low-speed nets until critical routing has passed or is explicitly accepted with documented non-blocking warnings.
- A full-routing request on 2026-05-03 was stopped before PCB edits because `reports/PCB_CRITICAL_NETS_ROUTING_REPORT.md` is `CRITICAL_ROUTING_FAIL`, `reports/PCB_ROUTING_PLAN.md` is `ROUTING_PLAN_BLOCKED`, and no `.kicad_pcb` exists.

Evidence:

- `reports/PCB_FULL_ROUTING_REPORT.md`
- `reports/TRACE_BY_TRACE_AUDIT.md`
- `_verification/pcb_visual/FULL_ROUTING_CLOSEUP_REVIEW.md`

## 2026-05-03 Final PCB Verification Before Fab Blocker

Status: `BLOCKED_UNTIL_COMPLETE_PCB_VERIFICATION_EXISTS`

Durable project rule:

- Do not generate even `NOT_FINAL` fabrication outputs until a `.kicad_pcb` exists, schematic-to-PCB sync is verified, footprints are verified, placement/routing/zones are complete, DRC passes, unrouted checks pass, PCB visuals and trace-by-trace audit pass, and human-review-required items are resolved or explicitly accepted for review export.
- A final PCB verification request on 2026-05-03 was stopped because no `.kicad_pcb` exists and the PCB verification chain is blocked.

Evidence:

- `reports/FINAL_PCB_VERIFICATION_BEFORE_FAB.md`

## 2026-05-03 NOT_FINAL Fabrication Export Blocker

Status: `BLOCKED_UNTIL_FINAL_PCB_VERIFICATION_READY`

Durable project rule:

- Do not create `fabrication/NOT_FINAL_<timestamp>/` or export Gerbers, drills, BOM, CPL/PNP, STEP, PCB PDFs/images, assembly notes, fab drawings, ZIPs, or `PACKAGE_MANIFEST.md` unless `reports/FINAL_PCB_VERIFICATION_BEFORE_FAB.md` is exactly `READY_FOR_NOT_FINAL_FAB_EXPORT`.
- A `NOT_FINAL` export request on 2026-05-03 was stopped before package creation because final PCB verification was `NOT_READY_FOR_FAB_EXPORT`.

Evidence:

- `reports/NOT_FINAL_FAB_PACKAGE_AUDIT.md`
