# P0/P1 Repair Commands

Date: 2026-05-03

Workspace: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Read/Audit Commands

- Read prior audit outputs from:
  - `02_HISTORY/design_reviews/FULL_REPO_PRODUCTION_QUALITY_AUDIT.md`
  - `05_OUTPUTS/release_readiness/FULL_REPO_BLOCKERS.md`
  - `05_OUTPUTS/release_readiness/FULL_REPO_WEAK_FILES.csv`
  - `05_OUTPUTS/release_readiness/FULL_REPO_EMPTY_OR_PLACEHOLDER_FILES.csv`
  - `05_OUTPUTS/release_readiness/FULL_REPO_BROKEN_REFERENCES.csv`
  - `05_OUTPUTS/release_readiness/FULL_REPO_SCRIPT_AUDIT.csv`
  - `05_OUTPUTS/release_readiness/FULL_REPO_NEXT_FIX_PLAN.md`
- Used `Get-Content`, `Select-String`, `Get-ChildItem`, and `Import-Csv` to inspect current P0/P1 targets.

## Edit Commands

- Used `apply_patch` for manual doc/config/script changes.
- Used a bounded PowerShell mechanical replacement for old checkout path normalization in `README_GPT.md` and `FOR CHAT GPT.MD`.

## Validation Commands

PowerShell syntax validation:

```powershell
[System.Management.Automation.Language.Parser]::ParseFile(...)
```

Result:

- `setup/windows/install_missing_windows_tools.ps1`: PASS
- `setup/windows/setup_windows.ps1`: PASS
- `03_TOOLS/kicad/run_schematic_visual_check.ps1`: PASS
- `installer/payload/build_payload.ps1`: PASS

Python syntax validation:

```powershell
python -m py_compile 03_TOOLS/scripts/project_validation/validate_kicad_project.py 03_TOOLS/scripts/ai_quality/ai_quality_common.py 03_TOOLS/scripts/memory_history/memory_history_common.py 03_TOOLS/scripts/kicad_schematic_checks/check_schematic_annotation.py 03_TOOLS/scripts/kicad_schematic_checks/check_schematic_completeness.py 03_TOOLS/scripts/visual/generate_schematic_closeups.py installer/payload/build_payload.py 28_SUPPLIER_INGESTION/scripts/normalize_supplier_part.py
```

Result: PASS after correcting an earlier command that accidentally included a JavaScript file.

Node syntax validation:

```powershell
node --check 31_PLAYWRIGHT_RESEARCH_PIPELINE/scripts/dry_run_research_plan.js
node --check 31_PLAYWRIGHT_RESEARCH_PIPELINE/scripts/browser_research_public_page.js
```

Result: PASS.

VS Code tasks JSON validation:

```powershell
python -m json.tool .vscode/tasks.json
```

Result: PASS.

Dry-run installer check:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File setup/windows/install_missing_windows_tools.ps1 -Tools git
```

Result: PASS. Script ran in default dry-run mode and did not install anything.

Targeted broken-reference scan:

- Scope: startup/handoff/release/datasheet index files changed in this repair pass.
- Result: `BROKEN_REFERENCE_SCAN_FINDINGS 0`.

Targeted placeholder scan:

- Scope: repaired core prompts, startup files, README_GPT, FOR CHAT GPT, VS Code tasks, datasheet index files, and release index files.
- Result: `PLACEHOLDER_SCAN_FINDINGS 0`.

Secret scan:

```powershell
rg -n --hidden --glob '!03_TOOLS/python_envs/**' --glob '!03_TOOLS/node_envs/**' --glob '!03_TOOLS/repos/**' --glob '!03_TOOLS/windows/repos/**' --glob '!05_OUTPUTS/installer_smoke_test/**' --glob '!99_BACKUPS/**' --glob '!node_modules/**' --glob '!installer/node_modules/**' --glob '!**/*.pdf' --glob '!**/*.zip' --glob '!**/*.exe' --glob '!**/*.dll' --glob '!**/*.pyc' '(?i)(api[_-]?key|token|password|secret|credential)\s*[:=]\s*[A-Za-z0-9_./+=-]{16,}' .
```

Result:

- No active credential was identified.
- The scan found placeholder token strings copied into `02_HISTORY/command_logs/KICAD_MCP_PRO_INSTALL_COMMANDS.md` from third-party `.env.example` and docs output.
- That historical log is now explicitly blocked from public release payloads by `17_RELEASE_BUILD/PUBLIC_RELEASE_EXCLUSION_MANIFEST.md`.

Git status:

```powershell
git status --short
```

Result: failed because this checkout is not a git repository. No repo state diff was available.

KiCad design/source file timestamp inventory:

```powershell
Get-ChildItem -Path '04_KICAD_PROJECTS' -Recurse -File -Include *.kicad_pro,*.kicad_sch,*.kicad_pcb,*.kicad_sym,*.kicad_mod,*.gbr,*.drl,*.step,*.stp
```

Result: read-only inventory only. No KiCad design files were intentionally edited in this P0/P1 repair pass; no git metadata was available to produce a formal diff.

## Failed Validation Commands

Documented in `02_HISTORY/failed_attempts/P0_P1_REPAIR_VALIDATION_COMMAND_MISTAKES.md`.
