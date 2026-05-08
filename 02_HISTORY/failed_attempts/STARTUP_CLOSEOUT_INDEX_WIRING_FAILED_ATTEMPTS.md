# Startup Closeout Index Wiring Failed Attempts

Date: 2026-05-03
Status: NON_BLOCKING_FAILURE_RECORDED

## Failed Attempt

Command:

`git status --short`

Observed result:

`fatal: not a git repository (or any of the parent directories): .git`

## Impact

This did not block the task. The requested work did not require Git metadata, and filesystem-based index builders were created and tested successfully.

## Lesson

Do not assume `.git` metadata is present in copied workspaces, installer payloads, or generated templates. Use filesystem-based indexes for startup/closeout, and verify Git worktree status before release tasks.

## Follow-Up

For release, commit, tag, diff, or GitHub workflow tasks, first confirm the real release checkout includes a `.git` directory or run from the correct Git worktree.

