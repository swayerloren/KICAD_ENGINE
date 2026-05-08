# Global Hallucination Risks

Status: `ACTIVE_GLOBAL_MEMORY`

Reusable hallucination risks across KiCad Engine.

## Known Risk Patterns

- Inferring footprints from generic KiCad names.
- Inferring connector orientation from a screenshot or 3D model.
- Claiming ERC/DRC status without command output.
- Reusing datasheet values from memory without source verification.
- Treating `NOT_FINAL` outputs as fabrication-ready.
- Treating automated schematic crop generation, annotation checks, footprint assignment checks, or ERC status as proof of human-readable schematic quality.

## Required Mitigation

Log risk records under `02_HISTORY/hallucination_risk_logs/` or project `history/hallucination_risk_logs/`.

## Human-Readable Visual Gate Risk

Status: `USER_CONFIRMED`

Risk: A rendered schematic may remain visually unacceptable even when file-level annotation checks, ERC, footprint assignment checks, no visible footprint fields, and automated crop generation pass.

Required mitigation: Agents must inspect rendered full-page and close-up schematic images against `09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md` and `09_ACCURACY_ENGINE/checklists/SCHEMATIC_HUMAN_READABILITY_CHECKLIST.md`. If the agent cannot inspect the rendered images, the visual status must be `VISUAL_NOT_VERIFIED`, not `PASS`.
## 2026-05-07 Stale Report Hallucination Risk

Status: `ACTIVE_BLOCKER`

Risk: Agents may hallucinate progress by reading stale reports with "current", "latest", "ready", or "pass" wording after later evidence superseded them.

Mitigation: Run memory maintenance, inspect `SUPERSEDED_REPORTS.md`, and apply `EVIDENCE_HIERARCHY_RULES.md` before making current-status claims.
