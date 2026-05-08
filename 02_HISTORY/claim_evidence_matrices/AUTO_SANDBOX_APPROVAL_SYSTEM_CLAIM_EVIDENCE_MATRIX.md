# Claim / Evidence Matrix - Auto Sandbox Approval System

Date: `2026-05-07`

| Claim | Evidence |
| --- | --- |
| Generic LJ approval is no longer the required sandbox gate | `34_PCB_LAYOUT_SANDBOX/AUTO_SANDBOX_APPROVAL_RULES.md`, `AGENTS.md`, `00_CODEX_START/START_HERE.md` |
| Sandbox auto-approval uses explicit status codes | `34_PCB_LAYOUT_SANDBOX/AUTO_APPROVAL_STATUS_CODES.md` |
| Real PCB work may proceed only when sandbox auto status is `AUTO_APPROVED_FOR_PCB_WORK` | `34_PCB_LAYOUT_SANDBOX/PCB_WORK_AUTO_START_RULES.md`, `09_ACCURACY_ENGINE/workflows/CREATE_PCB_WORKFLOW.md` |
| `ESP32_CSI_WIFI_NODE` remains blocked | `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md`, `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/layout_sandbox/AUTO_BLOCKED_LAYOUT_PLAN_REPORT.md` |
| The active project's primary sandbox auto-block reason is upstream precheck failure, with high-risk footprint verification still listed as a concrete blocker | `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`, `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/FOOTPRINT_PACKAGE_GATE_REPORT.md`, `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md` |
