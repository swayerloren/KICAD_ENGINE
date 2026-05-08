# Tools Index

This is the GitHub-facing tool catalog. The deeper script inventory lives in [03_TOOLS/TOOLS_INDEX.md](03_TOOLS/TOOLS_INDEX.md).

## Maintenance Tools

| Tool | Command Example | Effect | Safety |
|---|---|---|---|
| maintenance cycle | `python 03_TOOLS/scripts/maintenance/run_maintenance_cycle.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE` | rebuilds live state, stale-report audit, gates, memory/history indexes, and maintenance report | writes docs/state files, does not edit KiCad design geometry |
| maintenance due check | `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE` | checks prompt counter and maintenance threshold | read-only |
| prompt counter increment | `python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply` | increments project prompt counter | writes project memory only |

## Project State Tools

| Tool | Command Example | Effect | Safety |
|---|---|---|---|
| build live project state | `python 03_TOOLS/scripts/project_state/build_live_project_state.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply` | reads live KiCad files and writes live-state reports | writes reports/state only |
| detect stale reports | `python 03_TOOLS/scripts/project_state/detect_stale_reports.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply` | classifies stale/contradictory reports | writes audit docs only |
| reconcile project gates | `python 03_TOOLS/scripts/project_state/reconcile_project_gates.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply` | updates gate narratives from live evidence | writes gate reports only |
| update phase status | `python 03_TOOLS/scripts/project_state/update_phase_status_from_live_state.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply` | writes phase summary from live state | writes docs/state only |

## Project Gate Tools

| Tool | Command Example | Effect | Safety |
|---|---|---|---|
| phase gate check | `python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --phase 8` | checks a phase against live evidence plus stale-report handling | read-only on design files |
| aggregate project gate | `python 03_TOOLS/scripts/project_gate/run_project_gate.py --project 19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board` | builds project gate summary from existing evidence | read-only on design files |

## PCB Routing Tools

| Tool Area | Representative Files | Effect | Safety |
|---|---|---|---|
| project-specific routing helpers | `03_TOOLS/scripts/pcb_routing/esp32_csi_power_batch_02_reroute.py`, `esp32_csi_usb_control_batch_03.py`, `esp32_csi_control_batch_04.py`, `esp32_csi_usb_data_batch_05.py` | copied-board rehearsal or live-board routing edits when intentionally applied | may edit `.kicad_pcb` files |
| board inspection | `03_TOOLS/scripts/pcb_routing/esp32_csi_inspect_board.py` | inspects board/routing state | usually read-only |

## Layout Automation Tools

| Tool | Command Example | Effect | Safety |
|---|---|---|---|
| routing feasibility scorer | `python 03_TOOLS/scripts/routing_feasibility/score_routing_feasibility.py ...` | scores routing feasibility inputs | read-only |
| FreeRouting dry run | `python 03_TOOLS/scripts/routing_feasibility/run_freerouting_dry_run.py ...` | dry-run route feasibility review | copied-board/review workflow only |
| unrouted/via parser | `python 03_TOOLS/scripts/routing_feasibility/parse_unrouted_and_vias.py ...` | parses route outputs | read-only |

## GitHub And Release Tools

| Tool | Command Example | Effect | Safety |
|---|---|---|---|
| memory index rebuild | `python 03_TOOLS/scripts/memory_history/build_memory_index.py` | rebuilds memory indexes | writes index docs only |
| history index rebuild | `python 03_TOOLS/scripts/memory_history/build_history_index.py` | rebuilds history indexes | writes index docs only |
| AI quality index rebuild | `python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py` | rebuilds AI-quality indexes | writes index docs only |
| known problems rebuild | `python 03_TOOLS/scripts/ai_quality/build_current_known_problems.py` | rebuilds current-problems summary | writes docs only |

## Where To Look Next

- Detailed tool catalog: [03_TOOLS/TOOLS_INDEX.md](03_TOOLS/TOOLS_INDEX.md)
- Workflow usage: [WORKFLOWS_INDEX.md](WORKFLOWS_INDEX.md)
- Repo structure: [REPO_INDEX.md](REPO_INDEX.md)
