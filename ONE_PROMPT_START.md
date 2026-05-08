# One Prompt Start

This is the fastest onboarding path for a fresh ZIP or clone user.

## Use It Like This

1. Download the GitHub ZIP or clone the repo.
2. Extract or open the repo locally.
3. Open the `KICAD_ENGINE` folder in VS Code.
4. Start Codex or Claude from the repo root.
5. Paste the prompt below.

## Starter Prompt

```text
You are working inside the KICAD_ENGINE repo. First read README.md, ONE_PROMPT_START.md, CURRENT_STATUS.md, WORKFLOWS_INDEX.md, TOOLS_INDEX.md, and 00_CODEX_START/START_HERE.md. Run the repo health check if available. Detect local KiCad automatically if needed. Use repo-relative paths only. Do not assume C:\Users\LJ paths. Do not edit KiCad schematic or PCB files until you identify the active project, task type, live project state, and validation requirements. For PCB/routing work, obey the hard-fail routing geometry rules: no 90-degree bends, no acute angles, no ugly zig-zag traces, no bad pad-entry geometry, and no fabrication outputs without human review. After reading the repo, summarize current project status and ask what task to run next.
```

## What Must Exist Locally

- KiCad for live schematic or PCB GUI work
- Python for repo scripts
- VS Code recommended
- Git optional for ZIP users

## What Is Optional

- Codespaces
- GitHub CLI
- devcontainer
- Node/npm only for specific optional helper workflows
- FreeRouting only for specific routing-feasibility workflows

## What You Do Not Need

- extra cloned GitHub repos for the basic repo workflow
- `03_TOOLS/node_envs`
- `03_TOOLS/python_envs`
- `03_TOOLS/repos`
- `03_TOOLS/tool_logs`
- local backups from another machine
- secrets or personal machine paths
