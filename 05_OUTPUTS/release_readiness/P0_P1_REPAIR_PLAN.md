# P0/P1 Repair Plan

Date: `2026-05-03`

Source audit files:

- `02_HISTORY/design_reviews/FULL_REPO_PRODUCTION_QUALITY_AUDIT.md`
- `05_OUTPUTS/release_readiness/FULL_REPO_BLOCKERS.md`
- `05_OUTPUTS/release_readiness/FULL_REPO_WEAK_FILES.csv`
- `05_OUTPUTS/release_readiness/FULL_REPO_EMPTY_OR_PLACEHOLDER_FILES.csv`
- `05_OUTPUTS/release_readiness/FULL_REPO_BROKEN_REFERENCES.csv`
- `05_OUTPUTS/release_readiness/FULL_REPO_SCRIPT_AUDIT.csv`
- `05_OUTPUTS/release_readiness/FULL_REPO_NEXT_FIX_PLAN.md`

## Scope Limit

This pass fixes only P0 and P1 issues that are narrow, safe, and directly supported by the audit. It will not rewrite the repo, delete user work, edit KiCad design files, download datasheets, install tools, scrape websites, or generate manufacturing outputs.

## P0 Repairs

| Priority | Issue | Planned fix | Files |
|---|---|---|---|
| P0 | Public release payload is not clean. | Add root ignore policy and release exclusion manifest; tighten payload/release rules so envs, repos, generated outputs, backups, build artifacts, unreviewed PDFs, and secrets are excluded. | `.gitignore`, `17_RELEASE_BUILD/PUBLIC_RELEASE_EXCLUSION_MANIFEST.md`, `installer/payload/PAYLOAD_CONTENT_RULES.md`, `PUBLIC_RELEASE_CHECKLIST.md` |
| P0 | Datasheet redistribution review is open. | Record the two legacy migrated Espressif PDFs as blocked from public payload until human redistribution review or link-only conversion. | `06_DATASHEETS/00_INDEX/REDISTRIBUTION_REVIEW_REQUIRED.md`, `DATASHEET_REDISTRIBUTION_AUDIT.md` |
| P0 | Current project startup path is stale. | Update active project path to current workspace path and add path-portability startup rules. | `00_CODEX_START/CURRENT_PROJECT.md`, `00_CODEX_START/PATH_PORTABILITY_RULES.md`, `00_CODEX_START/START_HERE.md`, `00_CODEX_START/SESSION_START_CHECKLIST.md` |
| P0 | Install scripts can still install after prompt without a dry-run mode being the default on macOS/Linux and inconsistent on Windows. | Require explicit `--apply`/`-Apply` for installation. Default mode prints commands and exits without installing. | `setup/windows/install_missing_windows_tools.ps1`, `setup/macos/install_missing_macos_tools.sh`, `setup/linux/install_missing_linux_tools.sh` |
| P0 | Public README must not overclaim readiness. | Add explicit audit status block. | `README.md` |
| P0 | Supplier/Playwright live research must remain evidence, not truth. | Confirm/update safety language and live-mode blockers. | `31_PLAYWRIGHT_RESEARCH_PIPELINE/README.md`, `28_SUPPLIER_INGESTION/README.md` |

## P1 Repairs

| Priority | Issue | Planned fix | Files |
|---|---|---|---|
| P1 | Core memory/history indexes include `PROJECT_NAME` placeholders without clear template labeling. | Rewrite required project path sections as template patterns and list the real active project separately. | `00_CODEX_START/MEMORY_INDEX.md`, `00_CODEX_START/HISTORY_INDEX.md` |
| P1 | Datasheet index README is a generated `$rel`/`$name` placeholder. | Replace with actual useful 00_INDEX guidance. | `06_DATASHEETS/00_INDEX/README.md` |
| P1 | Broken references and old-path drift in core startup docs. | Fix current active project and add path rules rather than rewriting old history logs. | `00_CODEX_START/*`, `README_GPT.md`, `FOR CHAT GPT.MD` |
| P1 | Script safety audit needs first-party validation after edits. | Run parser/syntax validation and secret/path scans. | validation outputs |

## Explicitly Deferred To P2/P3

- Rewriting every thin README/INDEX file.
- Filling component/datasheet records with verified engineering data.
- Verifying footprints against package drawings.
- Removing generated historical outputs.
- Cleaning third-party/vendored repositories.
- Building/signing installers.
- Repairing the `ESP32_CSI_WIFI_NODE` design gate.
- Running live Playwright or supplier API capture.
