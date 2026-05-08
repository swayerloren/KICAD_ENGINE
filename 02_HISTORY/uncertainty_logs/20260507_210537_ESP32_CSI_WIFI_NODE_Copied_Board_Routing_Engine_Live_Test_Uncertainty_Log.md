# ESP32_CSI_WIFI_NODE Copied Board Routing Engine Live Test Uncertainty Log

Record kind: `uncertainty_log`
Created: `2026-05-07T21:05:37`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `NO`

## Summary

The copied-board live test verified the bridge and audit flow, but some routing-engine semantics remain partial and some score blockers may still reflect model limitations as well as real board incompleteness.

## Details

Per-net ratsnest extraction remains unavailable, via intent remains NOT_EXTRACTED, and the routing score still reports missing GND strategy and critical power gaps based on the current schema and heuristics. The copied-board test proves the bridge works, not that the routing-plan scorer is fully mature for every real board state.

## Evidence

Routing schema JSON not_extracted list, copied-board audit blockers, score.json, and bridge audit documentation.

## Issue

Treat copied-board audit failures as useful evidence, but continue improving real-board routing semantics before live project routing.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
