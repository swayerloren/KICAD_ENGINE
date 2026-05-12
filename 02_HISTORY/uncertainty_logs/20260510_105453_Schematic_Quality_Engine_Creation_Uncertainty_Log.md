# Schematic Quality Engine Creation Uncertainty Log

Record kind: `uncertainty_log`
Created: `2026-05-10T10:54:53`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Summary

The read-only overlap and spacing audits use bounding-box estimates rather than full KiCad rendering geometry.

## Details

The automated text-overlap and block-layout checks are intentionally conservative and may still produce warnings or some false positives. Human close-up visual review remains a required gate, and the native annotation proof still depends on authoritative KiCad GUI evidence.

## Evidence

03_TOOLS/scripts/schematic_quality/audit_schematic_text_overlaps.py; 03_TOOLS/scripts/schematic_quality/audit_schematic_block_layout.py; reports/schematic_quality/20260510_104847/text_overlaps.md; reports/CLOSE_UP_REVIEW.md

## Issue

Do not treat the automated overlap audit as a replacement for human visual inspection.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
