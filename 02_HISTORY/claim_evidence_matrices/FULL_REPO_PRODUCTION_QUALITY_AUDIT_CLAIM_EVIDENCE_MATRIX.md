# Claim Evidence Matrix - Full Repo Production Quality Audit

Date: `2026-05-03`

| Claim | Status | Evidence | Human review required |
|---|---|---|---|
| All requested top-level folders exist. | `VERIFIED_BY_COMMAND` | Root inventory and scan summary show no missing requested top-level folders. | No |
| Repo is not public GitHub release ready. | `PARTIALLY_VERIFIED` | Placeholder counts, unreviewed PDFs, no git metadata, blocked project, installer limitations. | Yes |
| Active ESP32 project is blocked before PCB update. | `VERIFIED_BY_FILE` | `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`, `PCB_UPDATE_FROM_SCHEMATIC_REPORT.md`, `FOOTPRINT_PACKAGE_AUDIT.md`. | No |
| Active ESP32 project has no PCB file. | `VERIFIED_BY_FILE` | Gate report, final PCB verification report, and project file listing. | No |
| Script syntax mostly passes. | `VERIFIED_BY_COMMAND` | `script_syntax_validation_summary.json`: 286 pass, 4 fail, 37 Bash unavailable. | Yes for shell scripts |
| Two datasheet PDFs exist in `06_DATASHEETS`. | `VERIFIED_BY_COMMAND` | PDF scan under `06_DATASHEETS/99_UNSORTED_INBOX/.../ESPRESSIF`. | Yes for redistribution |
| Current workspace is not a git repo. | `VERIFIED_BY_COMMAND` | `git status --short` returned fatal not-a-git-repository. | No |
| Playwright live capture is blocked locally. | `VERIFIED_BY_FILE` | `31_PLAYWRIGHT_RESEARCH_PIPELINE/reports/PILOT_LIVE_RESEARCH_REPORT.md`. | No |
| Windows installer prototype exists. | `VERIFIED_BY_FILE` | `installer/build/windows/WINDOWS_BUILD_STATUS.md` and artifact listing. | Yes before release |
| Security/legal readiness is not closed. | `PARTIALLY_VERIFIED` | Secret-like hit sample, PDFs, third-party repos, legal docs. | Yes |
