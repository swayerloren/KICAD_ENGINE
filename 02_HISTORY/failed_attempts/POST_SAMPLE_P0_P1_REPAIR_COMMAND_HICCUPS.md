# Failed Attempt - Post Sample P0/P1 Repair Command Hiccups

Date: `2026-05-06`

Status: `NON_BLOCKING_TOOLING_HICCUPS`

## Failed Attempt 1

Command purpose: PowerShell parser validation for
`03_TOOLS/scripts/project_gate/run_project_gate.ps1`.

What happened:

- The initial parser command used `[ref]$errors` before `$errors` existed.
- PowerShell reported that `[ref]` cannot be applied to a variable that does
  not exist.

Resolution:

- Reran with initialized `$tokens = $null` and `$parseErrors = $null`.
- Parser validation passed.

## Failed Attempt 2

Command purpose: inspect changed files with `git diff --name-only`.

What happened:

- Git reported this checkout is not a git repository.

Resolution:

- Treated git metadata as unavailable.
- Used explicit file list in session/audit records instead.
