# Knowledge Scrape Migration Controller Hallucination Risk Log

Record kind: `hallucination_risk_log`
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

The main risk is over-promoting scraped content into canonical folders without checking license and source quality at move time.

## Details

This run reduces that risk by forcing every file through an explicit ledger with action, destination, and license-risk fields. Residual risk remains if future migration prompts override MOVE_TO_LICENSE_QUARANTINE, skip MOVE_NORMALIZED review, or treat recovered scrape text as authoritative without using the canonical destination rules.

## Evidence

03_TOOLS/scripts/knowledge_migration/knowledge_migration_config.json; 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv; 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_DESTINATION_MAP.md

## Issue

Migration quality still depends on future apply-mode discipline.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
