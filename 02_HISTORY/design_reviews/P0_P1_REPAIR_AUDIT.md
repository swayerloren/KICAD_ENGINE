# P0/P1 Repair Audit

Date: 2026-05-03

Status: `P0_P1_REPAIR_COMPLETE_WITH_REMAINING_RELEASE_BLOCKERS`

## Basis

This repair pass was based strictly on:

- `02_HISTORY/design_reviews/FULL_REPO_PRODUCTION_QUALITY_AUDIT.md`
- `05_OUTPUTS/release_readiness/FULL_REPO_BLOCKERS.md`
- `05_OUTPUTS/release_readiness/FULL_REPO_WEAK_FILES.csv`
- `05_OUTPUTS/release_readiness/FULL_REPO_EMPTY_OR_PLACEHOLDER_FILES.csv`
- `05_OUTPUTS/release_readiness/FULL_REPO_BROKEN_REFERENCES.csv`
- `05_OUTPUTS/release_readiness/FULL_REPO_SCRIPT_AUDIT.csv`
- `05_OUTPUTS/release_readiness/FULL_REPO_NEXT_FIX_PLAN.md`

## P0 Fixes

| P0 issue | Action | Status |
| --- | --- | --- |
| Public payload could include generated/tool/vendor/build folders | Added `.gitignore`, `17_RELEASE_BUILD/PUBLIC_RELEASE_EXCLUSION_MANIFEST.md`, and stronger payload exclusion docs. | FIXED_FOR_CURRENT_SCOPE |
| Unreviewed local PDFs could leak into public release | Added `06_DATASHEETS/00_INDEX/REDISTRIBUTION_REVIEW_REQUIRED.md`, updated datasheet audit and payload/release gates. | FIXED_AS_BLOCKING_GATE |
| Active docs mixed old and current checkout paths | Added `PATH_PORTABILITY_RULES.md`, normalized current startup/handoff/config docs, and updated current project path. | FIXED_FOR_ACTIVE_DOCS |
| Setup install scripts could appear install-capable by default | Windows/macOS/Linux install helpers now default to dry-run and require explicit apply flags. | FIXED |
| Public README could overclaim readiness | Root README now states `INTERNAL_ALPHA_READY` for private development and `NOT_READY` for public release. | FIXED |
| Supplier/Playwright docs needed safe-source posture | Supplier and Playwright README files now emphasize dry-run/API-safe/link-only behavior and evidence-not-truth rules. | FIXED |
| Historical command logs contain placeholder token strings | Added exclusion manifest rule blocking historical logs with placeholder token text from public payloads. | FIXED_AS_RELEASE_GATE |

## P1 Fixes

| P1 issue | Action | Status |
| --- | --- | --- |
| Core datasheet index files had literal `TODO` placeholder rows | Replaced with actionable tracking rows for source links, missing documents, migrated PDFs, and redistribution review. | FIXED |
| `07_REFERENCE_DESIGNS/INDEX.md` and `17_RELEASE_BUILD/INDEX.md` were generic/duplicated | Replaced with purpose-specific indexes. | FIXED |
| Project index pointed archived sample projects at `active/` | Corrected paths to `04_KICAD_PROJECTS/archive/...`. | FIXED |
| Prompt pack and VS Code task files contained unresolved `PROJECT_NAME` style placeholders | Replaced with explicit `<project-id>` notation or current active-project defaults. | FIXED |
| Missing `.codex/config.example.toml` referenced by payload rules | Created non-secret example config. | FIXED |
| `.vscode/tasks.json` needed runnable default project path and JSON validation | Default project path now points to the existing active project schematic project file; JSON validation passed. | FIXED |

## Validation

| Check | Result |
| --- | --- |
| Required file/folder presence | PASS |
| Targeted broken-reference scan | PASS, 0 findings |
| Targeted placeholder scan | PASS, 0 findings |
| PowerShell parser validation | PASS for checked scripts |
| Python syntax validation | PASS after correcting one mixed-file command mistake |
| Node syntax validation | PASS for checked Playwright scripts |
| VS Code tasks JSON validation | PASS |
| Windows optional installer dry-run | PASS, no install performed |
| Secret scan | No active credentials found; historical placeholder token text remains in old command log and is now release-excluded |
| Git diff/status | NOT_AVAILABLE, current checkout is not a git repository |

## Remaining Blockers

- Public release remains `NOT_READY`.
- Unreviewed local PDFs remain present but are blocked from public payloads until human redistribution review.
- Historical command logs with third-party placeholder token strings remain present but are blocked from public payloads.
- Broad placeholder/scaffold cleanup remains outside this P0/P1 pass.
- Bash syntax validation still requires macOS/Linux or shellcheck-capable environment.
- `ESP32_CSI_WIFI_NODE` remains blocked before PCB update.

## Classification

Current result: `INTERNAL_ALPHA_READY_WITH_P0_P1_GATES_REPAIRED`

Public release classification: `NOT_READY`
