# KiCad Library Intelligence Session

Date: 2026-05-02

Task: build a KiCad library intelligence layer so AI agents can understand installed KiCad symbols, footprints, 3D models, and library tables from VS Code.

## Actions

- Read mandatory startup context.
- Confirmed KiCad 9 install paths exist under `C:\Program Files\KiCad\9.0`.
- Inspected stock KiCad `share`, `lib`, and `etc` directories read-only.
- Inspected accessible user KiCad config roots read-only.
- Created library intelligence documentation under `03_TOOLS/kicad_library_intelligence`.
- Created read-only Python scripts under `03_TOOLS/scripts/kicad_libraries`.
- Generated symbol, footprint, and 3D model indexes under `GENERATED_INDEXES`.
- Generated sample symbol and footprint candidate files for requested parts/topics.

## Commands Run

```powershell
python -m py_compile "03_TOOLS\scripts\kicad_libraries\kicad_library_common.py" "03_TOOLS\scripts\kicad_libraries\index_symbols.py" "03_TOOLS\scripts\kicad_libraries\index_footprints.py" "03_TOOLS\scripts\kicad_libraries\index_3d_models.py" "03_TOOLS\scripts\kicad_libraries\find_symbol_candidates.py" "03_TOOLS\scripts\kicad_libraries\find_footprint_candidates.py"
python "03_TOOLS\scripts\kicad_libraries\index_symbols.py" --kicad-root "C:\Program Files\KiCad\9.0"
python "03_TOOLS\scripts\kicad_libraries\index_footprints.py" --kicad-root "C:\Program Files\KiCad\9.0"
python "03_TOOLS\scripts\kicad_libraries\index_3d_models.py" --kicad-root "C:\Program Files\KiCad\9.0"
python "03_TOOLS\scripts\kicad_libraries\find_symbol_candidates.py" "ESP32-S3-WROOM-1"
python "03_TOOLS\scripts\kicad_libraries\find_footprint_candidates.py" "ESP32-S3-WROOM-1"
python "03_TOOLS\scripts\kicad_libraries\find_symbol_candidates.py" "STM32F103C8T6"
python "03_TOOLS\scripts\kicad_libraries\find_footprint_candidates.py" "STM32F103C8T6"
python "03_TOOLS\scripts\kicad_libraries\find_symbol_candidates.py" "USB-C connector generic"
python "03_TOOLS\scripts\kicad_libraries\find_footprint_candidates.py" "USB-C connector generic"
python "03_TOOLS\scripts\kicad_libraries\find_symbol_candidates.py" "MCP2562FD"
python "03_TOOLS\scripts\kicad_libraries\find_footprint_candidates.py" "MCP2562FD"
```

## Safety Notes

- Scripts write generated outputs only under `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES` by default.
- Scripts refuse output paths inside the KiCad install root or KiCad user config roots.
- Scripts do not run KiCad executables.
- Scripts do not edit symbol, footprint, 3D model, library table, or project files.

## Validation

- Required file check passed for 22 files.
- Python compile check passed.
- Generated JSON parse checks passed for symbol, footprint, 3D model, and candidate outputs.
- Candidate output counts:
  - `ESP32-S3-WROOM-1`: 20 symbol candidates, 20 footprint candidates.
  - `STM32F103C8T6`: 20 symbol candidates, 0 footprint candidates.
  - `USB-C connector generic`: 20 symbol candidates, 20 footprint candidates.
  - `MCP2562FD`: 8 symbol candidates, 0 footprint candidates.
- ASCII scan passed for docs, scripts, history, and generated Markdown summaries.
- Protected KiCad project file guard passed.
