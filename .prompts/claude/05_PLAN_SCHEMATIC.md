# Claude Prompt: Plan Schematic

You are Claude working from VS Code in:

`C:\Users\LJ\GitHub\KICAD_ENGINE`

## Read First

Read these files before planning schematic work:

1. `AGENTS.md`
2. `00_CODEX_START/START_HERE.md`
3. `00_CODEX_START/CURRENT_PROJECT.md`
4. `00_CODEX_START/PROJECT_INDEX.md`
5. `00_CODEX_START/KICAD_AGENT_OPERATING_MANUAL.md`
6. `00_CODEX_START/KICAD_SAFE_AUTOMATION_RULES.md`
7. `08_COMPONENT_DATABASE/00_INDEX/AI_USAGE_RULES.md`
8. `.prompts/shared/SAFETY_GATES.md`
9. `.prompts/shared/KICAD_VERIFICATION_STANDARD.md`
10. `.prompts/shared/COMPONENT_RESEARCH_STANDARD.md`

## Goal

Create a schematic plan that can be reviewed before any KiCad source file edits are made.

## Universal Requirements

- Do not modify schematic, PCB, project, symbol, or footprint files during planning.
- Require active project confirmation, backup, target file list, rollback plan, and verification plan before future edits.
- Record planning decisions or open questions in `02_HISTORY/`; durable approved decisions belong in `01_MEMORY/`.
- Define the verification reports that will be required after implementation.
- Do not fabricate component specs, datasheet claims, pinouts, power limits, or package data.
- Do not select footprints as final without exact package drawing verification.
- Label any future fabrication-style output `NOT_FINAL` until the full verification gate passes.

## Planning Checklist

1. Identify functional blocks.
2. List candidate parts and their verification status.
3. List required datasheets, reference designs, and app notes.
4. Define power rails, interfaces, connectors, protection, debug, boot, and programming paths.
5. Identify risk areas: connectors, polarity, RF, USB, CAN, automotive, power thermals, and footprint ambiguity.
6. Define ERC, DRC, BOM, datasheet, footprint, and visual checks required after edits.

## Output

Provide a schematic implementation plan with:

- Block diagram in text form.
- Candidate component table.
- Datasheet and source requirements.
- KiCad symbols and footprints as candidates only.
- Risks and human-review points.
- Required backup and verification gates before edits.
