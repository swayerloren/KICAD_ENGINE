# Tools Index

This is the GitHub-facing tool catalog for KiCad Engine.

It describes the main tool layers the repo provides for AI-assisted KiCad work. It is not only an index of scripts for `ESP32_CSI_WIFI_NODE`.

Use this file and the linked setup docs as the portable tool source of truth for normal repo use. `00_CODEX_START/TOOL_INDEX.md` is a machine-specific local inventory record, not a portable setup contract.

For the deeper portable internal catalog, see [03_TOOLS/TOOLS_INDEX.md](03_TOOLS/TOOLS_INDEX.md).

## Portable Setup Tools

| Tool | Command Example | Effect | Safety |
| --- | --- | --- | --- |
| repo health check | `python health_check.py --no-write` | checks repo shape, docs, Python, Git, KiCad discovery, and startup readiness | read-only |
| PowerShell health check | `powershell -ExecutionPolicy Bypass -File .\health_check.ps1 -NoWrite` | wrapper for the same health check | read-only |
| KiCad discovery | `python 03_TOOLS/scripts/kicad_discovery/find_kicad.py` | detects local KiCad install, `kicad-cli`, and `pcbnew` readiness | read-only |
| KiCad install validation | `python 03_TOOLS/scripts/kicad_discovery/validate_kicad_install.py` | gives a clear PASS/WARN/FAIL summary for local KiCad readiness | read-only |
| Python environment check | `python 03_TOOLS/scripts/python_env_check.py` | checks Python, pip, and optional module readiness | read-only |

## Task / Workflow Control Tools

| Tool | Command Example | Effect | Safety |
| --- | --- | --- | --- |
| task contract validation | `python 03_TOOLS/scripts/execution_contract/validate_task_contract.py --contract <TASK_CONTRACT.json>` | validates the declared task type and expected evidence | read-only |
| phase gate check | `python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project <ACTIVE_PROJECT_PATH> --phase <PHASE>` | checks whether the next project phase is allowed | read-only on design files |
| aggregate project gate | `python 03_TOOLS/scripts/project_gate/run_project_gate.py --project <PROJECT_PATH>` | summarizes current project gate status from existing evidence | read-only on design files |

## Project State Tools

| Tool | Command Example | Effect | Safety |
| --- | --- | --- | --- |
| build live project state | `python 03_TOOLS/scripts/project_state/build_live_project_state.py --project <ACTIVE_PROJECT_PATH> --apply` | reads live KiCad files and writes live-state summaries | writes reports/state only |
| detect stale reports | `python 03_TOOLS/scripts/project_state/detect_stale_reports.py --project <ACTIVE_PROJECT_PATH> --apply` | classifies stale or contradictory reports | writes audit docs only |
| reconcile project gates | `python 03_TOOLS/scripts/project_state/reconcile_project_gates.py --project <ACTIVE_PROJECT_PATH> --apply` | updates gate narratives from live evidence | writes gate reports only |

## Schematic And Validation Tools

| Tool Area | Command Example | Effect | Safety |
| --- | --- | --- | --- |
| schematic checks | `python 03_TOOLS/scripts/kicad_schematic_checks/<script>.py ...` | checks annotation, completeness, review markers, and related schematic issues | mostly read-only |
| project validation | `python 03_TOOLS/scripts/project_validation/validate_kicad_project.py <PROJECT_PATH>` | validates project structure, libraries, files, and tooling assumptions | report-writing only |
| ERC wrapper | `powershell -ExecutionPolicy Bypass -File .\03_TOOLS\scripts\run_erc.ps1 -ProjectPath <PROJECT_PATH>` | runs or structures ERC workflow | review/validation workflow |
| DRC wrapper | `powershell -ExecutionPolicy Bypass -File .\03_TOOLS\scripts\run_drc.ps1 -ProjectPath <PROJECT_PATH>` | runs or structures DRC workflow | review/validation workflow |

## Layout And Routing Tools

| Tool Area | Command Example | Effect | Safety |
| --- | --- | --- | --- |
| routing geometry checker | `python 14_LAYOUT_AUTOMATION/scripts/routing_geometry_quality.py <INPUT.json> <OUTPUT.json> --markdown <OUTPUT.md>` | hard-fails bad routing geometry | read-only on design files |
| routing feasibility | `python 03_TOOLS/scripts/routing_feasibility/score_routing_feasibility.py ...` | scores routing feasibility inputs | read-only |
| FreeRouting dry run | `python 03_TOOLS/scripts/routing_feasibility/run_freerouting_dry_run.py ...` | review-only route feasibility workflow | copied-board or review workflow only |
| placement readiness | `python 14_LAYOUT_AUTOMATION/scripts/score_placement_readiness.py <BOARD.kicad_pcb> <OUTPUT.json> --markdown <OUTPUT.md>` | scores placement readiness before routing | read-only board analysis |

Project-specific edit helpers may also exist under `03_TOOLS/scripts/pcb_routing/`, but those are examples of project-targeted helpers, not the identity of the repo.

## Maintenance And Indexing Tools

| Tool | Command Example | Effect | Safety |
| --- | --- | --- | --- |
| maintenance cycle | `python 03_TOOLS/scripts/maintenance/run_maintenance_cycle.py --project <ACTIVE_PROJECT_PATH>` | rebuilds live state, stale-report audit, gates, memory/history indexes, and maintenance records | writes docs/state only |
| repo index rebuild | `python 03_TOOLS/scripts/indexing/build_repo_index.py` | rebuilds repo indexes | writes index docs only |
| memory index rebuild | `python 03_TOOLS/scripts/indexing/build_memory_index.py` | rebuilds memory indexes | writes index docs only |
| history index rebuild | `python 03_TOOLS/scripts/indexing/build_history_index.py` | rebuilds history indexes | writes index docs only |
| AI quality index rebuild | `python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py` | rebuilds AI-quality indexes | writes index docs only |

## Where To Go Next

- Repo purpose and fast start: [README.md](README.md)
- Current repo/example-project status: [CURRENT_STATUS.md](CURRENT_STATUS.md)
- Project workspace layout: [PROJECTS_INDEX.md](PROJECTS_INDEX.md)
- Workflow catalog: [WORKFLOWS_INDEX.md](WORKFLOWS_INDEX.md)
