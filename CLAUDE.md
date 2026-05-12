# CLAUDE.md

Canonical startup for Claude must match `START_HERE_FOR_AI_AGENTS.md` and
`AGENTS.md`.

Read in this order before acting:

1. `START_HERE_FOR_AI_AGENTS.md`
2. `AGENTS.md`
3. `README_GPT.md`
4. `FOR CHAT GPT.MD`
5. `00_CODEX_START/START_HERE.md`
6. `00_CODEX_START/AI_AGENT_FAST_CONTEXT.md`
7. `00_CODEX_START/TASK_ROUTER.md`
8. `00_CODEX_START/CURRENT_PROJECT.md`
9. `00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md`
10. `00_CODEX_START/TASK_TYPE_TO_ALLOWED_ACTIONS.md`
11. `00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md`
12. `00_CODEX_START/TASK_TYPE_TO_OUTPUTS.md`
13. `00_CODEX_START/TASK_TYPE_TO_KNOWLEDGE_MAP.md`
14. `00_CODEX_START/TASK_TYPE_TO_TOOL_MAP.md`
15. `00_CODEX_START/TASK_TYPE_TO_RULE_MAP.md`

Task-routing rules:

- Use `KNOWLEDGE_RETRIEVAL` for shortest trusted repo knowledge lookup.
- Use `GITHUB_PUSH_PUBLIC_RELEASE` for push/public-release readiness and safety.
- Do not use retired `knowledge_scrape` residue as a live routing source.

Evidence rules:

- Prefer official datasheets, official app notes, official KiCad docs, KLC or
  library sources, and official fabricator docs before forums or blogs.
- Treat extracted PDF Markdown as secondary only.
- Use the original PDF for pinouts, footprints, package drawings, layout
  diagrams, and tables.
- Codex/Claude summaries are not proof. Use local file evidence, CLI evidence,
  GUI evidence, and source-registry context in that order.
- Never modify active KiCad project files until the repo sandbox and
  verification gates pass.
