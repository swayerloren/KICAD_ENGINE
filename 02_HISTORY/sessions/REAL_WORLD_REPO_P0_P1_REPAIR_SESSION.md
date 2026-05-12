# REAL_WORLD_REPO_P0_P1_REPAIR_SESSION

Date: `2026-05-12`
Task type: `DOCS_ONLY`
Final classification: `P0_P1_PARTIAL_REPAIR_NEEDS_HUMAN_DECISION`

## Scope

Repair only the safe P0/P1 issues from the real-world repo audit without
editing KiCad design files, routing, or generating fabrication outputs.

## Preconditions

- repair-plan controller existed:
  `T_E_M_P/real_world_repo_audit/14_P0_P1_P2_REPAIR_PLAN.md`
- safe auto-fix classification present: `YES`

## Safe P0 / P1 Repairs Applied

- added explicit `GITHUB_PUSH_PUBLIC_RELEASE` route
- added explicit `KNOWLEDGE_RETRIEVAL` route
- aligned startup companion docs with the canonical route
- synchronized retrieval mirror maps with canonical startup maps
- removed the non-portable workspace folder entry
- replaced maintainer-only absolute-path examples in active GUI docs
- demoted historical structured-text annotation reports
- demoted stale PCB gate reports that can conflict with live-state authority
- rebuilt generated repo/memory/history/AI/current-known-problems indexes after retrieval-map changes

## Validation Highlights

- `python health_check.py --repo-root . --no-write` -> `PASS=18 WARN=2 FAIL=0`
- retrieval mirrors vs canonical maps -> `MATCH` for all three tables
- targeted active GUI docs/workspace -> no `C:\Users\LJ` path residue found
- staged files -> `0`
- no KiCad design files edited in this repair pass
- `knowledge_scrape` remains retired/historical only

## Remaining Open P0 / P1 Items

- `RWA-P0-001`
- `RWA-P0-002`
- `RWA-P1-003`
- `RWA-P1-005`
- `RWA-P1-006`
- `RWA-P1-009`

These remain because they require human release, payload, onboarding-default,
registry-contract, or demo-path decisions.

## Output Files

- `05_OUTPUTS/release_readiness/REAL_WORLD_REPO_P0_P1_REPAIR_REPORT.md`
- `05_OUTPUTS/release_readiness/REAL_WORLD_REPO_POST_REPAIR_VALIDATION.md`
- `02_HISTORY/sessions/REAL_WORLD_REPO_P0_P1_REPAIR_SESSION.md`
- `02_HISTORY/command_logs/REAL_WORLD_REPO_P0_P1_REPAIR_COMMANDS.md`
