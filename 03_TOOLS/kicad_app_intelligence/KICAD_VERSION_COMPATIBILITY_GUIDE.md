# KiCad Version Compatibility Guide

Date: 2026-05-03

Purpose: keep Codex, Claude, and scripts realistic when the user's KiCad version differs from this repo's KiCad 9 Windows audit baseline.

## Current Baseline

Observed local baseline:

- KiCad install root: `C:\Program Files\KiCad\9.0`
- `kicad-cli version`: `9.0.7`
- Stock symbols: `${KICAD9_SYMBOL_DIR}`
- Stock footprints: `${KICAD9_FOOTPRINT_DIR}`
- Stock 3D models: `${KICAD9_3DMODEL_DIR}`

This baseline is evidence for this machine, not a universal assumption.

## What Must Be Detected Per Machine

Every agent or script should detect:

- Installed KiCad root.
- `kicad-cli` path.
- `kicad-cli version`.
- Stock symbol directory.
- Stock footprint directory.
- Stock 3D model directory.
- User-global KiCad config directory.
- Project-local library tables.

Do not hardcode `9.0` unless the task is explicitly KiCad 9-specific.

## Version Drift Risks

| Drift area | Risk | Agent response |
| --- | --- | --- |
| CLI syntax | ERC, DRC, export, render, or jobset options may change. | Run version/help discovery and prefer version-aware wrappers. |
| Path variables | `${KICAD9_*}` variables may differ in KiCad 8, KiCad 10, nightly, or custom packages. | Resolve variables from library tables and app config, not guesses. |
| Symbol library contents | Symbols may be added, removed, renamed, or edited. | Index the installed library for the user's version. |
| Footprint library contents | Footprints may be added, removed, renamed, or altered. | Verify exact footprint file and package drawing. |
| 3D model paths | Model filenames and folders may change. | Check existence and keep missing model warnings separate from fab blockers. |
| File formats | KiCad S-expressions and library formats can evolve. | Avoid ad hoc rewrites; use KiCad-aware parsers/tools where possible. |
| `pcbnew` Python | Python API availability and behavior can change. | Detect importability and version before relying on it. |
| Installed examples | Demo/template projects may change across versions. | Treat demos as examples only. |
| User global tables | A user's global config may point to private or old libraries. | Resolve and document dependencies; do not edit globals. |

## Command Compatibility Rules

Before running project commands:

1. Capture `kicad-cli version`.
2. Check wrapper support for that version.
3. Use explicit input and output paths.
4. Keep outputs outside project source unless approved.
5. Log exact commands and exit codes.

Allowed default discovery:

```powershell
& "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe" version
& "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe" --help
```

For non-Windows or non-KiCad-9 systems, replace the path with the detected `kicad-cli`.

## Library Compatibility Rules

Do not assume a symbol or footprint exists because it exists in another KiCad version.

For every project:

1. Resolve project-local library tables.
2. Resolve user-global library tables read-only if needed.
3. Resolve stock libraries from the installed KiCad version.
4. Record the resolved file path.
5. Verify symbols and footprints against datasheets/package drawings before approval.

## Project Migration Risks

Opening or saving an older KiCad project in a newer KiCad can update project files. Agents must not trigger format upgrades unless the user explicitly asks for migration and backups exist.

Never run these against installed stock libraries:

```text
kicad-cli fp upgrade
kicad-cli sym upgrade
```

Only run upgrade commands on copied project-local libraries after explicit approval, backup, and review.

## Compatibility Labels For Reports

Use these labels:

- `KICAD_VERSION_DETECTED`
- `KICAD_VERSION_UNVERIFIED`
- `CLI_SYNTAX_VERIFIED_FOR_THIS_VERSION`
- `CLI_SYNTAX_UNVERIFIED_FOR_THIS_VERSION`
- `STOCK_LIBRARY_RESOLVED`
- `PROJECT_LOCAL_LIBRARY_RESOLVED`
- `GLOBAL_LIBRARY_DEPENDENCY`
- `FORMAT_MIGRATION_RISK`

## Future KiCad Versions

For KiCad 10 or later:

- Re-run `deep_kicad_folder_inventory.py`.
- Rebuild symbol, footprint, and 3D model indexes.
- Update path-variable assumptions.
- Re-test ERC, DRC, BOM, Gerber, drill, STEP, and render wrappers.
- Treat any auto-migration prompts as project-source edit risks.

## External Reference Links

- KiCad 9 documentation: https://docs.kicad.org/9.0/
- KiCad current documentation: https://docs.kicad.org/
- KiCad downloads by platform: https://www.kicad.org/download/
