# Failed Attempt: Supplier Ingestion Secret Scan Quoting Failure

Date: 2026-05-03

Status: `RESOLVED`

## What Failed

A strict credential-value scan command failed because the regular expression quoting was invalid for PowerShell.

## Impact

No repo files were damaged. The failure was limited to command parsing before the scan could run.

## Fix

Reran the scan with safer quoting.

## Result

The corrected strict credential-value scan completed and returned `PASS`.

## Lesson

For PowerShell `rg` regex commands containing quote characters, prefer single-quoted patterns and avoid unescaped embedded quote sequences.
