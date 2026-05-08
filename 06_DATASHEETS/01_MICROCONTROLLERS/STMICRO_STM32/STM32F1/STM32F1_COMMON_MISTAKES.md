# STM32F1 Common Mistakes

Date: 2026-05-03
Status: `AI_REVIEW_CHECKLIST`

This file lists STM32F1 mistakes that Codex/Claude must check for when reviewing or planning KiCad schematics and PCBs.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact value checked in a named ST datasheet/reference document.
- `INFERRED_FROM_COMMON_DESIGN`: common mistake pattern; verify in the actual project.
- `UNVERIFIED`: not checked.
- `NEEDS_HUMAN_REVIEW`: must be reviewed before schematic/PCB/fab use.

## Schematic Mistakes

- `INFERRED_FROM_COMMON_DESIGN`: Missing BOOT0 default strap or recovery access.
- `INFERRED_FROM_COMMON_DESIGN`: Treating BOOT1/PB2 as a normal GPIO without checking boot-mode behavior.
- `INFERRED_FROM_COMMON_DESIGN`: No SWD header or no NRST/debug access.
- `INFERRED_FROM_COMMON_DESIGN`: Hidden power pins in the KiCad symbol causing incomplete or unclear power nets.
- `NEEDS_HUMAN_REVIEW`: VDDA/VSSA/VREF left floating, tied incorrectly, or undocumented.
- `NEEDS_HUMAN_REVIEW`: USB D+/D-, VBUS sense, pull-up/disconnect, ESD, and shield strategy copied from memory.
- `NEEDS_HUMAN_REVIEW`: Crystal and load capacitors chosen without AN2867 and crystal datasheet review.
- `UNVERIFIED`: Exact regulator/decoupling values copied from a dev board without checking the MCU and regulator datasheets.

## PCB Mistakes

- `NEEDS_HUMAN_REVIEW`: LQFP footprint selected by name only.
- `NEEDS_HUMAN_REVIEW`: Pin 1 orientation not cross-checked against ST package drawing and 3D model.
- `INFERRED_FROM_COMMON_DESIGN`: Decoupling capacitors placed too far from VDD/VSS pins.
- `INFERRED_FROM_COMMON_DESIGN`: Oscillator traces routed through noisy areas or with long stubs.
- `INFERRED_FROM_COMMON_DESIGN`: SWD header blocked mechanically after enclosure/connector placement.
- `NEEDS_HUMAN_REVIEW`: USB differential routing and connector shield strategy not reviewed.

## Blue Pill Mistakes

- `NEEDS_HUMAN_REVIEW`: Assuming a cheap Blue Pill has a genuine ST MCU.
- `NEEDS_HUMAN_REVIEW`: Assuming every Blue Pill variant uses the same USB resistor, regulator, boot jumpers, or crystal.
- `NEEDS_HUMAN_REVIEW`: Using Blue Pill as proof that a custom STM32F103C8T6 schematic is correct.

## Agent Rule

If any of these appear in a project review, mark the item `NEEDS_HUMAN_REVIEW` and block schematic-to-PCB promotion until resolved or formally accepted by the user.
