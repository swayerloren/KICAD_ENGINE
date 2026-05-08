# AUTO BLOCKED REPORT TEMPLATE

Project: `PROJECT_NAME`

Date: `YYYY-MM-DD`

Gate result: `BLOCKED`

Auto approval status: `AUTO_BLOCKED_MISSING_DATA`

Selected variant: `VARIANT_ID`

## Failed Or Missing Preconditions

| Check | Status | Evidence | Exact problem |
| --- | --- | --- | --- |
| schematic gate is `PASS` | `FAIL` | `...` | `...` |
| ERC is `PASS` | `PASS` | `...` | `...` |
| KiCad-native annotation verified | `PASS` | `...` | `...` |
| all physical footprints assigned | `FAIL` | `...` | `...` |
| high-risk footprints exact-verified or safe-candidate documented | `FAIL` | `...` | `...` |
| connector orientation known | `FAIL` | `...` | `...` |
| board shape and dimensions defined | `FAIL` | `...` | `...` |
| antenna keepout defined if RF exists | `PASS` | `...` | `...` |
| at least 3 variants exist | `PASS` | `...` | `...` |
| variant scorecard exists | `PASS` | `...` | `...` |
| selected variant has no hard fails | `PASS` | `...` | `...` |
| routing-feasibility check passes | `FAIL` | `...` | `...` |
| no DRC/precheck blocker exists | `FAIL` | `...` | `...` |
| auto approval report exists | `PASS` | `this file` | `...` |

## Exact Missing Items

1. `...`
2. `...`
3. `...`

## Blocked Actions

- do not update the real PCB from schematic
- do not place parts on the real PCB
- do not route the real PCB

## Next Objective Actions

1. `...`
2. `...`
3. `...`

