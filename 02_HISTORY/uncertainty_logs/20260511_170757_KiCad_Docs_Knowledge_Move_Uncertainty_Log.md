# KiCad Docs Knowledge Move Uncertainty Log

Record kind: `uncertainty_log`
Created: `2026-05-11T17:07:57`
Scope: `global`
Project: `N/A`
Severity: `LOW`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `LOW_RISK`
Gate result: `PASS`
Human review required: `NO`

## Summary

The migration counts are verified, but the normalized docs remain summaries rather than exhaustive upstream reproductions.

## Details

Uncertainty is limited to interpretation scope, not move completion. Raw captures were quarantined instead of promoted to canonical knowledge to reduce license risk and avoid treating scraped text as primary source of truth.

## Evidence

10_KNOWLEDGE_BASE/kicad_core/README.md;10_KNOWLEDGE_BASE/kicad_python_api/README.md;21_LICENSE_ATTRIBUTION/license_risk_reviews/knowledge_scrape_quarantine/

## Issue

None recorded.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
