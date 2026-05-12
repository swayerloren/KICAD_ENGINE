# KiCad GUI Safety Gates

## Gate 1 - Project Identity

Pass only if:

- active project is confirmed
- target `.kicad_pro` is exact
- target `.kicad_sch` is exact
- the target files are inside the active project

If Eeschema is open with a different project, stop.

## Gate 2 - Window State

Pass only if one of these is true:

- exact target Eeschema is already open and clean
- no Eeschema window is open and the workflow is still in dry-run or approved
  open-only live mode
- exact target Eeschema is dirty with `*` and that state was explicitly
  allowed

Fail if:

- a different-project Eeschema window is open
- multiple Eeschema windows make the target ambiguous
- a dirty `*` target window exists and was not explicitly allowed

## Gate 3 - Backup

Pass only if, before any live annotation or live save:

- backup exists under `99_BACKUPS/pre_codex_edits/`
- backup path is recorded
- the backup includes the target schematic and project file

## Gate 4 - Screenshot Evidence

Pass only if live workflow evidence includes:

- before screenshot
- after screenshot

## Gate 5 - Flag Safety

Pass only if the live workflow uses explicit flags:

- `--live`
- `--allow-annotation`
- `--allow-save`
- `--allow-gui-erc`

Use `--allow-unsaved-existing` only when LJ explicitly wants to preserve/save
an already-dirty matching GUI state.

## Gate 6 - Scope

Pass only if the workflow is limited to:

- opening the exact project/schematic
- native annotation
- GUI save
- GUI ERC
- screenshots
- post-save CLI/reference verification

PCB update, routing, zones, and manufacturing outputs are out of scope.

## Gate 7 - Post-Save Verification

Pass only if all of the following are recorded:

- GUI save completed
- GUI ERC shows `0` violations
- post-save `kicad-cli sch erc` passes
- saved schematic scan shows `0` unresolved `?` references
- saved schematic scan shows `0` duplicate references
