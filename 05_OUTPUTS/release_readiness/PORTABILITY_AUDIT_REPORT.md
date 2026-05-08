# Portability Audit Report

Date: `2026-05-08`
Task type: `GITHUB_DOCS_ONLY`
Repo root: `.`

## Goal

Make the GitHub repo usable as a normal ZIP download or `git clone` in VS Code without requiring hidden local-only folders, personal paths, or extra cloned GitHub repos for the basic workflow.

## Baseline Git Facts

- Current branch at audit start: `main`
- Origin URL: `https://github.com/swayerloren/KICAD_ENGINE.git`
- Local `HEAD` before remediation: `b8b661a3eec7d295a596b6dc790a315e904f0398`
- `origin/main` before remediation: `b8b661a3eec7d295a596b6dc790a315e904f0398`
- Local `main` matched `origin/main` before remediation: `YES`

## Portability Verdict

- ZIP-download portable after this docs/script hardening: `YES, WITH KNOWN LIMITATIONS`
- Extra cloned GitHub repos required for first use: `NO`
- Local KiCad install required for real GUI schematic/PCB work: `YES`
- Human KiCad review still required before fabrication: `YES`

## Local-Only Folder Audit

| Folder | Ignored | Tracked | Empty | Generated files | Required for basic workflow | Confirmed local-machine paths | Should be committed | README placeholder |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `03_TOOLS/node_envs` | `YES` | `YES, README only` | `NO` | `YES` | `NO` | `NO_CONFIRMED_HIT` | `NO` | `YES` |
| `03_TOOLS/python_envs` | `YES` | `YES, README only` | `NO` | `YES` | `NO` | `NO_CONFIRMED_HIT` | `NO` | `YES` |
| `03_TOOLS/repos` | `YES` | `YES, README only` | `NO` | `NO, but third-party clone payloads` | `NO` | `NO_CONFIRMED_HIT` | `NO` | `YES` |
| `03_TOOLS/tool_logs` | `YES` | `YES, README only` | `NO` | `YES` | `NO` | `YES` | `NO` | `YES` |
| `99_BACKUPS` | `YES` | `YES, docs only` | `NO` | `YES` | `NO` | `YES` | `NO` | `ALREADY_PRESENT` |
| `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work` | `PARTIAL, future scratch only` | `YES, large existing tracked payload` | `NO` | `YES` | `NO` | `NO_CONFIRMED_HIT` | `NO_NEW_SCRATCH_CONTENT` | `YES` |
| `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_rehearsals` | `YES` | `PLACEHOLDER ONLY AFTER THIS FIX` | `YES_BEFORE_PLACEHOLDER` | `EXPECTED_FUTURE_SCRATCH_ONLY` | `NO` | `NO` | `NO` | `YES` |

## Folder Size And Content Summary

| Folder | File count | Size bytes | Primary content | Recommendation |
| --- | ---: | ---: | --- | --- |
| `03_TOOLS/node_envs` | `11655` | `188707509` | local Node workspace, dependencies, build assets | Keep local-only. Do not push. |
| `03_TOOLS/python_envs` | `28712` | `720508017` | local virtual environments, site-packages, executables, caches | Keep local-only. Do not push. |
| `03_TOOLS/repos` | `5624` | `272132415` | cloned third-party helper repos and nested tool sources | Keep local-only. Do not push for baseline workflow. |
| `03_TOOLS/tool_logs` | `12` | `55193` | local health checks, setup notes, usage guides, config snippets | Keep local-only. Track README only. |
| `99_BACKUPS` | `4825` | `1251768383` | local backups, snapshots, screenshots, reports, recovery records | Keep local-only. Track docs only. |
| `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work` | `3300` | `291520635` | copied-board trials, DRC scratch JSON, copied `.kicad_pcb/.kicad_pro/.kicad_prl` variants | Do not add more scratch payload to Git. Keep future runs local-only. |

## Changes Applied

- Added explicit ZIP/local onboarding docs:
  - `DOWNLOAD_ZIP_START_HERE.md`
  - `LOCAL_SETUP_REQUIREMENTS.md`
  - `AGENT_STARTER_PROMPTS.md`
  - `SELF_CONTAINED_REPO_CHECKLIST.md`
  - `EXTERNAL_DEPENDENCIES.md`
  - `PORTABILITY_AUDIT.md`
- Updated front-door docs so new users are told to open the repo in VS Code, use repo-relative paths, and start AI agents from the repo root.
- Updated `03_TOOLS` docs so local-only envs, clones, and logs are documented as optional and non-required.
- Added placeholder docs for project-local routing scratch folders:
  - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work/README.md`
  - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_rehearsals/README.md`
- Hardened `.gitignore` so future `routing_rehearsals` scratch stays local-only and future timestamped `routing_work` runs are ignored by default.
- Hardened tracked helper scripts so passive Windows tools auto-detect the repo root instead of assuming a personal checkout path.
- Hardened AI-quality and prompt-counter helpers to emit repo-relative paths in new generated outputs.
- Incremented the active-project prompt counter to `5`; maintenance is now due before the next engineering task on the active project.

## Remaining Portability Gaps

1. `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work` already contains a large tracked copied-board rehearsal payload. This pass documented it and blocked future growth by default, but it did not purge the existing tracked history.
2. `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/*.json` still contain machine-local library URIs from earlier inventory work.
3. `00_CODEX_START/TOOL_INDEX.md` remains a machine-specific local inventory document, now labeled as such. It is useful, but not a portable assumption source.
4. `CURRENT_STATUS.md` is time-sensitive and can become stale quickly after new commits or PCB work.

## Recommended Next Actions

1. Keep this docs/script hardening commit docs-only and push it.
2. Run `python 03_TOOLS/scripts/maintenance/run_maintenance_cycle.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE` before the next engineering task on the active project.
3. In a separate approved cleanup, decide whether the tracked `routing_work` payload should be reduced to a sanitized evidence subset plus placeholder docs.
4. In a separate approved cleanup, rebuild or sanitize the tracked library-index JSON files that still contain machine-local URIs.
