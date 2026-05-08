# STM32F1 Common Part Numbers

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

This is a pilot index of common STM32F1 part-number families for AI planning. It is not a complete product selector and does not approve any specific BOM entry.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact value checked in a named ST datasheet/reference document.
- `INFERRED_FROM_COMMON_DESIGN`: common use pattern; verify before use.
- `UNVERIFIED`: not checked.
- `NEEDS_HUMAN_REVIEW`: must be reviewed before schematic/PCB use.

## Common Family Groups

| Group | Example Parts | Typical AI Use | Evidence Status | Review Needed |
| --- | --- | --- | --- | --- |
| STM32F103C8 | STM32F103C8T6, STM32F103C8T6TR, STM32F103C8T7TR | Blue Pill-class designs, low-cost USB/CAN-capable MCU experiments | `VERIFIED_SOURCE_LINK` for ST product page | Exact ordering code, package, lifecycle, and supplier status. |
| STM32F103CB | STM32F103CBTx variants | Same family with larger memory options than C8 class, exact details require source review | `UNVERIFIED` | Check ST product selector and datasheet. |
| STM32F103RB | STM32F103RBTx variants | NUCLEO-F103RB and LQFP64-class reference work | `VERIFIED_SOURCE_LINK` for NUCLEO-F103RB page | Check exact package and pin count. |
| STM32F103RE/VE/ZE | larger F103 variants | More pins/peripherals or package options | `UNVERIFIED` | Check exact package, power pins, and reference schematic. |
| STM32F100 | value-line variants | Legacy value-line work | `VERIFIED_SOURCE_LINK` at family level | Do not infer F103 USB/CAN behavior. |
| STM32F101/F102 | access/USB lines | Legacy designs with different peripheral support | `VERIFIED_SOURCE_LINK` at family level | Check exact product page. |
| STM32F105/F107 | connectivity line | Ethernet/USB/CAN designs | `VERIFIED_SOURCE_LINK` at family level | Use connectivity-line docs, not F103-only assumptions. |

## Part-Number Rules For Agents

- Do not shorten `STM32F103C8T6` to `STM32F103C8` in a BOM unless the BOM explicitly tracks orderable suffix separately.
- Do not assume `T6` maps to a package without checking the ST datasheet/order-code table.
- Do not treat `TR` tape-and-reel suffix as a different silicon part without source review.
- Do not treat Blue Pill board labels as proof of genuine ST silicon.
- Do not assume C8, CB, RB, RC, RE, VE, or ZE parts share pinout-compatible footprints without checking package and pinout.
