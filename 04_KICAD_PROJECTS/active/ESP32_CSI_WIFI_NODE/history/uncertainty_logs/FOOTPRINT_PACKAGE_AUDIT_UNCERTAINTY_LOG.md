# FOOTPRINT_PACKAGE_AUDIT_UNCERTAINTY_LOG

Status: `OPEN`

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

## Uncertainties

| Item | Confidence | Why uncertain | Required evidence |
| --- | --- | --- | --- |
| Exact USB-C connector MPN and footprint | `LOW` | Schematic value is generic and footprint is blank. | Manufacturer part number, drawing, KiCad footprint, pin numbering, board-edge review. |
| AO3401A-class PMOS package/pin mapping | `LOW` | Schematic explicitly marks pin mapping blocked and footprint is blank. | Exact datasheet, symbol pin map, footprint pad map, body diode orientation review. |
| ESP32-S3-WROOM-1U footprint | `LOW` | Value says `1U`; symbol says `WROOM-1`; footprint is blank. | Espressif drawing and exact KiCad footprint verification for selected module variant. |
| AP63203 regulator package | `LOW` | Symbol/value name suggests part family, but no datasheet or footprint is assigned. | Exact device datasheet/package and land-pattern match. |
| USB ESD package/pinout | `LOW` | Value is `TPD2EUSB30_OR_EQ_NEEDS_REVIEW`; exact suffix/package missing. | Exact part suffix, package drawing, footprint, and signal pin mapping. |
| Barrel jack, test pads, mounting holes | `LOW` | Mechanical footprints are blank. | Exact connector/hardware selections, mechanical drawings, board constraints, and 3D/mechanical review. |

## Gate Impact

These uncertainties block PCB update and require human/source review.

