# knowledge_scrape Closeout Prep Lookup Misses

Record kind: `failed_attempt`
Status: `RESOLVED`
Created: `2026-05-10T12:03:45`
Scope: `global`
Project: `N/A`

## Summary

A few exploratory closeout commands used the wrong assumption about UTF-8 BOM handling or expected helper-file locations, but the task work was not blocked.

## Details

The first before/after stats read of rejected_recovery_audit.json used plain UTF-8 instead of UTF-8-SIG, one inspection looked for a non-existent 02_HISTORY/claims folder instead of claim_evidence_matrices, and one sample self-review path used the wrong filename pattern. Each issue was corrected immediately and did not affect the recovery, doc updates, or final counts.

## Source Or Evidence

shell_exploration

## Verification Status

Mark this record `USER_CONFIRMED` or `VERIFIED_WORKFLOW` only after human confirmation or repeatable evidence exists.

## Secret Check

No secrets should be stored in this record.
