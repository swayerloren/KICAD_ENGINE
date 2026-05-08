# STM32 Research Status

Date: 2026-05-02

Workspace: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Scope Completed

Created or updated:

- `06_DATASHEETS\01_MICROCONTROLLERS\STMICRO_STM32\README.md`
- `06_DATASHEETS\01_MICROCONTROLLERS\STMICRO_STM32\STM32_MASTER_INDEX.md`
- `06_DATASHEETS\01_MICROCONTROLLERS\STMICRO_STM32\NUCLEO_BOARDS\NUCLEO_BOARD_INDEX.md`
- `06_DATASHEETS\01_MICROCONTROLLERS\STMICRO_STM32\DISCOVERY_BOARDS\DISCOVERY_BOARD_INDEX.md`
- `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\STM32_FAMILY_OVERVIEW.md`
- `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\STM32_PART_RECORDS.md`
- `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\stm32_part_records.json`
- `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\STM32_DEV_BOARD_RECORDS.md`
- `08_COMPONENT_DATABASE\13_DESIGN_RULE_SNIPPETS\STM32_POWER_DECOUPLING_RULES.md`
- `08_COMPONENT_DATABASE\13_DESIGN_RULE_SNIPPETS\STM32_BOOT_DEBUG_RULES.md`
- `08_COMPONENT_DATABASE\13_DESIGN_RULE_SNIPPETS\STM32_USB_RULES.md`
- `08_COMPONENT_DATABASE\13_DESIGN_RULE_SNIPPETS\STM32_CAN_FDCAN_RULES.md`
- `08_COMPONENT_DATABASE\00_INDEX\MASTER_COMPONENT_INDEX.md`

No datasheet PDFs were downloaded. No tools were installed. No KiCad project source files were edited.

## Repeat-Prompt Strengthening Pass

- Added official schematic-pack references for selected Nucleo and Discovery boards where direct ST resources were observed.
- Added explicit schematic/reference-source rows to each STM32 part record so agents do not confuse MCU product pages with reusable board schematics.
- Added `schematic_source_urls` arrays to the STM32 JSON records. Empty arrays mean no verified schematic source has been selected yet.
- Kept Blue Pill and Black Pill records as unverified community-board placeholders.

## Completed Families

| Family | Status | Notes |
| --- | --- | --- |
| STM32F0 | FAMILY_INDEXED | Official family page indexed; no individual F0 part record requested. |
| STM32F1 | PARTIAL_COMPLETE | Family guidance, STM32F103C8T6 record, NUCLEO-F103RB, and Blue Pill warning added. |
| STM32F3 | FAMILY_INDEXED | Mixed-signal family guidance added; no individual F3 part record requested. |
| STM32F4 | STRONG_INITIAL_COMPLETE | STM32F401CCU6, STM32F411CEU6, STM32F405RGT6, NUCLEO-F401RE, Black Pill, and Discovery references added. |
| STM32F7 | FAMILY_INDEXED | Family guidance and Discovery reference added; no bare F7 part record requested. |
| STM32G0 | PARTIAL_COMPLETE | STM32G030F6P6 record added. |
| STM32G4 | PARTIAL_COMPLETE | STM32G431CBT6 and NUCLEO-G431RB records added with FDCAN/analog warnings. |
| STM32H5 | FAMILY_INDEXED | Family guidance added; no individual H5 record requested. |
| STM32H7 | PARTIAL_COMPLETE | STM32H743VIT6 and NUCLEO-H743ZI records added; H7 power/clock risk called out. |
| STM32L0 | FAMILY_INDEXED | Low-power family guidance added. |
| STM32L4 | FAMILY_INDEXED | Low-power F4-class guidance added. |
| STM32L5 | FAMILY_INDEXED | Secure low-power family guidance added. |
| STM32U0 | FAMILY_INDEXED | Family guidance added; library maturity requires follow-up. |
| STM32U5 | PARTIAL_PLACEHOLDER | STM32U575ZIT6 representative placeholder added. |
| STM32WB | PARTIAL_PLACEHOLDER | STM32WB55RGV6 representative placeholder added with RF warnings. |
| STM32WL | FAMILY_INDEXED | Wireless/sub-GHz family guidance added; RF records need future work. |

## Part Records Created

- STM32F103C8T6
- STM32F401CCU6
- STM32F411CEU6
- STM32F405RGT6
- STM32G030F6P6
- STM32G431CBT6
- STM32H743VIT6
- STM32U575ZIT6 representative U5 placeholder
- STM32WB55RGV6 representative WB placeholder

## Dev Board Records Created

- Blue Pill STM32F103C8T6
- Black Pill STM32F401/STM32F411
- NUCLEO-F103RB
- NUCLEO-F401RE
- NUCLEO-G431RB
- NUCLEO-H743ZI
- Common Discovery board placeholder records

## Missing Documents Or Follow-Up Sources

- Exact reference manuals for each selected part should be linked and summarized.
- Exact errata sheets should be linked and summarized before design use.
- ST package drawings and land-pattern details need pad-by-pad footprint verification.
- Some official Nucleo and Discovery schematic-pack links are now indexed; full board-revision extraction and CAD/BOM package extraction still require a future pass.
- Blue Pill and Black Pill records need exact community board revision sources before any schematic-copy guidance can be trusted.
- STM32H5, STM32U0, STM32WL, STM32L families need representative part records if they become design targets.

## Uncertain Specs

- Exact package/order-code details remain verification-required except where explicitly noted from ST product pages or KiCad candidate data.
- KiCad stock library candidates were found by read-only name search only. They are not pad-verified or footprint-approved.
- STM32U5 SMPS versus non-SMPS variants require exact order-code handling.
- STM32WB RF network, antenna, certification, and stack/update requirements need deeper WB-specific research.
- NUCLEO-H743ZI official page was observed as obsolete/out of production; current replacement board research remains needed.

## Risk Areas

- False confidence from similar STM32 order codes and package suffixes.
- Community Blue Pill/Black Pill clone variance.
- BOOT0/option-byte assumptions copied across families.
- SWD pins consumed by application IO before recovery is proven.
- USB designs without CC, VBUS, clock, and ESD review.
- CAN/FDCAN pins connected without a transceiver and termination plan.
- Missing VDDA/VSSA/VREF+/VBAT/VCAP/SMPS power-domain handling.
- Copying Nucleo or Discovery board circuitry without separating ST-LINK, jumpers, solder bridges, and board peripherals.

## Next Research Needed

1. Extract exact reference manual and errata links for every recorded STM32 part.
2. Build pad-by-pad KiCad symbol/footprint verification checklists for each part.
3. Extract complete schematic/CAD/BOM resource sets for NUCLEO-F103RB, NUCLEO-F401RE, NUCLEO-G431RB, current H743 Nucleo replacement boards, STM32F4DISCOVERY, and 32F746GDISCOVERY.
4. Add STM32H5, STM32U0, STM32WL, and STM32L representative part records if they become target families.
5. Build RF-specific STM32WB/WL design snippets from official ST RF application notes.
6. Add a bootloader-interface matrix derived from AN2606 for the exact recorded parts.
