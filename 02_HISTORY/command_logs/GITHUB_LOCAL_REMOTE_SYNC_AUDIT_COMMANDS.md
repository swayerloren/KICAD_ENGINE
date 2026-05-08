# GITHUB_LOCAL_REMOTE_SYNC_AUDIT_COMMANDS

Record kind: `command_log`
Status: `VERIFIED_BY_COMMAND`
Created: `2026-05-08`
Scope: `global`
Project: `ESP32_CSI_WIFI_NODE`

## Summary

Command record for the local-versus-GitHub `03_TOOLS` visibility audit.

## Commands Run

```text
git status --ignored
git ls-files 03_TOOLS
git check-ignore -v 03_TOOLS/node_envs 03_TOOLS/python_envs 03_TOOLS/repos 03_TOOLS/tool_logs
Get-Content .gitignore
Get-Content 03_TOOLS/README.md
Get-Content 03_TOOLS/TOOLS_INDEX.md
Get-Content 03_TOOLS/INDEX.md
git fetch origin
git branch
git remote -v
git status
git log --oneline --decorate -n 10
git ls-tree -r origin/main --name-only | findstr /i "03_TOOLS"
git rev-parse HEAD
git rev-parse origin/main
Get-ChildItem / Measure-Object inspections for 03_TOOLS/node_envs
Get-ChildItem / Measure-Object inspections for 03_TOOLS/python_envs
Get-ChildItem / Measure-Object inspections for 03_TOOLS/repos
Get-ChildItem / Measure-Object inspections for 03_TOOLS/tool_logs
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --reason "GitHub local/remote sync audit" --apply
python 03_TOOLS/scripts/indexing/build_repo_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_memory_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_history_index.py --repo-root .
python 03_TOOLS/scripts/ai_quality/build_current_known_problems.py --repo-root .
python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py --repo-root .
```

## Key Results

- `git status --ignored` showed the four missing folders as explicitly ignored:
  - `03_TOOLS/node_envs/`
  - `03_TOOLS/python_envs/`
  - `03_TOOLS/repos/`
  - `03_TOOLS/tool_logs/`
- `git check-ignore -v` traced those ignores to `.gitignore` lines `35`, `34`, `39`, and `60`.
- `git status` showed a clean working tree before remediation.
- `git rev-parse HEAD` and `git rev-parse origin/main` both returned `d537a0ed98f43017b7664986589ca49c300777c1`.
- Folder inspections confirmed all four directories were non-empty and untracked.
- `check_maintenance_due.py` reported `PROMPT_COUNT: 3`, threshold `5`, and `MAINTENANCE_DUE: NO`.
- `increment_prompt_counter.py --apply` updated `PROMPT_COUNTER.md` from `3` to `4` and still reported `MAINTENANCE_DUE: NO`.
- Index rebuild commands completed and refreshed the generated repo, memory, history, known-problems, and AI-quality summaries.

## Source Or Evidence

Terminal command output captured during the audit session.

## Verification Status

Mark this record `USER_CONFIRMED` or `VERIFIED_WORKFLOW` only after human confirmation or repeatable evidence exists.

## Secret Check

No secrets should be stored in this record.
