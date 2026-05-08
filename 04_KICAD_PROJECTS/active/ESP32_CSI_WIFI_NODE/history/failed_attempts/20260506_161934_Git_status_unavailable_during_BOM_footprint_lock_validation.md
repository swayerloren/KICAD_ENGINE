# Git status unavailable during BOM footprint lock validation

Record kind: `failed_attempt`
Status: `NON_BLOCKING_VALIDATION_LIMITATION`
Created: `2026-05-06T16:19:34`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`

## Summary

A final git status check could not run because this directory is not currently detected as a Git worktree by the shell.

## Details

Validation continued using direct file existence checks, markdown row/status counts, and schematic SHA256 hash comparison. No KiCad design edits were made.

## Source Or Evidence

BOM footprint lock session command log

## Verification Status

Mark this record `USER_CONFIRMED` or `VERIFIED_WORKFLOW` only after human confirmation or repeatable evidence exists.

## Secret Check

No secrets should be stored in this record.
