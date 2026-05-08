# Deep KiCad App Folder Audit Report

Date: 2026-05-03

## Scope

Read-only audit of the installed KiCad app folders for AI-agent use from VS Code.

Audited Windows paths:

- `C:\Program Files\KiCad\9.0\bin`
- `C:\Program Files\KiCad\9.0\share`
- `C:\Program Files\KiCad\9.0\lib`
- `C:\Program Files\KiCad\9.0\etc`

No KiCad project source files were intentionally edited.

## Created Files

Documentation:

- `03_TOOLS/kicad_app_intelligence/DEEP_KICAD_APP_FOLDER_BREAKDOWN.md`
- `03_TOOLS/kicad_app_intelligence/KICAD_FOLDER_ROLE_MATRIX.md`
- `03_TOOLS/kicad_app_intelligence/KICAD_VERSION_COMPATIBILITY_GUIDE.md`
- `03_TOOLS/kicad_app_intelligence/KICAD_SYSTEM_VS_PROJECT_RESOURCE_RULES.md`
- `03_TOOLS/kicad_app_intelligence/KICAD_PATHS_WINDOWS_MAC_LINUX.md`

Script:

- `03_TOOLS/scripts/kicad_app_audit/deep_kicad_folder_inventory.py`

Generated inventory:

- `03_TOOLS/kicad_app_intelligence/generated/kicad_folder_inventory.windows.json`
- `03_TOOLS/kicad_app_intelligence/generated/kicad_executables.windows.json`
- `03_TOOLS/kicad_app_intelligence/generated/kicad_resource_summary.windows.json`
- `03_TOOLS/kicad_app_intelligence/generated/kicad_folder_inventory.windows.md`

## Commands Run

```powershell
& "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe" version
& "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe" --help
& "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe" sch --help
& "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe" pcb --help
& "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe" fp --help
& "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe" sym --help
& "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe" jobset --help
& "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe" version --help
python 03_TOOLS\scripts\kicad_app_audit\deep_kicad_folder_inventory.py --kicad-root "C:\Program Files\KiCad\9.0" --output-dir 03_TOOLS\kicad_app_intelligence\generated --platform-name windows
python -m py_compile 03_TOOLS\scripts\kicad_app_audit\deep_kicad_folder_inventory.py
python health_check.py --repo-root . --no-write
```

Only `kicad-cli` version/help commands were executed. No ERC, DRC, export, render, GUI automation, project command, or installer command was run.

## Key Findings

- `kicad-cli version` returned `9.0.7`.
- Top-level CLI commands observed: `fp`, `jobset`, `pcb`, `sch`, `sym`, `version`.
- `sch` exposes `erc` and `export`.
- `pcb` exposes `drc`, `export`, and `render`.
- `fp` and `sym` expose `export` and `upgrade`; upgrade commands are unsafe for installed stock libraries.
- `jobset` exposes `run`, which may generate outputs and must be controlled by explicit output paths.
- `bin` contains 18 `.exe` files, 1 `.bat` file, and 199 `.dll` files.
- Stock symbol library files: 223.
- Stock footprint library folders: 155.
- Stock footprint files: 15,415.
- Stock 3D model library folders: 105.
- Stock 3D model files: 14,043.
- Stock template folders: 19.
- Demo/example folders: 19.
- Installed scripting Python files: 20.
- `lib` contains crashpad/static library support and ngspice code models.
- `etc` contains fontconfig runtime configuration.

## Agent Safety Conclusions

- Installed KiCad folders are system resources and must be treated as read-only.
- `share\kicad\symbols`, `share\kicad\footprints`, and `share\kicad\3dmodels` are safe to index.
- `share\kicad\template`, `share\kicad\demos`, and `share\kicad\scripting` are safe to read and copy from, but only copied workspace/project versions may be edited.
- `bin`, `lib`, and `etc` should never be modified by Codex, Claude, setup scripts, or project automation.
- High-risk symbols/footprints should be copied into project-local libraries only after exact datasheet/package verification.
- Agents must resolve project-local library tables before user-global or stock libraries.

## Cross-Platform Documentation

The path guide now documents expected patterns for:

- Windows KiCad installs.
- macOS KiCad app bundles.
- Linux package installs.
- Linux Flatpak installs.
- Linux AppImage workflows.

The documentation explicitly treats non-Windows paths as expected patterns that must be detected on the user's machine.

## Validation

- Script compile: passed.
- KiCad Engine health check: `PASS=97 WARN=0 FAIL=0`.
- Generated JSON files were written under `03_TOOLS/kicad_app_intelligence/generated/`.
- Generated JSON files validated with `python -m json.tool`.
- Script hardened to refuse output folders inside the KiCad install root.

## Restrictions Observed

- Did not edit KiCad project source files.
- Did not install tools.
- Did not write into `C:\Program Files\KiCad`.
- Did not download datasheets.
- Did not generate fabrication outputs.

## Next Work

- Re-run the script on macOS and Linux machines to produce platform-specific generated JSON.
- Add CI/sample fixture tests for the inventory parser using copied metadata, not installed KiCad folders.
- Link the generated inventory into future agent task prompts where installed KiCad discovery is required.
