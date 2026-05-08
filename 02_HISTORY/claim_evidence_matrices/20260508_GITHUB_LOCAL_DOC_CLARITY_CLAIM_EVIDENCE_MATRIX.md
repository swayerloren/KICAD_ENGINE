# Claim / Evidence Matrix

| Claim | Evidence |
|---|---|
| Only docs/navigation files were changed | `git status --short --untracked-files=all` |
| No KiCad design files changed | `git diff --name-only -- "*.kicad_sch" "*.kicad_pcb" "*.kicad_pro"` returned empty |
| `.github/README.md` now explicitly scopes itself to the `.github/` folder | updated file contents |
| Root `README.md` now explains ZIP download and local VS Code use | updated `Download ZIP / Local VS Code Use` section |
| Root docs now tell users to start from `README.md` and `00_CODEX_START/START_HERE.md` | updated `README.md`, `START_HERE.md`, and `00_CODEX_START/START_HERE.md` |
