# P0/P1 Repair Summary

Date: 2026-05-03

## Result

Priority 0 and Priority 1 issues identified from the full production-quality audit were repaired where they were narrow, evidence-backed, and safe to change without touching KiCad design files.

Public GitHub release remains `NOT_READY`.

## P0 Fixed

- Added root `.gitignore`.
- Added `17_RELEASE_BUILD/PUBLIC_RELEASE_EXCLUSION_MANIFEST.md`.
- Added `06_DATASHEETS/00_INDEX/REDISTRIBUTION_REVIEW_REQUIRED.md`.
- Blocked unreviewed migrated Espressif PDFs from public release payloads.
- Blocked generated outputs, local environments, third-party repos, backups, installer build outputs, unreviewed PDFs, and historical token-placeholder command logs from public payloads.
- Normalized active startup/handoff/config docs to the current checkout path.
- Added `00_CODEX_START/PATH_PORTABILITY_RULES.md`.
- Updated install helper scripts so package-manager installation is dry-run by default and requires explicit apply flags.
- Updated README status so the repo does not overclaim public readiness.
- Updated supplier/Playwright docs to keep browser/API output source-link-only and unverified until official/human review.

## P1 Fixed

- Replaced core datasheet `TODO` rows with useful records.
- Replaced weak `07_REFERENCE_DESIGNS/INDEX.md` and `17_RELEASE_BUILD/INDEX.md`.
- Corrected sample project paths from `active/` to `archive/`.
- Replaced unresolved prompt/task placeholders with explicit `<project-id>` notation or current active-project defaults.
- Created `.codex/config.example.toml`.
- Updated `.codex/config.toml` to current checkout paths.
- Validated `.vscode/tasks.json`.

## Files Changed

Key files changed include:

- `.gitignore`
- `.codex/config.toml`
- `.codex/config.example.toml`
- `.codex/prompts/CREATE_REAL_KICAD_PROJECT_FROM_REQUIREMENTS.md`
- `.codex/prompts/NEW_KICAD_PROJECT.md`
- `.prompts/codex/02_CREATE_NEW_PROJECT_WORKSPACE.md`
- `.prompts/codex/05_PLAN_SCHEMATIC.md`
- `.vscode/tasks.json`
- `README.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `PUBLIC_RELEASE_CHECKLIST.md`
- `DATASHEET_REDISTRIBUTION_AUDIT.md`
- `installer/payload/PAYLOAD_CONTENT_RULES.md`
- `setup/windows/install_missing_windows_tools.ps1`
- `setup/windows/setup_windows.ps1`
- `setup/windows/README.md`
- `setup/macos/install_missing_macos_tools.sh`
- `setup/macos/setup_macos.sh`
- `setup/macos/README.md`
- `setup/linux/install_missing_linux_tools.sh`
- `setup/linux/setup_linux.sh`
- `setup/linux/README.md`
- `00_CODEX_START/START_HERE.md`
- `00_CODEX_START/SESSION_START_CHECKLIST.md`
- `00_CODEX_START/CURRENT_PROJECT.md`
- `00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md`
- `00_CODEX_START/PATH_PORTABILITY_RULES.md`
- `00_CODEX_START/PROJECT_INDEX.md`
- `00_CODEX_START/TOOL_INDEX.md`
- `00_CODEX_START/WORKFLOW_RULES.md`
- `00_CODEX_START/MEMORY_INDEX.md`
- `00_CODEX_START/HISTORY_INDEX.md`
- `06_DATASHEETS/00_INDEX/INDEX.md`
- `06_DATASHEETS/00_INDEX/MISSING.md`
- `06_DATASHEETS/00_INDEX/SOURCES.md`
- `06_DATASHEETS/00_INDEX/DUPLICATES_AND_REVISIONS.md`
- `06_DATASHEETS/00_INDEX/MASTER_DATASHEET_INDEX.md`
- `06_DATASHEETS/00_INDEX/REDISTRIBUTION_REVIEW_REQUIRED.md`
- `07_REFERENCE_DESIGNS/INDEX.md`
- `17_RELEASE_BUILD/README.md`
- `17_RELEASE_BUILD/INDEX.md`
- `17_RELEASE_BUILD/PUBLIC_RELEASE_EXCLUSION_MANIFEST.md`

## Validation Results

- Required file/folder presence: PASS.
- Targeted broken-reference scan: PASS, 0 findings.
- Targeted placeholder scan: PASS, 0 findings.
- PowerShell parser validation: PASS for checked scripts.
- Python syntax validation: PASS after rerun with Python files only.
- Node syntax validation: PASS.
- VS Code tasks JSON validation: PASS.
- Windows install helper dry-run: PASS; no install performed.
- Secret scan: no active credentials identified; historical placeholder token strings remain in an old command log and are now release-excluded.

## Remaining Blockers

- Public release is still blocked.
- Legal/human review is still required for migrated PDFs.
- Historical logs and generated outputs need public-release pruning or curated replacement.
- Bash script validation still needs macOS/Linux or shellcheck-style tooling.
- Broad scaffold cleanup remains.
- Active `ESP32_CSI_WIFI_NODE` design remains blocked before PCB update.

Final quality status for this repair pass: `MEDIUM_RISK`.
