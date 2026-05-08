# Failed Attempt - Post Sample Audit Validation Hiccups

Status: `RESOLVED_OR_DOCUMENTED`

Date: `2026-05-06`

## Failed / Incomplete Checks

1. A PowerShell directory inventory command failed with `An empty pipe element
   is not allowed`.
2. A broad recursive secret-pattern scan timed out after 120 seconds in local
   environment and third-party tool folders.
3. The gate runner command returned exit code 1 because the audited sample is
   correctly classified as `BLOCKED_UNTIL_HUMAN_REVIEW`.

## Impact

No KiCad files were edited. No files were deleted or moved. The failed checks
did not change audit evidence.

## Resolution

- Directory inventory was rerun successfully using a `$results` variable before
  piping.
- Secret scan was narrowed to sample/release/public/gate-runner areas and
  completed.
- Gate runner exit code 1 was treated as expected evidence of blocked sample
  status, not a tool crash.
