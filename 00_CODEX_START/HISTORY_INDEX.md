# History Index

History files store session records, command results, reviews, and generated reports. They are not durable design memory.

## Template Notation

Paths containing `<project-id>` are templates for real project names. Do not treat them as literal folders. For the current active project, use the path recorded in `CURRENT_PROJECT.md`.

## Current Active Project History

- Active project path: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE`
- Current project gate status: blocked before PCB update; read `reports\SCHEMATIC_TO_PCB_GATE_STATUS.md` before any PCB/layout/fab work.

## Required History Areas
- `sessions`
- `command_logs`
- `design_reviews`
- `erc_drc_reports`
- `fabrication_reviews`
- `project_history`
- `failed_attempts`
- `issue_logs`
- `user_corrections`
- `lessons_learned`
- `known_agent_mistakes`
- `workflow_runs`
- `ai_self_reviews`
- `ai_scorecards`
- `hallucination_risk_logs`
- `claim_evidence_matrices`
- `quality_gate_failures`
- `uncertainty_logs`
- `04_KICAD_PROJECTS\active\<project-id>\history`

## Folder Map
- `02_HISTORY\sessions\`: session summaries and meaningful work records.
- `02_HISTORY\command_logs\`: commands run, important outputs, failures, and environment observations.
- `02_HISTORY\design_reviews\`: schematic, PCB, component, and architecture review notes.
- `02_HISTORY\erc_drc_reports\`: ERC and DRC outputs or explanations when checks could not run.
- `02_HISTORY\fabrication_reviews\`: release readiness, Gerber, drill, BOM, placement, and fab package review notes.
- `02_HISTORY\project_history\<project-id>\`: project-specific history and milestone notes.
- `02_HISTORY\failed_attempts\`: global failed-attempt evidence.
- `02_HISTORY\issue_logs\`: global issue and blocker records.
- `02_HISTORY\user_corrections\`: global user-correction evidence.
- `02_HISTORY\lessons_learned\`: lesson records before memory promotion.
- `02_HISTORY\known_agent_mistakes\`: evidence records for recurring mistakes.
- `02_HISTORY\workflow_runs\`: global workflow-run evidence.
- `02_HISTORY\ai_self_reviews\`: global AI self-review records.
- `02_HISTORY\ai_scorecards\`: global AI response scorecards.
- `02_HISTORY\hallucination_risk_logs\`: global hallucination-risk records.
- `02_HISTORY\claim_evidence_matrices\`: global claim/evidence matrices.
- `02_HISTORY\quality_gate_failures\`: global quality-gate failure records.
- `02_HISTORY\uncertainty_logs\`: global uncertainty records.
- `04_KICAD_PROJECTS\active\<project-id>\history\sessions\`: project session summaries.
- `04_KICAD_PROJECTS\active\<project-id>\history\command_logs\`: project command logs.
- `04_KICAD_PROJECTS\active\<project-id>\history\failed_attempts\`: project failed attempts.
- `04_KICAD_PROJECTS\active\<project-id>\history\user_corrections\`: project user corrections.
- `04_KICAD_PROJECTS\active\<project-id>\history\design_decisions\`: project decision records.
- `04_KICAD_PROJECTS\active\<project-id>\history\issue_logs\`: project issue records.
- `04_KICAD_PROJECTS\active\<project-id>\history\workflow_runs\`: project workflow evidence.
- `04_KICAD_PROJECTS\active\<project-id>\history\verification_runs\`: project ERC, DRC, BOM, footprint, and fab-package verification evidence.
- `04_KICAD_PROJECTS\active\<project-id>\history\ai_self_reviews\`: project AI self-review records.
- `04_KICAD_PROJECTS\active\<project-id>\history\ai_scorecards\`: project AI response scorecards.
- `04_KICAD_PROJECTS\active\<project-id>\history\hallucination_risk_logs\`: project hallucination-risk records.
- `04_KICAD_PROJECTS\active\<project-id>\history\claim_evidence_matrices\`: project claim/evidence matrices.
- `04_KICAD_PROJECTS\active\<project-id>\history\quality_gate_failures\`: project quality-gate failure records.
- `04_KICAD_PROJECTS\active\<project-id>\history\uncertainty_logs\`: project uncertainty records.

## Use Rules
- After meaningful work, write a session log.
- Record commands and results in history, not memory.
- Record failed attempts when work fails or produces the wrong result.
- Record user corrections when the user says something was wrong, failed, or needs to be redone.
- Add unresolved problems to issue logs.
- Add AI self-review and scorecard records for meaningful sessions.
- Add claim/evidence matrices for major engineering claims.
- Add uncertainty and hallucination-risk logs when claims are not fully verified.
- Add quality-gate failure records when blocked or failed.
- Record ERC/DRC results or reasons they could not run.
- Do not store passwords, API keys, license keys, private tokens, or credentials in history.
- Update generated indexes after meaningful changes.

## Generated Indexes
- `02_HISTORY\MASTER_HISTORY_INDEX.md`
- `00_CODEX_START\HISTORY_INDEX.generated.md`
- `00_CODEX_START\HISTORY_INDEX.generated.json`

## Index Builder

Use `python 03_TOOLS/scripts/indexing/build_history_index.py --repo-root .` to rebuild the master history index and startup generated history indexes.

The builder is non-destructive. It scans `02_HISTORY/` and active project `history/` folders, then writes only:

- `02_HISTORY/MASTER_HISTORY_INDEX.md`
- `00_CODEX_START/HISTORY_INDEX.generated.md`
- `00_CODEX_START/HISTORY_INDEX.generated.json`

