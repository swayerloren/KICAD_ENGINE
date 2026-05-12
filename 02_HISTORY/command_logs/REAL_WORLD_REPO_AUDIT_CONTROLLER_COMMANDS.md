# REAL_WORLD_REPO_AUDIT_CONTROLLER Commands

Date: `2026-05-12`
Repo: `C:\Users\LJ\GitHub\KICAD_ENGINE`
Task type: `AUDIT_ONLY`

## Read-Only Commands Run

| Command | Purpose | Key result |
| --- | --- | --- |
| `python health_check.py --repo-root . --no-write` | baseline onboarding health | `PASS=18 WARN=2 FAIL=0`; warn: use KiCad Python for board-aware `pcbnew` work |
| `python 03_TOOLS/scripts/kicad_discovery/find_kicad.py` | detect KiCad/CLI/Python context | KiCad `9.0`, `kicad-cli 9.0.7`, GUI on `PATH`, `pcbnew` only via KiCad Python |
| `python 03_TOOLS/scripts/kicad_discovery/validate_kicad_install.py` | validate local KiCad install | `PASS` for KiCad root, GUI, CLI, and `pcbnew` via KiCad Python |
| `python 03_TOOLS/scripts/python_env_check.py` | baseline Python readiness | Python `3.12.10`, hidden repo env not required |
| `python setup/verify_optional_kicad_tools.py --dry-run` | optional-tool presence audit | `present=1`, `missing_or_manual=16` |
| `git status --short` | inspect local checkout state | dirty local checkout with active-project modifications and many untracked files |
| `git ls-files` size analysis | estimate real GitHub ZIP payload | `6999` tracked files; approx `316.94 MB` tracked payload |
| `git ls-files --others --exclude-standard` count | estimate local noise not in tracked payload | `2836` untracked files in current local checkout |

## Important File Inspections

- startup/router files under `00_CODEX_START/`
- user-facing onboarding docs at repo root
- `.prompts/`, `.vscode/`, `.codex/`, `CLAUDE.md`
- optional-tool, portability, security, and public-release docs
- active example-project gate reports under
  `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/`

## Key Evidence Captured

- active example-project schematic gate: `FAIL`
- active example-project sandbox gate: `BLOCKED`
- latest prelayout result: `3` variants, `0` passing, placement/routing `BLOCKED`
- final routed review: `BLOCKED_BEFORE_NOT_FINAL_EXPORT`
- tracked payload includes large committed evidence/index assets

## Safety Statement

All commands used in this audit were read-only with respect to KiCad design
files and fabrication outputs.
