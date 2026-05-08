# Failed broad regex schematic relayout attempt

Record kind: `failed_attempt`
Status: `UNVERIFIED`
Created: `2026-05-06T17:31:09`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`

## Summary

Initial broad regex coordinate rewrite made the schematic electrically invalid with 33 ERC violations, so the schematic was restored from backup before continuing with safer targeted edits.

## Details

Do not use broad unconstrained regex transformations for KiCad schematic relayout. Use UUID-bounded object shifts, exact replacements, ERC after each pass, and backup rollback when needed.

## Source Or Evidence

ESP32_CSI_WIFI_NODE_HUMAN_READABLE_SCHEMATIC_REPAIR_SESSION

## Verification Status

Mark this record `USER_CONFIRMED` or `VERIFIED_WORKFLOW` only after human confirmation or repeatable evidence exists.

## Secret Check

No secrets should be stored in this record.
