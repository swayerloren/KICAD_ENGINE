# STM32 Part Records

Date: 2026-05-02

Status: partial official-source records for AI-assisted KiCad planning. These are not design-approved until the exact datasheet, reference manual, errata, package drawing, KiCad symbol, and footprint are checked together.

## Record Status Language

- `VERIFIED_FROM_DATASHEET`: A stated value is taken from an official ST product page or datasheet link in the record.
- `VERIFIED_FROM_KICAD_LIBRARY`: A candidate symbol/footprint name was found by read-only search in the installed KiCad 9 stock libraries.
- `UNVERIFIED_PLACEHOLDER`: Exact pinout, package, footprint, errata, or layout details still require verification.

## Common Source Set

- ST STM32 master index: `06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32_MASTER_INDEX.md`
- AN2606 boot mode: https://www.st.com/resource/en/application_note/an2606-stm32-microcontroller-system-memory-boot-mode-stmicroelectronics.pdf
- AN2867 oscillator design: https://www.st.com/resource/en/application_note/an2867-oscillator-design-guide-for-stm8afals-stm32-mcus-and-mpus-stmicroelectronics.pdf
- AN4879 USB hardware guidelines: https://www.st.com/resource/en/application_note/an4879-introduction-to-usb-hardware-and-pcb-guidelines-using-stm32-mcus-stmicroelectronics.pdf
- ST-LINK documentation: https://www.st.com/en/development-tools/hardware-debugger-and-programmer-tools-for-stm32/documentation.html

## STM32F103C8T6

| Field | Value |
| --- | --- |
| Record ID | `STMICRO_STM32F103C8T6` |
| Vendor | STMicroelectronics |
| Family | STM32F1 |
| Category | `01_MICROCONTROLLERS` |
| Source documents | ST product page: https://www.st.com/en/microcontrollers-microprocessors/stm32f103c8.html ; datasheet link: https://www.st.com/resource/en/datasheet/stm32f103c8.pdf ; AN2606; AN2867 |
| Schematic/reference source | No custom schematic is verified for this part. Official NUCLEO-F103RB/MB1136 board schematics are reference-only after board revision check; Blue Pill schematics remain unverified community sources. |
| Verified features | ST product page identifies STM32F103C8 as medium-density STM32F1 Cortex-M3 class, 72 MHz, 64/128 Kbytes flash family range, 20 Kbytes SRAM family value, USB FS and CAN 2.0B family capabilities, 2.0 to 3.6 V supply range. Exact order-code/package details still need package table verification. |
| KiCad symbol candidates | `MCU_ST_STM32F1:STM32F103C8Tx` |
| KiCad footprint candidates | `Package_QFP:LQFP-48_7x7mm_P0.5mm` from KiCad symbol default; pad verification still required. |
| 3D model candidates | Unknown - requires source verification |
| Debug/programming notes | Provide SWDIO, SWCLK, NRST, GND, and target voltage. System bootloader interface support must be checked in AN2606 for this exact part. |
| Boot mode notes | BOOT0 handling must be explicit; do not copy Blue Pill boot jumpers without board revision review. |
| Clocking notes | HSE range and USB clock plan require datasheet/reference manual and AN2867 review. |
| Power/decoupling notes | Verify every VDD/VSS/VDDA/VSSA/VBAT pin for the LQFP48 package. |
| Common mistakes | Treating Blue Pill pin labels as the MCU pinout; assuming clone-board crystal, USB pull-up, or regulator choices are correct; forgetting SWD access. |
| Verification status | `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER` |

## STM32F401CCU6

| Field | Value |
| --- | --- |
| Record ID | `STMICRO_STM32F401CCU6` |
| Vendor | STMicroelectronics |
| Family | STM32F4 |
| Category | `01_MICROCONTROLLERS` |
| Source documents | ST product page: https://www.st.com/en/microcontrollers-microprocessors/stm32f401cc.html ; datasheet link: https://www.st.com/resource/en/datasheet/stm32f401cc.pdf ; AN4488; AN2606; AN2867; AN4879 |
| Schematic/reference source | No custom schematic is verified for this exact QFN/UFQFPN part. NUCLEO-F401RE/MB1136 references apply to the board MCU/package on that Nucleo and must not be treated as F401CCU6 package proof. |
| Verified features | ST product page identifies STM32F401CC as STM32F4 Cortex-M4 with DSP/FPU, 84 MHz CPU, 256 Kbytes flash, 1.7 to 3.6 V supply family range, USB 2.0 FS OTG capability in the family. Exact order-code package needs package table verification. |
| KiCad symbol candidates | `MCU_ST_STM32F4:STM32F401CCUx` |
| KiCad footprint candidates | `Package_DFN_QFN:QFN-48-1EP_7x7mm_P0.5mm_EP5.6x5.6mm` from KiCad symbol default; verify against ST UFQFPN/VFQFPN package drawing before layout. |
| 3D model candidates | Unknown - requires source verification |
| Debug/programming notes | SWD required for robust bring-up; confirm ST-LINK header voltage reference and NRST access. |
| Boot mode notes | Confirm BOOT0 and system memory bootloader interfaces in AN2606; do not assume F103 behavior. |
| Clocking notes | USB needs a verified clock plan; HSE and LSE crystal layout require AN2867. |
| Power/decoupling notes | Verify VDD/VDDA/VSSA/VBAT and exposed-pad handling for the package. |
| Common mistakes | Confusing F401CCU6 with F401RE Nucleo pinout; using Black Pill board assumptions as package proof. |
| Verification status | `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER` |

## STM32F411CEU6

| Field | Value |
| --- | --- |
| Record ID | `STMICRO_STM32F411CEU6` |
| Vendor | STMicroelectronics |
| Family | STM32F4 |
| Category | `01_MICROCONTROLLERS` |
| Source documents | ST product page: https://www.st.com/en/microcontrollers-microprocessors/stm32f411ce.html ; datasheet link: https://www.st.com/resource/en/datasheet/stm32f411ce.pdf ; AN4488; AN2606; AN2867; AN4879 |
| Schematic/reference source | No official complete custom-board schematic is verified for this exact part. Use only exact Black Pill board sources after vendor/revision verification, or choose an official ST F411 reference board before extracting circuits. |
| Verified features | ST product page identifies STM32F411 class as STM32F4 Cortex-M4 with DSP/FPU and USB 2.0 FS OTG family capability. Exact CEU6 package and memory details require datasheet/order-code table verification before use. |
| KiCad symbol candidates | `MCU_ST_STM32F4:STM32F411CEUx` |
| KiCad footprint candidates | `Package_DFN_QFN:QFN-48-1EP_7x7mm_P0.5mm_EP5.6x5.6mm` from KiCad symbol default; verify against exact ST package drawing. |
| 3D model candidates | Unknown - requires source verification |
| Debug/programming notes | SWD header strongly recommended; preserve PA13/PA14 debug function during bring-up. |
| Boot mode notes | Confirm BOOT0/system bootloader interfaces in AN2606 for F411CE. |
| Clocking notes | Black Pill boards often rely on an external crystal; custom designs must verify HSE frequency and USB clock plan from ST sources. |
| Power/decoupling notes | Verify all supplies, analog rails, VBAT, and exposed pad guidance. |
| Common mistakes | Assuming F401 and F411 Black Pill variants are schematic-identical; using community board pinouts as package proof. |
| Verification status | `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER` |

## STM32F405RGT6

| Field | Value |
| --- | --- |
| Record ID | `STMICRO_STM32F405RGT6` |
| Vendor | STMicroelectronics |
| Family | STM32F4 |
| Category | `01_MICROCONTROLLERS` |
| Source documents | ST product page: https://www.st.com/en/microcontrollers-microprocessors/stm32f405rg.html ; datasheet link: https://www.st.com/resource/en/datasheet/stm32f405rg.pdf ; AN4488; AN2606; AN2867; AN4879 |
| Schematic/reference source | No custom schematic is verified for this exact part. Official F4 Discovery/Nucleo references are block-level examples only after exact board revision and MCU package review. |
| Verified features | ST product page identifies STM32F405RG as active STM32F4 Cortex-M4 with DSP/FPU, 168 MHz CPU, 1 Mbyte flash product line, USB FS/HS family capability, classic CAN family capability, and 1.8 to 3.6 V family supply range. |
| KiCad symbol candidates | `MCU_ST_STM32F4:STM32F405RGTx` |
| KiCad footprint candidates | `Package_QFP:LQFP-64_10x10mm_P0.5mm` from KiCad symbol default; verify ST package drawing. |
| 3D model candidates | Unknown - requires source verification |
| Debug/programming notes | SWD/JTAG available in family; choose SWD for minimal custom boards unless trace/JTAG is required. |
| Boot mode notes | BOOT0 and supported ROM boot interfaces require AN2606 exact table. |
| Clocking notes | USB, CAN timing, and high-speed clock tree require reference manual review. |
| Power/decoupling notes | Larger F4 package means more power pins; verify all VDD/VSS/VDDA/VSSA/VBAT and decoupling locations. |
| Common mistakes | Treating any STM32F405RG symbol as valid for all package suffixes; omitting USB HS PHY/ULPI review when claiming HS USB. |
| Verification status | `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER` |

## STM32G030F6P6

| Field | Value |
| --- | --- |
| Record ID | `STMICRO_STM32G030F6P6` |
| Vendor | STMicroelectronics |
| Family | STM32G0 |
| Category | `01_MICROCONTROLLERS` |
| Source documents | ST product page: https://www.st.com/en/microcontrollers-microprocessors/stm32g030f6.html ; datasheet link: https://www.st.com/resource/en/datasheet/stm32g030f6.pdf ; AN2606; AN2867 |
| Schematic/reference source | No custom schematic or exact official board schematic has been verified for this low-pin-count part. Require exact ST evaluation-board or application-note source before copying circuits. |
| Verified features | ST product page identifies STM32G030F6 as active STM32G0 Cortex-M0+ value-line class with 32 Kbytes flash, 8 Kbytes RAM, 64 MHz CPU, and 2.0 to 3.6 V supply family range. |
| KiCad symbol candidates | `MCU_ST_STM32G0:STM32G030F6Px` |
| KiCad footprint candidates | `Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm` from KiCad symbol default; verify package drawing. |
| 3D model candidates | Unknown - requires source verification |
| Debug/programming notes | SWD is still required even on low-pin-count packages; reserve pins during bring-up. |
| Boot mode notes | G0 boot option behavior can differ from F1/F4; verify AN2606 and option bytes. |
| Clocking notes | Internal oscillator may be enough for many simple designs; exact timing and UART/USB requirements still require source verification. |
| Power/decoupling notes | Low pin count does not remove decoupling or VDDA/VSSA review. |
| Common mistakes | Spending SWD/boot pins on application IO with no recovery path; assuming F1 BOOT0 conventions. |
| Verification status | `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER` |

## STM32G431CBT6

| Field | Value |
| --- | --- |
| Record ID | `STMICRO_STM32G431CBT6` |
| Vendor | STMicroelectronics |
| Family | STM32G4 |
| Category | `01_MICROCONTROLLERS` |
| Source documents | ST product page: https://www.st.com/en/microcontrollers-microprocessors/stm32g431cb.html ; datasheet link: https://www.st.com/resource/en/datasheet/stm32g431cb.pdf ; AN2606; AN2867; AN4879 |
| Schematic/reference source | Official NUCLEO-G431RB/MB1367 schematic packs are verified board-level references for G431RB, not package proof for G431CBT6. Use only after matching circuit block, package, and board revision. |
| Verified features | ST product page identifies STM32G431CB as active STM32G4 Cortex-M4 with FPU/DSP, 170 MHz, 128 Kbytes flash, analog integration, one FDCAN, USB device, UCPD, and 1.71 to 3.6 V supply family range. |
| KiCad symbol candidates | `MCU_ST_STM32G4:STM32G431CBTx`, `MCU_ST_STM32G4:STM32G431CBTxZ` |
| KiCad footprint candidates | `Package_QFP:LQFP-48_7x7mm_P0.5mm` from KiCad symbol default; verify exact suffix and package drawing. |
| 3D model candidates | Unknown - requires source verification |
| Debug/programming notes | SWD/JTAG support appears in ST product summary; preserve SWD on prototypes. |
| Boot mode notes | Verify G4 system bootloader interfaces and BOOT0/option byte behavior in AN2606. |
| Clocking notes | Mixed-signal, USB, and FDCAN timing require a verified clock plan. |
| Power/decoupling notes | Treat VDD, VDDA, VSSA, VREF+, VBAT, analog peripherals, and high dV/dt layout carefully. |
| Common mistakes | Using FDCAN without a CAN FD transceiver; ignoring analog reference layout; copying Nucleo-G431RB pinout for CB package. |
| Verification status | `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER` |

## STM32H743VIT6

| Field | Value |
| --- | --- |
| Record ID | `STMICRO_STM32H743VIT6` |
| Vendor | STMicroelectronics |
| Family | STM32H7 |
| Category | `01_MICROCONTROLLERS` |
| Source documents | ST product page: https://www.st.com/en/microcontrollers-microprocessors/stm32h743vi.html ; datasheet link: https://www.st.com/resource/en/datasheet/stm32h743vi.pdf ; AN2606; AN2867; AN4879 |
| Schematic/reference source | Official NUCLEO-H743ZI/MB1364 schematic packs are verified historical board-level references. Check current replacement boards and do not use Nucleo circuitry as custom H743VIT6 package proof. |
| Verified features | ST product page identifies STM32H743VI as active Cortex-M7, 480 MHz, 2 Mbytes flash, 1 Mbyte RAM product line with multiple power domains, USB OTG, FDCAN, Ethernet, and high-performance peripherals. |
| KiCad symbol candidates | `MCU_ST_STM32H7:STM32H743VITx` |
| KiCad footprint candidates | `Package_QFP:LQFP-100_14x14mm_P0.5mm` from KiCad symbol default; verify ST package drawing and power pins. |
| 3D model candidates | Unknown - requires source verification |
| Debug/programming notes | SWD/JTAG and trace decisions should be made early; high-end debug connectors may be justified. |
| Boot mode notes | H7 boot/security/option behavior must be verified from AN2606, reference manual, and errata. |
| Clocking notes | H7 clock tree, PLLs, USB, Ethernet, SDRAM/external memory, and cache behavior need reference-manual review. |
| Power/decoupling notes | Do not use simple F1/F4 minimum circuits. Verify VCAP, regulator mode, independent domains, USB supply, and analog rails. |
| Common mistakes | Underestimating supply complexity; routing high-speed memory/USB/Ethernet casually; missing VCAP/regulator requirements. |
| Verification status | `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER` |

## STM32U575ZIT6 Representative U5 Placeholder

| Field | Value |
| --- | --- |
| Record ID | `STMICRO_STM32U5_REPRESENTATIVE_STM32U575ZIT6` |
| Vendor | STMicroelectronics |
| Family | STM32U5 |
| Category | `01_MICROCONTROLLERS` |
| Source documents | ST product page: https://www.st.com/en/microcontrollers-microprocessors/stm32u575zi.html ; datasheet link: https://www.st.com/resource/en/datasheet/stm32u575zi.pdf ; AN2606; AN2867; AN4879 |
| Schematic/reference source | Representative placeholder only. Select an exact STM32U5 Nucleo/Discovery/reference design and verify its schematic revision before extracting circuits. |
| Verified features | ST product page identifies STM32U575ZI as active STM32U5 Cortex-M33 with TrustZone, 160 MHz, 2 Mbytes flash. ST product quality table shows STM32U575ZIT6 in LQFP 144 20x20x1.4 mm and active status. |
| KiCad symbol candidates | `MCU_ST_STM32U5:STM32U575ZITx`, `MCU_ST_STM32U5:STM32U575ZITxQ` |
| KiCad footprint candidates | `Package_QFP:LQFP-144_20x20mm_P0.5mm` from KiCad symbol default; verify SMPS/non-SMPS order-code differences. |
| 3D model candidates | Unknown - requires source verification |
| Debug/programming notes | Preserve SWD and plan secure-debug policy before enabling security features. |
| Boot mode notes | Verify U5 boot/TrustZone/option-byte behavior from current ST documents. |
| Clocking notes | Low-power clocking and USB clocking require reference-manual review. |
| Power/decoupling notes | Verify SMPS versus non-SMPS order code, VCAP, power domains, and low-power leakage layout. |
| Common mistakes | Treating a representative U5 placeholder as a selected production part; mixing SMPS and non-SMPS variants. |
| Verification status | `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER` |

## STM32WB55RGV6 Representative WB Placeholder

| Field | Value |
| --- | --- |
| Record ID | `STMICRO_STM32WB_REPRESENTATIVE_STM32WB55RGV6` |
| Vendor | STMicroelectronics |
| Family | STM32WB |
| Category | `01_MICROCONTROLLERS` |
| Source documents | ST product page: https://www.st.com/en/microcontrollers-microprocessors/stm32wb55rg.html ; datasheet link: https://www.st.com/resource/en/datasheet/stm32wb55rg.pdf ; AN5434; AN5129; AN5165; AN2606 |
| Schematic/reference source | Representative placeholder only. Use NUCLEO-WB55RG or an exact ST RF reference design after schematic, matching network, antenna, and board revision verification. |
| Verified features | ST product page identifies STM32WB55RG as active ultra-low-power dual-core wireless MCU with Cortex-M4 application core, Cortex-M0+ radio layer, Bluetooth LE, IEEE 802.15.4, Zigbee/Thread/Matter context, USB, and RF companion documentation. ST quality table shows STM32WB55RGV6 in VFQFPN 68 8x8x1.0 mm. |
| KiCad symbol candidates | `MCU_ST_STM32WB:STM32WB55RGVx` |
| KiCad footprint candidates | `Package_DFN_QFN:QFN-68-1EP_8x8mm_P0.4mm_EP6.4x6.4mm` from KiCad symbol default; verify against ST VFQFPN package and RF layout notes. |
| 3D model candidates | Unknown - requires source verification |
| Debug/programming notes | SWD/JTAG for application processor; wireless stack and boot/update flow require ST WB docs. |
| Boot mode notes | Verify WB bootloader and wireless firmware update flow; do not treat like a simple F4. |
| Clocking notes | RF clocking, HSE/LSE, and wireless timing require WB-specific docs. |
| Power/decoupling notes | RF supply, matching/filter network, antenna/reference design, and low-power domains require dedicated review. |
| Common mistakes | Designing RF from generic STM32 rules; ignoring antenna/matching network; forgetting wireless firmware ownership. |
| Verification status | `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER` |
