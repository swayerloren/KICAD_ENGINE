# Real World Repo P0 / P1 Repair Report

Date: `2026-05-12`

Final classification: `P0_P1_PARTIAL_REPAIR_NEEDS_HUMAN_DECISION`

## Preconditions

- `T_E_M_P/real_world_repo_audit/14_P0_P1_P2_REPAIR_PLAN.md` exists: `YES`
- Safe auto-fix classification present: `YES`
- Repair scope stayed in docs/router/report/index/workspace lanes only: `YES`

## P0 Fixed

### `RWA-P0-003` AI startup safety / GitHub push routing

Status: `FIXED`

What changed:

- added first-class `GITHUB_PUSH_PUBLIC_RELEASE` routing to:
  - `START_HERE_FOR_AI_AGENTS.md`
  - `00_CODEX_START/TASK_ROUTER.md`
  - `00_CODEX_START/AI_AGENT_FAST_CONTEXT.md`
  - `00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md`
  - `00_CODEX_START/TASK_TYPE_TO_ALLOWED_ACTIONS.md`
  - `00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md`
  - `00_CODEX_START/TASK_TYPE_TO_OUTPUTS.md`
  - `00_CODEX_START/TASK_TYPE_TO_KNOWLEDGE_MAP.md`
  - `00_CODEX_START/TASK_TYPE_TO_TOOL_MAP.md`
  - `00_CODEX_START/TASK_TYPE_TO_RULE_MAP.md`
- the new route now forces GitHub/public-release work through:
  - `00_CODEX_START/GITHUB_NAVIGATION.md`
  - `00_CODEX_START/CURRENT_GITHUB_STATUS.md`
  - `PUBLIC_RELEASE_STATUS.md`
  - `PUBLIC_RELEASE_CHECKLIST.md`
  - `SECURITY.md`
  - `21_LICENSE_ATTRIBUTION/LICENSE_AUDIT.md`
  - `21_LICENSE_ATTRIBUTION/THIRD_PARTY_ATTRIBUTION.md`
  - `21_LICENSE_ATTRIBUTION/PUBLIC_REPO_RISK_REGISTER.md`

### Carried-forward P0 mitigation

Not changed in this pass, but preserved:

- `SEC-P0-001` prior `.gitignore` safety patch remains intact

## P1 Fixed

### `RWA-P1-001` AI startup path consistency

Status: `FIXED`

What changed:

- aligned startup surfaces so the canonical chain is explicit in:
  - `START_HERE_FOR_AI_AGENTS.md`
  - `README_GPT.md`
  - `FOR CHAT GPT.MD`
  - `CLAUDE.md`
  - `00_CODEX_START/AI_AGENT_FAST_CONTEXT.md`
  - `00_CODEX_START/TASK_ROUTER.md`
- refreshed stale health-check references in `README_GPT.md` and `FOR CHAT GPT.MD`

### `RWA-P1-002` Knowledge routing

Status: `FIXED`

What changed:

- added first-class `KNOWLEDGE_RETRIEVAL` routing to the startup/router stack
- synchronized the retrieval mirrors with the canonical startup maps:
  - `10_KNOWLEDGE_BASE/retrieval_indexes/TASK_TO_KNOWLEDGE_MAP.md`
  - `10_KNOWLEDGE_BASE/retrieval_indexes/TASK_TO_TOOL_MAP.md`
  - `10_KNOWLEDGE_BASE/retrieval_indexes/TASK_TO_RULE_MAP.md`

### `RWA-P1-004` Path portability / workspace portability

Status: `FIXED`

What changed:

- removed the non-portable `../temp ai chat logs` folder from `KICAD_ENGINE_WORKSPACE.code-workspace`
- replaced maintainer-only absolute-path examples in active GUI docs with repo-relative PowerShell variable patterns:
  - `33_KICAD_GUI_AUTOMATION/README.md`
  - `33_KICAD_GUI_AUTOMATION/KICAD_NATIVE_ANNOTATION_WORKFLOW.md`
  - `33_KICAD_GUI_AUTOMATION/KICAD_AUTO_OPEN_PROJECT_WORKFLOW.md`
  - `33_KICAD_GUI_AUTOMATION/KICAD_ANNOTATION_DO_AND_DO_NOT.md`
  - `33_KICAD_GUI_AUTOMATION/examples/ESP32_CSI_WIFI_NODE_SAFE_DETECTION.md`

### `RWA-P1-007` Schematic annotation proof

Status: `FIXED`

What changed:

- demoted legacy structured-text annotation repair narratives to historical/non-authoritative status in:
  - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
  - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_REPORT.md`
  - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ANNOTATION_REPAIR_ROLLBACK_AND_FIX_PLAN.md`

### `RWA-P1-008` PCB live-state truth

Status: `FIXED`

What changed:

- added explicit historical/non-authoritative warnings so stale PCB gate reports cannot be mistaken for live-board truth:
  - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md`
  - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/TRACE_BY_TRACE_AUDIT.md`
  - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/THROUGH_HOLE_TEST_PAD_VIA_STRATEGY.md`
- those files now point readers to:
  - `reports/LIVE_PROJECT_STATE.md`
  - `reports/GATE_RECONCILIATION_REPORT.md`
  - `reports/STALE_REPORTS_AUDIT.md`

## P0 / P1 Remaining

These remain open by design because they require human release or product decisions:

### `RWA-P0-001`
- Area: `Public release / license / attribution`
- Status: `REMAINS_HUMAN_DECISION_BLOCKER`

### `RWA-P0-002`
- Area: `Public payload hygiene / retired migration residue`
- Status: `REMAINS_HUMAN_DECISION_BLOCKER`

### `RWA-P1-003`
- Area: `New-user project selection`
- Status: `REMAINS_HUMAN_DECISION_BLOCKER`

### `RWA-P1-005`
- Area: `Baseline ZIP payload size and hygiene`
- Status: `REMAINS_HUMAN_DECISION_BLOCKER`

### `RWA-P1-006`
- Area: `Knowledge source registry contract`
- Status: `REMAINS_HUMAN_DECISION_BLOCKER`

### `RWA-P1-009`
- Area: `End-to-end demo path`
- Status: `REMAINS_HUMAN_DECISION_BLOCKER`

## Files Changed

### Startup / router

- `START_HERE_FOR_AI_AGENTS.md`
- `CLAUDE.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `00_CODEX_START/AI_AGENT_FAST_CONTEXT.md`
- `00_CODEX_START/TASK_ROUTER.md`
- `00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md`
- `00_CODEX_START/TASK_TYPE_TO_ALLOWED_ACTIONS.md`
- `00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md`
- `00_CODEX_START/TASK_TYPE_TO_OUTPUTS.md`
- `00_CODEX_START/TASK_TYPE_TO_KNOWLEDGE_MAP.md`
- `00_CODEX_START/TASK_TYPE_TO_TOOL_MAP.md`
- `00_CODEX_START/TASK_TYPE_TO_RULE_MAP.md`

### Retrieval mirrors

- `10_KNOWLEDGE_BASE/retrieval_indexes/TASK_TO_KNOWLEDGE_MAP.md`
- `10_KNOWLEDGE_BASE/retrieval_indexes/TASK_TO_TOOL_MAP.md`
- `10_KNOWLEDGE_BASE/retrieval_indexes/TASK_TO_RULE_MAP.md`

### Portability / GUI docs

- `KICAD_ENGINE_WORKSPACE.code-workspace`
- `33_KICAD_GUI_AUTOMATION/README.md`
- `33_KICAD_GUI_AUTOMATION/KICAD_NATIVE_ANNOTATION_WORKFLOW.md`
- `33_KICAD_GUI_AUTOMATION/KICAD_AUTO_OPEN_PROJECT_WORKFLOW.md`
- `33_KICAD_GUI_AUTOMATION/KICAD_ANNOTATION_DO_AND_DO_NOT.md`
- `33_KICAD_GUI_AUTOMATION/examples/ESP32_CSI_WIFI_NODE_SAFE_DETECTION.md`

### Historical report demotions

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_REPORT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ANNOTATION_REPAIR_ROLLBACK_AND_FIX_PLAN.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/TRACE_BY_TRACE_AUDIT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/THROUGH_HOLE_TEST_PAD_VIA_STRATEGY.md`

### Rebuilt generated indexes after retrieval-map changes

- `00_CODEX_START/REPO_INDEX.generated.md`
- `00_CODEX_START/REPO_INDEX.generated.json`
- `00_CODEX_START/MEMORY_INDEX.generated.md`
- `00_CODEX_START/MEMORY_INDEX.generated.json`
- `00_CODEX_START/HISTORY_INDEX.generated.md`
- `00_CODEX_START/HISTORY_INDEX.generated.json`
- `00_CODEX_START/AI_QUALITY_INDEX.generated.md`
- `00_CODEX_START/AI_QUALITY_INDEX.generated.json`
- `00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md`

## Summary

Safe P0/P1 startup, routing, portability, and stale-report fixes are repaired.

The repo is not yet ready for a final all-clear because the remaining open P0/P1 items are the human-decision release, payload, onboarding-default, registry-contract, and demo-path blockers.
