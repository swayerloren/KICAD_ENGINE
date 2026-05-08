# KiCad Installed App Deep Audit Commands

Date: 2026-05-02
Workspace: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Scope

Commands were used for read-only inspection of the installed KiCad app and for writing repo-local documentation/reports. No files were written under `C:\Program Files\KiCad`. No project design files were modified. No tools were installed.

## KiCad Executable Command

Only one KiCad executable command was run:

```powershell
& 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' version
```

Result:

```text
9.0.7
```

No ERC, DRC, export, package manager, plugin, or GUI command was run.

## Read-Only File Inspection

Read-only PowerShell inspections checked:

- Existence of `C:\Program Files\KiCad\9.0\etc`, `lib`, `share`, and `bin`.
- Executables and version metadata under `bin`.
- Top-level installed data under `share\kicad`.
- Stock symbol, footprint, 3D model, template, demo, scripting, schema, fontconfig, and ngspice files.
- User KiCad config/library table locations under `%APPDATA%\kicad\9.0`, `%LOCALAPPDATA%\kicad\9.0`, and `%USERPROFILE%\Documents\KiCad\9.0`.
- Stock and user-global library table entry counts.

## Script Verification

PowerShell parser checks were run against:

- `03_TOOLS\scripts\kicad_app_audit\audit_kicad_windows.ps1`
- `03_TOOLS\scripts\kicad_app_audit\check_kicad_cli.ps1`
- `03_TOOLS\scripts\kicad_app_audit\inventory_kicad_libraries.ps1`

Result: 0 parse errors after fixing `inventory_kicad_libraries.ps1`.

## Script Runs

Ran:

```powershell
& .\03_TOOLS\scripts\kicad_app_audit\audit_kicad_windows.ps1 -KiCadRoot 'C:\Program Files\KiCad\9.0'
```

Result:

- `05_OUTPUTS\kicad_app_audit\KICAD_WINDOWS_APP_AUDIT_20260502_160057.md`
- `05_OUTPUTS\kicad_app_audit\KICAD_WINDOWS_APP_AUDIT_20260502_160057.json`

Initial run of `inventory_kicad_libraries.ps1` failed because `Join-Path` calls in an array literal passed multiple child paths. The script was patched and syntax-checked.

Reran:

```powershell
& .\03_TOOLS\scripts\kicad_app_audit\inventory_kicad_libraries.ps1 -KiCadRoot 'C:\Program Files\KiCad\9.0'
```

Result:

- `05_OUTPUTS\kicad_app_audit\KICAD_LIBRARY_INVENTORY_20260502_160145.md`
- `05_OUTPUTS\kicad_app_audit\KICAD_SYMBOL_LIBRARIES_20260502_160145.csv`
- `05_OUTPUTS\kicad_app_audit\KICAD_FOOTPRINT_LIBRARIES_20260502_160145.csv`
- `05_OUTPUTS\kicad_app_audit\KICAD_3DMODEL_FOLDERS_20260502_160145.csv`
- `05_OUTPUTS\kicad_app_audit\KICAD_LIBRARY_TABLES_20260502_160145.csv`

`check_kicad_cli.ps1` was not run to avoid a second KiCad executable launch. It was syntax-checked only.
