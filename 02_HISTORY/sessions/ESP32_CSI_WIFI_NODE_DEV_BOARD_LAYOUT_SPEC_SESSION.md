# ESP32_CSI_WIFI_NODE Dev-Board Layout Spec Session

Date: 2026-05-07

Workspace: `C:/Users/LJ/GitHub/KICAD_ENGINE`

Active project: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`

Task: Reject current PCB placement and create a new ESP32/STM32 pill-style dev-board layout specification. Do not edit PCB.

## Startup / Read Evidence

- Read `AGENTS.md`.
- Read `README_GPT.md`.
- Read `FOR CHAT GPT.MD`.
- Read `09_ACCURACY_ENGINE/workflows/MANDATORY_KICAD_PHASE_GATE.md`.
- Read `09_ACCURACY_ENGINE/verification_rules/NO_PHASE_SKIPPING_RULES.md`.
- Read `reports/PCB_CREATE_FROM_SCHEMATIC_REPORT.md`.
- Read `reports/PCB_SYNC_STATUS.md`.
- Read `reports/PCB_INITIAL_DRC_REPORT.md`.
- Checked optional `PCB_PLACEMENT_REAL_LAYOUT_REPORT.md`: missing.
- Checked optional `PCB_PLACEMENT_DRC_REPORT.md`: missing; used `PCB_PLACEMENT_DRC_REPORT.rpt`.
- Read current `PCB_PLACEMENT_STRICT_AUDIT.md`.

## Phase Gate Check

Read-only phase checker was run for phases 3, 4, and 5. It reported `BLOCKED` because the checker was not supplied LJ approval/native evidence flags in this documentation-only run.

No PCB phase was advanced. This session produced only rejection/specification reports.

## PCB File Inspection

Read-only KiCad Python inspection was used to check footprint sizes from the current PCB:

- `U2` current footprint: `RF_Module:ESP32-S3-WROOM-1`, current bbox approximately `48.05 x 41.25 mm`.
- `J1` current footprint: `Connector_BarrelJack:BarrelJack_CUI_PJ-102AH_Horizontal`, current bbox approximately `11.55 x 16.05 mm`.
- `J2` current footprint: `Connector_USB:USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal`, current bbox approximately `10.69 x 8.99 mm`.

## Outputs

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/CURRENT_PCB_PLACEMENT_REJECTION_REPORT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_DEV_BOARD_LAYOUT_OPTIONS.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_SELECTED_DEV_BOARD_LAYOUT_SPEC.md`

## Result

Current placement classification is superseded by:

`PLACEMENT_REJECTED_NOT_PRODUCTION_SUITABLE`

Selected next layout spec:

`Option A - 38 mm x 80 mm pill board with side barrel jack compromise`

PCB reset/replacement placement may begin only after LJ approves the selected spec. Routing remains blocked.
