# KiCad Native Annotation Auto-Open Scorecard

Record kind: `ai_scorecard`
Created: `2026-05-10T11:11:32`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Scores

- Overall score: `93/100`
- Evidence support: `19/20`
- KiCad-specific correctness: `19/20`
- Datasheet/component accuracy: `12/15`
- Safety/compliance with repo rules: `15/15`
- Memory/history routing correctness: `9/10`
- Uncertainty disclosure: `10/10`
- End-user usefulness: `9/10`

## Summary

Requested GUI-annotation tooling and documentation work completed with successful syntax validation and dry-run validation, without editing KiCad design files.

## Evidence

Dry-run results: run_native_annotation_workflow.py => DRY_RUN_READY_NATIVE_ANNOTATION_WORKFLOW; ensure_eeschema_open.py => DRY_RUN_READY_TO_OPEN_PROJECT_AND_EESCHEMA; starting state => NO_EESCHEMA_WINDOW.

## Unresolved Issues

Live GUI interaction through the upgraded wrapper remains unverified in this task.
