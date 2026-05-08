# PCB Trace Angle Routing Correction

Date: `2026-05-07`

Status: `ACTIVE_EVIDENCE`

Scope: repo rule, memory, prompt-pack, and project-intelligence patch only. No KiCad schematic, PCB, or project files were edited.

## User Correction

When tracing a PCB, avoid using 90-degree angles where practical. Use 45-degree bends or smooth and rounded curves instead. Acute angles sharper than 90 degrees must be avoided. 90-degree turns may be manufacturable today, but they are still discouraged for professional routing quality. Acute angles can create acid-trap and manufacturing risks, poor copper geometry, and signal-quality problems. For high-speed or high-frequency routing, smooth curves or filleted routing is preferred. For normal routing, two 45-degree bends are the standard best practice.

## Permanent Rule Change

- Added permanent routing-angle rules under `09_ACCURACY_ENGINE/pcb_rules`.
- Added a routing-quality checklist under `09_ACCURACY_ENGINE/checklists`.
- Updated routing prompts and project routing intelligence to require angle-quality review.
- Recorded the correction in global memory and project memory.

## Applies To

- KiCad PCB routing
- routing automation
- routing prompt packs
- critical-net routing reviews
- final PCB verification

