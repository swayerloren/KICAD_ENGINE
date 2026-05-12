# KiCad Native Annotation Auto-Open Hallucination Risk Log

Record kind: `hallucination_risk_log`
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

Annotation tooling is especially prone to false confidence when agents trust saved-file scans over KiCad's live GUI state.

## Details

This upgrade reduces that risk by forcing exact-project window checks, dry-run-first closed-state recovery, explicit live flags, before/after screenshots, GUI ERC, post-save CLI ERC, and saved-schematic unresolved-? plus duplicate-reference scans.

## Evidence

33_KICAD_GUI_AUTOMATION/KICAD_GUI_SAFETY_GATES.md; KICAD_ANNOTATION_DO_AND_DO_NOT.md; run_native_annotation_workflow.py; gui_workflow_common.py

## Issue

Live GUI state still requires future explicit evidence before it should be treated as proven on the new wrapper path.

## Required Follow-Up

- Keep unverified claims marked until evidence is added.
- Create or update issue logs for unresolved high-risk items.
- Do not treat AI review as fabrication approval.
