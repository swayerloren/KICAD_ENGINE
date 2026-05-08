# Net Naming Pattern

Status: `DESIGN_PATTERN_REQUIRES_PROJECT_ADOPTION`

## Purpose

Use net names that make ERC, DRC, BOM review, visual review, and human debugging easier. Net names are part of project intent; changing them after a schematic exists can change connectivity and must be reviewed.

## Recommended Naming Rules

| Net Type | Pattern | Examples |
| --- | --- | --- |
| Raw input power | Source plus voltage | `USB_VBUS_5V`, `VIN_12V`, `BARREL_VIN` |
| Protected/fused power | Protection state plus voltage | `5V_FUSED`, `5V_PROTECTED`, `VBUS_PROTECTED` |
| Regulated rails | Voltage only when unambiguous | `3V3`, `1V8`, `5V_SYS` |
| Differential pairs | `_P` and `_N` suffixes or interface convention | `USB_D_P`, `USB_D_N`, `CANH`, `CANL` |
| MCU reset/boot/debug | Function, not package pin | `MCU_NRST`, `MCU_BOOT0`, `SWDIO`, `SWCLK` |
| Enables/resets | Active-low suffix when applicable | `REG_EN`, `SENSOR_RESET_N` |
| Test points | Target net name plus test role | `TP_3V3`, `TP_SWDIO`, `TP_UART_TX` |

## Agent Rules

- Do not use vague names such as `SIG1`, `GPIO2`, or `CONN_PIN_3` for important nets unless still in planning.
- Do not rename nets just for style after a design exists without a diff/review plan.
- Keep hierarchical labels consistent across sheets.
- Mark uncertain names as `PLANNING_PLACEHOLDER`.
- Preserve project standards when project memory defines rail names.
- Avoid mixing raw, fused, protected, and regulated rails under one name.

## Required Before PCB Gate

- Power rail names match the BOM lock and project design rules.
- USB, CAN, RF, debug, boot, reset, enable, and external connector nets are human-readable.
- Active-low signal naming matches symbol pin intent and datasheet polarity.
- Any intentional aliasing is documented.

## Stop Conditions

Stop and ask for review if a proposed rename could merge or split power rails, change connector pin intent, alter USB/CAN differential pairs, or contradict the BOM/project memory.
