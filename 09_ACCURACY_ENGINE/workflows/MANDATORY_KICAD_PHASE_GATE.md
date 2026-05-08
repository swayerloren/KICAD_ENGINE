# Mandatory KiCad Phase Gate

Status: `MANDATORY`

Purpose: prevent Codex, Claude, or any other AI agent from running later KiCad PCB, fabrication, or production-review phases before earlier engineering evidence exists.

This workflow is stricter than a report checklist. A phase is not complete because an agent wrote a report. A phase is complete only when the required design artifact and evidence files exist and support the claimed status.

## Required Phase Order

### Phase 0 - Project Intake

Required before schematic work:

- Project folder exists.
- `.kicad_pro` exists.
- Active project path is confirmed.

Evidence examples:

- Active project path in the user prompt or `00_CODEX_START/CURRENT_PROJECT.md`.
- Project folder under `04_KICAD_PROJECTS/active/`.
- KiCad project file under the active project.

### Phase 1 - Schematic Gate

Required before PCB creation or PCB update:

- Schematic exists.
- Native KiCad annotation completed.
- ERC passes.
- No `?` references remain.
- Physical symbols have footprints assigned or approved candidate footprints.
- LJ approves PCB creation/update from schematic.

Evidence examples:

- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
- `reports/KICAD_GUI_NATIVE_ANNOTATION_RUN_REPORT.md`
- `reports/KICAD_GUI_NATIVE_ANNOTATION_ERC_REPORT.md`
- `reports/KICAD_GUI_NATIVE_ANNOTATION_REFERENCE_TABLE.md`
- `reports/FOOTPRINT_ASSIGNMENT_PLAN.md`

### Phase 2 - PCB Creation / Update From Schematic

Required before placement planning and all later PCB phases:

- `.kicad_pcb` exists.
- Footprints are imported from the schematic.
- PCB is synchronized from schematic.
- Initial DRC has been run.
- `reports/PCB_SYNC_STATUS.md` exists.

Required evidence files:

- `reports/PCB_CREATE_FROM_SCHEMATIC_REPORT.md` or `reports/PCB_UPDATE_FROM_SCHEMATIC_REPORT.md`
- `reports/PCB_FOOTPRINT_IMPORT_REPORT.md`
- `reports/PCB_INITIAL_DRC_REPORT.md`
- `reports/PCB_SYNC_STATUS.md`

### Phase 3 - Placement Planning

Required before component placement:

- Three layout plans are created.
- Best plan is selected.
- Board size or board outline recommendation exists.

Required evidence files:

- `reports/PCB_LAYOUT_PLAN_OPTIONS.md`
- `reports/PCB_SELECTED_LAYOUT_PLAN.md`

### Phase 4 - Mechanical Setup

Required before routing and before final placement is treated as layout-ready:

- Board outline exists.
- Mounting holes are placed.
- Mechanical keepouts are defined.
- Basic constraints or net classes are started.

Required evidence files:

- `reports/PCB_MECHANICAL_SETUP_REPORT.md`
- `reports/PCB_BOARD_OUTLINE_AND_HOLES_REPORT.md`

### Phase 5 - Component Placement

Required before routing:

- All components are placed.
- Connectors are oriented.
- ESP32 antenna/U.FL/pigtail clearance is checked.
- Placement DRC has been run.
- LJ placement review checklist exists.

Required evidence files:

- `reports/PCB_PLACEMENT_PASS_1_REPORT.md`
- `reports/PCB_PLACEMENT_ORIENTATION_RISK_REPORT.md`
- `reports/LJ_PCB_PLACEMENT_REVIEW_CHECKLIST.md`

### Phase 6 - Placement Audit

Required before routing:

- Placement audit completed.
- Orientation and polarity risks listed.
- LJ approval or explicit risk acceptance exists.

Required evidence files:

- `reports/PCB_PLACEMENT_STRICT_AUDIT.md`
- `reports/LJ_PCB_PLACEMENT_REVIEW_CHECKLIST.md`

### Phase 7 - Zones / Ground Strategy

Required before routing:

- GND zones and keepouts are defined.
- Zone DRC has been run.

Required evidence files:

- `reports/PCB_COPPER_ZONE_GROUND_PLANE_REPORT.md`

### Phase 8 - Routing

Required before final PCB review:

- Critical nets are routed first.
- Remaining nets are routed second.
- No unrouted nets remain.
- DRC has been run.

Required evidence files:

- `reports/PCB_CRITICAL_NETS_ROUTING_REPORT.md`
- `reports/PCB_FULL_ROUTING_REPORT.md`
- `reports/TRACE_BY_TRACE_AUDIT.md`

### Phase 9 - Final PCB Audit

Required before JLCPCB, mechanical production, BOM/CPL production, or export review:

- DRC passes or all violations are documented as nonblocking by LJ.
- No unrouted nets remain.
- Board visuals are exported.
- Trace-by-trace audit exists.
- LJ PCB review checklist exists.

Required evidence files:

- `reports/FINAL_PCB_AUDIT_BEFORE_FAB.md` or `reports/FINAL_PCB_VERIFICATION_BEFORE_FAB.md`
- `reports/LJ_FINAL_PCB_REVIEW_CHECKLIST.md`
- `reports/TRACE_BY_TRACE_AUDIT.md`

### Phase 10 - JLCPCB / Production Review

Allowed only after Phase 9:

- JLCPCB DFM/DFA review.
- Mechanical/3D review.
- BOM/CPL review.
- Production risk review.

Required evidence files after completion:

- `reports/JLCPCB_DFM_DFA_REVIEW.md`
- `reports/MECHANICAL_3D_REVIEW.md`
- `bom/PRODUCTION_BOM_REVIEW.md`
- `reports/PRODUCTION_RISK_REGISTER.md`

### Phase 11 - NOT_FINAL Export

Allowed only after production reviews:

- NOT_FINAL Gerbers.
- Drills.
- BOM.
- CPL.
- Schematic PDF.
- PCB images.
- Manifest.
- ZIP.

Required evidence after completion:

- `fabrication/NOT_FINAL_JLCPCB_REVIEW_*`
- `reports/NOT_FINAL_JLCPCB_EXPORT_REPORT.md`
- `reports/JLCPCB_UPLOAD_CHECKLIST.md`

### Phase 12 - JLC Upload Feedback

Allowed only after a NOT_FINAL package exists and LJ provides JLCPCB upload feedback.

Required evidence after completion:

- `reports/JLCPCB_UPLOAD_FEEDBACK_REVIEW.md`
- `reports/JLCPCB_UPLOAD_FIX_PLAN.md`

### Phase 13 - Final Prototype Signoff

Allowed only after JLC feedback is reviewed and all blockers are resolved.

Required evidence after completion:

- `reports/FINAL_PRODUCTION_SIGNOFF_AUDIT.md`
- `reports/LJ_FINAL_APPROVAL_CHECKLIST.md`

## Mandatory Agent Behavior

Before starting any requested KiCad phase, run or manually apply the same checks as:

`python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project <ACTIVE_PROJECT_PATH> --phase <PHASE>`

If the result is `BLOCKED`, stop. State the missing earlier phase and required evidence. Redirect to the next allowed phase.

Agents must not create downstream blocked review reports for future phases unless LJ specifically asks for a blocker audit. Documentation/report creation is not engineering progress and cannot substitute for PCB files, DRC results, unrouted-net evidence, production packages, or human approval.

