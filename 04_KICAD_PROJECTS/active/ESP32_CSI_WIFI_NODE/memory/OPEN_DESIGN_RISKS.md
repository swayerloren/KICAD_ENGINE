# Open Design Risks

Status: `UNVERIFIED_PROJECT_MEMORY`

Durable summary of unresolved design risks for `ESP32_CSI_WIFI_NODE`.

## Rules

- Every open risk should have a matching issue record in `history/issue_logs/`.
- Keep risks open until evidence or a human decision closes them.
- Manufacturing status remains `NOT_FINAL` while high-risk items are open.

## Current Records

### 2026-05-06 BOM And Footprint Lock Created But Not Approved

- Status: `OPEN`
- Evidence:
  - `PRE_SCHEMATIC_BOM_LOCK.md`
  - `SCHEMATIC_READY_PARTS_LIST.md`
  - `NEEDS_REVIEW_BEFORE_SCHEMATIC.md`
  - `reports/FOOTPRINT_ASSIGNMENT_PLAN.md`
- Summary: A planning BOM/footprint lock was created for all 43 parsed physical schematic symbols without editing the schematic. Candidate KiCad footprints were recorded where there was enough local evidence, but no footprint is verified against an exact manufacturer package drawing.
- Open blockers:
  - 0 footprints are `VERIFIED_EXACT_PACKAGE_DRAWING`.
  - 30 rows are `CANDIDATE_NEEDS_HUMAN_REVIEW`.
  - 7 rows are `BLOCKED_NO_EXACT_PART`.
  - 6 rows are `BLOCKED_NO_PACKAGE`.
  - High-risk rows still include the barrel jack, USB-C connector, AO3401A-class PMOS, USB ESD array, ESP32-S3 module, AP63203 regulator, inductor, fuse, TVS, USB test pads, and mounting holes.
  - Schematic footprint assignment is not approved until LJ reviews and accepts exact MPNs or package defaults.

### 2026-05-06 Emergency Schematic Truth Audit

- Status: `OPEN`
- Evidence:
  - `reports/EMERGENCY_CURRENT_SCHEMATIC_TRUTH_AUDIT.md`
  - `reports/CURRENT_SCHEMATIC_BLOCKERS.md`
  - `reports/EMERGENCY_CURRENT_SCHEMATIC_TRUTH_PARSE.json`
  - `_verification/emergency_truth_audit_20260506_155934/CLOSE_UP_REVIEW.md`
- Summary: LJ reported the schematic looked visually unacceptable despite prior automated visual reports. A fresh read-only truth audit found that placed references are annotated in the narrow no-question-mark sense, but the schematic is not acceptable and PCB update remains blocked.
- Open blockers:
  - All 43 physical symbols have blank footprint fields.
  - Fresh visual crop generation reports `PASS`, but that status only checks for visible unannotated references and visible footprint/library/path fields.
  - Fresh SVG evidence found 573 text items, 356 heuristic overlap candidates, and 20 near-text candidates.
  - Long visible values and schematic notes create readability problems in the LED, USB-C/ESD, ESP32, and power areas.
  - 26 unresolved `NEEDS_REVIEW` / `BLOCKED` marker checks remain.
  - BOM lock alignment was not proven in the checker run.
  - PCB update remains forbidden.

### 2026-05-06 Electrical And Footprint Gate Remains Blocked

- Status: `OPEN`
- Evidence:
  - `reports/SCHEMATIC_ELECTRICAL_GATE_REPORT.md`
  - `reports/FOOTPRINT_PACKAGE_GATE_REPORT.md`
  - `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
- Summary: Post-repair read-only electrical and footprint/package gate review reran ERC and schematic checkers. ERC is clean, but schematic-to-PCB gate remains failed.
- Open blockers:
  - 43 physical schematic symbols still have blank footprint fields.
  - Every physical symbol still has placeholder datasheet/source value `SOURCE_LINK_REQUIRED`.
  - BOM lock, ready-parts list, and needs-review input files remain missing.
  - AO3401A-class PMOS pin mapping/package orientation remains blocked.
  - USB VBUS/backfeed policy and USB shield/EMC policy remain unresolved.
  - USB-C connector, ESP32 module, USB ESD, AP63203 regulator, inductor, TVS, fuse, barrel jack, switches, LEDs, test pads, and mounting holes all require exact package/mechanical evidence and human review.

### 2026-05-06 Safe Schematic Repair Remaining Blockers

- Status: `OPEN`
- Evidence: `reports/SCHEMATIC_VERIFICATION_REPORT.md`
- Summary: Safe display/status cleanup was applied after backup, ERC remains clean, and automated visual close-up crop generation now passes. The schematic-to-PCB gate remains blocked.
- Open blockers:
  - 43 physical symbols still have blank footprint fields.
  - BOM lock and ready-parts files are still missing.
  - High-risk `NEEDS_REVIEW` / `BLOCKED` markers remain.
  - AO3401A PMOS pin mapping/package orientation remains blocked.
  - USB VBUS/backfeed and USB shield/EMC policies remain blocked.
  - USB-C connector, ESP32 module land-pattern equivalence, regulator passives, and mounting-hole/mechanical decisions remain unverified.
  - Human visual review is still required even though automated crops now report `PASS`.

### 2026-05-03 Schematic-to-PCB Gate Failure

- Status: `OPEN`
- Evidence: `SCHEMATIC_ELECTRICAL_AUDIT.md`
- Gate file: `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
- Issue record: `history/issue_logs/SCHEMATIC_ELECTRICAL_BLOCKERS_REMAIN_OPEN.md`
- Summary: ERC is clean after the schematic electrical blocker repair pass, but PCB update remains forbidden because high-risk review blockers remain.
- Open blockers:
  - AO3401A PMOS symbol pin mapping and footprint orientation.
  - USB VBUS/backfeed policy.
  - USB shield EMC strategy.
  - Missing `PRE_SCHEMATIC_BOM_LOCK.md`.
  - Missing `SCHEMATIC_READY_PARTS_LIST.md`.
  - Missing `NEEDS_REVIEW_BEFORE_SCHEMATIC.md`.
  - Unverified footprints/package drawings.
  - Connector orientation review.
  - Polarity-sensitive component review.
  - Regulator passives and USB-C/ESP32 source verification.

### 2026-05-03 PCB Placement Pass 1 Blocked

- Status: `OPEN`
- Evidence: `reports/PCB_PLACEMENT_PASS_1_REPORT.md`
- Issue record: `history/issue_logs/PCB_PLACEMENT_PASS_1_BLOCKED_NO_PCB.md`
- Summary: Placement cannot start because no `.kicad_pcb` exists, no board outline exists, PCB update from schematic is blocked, and mechanical setup is blocked.
- Open blockers:
  - Schematic-to-PCB gate is not `PASS`.
  - Footprints are unassigned/unverified.
  - Board dimensions and mechanical constraints are unknown.
  - Connector orientation and polarity review remain unresolved.

### 2026-05-03 PCB Placement Pass 2 Orientation Blocked

- Status: `OPEN`
- Evidence: `reports/PCB_PLACEMENT_PASS_2_ORIENTATION_REPORT.md`
- Issue record: `history/issue_logs/PCB_PLACEMENT_PASS_2_BLOCKED_NO_PCB.md`
- Summary: Orientation, mechanical correctness, courtyard clearance, and visual readability review cannot run because no PCB exists and placement pass 1 did not run.
- Open blockers:
  - Schematic-to-PCB gate is not `PASS`.
  - `.kicad_pcb` file is missing.
  - Board outline is missing.
  - Placement pass 1 is `PLACEMENT_FAIL`.
  - No placed footprints exist for reference/value, pin 1, connector direction, polarity, courtyard, or board-edge review.

### 2026-05-03 Hole, Test-Pad, And Via Strategy Blocked

- Status: `OPEN`
- Evidence: `reports/THROUGH_HOLE_TEST_PAD_VIA_STRATEGY.md`
- Issue record: `history/issue_logs/HOLE_PAD_VIA_STRATEGY_BLOCKED_NO_PCB.md`
- Summary: Mounting-hole, test-pad, and via strategy cannot be verified because no PCB, board outline, placement, or selected fab drill/via limits exist.
- Open blockers:
  - Schematic-to-PCB gate is not `PASS`.
  - `.kicad_pcb` file is missing.
  - Board outline and stackup are missing.
  - Placement pass 2 is `PLACEMENT_ORIENTATION_FAIL`.
  - Mounting-hole hardware and GND/isolation policy are unconfirmed.
  - Test-pad requirements and access strategy are undefined.
  - Fab drill/via limits are not selected or verified.

### 2026-05-03 Copper Zone Strategy Blocked

- Status: `OPEN`
- Evidence: `reports/COPPER_ZONE_STRATEGY_REPORT.md`
- Issue record: `history/issue_logs/COPPER_ZONE_STRATEGY_BLOCKED_NO_PCB.md`
- Summary: Copper zones, GND planes, keepouts, thermal reliefs, and power copper cannot be set up because no PCB, board outline, placement, or via strategy exists.
- Open blockers:
  - Schematic-to-PCB gate is not `PASS`.
  - `.kicad_pcb` file is missing.
  - Board outline and stackup are missing.
  - Placement pass 2 is `PLACEMENT_ORIENTATION_FAIL`.
  - Hole/test-pad/via strategy is `HOLE_PAD_VIA_FAIL`.
  - ESP32 antenna keepout is not source-backed in PCB context.
  - USB and regulator return-path plans are not available.

### 2026-05-03 PCB Routing Plan Blocked

- Status: `OPEN`
- Evidence: `reports/PCB_ROUTING_PLAN.md`
- Issue record: `history/issue_logs/PCB_ROUTING_PLAN_BLOCKED_NO_PCB.md`
- Summary: Routing cannot start because no PCB exists, the schematic-to-PCB gate remains `FAIL`, placement pass 2 failed/not run, hole/test-pad/via strategy failed/not run, and copper-zone strategy failed/not run.
- Open blockers:
  - Schematic-to-PCB gate is not `PASS`.
  - `.kicad_pcb` file is missing.
  - Board outline and stackup are missing.
  - Placement pass 2 is `PLACEMENT_ORIENTATION_FAIL`.
  - Hole/test-pad/via strategy is `HOLE_PAD_VIA_FAIL`.
  - Copper-zone strategy is `ZONE_SETUP_FAIL`.
  - Exact trace widths, clearances, via sizes, USB geometry, RF keepouts, and switcher layout constraints are not source-backed.

### 2026-05-03 Critical Nets Routing Blocked

- Status: `OPEN`
- Evidence: `reports/PCB_CRITICAL_NETS_ROUTING_REPORT.md`
- Issue record: `history/issue_logs/PCB_CRITICAL_NETS_ROUTING_BLOCKED_NO_PCB.md`
- Summary: Critical-net routing cannot start because no PCB exists, the schematic-to-PCB gate remains `FAIL`, routing plan is `ROUTING_PLAN_BLOCKED`, placement pass 2 failed/not run, and copper-zone strategy failed/not run.
- Open blockers:
  - `.kicad_pcb` file is missing.
  - Schematic-to-PCB gate is not `PASS`.
  - Routing plan is not `READY`.
  - Placement pass 2 is `PLACEMENT_ORIENTATION_FAIL`.
  - Copper-zone strategy is `ZONE_SETUP_FAIL`.
  - Critical USB, RF, regulator, protection, and decoupling routing constraints are not source-backed in PCB context.

### 2026-05-03 Full Routing Blocked

- Status: `OPEN`
- Evidence: `reports/PCB_FULL_ROUTING_REPORT.md`
- Issue record: `history/issue_logs/PCB_FULL_ROUTING_BLOCKED_CRITICAL_ROUTING_FAIL.md`
- Summary: Full routing cannot start because critical routing is `CRITICAL_ROUTING_FAIL`, routing plan is `ROUTING_PLAN_BLOCKED`, and no `.kicad_pcb` exists.
- Open blockers:
  - Critical routing must pass or be accepted with documented non-blocking warnings.
  - Routing plan must be ready.
  - `.kicad_pcb` file is missing.
  - DRC, unrouted/ratsnest check, PCB visuals, close-up review, and trace-by-trace audit cannot run without a routed PCB.

### 2026-05-03 Final PCB Verification Before Fab Blocked

- Status: `OPEN`
- Evidence: `reports/FINAL_PCB_VERIFICATION_BEFORE_FAB.md`
- Issue record: `history/issue_logs/FINAL_PCB_VERIFICATION_BEFORE_FAB_BLOCKED.md`
- Summary: Final PCB verification before fabrication export failed. The project is not ready even for `NOT_FINAL` fabrication export because no `.kicad_pcb` exists and required PCB-side verification evidence is missing.
- Open blockers:
  - Schematic-to-PCB gate is `FAIL`.
  - Footprint audit is `FOOTPRINT_AUDIT_FAIL`.
  - PCB update from schematic is `NOT_RUN_GATE_FAIL`.
  - DRC, unrouted check, full routing, trace-by-trace audit, placement, zones, board outline, connector orientation, polarity review, BOM alignment, and PNP orientation review are not complete.

### 2026-05-03 NOT_FINAL Fabrication Export Blocked

- Status: `OPEN`
- Evidence: `reports/NOT_FINAL_FAB_PACKAGE_AUDIT.md`
- Issue record: `history/issue_logs/NOT_FINAL_FAB_EXPORT_BLOCKED.md`
- Summary: The `NOT_FINAL` fabrication review package export request was blocked because final PCB verification is `NOT_READY_FOR_FAB_EXPORT`, not `READY_FOR_NOT_FINAL_FAB_EXPORT`.
- Open blockers:
  - No `.kicad_pcb` exists.
  - Final PCB verification before fab must pass first.
  - No Gerbers, drills, BOM, CPL/PNP, STEP, PCB PDFs/images, manifest, or package ZIP should be created until the gate changes.

### 2026-05-06 Schematic Ready For LJ Review But PCB Gate Blocked

- Status: `OPEN`
- Evidence: `reports/SCHEMATIC_VERIFICATION_REPORT.md`, `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
- Summary: The schematic has been repaired for readability, annotation, ERC, and candidate footprint assignment, but it is not ready for PCB update.
- Open blockers:
  - LJ has not visually approved the full-page schematic or close-up crops.
  - Candidate footprints are assigned but none are verified against exact manufacturer package drawings.
  - `J1`, `J2`, `Q1`, `U1`, `U2`, `U3`, `L1`, `D1`, `D2`, `D3`, `SW1`, and `SW2` remain high-risk/human-review items.
  - USB VBUS and shield policy remain unresolved.
  - BOM lock alignment has warnings from shortened visible schematic values.
  - PCB update, placement, routing, zones, and fab outputs remain blocked until the schematic-to-PCB gate is `PASS`.

### 2026-05-06 Final Readiness Re-Audit Found More Visual Repair Needed

- Status: `OPEN`
- Evidence: `reports/FINAL_SCHEMATIC_READINESS_AUDIT.md`, `reports/LJ_FINAL_VISUAL_REVIEW_PACKET.md`
- Summary: A strict read-only re-audit found the schematic is not ready for LJ signoff despite passing ERC, annotation, and footprint-population checks.
- Open blockers:
  - Input power, buck regulator, USB-C/ESD, ESP32 module, reset/boot, and LED areas still have visible text/value/reference/net-label overlaps.
  - Automated crop `PASS` is not enough to prove human readability.
  - Another visual cleanup pass is required before LJ visual approval.
  - High-risk part/footprint decisions remain unresolved and continue to block PCB update.
