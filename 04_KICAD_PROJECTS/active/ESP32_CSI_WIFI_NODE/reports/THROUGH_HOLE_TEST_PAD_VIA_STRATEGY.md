# THROUGH_HOLE_TEST_PAD_VIA_STRATEGY

Status: `HOLE_PAD_VIA_FAIL_NOT_RUN`

Final result: `HOLE_PAD_VIA_FAIL`

Project: `ESP32_CSI_WIFI_NODE`

Date: 2026-05-03

## Result

Through-hole, mounting-hole, test-pad, and via strategy verification was not performed.

Reason: required PCB preconditions failed before any PCB edit:

- Placement pass 2 status: `PLACEMENT_ORIENTATION_FAIL_NOT_RUN`
- Placement pass 2 final result: `PLACEMENT_ORIENTATION_FAIL`
- `.kicad_pcb` exists: `NO`
- Board outline exists: `NO`
- Board mechanical constraints exist: `NO`
- Schematic-to-PCB gate result: `FAIL`
- PCB update allowed: `NO`

No mounting holes, mechanical holes, test pads, vias, copper keepouts, zones, or board-edge geometry exist in a PCB file to verify.

## Backup

Backup created: `YES`

Backup path:

- `99_BACKUPS/pre_codex_edits/ESP32_CSI_WIFI_NODE_HOLE_PAD_VIA_STRATEGY_BLOCKED_20260503_084327`

Backup contents:

- Existing `kicad/` project files were copied before writing this report and closeout records.
- No `.kicad_pcb` was present to back up.

## Files Inspected

- `reports/PCB_PLACEMENT_PASS_2_ORIENTATION_REPORT.md`
- `09_ACCURACY_ENGINE/pcb_rules/PCB_CREATION_STANDARD.md`
- `24_FAB_PROFILES/00_INDEX/FAB_PROFILE_SCHEMA.md`
- Active project `kicad/` folder

## Verification Table

| Item | Status | Evidence | Notes |
|---|---|---|---|
| Mounting-hole count | `NOT_RUN_NO_PCB` | No `.kicad_pcb` exists. | Count cannot be verified without board geometry and footprints. |
| Mounting-hole diameter | `NOT_RUN_NO_PCB` | No `.kicad_pcb` exists. | Exact diameter must come from enclosure/mechanical requirements or user confirmation. |
| Mounting-hole plated status | `NEEDS_HUMAN_REVIEW` | No `.kicad_pcb` exists. | Plated vs non-plated intent must be explicit before fab output. |
| Mounting-hole clearance | `NOT_RUN_NO_PCB` | No board outline or holes exist. | Copper keepout cannot be checked. |
| Mechanical hole positions | `NOT_RUN_NO_PCB` | No board outline or mechanical drawing exists. | Board size and hole coordinates remain unresolved. |
| Test pad count | `NOT_RUN_NO_PCB` | No `.kicad_pcb` exists. | Test-pad list and required nets need review after schematic/BOM lock. |
| Test pad size | `NEEDS_HUMAN_REVIEW` | No fab profile with verified drill/pad rules is selected. | Use fab-house limits only after source/user confirmation. |
| Test pad spacing | `NOT_RUN_NO_PCB` | No test pad footprints exist. | Spacing and accessibility cannot be verified. |
| Test pad accessibility | `NOT_RUN_NO_PCB` | No board side, enclosure, or fixture strategy exists. | Accessibility must account for assembly side and enclosure access. |
| Signal via rules | `NOT_DEFINED_BLOCKED` | No PCB stackup, fab profile, or board rules exist. | Do not choose via sizes from assumptions. |
| Power via rules | `NOT_DEFINED_BLOCKED` | No PCB stackup, current requirements, or copper strategy exists. | Current-carrying via strategy requires current, copper, thermal, and fab evidence. |
| Stitching via rules | `NOT_DEFINED_BLOCKED` | No PCB outline, zones, or RF/EMC strategy exists. | Ground stitching cannot be placed or sized without layout context. |
| Thermal via rules | `NOT_DEFINED_BLOCKED` | No thermal parts, pad geometries, or stackup exist in PCB. | Thermal vias require component package and fab evidence. |
| Ground stitching strategy | `NOT_DEFINED_BLOCKED` | No PCB zones or outline exist. | Must wait for board outline, stackup, connector/antenna placement, and DRC rules. |
| Mounting holes connected to GND or isolated | `NEEDS_HUMAN_REVIEW` | No mechanical/EMC requirement is recorded. | Must be decided intentionally; do not infer. |
| Copper keepout around mounting holes | `NOT_DEFINED_BLOCKED` | No hole footprints or board geometry exist. | Keepout rules depend on plated status, hardware, enclosure, and fab clearance. |
| Fab drill-size limits | `EVIDENCE_MISSING` | `FAB_PROFILE_SCHEMA.md` is a schema, not selected verified fab data. | No fab profile with verified drill limits was selected. |

## Via Strategy Decision

No via dimensions, drill sizes, annular rings, clearances, or stitching grid were defined.

Reason: the active project lacks:

- a PCB file;
- board outline;
- stackup;
- selected fab profile with verified drill and annular-ring limits;
- placement;
- routed or planned high-current/USB/RF/power zones;
- exact footprints and package drawings.

Any via sizes would be guessed and are therefore blocked.

## Future Required Strategy Fields

When the PCB exists and the gate allows layout work, the strategy must define and verify:

| Strategy area | Required evidence |
|---|---|
| Signal vias | Fab minimum drill, minimum annular ring, board thickness, layer count, DRC constraint path. |
| Power vias | Current estimate, copper thickness, thermal/current calculation or conservative source-backed rule, DRC constraint path. |
| Stitching vias | Ground-plane plan, RF/USB/ESD return path plan, spacing rationale, keepout from antenna and board edge. |
| Thermal vias | Exact component package thermal-pad drawing, paste-mask rule, via fill/tent/plug decision, fab capability. |
| Test pads | Required nets, pad side, fixture/access method, pad diameter/spacing, soldermask opening, silkscreen labels. |
| Mounting holes | Count, coordinates, diameter, hardware, plated/non-plated status, GND/isolation decision, copper keepout, mechanical drawing. |

## DRC

DRC result: `NOT_RUN`

Reason: no `.kicad_pcb` exists and no PCB changes were made.

## PCB Visual Export

Top visual: `NOT_RUN`

Bottom visual: `NOT_RUN`

Reason: no `.kicad_pcb` exists.

## Close-Up Review

Close-up review file:

- `_verification/pcb_visual/HOLE_PAD_VIA_CLOSEUP_REVIEW.md`

Review result: `NOT_RUN_NO_PCB`

Reason: no board, holes, test pads, vias, keepouts, or placement zones exist.

## Remaining Blockers

1. `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` must become `PASS`.
2. Footprints must be assigned and verified to exact package drawings.
3. PCB must be created or updated from schematic after the gate passes.
4. Board outline and mechanical constraints must be created.
5. Placement pass 1 and pass 2 must complete.
6. Fab profile must be selected or user-confirmed with drill/via limits.
7. Mounting-hole hardware, plated status, GND/isolation policy, and clearance must be user-confirmed.
8. Test-pad list and access strategy must be defined.

## Forbidden Until Blockers Clear

Do not:

- define final via drill sizes or annular rings;
- place vias;
- add ground stitching;
- add thermal vias;
- place or modify mounting holes;
- place or modify test pads;
- route traces;
- create or modify zones;
- generate manufacturing outputs;
- claim hole, pad, or via strategy has passed.

