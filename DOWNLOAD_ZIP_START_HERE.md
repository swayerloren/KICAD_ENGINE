# Download ZIP Start Here

KiCad Engine is designed to work after a normal GitHub ZIP download or a normal `git clone`.

## ZIP Workflow

1. Open the GitHub repo page.
2. Click `Code -> Download ZIP`.
3. Extract the ZIP to a local folder.
4. Open the extracted `KICAD_ENGINE` folder in VS Code.
5. Open Codex, Claude, or another AI coding agent in that workspace.
6. Paste the starter prompt from `README.md` or `ONE_PROMPT_START.md`.

## Starter Prompt

```text
You are working inside the KICAD_ENGINE repo. Before doing any work, read README.md, ONE_PROMPT_START.md if present, CURRENT_STATUS.md, WORKFLOWS_INDEX.md, TOOLS_INDEX.md, and 00_CODEX_START/START_HERE.md. Use repo-relative paths only. Do not assume the original author's local paths. Detect the local KiCad install if needed. Do not edit KiCad schematic or PCB files until you identify the active project, task type, live project state, and validation requirements. For PCB/routing work, obey the routing rules: no 90-degree bends, no acute angles, no ugly zig-zag traces, no bad pad-entry geometry, and no fabrication outputs without human review. Summarize the current repo/project status and ask what task to run next.
```

## What The AI Agent Should Read First

- `README.md`
- `ONE_PROMPT_START.md` if present
- `CURRENT_STATUS.md`
- `WORKFLOWS_INDEX.md`
- `TOOLS_INDEX.md`
- `00_CODEX_START/START_HERE.md`

## What Must Be Installed Locally

- KiCad for schematic and PCB GUI work
- VS Code recommended for workspace use
- Codex or Claude access

## Recommended

- Python
- Git

## Optional

- GitHub CLI
- Codespaces
- FreeRouting or KiBot if configured

## What You Do Not Need

- extra cloned GitHub repos for the baseline workflow
- hidden local env folders from another machine
- someone else's backups or logs
- the original author's hardcoded local paths
