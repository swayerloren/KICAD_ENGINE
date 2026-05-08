# Protection Master Index

Date: 2026-05-02

Status: starter index. No datasheet PDFs are bundled here yet. Every generic protection entry is a placeholder until an exact manufacturer part number, package drawing, electrical rating, and source URL are recorded.

## Purpose

This folder tracks ESD, TVS, surge, reverse-polarity, and transient-protection source documents for KiCad design work. AI agents should use it to find evidence before choosing or reviewing a protection part.

## Current Starter Records

| Topic | Component Database Record | Status | Required Verification Before Use |
| --- | --- | --- | --- |
| USB ESD diode array generic | `08_COMPONENT_DATABASE/05_PROTECTION/PROTECTION_RECORDS.md` | `UNVERIFIED_PLACEHOLDER` | Working voltage, capacitance, clamp behavior, package pinout, USB speed suitability, footprint |
| CAN TVS diode generic | `08_COMPONENT_DATABASE/05_PROTECTION/PROTECTION_RECORDS.md` | `UNVERIFIED_PLACEHOLDER` | Standoff voltage, surge rating, bidirectional behavior, bus capacitance, package, footprint |

## Source Priorities

1. Exact manufacturer datasheet for the selected part number.
2. Manufacturer application note for the specific interface or surge standard.
3. Reference design using the exact part number and package.
4. KiCad library symbol and footprint inspection.
5. Distributor parametric page only as a search aid, not as final evidence.

## Agent Rules

- Do not reuse a generic ESD or TVS footprint without checking the exact package drawing.
- Do not assume one USB ESD array is safe for USB 2.0, USB 3.x, USB-C CC, or power pins without capacitance and voltage verification.
- Do not assume a CAN TVS selected for 12 V automotive inputs is valid for a 5 V or 3.3 V CAN transceiver bus.
- Record source links in `SOURCES.md` before promoting any placeholder.
- Keep public-release entries link-first unless redistribution rights for datasheet PDFs are confirmed.

## Related Rules

- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/ESD_TVS_RULES.md`
- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/POWER_INPUT_PROTECTION_RULES.md`
- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/USB_C_LAYOUT_RULES.md`
- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/CAN_BUS_LAYOUT_RULES.md`
