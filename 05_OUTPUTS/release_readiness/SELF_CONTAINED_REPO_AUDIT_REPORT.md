# Self-Contained Repo Audit Report

Date: `2026-05-08`

## Verdict

The repo is self-contained enough for the baseline workflow:

1. Download ZIP or `git clone`.
2. Open the repo root in VS Code.
3. Run `python health_check.py --no-write`.
4. Paste the single prompt from `ONE_PROMPT_START.md`.
5. Let the agent read the included startup docs and guide the next step.

## Included For Basic Use

- onboarding docs at the repo root
- startup rules under `00_CODEX_START/`
- prompts under `.prompts/`
- helper scripts under `03_TOOLS/scripts/`
- health check and KiCad discovery
- example/active project structure
- validation rules, routing checks, and task contracts

## Not Required For Basic Use

- `03_TOOLS/node_envs`
- `03_TOOLS/python_envs`
- `03_TOOLS/repos`
- `03_TOOLS/tool_logs`
- `99_BACKUPS`
- extra cloned GitHub repos
- another machine's KiCad paths
- hidden private virtual environments

## Required External Installs

- `Python`
- `KiCad` only when the workflow needs live schematic/PCB GUI work or board-aware KiCad tooling

## Optional External Installs

- `VS Code`
- `Codex` or `Claude`
- `Git`
- `GitHub CLI`
- `Codespaces`
- `devcontainer`
- `FreeRouting`
- `Node/npm`

## Onboarding Status

- `README.md` points to `ONE_PROMPT_START.md`: `YES`
- `DOWNLOAD_ZIP_START_HERE.md` exists: `YES`
- `AGENT_STARTER_PROMPTS.md` exists: `YES`
- `LOCAL_SETUP_REQUIREMENTS.md` exists: `YES`
- `SELF_CONTAINED_REPO_CHECKLIST.md` exists: `YES`
- `EXTERNAL_DEPENDENCIES.md` exists: `YES`
- `docs/PYTHON_SETUP.md` exists: `YES`
- `docs/HEALTH_CHECK.md` exists: `YES`

## Constraints That Still Apply

- KiCad design files still require project and phase-gate discipline.
- Human KiCad review is still required before fabrication.
- Historical reports may still mention absolute local paths.
- Some advanced helper workflows remain optional and local-only by design.
