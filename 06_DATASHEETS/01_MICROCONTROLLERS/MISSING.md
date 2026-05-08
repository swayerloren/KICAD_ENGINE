# 01_MICROCONTROLLERS Missing Documents

Date: 2026-05-03
Status: `OPEN_RESEARCH_BACKLOG`

Use family-level `*_NEEDS_REVIEW.md` files for detailed backlogs. This root file tracks the cross-family evidence classes that must be filled before AI agents can make strong schematic, PCB, footprint, or BOM claims.

| Priority | Needed Evidence | Applies To | Reason Needed | Status |
| --- | --- | --- | --- | --- |
| High | official product pages and datasheets | all generated families | exact part identity, electrical limits, package, pinout | `NEEDS_RESEARCH` |
| High | reference manuals or programming guides | MCU families with complex boot/debug/peripheral behavior | boot, clocks, debug, USB/CAN/RF/peripheral behavior | `NEEDS_RESEARCH` |
| High | package drawings | every exact orderable part | footprint verification | `NEEDS_RESEARCH` |
| High | errata | every exact orderable part/family | known silicon and documentation limitations | `NEEDS_RESEARCH` |
| Medium | official hardware design guides and application notes | minimum-system and layout-sensitive families | source-backed schematic and PCB checklist content | `NEEDS_RESEARCH` |
| Medium | official dev-board/reference design links | boards used as examples | evidence for circuit patterns, not automatic approval | `NEEDS_RESEARCH` |
| Medium | KiCad symbol/footprint candidate inventory | every exact part | candidate search only; not verification | `NEEDS_RESEARCH` |
