# Agent Starter Prompts

## Default Starter Prompt

```text
You are working inside the KICAD_ENGINE repo. Before doing any work, read README.md, ONE_PROMPT_START.md if present, CURRENT_STATUS.md, WORKFLOWS_INDEX.md, TOOLS_INDEX.md, and 00_CODEX_START/START_HERE.md. Use repo-relative paths only. Do not assume the original author's local paths. Detect the local KiCad install if needed. Do not edit KiCad schematic or PCB files until you identify the active project, task type, live project state, and validation requirements. For PCB/routing work, obey the routing rules: no 90-degree bends, no acute angles, no ugly zig-zag traces, no bad pad-entry geometry, and no fabrication outputs without human review. Summarize the current repo/project status and ask what task to run next.
```

## Docs / Audit Variant

```text
You are working inside the KICAD_ENGINE repo. Before doing any work, read README.md, CURRENT_STATUS.md, WORKFLOWS_INDEX.md, TOOLS_INDEX.md, and 00_CODEX_START/START_HERE.md. Use repo-relative paths only. This is a docs, audit, or repo-structure task only. Do not edit KiCad schematic or PCB files. Stage only safe docs, scripts, configs, indexes, and reports.
```
