# KiCad Accuracy Engine

Purpose: stop AI agents from guessing while creating, editing, or reviewing KiCad schematics and PCBs.

This folder is an evidence-first rule system for Codex, Claude, and similar VS Code-based agents. It does not grant permission to edit KiCad project files. It defines what must be verified before an AI-generated design decision can be treated as usable.

## Core Gates

Every component must have:

- A source document or source link.
- A component database record or a task-local evidence note.
- A symbol selection with pinout verification status.
- A footprint selection with exact package drawing status.
- A datasheet or vendor-reference gap explicitly marked if missing.

Every schematic change must preserve:

- Verified pin numbers and pin functions.
- Explicit power nets.
- Required decoupling and support components.
- Reset, boot, strap, oscillator, programming, and interface requirements.
- Human-review flags for connectors, polarity-sensitive parts, RF, USB, CAN, and high-risk packages.

Every PCB change must preserve:

- Footprint-to-package evidence.
- Connector orientation review.
- Polarity and assembly orientation review.
- Interface-specific layout review for power, USB, CAN, and RF.
- DRC evidence.

Every manufacturing-style output is `NOT_FINAL` until final human review accepts the full verification evidence.

## Folder Map

- `schematic_rules/`: rules for schematic creation and review.
- `pcb_rules/`: rules for footprint choice, placement, layout, and board review.
- `verification_rules/`: ERC, DRC, BOM, PNP, Gerber, footprint, and final review rules.
- `workflows/`: repeatable workflows for component add, schematic creation, PCB creation, package release, and datasheet-to-KiCad translation.
- `checklists/`: mandatory accuracy gate checklists for engineering claims and closeout.

## Memory/History Maintenance

Use `workflows/MEMORY_HISTORY_MAINTENANCE_WORKFLOW.md` and the supporting verification rules before trusting old or conflicting memory/history/report files. Current truth must be compiled from evidence hierarchy, stale reports must be marked rather than deleted, and false-pass patterns must remain visible.

## Full KiCad Project Pipeline

Use `workflows/FULL_KICAD_PROJECT_PIPELINE.md` and `checklists/FULL_PIPELINE_GATE_CHECKLIST.md` with `.prompts/kicad_pipeline/` for future schematic-to-PCB-to-routing-to-`NOT_FINAL` fabrication workflows.

The full pipeline is a reusable gate system, not proof that a project passed. A project must still have its own current reports, command evidence, visuals, ERC/DRC results, footprint/package evidence, and human-review flags.

Pipeline gate exceptions require explicit user approval and must be logged with the affected gate, reason, risk, evidence path, and `HUMAN_REVIEW_REQUIRED`.

## Required Agent Behavior

Agents must:

1. Read the relevant rule files before creating or changing schematic/PCB content.
2. Prefer source-backed component records over memory or guesses.
3. Mark missing evidence as `UNKNOWN_REQUIRES_SOURCE_VERIFICATION`.
4. Mark unverified footprints as `UNVERIFIED_FOOTPRINT`.
5. Mark connector orientation as `HUMAN_REVIEW_REQUIRED` unless exact drawing and 3D/mechanical evidence are verified.
6. Keep generated outputs `NOT_FINAL`.

## Anti-Hallucination Gate

Before making or acting on an engineering claim, agents must identify evidence status:

- `VERIFIED_BY_FILE`
- `VERIFIED_BY_COMMAND`
- `VERIFIED_BY_DATASHEET`
- `VERIFIED_BY_KICAD_LIBRARY`
- `VERIFIED_BY_USER`
- `PARTIALLY_VERIFIED`
- `UNVERIFIED`
- `CONTRADICTED`
- `REQUIRES_HUMAN_REVIEW`

If a claim affects schematic creation, PCB creation, footprint selection, BOM review, or fab output generation and evidence is missing, the agent must stop or mark the work blocked instead of guessing.

## Mandatory Closeout For Engineering Claims

Every meaningful Codex/Claude session that makes engineering claims must create:

- AI self-review.
- AI response scorecard.
- Claim/evidence matrix.
- Uncertainty log.

Create a hallucination-risk log when any claim was inferred, guessed, weakly sourced, or contradicted.

Use `26_AGENT_QUALITY/` for policy and templates, and write real records under `02_HISTORY/` or project `history/`.

## Status Labels

Use these labels in plans, reports, and review notes:

- `SOURCE_VERIFIED`
- `SOURCE_MISSING`
- `SYMBOL_PINOUT_VERIFIED`
- `SYMBOL_PINOUT_UNVERIFIED`
- `FOOTPRINT_VERIFIED_AGAINST_DRAWING`
- `UNVERIFIED_FOOTPRINT`
- `CONNECTOR_ORIENTATION_HUMAN_REVIEW_REQUIRED`
- `POLARITY_HUMAN_REVIEW_REQUIRED`
- `RF_LAYOUT_REVIEW_REQUIRED`
- `USB_LAYOUT_REVIEW_REQUIRED`
- `CAN_LAYOUT_REVIEW_REQUIRED`
- `NOT_FINAL`

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
