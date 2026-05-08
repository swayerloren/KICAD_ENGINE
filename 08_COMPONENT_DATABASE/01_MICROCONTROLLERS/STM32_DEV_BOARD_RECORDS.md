# STM32 Dev Board Records

Date: 2026-05-02

Status: dev-board guidance for AI-assisted KiCad planning. Board records are reference-only and do not prove custom-board schematic or PCB correctness.

## Blue Pill STM32F103C8T6

| Field | Value |
| --- | --- |
| Record ID | `DEVBOARD_BLUE_PILL_STM32F103C8T6` |
| Source documents | Official MCU source: https://www.st.com/en/microcontrollers-microprocessors/stm32f103c8.html ; community board schematic link: Unknown - requires source verification |
| Schematic link | Unknown - requires source verification; Blue Pill has many clone revisions. |
| KiCad symbol candidates | Bare MCU candidate: `MCU_ST_STM32F1:STM32F103C8Tx`; board-level connector symbols depend on selected board revision. |
| KiCad footprint candidates | Bare MCU candidate: `Package_QFP:LQFP-48_7x7mm_P0.5mm`; board footprint unknown. |
| Debug/programming notes | Use SWD header if available; verify SWD header pinout and target voltage. |
| Boot mode notes | BOOT0 jumpers/buttons vary by board; verify exact board. |
| Clocking notes | Crystal frequency and loading vary by clone; verify against the exact schematic and AN2867. |
| Power/decoupling notes | On-board regulator quality and 5 V/3.3 V behavior are clone-dependent. |
| Common mistakes | Assuming Blue Pill pinout/schematic is official ST; trusting USB pull-up/regulator/crystal choices; ignoring counterfeit/clone MCU risk. |
| Verification status | `UNVERIFIED_PLACEHOLDER` |

## Black Pill STM32F401/STM32F411

| Field | Value |
| --- | --- |
| Record ID | `DEVBOARD_BLACK_PILL_STM32F401_STM32F411` |
| Source documents | Official MCU sources: https://www.st.com/en/microcontrollers-microprocessors/stm32f401cc.html ; https://www.st.com/en/microcontrollers-microprocessors/stm32f411ce.html ; community board schematic link: Unknown - requires source verification |
| Schematic link | Unknown - requires source verification; Black Pill variants differ by vendor, connector, MCU, crystal, and USB connector. |
| KiCad symbol candidates | `MCU_ST_STM32F4:STM32F401CCUx`; `MCU_ST_STM32F4:STM32F411CEUx` |
| KiCad footprint candidates | `Package_DFN_QFN:QFN-48-1EP_7x7mm_P0.5mm_EP5.6x5.6mm`; verify exact package. |
| Debug/programming notes | SWD is preferred; verify boot button, reset button, and USB boot path on exact board. |
| Boot mode notes | BOOT0/button behavior is board-specific. |
| Clocking notes | Do not assume F401 and F411 variants use identical HSE/LSE circuits. |
| Power/decoupling notes | USB power, regulator rating, and exposed pad/grounding are board-specific. |
| Common mistakes | Treating all Black Pills as pin-compatible; assuming USB-C boards implement USB-C correctly; copying community board circuits into products. |
| Verification status | `UNVERIFIED_PLACEHOLDER` |

## NUCLEO-F103RB

| Field | Value |
| --- | --- |
| Record ID | `DEVBOARD_ST_NUCLEO-F103RB` |
| Source documents | Official board page: https://www.st.com/en/evaluation-tools/nucleo-f103rb.html ; Nucleo docs: https://www.st.com/en/evaluation-tools/stm32-nucleo-boards/documentation.html ; UM1724; MB1136 schematic family |
| Schematic link | Official ST MB1136 C03 schematic observed: https://www.st.com/resource/en/schematic_pack/mb1136-default-c03_schematic.pdf ; ST product page also lists later MB1136 C04/C05 schematic resources. Match board revision before use. |
| KiCad symbol candidates | Board-level reference only; use bare MCU records for custom MCU symbols. |
| KiCad footprint candidates | Board-level reference only; not a custom-board footprint source. |
| Debug/programming notes | Integrated ST-LINK/V2-1 class debug/programmer on Nucleo-64 boards; verify board revision and jumpers. |
| Boot mode notes | Nucleo BOOT0/headers/solder bridges are board-specific. |
| Clocking notes | Use as reference only; custom F103 clock must follow datasheet and AN2867. |
| Power/decoupling notes | Nucleo power selection and ST-LINK USB power are board-specific. |
| Common mistakes | Using F103RB Nucleo as F103C8T6 package proof; copying ST-LINK section unnecessarily. |
| Verification status | `VERIFIED_FROM_VENDOR_REFERENCE_DESIGN`, `UNVERIFIED_PLACEHOLDER` |

## NUCLEO-F401RE

| Field | Value |
| --- | --- |
| Record ID | `DEVBOARD_ST_NUCLEO-F401RE` |
| Source documents | Official board page: https://www.st.com/en/evaluation-tools/nucleo-f401re.html ; Nucleo docs; UM1724; MB1136 schematic family |
| Schematic link | Official Nucleo-64 MB1136 schematic family reference; direct C03 schematic observed at https://www.st.com/resource/en/schematic_pack/mb1136-default-c03_schematic.pdf . Verify F401RE board revision and ST product CAD resources before copying circuits. |
| KiCad symbol candidates | Board-level reference only; use bare MCU records for custom MCU symbols. |
| KiCad footprint candidates | Board-level reference only. |
| Debug/programming notes | Integrated ST-LINK; includes Arduino/ST morpho expansion context. |
| Boot mode notes | Board jumpers and headers must be checked before copying. |
| Clocking notes | Do not infer F401CCU6 Black Pill clocking from F401RE Nucleo. |
| Power/decoupling notes | Nucleo regulator/power-source circuit is board-specific. |
| Common mistakes | Confusing F401RE LQFP64 Nucleo with F401CCU6 QFN/UFQFPN package. |
| Verification status | `VERIFIED_FROM_VENDOR_REFERENCE_DESIGN`, `UNVERIFIED_PLACEHOLDER` |

## NUCLEO-G431RB

| Field | Value |
| --- | --- |
| Record ID | `DEVBOARD_ST_NUCLEO-G431RB` |
| Source documents | Official board page: https://www.st.com/en/evaluation-tools/nucleo-g431rb.html ; Nucleo docs; UM1724; MB1367-G431RB schematic resources |
| Schematic link | Official ST schematic resources observed: https://www.st.com/resource/en/schematic_pack/mb1367-g431rb-c04_schematic.pdf and https://www.st.com/resource/en/schematic_pack/mb1367-g431rb-c05_schematic.pdf . Match board revision before use. |
| KiCad symbol candidates | Board-level reference only; use exact G4 MCU record for custom symbols. |
| KiCad footprint candidates | Board-level reference only. |
| Debug/programming notes | Integrated ST-LINK; verify whether ST-LINK, VCP, headers, and solder bridges affect target pins. |
| Boot mode notes | G4 boot behavior needs AN2606 and board jumper review. |
| Clocking notes | Useful G4 reference but custom USB/FDCAN timing still requires exact schematic and reference manual. |
| Power/decoupling notes | Mixed-signal analog pins and FDCAN/USB board options should be separated from MCU minimum circuit. |
| Common mistakes | Treating G431RB board circuitry as G431CBT6 package proof. |
| Verification status | `VERIFIED_FROM_VENDOR_REFERENCE_DESIGN`, `UNVERIFIED_PLACEHOLDER` |

## NUCLEO-H743ZI

| Field | Value |
| --- | --- |
| Record ID | `DEVBOARD_ST_NUCLEO-H743ZI` |
| Source documents | Official board page: https://www.st.com/en/evaluation-tools/nucleo-h743zi.html ; Nucleo-144 docs; MB1364-H743ZI schematic resources |
| Schematic link | Official ST schematic resources observed: https://www.st.com/resource/en/schematic_pack/mb1364-h743zi-c01_schematic.pdf and https://www.st.com/resource/en/schematic_pack/mb1364-h743zi-e01_schematic.pdf . Historical board reference only; check current replacement boards. |
| KiCad symbol candidates | Board-level reference only. |
| KiCad footprint candidates | Board-level reference only. |
| Debug/programming notes | H7 debug may need SWD/JTAG/trace decisions early; Nucleo ST-LINK section is reference-only. |
| Boot mode notes | H7 boot and option bytes require AN2606, reference manual, and errata. |
| Clocking notes | H7 clock tree is complex; board is a reference, not a shortcut. |
| Power/decoupling notes | Review H7 regulator/VCAP/power-domain implementation carefully. |
| Common mistakes | Starting a new design from NUCLEO-H743ZI without noting ST page marks it obsolete/out of production; ignoring current replacement boards. |
| Verification status | `VERIFIED_FROM_VENDOR_REFERENCE_DESIGN`, `UNVERIFIED_PLACEHOLDER` |

## Common Discovery Board Placeholder Records

| Field | Value |
| --- | --- |
| Record ID | `DEVBOARD_ST_DISCOVERY_COMMON_PLACEHOLDERS` |
| Source documents | STM32F4DISCOVERY: https://www.st.com/en/evaluation-tools/stm32f4discovery.html ; 32F746GDISCOVERY: https://www.st.com/en/evaluation-tools/32f746gdiscovery.html ; board selector: https://www.st.com/en/evaluation-tools/stm32-mcu-mpu-eval-tools.html |
| Schematic link | STM32F4DISCOVERY official schematic resources observed include https://www.st.com/resource/en/schematic_pack/mb997-f407vgt6-e01_schematic.pdf and https://www.st.com/resource/en/schematic_pack/mb997-f407vgt6-g01-schematic.pdf . 32F746GDISCOVERY schematic resources are listed on the official product page and must be selected by board revision. |
| KiCad symbol candidates | Board-level only; use exact MCU records for custom schematic symbols. |
| KiCad footprint candidates | Board-level only. |
| Debug/programming notes | Discovery boards often include ST-LINK plus rich peripherals; isolate only the circuit block needed. |
| Boot mode notes | Buttons, solder bridges, boot jumpers, and option headers are board-specific. |
| Clocking notes | Discovery boards often include multiple clock sources for MCU, audio, display, USB, or external memory. Do not copy without understanding. |
| Power/decoupling notes | Discovery boards include board-specific regulators, load switches, memories, and peripherals. |
| Common mistakes | Copying display/audio/USB/external memory circuits without checking exact MCU package and board revision. |
| Verification status | `UNVERIFIED_PLACEHOLDER` |
