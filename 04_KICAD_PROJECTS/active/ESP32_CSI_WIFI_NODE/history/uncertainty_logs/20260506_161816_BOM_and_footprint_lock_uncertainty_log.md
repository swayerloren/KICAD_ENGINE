# BOM and footprint lock uncertainty log

Record kind: `uncertainty_log`
Created: `2026-05-06T16:18:16`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`
Severity: `HIGH`
Confidence: `HIGH`
Claim status: `UNVERIFIED`
Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`
Gate result: `FAIL`
Human review required: `YES`

## Summary

Exact package drawings, full manufacturer part suffixes, and connector/mechanical orientation remain unverified.

## Details

Uncertain items include USB-C exact connector suffix, barrel jack exact MPN, AO3401A pin mapping to footprint, AP63203 package drawing match, USB ESD exact MPN/package, inductor package/current rating, capacitor packages/voltage ratings, mounting hole mechanical fit, and all connector orientation details.

## Evidence

NEEDS_REVIEW_BEFORE_SCHEMATIC.md; reports/FOOTPRINT_ASSIGNMENT_PLAN.md

## Issue

Human review and source-backed package verification are required before schematic footprint assignment.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
