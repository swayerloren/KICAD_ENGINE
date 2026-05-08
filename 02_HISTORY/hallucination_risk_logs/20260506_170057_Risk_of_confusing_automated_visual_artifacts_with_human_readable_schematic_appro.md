# Risk of confusing automated visual artifacts with human-readable schematic approval

Record kind: `hallucination_risk_log`
Created: `2026-05-06T17:00:57`
Scope: `global`
Project: `N/A`
Severity: `HIGH`
Confidence: `HIGH`
Claim status: `VERIFIED_BY_USER`
Risk label: `HIGH_RISK`
Gate result: `BLOCKED_UNTIL_HUMAN_REVIEW`
Human review required: `YES`

## Summary

Automated crop generation and parser checks can produce false confidence about schematic readability.

## Details

Future agents must not infer VISUAL_PASS from ERC_PASS, automated crops, no visible footprint fields, footprint assignments, or no-question-token scans. Rendered human-readable review is required.

## Evidence

User correction; HUMAN_READABLE_SCHEMATIC_RULES.md; VISUAL_PASS_IS_NOT_AUTOMATED_PASS.md

## Issue

ESP32_CSI_WIFI_NODE reports previously overstated visual readiness.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
