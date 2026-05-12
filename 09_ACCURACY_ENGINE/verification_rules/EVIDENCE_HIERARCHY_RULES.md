# Evidence Hierarchy Rules

Status: `ACTIVE_EVIDENCE`

Generated date/time: `2026-05-07`

Project: `KICAD_ENGINE`

Supersedes: `None`

Superseded by: `None`

Evidence files: `AGENTS.md`, `README_GPT.md`, `FOR CHAT GPT.MD`, `01_MEMORY`, `02_HISTORY`.

Current relevance: mandatory interpretation rule for memory/history/report maintenance.

## Rule

Codex summaries are not primary evidence.

Use this hierarchy when compiling current truth:

1. Live KiCad GUI state and screenshots.
2. KiCad-native ERC/DRC evidence.
3. `kicad-cli` ERC/DRC output.
4. Parsed KiCad design files.
5. Generated reports and machine-readable JSON.
6. Canonical normalized summaries and policy files.
7. Training, forum, video, and case-study guidance.
8. Codex/Claude summary text.

## Required Behavior

- If higher-level evidence contradicts lower-level summaries, trust the higher-level evidence.
- If the only source is an AI summary, mark the claim `UNVERIFIED` or `NEEDS_HUMAN_REVIEW`.
- If the only non-AI source is forum, video, training, or case-study material,
  keep the claim at `GUIDANCE_ONLY`, `UNVERIFIED`, or `NEEDS_HUMAN_REVIEW`.
- Current-state files must cite evidence paths, not just session prose.
