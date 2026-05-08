# 03_TOOLS/python_envs

## PURPOSE

Local-only Python virtual environments for KiCad Engine helper tools, isolated CLI installs, and Windows GUI automation packages.

## WHAT_BELONGS_HERE

- Tool-specific virtual environments such as `kicad-mcp-pro`, `kicad-happy`, `kibot`, `PcbDraw`, and `windows_gui`.
- Installed Python packages, console entry points, and environment metadata.
- Local-only package state used to run approved helper tools without polluting system Python.

## WHY_CONTENTS_ARE_IGNORED

- Virtual environments are machine-specific and not reproducible as tracked source.
- They contain installed packages, executables, caches, and generated files that do not belong in the GitHub payload.
- Pushing them would add unnecessary size and risk stale or unsafe dependency state.

## HOW_TO_RECREATE_LOCALLY

1. Use the tracked tool docs in `00_CODEX_START/TOOL_INDEX.md`, `03_TOOLS/TOOLS_INDEX.md`, and `03_TOOLS/tool_logs/README.md` as the source of truth for which environments are expected.
2. Create a dedicated virtual environment under this folder for the approved tool.
3. Install only the packages required for that tool's local workflow.
4. Rebuild the environment when dependency state changes instead of trying to preserve it in Git.

## WHAT_SHOULD_NEVER_BE_COMMITTED

- `Lib/site-packages/`, `Scripts/`, and interpreter binaries
- package caches and compiled bytecode
- local secrets, tokens, or private configuration
- machine-specific activation scripts or generated logs

## PUBLIC_RELEASE_NOTES

GitHub should show this folder as a placeholder only. The actual local environments remain ignored on purpose.

ZIP users do not need this folder populated for the basic workflow.
