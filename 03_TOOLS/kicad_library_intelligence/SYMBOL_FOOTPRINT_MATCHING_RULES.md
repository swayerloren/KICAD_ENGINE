# Symbol Footprint Matching Rules

Date: 2026-05-02

Purpose: define how agents should connect KiCad symbols to footprints safely.

## Core Rule

Never treat a symbol-footprint pair as correct because both names look similar. Correctness requires source evidence.

## Required Evidence

| Evidence | Required Check |
| --- | --- |
| Datasheet or package drawing | Exact package, pin numbers, mechanical outline, exposed pad, recommended land pattern. |
| Symbol | Pin numbers, pin names, units, hidden power pins, alternate functions, footprint field. |
| Footprint | Pad numbers, pad geometry, drill sizes, courtyard, paste/mask, pin 1, fab outline. |
| 3D model | Orientation, body size, height, connector/cable/mechanical clearance. |
| KiCad ERC/DRC | Electrical and layout consistency, not datasheet correctness. |

## Workflow

1. Find symbol candidates with `find_symbol_candidates.py`.
2. Read the exact symbol entry in the `.kicad_sym` file.
3. Find footprint candidates with `find_footprint_candidates.py` only after package or connector family is known.
4. Read the exact `.kicad_mod` file.
5. Compare symbol pad numbers to footprint pad names and numbers.
6. Compare footprint geometry to the manufacturer drawing.
7. Verify 3D model exists and visually matches the selected part where mechanical review matters.
8. Record unresolved mismatches in project history or design review notes.

## High-Risk Matching Cases

- USB-C receptacles and plugs.
- RF connectors and antenna modules.
- Board-to-board connectors.
- Automotive or OEM harness connectors.
- STM32 and other MCUs with wildcard package symbols.
- QFN/DFN with exposed pads and thermal vias.
- Modules with castellated pads and antenna keepouts.
- Crystals with small 2-pin or 4-pin packages.
- Power regulators with similar ordering codes but different packages.

## AI Warnings

- A KiCad symbol footprint field is a hint, not proof.
- A footprint 3D model is a visual aid, not pad-geometry proof.
- A package name such as `SOIC-8` is incomplete without body width, pitch, exposed pad status, and manufacturer drawing.
- A connector pitch is incomplete without orientation, latch direction, pin 1, mating part, and mounting feature review.
