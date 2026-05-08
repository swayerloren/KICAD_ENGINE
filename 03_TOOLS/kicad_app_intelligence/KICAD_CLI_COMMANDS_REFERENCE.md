# KiCad CLI Commands Reference

Date: 2026-05-02
Audited executable: `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe`
Version command result: `9.0.7`

## Scope

This reference is for Codex, Claude, and other agents using a user's installed KiCad app from VS Code or a local terminal. During the audit, only `kicad-cli version` was executed. No ERC, DRC, export, project, schematic, PCB, or GUI action was run.

Agents must treat command examples here as workflow references. Before using any command on a real project, confirm active project, target files, output paths, backup state, and verification purpose.

## Path Resolution

Preferred detection order:

1. Explicit user-provided `-KiCadRoot` or `-KiCadCliPath`.
2. `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe` for KiCad 9.
3. Highest installed `C:\Program Files\KiCad\<version>\bin\kicad-cli.exe`.
4. `kicad-cli.exe` found on `PATH`.

Always quote Windows paths:

```powershell
& "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe" version
```

## Safe Discovery Command

Allowed for basic install confirmation:

```powershell
& "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe" version
```

Observed output:

```text
9.0.7
```

Note: Even simple KiCad executable invocations may touch user-level KiCad config timestamps. They must not write to `C:\Program Files\KiCad`, but agents should still avoid unnecessary executable calls.

## Common Command Families

KiCad CLI command families commonly used by automation include:

- `version`: report KiCad CLI version.
- `sch`: schematic operations such as ERC and schematic exports.
- `pcb`: PCB operations such as DRC and PCB/manufacturing exports.
- `sym`: symbol library operations.
- `fp`: footprint library operations.

Do not assume the exact option set across KiCad versions. Use the installed version's help only when the user authorizes command discovery, or rely on already validated scripts in `03_TOOLS/scripts`.

## Existing Workspace Script Mapping

KiCad Engine already wraps common CLI workflows:

| Workspace script | Intended KiCad CLI use | Authority |
| --- | --- | --- |
| `03_TOOLS/scripts/run_erc.ps1` | Schematic ERC | Active project required |
| `03_TOOLS/scripts/run_drc.ps1` | PCB DRC | Active project required |
| `03_TOOLS/scripts/export_bom.ps1` | BOM export for review | Active project required |
| `03_TOOLS/scripts/export_gerbers.ps1` | Gerber export into `NOT_FINAL` review folders | ERC/DRC gate required unless explicitly overridden |
| `03_TOOLS/scripts/export_drill.ps1` | Drill export into `NOT_FINAL` review folders | ERC/DRC gate required unless explicitly overridden |
| `03_TOOLS/scripts/export_step.ps1` | STEP export into review folders | Active project required |
| `03_TOOLS/scripts/full_verify_project.ps1` | Backup, ERC, DRC, BOM, Gerber, drill, STEP, and summary | Active project and backup gates required |

Agents should prefer these guarded workspace scripts over direct ad hoc `kicad-cli` commands for real project work.

## Read-Only Command Rules

Allowed without active project edit approval:

- Check whether `kicad-cli.exe` exists.
- Read file metadata for `kicad-cli.exe`.
- Run `kicad-cli version` when requested.
- Read installed docs, examples, library tables, and stock library files.

Not allowed without active project gates:

- Run ERC or DRC against a project if the task is not explicitly verification.
- Export Gerbers, drills, STEP, BOM, PDF, SVG, or manufacturing files.
- Run commands that write into project folders.
- Run commands against original finished PCB folders unless the user explicitly approves that scope.

## Real Project Guardrails

Before any project-targeted command:

1. Confirm active project name and path from `00_CODEX_START/CURRENT_PROJECT.md`.
2. Confirm target `.kicad_pro`, `.kicad_sch`, or `.kicad_pcb` is inside the active project folder.
3. Create or confirm a backup in `99_BACKUPS/pre_codex_edits`.
4. State output folder.
5. State whether outputs are `NOT_FINAL`.
6. Record command result in `02_HISTORY`.

## Output Folder Rules

For reports:

- `02_HISTORY/erc_drc_reports`
- `02_HISTORY/fabrication_reviews`
- `02_HISTORY/command_logs`
- Project-local `reports` folder when approved

For generated review artifacts:

- `05_OUTPUTS`
- Project-local `bom`, `fabrication`, or `renders` folders when approved

Never write generated outputs into `C:\Program Files\KiCad`.

## Direct CLI Use Pattern

Use explicit paths and quoted arguments:

```powershell
$KiCadCli = "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe"
& $KiCadCli version
```

For project commands, prefer existing scripts instead of raw CLI. When raw CLI is necessary, log the exact command, the KiCad CLI version, exit code, output folder, and whether source files were modified.

## Future Version Adaptation

For KiCad 10 or later:

- Detect the installed root dynamically.
- Capture the exact `kicad-cli version`.
- Re-check command syntax before using automation.
- Keep command wrappers version-aware.
- Treat changes in ERC/DRC/export output as compatibility risks until validated on sample projects.
