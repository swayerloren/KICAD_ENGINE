# Local Vs GitHub Sync Report

Date: `2026-05-08`
Scope: `pre-remediation sync baseline plus current portability hardening`

## Baseline Before This Pass

- Branch: `main`
- Origin URL: `https://github.com/swayerloren/KICAD_ENGINE.git`
- Local `HEAD`: `bfa7bcf9dec65d82007297729036481e11d8cd6c`
- `origin/main`: `bfa7bcf9dec65d82007297729036481e11d8cd6c`
- Local `main` equaled GitHub `main`: `YES`

## Local-Only Folders Missing From GitHub Payload

- `03_TOOLS/node_envs`
- `03_TOOLS/python_envs`
- `03_TOOLS/repos`
- `03_TOOLS/tool_logs`
- `99_BACKUPS`

These are intentionally local-only and now documented through tracked placeholder docs.

## Special Cases

- `routing_rehearsals` is intentionally local-only and now represented by a tracked placeholder README.
- `routing_work` is not purely local-only because a legacy tracked scratch payload already exists in Git. Future scratch runs should still stay local-only.

## Safe Sync Policy For This Task

- Commit only safe docs, reports, helper scripts, prompts, CI config, and ignore rules.
- Do not stage generated envs, cloned repos, backups, logs, caches, or copied-board scratch payloads.
- Do not stage the unrelated local KiCad workspace file:
  - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_prl`
