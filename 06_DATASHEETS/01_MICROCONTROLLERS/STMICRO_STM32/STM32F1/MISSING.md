# STM32F1 Missing Documents And Review Backlog

Date: 2026-05-03

Use this file to track STM32F1 documents and evidence still needed before KiCad Engine can treat a schematic, symbol, footprint, or PCB decision as verified.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: source URL exists.
- `VERIFIED_FROM_DATASHEET`: exact document content has been checked.
- `INFERRED_FROM_COMMON_DESIGN`: common practice, not approval.
- `UNVERIFIED`: no evidence yet.
- `NEEDS_HUMAN_REVIEW`: must be reviewed by an engineer.

| Priority | Part / Topic | Needed Document / Evidence | Reason Needed | Candidate Source | Status |
| --- | --- | --- | --- | --- | --- |
| High | STM32F103C8T6 | exact ST datasheet revision and package drawing section | Confirm package suffix, pinout, electrical limits, oscillator limits, ADC/VDDA rules, USB pins, and package dimensions. | ST product page datasheet link | `NEEDS_HUMAN_REVIEW` |
| High | STM32F103C8T6 | RM0008 sections for boot pins, AFIO/SWD/JTAG, clocks, USB, CAN, and reset behavior | Avoid wrong BOOT0/BOOT1, SWD remap, and peripheral pin assumptions. | ST RM0008 reference manual | `NEEDS_HUMAN_REVIEW` |
| High | STM32F103C8T6 | AN2586 hardware checklist sections | Confirm minimum schematic and board-level hardware guidance. | ST AN2586 | `NEEDS_HUMAN_REVIEW` |
| High | STM32F103C8T6 | exact KiCad symbol pin audit | Installed symbol exists, but pin numbers/names/electrical types must be checked against the exact datasheet. | local KiCad 9 library and ST datasheet | `NEEDS_HUMAN_REVIEW` |
| High | STM32F103C8T6 | exact KiCad LQFP-48 footprint/package drawing audit | Installed footprint exists, but dimensions, pin 1, courtyard, pad geometry, and 3D model alignment are not approved. | local KiCad 9 footprint and ST package drawing | `NEEDS_HUMAN_REVIEW` |
| Medium | STM32F103C8T6 | ST errata sheet | Avoid known silicon/peripheral limitations before design lock. | ST documentation page | `UNVERIFIED` |
| Medium | Blue Pill references | exact board revision and schematic source for the user's board | Blue Pill variants differ and may use clone MCUs or different passives. | STM32-base and user-provided board evidence | `NEEDS_HUMAN_REVIEW` |
| Medium | USB design | AN4879 and STM32F103 USB reference manual sections | Confirm VBUS sensing, pull-up/disconnect behavior, ESD, routing, and clock requirements for the exact design. | ST AN4879, RM0008, datasheet | `NEEDS_HUMAN_REVIEW` |
| Medium | oscillator design | AN2867 and exact crystal datasheet | Select crystal, load capacitors, drive level, and layout. | ST AN2867 and crystal vendor docs | `NEEDS_HUMAN_REVIEW` |
