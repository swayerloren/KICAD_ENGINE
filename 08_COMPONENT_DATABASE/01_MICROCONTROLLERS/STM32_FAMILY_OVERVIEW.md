# STM32 Family Overview

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

This component-database overview links the STM32 component intelligence layer to the expanded STM32 datasheet tree. It is family-level guidance only. Exact part records must use official ST source links and package drawings.

## Source Baseline

- STM32 AI master index: `06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32_AI_MASTER_INDEX.md`
- STM32 legacy master index: `06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32_MASTER_INDEX.md`
- Official STM32 portfolio: https://www.st.com/en/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus.html
- STM32CubeMX planning tool: https://www.st.com/en/development-tools/stm32cubemx.html

## Family Selection Matrix

| Family | Family-Level Purpose | Design Watch Items | Datasheet Tree Link | Verification |
| --- | --- | --- | --- | --- |
| STM32F0 | Entry-level STM32 MCU family for cost-sensitive control, simple mixed-signal IO, and compact embedded products. | low cost, pin multiplexing limits, simple SWD access, package-specific USB/CAN availability | [STM32F0 docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32F0/FAMILY_OVERVIEW.md) | SCAFFOLDED_WITH_AI_SUMMARIES |
| STM32F1 | Mature mainstream STM32 family used in many legacy and prototype designs. | legacy ecosystem, Blue Pill clone risk, BOOT0/recovery access, SWD pins not overloaded | [STM32F1 docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32F1/FAMILY_OVERVIEW.md) | SCAFFOLDED_WITH_AI_SUMMARIES |
| STM32F2 | Higher-performance Cortex-M3 STM32 family bridging older F1-class designs and later F4/F7 families. | legacy high-performance supply domains, USB/Ethernet clocking, larger package footprints, external memory or PHY routing | [STM32F2 docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32F2/FAMILY_OVERVIEW.md) | SCAFFOLDED_WITH_AI_SUMMARIES |
| STM32F3 | Mixed-signal STM32 family for motor control, analog-heavy control loops, and precision sensing designs. | analog partitioning, VREF and VDDA filtering, comparator/op-amp pin mapping, motor-control noise containment | [STM32F3 docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32F3/FAMILY_OVERVIEW.md) | SCAFFOLDED_WITH_AI_SUMMARIES |
| STM32F4 | Mature performance STM32 family for general embedded control, USB, classic CAN, audio, and high-speed MCU designs. | clock tree, USB clock and routing, BOOT0 recovery path, package suffix and footprint matching | [STM32F4 docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32F4/FAMILY_OVERVIEW.md) | SCAFFOLDED_WITH_AI_SUMMARIES |
| STM32F7 | High-performance STM32 family for graphics, audio, external memory, Ethernet, and complex embedded applications. | cache-aware firmware implications, external memory layout, USB HS PHY decisions, Ethernet/RMII/MII constraints | [STM32F7 docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32F7/FAMILY_OVERVIEW.md) | SCAFFOLDED_WITH_AI_SUMMARIES |
| STM32G0 | Modern value-line STM32 family for compact, cost-sensitive control with current ecosystem support. | low-pin-count pin conflicts, SWD access preservation, BOOT behavior differences from F1, modern small packages | [STM32G0 docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32G0/FAMILY_OVERVIEW.md) | SCAFFOLDED_WITH_AI_SUMMARIES |
| STM32G4 | Mixed-signal STM32 family for motor control, digital power, FDCAN, USB, and fast analog control loops. | analog and power ground partitioning, FDCAN transceiver/protection, USB/UCPD pins on variants, switching-noise containment | [STM32G4 docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32G4/FAMILY_OVERVIEW.md) | SCAFFOLDED_WITH_AI_SUMMARIES |
| STM32H5 | Modern secure STM32 family for connected products needing stronger security and mid/high performance. | TrustZone/security lifecycle, debug authentication/recovery, power domain details, newer library support | [STM32H5 docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32H5/FAMILY_OVERVIEW.md) | SCAFFOLDED_WITH_AI_SUMMARIES |
| STM32H7 | High-end STM32 family for performance-heavy control, graphics, Ethernet, USB HS, external memory, and complex boards. | complex power tree, VCAP/SMPS/LDO mode, impedance-controlled interfaces, external memory and cache effects | [STM32H7 docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32H7/FAMILY_OVERVIEW.md) | SCAFFOLDED_WITH_AI_SUMMARIES |
| STM32L0 | Ultra-low-power STM32 family for battery sensors, low-duty-cycle products, and RTC-centric nodes. | leakage budgeting, LSE/RTC layout, VBAT behavior, low-power pin states | [STM32L0 docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32L0/FAMILY_OVERVIEW.md) | SCAFFOLDED_WITH_AI_SUMMARIES |
| STM32L1 | Legacy ultra-low-power STM32 family for low-power control and LCD/sensor products. | low-power leakage, LCD pin multiplexing, VBAT/backup domain, legacy lifecycle review | [STM32L1 docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32L1/FAMILY_OVERVIEW.md) | SCAFFOLDED_WITH_AI_SUMMARIES |
| STM32L4 | Ultra-low-power performance STM32 family for battery products needing more compute and richer peripherals. | low-power clock tree, USB clocking, analog rail filtering, package-specific pin conflicts | [STM32L4 docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32L4/FAMILY_OVERVIEW.md) | SCAFFOLDED_WITH_AI_SUMMARIES |
| STM32L5 | Secure ultra-low-power STM32 family for connected products needing TrustZone-class isolation. | TrustZone configuration, debug recovery, secure boot policy, low-power domains | [STM32L5 docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32L5/FAMILY_OVERVIEW.md) | SCAFFOLDED_WITH_AI_SUMMARIES |
| STM32U0 | Newer low-power entry STM32 family for compact products needing current ST ecosystem support. | newer library support, low-power modes, small packages, exact boot/debug behavior | [STM32U0 docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32U0/FAMILY_OVERVIEW.md) | SCAFFOLDED_WITH_AI_SUMMARIES |
| STM32U5 | Modern ultra-low-power STM32 family for secure, battery-powered, high-integration products. | SMPS versus LDO order codes, TrustZone/debug policy, low-power measurement design, complex power pins | [STM32U5 docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32U5/FAMILY_OVERVIEW.md) | SCAFFOLDED_WITH_AI_SUMMARIES |
| STM32WB | Wireless STM32 family for BLE and IEEE 802.15.4-class products where integrated radio is required. | RF matching, antenna keepout, HSE/LSE clock source, wireless stack and certification | [STM32WB docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32WB/FAMILY_OVERVIEW.md) | SCAFFOLDED_WITH_AI_SUMMARIES |
| STM32WL | Sub-GHz wireless STM32 family for LoRa and other regional low-power wide-area radio products where supported. | regional RF compliance, matching network, antenna/feedline layout, reference design fidelity | [STM32WL docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32WL/FAMILY_OVERVIEW.md) | SCAFFOLDED_WITH_AI_SUMMARIES |
| STM32MP | Linux-capable STM32 MPU family for application processors with DDR, PMIC, high-speed interfaces, and complex board design. | DDR layout, PMIC sequencing, BGA escape, Linux boot chain, reference design dependency | [STM32MP docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32MP/FAMILY_OVERVIEW.md) | SCAFFOLDED_WITH_AI_SUMMARIES |

## Component Database Rules

- Create exact part records before schematic use.
- Candidate KiCad symbols and footprints must be attached to exact package/order-code records, not only family names.
- Use `UNKNOWN_REQUIRES_SOURCE` for unverified voltage, current, clock, package, pinout, errata, lifecycle, and footprint data.
- Set `human_review_required: true` for every unverified package, connector, RF, USB, CAN/FDCAN, BGA, WLCSP, or power-domain decision.

## Current Classification

`SCAFFOLDED_WITH_AI_SUMMARIES`

This is not a complete STM32 database.
