# Knowledge Scrape Migration Controller Uncertainty Log

Record kind: `uncertainty_log`
Created: `2026-05-11T16:31:53`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Summary

The ledger classification is deterministic and complete, but some future move decisions still need human judgment because license status or value is unclear.

## Details

The controller marks 285 items for license quarantine and 6 items for explicit human review. Forum captures, standards text, university training material, and some unsorted items should not be normalized into public source-of-truth folders until the next migration step confirms license and value. MOVE_NORMALIZED rows also require a reviewed normalized canonical file during apply mode.

## Evidence

05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv; 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_DESTINATION_MAP.md

## Issue

The controller is ready, but not every future move is automatic.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
