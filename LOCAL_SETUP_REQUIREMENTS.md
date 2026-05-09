# Local Setup Requirements

## Required

- KiCad: required for real schematic and PCB GUI work
- Python: required for repo scripts, checks, and index builders

## Recommended

- VS Code: recommended editor/workspace shell
- Codex or Claude: recommended AI agent interface
- Git: recommended for normal clone, sync, branch, and PR workflows

## Optional

- GitHub CLI
- Codespaces
- devcontainer
- Node/npm only when a specific optional helper workflow calls for it
- FreeRouting only when a routing-feasibility workflow explicitly calls for it

## First Commands For A Fresh Checkout

```powershell
python health_check.py --no-write
python 03_TOOLS/scripts/python_env_check.py
python 03_TOOLS/scripts/kicad_discovery/validate_kicad_install.py
python 03_TOOLS/scripts/kicad_api/pcbnew_import_check.py
```

## Board-Aware Note

`kicad-cli` and KiCad GUI are enough for many tasks. Some board-aware scripts also need `pcbnew`, and normal Python may not be able to import it directly. When that happens, the repo should use KiCad's bundled Python context instead of any hidden repo-local venv.

## Not Required For First Use

- extra cloned GitHub repos
- private local `venv` folders
- `node_modules`
- local logs
- local backups
- personal secrets or credentials
