# Portability Audit Session

Record kind: `session`
Status: `UNVERIFIED`
Created: `2026-05-08T18:30:00`
Scope: `global`
Project: `N/A`

## Summary

Audited KICAD_ENGINE for clone-or-ZIP portability, documented local-only folders, hardened startup/onboarding docs for local VS Code plus Codex/Claude use, and removed hardcoded personal checkout assumptions from the tracked passive helper layer.

## Details

- Verified that local `main` matched `origin/main` before remediation.
- Audited `03_TOOLS/node_envs`, `03_TOOLS/python_envs`, `03_TOOLS/repos`, `03_TOOLS/tool_logs`, `99_BACKUPS`, `routing_work`, and `routing_rehearsals`.
- Added explicit onboarding docs for ZIP users, local setup requirements, AI starter prompts, self-contained checklist, and dependency classification.
- Updated README/startup/tool docs to emphasize repo-relative paths, local KiCad requirement, optional Codespaces use, and no extra helper repos for first use.
- Hardened tracked scripts that emitted or depended on machine-local paths.
- Documented remaining portability gaps instead of silently rewriting or deleting historical tracked scratch payloads.

## Source Or Evidence

- `git status --ignored`
- `git fetch origin`
- `git rev-parse HEAD`
- `git rev-parse origin/main`
- `git log --oneline --decorate -n 10`
- folder inventory commands for local-only directories
- `.gitignore`
- repo docs and tracked helper scripts listed in the task contract

## Verification Status

Mark this record `USER_CONFIRMED` or `VERIFIED_WORKFLOW` only after human confirmation or repeatable evidence exists.

## Secret Check

No secrets should be stored in this record.
