# Clocks And Timing Master Index

Date: 2026-05-02

Status: starter index. Crystal records are generic placeholders until exact manufacturer part, load capacitance, ESR, drive level, tolerance, stability, package, and oscillator-source guidance are verified.

## Purpose

This folder tracks clock-source datasheets, oscillator application notes, MCU oscillator requirements, and crystal layout references. It exists because clock circuits often fail from small assumptions: wrong load capacitors, poor routing, excessive drive level, unsuitable ESR, or copying a dev-board value into a different stackup.

## Current Starter Records

| Topic | Component Database Record | Status | Required Verification Before Use |
| --- | --- | --- | --- |
| 8 MHz crystal generic | `08_COMPONENT_DATABASE/09_PASSIVES/PASSIVE_SUPPORT_RECORDS.md` | `UNVERIFIED_PLACEHOLDER` | MCU oscillator mode, CL, ESR, tolerance, drive level, package |
| 16 MHz crystal generic | `08_COMPONENT_DATABASE/09_PASSIVES/PASSIVE_SUPPORT_RECORDS.md` | `UNVERIFIED_PLACEHOLDER` | MCU oscillator mode, CL, ESR, tolerance, drive level, package |
| 40 MHz crystal generic | `08_COMPONENT_DATABASE/09_PASSIVES/PASSIVE_SUPPORT_RECORDS.md` | `UNVERIFIED_PLACEHOLDER` | RF chip/module reference requirement, CL, ESR, tolerance, layout |
| 32.768 kHz crystal generic | `08_COMPONENT_DATABASE/09_PASSIVES/PASSIVE_SUPPORT_RECORDS.md` | `UNVERIFIED_PLACEHOLDER` | Low-power oscillator requirements, CL, ESR, leakage, guard routing |

## Agent Rules

- Do not assume crystal frequency alone is enough to select a part.
- Do not assume 22pF load capacitors are correct for every crystal.
- Verify crystal load capacitance using the selected crystal CL, estimated stray capacitance, and MCU/vendor oscillator guidance.
- Verify exact package footprint and pad geometry against the crystal drawing.
- Keep clock traces short, quiet, and away from switching nodes, USB pairs, RF feedlines, and high-current loops.

## Related Rules

- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/CRYSTAL_LAYOUT_RULES.md`
- `08_COMPONENT_DATABASE/09_PASSIVES/PASSIVE_SUPPORT_RECORDS.md`
