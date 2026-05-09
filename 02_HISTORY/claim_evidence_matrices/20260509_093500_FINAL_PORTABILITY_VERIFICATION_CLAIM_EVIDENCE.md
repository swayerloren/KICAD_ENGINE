# Claim Evidence Matrix - Final Portability Verification

Date: `2026-05-09`
Task type: `GITHUB_DOCS_ONLY`

| Claim | Evidence |
| --- | --- |
| No tracked `routing_work` scratch payload remains. | `git ls-files 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work` returned only `routing_work/README.md`. |
| No tracked generated KiCad library local index payload remains. | `git ls-files 03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES` returned only `GENERATED_INDEXES/README.md`. |
| `00_CODEX_START/TOOL_INDEX.md` is clearly marked machine-specific. | `Get-Content 00_CODEX_START\TOOL_INDEX.md -TotalCount 40` shows `WARNING: MACHINE-SPECIFIC INVENTORY` plus portable-tool-truth links. |
| Historical local paths are documented as evidence only. | `README.md`, `ONE_PROMPT_START.md`, `docs/PATH_PORTABILITY.md`, and `00_CODEX_START/PATH_PORTABILITY_RULES.md` explicitly warn against using old absolute paths as current config. |
| `pcbnew` is a warning for onboarding, not a hard fail. | `python health_check.py --no-write` and `powershell ... health_check.ps1 -NoWrite` both returned `PASS=18 WARN=2 FAIL=0`; `health_check.py` only upgrades to fail with `--require-pcbnew`. |
| Baseline startup does not require extra cloned repos. | `EXTERNAL_DEPENDENCIES.md` classifies extra cloned repos as `NOT_INCLUDED` and `03_TOOLS/README.md` says repos under `03_TOOLS/repos/` are optional helper sources only. |
| No KiCad design files changed in this task. | `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'` returned no files. |
