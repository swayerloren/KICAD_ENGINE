# KiCad Installed App Deep Audit Session

Date: 2026-05-02
Workspace: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Scope

Deep read-only audit of the installed KiCad 9 Windows app so KiCad Engine can teach Codex, Claude, and similar VS Code-based agents how to use a user's installed KiCad app from VS Code.

## Startup Context

- Read `AGENTS.md`.
- Read `00_CODEX_START/PRODUCT_VISION.md`.
- Read `00_CODEX_START/KICAD_ENGINE_ARCHITECTURE.md`.
- Confirmed requested install paths exist:
  - `C:\Program Files\KiCad\9.0\etc`
  - `C:\Program Files\KiCad\9.0\lib`
  - `C:\Program Files\KiCad\9.0\share`
  - `C:\Program Files\KiCad\9.0\bin`

## Files Created

- `02_HISTORY/design_reviews/KICAD_INSTALLED_APP_DEEP_AUDIT.md`
- `02_HISTORY/command_logs/KICAD_INSTALLED_APP_DEEP_AUDIT_COMMANDS.md`
- `03_TOOLS/kicad_app_intelligence/KICAD_9_WINDOWS_PATH_MAP.md`
- `03_TOOLS/kicad_app_intelligence/KICAD_CLI_COMMANDS_REFERENCE.md`
- `03_TOOLS/kicad_app_intelligence/KICAD_LIBRARY_DISCOVERY_GUIDE.md`
- `03_TOOLS/kicad_app_intelligence/KICAD_DO_NOT_TOUCH_RULES.md`
- `03_TOOLS/scripts/kicad_app_audit/audit_kicad_windows.ps1`
- `03_TOOLS/scripts/kicad_app_audit/check_kicad_cli.ps1`
- `03_TOOLS/scripts/kicad_app_audit/inventory_kicad_libraries.ps1`

## Files Updated

- `00_CODEX_START/TOOL_INDEX.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`

## Backups Created

- `99_BACKUPS/pre_codex_edits/00_CODEX_START_TOOL_INDEX.md_before_kicad_app_audit_20260502_160204.md`
- `99_BACKUPS/pre_codex_edits/README_GPT.md_before_kicad_app_audit_20260502_160204.md`
- `99_BACKUPS/pre_codex_edits/FOR_CHAT_GPT.MD_before_kicad_app_audit_20260502_160204.md`

## Generated Outputs

- `05_OUTPUTS/kicad_app_audit/KICAD_WINDOWS_APP_AUDIT_20260502_160057.md`
- `05_OUTPUTS/kicad_app_audit/KICAD_WINDOWS_APP_AUDIT_20260502_160057.json`
- `05_OUTPUTS/kicad_app_audit/KICAD_LIBRARY_INVENTORY_20260502_160145.md`
- `05_OUTPUTS/kicad_app_audit/KICAD_SYMBOL_LIBRARIES_20260502_160145.csv`
- `05_OUTPUTS/kicad_app_audit/KICAD_FOOTPRINT_LIBRARIES_20260502_160145.csv`
- `05_OUTPUTS/kicad_app_audit/KICAD_3DMODEL_FOLDERS_20260502_160145.csv`
- `05_OUTPUTS/kicad_app_audit/KICAD_LIBRARY_TABLES_20260502_160145.csv`

## Key Findings

- `kicad-cli version` reports `9.0.7`.
- Stock symbols: 224 `.kicad_sym` files.
- Stock footprints: 155 `.pretty` folders with 15,415 `.kicad_mod` files.
- Stock 3D models: 105 `.3dshapes` folders with 14,043 files.
- Stock templates and demos are present and should be treated as read-only examples.
- User-global KiCad 9 library tables live under `%APPDATA%\kicad\9.0`.
- Current process environment did not expose `KICAD*` variables; agents should resolve KiCad variables through install-root knowledge and library tables, not shell assumptions.

## Safety Result

- No files were modified under `C:\Program Files\KiCad`.
- No KiCad project design files were modified.
- No tools were installed.
- No datasheets were downloaded.
- No ERC, DRC, export, GUI, package manager, or plugin command was run.
