# Real KiCad PCB Routing Bridge Uncertainty Log

Record kind: `uncertainty_log`
Created: `2026-05-07T21:00:12`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `NO`

## Summary

The bridge is implemented and copied-board tested, but some real-board extraction semantics remain partial and the active project is still upstream-blocked.

## Details

The largest remaining uncertainty is not whether the bridge can read boards; that is verified. The remaining uncertainty is how complete the extracted semantics are for real routing decisions, especially per-net ratsnest state, via intent, and richer rule-area interpretation. Downstream routing-plan heuristics also still need stronger real-board critical-loop recognition.

## Evidence

Copied-board extraction and audit outputs exist; NOT_EXTRACTED notes are recorded in routing_schema.json and the extraction report; active-project hashes were rechecked unchanged.

## Issue

Do not treat the bridge as permission for active-project routing until the remaining blockers are resolved and the real-project gate passes.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
