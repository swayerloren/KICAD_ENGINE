# PowerShell wildcard py_compile invocation failed

Record kind: `failed_attempt`
Status: `UNVERIFIED`
Created: `2026-05-02T22:48:12`
Scope: `global`
Project: `N/A`

## Summary

Initial Python compile check used a wildcard argument that PowerShell did not expand for Python.

## Details

Command failed with Invalid argument for 03_TOOLS/scripts/memory_history/*.py. Recovery was to enumerate files with Get-ChildItem and pass the resolved file list to python -m py_compile, which passed.

## Source Or Evidence

This setup session command output.

## Verification Status

Mark this record `USER_CONFIRMED` or `VERIFIED_WORKFLOW` only after human confirmation or repeatable evidence exists.

## Secret Check

No secrets should be stored in this record.
