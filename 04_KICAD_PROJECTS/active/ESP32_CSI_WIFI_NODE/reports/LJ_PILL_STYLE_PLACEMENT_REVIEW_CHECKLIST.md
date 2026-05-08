# LJ Pill-Style Placement Review Checklist

Project: `ESP32_CSI_WIFI_NODE`

Date: 2026-05-07

Current classification: `BLOCKED_BY_MECHANICAL_OR_FOOTPRINT_RISK`

Routing allowed: `NO`

## Required LJ Decisions

| Decision | Options | LJ selection |
|---|---|---|
| Board format | Keep `38 x 80 mm` pill board / switch to `45 x 80 mm` wider board / choose another size | `[ ]` |
| Barrel jack | Keep side-mounted J1 / replace with smaller connector / DNP/remove barrel input | `[ ]` |
| Mounting holes | Use 2 holes / use shifted 4 holes / widen board for true 4 holes | `[ ]` |
| ESP32 footprint | Accept current footprint/keepout / replace with verified WROOM-1U footprint / widen board | `[ ]` |
| U2 drill issue | Accept 0.20 mm holes with fab proof / modify rule / modify footprint | `[ ]` |
| USB-C edge | Accept current overhang / adjust connector placement / verify exact footprint edge line | `[ ]` |
| USB test pads | Keep D+/D- test pads / move them / DNP/remove USB data test pads | `[ ]` |

## Visual Review Items

| Item | Current audit status | LJ status |
|---|---:|---|
| Pill-board silhouette | `PARTIAL_PASS` | `[ ] ACCEPT / [ ] REJECT` |
| Dead area removed | `PASS` | `[ ] ACCEPT / [ ] REJECT` |
| U2 top/RF orientation | `PASS_WITH_RISK` | `[ ] ACCEPT / [ ] REJECT` |
| USB-C bottom placement | `PASS_FOR_REVIEW` | `[ ] ACCEPT / [ ] REJECT` |
| Barrel jack side placement | `FAIL` | `[ ] ACCEPT / [ ] REJECT` |
| Mounting-hole strategy | `FAIL` | `[ ] ACCEPT / [ ] REJECT` |
| Button accessibility | `PARTIAL_PASS` | `[ ] ACCEPT / [ ] REJECT` |
| LED visibility | `PASS_FOR_REVIEW` | `[ ] ACCEPT / [ ] REJECT` |
| Test-pad row | `PARTIAL_PASS` | `[ ] ACCEPT / [ ] REJECT` |
| Power cluster compactness | `PASS_WITH_RISK` | `[ ] ACCEPT / [ ] REJECT` |
| Buck loop compactness | `PASS_WITH_RISK` | `[ ] ACCEPT / [ ] REJECT` |
| USB cluster compactness | `PASS_WITH_RISK` | `[ ] ACCEPT / [ ] REJECT` |
| Reference/silkscreen readability | `FAIL_FOR_ROUTING` | `[ ] ACCEPT / [ ] REJECT` |

## Routing Gate

Routing may not begin until:

- `[ ]` LJ chooses a barrel/input strategy.
- `[ ]` LJ chooses a mounting-hole strategy.
- `[ ]` U2 footprint/keepout risk is resolved or explicitly accepted.
- `[ ]` Courtyard/clearance blockers are repaired in a new placement pass.
- `[ ]` LJ explicitly approves routing after a repaired placement audit.

Current routing decision: `BLOCKED`

## 2026-05-07 Placement Repair Attempt Status

Repair applied: `NO`

Reason:

- Mandatory phase gate blocked Phase 5 component placement repair.
- `SCHEMATIC_TO_PCB_GATE_STATUS.md` still says `Gate result: FAIL`.
- `PCB_SYNC_STATUS.md` says `PCB_SYNCED`, so the project evidence needs cleanup before more PCB placement edits.

Updated LJ decision needed:

- `[ ]` Confirm whether `SCHEMATIC_TO_PCB_GATE_STATUS.md` should be repaired to match the later PCB sync/Q1 repair evidence, or approve a logged exception for placement repair.

Routing remains: `NO`
