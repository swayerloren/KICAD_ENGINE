# STM32F103C8T6 Part Record

Date: 2026-05-03
Status: `PARTIAL_SOURCE_LINK_RECORD`

This record is for AI-assisted planning only. It does not approve schematic use, footprint use, or PCB layout.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact value checked in the named ST datasheet/reference document.
- `INFERRED_FROM_COMMON_DESIGN`: common design pattern; verify before use.
- `UNVERIFIED`: not checked.
- `NEEDS_HUMAN_REVIEW`: must be reviewed before schematic/PCB/fab use.

## Identity

| Field | Value | Status |
| --- | --- | --- |
| Manufacturer | STMicroelectronics | `VERIFIED_SOURCE_LINK` |
| Part number | STM32F103C8T6 | `VERIFIED_SOURCE_LINK` from ST product page orderable part listing |
| Family | STM32F1 / STM32F103 | `VERIFIED_SOURCE_LINK` |
| Category | microcontroller | `VERIFIED_SOURCE_LINK` |
| Datasheet source | https://www.st.com/resource/en/datasheet/stm32f103c8.pdf | `VERIFIED_SOURCE_LINK` |
| Product page | https://www.st.com/en/microcontrollers-microprocessors/stm32f103c8 | `VERIFIED_SOURCE_LINK` |
| Local datasheet | none bundled | `UNVERIFIED` |

## Known Source-Linked Capabilities

`VERIFIED_SOURCE_LINK`: ST's STM32F103C8 page describes the part family as Cortex-M3, 64 Kbytes Flash, 72 MHz CPU, with USB and CAN support.

`NEEDS_HUMAN_REVIEW`: Treat those as product-page facts only until the exact datasheet revision is checked for electrical limits, package, and pinout.

## Candidate KiCad Links

| Item | Candidate | Evidence | Status |
| --- | --- | --- | --- |
| Symbol | `MCU_ST_STM32F1:STM32F103C8Tx` | Found in installed KiCad 9 symbol library | `VERIFIED_FROM_KICAD_LIBRARY` for existence only |
| Footprint | `Package_QFP:LQFP-48_7x7mm_P0.5mm` | Found in installed KiCad 9 footprint library | `UNVERIFIED` exact package match |
| 3D model | `${KICAD9_3DMODEL_DIR}/Package_QFP.3dshapes/LQFP-48_7x7mm_P0.5mm.step` | Found via KiCad footprint model path | `UNVERIFIED` mechanical fit |

## Required External Circuit Blocks

| Block | Guidance | Status |
| --- | --- | --- |
| VDD/VSS decoupling | Place local decoupling for every supply pair and verify AN2586/datasheet recommendations. | `INFERRED_FROM_COMMON_DESIGN`, `NEEDS_HUMAN_REVIEW` |
| VDDA/VSSA | Do not leave analog supply/ground handling to hidden pins or implicit nets. Verify filtering and connection rules. | `NEEDS_HUMAN_REVIEW` |
| NRST | Provide reset access and verify pull/reset circuit against ST guidance. | `INFERRED_FROM_COMMON_DESIGN` |
| BOOT0/BOOT1 | Provide deterministic straps and recovery access. Verify exact boot mode table. | `NEEDS_HUMAN_REVIEW` |
| SWD | Expose SWDIO, SWCLK, GND, target voltage, and preferably NRST. | `INFERRED_FROM_COMMON_DESIGN` |
| clocking | Decide HSI/HSE/LSE from firmware and USB needs; verify with AN2867 and datasheet. | `NEEDS_HUMAN_REVIEW` |
| USB | Verify USB pins, clock, VBUS policy, pull-up/disconnect behavior, ESD, and routing. | `NEEDS_HUMAN_REVIEW` |

## Common Mistakes

- Using a KiCad symbol without checking every power pin and boot/debug pin.
- Assigning `LQFP-48_7x7mm_P0.5mm` only because the name looks right.
- Copying a Blue Pill schematic without checking the exact board variant.
- Omitting BOOT0 access and then losing serial bootloader recovery.
- Reusing SWD pins without preserving debug access.
- Treating USB pull-up, VBUS sensing, and ESD as optional memory-based details.

## Before PCB

This part record remains blocked for PCB until:

- exact ST datasheet revision is reviewed;
- package/order-code table confirms the package for `STM32F103C8T6`;
- KiCad symbol pin numbers are audited against the datasheet;
- footprint pads/courtyard/fab/pin-1/3D model are compared to ST package drawing;
- BOOT0/BOOT1, SWD, NRST, VDDA/VSSA, oscillator, and USB policies are reviewed.
