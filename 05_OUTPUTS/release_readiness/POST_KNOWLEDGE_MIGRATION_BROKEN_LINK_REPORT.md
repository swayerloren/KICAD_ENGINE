# Post-Knowledge-Migration Broken Link Report

Generated: `2026-05-12`

Status: `PASS_ACTIVE_ROUTING_LINKS`

## Scope

This rerun checked the active startup/routing docs that matter for normal agent
operation after the retired `knowledge_scrape/` migration.

## Markdown Link Scan

- files scanned:
  - `README.md`
  - `START_HERE_FOR_AI_AGENTS.md`
  - `00_CODEX_START/TASK_ROUTER.md`
  - `00_CODEX_START/AI_AGENT_FAST_CONTEXT.md`
  - `README_GPT.md`
  - `FOR CHAT GPT.MD`
- local Markdown links checked: `16`
- missing local Markdown links: `0`

## Task-Map / Retrieval-Map Existence

Verified present:

- `00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md`
- `00_CODEX_START/TASK_TYPE_TO_ALLOWED_ACTIONS.md`
- `00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md`
- `00_CODEX_START/TASK_TYPE_TO_OUTPUTS.md`
- `00_CODEX_START/TASK_TYPE_TO_KNOWLEDGE_MAP.md`
- `00_CODEX_START/TASK_TYPE_TO_TOOL_MAP.md`
- `00_CODEX_START/TASK_TYPE_TO_RULE_MAP.md`
- `10_KNOWLEDGE_BASE/retrieval_indexes/MASTER_KNOWLEDGE_INDEX.md`
- `10_KNOWLEDGE_BASE/retrieval_indexes/TASK_TO_KNOWLEDGE_MAP.md`
- `10_KNOWLEDGE_BASE/retrieval_indexes/TASK_TO_RULE_MAP.md`
- `10_KNOWLEDGE_BASE/retrieval_indexes/TASK_TO_TOOL_MAP.md`

Missing map files: `0`

## `knowledge_scrape` Reference Audit

Active-doc `knowledge_scrape` mentions were reviewed and are acceptable because
they are:

- retirement notices,
- migration-history references,
- backup references, or
- generated history/index provenance.

Bad active-route references: `0`

## Conclusion

No broken active startup/routing links were found, and no live routing document
still requires `knowledge_scrape/` as a dependency.
