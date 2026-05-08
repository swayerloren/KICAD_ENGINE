# Human-readable schematic repair uncertainty log

Record kind: `uncertainty_log`
Created: `2026-05-06T17:31:26`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`
Severity: `HIGH`
Confidence: `HIGH`
Claim status: `UNVERIFIED`
Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`
Gate result: `FAIL`
Human review required: `YES`

## Summary

Uncertainty remains for visual acceptability, high-risk footprint/package choices, USB policy, PMOS pin mapping, and LJ review acceptance.

## Details

No exact datasheet/package drawing verification was performed in this pass. Visual quality was inspected from generated PNG crops but final acceptance requires LJ review and another cleanup pass.

## Evidence

reports/SCHEMATIC_TO_PCB_GATE_STATUS.md

## Issue

Schematic cannot move to PCB update.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
