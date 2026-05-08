# Create Schematic Workflow

Status: `GATED_WORKFLOW`

This workflow is for creating or editing KiCad schematics without guessing symbols, pinouts, footprints, power rails, or support circuits. It applies to new schematics, schematic repairs, and schematic block additions.

## Precondition

Do not edit `.kicad_sch` files until all of these are true:

1. The active project is identified in `00_CODEX_START/CURRENT_PROJECT.md` or by the user.
2. The target schematic path is inside that active project.
3. A backup exists under `99_BACKUPS/pre_codex_edits/` or the user explicitly approved a disposable copy.
4. `10_KNOWLEDGE_BASE/checklists/PRE_SCHEMATIC_CHECKLIST.md` has been applied.
5. Every selected exact component has at least a source-link or component-database record.
6. Missing source, pinout, or footprint information is marked `TODO_SOURCE_REQUIRED` or `NEEDS_HUMAN_REVIEW`.

## Workflow

1. Read `AGENTS.md`, startup files, project memory/history, and relevant schematic rules.
2. Capture design requirements and functional blocks: power input, protection, regulators, MCU/module, programming/debug, USB/CAN/RF/other interfaces, indicators, test points, and mechanical notes.
3. For each block, create a component list with `exact`, `generic`, or `placeholder` status.
4. For each component, record source evidence or route the missing evidence to `06_DATASHEETS/00_INDEX/MISSING_DATASHEETS.md` or project issue logs.
5. Select symbol candidates only after checking pin numbers, pin names, hidden pins, power pins, and electrical types.
6. Add support circuits only when the source or family guide supports them; otherwise create notes and blockers instead of schematic certainty.
7. Assign footprints only as candidates unless exact package drawings and KiCad pad geometry are reviewed.
8. Add explicit labels for high-risk items: connectors, PMOS, ESD arrays, regulators, crystals, RF, USB, CAN, polarity-sensitive parts, and modules.
9. Run annotation and completeness checks.
10. Run ERC or document exactly why ERC could not run.
11. Export visual review outputs and close-up crops when the project requires schematic-to-PCB gating.
12. Update project reports, memory/history, and unresolved issue logs.

## Required Outputs

- Schematic edit summary.
- Updated component/source evidence table.
- Annotation/completeness report.
- ERC report path or explicit blocker.
- Visual review path when applicable.
- Unresolved risk list with `PASS`, `FAIL`, `NEEDS_REVIEW`, or `BLOCKED_UNTIL_HUMAN_REVIEW`.

## Exit Criteria

The schematic can be called `SCHEMATIC_DRAFT_READY_FOR_REVIEW` only when source, symbol, pinout, power, and high-risk flags are recorded. It can move toward PCB update only through `SCHEMATIC_TO_PCB_GATE_WORKFLOW.md`.

If any exact pinout, connector orientation, package, footprint, power limit, or required ERC evidence is missing, the correct result is `SCHEMATIC_BLOCKED`, not silent confidence.
