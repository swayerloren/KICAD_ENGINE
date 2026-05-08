# Failed Attempt

Date: `2026-05-08`

Task: `Placement readiness scoring before routing`

## Failure

The first staging command used `&&` in PowerShell while composing:

- `git add ... && git diff --cached --name-only`

This checkout's PowerShell rejected `&&` as an invalid statement separator.

## Correction

Re-ran the exact same scope using native PowerShell statement separation:

- `git add ...; git diff --cached --name-only`

## Impact

- no repo content was lost
- no KiCad files were touched
- staging completed successfully on the second attempt
