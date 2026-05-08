# Knowledge Base Index

Status: `ACTIVE`

## Key Areas

- `circuits/`: reusable circuit block guidance.
- `design_patterns/`: project and schematic organization patterns.
- `checklists/`: pre-schematic, pre-PCB, pre-fab, and interface review checklists.
- `common_mistakes/`: recurring engineering mistakes.
- `manufacturing/`: fab and assembly package rules.
- `ai_agent_guidance/`: anti-hallucination and human-review rules.

## Required Use

Use this folder for planning guidance only. Exact values still require datasheet and source verification.

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

## Core Common Mistake Files

- `common_mistakes/ESP32_COMMON_MISTAKES.md`
- `common_mistakes/STM32_COMMON_MISTAKES.md`
- `common_mistakes/PIC_COMMON_MISTAKES.md`
- `common_mistakes/USB_C_COMMON_MISTAKES.md`
- `common_mistakes/CAN_COMMON_MISTAKES.md`
- `common_mistakes/REGULATOR_COMMON_MISTAKES.md`
- `common_mistakes/CONNECTOR_COMMON_MISTAKES.md`
- `common_mistakes/FOOTPRINT_COMMON_MISTAKES.md`

## Verification Reminder

Knowledge-base patterns are not approval. Use `09_ACCURACY_ENGINE/checklists/ACCURACY_GATE_CHECKLIST.md` before acting on any pattern.


## PURPOSE

Store reusable circuit patterns, design patterns, checklists, common mistakes, and practical review guidance.

## WHAT_BELONGS_HERE

Circuit guides, design patterns, review checklists, manufacturing rules, and AI stop/verify guidance.

## WHAT_DOES_NOT_BELONG_HERE

Datasheet replacements, active KiCad projects, exact specs without sources, or generated outputs.

## AI_AGENT_RULES

- Read this folder's README.md and INDEX.md before adding or relying on content here.
- Mark unverified engineering claims explicitly.
- Keep source links, verification status, and human-review requirements visible.
- Route generated logs and reports to 2_HISTORY/, 5_OUTPUTS/, or project history/ unless this folder explicitly calls for generated indexes.

## SAFE_EDIT_RULES

- Preserve existing user work.
- Do not delete or overwrite files without explicit approval.
- Do not edit KiCad design files from this folder.
- Do not store secrets or credentials.

## PUBLIC_RELEASE_NOTES

- Review this folder for secrets, personal paths, copyrighted documents, unsupported claims, and large generated files before public release.
- Folder existence is not a completeness or production-readiness claim.
