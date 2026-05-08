# ESP32_CSI_WIFI_NODE Layout Sandbox Variants Uncertainty Log

Record kind: `uncertainty_log`
Created: `2026-05-07T17:37:08`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `LOW_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `NO`

## Summary

The sandbox variants are documented and scored, but exact board dimensions, exact connector/package lock, and LJ mechanical approval remain unresolved.

## Details

The main uncertainty is mechanical closure rather than document completeness. The project uses an ESP32-S3-WROOM-1U external-antenna module, so the RF planning is based on reserved RF connector and pigtail clearance rather than a fully proven final enclosure path. Board dimensions are still assumptions in all three variants, which keeps every variant in NEEDS_HUMAN_REVIEW even though Variant C scores highest.

## Evidence

SCHEMATIC_TO_PCB_GATE_STATUS.md, FOOTPRINT_PACKAGE_GATE_REPORT.md, PCB_SYNC_STATUS.md, current project memory, the three variant docs, and compare_layout_variants.py output.

## Issue

LJ must still approve the selected plan before any real PCB placement or edit work.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
