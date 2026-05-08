# Failed Attempt - Sample Payload Validation Command Syntax

Status: `RESOLVED_WITH_RERUN`

Date: `2026-05-06`

## What Failed

Three validation commands failed during the sample payload policy update:

1. A PowerShell `foreach` pipeline was written in a way that produced
   `An empty pipe element is not allowed`.
2. A direct `rg` secret-scan command had PowerShell quoting problems.
3. `git status` failed because this checkout does not expose `.git` metadata
   to the current shell.

## Impact

No source files were deleted, moved, or corrupted. No KiCad design files were
edited. The failed commands were validation-only.

## Resolution

- Presence checks were rerun with `$results = foreach (...) { ... }`.
- Secret scan was rerun using a PowerShell `$pattern` variable and
  `Select-String`.
- Git status was treated as unavailable; file changes were tracked through
  explicit path validation and read-only inventories instead.

## Lesson

For PowerShell validation in this repo, assign `foreach` output to a variable
before piping and avoid embedding complex regex patterns directly in command
strings.
