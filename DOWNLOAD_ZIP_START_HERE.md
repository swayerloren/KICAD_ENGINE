# Download ZIP Start Here

This repo is intended to work after a normal GitHub ZIP download or a normal `git clone`.

## ZIP Workflow

1. Open the GitHub repo page.
2. Click `Code -> Download ZIP`.
3. Extract the ZIP to a local folder.
4. Open the extracted `KICAD_ENGINE` folder in VS Code.
5. Open Codex, Claude, or another AI coding agent in that workspace.
6. Start the agent from the repo root.
7. Run `python health_check.py --no-write`.
8. Paste the starter prompt from [ONE_PROMPT_START.md](ONE_PROMPT_START.md).

## Starter Prompt

```text
You are working inside the KICAD_ENGINE repo. First read README.md, ONE_PROMPT_START.md, CURRENT_STATUS.md, WORKFLOWS_INDEX.md, TOOLS_INDEX.md, and 00_CODEX_START/START_HERE.md. Run the repo health check if available. Detect local KiCad automatically if needed. Use repo-relative paths only. Do not assume C:\Users\LJ paths. Do not edit KiCad schematic or PCB files until you identify the active project, task type, live project state, and validation requirements. For PCB/routing work, obey the hard-fail routing geometry rules: no 90-degree bends, no acute angles, no ugly zig-zag traces, no bad pad-entry geometry, and no fabrication outputs without human review. After reading the repo, summarize current project status and ask what task to run next.
```

## What The AI Agent Should Read First

- `README.md`
- `ONE_PROMPT_START.md`
- `CURRENT_STATUS.md`
- `WORKFLOWS_INDEX.md`
- `TOOLS_INDEX.md`
- `00_CODEX_START/START_HERE.md`

## What Must Be Installed Locally

- KiCad for actual schematic and PCB GUI work
- VS Code recommended for workspace use
- Python for repo scripts
- Git only if you want clone/pull/branch workflows instead of ZIP download

## Optional

- Codespaces
- GitHub CLI
- devcontainer

## What You Do Not Need

- cloning extra GitHub repos for basic repo use
- someone else's local `node_envs` or `python_envs`
- someone else's `03_TOOLS/repos`
- someone else's backups or logs
- secrets, tokens, or personal machine configs
