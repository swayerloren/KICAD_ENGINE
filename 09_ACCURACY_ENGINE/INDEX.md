# Accuracy Engine Index

Status: `ACTIVE`

## Key Areas

- `schematic_rules/`: schematic creation and review standards.
- `pcb_rules/`: PCB creation, footprint, layout, and review standards.
- `verification_rules/`: ERC, DRC, BOM, PNP, Gerber, and final review rules.
- `workflows/`: source-backed workflows for schematic, PCB, library, and release tasks.
- `checklists/`: accuracy gate checklists for engineering claims and closeout.

## Required Use

Read the relevant rules before making or approving schematic, PCB, footprint, connector, or manufacturing-output claims.

## Core Gate Files

- `checklists/ACCURACY_GATE_CHECKLIST.md`
- `workflows/FULL_KICAD_PROJECT_PIPELINE.md`
- `workflows/MEMORY_HISTORY_MAINTENANCE_WORKFLOW.md`
- `checklists/FULL_PIPELINE_GATE_CHECKLIST.md`
- `verification_rules/ERC_DRC_REQUIRED_RULES.md`
- `verification_rules/FAB_OUTPUT_NOT_FINAL_RULES.md`
- `verification_rules/HUMAN_REVIEW_GATE_RULES.md`
- `verification_rules/EVIDENCE_HIERARCHY_RULES.md`
- `verification_rules/FALSE_PASS_PREVENTION_RULES.md`
- `verification_rules/REPORT_STATUS_TAGGING_RULES.md`
- `verification_rules/STALE_REPORT_SUPERSESSION_RULES.md`
- `verification_rules/DATE_NORMALIZATION_RULES.md`
- `verification_rules/DUPLICATE_HISTORY_HANDLING_RULES.md`

## Pipeline Prompt Pack

- `.prompts/kicad_pipeline/01_schematic_annotation_and_completeness.md` through `.prompts/kicad_pipeline/17_export_not_final_fab_package.md`

Use the prompts in order unless the user explicitly approves a logged exception.

## Agent Quality Link

Use `26_AGENT_QUALITY/` with this accuracy engine. Engineering claims require a self-review, scorecard, claim/evidence matrix, and uncertainty log.


## PURPOSE

Define anti-hallucination and source-evidence rules for schematic, PCB, verification, and release workflows.

## WHAT_BELONGS_HERE

Rules, checklists, workflows, and interpretation standards for KiCad engineering accuracy.

## WHAT_DOES_NOT_BELONG_HERE

Project source files, generated fab packages, guessed datasheet values, or tool output logs.

## AI_AGENT_RULES

- Read this folder's README.md and INDEX.md before adding or relying on content here.
- Mark unverified engineering claims explicitly.
- Keep source links, verification status, and human-review requirements visible.
- Route generated logs and reports to 2_HISTORY/, 5_OUTPUTS/, or project history/ unless this folder explicitly calls for generated indexes.

## SAFE_EDIT_RULES

- Preserve existing user work.
- Do not delete or overwrite files without explicit approval.
- Do not edit KiCad design files from this folder.
- Do not store secrets or credentials.

## PUBLIC_RELEASE_NOTES

- Review this folder for secrets, personal paths, copyrighted documents, unsupported claims, and large generated files before public release.
- Folder existence is not a completeness or production-readiness claim.
