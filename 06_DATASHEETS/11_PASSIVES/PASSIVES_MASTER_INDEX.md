# Passives Master Index

Date: 2026-05-02

Status: starter index. Generic passive records are placeholders for AI-assisted design review and must not be treated as approved BOM selections.

## Purpose

This folder tracks source documents and selection notes for capacitors, resistors, jumpers, ferrites, common mode chokes, and other board-support passives. It is meant to help agents avoid vague passive choices such as "add a cap" without voltage, package, dielectric, tolerance, derating, and layout evidence.

## Current Starter Records

| Topic | Component Database Record | Status | Required Verification Before Use |
| --- | --- | --- | --- |
| 0.1uF decoupling capacitor generic | `08_COMPONENT_DATABASE/09_PASSIVES/PASSIVE_SUPPORT_RECORDS.md` | `UNVERIFIED_PLACEHOLDER` | Capacitance after DC bias, voltage rating, dielectric, package, placement |
| 10uF bulk capacitor generic | `08_COMPONENT_DATABASE/09_PASSIVES/PASSIVE_SUPPORT_RECORDS.md` | `UNVERIFIED_PLACEHOLDER` | Effective capacitance, ripple current if relevant, ESR, voltage derating, package |
| 22pF crystal load capacitor generic | `08_COMPONENT_DATABASE/09_PASSIVES/PASSIVE_SUPPORT_RECORDS.md` | `UNVERIFIED_PLACEHOLDER` | Crystal load capacitance math, stray capacitance, MCU oscillator recommendation |
| 10k pull-up resistor generic | `08_COMPONENT_DATABASE/09_PASSIVES/PASSIVE_SUPPORT_RECORDS.md` | `UNVERIFIED_PLACEHOLDER` | Interface speed, leakage, voltage domain, boot strap requirements |
| 0 ohm jumper resistor generic | `08_COMPONENT_DATABASE/09_PASSIVES/PASSIVE_SUPPORT_RECORDS.md` | `UNVERIFIED_PLACEHOLDER` | Current rating, package, assembly intent, test/rework access |
| Ferrite bead generic | `08_COMPONENT_DATABASE/09_PASSIVES/PASSIVE_SUPPORT_RECORDS.md` | `UNVERIFIED_PLACEHOLDER` | Impedance curve, DC current, DC resistance, resonance, target noise band |
| Common mode choke generic | `08_COMPONENT_DATABASE/09_PASSIVES/PASSIVE_SUPPORT_RECORDS.md` | `UNVERIFIED_PLACEHOLDER` | Differential impedance, common-mode impedance, current, connector/interface match |

## Agent Rules

- Do not promote nominal capacitance alone as a complete capacitor selection.
- Treat MLCC effective capacitance as unknown until package, dielectric, voltage rating, DC bias, and temperature are known.
- Treat 22pF crystal capacitors as a legacy/common placeholder, not a universal answer.
- For ferrites and common mode chokes, verify the impedance curve, current rating, and insertion-loss impact on the actual signal or rail.
- Use `SOURCES.md` for manufacturer design guides and exact passive datasheets before public release.

## Related Rules

- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/DECOUPLING_CAPACITOR_RULES.md`
- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/CRYSTAL_LAYOUT_RULES.md`
- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/ESD_TVS_RULES.md`
