# Real KiCad PCB Routing Bridge Hallucination Risk Log

Record kind: `hallucination_risk_log`
Created: `2026-05-07T21:00:12`
Scope: `global`
Project: `N/A`
Severity: `LOW`
Confidence: `HIGH`
Claim status: `VERIFIED_BY_COMMAND`
Risk label: `LOW_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `NO`

## Summary

Hallucination risk was controlled by running the bridge against copied boards, using KiCad's own Python for extraction, and using kicad-cli DRC JSON instead of inferred board state.

## Details

The main risk was overstating real-board readiness after the fixture-only stage. That risk was reduced by building the bridge first, running it on copied boards, fixing the keepout misclassification bug, and explicitly keeping active-project routing blocked. Another risk was claiming active-project file safety without proof; that was controlled by final SHA256 hash recheck on the ESP32_CSI_WIFI_NODE .kicad_pcb, .kicad_sch, and .kicad_pro files.

## Evidence

KiCad Python introspection, copied-board extraction outputs, copied-board DRC JSON, bridge reports, failed-attempt logs for extraction bugs, and final active-project hash evidence.

## Issue

No unresolved hallucination blocker was found, but active-project routing claims must remain blocked.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
