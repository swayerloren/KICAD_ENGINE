# Project AGENTS.md

Project-specific AI agent rules for `CLEAN_KICAD_PASSING_SAMPLE`.

## Required Startup

Before inspecting or editing this project, Codex must:

1. Read the root `KICAD_ENGINE/AGENTS.md` first.
2. Read every required `KICAD_ENGINE/00_CODEX_START/` instruction file in the root startup order.
3. Identify the active project from `KICAD_ENGINE/00_CODEX_START/CURRENT_PROJECT.md`.
4. Confirm the active project name and path match this project before touching KiCad files.
5. Load relevant global memory and this project's memory/history.

If this project is not the active project, Codex may read documentation only when requested, but must not edit KiCad project files.

## Protected Project Files

Do not edit these files unless the root startup gates are complete, the active project is identified, and the user explicitly requested the edit:

- `.kicad_pro`
- `.kicad_sch`
- `.kicad_pcb`
- symbol libraries
- footprint libraries
- manufacturing output files

## Required Before Edits

Before any protected edit, Codex must:

- Confirm the active project name.
- Confirm the active project path.
- Confirm target files are inside this project.
- Create or confirm a backup in `KICAD_ENGINE/99_BACKUPS/pre_codex_edits/`.
- State files likely to change.
- State the verification plan.
- State the rollback plan.

## Verification Rules

- After schematic changes, run ERC or explain why ERC could not be run.
- After PCB changes, run DRC or explain why DRC could not be run.
- Save ERC, DRC, review, and export outputs to this project's `reports`, `fabrication`, `bom`, or `renders` folders, or to approved `KICAD_ENGINE/05_OUTPUTS` folders.
- Do not fabricate, release, or label outputs final unless the verify-before-fab workflow passes.
- Manufacturing output is not final until ERC, DRC, BOM, footprint, netlist, datasheet, connector, polarity/orientation, power/protection, mechanical, and visual reviews are complete.

## Memory And History

- Durable project decisions belong in this project's memory folder and in `KICAD_ENGINE/01_MEMORY/projects/CLEAN_KICAD_PASSING_SAMPLE/PROJECT_MEMORY.md`.
- Session notes and command results belong in this project's history folder or `KICAD_ENGINE/02_HISTORY/project_history/CLEAN_KICAD_PASSING_SAMPLE/`.
- Do not store passwords, API keys, license keys, private tokens, or credentials in project memory, history, notes, scripts, or generated reports.

## Folder Rules

- KiCad source files belong in `kicad/`.
- Datasheets belong in `datasheets/`.
- BOM work belongs in `bom/`.
- Fabrication exports belong in `fabrication/`.
- Visual render outputs belong in `renders/`.
- Reports belong in `reports/`.
- Working notes belong in `notes/`.
- Project-local scripts belong in `scripts/`.
- Project-local durable memory belongs in `memory/`.
- Project-local history belongs in `history/`.

