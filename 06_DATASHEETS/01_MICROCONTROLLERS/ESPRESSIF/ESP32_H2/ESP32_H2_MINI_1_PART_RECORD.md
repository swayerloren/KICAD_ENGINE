# ESP32-H2-MINI-1 Part Record

Date: 2026-05-03
Vendor: `ESPRESSIF`
Family: `ESP32_H2`
Status: `UNVERIFIED_PLACEHOLDER`
Human review required: `true`

This generated record is for AI-assisted planning only. It does not approve schematic use, footprint use, BOM lock, or PCB layout.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public source URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact value checked in a named datasheet/reference document.
- `INFERRED_FROM_COMMON_DESIGN`: common design pattern; verify before use.
- `UNVERIFIED`: not checked against source evidence.
- `NEEDS_HUMAN_REVIEW`: must be reviewed before schematic, PCB, BOM, or fabrication use.

## Identity

| Field | Value | Status |
| --- | --- | --- |
| manufacturer | `ESPRESSIF` | `UNVERIFIED` |
| part_number | `ESP32-H2-MINI-1` | `UNVERIFIED` |
| family | `ESP32_H2` | `UNVERIFIED` |
| category | microcontroller | `UNVERIFIED` |
| datasheet source | `UNKNOWN_REQUIRES_SOURCE` | `UNVERIFIED` |
| local datasheet | none bundled | `UNVERIFIED` |

## Candidate KiCad Links

| Item | Candidate | Status |
| --- | --- | --- |
| symbol | `UNKNOWN_REQUIRES_SOURCE` | `UNVERIFIED` |
| footprint | `UNKNOWN_REQUIRES_SOURCE` | `UNVERIFIED` |
| 3D model | `UNKNOWN_REQUIRES_SOURCE` | `UNVERIFIED` |

## Required External Circuit Blocks

| Block | Guidance | Status |
| --- | --- | --- |
| power rails | Verify all supply pins, domains, and decoupling from datasheet. | `NEEDS_HUMAN_REVIEW` |
| reset | Verify reset circuit and programmer requirements. | `NEEDS_HUMAN_REVIEW` |
| boot/config pins | Verify default state and recovery access. | `NEEDS_HUMAN_REVIEW` |
| debug/programming | Verify connector, target voltage, and pin conflicts. | `NEEDS_HUMAN_REVIEW` |
| clocks | Verify internal/external oscillator plan and component values. | `NEEDS_HUMAN_REVIEW` |
| communication interfaces | Verify interface-specific requirements before use. | `NEEDS_HUMAN_REVIEW` |

## Before PCB

- Verify exact datasheet revision.
- Verify package/order-code mapping.
- Audit KiCad symbol pinout.
- Audit footprint against exact package drawing.
- Record unresolved items in `NEEDS_REVIEW`.
