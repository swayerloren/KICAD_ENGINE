# Agent Quality Index

Status: `SCAFFOLD`

## Related Existing System

- `00_CODEX_START/AI_SELF_REVIEW_RULES.md`
- `00_CODEX_START/AI_TRUTHFULNESS_SCORING.md`
- `00_CODEX_START/AI_RESPONSE_QUALITY_GATE.md`
- `03_TOOLS/scripts/ai_quality/`
- `02_HISTORY/ai_self_reviews/`
- `02_HISTORY/ai_scorecards/`

## Local Policy Files

- `AI_SELF_REVIEW_RULES.md`
- `AI_TRUTHFULNESS_SCORING.md`
- `AI_HALLUCINATION_RISK_RULES.md`
- `AI_RESPONSE_QUALITY_GATE.md`
- `AI_EVIDENCE_REQUIREMENTS.md`
- `AI_PCB_FAILURE_MODES.md`
- `CODEX_KICAD_FAILURE_PATTERNS.md`
- `FALSE_PASS_PATTERNS.md`
- `AI_AGENT_PCB_REVIEW_CHECKLIST.md`
- `templates/AI_RESPONSE_SCORECARD_TEMPLATE.md`
- `templates/CLAIM_EVIDENCE_MATRIX_TEMPLATE.md`
- `templates/UNCERTAINTY_LOG_TEMPLATE.md`

## Required Use

Use these files with `09_ACCURACY_ENGINE/` whenever an agent makes claims about components, datasheets, symbols, footprints, schematics, PCBs, BOMs, or fab outputs.


## PURPOSE

Store AI quality support artifacts that complement startup scoring and history evidence.

## WHAT_BELONGS_HERE

Quality-gate indexes, scorecard support notes, uncertainty examples, and hallucination-risk support records.

## WHAT_DOES_NOT_BELONG_HERE

Fake scorecards, project-specific records that belong in project history, secrets, or unsupported engineering claims.

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
