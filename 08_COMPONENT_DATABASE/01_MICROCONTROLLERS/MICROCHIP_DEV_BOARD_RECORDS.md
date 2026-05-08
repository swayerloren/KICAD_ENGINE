# Microchip Dev Board Records

Date: 2026-05-02

Status: reference-only dev-board guidance for AI-assisted KiCad planning. Board records do not prove custom-board schematic or PCB correctness.

## Curiosity Development Board Family

| Field | Value |
| --- | --- |
| Record ID | `DEVBOARD_MICROCHIP_CURIOSITY_FAMILY` |
| Source documents | Curiosity board family page: https://www.microchip.com/en-us/tools-resources/evaluation-boards/curiosity |
| Schematic link | Board-specific schematic must be selected by part number and revision. |
| KiCad symbol candidates | Board-level reference only; use exact MCU records for custom symbols. |
| KiCad footprint candidates | Board-level reference only. |
| Debug/programming notes | Many Curiosity boards include integrated programmer/debugger circuits. Separate those circuits from the target MCU minimum circuit. |
| Boot/programming notes | Do not infer ICSP, UPDI, or bootloader behavior from a board header without checking the exact board and target part. |
| Clocking notes | Board clock sources are examples only; custom designs need datasheet-based clock plans. |
| Power/decoupling notes | Board regulators, power muxes, USB power, and expansion headers are board-specific. |
| Common mistakes | Copying Curiosity circuits without matching board revision; assuming integrated programmer circuitry belongs in the final product. |
| Verification status | `VERIFIED_FROM_VENDOR_REFERENCE_DESIGN`, `UNVERIFIED_PLACEHOLDER` |

## 8-bit Curiosity HPC

| Field | Value |
| --- | --- |
| Record ID | `DEVBOARD_MICROCHIP_CURIOSITY_HPC_DM164136` |
| Source documents | Official board page: https://www.microchip.com/en-us/development-tool/DM164136 |
| Schematic link | Exact schematic resource not extracted in this pass. |
| KiCad symbol candidates | Board-level reference only. |
| KiCad footprint candidates | Board-level reference only. |
| Debug/programming notes | Integrated programmer/debugger; verify target socket, supported PIC parts, jumpers, and voltage before using as a reference. |
| Boot/programming notes | Use as an ICSP and reset reference only after schematic extraction. |
| Clocking notes | Clock circuits are board-specific and not universal PIC defaults. |
| Power/decoupling notes | Board power selection and regulator details require schematic review. |
| Common mistakes | Treating DIP socket board routing as a package-specific custom design. |
| Verification status | `VERIFIED_FROM_VENDOR_REFERENCE_DESIGN`, `UNVERIFIED_PLACEHOLDER` |

## PIC24F Curiosity

| Field | Value |
| --- | --- |
| Record ID | `DEVBOARD_MICROCHIP_PIC24F_CURIOSITY_DM240004` |
| Source documents | Official board page: https://www.microchip.com/en-us/development-tool/DM240004 |
| Schematic link | Exact schematic resource not extracted in this pass. |
| KiCad symbol candidates | Board-level reference only. |
| KiCad footprint candidates | Board-level reference only. |
| Debug/programming notes | Integrated programmer/debugger; verify target MCU and board revision before copying ICSP/debug circuits. |
| Boot/programming notes | PIC24 programming/debug pins are part-specific; do not generalize to PIC24FJ64GA002 without source proof. |
| Clocking notes | Verify external and internal clock source use in the exact board schematic. |
| Power/decoupling notes | PIC24 power rails, analog rails, and any VCAP/core requirements need exact part review. |
| Common mistakes | Assuming PIC24F Curiosity target MCU pinout matches older PIC24FJ64GA002. |
| Verification status | `VERIFIED_FROM_VENDOR_REFERENCE_DESIGN`, `UNVERIFIED_PLACEHOLDER` |

## Explorer 16/32

| Field | Value |
| --- | --- |
| Record ID | `DEVBOARD_MICROCHIP_EXPLORER_16_32_DM240001_2` |
| Source documents | Official board page: https://www.microchip.com/en-us/development-tool/DM240001-2 ; developer help: https://developerhelp.microchip.com/xwiki/bin/view/software-tools/mcu-dev-boards/exp16-32/ |
| Schematic link | Developer help page has schematic and BOM download section; exact file not downloaded in this pass. |
| KiCad symbol candidates | Board-level reference only; exact PIM and MCU records required. |
| KiCad footprint candidates | Board-level reference only. |
| Debug/programming notes | Explorer 16/32 uses PIMs and integrated programmer/debugger context. The central onboard MCU is part of programmer circuitry, not application code. |
| Boot/programming notes | Always identify the exact PIM and target MCU before using board pins or circuits. |
| Clocking notes | Board and PIM clock sources can both matter. Do not copy without exact PIM schematic. |
| Power/decoupling notes | Board has multiple power sources and rails; isolate only the target circuit block needed. |
| Common mistakes | Treating PIM socket pins as MCU pins; copying programmer/debugger and expansion circuitry into a product. |
| Verification status | `VERIFIED_FROM_VENDOR_REFERENCE_DESIGN`, `UNVERIFIED_PLACEHOLDER` |

## Curiosity PIC32MX470

| Field | Value |
| --- | --- |
| Record ID | `DEVBOARD_MICROCHIP_CURIOSITY_PIC32MX470_DM320103` |
| Source documents | Official board page: https://www.microchip.com/en-us/development-tool/DM320103 |
| Schematic link | Exact schematic resource not extracted in this pass. |
| KiCad symbol candidates | Board-level reference only. |
| KiCad footprint candidates | Board-level reference only. |
| Debug/programming notes | Integrated programmer/debugger; useful as a PIC32MX reference only after exact board schematic review. |
| Boot/programming notes | PIC32 ICSP/debug and Harmony workflow require exact part verification. |
| Clocking notes | Useful reference for USB/audio-style PIC32MX design blocks, not a generic clock proof. |
| Power/decoupling notes | PIC32MX power, VCAP, USB, and expansion circuits must be separated. |
| Common mistakes | Copying PIC32MX470 board circuits to PIC32MX250F128D without package and peripheral review. |
| Verification status | `VERIFIED_FROM_VENDOR_REFERENCE_DESIGN`, `UNVERIFIED_PLACEHOLDER` |

## dsPIC33CK Curiosity / PIM References

| Field | Value |
| --- | --- |
| Record ID | `DEVBOARD_MICROCHIP_DSPIC33CK_REFERENCE_PLACEHOLDER` |
| Source documents | dsPIC33CK Curiosity guide observed in official Microchip sources; product-specific PIM guide links are indexed in `MICROCHIP_PIC_MASTER_INDEX.md`. |
| Schematic link | Exact schematic resource not extracted in this pass. |
| KiCad symbol candidates | Board-level reference only. |
| KiCad footprint candidates | Board-level reference only. |
| Debug/programming notes | dsPIC33CK programming and debug circuits must be reviewed with the exact DSC and selected board. |
| Boot/programming notes | Do not infer PGC/PGD pair, MCLR, or reset behavior from another dsPIC33 family. |
| Clocking notes | Digital power, motor control, PWM, ADC, and CAN FD timing need source-based clock review. |
| Power/decoupling notes | Analog and power-stage reference circuits are high risk; use only after exact schematic extraction. |
| Common mistakes | Copying PIM or power-stage examples without understanding measurement ground, gate-drive, and high-current layout. |
| Verification status | `UNVERIFIED_PLACEHOLDER` |
