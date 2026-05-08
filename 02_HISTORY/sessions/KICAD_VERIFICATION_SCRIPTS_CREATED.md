# KiCad Verification Scripts Created

Date: 2026-04-30 15:27:46 -04:00
Workspace: `C:\Users\LJ\KICAD_ENGINE`

## Scope
- Created safe PowerShell scripts for KiCad verification, backup, file discovery, and not-final exports.
- Did not install dependencies.
- Did not configure MCP.
- Did not edit KiCad project files.
- Did not run scripts against a real KiCad project.
- Did not generate final manufacturing outputs.

## Files Created
- `03_TOOLS\scripts\kicad_automation_common.ps1`
- `03_TOOLS\scripts\run_erc.ps1`
- `03_TOOLS\scripts\run_drc.ps1`
- `03_TOOLS\scripts\export_gerbers.ps1`
- `03_TOOLS\scripts\export_drill.ps1`
- `03_TOOLS\scripts\export_step.ps1`
- `03_TOOLS\scripts\export_bom.ps1`
- `03_TOOLS\scripts\full_verify_project.ps1`
- `03_TOOLS\scripts\backup_kicad_project.ps1`
- `03_TOOLS\scripts\find_kicad_project_files.ps1`

## File Updated
- `00_CODEX_START\TOOL_INDEX.md`

## Safety Characteristics
- Every entry script accepts `-ProjectPath`.
- Scripts fail if `ProjectPath` does not exist.
- Scripts resolve `kicad-cli` from PATH, search `C:\Program Files\KiCad`, or accept `-KiCadCliPath`.
- Scripts write timestamped report or output folders.
- Scripts do not delete source files.
- Export scripts mark outputs as not final.
- Backup script writes to `99_BACKUPS\pre_codex_edits\PROJECT_NAME_TIMESTAMP` and does not delete older backups.
- Scripts return non-zero exit codes on failure.

## Checks Run
- PowerShell parser syntax checks passed for all scripts.
- Static scan found no destructive delete commands such as `Remove-Item`, `del`, `erase`, `rmdir`, or `rd`.

## Revalidation
Date: 2026-04-30 15:32:27 -04:00

- Confirmed all nine requested entry scripts still exist in `03_TOOLS\scripts`.
- Confirmed every entry script accepts `-ProjectPath`.
- Confirmed every entry script has a non-zero failure exit path.
- Confirmed every entry script uses the shared KiCad CLI check path or directly resolves `kicad-cli`.
- Re-ran PowerShell parser syntax checks; all scripts passed.
- Re-ran a scoped destructive-command scan on workspace `.ps1` files; no delete commands were found.
- Did not run scripts against a real KiCad project.
- Did not edit KiCad project files.
- Did not generate manufacturing outputs.

## Not Tested Yet
- No script was run against a real project.
- KiCad CLI command behavior was not validated on a sample project in this session.

## Recommended Next Test
Create or use a disposable/sample KiCad project, then run `find_kicad_project_files.ps1` first. If that passes, run `backup_kicad_project.ps1`, then `run_erc.ps1` and `run_drc.ps1`. Only after those pass should the not-final export scripts be tested.
