# KiBot Install Session

Date: 2026-04-30

## Scope
Installed and safe-tested only KiBot as the deterministic KiCad fabrication and documentation automation engine.

## Result
- Status: installed, not project-tested.
- Repo: `03_TOOLS\repos\KiBot`
- Branch: `master`
- Commit: `367a2e04122aa46413a30e61cb213bfe7223c8c8`
- Installed version: KiBot 1.8.5
- Environment: `03_TOOLS\python_envs\kibot`
- CLI: `C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\kibot\Scripts\kibot.exe`
- KiCad Python: `C:\Program Files\KiCad\9.0\bin\python.exe`
- KiCad version via `pcbnew`: 9.0.7

## Actions
- Read workspace startup files, relevant memory, KiBot install docs, dependency docs, setup metadata, and sample configs.
- Confirmed Docker is not available, so the documented Docker-preferred path is blocked locally.
- Created a KiCad-Python-based virtual environment under `03_TOOLS\python_envs\kibot`.
- Installed KiBot and Python dependencies into the venv.
- Added `lxml` after KiBot output plugin listing reported it missing.
- Did not edit real KiCad project files.
- Did not generate final manufacturing outputs.
- Created starter config template `04_KICAD_PROJECTS\templates\kibot_default.kibot.yaml`.

## Safe Tests
- Imported `kibot` and KiCad `pcbnew` from the final venv with KiCad paths set.
- Ran `kibot --version`.
- Ran `kibot --help`.
- Ran output and preflight help checks for requested output families.
- Parsed the starter template as YAML.
- Ran `kibot -c 04_KICAD_PROJECTS\templates\kibot_default.kibot.yaml --list --only-names`.

## Command Pattern
Use KiCad paths when invoking KiBot:

```powershell
$env:PATH = "C:\Program Files\KiCad\9.0\bin;$env:PATH"
$env:PYTHONPATH = "C:\Program Files\KiCad\9.0\bin\Lib\site-packages;C:\Program Files\KiCad\9.0\bin"
& "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\kibot\Scripts\kibot.exe" -c "<project.kibot.yaml>" -b "<board.kicad_pcb>" -e "<schematic.kicad_sch>" -d "<output_dir>" -A
```

`-A` disables KiBot auto-downloads and should remain enabled for first tests.

## Limits
- KiBot warns that running on Windows is experimental.
- No real KiCad project was tested.
- The starter config is syntactically validated but not output-validated against a project.
- Outputs are not final until ERC, DRC, BOM, footprint, netlist, datasheet, and visual review are complete.

## Next Recommended Step
Copy a disposable KiCad sample project, run KiBot with the starter template into `05_OUTPUTS\tool_tests\kibot`, inspect all generated outputs, then compare ERC/DRC results with direct `kicad-cli` checks.
