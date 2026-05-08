# STM32F103C8T6 Schematic Notes

Date: 2026-05-03
Status: `AI_PLANNING_CHECKLIST`

These notes define a conservative minimum-system review checklist for STM32F103C8T6. They are not source-complete schematic instructions.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact value checked in a named ST datasheet/reference document.
- `INFERRED_FROM_COMMON_DESIGN`: common STM32F1 design pattern; verify before use.
- `UNVERIFIED`: not checked.
- `NEEDS_HUMAN_REVIEW`: must be reviewed before schematic/PCB/fab use.

## Minimum System Blocks

| Block | Required Checks | Evidence Status |
| --- | --- | --- |
| MCU symbol | Correct exact symbol, all pins visible/audited, hidden power pins understood, no unconnected required pins. | `NEEDS_HUMAN_REVIEW` |
| VDD/VSS | Supply pins connected with local decoupling and a clear rail name. | `INFERRED_FROM_COMMON_DESIGN` |
| VDDA/VSSA/VREF | Analog supply/ground/reference handling intentionally designed, not left implicit. | `NEEDS_HUMAN_REVIEW` |
| NRST | Reset circuit, button/header access, and programming-tool compatibility reviewed. | `INFERRED_FROM_COMMON_DESIGN` |
| BOOT0/BOOT1 | Deterministic default boot mode plus recovery access. | `NEEDS_HUMAN_REVIEW` |
| SWD/ST-Link | SWDIO, SWCLK, GND, target voltage, and preferably NRST available. | `INFERRED_FROM_COMMON_DESIGN` |
| clock source | Internal/external oscillator decision documented; HSE/LSE circuits source-checked. | `NEEDS_HUMAN_REVIEW` |
| USB FS | PA11/PA12 use, VBUS policy, pull-up/disconnect behavior, ESD, series resistors, connector shield policy reviewed. | `NEEDS_HUMAN_REVIEW` |
| CAN | If used, add a proper CAN transceiver, protection, termination strategy, and pin remap review. | `NEEDS_HUMAN_REVIEW` |
| test points | Reset, SWD, power rails, boot pins, and critical interfaces accessible where appropriate. | `INFERRED_FROM_COMMON_DESIGN` |

## Do Not Guess

- Do not infer pin numbers from a package picture.
- Do not assume every STM32F103 variant supports the same USB/CAN/pin mapping.
- Do not omit BOOT pins because firmware normally uses SWD.
- Do not use Blue Pill resistor/crystal/power choices as a copied schematic.
- Do not treat ERC pass as datasheet verification.

## Schematic Gate For PCB

Before PCB update, the schematic must have:

- exact part record linked;
- all references annotated;
- no unresolved `NEEDS_REVIEW` on boot/debug/power/USB/package/footprint;
- ERC run and reviewed;
- BOM lock alignment;
- footprint package audit complete;
- human-review-required items listed.
