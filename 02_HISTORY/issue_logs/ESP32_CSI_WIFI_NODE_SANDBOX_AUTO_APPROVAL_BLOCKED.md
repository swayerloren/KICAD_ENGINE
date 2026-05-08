# ESP32_CSI_WIFI_NODE Sandbox Auto Approval Blocked

Date: `2026-05-07`

Status: `OPEN`

## Summary

The repo now supports evidence-based sandbox auto approval, but `ESP32_CSI_WIFI_NODE` is still blocked from real PCB work.

## Primary Blockers

1. `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` is still `FAIL`
2. `reports/FOOTPRINT_PACKAGE_GATE_REPORT.md` is still `FAIL`
3. board dimensions remain assumption-only
4. the selected sandbox artifacts have not yet been reissued as an auto-approved set

## Current Auto Status

`AUTO_BLOCKED_DRC_PRECHECK_FAIL`
