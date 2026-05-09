# Historical Paths Portability Report

Date: `2026-05-09`
Task type: `DOCS_ONLY`
Repo root: `.`

## Goal

Prevent old absolute local paths in tracked evidence from being misread as current setup instructions for ZIP users or AI agents.

## Search Scope

Tracked files were scanned for:

- `C:\Users\LJ`
- `C:/Users/LJ`
- absolute Windows KiCad install roots
- user-global KiCad config path patterns

## Classification Summary

| Category | Files with findings | Match count | Decision |
| --- | ---: | ---: | --- |
| `ACTIVE_ONBOARDING_DOC` | `3` | `27` | Keep portable. Add explicit warnings and current-machine discovery guidance. |
| `ACTIVE_SCRIPT` | `13` | `29` | Keep dynamic/configurable. Remove fixed-path bias where it still mattered. |
| `ACTIVE_CONFIG` | `110` | `883` | Mixed install-intelligence, prompts, example docs, and project evidence. Leave audit/example content intact unless it acts like onboarding. |
| `GENERATED_INDEX` | `6` | `12` | Treat as machine-generated reference, not current setup truth. |
| `HISTORICAL_REPORT` | `276` | `49566` | Preserve unchanged as evidence. Do not rewrite blindly. |
| `EXAMPLE_ONLY` | `1` | `1` | Keep as example-only. |

Total tracked files with path findings: `409`

## What Was Fixed

### Startup And Onboarding

- Added a stronger startup rule in `00_CODEX_START/PATH_PORTABILITY_RULES.md`.
- Added public-facing guidance in `docs/PATH_PORTABILITY.md`.
- Updated `README.md`, `ONE_PROMPT_START.md`, and `00_CODEX_START/START_HERE.md` to warn that historical reports may show original local paths and that current work must use repo-relative paths plus live discovery.
- Updated `README_GPT.md`, `FOR CHAT GPT.MD`, and `01_MEMORY/GLOBAL_MEMORY.md` so future agents do not treat historical absolute paths as active configuration.

### Prompt Files

- Updated `.prompts/codex/01_AUDIT_KICAD_INSTALL.md` to require live discovery first and to treat `C:\Program Files\KiCad\*` only as fallback examples.
- Updated `.prompts/claude/01_AUDIT_KICAD_INSTALL.md` with the same discovery-first behavior.
- Updated `.prompts/shared/SAFETY_GATES.md` to require `00_CODEX_START/PATH_PORTABILITY_RULES.md` during startup and to treat historical absolute paths as non-authoritative.

### Live Script Hardening

- `03_TOOLS/scripts/kicad_app_audit/deep_kicad_folder_inventory.py`
  - removed the single fixed `C:\Program Files\KiCad\9.0` preference
  - now relies on `%ProgramFiles%\KiCad` version discovery plus CLI/PATH fallback
- `03_TOOLS/scripts/project_validation/validate_kicad_project.py`
  - removed the single fixed KiCad 9 executable preference from fallback detection
  - now walks `%ProgramFiles%\KiCad` dynamically after explicit/env/discovery probes

## What Was Left Unchanged On Purpose

Historical evidence was preserved instead of rewritten, including:

- `02_HISTORY/`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/history/`
- project `_verification` records
- sample-intake review reports
- archived test/sample review artifacts

These files are evidence records. Their historical absolute paths are part of the preserved command or review context.

## Validation

- `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'` -> no KiCad design files changed
- onboarding warning present in `README.md` and `ONE_PROMPT_START.md`
- startup path rule present in `00_CODEX_START/PATH_PORTABILITY_RULES.md`
- new public portability doc present at `docs/PATH_PORTABILITY.md`
- changed Python scripts syntax-checked after edits

## Remaining Gaps

1. Historical reports outside `02_HISTORY/`, including some project `reports/`, `_verification/`, and sample-intake artifacts, still contain absolute local paths by design.
2. `29_FOOTPRINT_GAP_ANALYSIS/GENERATED_INDEXES/` still contains machine-local generated inventory paths and should eventually receive the same placeholder-only treatment as other generated inventory folders.
3. Some install-intelligence docs under `03_TOOLS/kicad_app_intelligence/` still mention audited one-machine install paths. They are acceptable as audit/example content, but they should continue to be labeled as examples or audited-machine records rather than portable setup requirements.
