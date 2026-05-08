# ZIP portability and local toolchain setup uncertainty log

Record kind: `uncertainty_log`
Created: `2026-05-08T19:03:31`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Summary

The startup path is now portable, but some historical and generated artifacts still contain absolute local paths, and pcbnew remains unavailable from the user's normal Python runtime on this machine.

## Details

Uncertainties: whether all older tracked reports should be sanitized or preserved as historical evidence; whether the legacy tracked routing_work payload should be reduced; whether generated library-index JSON files should be rebuilt or filtered before a future broader release. This task did not edit KiCad design files or attempt live pcbnew board work.

## Evidence

Hardcoded path scan results, release-readiness audit reports, and validate_kicad_install.py JSON output.

## Issue

See 02_HISTORY/issue_logs/20260508_portability_remaining_gaps.md.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
