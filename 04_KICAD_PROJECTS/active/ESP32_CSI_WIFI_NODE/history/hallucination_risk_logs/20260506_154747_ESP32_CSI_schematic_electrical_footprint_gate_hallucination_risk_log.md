# ESP32 CSI schematic electrical footprint gate hallucination risk log

Record kind: `hallucination_risk_log`
Created: `2026-05-06T15:47:47`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`
Severity: `HIGH`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`
Gate result: `FAIL`
Human review required: `YES`

## Summary

Risk exists if ERC pass is mistaken for schematic-to-PCB readiness.

## Details

This session explicitly did not claim footprints, pinouts, package drawings, connector orientation, USB policy, or PMOS mapping are verified. Remaining electrical interpretations are limited to parsed schematic labels/values and require human review.

## Evidence

reports/SCHEMATIC_ELECTRICAL_GATE_REPORT.md; reports/FOOTPRINT_PACKAGE_GATE_REPORT.md

## Issue

Do not infer layout readiness from clean ERC.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
