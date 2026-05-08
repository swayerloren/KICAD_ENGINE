# 03_TOOLS Index

## Purpose

`03_TOOLS/` contains scripts, wrappers, and tool-support assets. Some tools are read-only, some update reports and memory, and some can edit project files when explicitly used for real PCB work.

GitHub note: `03_TOOLS/node_envs`, `03_TOOLS/python_envs`, `03_TOOLS/repos`, and `03_TOOLS/tool_logs` are intentionally local-only working folders. Git tracks placeholder `README.md` files there, not the real local environments, clones, or logs.

Portability note: a new user should be able to open this repo in VS Code, read the included startup docs, and use the included scripts without first cloning extra helper repos or restoring someone else's private env folders.

## Project State Tools

| Tool | Run | Effect |
|---|---|---|
| `build_live_project_state.py` | `python 03_TOOLS/scripts/project_state/build_live_project_state.py --project <ACTIVE_PROJECT_PATH> --apply` | reads live KiCad files, writes live-state reports |
| `detect_stale_reports.py` | `python 03_TOOLS/scripts/project_state/detect_stale_reports.py --project <ACTIVE_PROJECT_PATH> --apply` | detects stale/contradictory reports |
| `reconcile_project_gates.py` | `python 03_TOOLS/scripts/project_state/reconcile_project_gates.py --project <ACTIVE_PROJECT_PATH> --apply` | updates gate narratives from live evidence |
| `update_phase_status_from_live_state.py` | `python 03_TOOLS/scripts/project_state/update_phase_status_from_live_state.py --project <ACTIVE_PROJECT_PATH> --apply` | writes phase status summary from live state |

Safety: read live files and write report/state files. They do not edit KiCad design geometry.

## Maintenance Tools

| Tool | Run | Effect |
|---|---|---|
| `run_maintenance_cycle.py` | `python 03_TOOLS/scripts/maintenance/run_maintenance_cycle.py --project <ACTIVE_PROJECT_PATH>` | runs canonical maintenance cycle |
| `prompt_counter.py` | `python 03_TOOLS/scripts/maintenance/prompt_counter.py --project <ACTIVE_PROJECT_PATH> show` | reads or updates prompt counter |
| `check_maintenance_due.py` | `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project <ACTIVE_PROJECT_PATH>` | reports maintenance-due state |
| `run_memory_maintenance.py` | `python 03_TOOLS/scripts/memory_maintenance/run_memory_maintenance.py --project <ACTIVE_PROJECT_PATH> --apply` | legacy-compatible memory/history maintenance |

Safety: updates memory/history/status files; does not edit KiCad design files.

## Project Gate Tools

| Tool | Run | Effect |
|---|---|---|
| `check_phase_allowed.py` | `python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project <ACTIVE_PROJECT_PATH> --phase <PHASE>` | read-only phase decision using live state plus fresh/stale report handling |
| `run_project_gate.py` | `python 03_TOOLS/scripts/project_gate/run_project_gate.py --project <PROJECT_PATH>` | aggregates project gate evidence |

Safety: read-only on design files; writes gate output files.

## PCB Routing Tools

Representative scripts:

- `esp32_csi_power_batch_02_reroute.py`
- `esp32_csi_usb_control_batch_03.py`
- `esp32_csi_control_batch_04.py`
- `esp32_csi_usb_data_batch_05.py`
- `esp32_csi_full_route_pass.py`

Effect: these are project-specific and may edit copied boards or live `.kicad_pcb` files when intentionally run for routing work.

Safety level: `EDITS_KICAD_PCB_WHEN_APPLIED`

## Layout Automation Tools

| Tool | Run | Effect |
|---|---|---|
| `score_routing_feasibility.py` | `python 03_TOOLS/scripts/routing_feasibility/score_routing_feasibility.py ...` | routing feasibility scoring |
| `run_freerouting_dry_run.py` | `python 03_TOOLS/scripts/routing_feasibility/run_freerouting_dry_run.py ...` | dry-run routing feasibility |
| `parse_unrouted_and_vias.py` | `python 03_TOOLS/scripts/routing_feasibility/parse_unrouted_and_vias.py ...` | parses route-result evidence |

Safety: typically read-only or copied-board-only, depending on invocation.

## GitHub And Release Tools

| Tool | Run | Effect |
|---|---|---|
| `build_repo_index.py` | `python 03_TOOLS/scripts/indexing/build_repo_index.py` | builds repo-level index outputs |
| `build_memory_index.py` | `python 03_TOOLS/scripts/indexing/build_memory_index.py` | rebuilds memory indexes |
| `build_history_index.py` | `python 03_TOOLS/scripts/indexing/build_history_index.py` | rebuilds history indexes |
| `build_ai_quality_index.py` | `python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py` | rebuilds AI-quality indexes |
| `build_current_known_problems.py` | `python 03_TOOLS/scripts/ai_quality/build_current_known_problems.py` | rebuilds known-problems summary |

Safety: documentation/index generation only.

## Schematic And Validation Tools

- `03_TOOLS/scripts/kicad_schematic_checks/`
- `03_TOOLS/scripts/project_validation/`
- `03_TOOLS/scripts/run_erc.ps1`
- `03_TOOLS/scripts/run_drc.ps1`

Most are read-only validators and report generators.
