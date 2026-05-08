# GitHub Repo Push Commands

Date: `2026-05-08`

## Authentication And Repo State

- `gh auth status`
  - authenticated as `swayerloren`
- `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
  - maintenance due: `NO`
- `git status --short --branch`
  - failed because the workspace was not yet a git repo
- `git init`
  - initialized local git repo
- `git branch -m main`
  - renamed default branch to `main`

## Safety And Ignore Audit

- secret-format `rg` scans for `ghp_`, `github_pat_`, and `sk-`
  - no live token-format matches
- assignment-style credential scan for `API_KEY`, `SECRET`, `TOKEN`, `PASSWORD`
  - no credential assignment matches
- `.env` discovery with `Get-ChildItem`
  - only `.env.example` found in ignored third-party repo content
- `Get-ChildItem -Recurse -Force -File -Include *.lck`
  - `8` lock files found, all ignored
- large-file scan over `50 MB`
  - `7` files found, all ignored

## Staging And Commit

- `git add -A`
  - staged the safe workspace under active ignore rules
- `git diff --cached --name-only | Measure-Object`
  - staged file count: `8981`
- targeted staged-content checks with `rg`
  - no staged lock files, backups, copied-board rehearsal trees, `.env` files, or ignored large build trees
- `git commit -m "Initial KiCad Engine workspace commit"`
  - created root commit `d6b881ff4bd62548235020949e63a3def1aa1bf2`

## GitHub Create And Push

- `gh repo view swayerloren/KICAD_ENGINE --json nameWithOwner,url,visibility,defaultBranchRef`
  - repo did not exist before creation
- `gh repo create KICAD_ENGINE --private --source . --remote origin`
  - created `https://github.com/swayerloren/KICAD_ENGINE`
- `git push -u origin main`
  - pushed `main` successfully and set upstream to `origin/main`

## Closeout Automation

- `python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --reason "GitHub repo initialization and private push" --apply`
  - prompt counter advanced from `2` to `3`
- `python 03_TOOLS/scripts/memory_history/build_memory_index.py --repo-root .`
  - rebuilt `00_CODEX_START/MEMORY_INDEX.generated.json` and `.md`
- `python 03_TOOLS/scripts/memory_history/build_history_index.py --repo-root .`
  - rebuilt `00_CODEX_START/HISTORY_INDEX.generated.json` and `.md`
- `python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py --repo-root .`
  - rebuilt `00_CODEX_START/AI_QUALITY_INDEX.generated.json` and `.md`
- `python 03_TOOLS/scripts/ai_quality/build_current_known_problems.py --repo-root .`
  - rebuilt `00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md`
