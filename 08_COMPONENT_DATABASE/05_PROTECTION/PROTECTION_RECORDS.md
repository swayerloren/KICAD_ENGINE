# Protection Records

Date: 2026-05-02

Status: generic placeholders. These records are not approved selections and must be replaced or promoted only after exact manufacturer part, datasheet, package drawing, and footprint evidence are recorded.

## Records

| Record ID | Part | Category | Status | Primary Checks |
| --- | --- | --- | --- | --- |
| `PROTECTION_USB_ESD_DIODE_ARRAY_GENERIC` | USB ESD diode array generic | USB/data-line ESD | `UNVERIFIED_PLACEHOLDER` | Working voltage, capacitance, clamp behavior, channel count, package pinout |
| `PROTECTION_CAN_TVS_DIODE_GENERIC` | CAN TVS diode generic | CAN bus transient protection | `UNVERIFIED_PLACEHOLDER` | Standoff voltage, surge rating, bus capacitance, bidirectional behavior, package |

## USB ESD Diode Array Generic

- Use for: documenting the need for USB data/CC protection near a connector.
- Do not use for: final USB 2.0, USB 3.x, USB-C, or power-path protection without part-specific verification.
- KiCad candidates: generic ESD/TVS diode symbols only; package and pinout must come from the exact part.
- Layout warning: place near connector and keep protected traces from forming long stubs.
- AI warning: capacitance is interface-critical and is unknown until the exact part is selected.

## CAN TVS Diode Generic

- Use for: documenting the need for CAN_H/CAN_L transient protection near the bus connector.
- Do not use for: final automotive, industrial, or long-cable CAN designs without surge and EMC requirements.
- KiCad candidates: bidirectional TVS diode or array symbols only; footprint must match the exact package.
- Layout warning: TVS return path must be short and intentional, and CAN differential routing must preserve pair behavior.
- AI warning: do not reuse power-input TVS parts on CAN lines without bus capacitance and standoff verification.

## Promotion Checklist

- Exact manufacturer part number selected.
- Datasheet source URL recorded.
- Public redistribution status recorded if a PDF is bundled.
- Package drawing matched to KiCad footprint.
- Symbol pinout checked against datasheet.
- Interface capacitance and clamp behavior reviewed.
- PCB placement and ground path reviewed.
