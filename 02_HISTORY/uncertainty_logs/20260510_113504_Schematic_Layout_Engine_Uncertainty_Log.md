# Schematic Layout Engine Uncertainty Log

Record kind: `uncertainty_log`
Created: `2026-05-10T11:35:04`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Summary

The layout engine uses heuristic block assignment, approximate region scoring, and estimated text-overlap geometry.

## Details

The scoring and layout-plan logic are intentionally conservative. Human visual review is still required before treating the schematic as professionally readable, and native KiCad annotation proof remains a separate authoritative gate.

## Evidence

03_TOOLS/scripts/schematic_layout/schematic_layout_common.py; 03_TOOLS/scripts/schematic_layout/score_schematic_readability.py; reports/schematic_layout/20260510_113053/.

## Issue

Do not treat automated layout score alone as a replacement for human visual review.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
