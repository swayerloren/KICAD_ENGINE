# ESP32_CSI_WIFI_NODE Routing Work Prep Commands

Date: `2026-05-08`

## Commands And Results

1. `python 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py --project C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE`
   - result: prompt count `4`, maintenance due `NO`

2. PowerShell file-identity checks on `kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`
   - result: target PCB exists, timestamp `2026-05-08 08:59:46 -04:00`, SHA256 `5E6486A2C188B68207C9FF4692618AE81BF322355ACAEE686146EF075330C2F6`

3. Backup and routing-work folder creation under:
   - `99_BACKUPS\pre_codex_edits\20260508_091428_ESP32_CSI_WIFI_NODE_routing_work_prep`
   - `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\routing_work\20260508_091428`
   - result: snapshot copies of `.kicad_pcb` and `.kicad_pro` created

4. `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe pcb drc --format json --severity-all --units mm --output <routing_work>\CURRENT_DRC_BASELINE.json <target pcb>`
   - result: DRC baseline JSON created

5. KiCad Python baseline extraction runs for placement, net status, net/ratsnest grouping, and raw trace snapshot
   - result: `CURRENT_COMPONENT_PLACEMENT_LIST.csv`, `CURRENT_NET_STATUS.csv`, `CURRENT_NET_RATSNEST_BASELINE.md`, and `CURRENT_TRACE_LIST.txt` created

6. `python 03_TOOLS\scripts\project_gate\check_phase_allowed.py --project C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --phase 8`
   - result: blocked by live evidence only, with stale routing-history reports explicitly ignored

7. Session-owned orphan KiCad Python processes from timed-out extraction attempts were stopped and the zero-byte trace CSV stub was removed
   - result: routing-work folder cleaned back to authoritative artifacts only

8. `python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --reason "routing work prep" --apply`
   - result: prompt counter `4 -> 5`, maintenance due `YES`

9. `python 03_TOOLS\scripts\maintenance\run_maintenance_cycle.py --project C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE`
   - result: maintenance `APPLY` completed, prompt counter reset to `0`, live classification remained `PCB_EXISTS_PARTIAL_ROUTING_EXISTS_NEEDS_AUDIT`
