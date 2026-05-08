# Portability Audit Uncertainty Log

Record kind: `uncertainty_log`
Created: `2026-05-08T18:35:00`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `MEDIUM`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Summary

Some portability conclusions are based on measured folder inventory plus targeted path sampling, not a byte-perfect review of every tracked/generated artifact in the repo.

## Details

- `routing_work` was confirmed as a large tracked payload, but this task did not decide which historical files should be preserved versus removed in a future cleanup.
- `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/*.json` were identified as remaining machine-local URI risk by search results, but were not regenerated here.
- `00_CODEX_START/TOOL_INDEX.md` is intentionally still a machine-specific local inventory document, now labeled as such.

## Evidence

Folder inventory commands, `rg` path search results, `.gitignore`, `git ls-files`, and the portability reports.

## Issue

See `02_HISTORY/issue_logs/20260508_portability_remaining_gaps.md`.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
