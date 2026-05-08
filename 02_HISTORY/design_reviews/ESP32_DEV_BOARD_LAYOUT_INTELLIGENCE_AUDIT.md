# ESP32 Dev Board Layout Intelligence Audit

Date: `2026-05-07`

## Scope

Repo knowledge-base, sandbox-rule, memory, and handoff updates only. No KiCad schematic, PCB, project, or manufacturing files were edited.

## Files Created

- `10_KNOWLEDGE_BASE/design_patterns/ESP32_DEV_BOARD_LAYOUT_PATTERN.md`
- `10_KNOWLEDGE_BASE/design_patterns/STM32_DEV_BOARD_LAYOUT_PATTERN.md`
- `10_KNOWLEDGE_BASE/design_patterns/CONNECTOR_EDGE_PLACEMENT_PATTERN.md`
- `10_KNOWLEDGE_BASE/design_patterns/RF_MODULE_ANTENNA_KEEP_OUT_PATTERN.md`
- `10_KNOWLEDGE_BASE/common_mistakes/ESP32_LAYOUT_COMMON_MISTAKES.md`
- `10_KNOWLEDGE_BASE/common_mistakes/USB_C_CONNECTOR_LAYOUT_COMMON_MISTAKES.md`
- `10_KNOWLEDGE_BASE/common_mistakes/BARREL_JACK_LAYOUT_COMMON_MISTAKES.md`
- `34_PCB_LAYOUT_SANDBOX/ESP32_STYLE_BOARD_PLACEMENT_RULES.md`
- `34_PCB_LAYOUT_SANDBOX/DEV_BOARD_SHAPE_REASONING_RULES.md`

## Files Updated

- `34_PCB_LAYOUT_SANDBOX/COMPONENT_PLACEMENT_RULES.md`
- `34_PCB_LAYOUT_SANDBOX/CONNECTOR_ORIENTATION_RULES.md`
- `34_PCB_LAYOUT_SANDBOX/RF_ANTENNA_KEEP_OUT_RULES.md`
- `34_PCB_LAYOUT_SANDBOX/INDEX.md`
- `34_PCB_LAYOUT_SANDBOX/README.md`
- `01_MEMORY/DESIGN_RULES_MEMORY.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`

## Rule Coverage Summary

- ESP32 antenna must stay at a board edge or clear keepout unless the project uses an external antenna module.
- Copper, traces, connectors, mounting holes, test pads, and tall parts are blocked from the antenna keepout unless exact source documentation allows them.
- USB-C and barrel-jack connectors are treated as edge-serving mechanical parts by default.
- Buttons must remain user-accessible.
- LEDs must remain visible.
- Test pads must remain accessible after assembly.
- Mounting holes must be mechanically spaced and clearance-checked.
- Board shape must be justified; rectangle or square cannot be assumed by default.
- The new docs explicitly warn that these are patterns, not universal rules, and that project requirements come first.

## Validation

- File-existence checks confirmed every requested file was created.
- Reference scans confirmed the warning language and core placement requirements in the new docs, global memory, and handoff files.
- Final active-project KiCad hashes matched the pre-edit baseline.

## Residual Risk

- These placement-intelligence docs are now available, but they have not yet been exercised in a full project-local sandbox variant set.
- First live use should confirm whether any prompt-pack files need additional direct references beyond the sandbox/handoff layer.
