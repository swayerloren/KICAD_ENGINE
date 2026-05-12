# KiCad Native Annotation Auto-Open Uncertainty Log

Record kind: `uncertainty_log`
Created: `2026-05-10T11:11:32`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Summary

The upgraded wrapper proves the dry-run branch and exact future live command, but this task did not execute live KiCad GUI control.

## Details

Closed-state live opening, live annotation, live save, live GUI ERC, and live screenshot capture remain intentionally unexecuted in this task. The docs and scripts now require those steps explicitly for future live proof.

## Evidence

Dry-run outputs from run_native_annotation_workflow.py and ensure_eeschema_open.py on ESP32_CSI_WIFI_NODE; updated safety-gate docs; updated flag-gated scripts.

## Issue

Do not claim live native-annotation proof from this setup task alone.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
