# Human-readable visual pass risk log

Record kind: `hallucination_risk_log`
Created: `2026-05-06T17:31:26`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`
Severity: `HIGH`
Confidence: `HIGH`
Claim status: `VERIFIED_BY_FILE`
Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`
Gate result: `FAIL`
Human review required: `YES`

## Summary

Risk: automated crop generation could be mistaken for visual pass.

## Details

The script reported crop generation PASS, but manual rendered image inspection showed visible overlap/crowding. Reports explicitly classify visual status as FAIL to prevent overclaiming.

## Evidence

_verification/VISUAL_CHECK_REPORT.md

## Issue

Do not use automated crop generation as visual approval.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
