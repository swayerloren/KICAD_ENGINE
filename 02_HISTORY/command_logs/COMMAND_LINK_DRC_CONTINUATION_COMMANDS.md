# COMMAND LINK DRC Continuation Command Log

Date: 2026-04-30

Project:

`C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK`

## Snapshot / Setup

Created a full continuation snapshot before edits:

```powershell
Copy-Item -Recurse -Force "C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK" "C:\Users\LJ\KICAD_ENGINE\99_BACKUPS\project_snapshots\COMMAND_LINK_DRC_CONTINUATION_20260430_210726"
```

Created working folder:

```powershell
New-Item -ItemType Directory -Force "C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_210726"
```

## Baseline DRC

```powershell
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\run_drc.ps1 -ProjectPath "C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK" -OutputRoot "C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_210726\baseline"
```

Result:

- Exit code 5.
- 44 DRC violations.
- Report: `Codex Review Outputs\20260430_210726\baseline\drc_20260430_210803\drc_report.txt`

Additional JSON parse command:

```powershell
kicad-cli pcb drc --format json --output "C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_210726\baseline\drc_baseline.json" "C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK\COMMAND LINK DRAFT.kicad_pcb"
```

## Dry-Run Repair Checks

Dry-run project copies were created under:

- `Codex Review Outputs\20260430_210726\dry_run_local_fplib_test`
- `Codex Review Outputs\20260430_210726\dry_run_single_local_item_names`
- `Codex Review Outputs\20260430_210726\dry_run_physical_drc_fixes`

Dry-run outcomes:

- Exact per-reference local footprint library: reduced DRC from 44 to 4.
- Shared original item-name local library test: left 12 DRC violations, so it was not applied.
- Physical DRC dry-run fixes: reduced DRC to 0.

## Applied Source Fixes

Applied with KiCad Python/pcbnew:

- Exported exact embedded footprints to `COMMAND_LINK_EMBEDDED.pretty`.
- Added `COMMAND_LINK_EMBEDDED` to `fp-lib-table`.
- Updated 40 board footprint IDs to project-local exact footprints.
- Set R2/U3/U4 pad 2 GND local zone connection to full.
- Adjusted C3/C9 opposing `F.CrtYd` edges.
- Refilled zones.
- Saved `COMMAND LINK DRAFT.kicad_pcb`.

Change details:

- `Codex Review Outputs\20260430_210726\footprint_reference_map.csv`
- `Codex Review Outputs\20260430_210726\physical_drc_fix_changes.txt`

## Final ERC

```powershell
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\run_erc.ps1 -ProjectPath "C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK" -OutputRoot "C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_210726\final_verification"
```

Result:

- Exit code 0.
- 0 errors.
- 0 warnings.

## Final DRC

```powershell
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\run_drc.ps1 -ProjectPath "C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK" -OutputRoot "C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_210726\final_verification"
```

Result:

- Exit code 0.
- 0 DRC violations.
- 0 unconnected pads.
- 0 footprint errors.

## NOT_FINAL Export Commands

The exact export commands and output from KiCad CLI are recorded in:

`C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_210726\new_outputs_NOT_FINAL\export_commands.log`

Exports:

- Gerbers: exit code 0.
- Excellon drill: exit code 0.
- BOM: exit code 0.
- Pick-and-place: exit code 0.
- Schematic PDF: exit code 0.
- PCB layer PDF: exit code 0.
- STEP: exit code 0, with missing 3D model warnings for J2, J3, J4, and L1.

## Output Comparison

Comparison command generated:

`C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_210726\output_comparison_summary.md`

Comparison summary:

- Only old: 1 file.
- Only new: 2 report files.
- Changed common files: 22.
- PNP package metadata changes: 37.
- PNP position/rotation/side changes: 0.
