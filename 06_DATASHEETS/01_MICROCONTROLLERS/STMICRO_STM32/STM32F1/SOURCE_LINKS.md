# STM32F1 Source Links

Date: 2026-05-03
Status: `PARTIALLY_RESEARCHED_SOURCE_LINKS`

This is a link-only official/public source index. It does not bundle ST PDFs and does not prove part-level schematic or footprint correctness.

Pilot-specific STM32F103C8T6-focused source links are also tracked in `STM32F1_SOURCE_LINKS.md`.

## Source Link Table

| document_type | part_number | title | source_url | verification_status | redistribution_status | notes |
| --- | --- | --- | --- | --- | --- | --- |
| portfolio_page | ALL_STM32 | STM32 32-bit Arm Cortex MCUs official portfolio | https://www.st.com/en/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus.html | OFFICIAL_SOURCE_LINK | PUBLIC_LINK_ONLY | Official ST portfolio starting point. Use exact product pages for part-level work. |
| application_note | ALL_STM32 | AN2606 STM32 microcontroller system memory boot mode | https://www.st.com/resource/en/application_note/an2606-stm32-microcontroller-system-memory-boot-mode-stmicroelectronics.pdf | OFFICIAL_SOURCE_LINK | LINK_ONLY_DO_NOT_BUNDLE_PDF | Official ST bootloader/boot-mode reference. Link only; do not bundle PDF unless redistribution is reviewed. |
| application_note | ALL_STM32 | AN2867 oscillator design guide for STM8AF/STM8AL/S and STM32 MCUs and MPUs | https://www.st.com/resource/en/application_note/an2867-oscillator-design-guide-for-stm8afals-stm32-mcus-and-mpus-stmicroelectronics.pdf | OFFICIAL_SOURCE_LINK | LINK_ONLY_DO_NOT_BUNDLE_PDF | Official ST oscillator/crystal guidance. Verify selected crystal and board layout separately. |
| application_note | ALL_STM32 | AN4879 introduction to USB hardware and PCB guidelines using STM32 MCUs | https://www.st.com/resource/en/application_note/an4879-introduction-to-usb-hardware-and-pcb-guidelines-using-stm32-mcus-stmicroelectronics.pdf | OFFICIAL_SOURCE_LINK | LINK_ONLY_DO_NOT_BUNDLE_PDF | Official ST USB hardware/layout guidance. Use only when exact part supports required USB function. |
| debug_programming_hub | ST-LINK | STM32 programming and hardware development tools | https://www.st.com/en/development-tools/hardware-debugger-and-programmer-tools-for-stm32.html | OFFICIAL_SOURCE_LINK | PUBLIC_LINK_ONLY | Official ST hardware debug/programming tools page. |
| planning_tool | STM32CubeMX | STM32CubeMX official configuration and code-generation tool | https://www.st.com/en/development-tools/stm32cubemx.html | OFFICIAL_SOURCE_LINK | PUBLIC_LINK_ONLY | Use as planning aid only. It does not replace datasheet/reference-manual verification. |
| family_page | STM32F1 | STM32F1 official family page | https://www.st.com/en/microcontrollers-microprocessors/stm32f1-series.html | OFFICIAL_SOURCE_LINK | PUBLIC_LINK_ONLY | Official ST family landing page. |
| datasheet_index | STM32F1 | STM32F1 datasheet index via official family documentation | https://www.st.com/en/microcontrollers-microprocessors/stm32f1-series.html | NEEDS_REVIEW | PUBLIC_LINK_ONLY | Exact datasheet links must be selected per part/order code. |
| reference_manual_index | STM32F1 | STM32F1 reference manual index via official family documentation | https://www.st.com/en/microcontrollers-microprocessors/stm32f1-series.html | NEEDS_REVIEW | PUBLIC_LINK_ONLY | Exact reference manual links must be selected per subfamily/part. |
| errata_index | STM32F1 | STM32F1 errata index via official family documentation | https://www.st.com/en/microcontrollers-microprocessors/stm32f1-series.html | NEEDS_REVIEW | PUBLIC_LINK_ONLY | Exact errata sheet must be selected per part/subfamily. |
| application_note_index | STM32F1 | STM32F1 application notes via official family documentation | https://www.st.com/en/microcontrollers-microprocessors/stm32f1-series.html | NEEDS_REVIEW | PUBLIC_LINK_ONLY | Use official Documentation tab; do not infer app-note applicability. |
| datasheet | STM32F103C8 | STM32F103C8 datasheet | https://www.st.com/resource/en/datasheet/stm32f103c8.pdf | OFFICIAL_SOURCE_LINK | LINK_ONLY_DO_NOT_BUNDLE_PDF | Official ST datasheet URL from existing repo STM32 master index. Link-only; do not bundle PDF. |

## Use Rules

- Use `OFFICIAL_SOURCE_LINK` rows as starting points, not final design approval.
- Use `NEEDS_REVIEW` rows to find exact part-level documents before schematic or footprint work.
- Do not download or redistribute PDFs unless redistribution rights are confirmed.
- Exact voltage, current, pinout, package, and errata values remain `UNKNOWN_REQUIRES_SOURCE` until extracted from the exact source.
