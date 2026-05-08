# P0/P1 Repair Session

Date: 2026-05-03

Workspace: `C:\Users\LJ\GitHub\KICAD_ENGINE`

Task: create a prioritized repair plan from the full production-quality audit and fix only Priority 0 and Priority 1 issues.

## Scope

Allowed:

- Public-release safety gates.
- Startup and closeout routing fixes.
- Path drift fixes.
- Placeholder/index fixes in core systems.
- API-safe supplier/Playwright documentation checks.
- Script dry-run and syntax validation.

Not allowed:

- KiCad design file edits.
- Datasheet downloads.
- Tool installs.
- Web scraping.
- Manufacturing output generation.
- Mass rewrite of the repo.

## Work Completed

- Created `05_OUTPUTS/release_readiness/P0_P1_REPAIR_PLAN.md`.
- Added root `.gitignore` for secrets, local environments, generated outputs, backups, installer build outputs, unreviewed PDFs, and manufacturing-style artifacts.
- Added `17_RELEASE_BUILD/PUBLIC_RELEASE_EXCLUSION_MANIFEST.md`.
- Added `06_DATASHEETS/00_INDEX/REDISTRIBUTION_REVIEW_REQUIRED.md`.
- Normalized active startup/handoff/config paths to the current checkout and created `00_CODEX_START/PATH_PORTABILITY_RULES.md`.
- Updated setup install helpers so default behavior is dry-run and explicit apply flags are required before package-manager installs.
- Replaced core placeholder/TODO rows in datasheet index files and prompt/index files with actionable status records or explicit template notation.
- Added `.codex/config.example.toml` and updated `.codex/config.toml` to current checkout paths.
- Updated `CURRENT_KNOWN_PROBLEMS.md` and `FOR CHAT GPT.MD` with P0/P1 repair status.
- Ran safe validation scans.

## KiCad Design File Safety

No `.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, KiCad symbol, KiCad footprint, Gerber, drill, STEP, PNP/CPL, or manufacturing output file was edited.

## Result

P0/P1 repairs are complete for the scoped audit items. Public release remains blocked until the remaining backlog and human legal/release review are complete.
