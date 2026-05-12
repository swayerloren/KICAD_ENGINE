# KiCad docs move closeout argument validation mismatch

Record kind: `failed_attempt`
Status: `RESOLVED`
Created: `2026-05-11T17:07:17`
Scope: `global`
Project: `N/A`

## Summary

Initial AI-quality closeout command batch used unsupported claim-status values and out-of-range scorecard subscores.

## Details

The migration itself succeeded. The failed attempt was limited to closeout script argument formatting. The batch was rerun with repo-accepted claim-status values and 0-20 subscore ranges.

## Source Or Evidence

KICAD_DOCS_KNOWLEDGE_MOVE

## Verification Status

Mark this record `USER_CONFIRMED` or `VERIFIED_WORKFLOW` only after human confirmation or repeatable evidence exists.

## Secret Check

No secrets should be stored in this record.
