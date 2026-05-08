# 03_TOOLS/node_envs

## PURPOSE

Local-only Node workspaces and npm build sandboxes for tool evaluation, isolated test builds, and disposable package installs.

## WHAT_BELONGS_HERE

- Copied tool workspaces such as `kicanvas/workspace_<timestamp>`.
- `npm ci` or `npm install` dependency trees.
- Build outputs, lockfiles, and temporary local test artifacts.

## WHY_CONTENTS_ARE_IGNORED

- Node dependency trees are large, machine-specific, and noisy in Git history.
- These workspaces may contain copied upstream source plus generated `node_modules/` content.
- Public GitHub consumers should not be asked to download disposable local build sandboxes.

## HOW_TO_RECREATE_LOCALLY

1. Start from the approved upstream repo or local source path documented in `00_CODEX_START/TOOL_INDEX.md` and `00_CODEX_START/REPO_MAP.md`.
2. Create an isolated workspace under this folder.
3. Run the tool-specific npm commands documented in tracked setup docs or local tool notes.
4. Treat the resulting workspace as disposable local state.

## WHAT_SHOULD_NEVER_BE_COMMITTED

- `node_modules/`
- generated build outputs and caches
- copied third-party workspaces unless explicitly curated for tracking
- local logs, credentials, tokens, or machine-specific config

## PUBLIC_RELEASE_NOTES

GitHub should show this folder as a placeholder only. The actual local contents remain ignored on purpose.

ZIP users do not need this folder populated for the basic workflow.
