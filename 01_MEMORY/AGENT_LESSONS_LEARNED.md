# Agent Lessons Learned

Durable, reusable lessons for Codex, Claude, and similar agents working in KiCad Engine.

This file is for repo-wide lessons that should influence future sessions across projects. Do not store one-off command output, raw logs, secrets, or unverified project facts here.

## Use Rules

- Add only lessons that are reusable beyond one project.
- Mark every lesson `UNVERIFIED` unless the user confirms it or a repeatable workflow proves it.
- Link to evidence in `02_HISTORY/` when possible.
- Keep project-specific decisions in the project `memory/` folder.
- Keep command transcripts in `02_HISTORY/command_logs/`.

## Lesson Record Format

```text
ID:
Date:
Status: UNVERIFIED | USER_CONFIRMED | VERIFIED_WORKFLOW
Scope: Global
Source:
Lesson:
Why it matters:
Evidence:
Follow-up:
```

## Current Lessons

ID: GLOBAL_INDEXING_001
Date: 2026-05-03
Status: VERIFIED_WORKFLOW
Scope: Global
Source: `02_HISTORY/design_reviews/STARTUP_CLOSEOUT_INDEX_WIRING_AUDIT.md`
Lesson: Startup and closeout should not depend on Git metadata being available. Use filesystem-based repo, memory, history, and known-problem index builders as the durable baseline, then use Git only when the workspace is confirmed to be a Git worktree.
Why it matters: Installer payloads, copied workspaces, and test templates may intentionally omit `.git`, while Codex/Claude still need accurate startup and closeout indexes.
Evidence: `git status --short` returned "not a git repository" during the startup/closeout wiring session, while filesystem-based index builders and health check completed successfully.
Follow-up: If Git metadata is required for a release task, first confirm `.git` exists or run from the real release checkout.
