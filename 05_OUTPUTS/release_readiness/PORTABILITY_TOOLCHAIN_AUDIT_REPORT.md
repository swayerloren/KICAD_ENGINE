# Portability Toolchain Audit Report

Date: `2026-05-08`
Task type: `GITHUB_DOCS_ONLY`
Repo root: `.`

## Goal

Make `KICAD_ENGINE` usable as a normal GitHub ZIP download or `git clone` in VS Code without requiring hidden local-only folders, extra cloned GitHub repos, hardcoded `C:\Users\LJ` assumptions, or private local environments for the basic workflow.

## Baseline Git Facts

- Branch at audit start: `main`
- Origin URL: `https://github.com/swayerloren/KICAD_ENGINE.git`
- Local `HEAD` before this pass: `bfa7bcf9dec65d82007297729036481e11d8cd6c`
- `origin/main` before this pass: `bfa7bcf9dec65d82007297729036481e11d8cd6c`
- Local `main` matched GitHub `main` before this pass: `YES`

## Portability Verdict

- ZIP-download portable for the baseline docs/script workflow: `YES, WITH KNOWN LIMITATIONS`
- Extra cloned GitHub repos required for first use: `NO`
- Local KiCad install required for live schematic or PCB GUI work: `YES`
- Human KiCad review still required before fabrication: `YES`

## Required Installs

- `Python 3.11+`
- `KiCad` for live schematic, PCB, or `pcbnew` workflows

## Optional Installs

- `VS Code`
- `Codex` or `Claude`
- `Git`
- `GitHub CLI`
- `Codespaces`
- `devcontainer`
- `FreeRouting`
- `Node/npm`
- optional Windows GUI helper packages from `pyproject.toml`

## Local-Only Folder Audit

| Folder | Classification | Ignored | Tracked | Empty | Generated contents | Required for basic use | Recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `03_TOOLS/node_envs` | `LOCAL_ONLY_ENV` | `YES` | `README only` | `NO` | `YES` | `NO` | Keep local-only. Track placeholder docs only. |
| `03_TOOLS/python_envs` | `LOCAL_ONLY_ENV` | `YES` | `README only` | `NO` | `YES` | `NO` | Keep local-only. Track placeholder docs only. |
| `03_TOOLS/repos` | `DOWNLOADED_THIRD_PARTY_REPOS` | `YES` | `README only` | `NO` | `NO, but cloned payloads` | `NO` | Keep local-only. Do not require for baseline workflow. |
| `03_TOOLS/tool_logs` | `GENERATED_LOGS` | `YES` | `README only` | `NO` | `YES` | `NO` | Keep local-only. Track placeholder docs only. |
| `99_BACKUPS` | `BACKUPS` | `YES` | `README/INDEX placeholder docs` | `NO` | `YES` | `NO` | Keep local-only. Never push backup payloads. |
| `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work` | `TEMP_REHEARSALS` | `PARTIAL, future scratch ignored` | `README plus legacy tracked scratch payload` | `NO` | `YES` | `NO` | Do not add more scratch payload to Git. |
| `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_rehearsals` | `TEMP_REHEARSALS` | `YES` | `README only` | `NO` | `future-only` | `NO` | Keep local-only. Track placeholder docs only. |

## Folder Size And Content Summary

| Folder | File count | Size bytes | Primary content |
| --- | ---: | ---: | --- |
| `03_TOOLS/node_envs` | `11655` | `188707509` | local npm workspaces, dependency trees, build outputs |
| `03_TOOLS/python_envs` | `28712` | `720508017` | local venvs, site-packages, console entry points |
| `03_TOOLS/repos` | `5624` | `272132415` | cloned third-party tool repos |
| `03_TOOLS/tool_logs` | `12` | `55193` | local environment and tool logs |
| `99_BACKUPS` | `4825` | `1251768383` | pre-edit backups, snapshots, recovery records |
| `routing_work` | `3301` | `291521516` | copied-board trials, DRC scratch output, scratch variants |

## Toolchain Findings

### Included In Repo

- startup docs, prompts, indexes, and workflow rules
- `health_check.py`
- `health_check.ps1`
- `03_TOOLS/scripts/kicad_discovery/find_kicad.py`
- `03_TOOLS/scripts/kicad_discovery/validate_kicad_install.py`
- `03_TOOLS/scripts/python_env_check.py`
- task-contract validator and examples
- routing-geometry fixture tests
- CI workflows for portability-safe validation

### Required Install

- `Python`
- `KiCad` only when the task requires live KiCad GUI, `kicad-cli`, or `pcbnew`

### Optional Install

- `VS Code`
- `Git`
- `GitHub CLI`
- `Codespaces`
- `Node/npm`
- `FreeRouting`
- optional Windows GUI helper pip packages

### Not Required For Basic Use

- `03_TOOLS/node_envs`
- `03_TOOLS/python_envs`
- `03_TOOLS/repos`
- `03_TOOLS/tool_logs`
- `99_BACKUPS`
- extra cloned GitHub repos

## KiCad Discovery Status

`validate_kicad_install.py --json` reported:

- KiCad root: `PASS`
- KiCad GUI: `PASS`
- `kicad-cli`: `PASS`
- `pcbnew`: `WARN`

Detected local install:

- Root: `C:\Program Files\KiCad\9.0`
- GUI: `C:\Program Files\KiCad\9.0\bin\kicad.exe`
- CLI: `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe`
- `pcbnew` warning detail: `Module use of python311.dll conflicts with this version of Python.`

Interpretation: the repo can find KiCad correctly on this machine, but board-aware `pcbnew` work still requires the KiCad-compatible Python context instead of the user's normal Python 3.12 interpreter.

## Python Readiness Status

`python_env_check.py --json` reported:

- Python executable: `C:\Users\LJ\AppData\Local\Python\pythoncore-3.12-64\python.exe`
- Version: `3.12.10`
- Version acceptable: `YES`
- `pip` available: `YES`
- Hidden repo venv required: `NO`
- `requirements.txt` present: `YES`
- `pyproject.toml` present: `YES`

## Health Check Result

Validated with:

- `python health_check.py --no-write`
- `powershell -ExecutionPolicy Bypass -File .\health_check.ps1 -NoWrite`

Result:

- `PASS=15`
- `WARN=2`
- `FAIL=0`

Warnings were expected for `pcbnew` availability in the current Python runtime.

## Changes Applied

- Added one-prompt onboarding via `ONE_PROMPT_START.md`.
- Added portable KiCad discovery scripts and README.
- Added Python readiness metadata and setup documentation.
- Reworked top-level docs to emphasize ZIP download, VS Code, repo-relative paths, and local KiCad requirements.
- Updated placeholder docs for local-only folders.
- Removed hardcoded maintainer checkout paths from tracked prompt templates and key startup/public docs.
- Updated CI to run a no-KiCad-safe health check and stronger repo-hygiene checks.
- Updated helper scripts to prefer auto-discovery over fixed KiCad paths.

## Validation Run

- `python health_check.py --no-write` -> `PASS`
- `powershell -ExecutionPolicy Bypass -File .\health_check.ps1 -NoWrite` -> `PASS`
- `python -m py_compile ...` on changed Python scripts -> `PASS`
- routing-geometry fixtures -> `PASS`
- task-contract example validation -> `PASS`
- portability task contract validation -> `PASS`

## Remaining Portability Gaps

1. `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work/20260508_091428/` is still a large tracked historical scratch payload.
2. `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/*.json` still contain machine-local library URIs from older inventory runs.
3. `00_CODEX_START/TOOL_INDEX.md` is intentionally machine-specific inventory, not a portable assumptions source.
4. Many tracked historical reports and archived audit artifacts still contain absolute local paths; they were not rewritten because they are evidence records, not active onboarding docs.
5. `pcbnew` is not importable from the user's normal Python 3.12 runtime on this machine; live board-aware workflows still need the KiCad-compatible Python context.
