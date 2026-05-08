# Agent Starter Prompts

## Default Starter Prompt

```text
You are working inside the KICAD_ENGINE repo. First read README.md, CURRENT_STATUS.md, WORKFLOWS_INDEX.md, TOOLS_INDEX.md, and 00_CODEX_START/START_HERE.md. Use repo-relative paths. Do not assume C:\Users\LJ paths. Do not edit KiCad schematic or PCB files until you understand the active project, task type, live project state, and validation requirements. For PCB/routing work, obey 45-degree/no-acute-angle routing rules, run DRC/checks, and require human review before fabrication.
```

## Docs/Audit Variant

```text
You are working inside the KICAD_ENGINE repo. First read README.md, CURRENT_STATUS.md, WORKFLOWS_INDEX.md, TOOLS_INDEX.md, and 00_CODEX_START/START_HERE.md. Use repo-relative paths. This is a docs or audit task only. Do not edit KiCad schematic or PCB files. Stage only safe docs, indexes, and reports.
```
