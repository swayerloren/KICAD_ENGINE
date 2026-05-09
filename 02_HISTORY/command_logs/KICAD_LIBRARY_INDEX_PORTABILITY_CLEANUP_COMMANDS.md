# Command Log - KiCad Library Index Portability Cleanup

Date: `2026-05-09`

## Commands Run

```powershell
Get-Content -Raw AGENTS.md
Get-Content -Raw 05_OUTPUTS/release_readiness/PORTABILITY_TOOLCHAIN_AUDIT_REPORT.md
Get-Content -Raw .gitignore
Get-ChildItem -Force 03_TOOLS/kicad_library_intelligence
Get-Content -Raw 03_TOOLS/kicad_library_intelligence/LIBRARY_TABLE_GUIDE.md
Get-Content -Raw README_GPT.md
Get-Content -Raw "FOR CHAT GPT.MD"
Get-Content -Raw 00_CODEX_START/START_HERE.md
Get-Content -Raw 00_CODEX_START/PROMPT_COUNTER_RULES.md
Get-Content -Raw 00_CODEX_START/CURRENT_PROJECT.md
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
Get-Content -Raw 03_TOOLS/scripts/execution_contract/README.md
Get-Content -Raw 00_CODEX_START/PATH_PORTABILITY_RULES.md
Get-ChildItem -Force 03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES
git ls-files 03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES
Get-Content -TotalCount 80 03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/footprint_index_summary.md
Get-Content -TotalCount 80 03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/symbol_index_summary.md
Get-Content -TotalCount 80 03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/3d_model_summary.md
Get-Content -Raw 03_TOOLS/kicad_library_intelligence/README.md
Get-Content -Raw 03_TOOLS/scripts/kicad_libraries/index_symbols.py
Get-Content -Raw 03_TOOLS/scripts/kicad_libraries/index_footprints.py
Get-Content -Raw 03_TOOLS/scripts/kicad_libraries/index_3d_models.py
Get-Content -Raw 03_TOOLS/scripts/kicad_libraries/find_symbol_candidates.py
Get-Content -Raw 03_TOOLS/scripts/kicad_libraries/find_footprint_candidates.py
Get-Content -Raw 03_TOOLS/scripts/kicad_libraries/kicad_library_common.py
git status --short
rg -n --hidden --glob "03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/*" "C:\\Users\\LJ|file:///|AppData|KiCad\\|[A-Z]:\\"
git rm -r --cached -- 03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES
python 03_TOOLS/scripts/kicad_libraries/index_symbols.py --output-dir T_E_M_P/kicad_library_regen_smoke
python 03_TOOLS/scripts/kicad_libraries/index_footprints.py --output-dir T_E_M_P/kicad_library_regen_smoke
python 03_TOOLS/scripts/kicad_libraries/index_3d_models.py --output-dir T_E_M_P/kicad_library_regen_smoke
python 03_TOOLS/scripts/kicad_libraries/find_symbol_candidates.py "USB-C connector generic" --output-dir T_E_M_P/kicad_library_regen_smoke
python 03_TOOLS/scripts/kicad_libraries/find_footprint_candidates.py "USB-C connector generic" --output-dir T_E_M_P/kicad_library_regen_smoke
python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply
```

## Important Results

- `check_maintenance_due.py` returned `MAINTENANCE_NOT_DUE`.
- `git ls-files` showed `22` tracked generated files under `GENERATED_INDEXES`.
- The staged cleanup removed those generated files from Git tracking only.
- Regeneration smoke tests succeeded after one footprint-index timeout retry with a longer timeout.
