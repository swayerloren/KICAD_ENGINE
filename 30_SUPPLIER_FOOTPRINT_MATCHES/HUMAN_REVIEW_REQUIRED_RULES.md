# Human Review Required Rules

Status: mandatory human-review rules for supplier-to-KiCad footprint matches.

## Always Human-Review Required

Keep `human_review_required: true` for:

- USB-C connectors.
- RF connectors and antenna connectors.
- Board-edge connectors.
- Automotive connectors.
- Any connector without exact mating-part and orientation review.
- PMOS and MOSFET footprints where source/gate/drain mapping matters.
- ESD diode arrays and TVS arrays.
- MCU modules such as ESP32 WROOM/WROVER/MINI.
- Bare MCUs in QFN, BGA, WLCSP, UFQFPN, LQFP, or similar packages.
- Regulators with exposed pads, thermal requirements, or switching-loop constraints.
- Barrel jacks and mechanically loaded connectors.
- Mounting holes, test pads, pogo pads, and assembly-critical features.

## Human Review Can Be Cleared Only When

- Exact MPN and package suffix are known.
- Source drawing is recorded.
- KiCad footprint candidate is inspected.
- Pad numbering and pin mapping are checked.
- Mechanical orientation is reviewed.
- 3D model or physical drawing is checked where useful.
- The reviewer records their name or user-confirmed status in evidence.

## Prohibited

- Do not clear human review from supplier package text alone.
- Do not clear human review from KiCad library name alone.
- Do not clear human review from a generic footprint candidate.
- Do not clear human review for connectors without orientation and mating connector evidence.

