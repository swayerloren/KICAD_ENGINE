# Knowledge Scrape Metadata Normalizer Initial BOM Parse Failure

Record kind: `failed_attempt`
Status: `RESOLVED`
Created: `2026-05-11T16:49:11`
Scope: `global`
Project: `N/A`

## Summary

The first normalization pass failed because MANIFEST.json had a UTF-8 BOM and the initial JSON loader used plain utf-8.

## Details

No source files were lost or duplicated. The normalization step was rerun with utf-8-sig handling, after which the canonical SOURCE_REGISTRY outputs and migration reports were generated successfully.

## Source Or Evidence

Inline Python normalization step during the 2026-05-11 metadata move session

## Verification Status

Mark this record `USER_CONFIRMED` or `VERIFIED_WORKFLOW` only after human confirmation or repeatable evidence exists.

## Secret Check

No secrets should be stored in this record.
