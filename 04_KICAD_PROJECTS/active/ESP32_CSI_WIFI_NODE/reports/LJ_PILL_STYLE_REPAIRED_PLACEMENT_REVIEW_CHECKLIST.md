# LJ Pill-Style Repaired Placement Review Checklist

Project: `ESP32_CSI_WIFI_NODE`

Date: 2026-05-07

Current audit classification: `BLOCKED_BY_MECHANICAL_OR_FOOTPRINT_RISK`

Routing allowed: `NO`

## Review Status

Repaired placement exists: `NO`

The previous placement repair task was blocked by the phase gate and did not edit the PCB. The latest available visuals are still the unrepaired 38 mm x 80 mm pill-style placement.

## LJ Decisions Required Before Another Repair Pass

| Decision | Required LJ action |
|---|---|
| Phase-gate inconsistency | Decide whether to repair `SCHEMATIC_TO_PCB_GATE_STATUS.md` to match later PCB sync evidence, or approve a logged exception for placement repair. |
| Board size | Choose whether to keep `38 x 80 mm`, move to a modest wider board such as `42 x 85 mm`, or choose a different compact pill size. |
| Barrel jack `J1` | Accept lower-left side barrel jack, replace with smaller input connector in a future schematic revision, or allow a wider board. |
| USB-C `J2` | Confirm exact bottom-edge placement/overhang and footprint edge-line interpretation. |
| Test pads | Approve moving `TP1-TP9` to a clean side service row away from USB-C and USB support parts. |
| Mounting holes | Choose two-hole compact strategy, shifted four-hole strategy, or wider board for true corner holes. |
| `U2` footprint/keepout | Confirm current ESP32 footprint/keepout is acceptable, or require verified WROOM-1U footprint replacement. |
| `U2` drill issue | Confirm fabrication capability/rule exception or require footprint/rule repair. |
| Silkscreen policy | Approve hiding values and moving only useful reference labels away from pads/holes/connectors. |

## Visual Checklist

| Item | Current status | LJ status |
|---|---:|---|
| Pill-board silhouette | `PASS` | `[ ] ACCEPT / [ ] REJECT` |
| U2 top/RF orientation | `PASS_WITH_RISK` | `[ ] ACCEPT / [ ] REJECT` |
| Antenna keepout free | `PASS_WITH_RISK` | `[ ] ACCEPT / [ ] REJECT` |
| USB-C bottom placement | `PARTIAL_PASS_REQUIRES_REPAIR` | `[ ] ACCEPT / [ ] REJECT` |
| Barrel jack placement | `FAIL_REQUIRES_LJ_DECISION` | `[ ] ACCEPT / [ ] REJECT` |
| Test pad row | `FAIL` | `[ ] ACCEPT / [ ] REJECT` |
| USB support not mixed with pads | `FAIL` | `[ ] ACCEPT / [ ] REJECT` |
| LED/resistor readability | `PARTIAL_FAIL` | `[ ] ACCEPT / [ ] REJECT` |
| Button accessibility | `PARTIAL_PASS_WITH_MECHANICAL_RISK` | `[ ] ACCEPT / [ ] REJECT` |
| Mounting-hole clearance | `FAIL_REQUIRES_LJ_DECISION` | `[ ] ACCEPT / [ ] REJECT` |
| Buck cluster compact | `PASS_WITH_DENSITY_RISK` | `[ ] ACCEPT / [ ] REJECT` |
| USB cluster compact | `PASS_WITH_LAYOUT_RISK` | `[ ] ACCEPT / [ ] REJECT` |
| Silkscreen clear of pads/holes | `FAIL` | `[ ] ACCEPT / [ ] REJECT` |

## Routing Gate

Routing may begin only after:

- `[ ]` a real repaired placement is applied,
- `[ ]` DRC after repair is reviewed,
- `[ ]` remaining mechanical/footprint risks are resolved or explicitly accepted,
- `[ ]` LJ visually approves the repaired placement.

Current routing decision: `BLOCKED`
