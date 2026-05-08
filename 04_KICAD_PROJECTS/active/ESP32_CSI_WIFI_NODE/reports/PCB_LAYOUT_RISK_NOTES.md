# PCB Layout Risk Notes

Project: ESP32_CSI_WIFI_NODE  
Date: 2026-05-07  
Phase: `PHASE_3_PLACEMENT_PLANNING`  
Scope: planning risks only. No PCB edits performed.

## Classification

`PLACEMENT_PLANNING_READY_WITH_REVIEW_RISKS`

Phase 3 planning is complete enough to proceed to Phase 4 mechanical setup. These risks must be reviewed before component placement is considered ready for LJ review.

## High-Risk Placement / Orientation Items

| Item | Risk | Placement impact | Required action |
|---|---|---|---|
| `J1` barrel jack | Footprint anchor may not equal jack mouth/edge | Center coordinate alone may misalign off-board opening | During mechanical setup, align actual connector opening to left board edge |
| `J2` USB-C | USB-C orientation and PCB-edge alignment are footprint-specific | Wrong rotation can put mouth inward or misalign board edge | Verify with footprint courtyard/fab layer before placement approval |
| `U2` ESP32 module | Value is `ESP32-S3-WROOM-1U`, footprint is `RF_Module:ESP32-S3-WROOM-1` | Antenna/U.FL/pigtail clearance may be wrong if footprint variant differs | Human review required before placement signoff |
| `U2` pad 41 | Initial DRC reports drill-size violations | Could affect fab capability and footprint validity | Review footprint/package before final mechanical placement |
| `Q1` AO3401A | Pin mapping is repaired, but physical SOT-23 orientation still matters | Wrong rotation can invert source/drain path in layout even with correct nets | Verify pad 1 marker and AO3401A package orientation during placement audit |
| `D3` TVS | Package/polarity still marked `NEEDS_REVIEW` | Wrong orientation can defeat protection or short rail | Verify exact TVS part/package/polarity before final placement |
| `U3` USB ESD | Pinout/orientation marked review | Wrong orientation can swap protected/connector sides | Verify package pinout before routing USB |
| `R5` USB shield link | Shield/GND policy unresolved | Placement near J2 is fine, but final connection strategy is not approved | Human decision before zones/routing |
| `TP8/TP9` USB test pads | USB D+/D- stubs | Can degrade signal integrity, even at full speed if long or poorly placed | Keep optional, document stub length, or remove/move during later review |

## Board / Mechanical Risks

| Risk | Detail | Mitigation |
|---|---|---|
| Mounting-hole clearance | Bottom test row starts at `x=25`, safely away from bottom holes, but connector bodies need courtyard verification | Use `r=4.35 mm` no-copper/component keepout around each hole |
| Barrel jack overhang | J1 horizontal body may extend outside board | Allow overhang only if footprint/mechanical drawing supports it |
| USB-C cable clearance | USB-C must have right-side plug clearance | Reserve `x=84..100`, `y=8..29` during early placement |
| Enclosure assumptions | No enclosure dimensions are known | Treat board size and connector locations as prototype-first assumptions |
| Board thickness | 1.6 mm assumed | Confirm connector compatibility with 1.6 mm board during mechanical review |

## RF / Antenna Risks

| Risk | Detail | Mitigation |
|---|---|---|
| Antenna/U.FL keepout | `ESP32-S3-WROOM-1U` may require external antenna/pigtail handling, not onboard antenna clearance only | Reserve top keepout `x=52..86`, `y=52..65` until exact module footprint/keepout is verified |
| Copper under RF area | Copper near antenna/pigtail can detune RF path | No copper/components in RF keepout during zones phase |
| Buck proximity | Buck switch node noise can couple into RF | Keep U1/L1 near center-left, away from top RF keepout |

## Power Risks

| Risk | Detail | Mitigation |
|---|---|---|
| Buck switch node | Long BUCK_SW route increases EMI | Place U1/L1/C6 as a tight cluster and keep SW copper compact |
| Input protection heat/current | J1/F1/Q1/D3/C5 path carries input current | Use wide +5V/protected traces later and short left-to-center chain |
| AP63203 support parts | Regulator stability depends on correct inductor/cap selection | Placement plan keeps parts close, but BOM/package review remains required |
| Brownout risk | ESP32 WiFi current spikes need good 3V3 decoupling | Place C7/C8 and C3/C4 close to output/module power path |

## USB Risks

| Risk | Detail | Mitigation |
|---|---|---|
| USB D+/D- length/skew | U2 is in top/right half while J2 is lower/right | Keep J2/U3/R8/R9 in a direct corridor and avoid detours |
| USB ESD return | ESD needs short return to GND/shield policy | Place U3 near J2 and add via stitching later |
| CC resistor placement | CC resistors should be close to J2 | Place R6/R7 behind connector at `(87,13)` and `(87,15)` |
| Test pad stubs | TP8/TP9 on USB lines are risky | Keep at bottom only if accepted; otherwise do not populate/use |

## Blockers Before Actual Component Placement

These do not block Phase 4 mechanical setup, but they block placement approval:

1. Confirm J1 edge/orientation with footprint fab/courtyard layers.
2. Confirm J2 edge/orientation with footprint fab/courtyard layers.
3. Confirm U2 footprint is correct for ESP32-S3-WROOM-1U.
4. Review U2 pad 41 drill-size DRC issue.
5. Confirm U3 USB ESD exact pinout and orientation.
6. Confirm D3 TVS exact package and polarity.
7. Confirm Q1 SOT-23 physical orientation and pin 1 marker.
8. Decide TP8/TP9 USB test pad policy.
9. Decide USB shield/GND policy.

## Next Phase

Next allowed phase: `PHASE_4_MECHANICAL_SETUP`

Allowed next work:

- Create board outline `(0,0)` to `(100,65)`.
- Place MH1-MH4 at specified coordinates.
- Add mechanical keepouts and basic constraints.

Still not allowed:

- final component placement
- routing
- copper zones
- fabrication outputs
- JLCPCB/production review
