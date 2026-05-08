# Playwright Pilot Footprint Gap Report

Status: `UNVERIFIED`

## Summary

The pilot produced source-link-only candidates. No live browser capture, screenshot evidence, or footprint metadata extraction was run because Playwright is not installed locally.

## Footprint Risk Table

| Part | Candidate Source | Footprint Status | Risk | Notes |
| --- | --- | --- | --- | --- |
| STM32F103C8T6 | ST official product page link | `UNVERIFIED` | Medium | Exact package variant and KiCad footprint must be matched to official package drawing. |
| ESP32-S3-WROOM-1 | Espressif official module page link | `UNVERIFIED` | High | Module footprint, antenna keepout, and 3D/mechanical orientation require official drawing review. |
| MCP2562FD | Microchip official product page link | `UNVERIFIED` | Medium | Package variant must be selected before footprint verification. |
| AP63203 | Diodes Inc official product page link | `UNVERIFIED` | High | Regulator package, thermal pad if any, and layout rules require datasheet review. |
| USB-C 16-pin receptacle generic | KiCad Connector_USB library folder link | `UNVERIFIED` | High | Generic USB-C connector cannot be footprint-verified without exact manufacturer drawing and orientation review. |

## Blockers

- Playwright package is not installed, so no screenshots or public-page metadata were captured.
- No datasheets or package drawings were downloaded.
- No exact footprint was verified.

