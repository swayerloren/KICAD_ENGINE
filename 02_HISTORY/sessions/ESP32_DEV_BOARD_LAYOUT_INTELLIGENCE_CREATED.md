# ESP32 Dev Board Layout Intelligence Created

Date: `2026-05-07`

## Summary

Added reusable PCB placement intelligence for ESP32-style boards, STM32-style dev boards, USB-C edge connectors, barrel-jack inputs, RF keepouts, buttons, LEDs, mounting holes, and test pads. The patch also added sandbox-level rules for ESP32 board placement and board-shape reasoning.

## Work Performed

1. Read the requested startup and sandbox placement files.
2. Incremented the active-project prompt counter and confirmed maintenance was not due.
3. Captured baseline hashes for the active project's `.kicad_pcb`, `.kicad_sch`, and `.kicad_pro` files.
4. Created new knowledge-base design-pattern and common-mistake files.
5. Created new sandbox placement-rule files for ESP32-style boards and dev-board shape reasoning.
6. Updated sandbox index/discovery files, global design-rule memory, and handoff docs.
7. Validated file existence, warning coverage, and no-design-file-change status.

## Result

- Design-pattern docs: `CREATED`
- Common-mistake docs: `CREATED`
- Sandbox placement intelligence: `CREATED`
- Memory and handoff: `UPDATED`
- KiCad design file changes: `NONE`

## Follow-Up

- Use these rules in the next project-local sandbox variant set before real PCB placement work.
- Record the first real adoption pass to confirm whether extra prompt-pack routing is needed.
