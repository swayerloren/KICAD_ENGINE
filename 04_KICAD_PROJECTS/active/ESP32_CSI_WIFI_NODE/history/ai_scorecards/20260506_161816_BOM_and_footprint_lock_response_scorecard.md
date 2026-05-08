# BOM and footprint lock response scorecard

Record kind: `ai_scorecard`
Created: `2026-05-06T16:18:16`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`
Severity: `HIGH`
Confidence: `HIGH`
Claim status: `VERIFIED_BY_FILE`
Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`
Gate result: `FAIL`
Human review required: `YES`

## Scores

- Overall score: `90/100`
- Evidence support: `18/20`
- KiCad-specific correctness: `18/20`
- Datasheet/component accuracy: `12/15`
- Safety/compliance with repo rules: `15/15`
- Memory/history routing correctness: `9/10`
- Uncertainty disclosure: `10/10`
- End-user usefulness: `8/10`

## Summary

Planning outputs were file-backed and conservative; remaining footprint/package choices are explicitly unverified or blocked.

## Evidence

PRE_SCHEMATIC_BOM_LOCK.md; SCHEMATIC_READY_PARTS_LIST.md; NEEDS_REVIEW_BEFORE_SCHEMATIC.md; reports/FOOTPRINT_ASSIGNMENT_PLAN.md

## Unresolved Issues

Schematic footprint assignment cannot proceed safely yet.
