# AUTO APPROVAL REPORT TEMPLATE

Project: `PROJECT_NAME`

Date: `YYYY-MM-DD`

Gate result: `PASS`

Auto approval status: `AUTO_APPROVED_FOR_PCB_WORK`

Selected variant: `VARIANT_ID`

## Preconditions

| Check | Status | Evidence | Notes |
| --- | --- | --- | --- |
| schematic gate is `PASS` | `PASS` | `...` | `...` |
| ERC is `PASS` | `PASS` | `...` | `...` |
| KiCad-native annotation verified | `PASS` | `...` | `...` |
| all physical footprints assigned | `PASS` | `...` | `...` |
| high-risk footprints exact-verified or safe-candidate documented | `PASS` | `...` | `...` |
| connector orientation known | `PASS` | `...` | `...` |
| board shape and dimensions defined | `PASS` | `...` | `...` |
| antenna keepout defined if RF exists | `PASS` | `...` | `...` |
| at least 3 variants exist | `PASS` | `...` | `...` |
| variant scorecard exists | `PASS` | `...` | `...` |
| selected variant has no hard fails | `PASS` | `...` | `...` |
| routing-feasibility check passes | `PASS` | `...` | `...` |
| no DRC/precheck blocker exists | `PASS` | `...` | `...` |
| auto approval report exists | `PASS` | `this file` | `...` |

## Decision

- Selected variant score: `...`
- Selected variant risk: `...`
- Ready for real PCB work: `YES`

## Allowed Next Actions

- update PCB from schematic if needed
- perform real PCB placement
- begin later PCB phases only when their own gates pass

