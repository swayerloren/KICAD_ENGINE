# ESP32_CSI_WIFI_NODE PCB Quality Gate Failure

Record kind: `quality_gate_failure`
Created: `2026-05-10T14:25:22`
Scope: `global`
Project: `N/A`
Severity: `HIGH`
Confidence: `HIGH`
Claim status: `VERIFIED_BY_FILE`
Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`
Gate result: `FAIL`
Human review required: `YES`

## Summary

The new enforceable PCB quality gate classified the live board as FAIL_DRC.

## Details

The corrected gate found 22 schematic parity issues, 13 unconnected items, 3 detectable unrouted nets, 36 non-testpoint geometry findings, USB-routing failures, power-width failures, testpoint-topology failures, and connector proof that still needs human review. This is the authoritative routing block for the current board.

## Evidence

04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/pcb_quality_gate/20260510_quality_gate_creation_v2/pcb_quality_gate_result.json; 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/pcb_quality_gate/20260510_quality_gate_creation_v2/PCB_QUALITY_GATE_REPORT.md

## Issue

Routing is not acceptable on the current board until the quality gate reaches PASS_FINAL_ROUTING.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
