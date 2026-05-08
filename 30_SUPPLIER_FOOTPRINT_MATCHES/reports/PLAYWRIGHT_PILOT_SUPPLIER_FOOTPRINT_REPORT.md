# Playwright Pilot Supplier-Footprint Report

Status: `UNVERIFIED`

## Scope

Pilot parts:

- STM32F103C8T6
- ESP32-S3-WROOM-1
- MCP2562FD
- AP63203
- USB-C 16-pin receptacle generic

## Result

No supplier SKU to KiCad footprint match was verified in this run. The pilot only created dry-run normalized records and source-link-only candidate records.

## Match Status

| Part | Supplier SKU | KiCad Footprint Candidate | Match Status | Human Review |
| --- | --- | --- | --- | --- |
| STM32F103C8T6 | `UNKNOWN` | `UNKNOWN` | `UNVERIFIED` | Required |
| ESP32-S3-WROOM-1 | `UNKNOWN` | `UNKNOWN` | `UNVERIFIED` | Required |
| MCP2562FD | `UNKNOWN` | `UNKNOWN` | `UNVERIFIED` | Required |
| AP63203 | `UNKNOWN` | `UNKNOWN` | `UNVERIFIED` | Required |
| USB-C 16-pin receptacle generic | `UNKNOWN` | KiCad Connector_USB folder only | `UNVERIFIED` | Required |

## Rule Reinforcement

No connector, PMOS, ESD array, MCU module, or regulator footprint may be marked verified from a generic package or library-folder match. Exact package drawing and human review are still required.

