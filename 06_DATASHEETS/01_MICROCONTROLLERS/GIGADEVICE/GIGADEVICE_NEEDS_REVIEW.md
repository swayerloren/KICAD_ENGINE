# GIGADEVICE Needs Review

Date: 2026-05-03
Status: `OPEN_REVIEW_BACKLOG`

This is the blocker list for promoting `GIGADEVICE` content beyond planning.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public source URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact value checked in a named datasheet/reference document.
- `INFERRED_FROM_COMMON_DESIGN`: common design pattern; verify before use.
- `UNVERIFIED`: not checked against source evidence.
- `NEEDS_HUMAN_REVIEW`: must be reviewed before schematic, PCB, BOM, or fabrication use.

## Open Blockers

| Blocker | Status | Required Evidence |
| --- | --- | --- |
| exact representative part datasheet | `NEEDS_HUMAN_REVIEW` | official vendor datasheet for `GIGADEVICE-REPRESENTATIVE_PART_REQUIRES_SOURCE` |
| package/order-code mapping | `NEEDS_HUMAN_REVIEW` | official package table and drawing |
| symbol pinout audit | `NEEDS_HUMAN_REVIEW` | KiCad symbol compared to datasheet pin table |
| footprint audit | `NEEDS_HUMAN_REVIEW` | KiCad footprint compared to package drawing |
| boot/debug behavior | `NEEDS_HUMAN_REVIEW` | reference manual/application note |
| power/clock/reset design | `NEEDS_HUMAN_REVIEW` | datasheet and hardware app note |
| errata | `UNVERIFIED` | official errata source |

## Rule For KiCad Projects

Any project using `GIGADEVICE-REPRESENTATIVE_PART_REQUIRES_SOURCE` must keep schematic-to-PCB promotion blocked until required reviews are complete or explicitly accepted by a human.
