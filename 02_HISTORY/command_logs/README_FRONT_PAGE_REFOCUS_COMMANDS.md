# README Front Page Refocus Commands

Record kind: `workflow_run`
Status: `UNVERIFIED`
Created: `2026-05-08T19:17:46`
Scope: `global`
Project: `N/A`

## Summary

Commands used to verify and narrow the README front-page identity wording.

## Details

- `Get-Content README.md`
- `Get-Content START_HERE.md`
- `Get-Content CURRENT_STATUS.md`
- `git status --short`
- `rg -n "ESP32_CSI_WIFI_NODE|AI-agent operating system|^## Current Example Project$|^## What KiCad Engine Is Not$" README.md`
- changed-file scan confirming only `README.md` was modified for this follow-up fix

## Source Or Evidence

Command outputs were used to confirm:

- the README leads with `KiCad Engine`
- the repo is described as the main workflow engine
- `ESP32_CSI_WIFI_NODE` appears only as an example workspace
- no KiCad design files changed

## Verification Status

Mark this record `USER_CONFIRMED` or `VERIFIED_WORKFLOW` only after human confirmation or repeatable evidence exists.

## Secret Check

No secrets should be stored in this record.
