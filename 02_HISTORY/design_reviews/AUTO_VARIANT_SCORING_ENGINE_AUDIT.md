# Auto Variant Scoring Engine Audit

Date: `2026-05-07`

## Scope

Build the automatic PCB layout variant scoring engine so Codex/Claude can select the best layout variant without waiting for generic manual approval.

## What Was Added

- updated per-variant scorer
- updated multi-variant comparator
- new automatic selector
- new selected-variant auto-approval script
- new scripts README
- dry-run sample variants and approval context

## Verified Behavior

- hard-failed variants are excluded from selection
- `PASS`, `FAIL`, `AUTO_BLOCKED_MISSING_DATA`, and `AUTO_BLOCKED_BAD_LAYOUT` are produced at variant level
- selected candidate receives `AUTO_SELECTED`
- selected candidate can then map to `AUTO_APPROVED_FOR_PCB_WORK` or a specific `AUTO_BLOCKED_*` reason

## Dry Run Summary

- `VARIANT_A`: `AUTO_BLOCKED_BAD_LAYOUT`
- `VARIANT_B`: `FAIL`
- `VARIANT_C`: `PASS`
- auto-selected candidate: `VARIANT_C`
- auto-approval result with passing context: `AUTO_APPROVED_FOR_PCB_WORK`

## Residual Risk

The engine is dry-run validated only. It still needs first live use against a real project sandbox report set.

