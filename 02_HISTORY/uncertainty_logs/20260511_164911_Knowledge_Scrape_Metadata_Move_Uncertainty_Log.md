# Knowledge Scrape Metadata Move Uncertainty Log

Record kind: `uncertainty_log`
Created: `2026-05-11T16:49:11`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Summary

The move phase is verified for the targeted metadata/log/index set, but remaining technical content still needs later migration decisions and some future items may require quarantine or human review.

## Details

No files were quarantined in this phase because the user limited movement to metadata, manifests, registry files, URL indexes, reports, logs, raw inventory, and source logs. Future ledger rows for scraped technical content still include license-risk, low-value, and human-review paths that must not be normalized blindly into canonical knowledge folders.

## Evidence

05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv; 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_DESTINATION_MAP.md

## Issue

Full knowledge_scrape drainage is not complete yet.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
