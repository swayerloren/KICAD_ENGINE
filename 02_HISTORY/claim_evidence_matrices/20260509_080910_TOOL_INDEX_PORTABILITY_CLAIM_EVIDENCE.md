# Claim / Evidence Matrix - Tool Index Portability Fix

| Claim | Evidence |
| --- | --- |
| `00_CODEX_START/TOOL_INDEX.md` was machine-specific inventory | direct file audit showed absolute local paths, local venv paths, local clone paths, and observed installed-tool versions |
| The file should stay but be relabeled rather than moved | `AGENTS.md` and startup docs still reference `00_CODEX_START/TOOL_INDEX.md`; the repo already has separate portable tool-truth docs |
| Portable tool truth already exists elsewhere | root `TOOLS_INDEX.md`, `03_TOOLS/TOOLS_INDEX.md`, `EXTERNAL_DEPENDENCIES.md`, `LOCAL_SETUP_REQUIREMENTS.md`, `docs/HEALTH_CHECK.md`, `health_check.py`, `find_kicad.py`, and `python_env_check.py` |
| Startup prompts now prefer portable truth | updated `README.md`, `ONE_PROMPT_START.md`, and `00_CODEX_START/START_HERE.md` |
