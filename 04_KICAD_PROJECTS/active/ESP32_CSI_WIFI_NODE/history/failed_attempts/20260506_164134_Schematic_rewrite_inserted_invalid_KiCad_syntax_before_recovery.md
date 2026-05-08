# Schematic rewrite inserted invalid KiCad syntax before recovery

Record kind: `failed_attempt`
Status: `RECOVERED`
Created: `2026-05-06T16:41:34`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`

## Summary

First rewrite attempt placed hidden properties outside valid symbol expressions; ERC load failed and the schematic was restored from backup before retry.

## Details

Recovered by restoring the backed-up schematic and rerunning a corrected transformation that preserves KiCad symbol syntax.

## Source Or Evidence

Command log: 02_HISTORY/command_logs/ESP32_CSI_WIFI_NODE_SCHEMATIC_REAL_REPAIR_COMMANDS.md

## Verification Status

Mark this record `USER_CONFIRMED` or `VERIFIED_WORKFLOW` only after human confirmation or repeatable evidence exists.

## Secret Check

No secrets should be stored in this record.
