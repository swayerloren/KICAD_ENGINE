# ESP32-S2-REPRESENTATIVE_PART_REQUIRES_SOURCE Schematic Notes

Date: 2026-05-03
Status: `AI_PLANNING_CHECKLIST`

These notes define a conservative minimum-system checklist for `ESP32-S2-REPRESENTATIVE_PART_REQUIRES_SOURCE`. They are not schematic instructions until exact source evidence is added.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public source URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact value checked in a named datasheet/reference document.
- `INFERRED_FROM_COMMON_DESIGN`: common design pattern; verify before use.
- `UNVERIFIED`: not checked against source evidence.
- `NEEDS_HUMAN_REVIEW`: must be reviewed before schematic, PCB, BOM, or fabrication use.

## Minimum System Blocks

| Block | Required Checks | Evidence Status |
| --- | --- | --- |
| MCU symbol | exact symbol, all pins audited, hidden power pins understood | `NEEDS_HUMAN_REVIEW` |
| power pins | all supply and ground pins connected intentionally | `NEEDS_HUMAN_REVIEW` |
| decoupling | capacitor count, values, placement, and voltage rating source-checked | `NEEDS_HUMAN_REVIEW` |
| analog supply/reference | VDDA/VSSA/VREF or equivalent pins handled explicitly | `NEEDS_HUMAN_REVIEW` |
| reset | reset circuit and programmer compatibility reviewed | `NEEDS_HUMAN_REVIEW` |
| boot/config pins | deterministic defaults and recovery access | `NEEDS_HUMAN_REVIEW` |
| debug/programming | connector pins, target voltage, reset, and ground | `NEEDS_HUMAN_REVIEW` |
| clocks | internal/external oscillator choice and component values | `NEEDS_HUMAN_REVIEW` |
| interfaces | USB/CAN/UART/I2C/SPI/RF rules checked only if used | `NEEDS_HUMAN_REVIEW` |

## Do Not Guess

- Do not infer pin numbers from package name.
- Do not assume one family member matches another.
- Do not copy dev-board circuits without source and license review.
- Do not treat ERC pass as datasheet verification.
