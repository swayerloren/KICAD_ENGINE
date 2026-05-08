# Portability Audit

This repo is intended to be portable as a normal GitHub clone or ZIP download.

## Portable Use Means

- open the repo in VS Code
- run Codex or Claude from the repo root
- use `ONE_PROMPT_START.md` as the single copy-paste bootstrap
- run `health_check.py` or `health_check.ps1` without editing KiCad files
- let the repo auto-detect KiCad through `03_TOOLS/scripts/kicad_discovery/`
- use repo-relative paths
- rely on included rules, prompts, scripts, checklists, and indexes
- install KiCad locally for actual GUI schematic or PCB work

## Local-Only Content Policy

- `03_TOOLS/node_envs`, `03_TOOLS/python_envs`, `03_TOOLS/repos`, and `03_TOOLS/tool_logs` are local-only by default
- `99_BACKUPS` is local-only
- future routing scratch folders should stay local-only by default
- placeholder `README.md` files may be tracked when the folder purpose matters on GitHub

## What A New User Should Not Need

- hidden local environment folders
- someone else's cloned helper repos
- personal machine paths
- private backups or logs
- secrets

## Related Docs

- [ONE_PROMPT_START.md](ONE_PROMPT_START.md)
- [DOWNLOAD_ZIP_START_HERE.md](DOWNLOAD_ZIP_START_HERE.md)
- [LOCAL_SETUP_REQUIREMENTS.md](LOCAL_SETUP_REQUIREMENTS.md)
- [AGENT_STARTER_PROMPTS.md](AGENT_STARTER_PROMPTS.md)
- [SELF_CONTAINED_REPO_CHECKLIST.md](SELF_CONTAINED_REPO_CHECKLIST.md)
- [EXTERNAL_DEPENDENCIES.md](EXTERNAL_DEPENDENCIES.md)
- [docs/PYTHON_SETUP.md](docs/PYTHON_SETUP.md)
- [docs/HEALTH_CHECK.md](docs/HEALTH_CHECK.md)
- [05_OUTPUTS/release_readiness/PORTABILITY_AUDIT_REPORT.md](05_OUTPUTS/release_readiness/PORTABILITY_AUDIT_REPORT.md)
