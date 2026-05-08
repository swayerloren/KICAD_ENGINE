# Failed Attempt: Auto-Open Dry-Run Report Formatting Hiccup

Date: `2026-05-06`

## What Failed

The first generated `AUTO_OPEN_PROJECT_DRY_RUN_REPORT.md` contained escaped PowerShell variables and malformed markdown code fences.

## Cause

PowerShell string escaping was used incorrectly while embedding command output into a here-string.

## Resolution

The report was replaced with a corrected markdown report using `apply_patch`.

## Impact

No KiCad design files were edited. No live KiCad GUI action was run.

