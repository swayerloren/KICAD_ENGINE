# Agent Mistakes To Avoid

Repo-wide mistakes Codex, Claude, and similar agents must avoid across KiCad Engine projects.

Use this file for recurring AI failure modes, not for blaming a specific session. Project-specific mistakes belong in that project's `memory/AGENT_MISTAKES_TO_AVOID.md`.

## Required Rules

- Do not approve a connector footprint without exact manufacturer drawing, pin numbering, mechanical orientation, and human review.
- Do not claim a footprint is correct from a generic KiCad library name alone.
- Do not treat a 3D model as proof of footprint correctness.
- Do not silently convert a user correction into a global rule unless it is reusable beyond the project.
- Do not store secrets, tokens, or private credentials.

## Mistake Record Format

```text
ID:
Date:
Status: UNVERIFIED | USER_CONFIRMED | VERIFIED_WORKFLOW
Mistake:
Risk:
Avoidance rule:
Evidence:
Applies to:
```

## EXAMPLE_ONLY: USB-C Connector Footprint Was Wrong

ID: `EXAMPLE_ONLY_GLOBAL_AGENT_MISTAKE_USB_C_FOOTPRINT`

Status: `EXAMPLE_ONLY`

Mistake: An AI agent selected or approved a USB-C connector footprint without verifying the exact manufacturer part drawing, pin numbering, shell tab geometry, board edge relationship, and mating/mechanical orientation.

Risk: The board may not physically fit the connector, assembly may fail, or USB pins may be reversed/misnumbered.

Avoidance rule: USB-C connector footprints must remain `UNVERIFIED_FOOTPRINT` until matched to an exact manufacturer part number and drawing, reviewed against the KiCad footprint, and human-confirmed for orientation.

Evidence: Example only. This is not a claim about an actual KiCad Engine project.

## 2026-05-06: Automated Crop Pass Was Treated As Visual Approval

ID: `GLOBAL_AGENT_MISTAKE_AUTOMATED_CROP_PASS_VISUAL_APPROVAL`

Date: `2026-05-06`

Status: `USER_CONFIRMED`

Mistake: An AI agent treated automated schematic checks, crop generation, annotation checks, footprint assignment checks, and ERC status as sufficient evidence that a schematic was human-readable.

Risk: A schematic can still be unusable for human review when values, references, net labels, notes, power symbols, and wires visually overlap or crowd each other. This can let an unreadable schematic advance toward PCB work.

Avoidance rule: Automated crop generation is only evidence that review images exist. It is not `VISUAL_PASS`. A schematic requires rendered full-page and close-up human-readability review before it can be marked ready for LJ visual review or PCB gate progression.

Evidence: User correction on `2026-05-06` for `ESP32_CSI_WIFI_NODE`; see `09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md` and `09_ACCURACY_ENGINE/verification_rules/VISUAL_PASS_IS_NOT_AUTOMATED_PASS.md`.

Applies to: All KiCad schematic visual reviews.

## 2026-05-06: Evidence Generation Was Confused With Gate Completion

ID: `GLOBAL_AGENT_MISTAKE_EVIDENCE_GENERATION_AS_GATE_COMPLETION`

Date: `2026-05-06`

Status: `USER_CONFIRMED`

Mistake: An AI agent treated generated reports, crop files, ERC results, annotation checks, and footprint-population checks as if they completed the visual and readiness gates. The repo had many artifacts, but the decisive human-readable schematic judgment was not actually enforced before readiness wording was used.

Risk: Large documentation systems can create false confidence. A project can look heavily verified while the actual schematic remains unreadable or blocked.

Avoidance rule: Every gate must distinguish evidence generation from gate completion. A gate passes only when its specific acceptance criteria are explicitly satisfied and cited. For schematic visual work, `AUTOMATED_CROP_PASS_ONLY` is not `VISUAL_PASS`.

Evidence: `02_HISTORY/design_reviews/KICAD_ENGINE_SCHEMATIC_FAILURE_ROOT_CAUSE_AUDIT.md`; `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/STRICT_VISUAL_READABILITY_REAUDIT.md`.

Applies to: All KiCad Engine project gates.

## 2026-05-07: Downstream PCB Reviews Ran Before Required Evidence

ID: `GLOBAL_AGENT_MISTAKE_PHASE_SKIPPING_AND_FALSE_CURRENT_STATE`

Date: `2026-05-07`

Status: `USER_CONFIRMED`

Mistake: Agents created downstream JLCPCB, mechanical, BOM, export, upload-feedback, and signoff-style reports before earlier PCB evidence was valid, and repeated sessions left stale/conflicting "current" reports.

Risk: Future agents may trust obsolete reports, duplicate blockers, or false-pass wording instead of current design evidence.

Avoidance rule: Run the phase gate and memory maintenance workflow. Current truth must come from active evidence files and project `memory/CURRENT_PROJECT_STATE.md`, not from the newest-looking report name or Codex summary.

Evidence: `09_ACCURACY_ENGINE/workflows/MANDATORY_KICAD_PHASE_GATE.md`; `09_ACCURACY_ENGINE/workflows/MEMORY_HISTORY_MAINTENANCE_WORKFLOW.md`.

Applies to: All KiCad PCB, production, export, and signoff workflows.

## 2026-05-07: Barrel Jack Solder Side Was Confused With The Front Opening

ID: `GLOBAL_AGENT_MISTAKE_BARREL_JACK_FRONT_BACK_CONFUSION`

Date: `2026-05-07`

Status: `USER_CONFIRMED`

Mistake: Codex confused the 3-pin solder-leg side of a horizontal DC barrel jack with the female barrel opening/front side.

Risk: A barrel jack can be rotated so the solder/back side faces off-board and the female opening faces inward, making the PCB mechanically wrong even when coordinates look close.

Avoidance rule: For horizontal DC barrel jacks, the 3-pin solder-leg side is the back/rear. The female circular opening is the front/mating side and must face off-board for edge placement. For bottom-edge placement, the female opening faces down/off-board and the 3-pin solder side faces up/inward.

Evidence: LJ correction and reference image provided on `2026-05-07`; see `09_ACCURACY_ENGINE/pcb_rules/BARREL_JACK_ORIENTATION_RULES.md`.

Applies to: All barrel-jack connector orientation reviews.

## 2026-05-07: BOM/CPL Validation Was Confused With Upload Approval

ID: `GLOBAL_AGENT_MISTAKE_BOM_CPL_VALIDATION_AS_UPLOAD_APPROVAL`

Date: `2026-05-07`

Status: `USER_CONFIRMED`

Mistake: An agent could treat structurally valid BOM, CPL, centroid, Gerber, or package-folder files as if the board were approved for assembly upload.

Risk: A package with correct columns can still have wrong part orientation, wrong connector mating direction, wrong pin 1, wrong polarity, bad Gerbers, missing drills, failing DRC, unrouted nets, or unapproved substitutions.

Avoidance rule: JLCPCB and PCBWay packages require fab-house-specific BOM/placement formats, validators, assembly notes, orientation checks, DRC/no-unrouted proof, external Gerber review, and LJ approval. Pick-and-place rotations must not be trusted blindly.

Evidence: `T_E_M_P/file format.md` integration on `2026-05-07`; see `24_FAB_PROFILES/` and `03_TOOLS/scripts/fabrication/`.

Applies to: All manufacturing export, assembly, JLCPCB, PCBWay, BOM, CPL, centroid, and NOT_FINAL package workflows.

## 2026-05-07: Crude 90-Degree Scripted Routing Was Treated As Acceptable

ID: `GLOBAL_AGENT_MISTAKE_CRUDE_90_DEGREE_SCRIPTED_ROUTING`

Date: `2026-05-07`

Status: `USER_CONFIRMED`

Mistake: An AI routing pass left harsh 90-degree bends, awkward pathing, and non-professional trace geometry in a PCB routing result.

Risk: Even when manufacturable and DRC-clean, crude routing increases review churn, can worsen copper geometry and signal behavior, and fails the board's visual and engineering quality gate.

Avoidance rule: Avoid 90-degree corners where practical, never use acute bends sharper than 90 degrees unless documented as unavoidable, use 45-degree bends for normal routing, and prefer smoother geometry for high-speed or sensitive nets. If placement causes ugly routing, move the local cluster instead of forcing bad traces.

Evidence: LJ user correction on `2026-05-07`; see `09_ACCURACY_ENGINE/pcb_rules/TRACE_ANGLE_ROUTING_RULES.md` and `02_HISTORY/known_agent_mistakes/CRUDE_90_DEGREE_SCRIPTED_ROUTING.md`.

Applies to: All KiCad PCB routing, routing automation, and routing review workflows.
