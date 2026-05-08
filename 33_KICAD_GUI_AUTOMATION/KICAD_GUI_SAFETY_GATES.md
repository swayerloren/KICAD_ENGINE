# KiCad GUI Safety Gates

## Gate 1 - Project Identity

Pass only if:

- active project is selected in `00_CODEX_START/CURRENT_PROJECT.md`
- expected schematic path is absolute and inside the active project
- GUI process command line points to the same schematic

If Eeschema is not open for an annotation task, automation may attempt to open the target `.kicad_pro` only after project identity is confirmed and the action is logged. If Eeschema is open with any different project, stop.

## Gate 2 - Backup

Pass only if:

- backup exists under `99_BACKUPS/pre_codex_edits/`
- backup includes `.kicad_sch` and `.kicad_pro`
- backup path is recorded

## Gate 3 - Unsaved State

Pass only if:

- title does not start with `*`, or
- LJ explicitly approves keeping/saving the unsaved GUI state

## Gate 4 - Screenshots

Pass only if:

- before screenshot exists
- after screenshot exists for live actions
- screenshot paths are recorded

## Gate 5 - Tool Capability

Pass only if:

- required GUI libraries are available
- UI selection strategy is verified
- automation can identify controls without random clicking

## Gate 6 - Scope

Pass only if action is limited to one approved native KiCad schematic action:

- annotate schematic
- save schematic
- run GUI ERC
- capture screenshot

PCB/layout/routing/manufacturing actions are out of scope.

## Gate 7 - Post Action Verification

Pass only if:

- GUI state is checked after the action
- saved-file state is checked after save
- ERC/reference-table evidence is updated

For annotation, post-action verification must include GUI ERC 0 violations when safely automatable, post-save `kicad-cli` ERC pass, 0 unresolved `?` references in the saved schematic, and duplicate-reference scan pass.
