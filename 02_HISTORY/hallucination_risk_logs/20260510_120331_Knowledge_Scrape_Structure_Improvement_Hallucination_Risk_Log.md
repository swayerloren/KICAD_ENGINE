# Knowledge Scrape Structure Improvement Hallucination Risk Log

Record kind: `hallucination_risk_log`
Created: `2026-05-10T12:03:31`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Summary

The main risk is over-trusting recovered scrape material after the folder structure improves.

## Details

This session reduces that risk by requiring URL_INDEX-first lookup, source-of-truth routing, original-PDF priority for exact package/pin/layout details, and explicit low-trust handling for rejected or low-value captures. Residual risk remains if a future agent cites recovered Markdown without checking the registry row and the original source tier.

## Evidence

AGENTS.md; CLAUDE.md; knowledge_scrape/00_ai_entrypoints/AI_START_HERE.md; knowledge_scrape/00_source_of_truth/SOURCE_OF_TRUTH_INDEX.md; knowledge_scrape/URL_INDEX.md

## Issue

Folder cleanup improves retrieval, not truth by itself.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
