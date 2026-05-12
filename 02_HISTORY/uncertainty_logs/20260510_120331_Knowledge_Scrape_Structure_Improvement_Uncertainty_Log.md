# Knowledge Scrape Structure Improvement Uncertainty Log

Record kind: `uncertainty_log`
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

Recovered scrape files are more discoverable now, but not all of them are equally trustworthy or equally clean.

## Details

Recovered rows can still carry needs_rescrape or rejected scrape status, extracted PDF Markdown remains secondary to original PDFs, some peer-review sources are index pages rather than thread-level evidence, and blocked-site captures remain poor inputs until replaced. The routing docs explicitly preserve those boundaries.

## Evidence

knowledge_scrape/URL_INDEX.csv; knowledge_scrape/URL_INDEX.md; knowledge_scrape/00_source_of_truth/SOURCE_OF_TRUTH_INDEX.md; knowledge_scrape/STRUCTURE_IMPROVEMENT_REPORT.md

## Issue

Future engineering decisions still need URL_INDEX row checks and original-source confirmation for exact values or drawings.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
