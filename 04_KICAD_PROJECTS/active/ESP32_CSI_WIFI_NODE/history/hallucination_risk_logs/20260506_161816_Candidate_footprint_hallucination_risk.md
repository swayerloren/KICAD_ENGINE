# Candidate footprint hallucination risk

Record kind: `hallucination_risk_log`
Created: `2026-05-06T16:18:16`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`
Severity: `HIGH`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`
Gate result: `FAIL`
Human review required: `YES`

## Summary

Candidate footprint suggestions could be mistaken for verified selections if not clearly marked.

## Details

All candidate footprints in this pass are planning candidates only. Exact footprint verification requires exact manufacturer drawing, package dimensions, pin mapping, orientation, and human review for high-risk parts.

## Evidence

PRE_SCHEMATIC_BOM_LOCK.md status column; FOOTPRINT_ASSIGNMENT_PLAN.md gate summary

## Issue

Do not convert candidate footprints into schematic assignments until blockers are resolved.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
