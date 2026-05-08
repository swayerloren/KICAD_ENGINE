# Component Database Core Setup Failed Attempts

Generated: `2026-05-02 23:55 -04:00`

## PowerShell Pipeline Wrapper Mistake

Status: `FAILED_THEN_CORRECTED`

Two quick verification commands attempted to pipe directly from a `foreach` statement and PowerShell returned:

`An empty pipe element is not allowed.`

Correction:

- Re-ran the commands with the loop wrapped in `& { ... } | Format-Table`.

Impact:

- No files were changed by the failed commands.
- The corrected checks passed.

## Directory-Including NUL Scan

Status: `FAILED_THEN_CORRECTED`

A broad scan for NUL characters under `08_COMPONENT_DATABASE` used `Get-ChildItem -Recurse -Include` without `-File`, which included directories and caused access-denied errors when `ReadAllText` tried to open directories.

Correction:

- Re-ran the scan with `Get-ChildItem -Recurse -File`.
- Corrected scan returned no rows.

Impact:

- No files were changed by the failed command.
