# GitHub Indexing Report

Date: `2026-05-08`

## Task

Tighten the GitHub-facing repo index and navigation layer without editing KiCad design files.

## Scope Of This Pass

The first indexing layer already existed. This pass focused on the files that were still too light for GitHub readers:

- `README.md`
- `REPO_INDEX.md`
- `PROJECTS_INDEX.md`
- `TOOLS_INDEX.md`
- `WORKFLOWS_INDEX.md`
- `CURRENT_STATUS.md`
- `PUBLIC_RELEASE_STATUS.md`
- `00_CODEX_START/GITHUB_NAVIGATION.md`
- `00_CODEX_START/CURRENT_GITHUB_STATUS.md`

## Validation Summary

- `git status` was checked before edits.
- Maintenance due check returned `NO` before work began.
- Current project state and blocker files were re-read from the active project.
- No KiCad lock files, `.env` files, secrets, backups, copied-board rehearsal trees, or raw imported-original paths were part of the intended doc-only scope.
- Existing GitHub-facing files were tightened rather than recreated blindly.
- Closeout index rebuilds were run.
- The prompt counter was incremented to `5`, then the canonical maintenance cycle was run and reset it to `0`.

## Active Project State Reflected In The Docs

- active project: `ESP32_CSI_WIFI_NODE`
- live PCB exists
- partial routing exists
- current live DRC is `0` violations with `17` unconnected items
- explicit unrouted nets remain: `/DM_C`, `/DM_E`, `/DP_C`, `/DP_E`
- remaining must-route blockers still include `/+5V_PROTECTED`, `/BOOT0`, and `/ESP_EN`
- board is not fabrication-ready

## Remaining Gaps

- many deeper subtrees still rely on existing README or INDEX files rather than normalized GitHub-facing summaries
- some historical docs still reference the pre-GitHub checkout path
- public-release blockers remain open
