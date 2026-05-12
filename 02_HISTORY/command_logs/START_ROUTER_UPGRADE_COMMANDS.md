# Start Router Upgrade Commands

Date: `2026-05-10`

## Commands Run

1. Read startup and handoff docs with `Get-Content -Raw`:
   - `START_HERE_FOR_AI_AGENTS.md`
   - `AGENTS.md`
   - `README_GPT.md`
   - `FOR CHAT GPT.MD`
   - selected `00_CODEX_START/*` structure, workflow, closeout, prompt-counter,
     and current-project files
   - `.prompts/README.md`
   - `.prompts/codex/00_START_SESSION.md`
   - `.prompts/claude/00_START_SESSION.md`

2. Searched repo structure and route targets with `rg` and `Get-ChildItem`:
   - `00_CODEX_START`
   - `09_ACCURACY_ENGINE/schematic_rules`
   - `09_ACCURACY_ENGINE/pcb_rules`
   - `14_LAYOUT_AUTOMATION`
   - `24_FAB_PROFILES`
   - `17_RELEASE_BUILD`
   - `08_COMPONENT_DATABASE`
   - `11_LIBRARY_FACTORY`
   - `29_FOOTPRINT_GAP_ANALYSIS`
   - active-project `pcb_intelligence`

3. Checked prompt counter and maintenance status:
   - `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - `python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply`
   - `python 03_TOOLS/scripts/maintenance/run_maintenance_cycle.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
   - rechecked the prompt counter after maintenance

4. Validated router coverage:
   - `rg -n "TASK_ROUTER\.md" START_HERE_FOR_AI_AGENTS.md`
   - PowerShell route-coverage loop over:
     - `00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md`
     - `00_CODEX_START/TASK_TYPE_TO_ALLOWED_ACTIONS.md`
     - `00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md`
     - `00_CODEX_START/TASK_TYPE_TO_OUTPUTS.md`

5. Checked KiCad design-file safety:
   - `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb'`
   - `git status --short`

## Result

All validation commands completed without showing `.kicad_sch` or `.kicad_pcb`
changes for this task.
