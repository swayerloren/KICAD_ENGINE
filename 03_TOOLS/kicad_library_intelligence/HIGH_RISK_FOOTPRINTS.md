# High-Risk Footprints

Date: 2026-05-02

Purpose: identify footprint classes where AI agents must slow down and verify exact source drawings.

## High-Risk Classes

| Class | Why It Is Risky | Required Verification |
| --- | --- | --- |
| USB-C connectors | Many pin counts, shell styles, mounting stakes, hybrid pads, and orientation variants. | Exact manufacturer drawing, pin numbering, shield strategy, CC pins, VBUS current, cable direction. |
| RF connectors | Edge launch geometry, impedance, ground via strategy, gender, and mechanical fit. | Exact connector drawing, board stackup, launch geometry, 3D clearance. |
| JST/Molex/TE connectors | Similar pitch names hide latch, pin 1, and mating differences. | Series, pitch, orientation, latch direction, mating part, drawing. |
| Automotive connectors | OEM variants and seals are mechanically specific. | Exact part family, terminal system, seal, latch, pin numbering, harness side. |
| QFN/DFN | Exposed pad, paste, thermal vias, and pin 1 errors are common. | JEDEC/vendor package drawing, pad count, EP size, paste, via plan. |
| BGA/CSP/WLCSP | Ball maps and fab capability dominate. | Ball map, pitch, escape routing, via/drill capability, assembly process. |
| RF modules | Castellated pads, keepouts, antenna zones, and thermal pads vary. | Module datasheet, recommended footprint, keepout, antenna orientation. |
| MCU packages | One part family has many package codes and pin-count variants. | Exact ordering code, symbol pin map, package drawing, footprint drawing. |
| Crystals | Similar packages can have different pad geometry and grounding. | Crystal package drawing, CL/ESR/drive-level source, layout guide. |
| Power packages | Thermal pad, tab net, and heat dissipation are often missed. | Package thermal drawing, exposed pad net, copper area, paste mask. |

## Agent Rule

If the footprint affects mechanical fit, assembly yield, pin numbering, RF behavior, thermal behavior, or high-speed routing, treat it as high-risk until proven otherwise.

## Do Not Claim

- Do not claim connector orientation is correct without a drawing.
- Do not claim an MCU footprint is correct from the symbol name alone.
- Do not claim a module footprint is correct without keepout review.
- Do not claim a QFN/DFN footprint is production-ready without exposed-pad and paste review.
