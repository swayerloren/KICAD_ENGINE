# Emergency schematic truth audit uncertainty log

Record kind: `uncertainty_log`
Created: `2026-05-06T16:07:34`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`
Severity: `HIGH`
Confidence: `MEDIUM`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`
Gate result: `FAIL`
Human review required: `YES`

## Summary

Text-overlap counts are heuristic and require human visual confirmation; automated crop PASS is not enough for readability.

## Details

Known verified facts: no placed question-mark refs, no duplicate physical refs, 43 blank footprints, ERC 0 violations. Uncertainty: exact severity of each text overlap must be confirmed in KiCad or by human visual review.

## Evidence

reports/EMERGENCY_CURRENT_SCHEMATIC_TRUTH_AUDIT.md

## Issue

Visual overlap detection needs human review.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
