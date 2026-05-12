# Task Type To Blockers

## Purpose

This file lists the hard blockers that stop each task route from proceeding.

If a blocker is present, stop or reroute to the earlier required phase.

## Global Blockers

- active project is undefined for project-edit work
- prompt-counter maintenance is due and has not been run
- execution contract is missing for a meaningful run
- requested task is a later pipeline phase than the evidence supports
- user request would require editing KiCad design files without the required
  backup, verification, or rollback plan

## SCHEMATIC_CREATE_OR_REPAIR

Blocked when:

- the active project is not confirmed
- required component or datasheet evidence for high-risk parts is missing
- native annotation proof is required but unresolved
- the schematic quality/readability gate is failing and the request is really a
  cleanup or PCB-readiness task
- the user actually asked for annotation proof, visual cleanup, or PCB work and
  the route should be different

## SCHEMATIC_VISUAL_CLEANUP

Blocked when:

- rendered images or crop evidence are missing
- annotation state is still unresolved
- the schematic quality gate still shows unresolved readability blockers that
  are not being addressed by the task
- the task tries to claim `VISUAL_PASS` without image inspection

## NATIVE_ANNOTATION

Blocked when:

- the exact active project and target schematic are not confirmed
- no backup exists for the active project
- a wrong-project or unsafe KiCad GUI window is open
- a matching target window is dirty with `*` and that state was not explicitly
  allowed
- Eeschema is closed and the workflow has not been allowed to use the exact
  auto-open path
- the GUI safety gates fail

## FOOTPRINT_PACKAGE_GATE

Blocked when:

- `FOOTPRINT_LOCK.csv` is missing
- any physical symbol is missing a lock row
- any physical symbol still has a blank footprint
- source evidence or package proof is missing
- the exact package drawing or datasheet evidence is missing
- the candidate footprint cannot be tied to the part with drawing-level proof
- connector orientation proof is missing for connector footprints
- PMOS pin mapping proof is missing
- high-risk footprints remain unreviewed

## PCB_UPDATE_FROM_SCHEMATIC

Blocked when:

- ERC is not clean enough for the gate
- native annotation is not proven
- physical parts still lack footprints
- high-risk footprints remain unreviewed
- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` is not exactly `PASS`

## PCB_PRELAYOUT_VARIANT_PLANNING

Blocked for real-board progression when:

- fewer than three variants exist
- no variant passes
- the latest prelayout result does not show `placement_gate_status = PASS`
- routing work is requested and the latest result does not show
  `routing_gate_status = PASS`

## PCB_PLACEMENT

Blocked when:

- the phase gate blocks placement
- the PCB sandbox gate is not exactly `PASS`
- the latest prelayout gate is not placement-pass
- connector orientation is unproven or `NEEDS_HUMAN_REVIEW`
- antenna keepout, mechanical clearance, overlap, or board-shape issues remain
- no backup exists for the real board

## CONNECTOR_ORIENTATION_AUDIT

Blocked from passing when:

- the connector mouth, mating face, pin side, or body side is not proven
- the exact 3D model is missing and the workflow requires 3D proof
- the USB-C opening does not face off-board and align with `Edge.Cuts`
- the antenna keepout does not face outward

## PCB_ROUTING

Blocked when:

- placement is not approved
- the latest prelayout result does not show `routing_gate_status = PASS`
- connector orientation is not proven
- new unconnected or unrouted nets appear
- DRC fails
- the trace-geometry audit fails
- copied-board rehearsal is required by the workflow and has not passed

## TRACE_GEOMETRY_AUDIT

Blocked from passing when:

- right-angle or acute-angle findings remain
- excessive detours, rectangular loops, or zigzags remain
- test-point stubs exceed the allowed limit
- traces cross board edges, RF keepouts, or split return paths

## PCB_COPPER_ZONES

Blocked when:

- routing is not substantially complete
- unrouted or unconnected nets remain, except explicitly documented nonblocking
  exceptions
- RF keepout proof is missing
- connector-orientation proof is missing
- the routing geometry audit is still failing

## FAB_EXPORT

Blocked when:

- final DRC is not clean
- unrouted or unconnected nets remain
- connector orientation or polarity reviews are unresolved
- BOM, CPL/PNP, or package-validation checks are incomplete
- outputs would be mislabeled as final without LJ approval

## MEMORY_MAINTENANCE

Blocked only when:

- the target project path is unknown for project-scoped maintenance
- the maintenance scripts themselves are missing or broken

Otherwise this route is the required blocker-resolver when maintenance is due.

## OPEN_SOURCE_TOOL_USE

Blocked when:

- the task would require installing tools or cloning repos
- license or redistribution status is unclear
- the proposed integration would break ZIP portability or require bundling large
  external payloads
- the proposed tool has no graceful `not installed` behavior or offline fallback
- the workflow would bypass login, CAPTCHA, paywalls, or site terms
- the task would expose secrets or unsafe local-machine details
