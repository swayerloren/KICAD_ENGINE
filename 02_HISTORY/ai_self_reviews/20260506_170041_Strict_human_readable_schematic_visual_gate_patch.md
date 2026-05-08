# Strict human-readable schematic visual gate patch

Record kind: `ai_self_review`
Created: `2026-05-06T17:00:41`
Scope: `global`
Project: `N/A`
Severity: `HIGH`
Confidence: `HIGH`
Claim status: `VERIFIED_BY_FILE`
Risk label: `LOW_RISK`
Gate result: `PASS`
Human review required: `NO`

## Summary

Patched repo-wide rules to separate automated crop/check generation from human-readable schematic visual approval.

## Details

No KiCad design files were edited. New visual rules require rendered full-page/crop inspection and classify uninspected images as VISUAL_NOT_VERIFIED, not PASS.

## Evidence

AGENTS.md; 03_TOOLS/kicad/VISUAL_VERIFICATION_WORKFLOW.md; 09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md; 09_ACCURACY_ENGINE/verification_rules/VISUAL_PASS_IS_NOT_AUTOMATED_PASS.md

## Issue

Prior workflow could overstate schematic visual readiness.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
