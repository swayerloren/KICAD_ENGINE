# ESP32 CSI schematic to PCB gate remains failed after electrical footprint gate

Record kind: `quality_gate_failure`
Created: `2026-05-06T15:47:47`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`
Severity: `HIGH`
Confidence: `HIGH`
Claim status: `VERIFIED_BY_COMMAND`
Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`
Gate result: `FAIL`
Human review required: `YES`

## Summary

The post-repair electrical/footprint gate blocked PCB update.

## Details

ERC passes, but annotation/footprint checker fails with 43 blank footprints, BOM lock alignment fails, NEEDS_REVIEW marker checker fails, and all high-risk footprints require human review.

## Evidence

reports/SCHEMATIC_TO_PCB_GATE_STATUS.md; reports/SCHEMATIC_ELECTRICAL_GATE_REPORT.md; reports/FOOTPRINT_PACKAGE_GATE_REPORT.md

## Issue

Do not update PCB until gate result is PASS.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
