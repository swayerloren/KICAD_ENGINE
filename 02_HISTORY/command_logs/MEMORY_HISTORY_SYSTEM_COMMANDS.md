# Memory History System Commands

Status: `UNVERIFIED_COMMAND_LOG`

## Scope

- Task: Build durable learning, memory, history, issue, and correction system.
- KiCad design files edited: No.
- Tools installed: No.

## Commands Run

```text
Get-Content -Raw -LiteralPath AGENTS.md
Get-Content -Raw -LiteralPath README.md
Get-Content -Raw -LiteralPath README_GPT.md
Get-Content -Raw -LiteralPath "FOR CHAT GPT.MD"
Get-Content -Raw -LiteralPath 00_CODEX_START/START_HERE.md
Get-Content -Raw -LiteralPath 00_CODEX_START/SESSION_START_CHECKLIST.md
Get-Content -Raw -LiteralPath 00_CODEX_START/WORKFLOW_RULES.md
Get-Content -Raw -LiteralPath 00_CODEX_START/SAFETY_RULES.md
Get-Content -Raw -LiteralPath 00_CODEX_START/CONTROL_PLANES.md
Get-Content -Raw -LiteralPath 00_CODEX_START/REPO_MAP.md
Get-Content -Raw -LiteralPath 00_CODEX_START/TOOL_INDEX.md
Get-Content -Raw -LiteralPath 00_CODEX_START/MEMORY_INDEX.md
Get-Content -Raw -LiteralPath 00_CODEX_START/HISTORY_INDEX.md
Get-Content -Raw -LiteralPath 00_CODEX_START/PROJECT_INDEX.md
Get-Content -Raw -LiteralPath 00_CODEX_START/CURRENT_PROJECT.md
Get-ChildItem -LiteralPath 01_MEMORY -Force
Get-ChildItem -LiteralPath 02_HISTORY -Force
Get-ChildItem -LiteralPath 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory -Force -Recurse
Get-ChildItem -LiteralPath 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/history -Force -Recurse
Get-ChildItem -LiteralPath 04_KICAD_PROJECTS/active -Directory -Force
New-Item -ItemType Directory -Force for global and project memory/history folders
Copy-Item startup and handoff docs into 99_BACKUPS/pre_codex_edits/memory_history_system_docs_20260502_223950
python -m py_compile 03_TOOLS/scripts/memory_history/*.py
Get-ChildItem 03_TOOLS/scripts/memory_history -Filter *.py | python -m py_compile
python 03_TOOLS/scripts/memory_history/build_memory_index.py --repo-root .
python 03_TOOLS/scripts/memory_history/build_history_index.py --repo-root .
python 03_TOOLS/scripts/memory_history/create_session_log.py --help
python 03_TOOLS/scripts/memory_history/create_failed_attempt.py --help
python 03_TOOLS/scripts/memory_history/update_project_memory_stub.py --help
python 03_TOOLS/scripts/memory_history/update_global_memory_stub.py --help
python 03_TOOLS/scripts/memory_history/create_failed_attempt.py --repo-root . --scope global --title "PowerShell wildcard py_compile invocation failed" ...
python 03_TOOLS/scripts/memory_history/create_session_log.py --repo-root . --scope global --title "Memory history learning system created" ...
python health_check.py --repo-root . --no-write
Resolve-Path 03_TOOLS/scripts/memory_history/__pycache__; Remove-Item verified generated cache folder
```

## Result

- Startup and context files read.
- Existing global memory/history and active project memory/history inspected.
- New folders, templates, docs, project memory files, project history folders, scripts, and example records created.
- Memory/history scripts compile after using resolved file paths.
- Generated memory/history indexes created.
- Health check passed with `PASS=131 WARN=0 FAIL=0`.
- Generated Python `__pycache__` under the new script folder was removed after verifying the resolved path was inside `03_TOOLS/scripts/memory_history`.

## Failure Recorded

- The wildcard `python -m py_compile 03_TOOLS/scripts/memory_history/*.py` failed because PowerShell did not expand the wildcard for Python.
- Failed attempt record: `02_HISTORY/failed_attempts/20260502_224812_PowerShell_wildcard_py_compile_invocation_failed.md`.
