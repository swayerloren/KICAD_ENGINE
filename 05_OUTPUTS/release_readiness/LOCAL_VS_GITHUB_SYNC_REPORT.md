# Local Vs GitHub Sync Report

Date: `2026-05-08`
Scope: `pre-remediation sync baseline plus current docs-only working tree`

## Baseline Before Portability Changes

- Branch: `main`
- Origin URL: `https://github.com/swayerloren/KICAD_ENGINE.git`
- Local `HEAD`: `b8b661a3eec7d295a596b6dc790a315e904f0398`
- `origin/main`: `b8b661a3eec7d295a596b6dc790a315e904f0398`
- Local `main` equaled GitHub `main`: `YES`

## Current Working Tree During Audit

- Branch remains `main`
- Repo is still configured to push to `origin`
- The current uncommitted work is docs/index/script portability hardening only
- One unrelated local KiCad workspace file remains unstaged and must stay out of the commit:
  - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_prl`

## Observed GitHub/Repo Mismatch Causes

- `03_TOOLS/node_envs`, `03_TOOLS/python_envs`, `03_TOOLS/repos`, `03_TOOLS/tool_logs`, and `99_BACKUPS` are intentionally local-only by ignore policy.
- `routing_rehearsals` was absent locally until a placeholder README was added for documentation.
- `routing_work` is different: it already has a large tracked payload in Git, so it is visible on GitHub for historical reasons even though future scratch runs should stay local-only.

## Safe Sync Outcome Expected From This Task

- Commit only safe docs, reports, indexes, and non-design helper-script fixes.
- Do not stage generated envs, cloned repos, backups, tool logs, caches, or copied-board scratch payloads.
- Push the docs-only commit to `main` if the branch remains `main`.
