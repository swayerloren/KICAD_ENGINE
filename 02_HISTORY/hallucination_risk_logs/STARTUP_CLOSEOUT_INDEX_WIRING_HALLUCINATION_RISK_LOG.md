# Hallucination Risk Log: Startup Closeout Index Wiring

Date: 2026-05-03
Status: LOW_RISK_RECORDED

## Risk

Future agents may infer that a workspace under a GitHub-named folder is definitely a Git worktree. This session showed that `git status --short` can fail in the current command context.

## Required Behavior

Do not claim Git cleanliness, branch, commit, diff, release readiness, or tag status unless verified by a successful Git command or equivalent file evidence.

## Mitigation

Use filesystem-based startup/closeout indexes for repo context, and only use Git metadata after confirming the workspace is a Git worktree.

