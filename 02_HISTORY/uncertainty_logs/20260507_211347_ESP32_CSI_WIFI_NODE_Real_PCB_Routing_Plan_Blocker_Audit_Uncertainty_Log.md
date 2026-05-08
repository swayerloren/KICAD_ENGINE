# ESP32_CSI_WIFI_NODE Real PCB Routing Plan Blocker Audit Uncertainty Log

Record kind: `uncertainty_log`
Created: `2026-05-07T21:13:47`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `NO`

## Summary

The live-board routing plan is real, but some extracted semantics remain partial and some existing project evidence is stale or inconsistent.

## Details

The largest uncertainties are per-net ratsnest extraction, zone polygon extraction, and USB pair role inference from the current net naming. Another important uncertainty is evidence consistency: the current PCB exists, but an older placement pass 1 report still says no PCB existed. Those inconsistencies are precisely why the final result remains ROUTING_BLOCKED.

## Evidence

Routing schema not_extracted list, missing placement orientation report, stale placement pass 1 report, and live audit outputs.

## Issue

Do not start routing until earlier-phase evidence is reconciled and the board-state blockers are reduced.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
