# STM32F1 Pilot Remaining Verification Backlog

Date: 2026-05-03
Status: `OPEN`

## Issue

STM32F1 pilot content is now useful for AI planning, but STM32F103C8T6 is not yet approved for schematic, footprint, PCB, or fabrication decisions.

## Open Items

- Exact ST datasheet revision and section references need extraction.
- `STM32F103C8T6` package/order-code table must be checked.
- KiCad symbol `MCU_ST_STM32F1:STM32F103C8Tx` must be audited pin-by-pin.
- KiCad footprint `Package_QFP:LQFP-48_7x7mm_P0.5mm` must be compared to ST package drawing.
- BOOT0/BOOT1 behavior must be checked in AN2606/RM0008 for the exact part.
- USB, oscillator, VDDA/VSSA/VREF, reset, and SWD choices require source-section review.
- Blue Pill notes require exact board revision and human review before reuse.

## Risk

`HIGH_RISK` if an AI agent treats candidate symbol/footprint data as verified.

## Required Close Condition

Create source-section-backed verification records and human-review signoff before using these records to approve a PCB update or manufacturing package.
