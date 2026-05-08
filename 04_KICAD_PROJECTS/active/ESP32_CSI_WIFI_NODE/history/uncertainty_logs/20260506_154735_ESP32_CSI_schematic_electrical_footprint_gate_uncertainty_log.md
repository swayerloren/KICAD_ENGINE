# ESP32 CSI schematic electrical footprint gate uncertainty log

Record kind: `uncertainty_log`
Created: `2026-05-06T15:47:35`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`
Severity: `HIGH`
Confidence: `HIGH`
Claim status: `UNVERIFIED`
Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`
Gate result: `FAIL`
Human review required: `YES`

## Summary

Unverified electrical and footprint decisions remain open.

## Details

Unknowns include AO3401A pin mapping, USB VBUS policy, USB shield policy, ESP32 module footprint, USB-C connector drawing/orientation, regulator passives, mounting holes, test pads, and all exact footprints.

## Evidence

reports/SCHEMATIC_ELECTRICAL_GATE_REPORT.md; reports/FOOTPRINT_PACKAGE_GATE_REPORT.md

## Issue

Gate cannot pass until human review and source-backed package evidence are recorded.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
