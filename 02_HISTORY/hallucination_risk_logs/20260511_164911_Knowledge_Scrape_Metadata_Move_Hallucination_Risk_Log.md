# Knowledge Scrape Metadata Move Hallucination Risk Log

Record kind: `hallucination_risk_log`
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

The main residual risk is future agents assuming knowledge_scrape still holds the authoritative registry metadata or overpromoting scraped technical content without following the ledger.

## Details

This move reduces that risk by relocating the authoritative registry/index layer into 10_KNOWLEDGE_BASE and archiving originals into 02_HISTORY. Residual risk remains if later prompts ignore the ledger, rely on stale historical docs that mention knowledge_scrape/URL_INDEX.*, or normalize unclear-license technical captures without review.

## Evidence

10_KNOWLEDGE_BASE/source_registry/; 10_KNOWLEDGE_BASE/retrieval_indexes/; README_GPT.md; FOR CHAT GPT.MD; 05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv

## Issue

Remaining technical category folders still need disciplined ledger-driven migration.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
