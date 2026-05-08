# AI Reliability Memory

Status: `ACTIVE_GLOBAL_MEMORY`

Reusable reliability lessons for AI agents working in KiCad Engine.

## Rules

- Prefer verified facts over broad confident prose.
- Score responses strictly using `00_CODEX_START/AI_TRUTHFULNESS_SCORING.md`.
- Use `BLOCKED_UNTIL_HUMAN_REVIEW` when high-risk engineering evidence is missing.
- Do not hide uncertainty in final answers.
- Do not treat memory as proof; memory points to evidence.

## Current Durable Lessons

- Connector footprints require exact manufacturer drawing review and human orientation confirmation before approval.
## 2026-05-07 Memory/History Reliability Rule

Status: `USER_CONFIRMED`

Agents must not infer current project truth from the newest or longest report. Use the evidence hierarchy and project current-state maintenance files. Codex/Claude summaries are low-level evidence and cannot override KiCad GUI evidence, ERC/DRC reports, parsed design files, or current maintenance indexes.
