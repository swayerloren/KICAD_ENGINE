# Workflows Index

## Startup Workflow

- Human start: [START_HERE.md](START_HERE.md)
- AI start: [00_CODEX_START/START_HERE.md](00_CODEX_START/START_HERE.md)
- Safety and startup rules: `AGENTS.md`, `README_GPT.md`, `FOR CHAT GPT.MD`

## Maintenance Workflow

- Main supervisor: `python 03_TOOLS/scripts/maintenance/run_maintenance_cycle.py --project <ACTIVE_PROJECT_PATH>`
- Prompt counter rules: `00_CODEX_START/PROMPT_COUNTER_RULES.md`
- Legacy maintenance compatibility: `03_TOOLS/scripts/memory_maintenance/`

## Live Project State Workflow

- run `python 03_TOOLS/scripts/project_state/build_live_project_state.py --project <ACTIVE_PROJECT_PATH> --apply`
- confirm `reports/LIVE_PROJECT_STATE.json` and `.md` refreshed
- use `memory/CURRENT_PROJECT_STATE.md` for the project-facing summary

## Stale-Report Reconciliation Workflow

- run `python 03_TOOLS/scripts/project_state/detect_stale_reports.py --project <ACTIVE_PROJECT_PATH> --apply`
- run `python 03_TOOLS/scripts/project_state/reconcile_project_gates.py --project <ACTIVE_PROJECT_PATH> --apply`
- confirm stale `NO_PCB` or `0 footprints` narratives are not overriding live evidence

## KiCad Schematic Workflow

- Read startup and safety files first
- Use `03_TOOLS/scripts/kicad_schematic_checks/`
- Review project reports under `reports/`
- Run or review ERC before downstream PCB phases

## KiCad PCB Placement Workflow

- Phase gating: `python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project <ACTIVE_PROJECT_PATH> --phase <PHASE>`
- Live state build: `python 03_TOOLS/scripts/project_state/build_live_project_state.py --project <ACTIVE_PROJECT_PATH> --apply`
- Read `34_PCB_LAYOUT_SANDBOX/` planning rules first
- Require sandbox variant evidence before real board edits
- Use project reports plus human visual review

## KiCad PCB Routing Workflow

- Read `14_LAYOUT_AUTOMATION/REAL_PROJECT_ROUTING_WORKFLOW.md`
- Read `14_LAYOUT_AUTOMATION/REAL_PROJECT_ROUTING_STOP_CONDITIONS.md`
- Rehearse on copied boards first
- Apply only proven clean geometry to the live board

## Trace-By-Trace Audit Workflow

- inspect routed nets against `14_LAYOUT_AUTOMATION/TRACE_BY_TRACE_VERIFICATION_RULES.md`
- repair only clearly bad traces
- preserve `0` DRC violations
- regenerate visual review evidence after any accepted repair

## PCB Final Review Workflow

- Run DRC
- inspect unconnected items
- export visual review package
- complete LJ/human checklist
- do not claim fabrication-ready while blockers remain

## GitHub Push Workflow

- See [05_OUTPUTS/release_readiness/GITHUB_PUSH_PLAN.md](05_OUTPUTS/release_readiness/GITHUB_PUSH_PLAN.md)
- verify `.gitignore`
- scan for secrets and lock files
- stage safe files only
- commit intentionally
- push to `origin main`

## Public Release Workflow

- See [PUBLIC_RELEASE_STATUS.md](PUBLIC_RELEASE_STATUS.md)
- close checklist gaps in [PUBLIC_RELEASE_CHECKLIST.md](PUBLIC_RELEASE_CHECKLIST.md)
- complete license review in [21_LICENSE_ATTRIBUTION/LICENSE_AUDIT.md](21_LICENSE_ATTRIBUTION/LICENSE_AUDIT.md)
- clean placeholder-token references and excluded-content assumptions before switching visibility
