# Knowledge Base Index

Status: `ACTIVE`

## Key Areas

- `kicad_core/`: normalized KiCad project-manager, CLI, and ERC/DRC guidance.
- `kicad_python_api/`: normalized `pcbnew` context and safe-usage guidance.
- `kicad_file_formats/`: normalized s-expression format and connectivity notes.
- `kicad_libraries/`: normalized KLC and library-usage guidance.
- `summaries/`: normalized migration summaries for drained knowledge sources.
- `pcb_layout/`: PCB routing/return-path summaries.
- `usb_c/`: USB-C and USB ESD summaries.
- `power_integrity/`: buck and decoupling summaries.
- `rf_wifi/`: RF/Wi-Fi keepout summaries.
- `thermal_mechanical/`: thermal, mounting, and test-access summaries.
- `training/`: normalized training and lecture guidance with confidence rules.
- `peer_review/`: forum and peer-review usage policy plus observation indexes.
- `case_studies/`: good-board and bad-board pattern extraction summaries.
- `circuits/`: reusable circuit block guidance.
- `design_patterns/`: project and schematic organization patterns.
- `checklists/`: pre-schematic, pre-PCB, pre-fab, and interface review checklists.
- `common_mistakes/`: recurring engineering mistakes.
- `manufacturing/`: fab and assembly package rules.
- `ai_agent_guidance/`: anti-hallucination and human-review rules.

## Required Use

Use this folder for planning guidance only. Exact values still require
datasheet and source verification.

The legacy `knowledge_scrape/` source folder has been retired and removed.
Canonical knowledge lookup now starts here, in `09_ACCURACY_ENGINE/`, and in
the related source-registry / retrieval-index surfaces.

## Core Circuit Files

- `circuits/USB_C_POWER_ONLY.md`
- `circuits/USB_C_USB2_DEVICE.md`
- `circuits/ESP32_S3_MINIMUM_SYSTEM.md`
- `circuits/STM32_MINIMUM_SYSTEM.md`
- `circuits/PIC_MINIMUM_SYSTEM.md`
- `circuits/CAN_BUS_NODE.md`
- `circuits/CAN_FD_NODE.md`
- `circuits/RS485_NODE.md`
- `circuits/12V_TO_5V_BUCK.md`
- `circuits/5V_TO_3V3_LDO.md`
- `circuits/AUTOMOTIVE_12V_INPUT_PROTECTION.md`
- `circuits/RF_ANTENNA_UFL_MODULE.md`
- `circuits/STATUS_LED_BUTTON_RESET.md`

## Verification Reminder

Knowledge-base patterns are not approval. Use
`09_ACCURACY_ENGINE/checklists/ACCURACY_GATE_CHECKLIST.md` before acting on any
pattern.

For the drained engineering-rule knowledge phase, use the canonical rule files
under `09_ACCURACY_ENGINE/` before consulting the summary notes here.
