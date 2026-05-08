# STM32H7 Dev Board References

Date: 2026-05-03
Status: `PARTIALLY_RESEARCHED_SOURCE_LINKS`

This is a link-only board/source index. Board schematics are reference evidence, not permission to copy blindly and not proof for a different package.

## Dev Board And Schematic Links

| part_number | document_type | title | source_url | verification_status | notes |
| --- | --- | --- | --- | --- | --- |
| STM32_NUCLEO | dev_board_hub | STM32 Nucleo boards | https://www.st.com/en/evaluation-tools/stm32-nucleo-boards.html | OFFICIAL_SOURCE_LINK | Nucleo family hub. |
| STM32_NUCLEO_DOCS | dev_board_documentation_hub | STM32 Nucleo board documentation | https://www.st.com/en/evaluation-tools/stm32-nucleo-boards/documentation.html | OFFICIAL_SOURCE_LINK | Use to find exact board manuals/schematics. |
| STM32_DISCOVERY | dev_board_hub | STM32 Discovery kits | https://www.st.com/en/evaluation-tools/stm32-discovery-kits.html | OFFICIAL_SOURCE_LINK | Discovery kit family hub. |
| STM32_EVAL | dev_board_hub | STM32 MCU eval boards | https://www.st.com/en/evaluation-tools/stm32-mcu-eval-boards.html | OFFICIAL_SOURCE_LINK | Official STM32 eval board hub. |
| NUCLEO-H743ZI | official_board_product_page | NUCLEO-H743ZI official board page | https://www.st.com/en/evaluation-tools/nucleo-h743zi.html | OFFICIAL_SOURCE_LINK | Official ST page observed; status may be obsolete/out-of-production; verify replacement before new work. |
| MB1364-H743ZI-C01 | official_board_schematic_pack | MB1364-H743ZI-C01 board schematic | https://www.st.com/resource/en/schematic_pack/mb1364-h743zi-c01_schematic.pdf | OFFICIAL_SOURCE_LINK | Link-only schematic pack; match exact board revision. |
| MB1364-H743ZI-E01 | official_board_schematic_pack | MB1364-H743ZI-E01 board schematic | https://www.st.com/resource/en/schematic_pack/mb1364-h743zi-e01_schematic.pdf | OFFICIAL_SOURCE_LINK | Link-only schematic pack; match exact board revision. |

## Board Use Rules

- Match exact board name and revision before extracting circuits.
- Do not treat dev board schematic packs as proof of custom-board footprint correctness.
- Record ST-LINK, power muxes, solder bridges, crystals, jumpers, protection, external transceivers, and connector orientation before reuse.
- Keep ST schematic packs link-only unless redistribution permission is confirmed.
