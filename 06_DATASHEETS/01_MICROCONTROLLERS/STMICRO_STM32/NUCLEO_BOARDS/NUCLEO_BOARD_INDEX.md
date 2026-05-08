# STM32 Nucleo Board Index

Date: 2026-05-02

Status: official ST board-link index. Board pages and user manuals are references, not drop-in custom schematic proof.

## Official Source Baseline

- STM32 Nucleo documentation: https://www.st.com/en/evaluation-tools/stm32-nucleo-boards/documentation.html
- Nucleo-64 user manual UM1724: https://www.st.com/resource/en/user_manual/um1724-stm32-nucleo64-boards-mb1136-stmicroelectronics.pdf

## Boards In This Pass

| Board | ST Status Observed | MCU | Official URL | Agent Use | Do Not Use For |
| --- | --- | --- | --- | --- | --- |
| NUCLEO-F103RB | Active | STM32F103RB | https://www.st.com/en/evaluation-tools/nucleo-f103rb.html | F1 Nucleo-64 ST-LINK, headers, power, reset, and boot reference. | STM32F103C8T6 Blue Pill proof or C8 package proof. |
| NUCLEO-F401RE | Active | STM32F401RE | https://www.st.com/en/evaluation-tools/nucleo-f401re.html | F4 Nucleo-64 ST-LINK and Arduino/ST morpho reference. | STM32F401CCU6 Black Pill footprint proof. |
| NUCLEO-G431RB | Active | STM32G431RB | https://www.st.com/en/evaluation-tools/nucleo-g431rb.html | G4 Nucleo-64 reference with analog, FDCAN, USB, and board option context. | Exact STM32G431CBT6 package/pinout proof. |
| NUCLEO-H743ZI | Obsolete / out of production page observed | STM32H743ZI | https://www.st.com/en/evaluation-tools/nucleo-h743zi.html | Historical H743 Nucleo-144 reference; useful for ST-LINK and high-pin-count power/clock examples. | New board selection without checking current replacement boards such as NUCLEO-H743ZI2 or NUCLEO-H753ZI. |

## Official Schematic Pack References

These are official ST schematic-pack resources or official product-page resource names. Select the schematic that matches the physical board revision before using it.

| Board | Official Schematic Resource Evidence |
| --- | --- |
| NUCLEO-F103RB | ST product page lists MB1136-DEFAULT-C03, MB1136-DEFAULT-C04, and MB1136-DEFAULT-C05 board schematic PDFs. Direct C03 resource observed: https://www.st.com/resource/en/schematic_pack/mb1136-default-c03_schematic.pdf |
| NUCLEO-F401RE | Shares the Nucleo-64 MB1136 schematic family for board-revision-specific default schematics; verify exact F401RE board revision on ST product CAD resources before use. |
| NUCLEO-G431RB | ST product page lists MB1367-G431RB-C04 and MB1367-G431RB-C05 board schematic PDFs. Direct resources observed: https://www.st.com/resource/en/schematic_pack/mb1367-g431rb-c04_schematic.pdf and https://www.st.com/resource/en/schematic_pack/mb1367-g431rb-c05_schematic.pdf |
| NUCLEO-H743ZI | ST product page lists MB1364-H743ZI-C01 and MB1364-H743ZI-E01 board schematic PDFs. Direct resources observed: https://www.st.com/resource/en/schematic_pack/mb1364-h743zi-c01_schematic.pdf and https://www.st.com/resource/en/schematic_pack/mb1364-h743zi-e01_schematic.pdf |

## AI Handling Rules

- Treat Nucleo schematics as educational references.
- Separate ST-LINK, board power, jumpers, solder bridges, and Arduino/ST morpho headers from the target MCU minimum circuit.
- Verify whether SWD pins are shared with headers and whether the ST-LINK section is still attached.
- Confirm board revision and user manual revision before copying any detail.
- Do not infer bare MCU package, pin count, or footprint from a different Nucleo part number.
