# STM32L1 Schematic Block Checklist

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Required Before Schematic Placement

- Exact order code selected and recorded.
- Official product page, datasheet, reference manual, errata, and package drawing linked.
- Power pins, analog rails, VREF, VBAT, VCAP/SMPS/LDO pins, exposed pads, and decoupling reviewed.
- Reset and boot mode network reviewed against AN2606 and reference manual.
- SWD/debug connector or test pads included.
- Clock sources selected only after source review.
- USB/CAN/FDCAN only added when exact part/package supports required pins.
- All communication transceivers/protection components have source-backed component records.
- KiCad symbol candidate compared with official pinout.
- Footprint candidate compared with package drawing or marked UNVERIFIED.
- Every unknown exact value marked UNKNOWN_REQUIRES_SOURCE or NEEDS_REVIEW.

## Minimum Block Categories

- Power input and regulation appropriate for selected part.
- MCU power domains and decoupling.
- Reset and boot/recovery.
- SWD/debug/programming.
- Clock sources as required.
- USB/CAN/FDCAN/external transceivers only when source-backed.
- Test points for critical rails, reset, boot, debug, and high-risk interfaces.
- Notes for all unresolved `UNKNOWN_REQUIRES_SOURCE` items.

## Blocking Conditions

- Missing exact order code.
- Missing official datasheet/reference manual/package drawing.
- Unverified pinout.
- Unverified footprint.
- Connector orientation or polarity not reviewed.
- Claimed ERC pass without report.
