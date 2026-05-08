# PCB Phase Gate Checklist

Status: `MANDATORY`

Use this checklist before starting any PCB, routing, fabrication, production, or signoff task.

## Phase 0 - Project Intake

- [ ] Active project path confirmed.
- [ ] Project folder exists.
- [ ] `.kicad_pro` exists.

## Phase 1 - Schematic Gate

- [ ] `.kicad_sch` exists.
- [ ] Native KiCad annotation completed.
- [ ] ERC passes.
- [ ] No `?` references remain.
- [ ] Physical symbols have footprints or approved candidates.
- [ ] LJ approval exists for PCB creation/update.

## Phase 2 - PCB Creation / Update From Schematic

- [ ] `.kicad_pcb` exists.
- [ ] Footprints imported.
- [ ] PCB synchronized from schematic.
- [ ] Initial DRC run.
- [ ] `reports/PCB_SYNC_STATUS.md` exists.

## Phase 3 - Placement Planning

- [ ] `reports/PCB_LAYOUT_PLAN_OPTIONS.md` exists.
- [ ] `reports/PCB_SELECTED_LAYOUT_PLAN.md` exists.
- [ ] Board size/outline recommendation exists.

## Phase 4 - Mechanical Setup

- [ ] Board outline exists.
- [ ] Mounting holes placed.
- [ ] Keepouts defined.
- [ ] Basic constraints/net classes started.
- [ ] Mechanical setup report exists.

## Phase 5 - Component Placement

- [ ] All components placed.
- [ ] Connectors oriented.
- [ ] ESP32 antenna/U.FL/pigtail clearance checked.
- [ ] Placement DRC run.
- [ ] LJ placement review checklist exists.

## Phase 6 - Placement Audit

- [ ] Strict placement audit exists.
- [ ] Orientation and polarity risks listed.
- [ ] LJ approval or explicit risk acceptance exists.

## Phase 7 - Zones / Ground Strategy

- [ ] GND zones defined.
- [ ] RF/antenna keepouts defined.
- [ ] Zone DRC run.

## Phase 8 - Routing

- [ ] Critical nets routed first.
- [ ] Remaining nets routed second.
- [ ] No unrouted nets remain.
- [ ] DRC run after routing.
- [ ] Trace-by-trace audit exists.

## Phase 9 - Final PCB Audit

- [ ] DRC passes or violations are explicitly accepted as nonblocking by LJ.
- [ ] No unrouted nets.
- [ ] Board visuals exported.
- [ ] Trace-by-trace audit exists.
- [ ] LJ final PCB review checklist exists.

## Phase 10 - JLCPCB / Production Review

- [ ] Phase 9 is complete.
- [ ] JLCPCB DFM/DFA review created.
- [ ] Mechanical/3D review created.
- [ ] BOM/CPL review created.
- [ ] Production risk register created.

## Phase 11 - NOT_FINAL Export

- [ ] Production reviews completed or accepted with documented blockers.
- [ ] NOT_FINAL package folder exists.
- [ ] Gerbers, drills, BOM, CPL, schematic PDF, PCB images, manifest, and ZIP are marked NOT_FINAL.

## Phase 12 - JLC Upload Feedback

- [ ] NOT_FINAL package exists.
- [ ] LJ supplied JLC upload screenshots/text.
- [ ] Upload feedback review exists.
- [ ] Upload fix plan exists.

## Phase 13 - Final Prototype Signoff

- [ ] JLC feedback is reviewed.
- [ ] All blockers are resolved or explicitly accepted by LJ.
- [ ] Final prototype signoff audit exists.
- [ ] LJ final approval checklist exists.

## Stop Rule

If any unchecked item is a prerequisite for the requested phase, stop. Do not run the phase. Do not create a downstream blocked report unless LJ specifically asked for a blocker audit.

