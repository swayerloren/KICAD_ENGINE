# COMMAND LINK Direct Edit Commands

Date: 2026-04-30

This command log summarizes the direct approved `COMMAND LINK` repair/review/re-export session. Full script output logs are in the timestamped project review folder.

## Paths

- Project: `C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK`
- Snapshot: `C:\Users\LJ\KICAD_ENGINE\99_BACKUPS\project_snapshots\COMMAND_LINK_DIRECT_EDIT_APPROVED_20260430_203134`
- Review folder: `C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_203134`
- New outputs: `C:\Users\LJ\KICAD_ENGINE\99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_203134\new_outputs_NOT_FINAL`

## Command Summary

- Created snapshot and original-output archive with PowerShell `Copy-Item`.
- Ran `find_kicad_project_files.ps1` against the project.
- Ran `backup_kicad_project.ps1` against the project.
- Ran baseline `run_erc.ps1`; KiCad returned exit code 5 with 2 warnings.
- Ran baseline `run_drc.ps1`; KiCad returned exit code 5 with 46 violations.
- Used KiCad Python `pcbnew.PCB_IO_KICAD_SEXPR().FootprintSave()` to export embedded U2 footprint to `ULN2803ADW.pretty`.
- Ran `run_erc.ps1` after library fix; KiCad returned exit code 5 with 1 warning.
- Ran `run_drc.ps1` after library fix; KiCad returned exit code 5 with 45 violations.
- Ran `run_erc.ps1` after `CAN_P` label fix; KiCad returned exit code 0.
- Ran `run_drc.ps1` after duplicate via fix; KiCad returned exit code 5 with 44 violations.
- Ran final `find_kicad_project_files.ps1`, `backup_kicad_project.ps1`, `run_erc.ps1`, and `run_drc.ps1`.
- Ran KiCad CLI exports for Gerbers, Excellon drills, BOM, position CSV, schematic PDF, PCB layer PDF, and STEP.

## Full Logs

- Final ERC: `Codex Review Outputs\20260430_203134\final_verification\erc_20260430_204227\script.log`
- Final DRC: `Codex Review Outputs\20260430_203134\final_verification\drc_20260430_204232\script.log`
- Export log: `Codex Review Outputs\20260430_203134\new_outputs_NOT_FINAL\export_commands_rerun.log`
- Failed export wrapper log retained: `Codex Review Outputs\20260430_203134\new_outputs_NOT_FINAL\export_commands.log`
