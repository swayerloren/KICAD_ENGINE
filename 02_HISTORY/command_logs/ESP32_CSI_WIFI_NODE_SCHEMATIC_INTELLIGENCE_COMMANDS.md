# ESP32_CSI_WIFI_NODE Schematic Intelligence Commands

Status: `UNVERIFIED`
Date: `2026-05-10`
Project: `ESP32_CSI_WIFI_NODE`

## Commands Run

1. Prompt-counter increment:
   `python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply`
2. Routing / project context reads:
   `Get-Content START_HERE_FOR_AI_AGENTS.md`, `Get-Content README_GPT.md`, `Get-Content FOR CHAT GPT.MD`, `Get-Content 00_CODEX_START\TASK_ROUTER.md`, `Get-Content 00_CODEX_START\CURRENT_PROJECT.md`
3. Project memory and gate reads:
   `Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\PROJECT_MEMORY.md`
   `Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_TO_PCB_GATE_STATUS.md`
   `Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\schematic_quality\20260510_104847\*`
   `Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\footprint_package\20260510_115257\*`
4. Fresh saved-schematic netlist export:
   `kicad-cli sch export netlist --format kicadxml --output %TEMP%\esp32_schematic_netlist.xml 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`
5. Generator syntax check:
   `python -m py_compile 03_TOOLS\scripts\project_intelligence\build_project_schematic_intelligence.py`
6. Generator run:
   `python 03_TOOLS\scripts\project_intelligence\build_project_schematic_intelligence.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE`
7. Final no-design-change checks:
   `git diff --name-only -- *.kicad_sch *.kicad_pcb *.kicad_pro`
   `git diff --cached --name-only -- *.kicad_sch *.kicad_pcb *.kicad_pro`
   `git status --short --untracked-files=no -- *.kicad_sch *.kicad_pcb *.kicad_pro`

## Notable Failure

- An earlier attempt to generate the full intelligence layer through one very large inline PowerShell/Python command failed with Windows error `The filename or extension is too long.` That failed approach was replaced by the reusable generator script in `03_TOOLS/scripts/project_intelligence/build_project_schematic_intelligence.py`.
