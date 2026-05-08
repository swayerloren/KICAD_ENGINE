# User Corrections Memory

Global memory for user corrections that should change future KiCad Engine behavior across projects.

Project-specific corrections belong in the project `memory/USER_CORRECTIONS.md` and `history/user_corrections/`. Promote a correction here only when it is reusable for multiple projects.

## Capture Rules

- Record the user's correction in their wording when practical, but do not quote secrets or private credentials.
- Mark status `UNVERIFIED` until the correction is checked or user-confirmed.
- Record what behavior must change.
- Link to the project correction record when applicable.

## Correction Record Format

```text
ID:
Date:
Status: UNVERIFIED | USER_CONFIRMED | VERIFIED_WORKFLOW
User correction:
Changed global rule:
Affected workflows:
Evidence:
Next check:
```

## Current Global Corrections

## 2026-05-06: Unreadable Schematic Was Overclaimed As Improved

ID: `USER_CORRECTION_SCHEMATIC_VISUAL_PASS_NOT_AUTOMATED_PASS`

Date: `2026-05-06`

Status: `USER_CONFIRMED`

User correction: LJ reported that the ESP32_CSI_WIFI_NODE schematic remained visually unacceptable in KiCad even though prior reports claimed annotation/visual status had improved.

Changed global rule: Automated visual crop generation, ERC pass, annotation pass, populated footprints, hidden fields, and no `?` token detection must never be treated as human-readable schematic approval. Rendered images must be inspected block by block.

Affected workflows: Schematic visual audit, schematic visual repair, schematic-to-PCB gate, close-up visual crop generation, project gate runner visual gate.

Evidence: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/EMERGENCY_CURRENT_SCHEMATIC_TRUTH_AUDIT.md`, `FINAL_SCHEMATIC_READINESS_AUDIT.md`, `STRICT_VISUAL_READABILITY_REAUDIT.md`, and `02_HISTORY/design_reviews/KICAD_ENGINE_SCHEMATIC_FAILURE_ROOT_CAUSE_AUDIT.md`.

Next check: Future visual prompts must return `AUTOMATED_CROP_PASS_ONLY`, `VISUAL_FAIL`, or `VISUAL_NOT_VERIFIED` unless rendered images are inspected and every required block passes.

## 2026-05-07: Memory/History Must Compile Current Truth Without Deleting History

ID: `USER_CORRECTION_MEMORY_HISTORY_CURRENT_TRUTH_MAINTENANCE`

Date: `2026-05-07`

Status: `USER_CONFIRMED`

User correction: LJ reported that repeated agent sessions created duplicate blockers, stale current-status language, false-pass claims, vague dates, and conflicting status files.

Changed global rule: Maintain the existing `01_MEMORY`, `02_HISTORY`, and project memory/history folders by compiling current truth, marking superseded/stale/false-pass records, normalizing dates, and preserving old history.

Affected workflows: Session closeout, current project state compilation, report review, phase-gate review, memory/history index rebuilds.

Evidence: `03_TOOLS/scripts/memory_maintenance/`; `09_ACCURACY_ENGINE/workflows/MEMORY_HISTORY_MAINTENANCE_WORKFLOW.md`.

Next check: Future agents should run dry-run maintenance before trusting old project reports with conflicting status.

## 2026-05-07: Barrel Jack Front/Back Orientation Was Misread

ID: `USER_CORRECTION_BARREL_JACK_FRONT_BACK_ORIENTATION`

Date: `2026-05-07`

Status: `USER_CONFIRMED`

User correction: LJ clarified with a physical reference image that, for CUI/PJ-102AH-style horizontal DC barrel jacks, the female circular barrel opening is the front/mating side and the 3-pin solder-leg side is the back/rear side.

Changed global rule: Edge-mounted barrel jacks must place the female opening off-board and the solder-leg rear/back side inward toward the PCB. Bottom-edge barrel jacks must have the female opening facing down/off-board and the 3-pin solder side facing up/inward.

Affected workflows: Connector orientation review, PCB placement, pill-style dev-board layout, barrel-jack footprint approval, prompt-pack placement passes.

Evidence: `09_ACCURACY_ENGINE/pcb_rules/BARREL_JACK_ORIENTATION_RULES.md`; `10_KNOWLEDGE_BASE/connectors/BARREL_JACK_ORIENTATION_GUIDE.md`; project reference `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/references/connector_orientation/J1_BARREL_JACK_ORIENTATION_REFERENCE.md`.

Next check: Future barrel-jack placement reviews must verify front/back using 3D model if available, `F.Fab`/`F.SilkS`/`F.CrtYd` footprint geometry, and manufacturer/product-image evidence. Coordinates alone are not proof.

## 2026-05-07: PCB Trace Routing Must Avoid Crude 90-Degree And Acute Angles

ID: `USER_CORRECTION_PCB_TRACE_ANGLE_ROUTING_QUALITY`

Date: `2026-05-07`

Status: `USER_CONFIRMED`

User correction: When tracing a PCB, avoid using 90-degree angles where practical. Use 45-degree bends or smooth and rounded curves instead. Acute angles sharper than 90 degrees must be avoided. 90-degree turns may be manufacturable today, but they are still discouraged for professional routing quality. Acute angles can create acid-trap and manufacturing risks, poor copper geometry, and signal-quality problems. For high-speed or high-frequency routing, smooth curves or filleted routing is preferred. For normal routing, two 45-degree bends are the standard best practice.

Changed global rule: PCB routing quality requires angle and geometry review in addition to DRC. Crude 90-degree routing, acute-angle routing, and awkward pathing are not acceptable finished results.

Affected workflows: PCB routing, routing-plan prompts, routing automation, critical-net routing, remaining-net routing, final PCB verification, and project routing reviews.

Evidence: `09_ACCURACY_ENGINE/pcb_rules/TRACE_ANGLE_ROUTING_RULES.md`; `09_ACCURACY_ENGINE/checklists/PCB_ROUTING_QUALITY_CHECKLIST.md`; `02_HISTORY/user_corrections/PCB_TRACE_ANGLE_ROUTING_CORRECTION.md`.

Next check: Future routing prompts and project routing reviews must explicitly audit trace angles, unnecessary vias, awkward detours, and visually crude routing before the board can advance.
