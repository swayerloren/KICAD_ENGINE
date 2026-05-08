# PowerShell footprint candidate pipeline syntax mistake

Record kind: `failed_attempt`
Status: `RESOLVED_COMMAND_SYNTAX_ONLY`
Created: `2026-05-06T16:18:16`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`

## Summary

An initial PowerShell command that piped directly after a foreach block failed with an empty pipe element parser error.

## Details

The command was corrected by assigning the foreach output to a variable before piping to Format-Table. This did not modify project files.

## Source Or Evidence

BOM footprint lock session command log

## Verification Status

Mark this record `USER_CONFIRMED` or `VERIFIED_WORKFLOW` only after human confirmation or repeatable evidence exists.

## Secret Check

No secrets should be stored in this record.
