# {family} Needs Review

Date: {date}
Status: `OPEN_REVIEW_BACKLOG`

This is the blocker list for promoting `{family}` content beyond planning.

## Evidence Labels

{evidence_labels}

## Open Blockers

| Blocker | Status | Required Evidence |
| --- | --- | --- |
| exact representative part datasheet | `NEEDS_HUMAN_REVIEW` | official vendor datasheet for `{representative_part}` |
| package/order-code mapping | `NEEDS_HUMAN_REVIEW` | official package table and drawing |
| symbol pinout audit | `NEEDS_HUMAN_REVIEW` | KiCad symbol compared to datasheet pin table |
| footprint audit | `NEEDS_HUMAN_REVIEW` | KiCad footprint compared to package drawing |
| boot/debug behavior | `NEEDS_HUMAN_REVIEW` | reference manual/application note |
| power/clock/reset design | `NEEDS_HUMAN_REVIEW` | datasheet and hardware app note |
| errata | `UNVERIFIED` | official errata source |

## Rule For KiCad Projects

Any project using `{representative_part}` must keep schematic-to-PCB promotion blocked until required reviews are complete or explicitly accepted by a human.
