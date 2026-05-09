# Historical Path Evidence Remaining

Date: `2026-05-09`
Status: `OPEN`

## Problem

The repo still contains many absolute local paths outside the live onboarding layer.

## Current Scope

- preserved historical reports in `02_HISTORY/`
- project review evidence under project `reports/` and `_verification/`
- sample-intake review artifacts
- generated inventory under `29_FOOTPRINT_GAP_ANALYSIS/GENERATED_INDEXES/`
- install-intelligence docs that intentionally document one audited Windows KiCad install

## Why This Is Still Acceptable

- historical records are evidence and should not be rewritten blindly
- current startup/onboarding now explicitly warns agents not to use those paths as active config
- live discovery and portable docs are now the intended source of truth

## Remaining Follow-Up

1. audit `29_FOOTPRINT_GAP_ANALYSIS/GENERATED_INDEXES/` for placeholder-only treatment
2. keep install-intelligence docs clearly labeled as examples or audited-machine records
3. continue avoiding new `C:\Users\LJ` references in active onboarding, prompts, scripts, and public docs
