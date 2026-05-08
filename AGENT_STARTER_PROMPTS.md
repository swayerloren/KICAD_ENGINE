# Agent Starter Prompts

## Default Starter Prompt

```text
You are working inside the KICAD_ENGINE repo. First read README.md, ONE_PROMPT_START.md, CURRENT_STATUS.md, WORKFLOWS_INDEX.md, TOOLS_INDEX.md, and 00_CODEX_START/START_HERE.md. Run the repo health check if available. Detect local KiCad automatically if needed. Use repo-relative paths only. Do not assume C:\Users\LJ paths. Do not edit KiCad schematic or PCB files until you identify the active project, task type, live project state, and validation requirements. For PCB/routing work, obey the hard-fail routing geometry rules: no 90-degree bends, no acute angles, no ugly zig-zag traces, no bad pad-entry geometry, and no fabrication outputs without human review. After reading the repo, summarize current project status and ask what task to run next.
```

## Docs/Audit Variant

```text
You are working inside the KICAD_ENGINE repo. First read README.md, ONE_PROMPT_START.md, CURRENT_STATUS.md, WORKFLOWS_INDEX.md, TOOLS_INDEX.md, and 00_CODEX_START/START_HERE.md. Run the repo health check if available. Use repo-relative paths only. This is a docs, audit, or setup-hardening task. Do not edit KiCad schematic or PCB files. Stage only safe docs, scripts, configs, indexes, and reports.
```
