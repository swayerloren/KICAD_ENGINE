# ESP32_CSI_WIFI_NODE JLCPCB Upload Fix Plan

Date: 2026-05-07

Mode: `PLAN_ONLY`

PCB edited: `NO`

BOM edited: `NO`

Fixes approved: `NO`

Final classification: `JLC_FEEDBACK_NEEDS_MORE_INFO`

## Plan Decision

No exact PCB/BOM fix plan can be created yet because no JLCPCB upload feedback was provided. This file defines the review structure to use once LJ provides screenshots or text.

No edits are approved by this plan.

## Current Action Plan

| Step | Action | Owner | Status |
|---:|---|---|---:|
| 1 | LJ provides JLCPCB screenshot/text feedback or the uploaded package path. | LJ | `WAITING_FOR_INPUT` |
| 2 | Codex transcribes each warning/error exactly. | Codex | `BLOCKED` |
| 3 | Codex maps each item to Gerber, drill, BOM, CPL, footprint, rotation, package, stock, or assembly side. | Codex | `BLOCKED` |
| 4 | Codex classifies each item as must fix, should fix, okay to ignore, or needs human decision. | Codex | `BLOCKED` |
| 5 | Codex writes exact PCB/BOM repair steps without editing files. | Codex | `BLOCKED` |
| 6 | LJ approves or rejects the fix plan. | LJ | `BLOCKED` |
| 7 | Only after approval, Codex may perform allowed safe fixes under a new task with backup. | Codex | `BLOCKED` |

## Fix-Plan Template For Incoming JLC Feedback

| JLC item | Source | Classification | Proposed fix | File likely affected | Requires human decision | Verification after fix |
|---|---|---:|---|---|---:|---|
| `TBD_AFTER_LJ_INPUT` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | `TBD` |

## Classification Rules

| Classification | Meaning |
|---|---|
| `MUST_FIX` | Blocks upload, fabrication, assembly, electrical safety, fit, polarity, pinout, or order correctness. |
| `SHOULD_FIX` | Not immediately blocking, but likely improves manufacturability, assembly yield, readability, or review confidence. |
| `OKAY_TO_IGNORE` | Benign JLC warning with documented reason and no expected production impact. |
| `NEEDS_HUMAN_DECISION` | Requires LJ choice, exact part selection, assembly strategy, cost/availability decision, or acceptance of risk. |

## Known Non-Feedback Blockers

These must not be confused with actual JLC upload feedback:

| Blocker | Current state | Required before normal upload |
|---|---:|---|
| PCB source file | `MISSING` | Create/update PCB only after schematic-to-PCB gate passes. |
| Gerbers/drills/CPL | `NOT_CREATED` | Export only after valid PCB, DRC/routing gates, and NOT_FINAL export approval. |
| DRC | `NOT_RUN_NO_PCB` | Run after PCB exists. |
| BOM readiness | `BOM_BLOCKED` | Resolve exact parts, package drawings, JLC/LCSC status, and assembly strategy. |
| JLC DFM/DFA readiness | `JLCPCB_REVIEW_BLOCKED` | Re-run after PCB and package exist. |

## Editing Rule

Do not edit schematic, PCB, BOM, CPL, footprints, rotations, or package metadata until LJ provides feedback and approves a concrete fix plan.

## Final Classification

`JLC_FEEDBACK_NEEDS_MORE_INFO`

