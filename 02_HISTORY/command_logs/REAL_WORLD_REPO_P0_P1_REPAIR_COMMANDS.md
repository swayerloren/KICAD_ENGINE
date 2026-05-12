# REAL_WORLD_REPO_P0_P1_REPAIR_COMMANDS

Date: `2026-05-12`
Task type: `DOCS_ONLY`

## Commands And Tool Actions

1. Read startup/router/repair-plan docs:
   - `START_HERE_FOR_AI_AGENTS.md`
   - `AGENTS.md`
   - `README_GPT.md`
   - `FOR CHAT GPT.MD`
   - `00_CODEX_START/START_HERE.md`
   - `00_CODEX_START/AI_AGENT_FAST_CONTEXT.md`
   - `00_CODEX_START/TASK_ROUTER.md`
   - `00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md`
   - `00_CODEX_START/TASK_TYPE_TO_ALLOWED_ACTIONS.md`
   - `00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md`
   - `00_CODEX_START/TASK_TYPE_TO_OUTPUTS.md`
   - `00_CODEX_START/TASK_TYPE_TO_KNOWLEDGE_MAP.md`
   - `00_CODEX_START/TASK_TYPE_TO_TOOL_MAP.md`
   - `00_CODEX_START/TASK_TYPE_TO_RULE_MAP.md`
   - `00_CODEX_START/CURRENT_PROJECT.md`
   - `T_E_M_P/real_world_repo_audit/14_P0_P1_P2_REPAIR_PLAN.md`
2. Inspected targeted repair surfaces:
   - `CLAUDE.md`
   - `KICAD_ENGINE_WORKSPACE.code-workspace`
   - `10_KNOWLEDGE_BASE/retrieval_indexes/TASK_TO_KNOWLEDGE_MAP.md`
   - `10_KNOWLEDGE_BASE/retrieval_indexes/TASK_TO_TOOL_MAP.md`
   - `10_KNOWLEDGE_BASE/retrieval_indexes/TASK_TO_RULE_MAP.md`
   - active project report files for schematic annotation and PCB stale-state drift
3. Used `rg` searches to locate:
   - retired `knowledge_scrape` references
   - maintainer-only absolute paths
   - `STRUCTURED_S_EXPRESSION` report residue
   - stale `NO_PCB` / `NOT_RUN_NO_PCB` report language
   - route-map drift between canonical and mirror files
4. Applied docs/router/report/workspace edits with `apply_patch`
5. Validation commands:
   - `python health_check.py --repo-root . --no-write`
   - `python 03_TOOLS/scripts/knowledge_migration/rebuild_knowledge_indexes.py --help`
   - `python 03_TOOLS/scripts/knowledge_migration/rebuild_knowledge_indexes.py --repo-root .`
   - PowerShell comparison of canonical route-map tables vs retrieval mirrors
   - `git diff --cached --name-only`
   - `git status --short`
   - token-pattern `rg` scans for `ghp_`, `github_pat_`, and `sk-`
   - `.env` file scan
   - `.sfdx` presence check

## Notes

- This repair pass did not edit KiCad design files.
- No files were staged.
- No routing or fabrication generation was performed.
- Generated indexes were rebuilt because retrieval indexes changed.
