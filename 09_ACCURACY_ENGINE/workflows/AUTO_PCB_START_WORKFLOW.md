# Auto PCB Start Workflow

## Purpose

Define the exact evidence-based transition from an auto-approved layout sandbox plan into real KiCad PCB work.

This workflow is the bridge between:

- schematic-ready-for-PCB evidence
- sandbox variant planning
- first real `.kicad_pcb` creation/update and placement work

## Required Status

Use only one result:

- `AUTO_PCB_START_PASS`
- `AUTO_PCB_START_BLOCKED`
- `AUTO_PCB_START_FAIL`

## Mandatory Preconditions

Real PCB work may begin automatically only when all of these are true:

1. `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` is exactly `PASS`
2. the footprint/package gate result is `PASS` or `SAFE_CANDIDATE_WITH_EVIDENCE`
3. `layout_sandbox/SELECTED_LAYOUT_PLAN.md` exists
4. the sandbox auto-approval report exists and says `AUTO_APPROVED_FOR_PCB_WORK`
5. board dimensions are defined
6. connector-orientation planning exists
7. antenna-keepout planning exists when the project includes RF
8. routing-feasibility planning exists
9. `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md` is exactly `PASS`
10. active project, backup plan, verification plan, and rollback plan are confirmed

If any item is missing or failed, stop with `AUTO_PCB_START_BLOCKED` and list exact blockers.

Do not ask LJ for generic approval when the evidence can answer the question.

## Allowed Actions After Pass

When the preconditions pass, Codex/Claude may automatically:

1. update PCB from schematic
2. create or update the real `.kicad_pcb`
3. apply the approved board outline
4. place fixed mechanical parts
5. place main component groups according to the selected layout plan
6. run DRC
7. export placement and mechanical visual review evidence
8. create an auto-start report

## Still Blocked After Pass

`AUTO_APPROVED_FOR_PCB_WORK` is not permission to:

- route final traces before placement gates pass
- generate Gerbers, drills, BOM/CPL, STEP, or fab packages
- mark the board fabrication-ready
- ignore DRC
- ignore connector, antenna, RF, USB, or power-path risks

## Execution Sequence

1. Confirm the active project path and target files.
2. Confirm all mandatory preconditions from the checklist.
3. Create a backup under `99_BACKUPS/pre_codex_edits/`.
4. Record the exact evidence paths used for the go/no-go decision.
5. Update PCB from schematic using a KiCad-safe method.
6. Create or update the `.kicad_pcb`.
7. Apply the approved board outline from the selected layout plan.
8. Place fixed mechanical components first.
9. Place main component groups from the selected layout plan.
10. Run DRC.
11. Export board and placement visual review evidence.
12. Create `AUTO_PCB_START_REPORT.md` from the template.

## Blocking Behavior

If blocked, create a report that includes:

- `AUTO_PCB_START_BLOCKED`
- exact failing preconditions
- evidence paths checked
- next valid action

If execution starts but the PCB update, outline application, placement, or DRC step fails, return `AUTO_PCB_START_FAIL` and capture the exact failed step.

## Required Evidence

The auto-start report must cite:

- schematic-to-PCB gate path and status
- footprint/package gate path and status
- selected layout plan path
- sandbox auto-approval report path and status
- connector-orientation evidence path
- antenna-keepout evidence path
- board-dimension evidence path
- routing-feasibility evidence path
- backup path
- DRC evidence path
- placement-visual evidence path
