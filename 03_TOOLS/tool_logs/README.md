# 03_TOOLS/tool_logs

## PURPOSE

Local-only tool reports, install notes, health-check outputs, and machine-specific workflow logs that support local setup and troubleshooting.

## WHAT_BELONGS_HERE

- Health-check outputs such as `KICAD_ENGINE_HEALTH_CHECK.md`.
- Local install and migration notes.
- Machine-specific environment and path reports.
- Sanitized local config snippets used for personal setup, not public payloads.

## WHY_CONTENTS_ARE_IGNORED

- These files often contain machine-specific paths, local runtime state, and disposable troubleshooting notes.
- Some records are generated logs rather than durable public repo documentation.
- Public-facing summaries belong in tracked docs or `05_OUTPUTS/release_readiness/`, not in a blanket-unignored local log folder.

## HOW_TO_RECREATE_LOCALLY

1. Re-run the relevant health-check, tool-audit, or setup scripts from `03_TOOLS/scripts/`.
2. Save local outputs in this folder when they are useful for personal setup or troubleshooting.
3. If one of those records becomes durable public documentation, copy a sanitized summary into a tracked docs or release-readiness file instead of unignoring the whole folder.

## WHAT_SHOULD_NEVER_BE_COMMITTED

- raw local logs and transient troubleshooting output
- private config files, tokens, or credentials
- screenshots or captures that are only useful on one machine
- generated noise that belongs in disposable local troubleshooting records

## PUBLIC_RELEASE_NOTES

GitHub should show this folder as a placeholder only. The actual local log files remain ignored on purpose.

ZIP users do not need this folder populated for the basic workflow.
