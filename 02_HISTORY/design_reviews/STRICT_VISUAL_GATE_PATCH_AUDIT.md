# Strict Visual Gate Patch Audit

Status: `PASS_WITH_ESP32_BLOCKED`

Date: 2026-05-06

## Problem

The existing schematic visual workflow allowed an automated crop result to be treated as a visual readiness signal even when the rendered schematic remained unreadable.

ESP32_CSI_WIFI_NODE exposed the failure mode:

- ERC passed.
- Annotation passed.
- Physical footprint fields were populated.
- Automated crop generation passed.
- No visible footprint/library/path strings were detected.
- No `?` reference tokens were detected.
- The rendered schematic still had visible text/value/reference/net-label overlaps and was not human-readable.

## Rule Changes Added

| Rule | File |
| --- | --- |
| Automated visual crop `PASS` is not `VISUAL_PASS`. | `09_ACCURACY_ENGINE/verification_rules/VISUAL_PASS_IS_NOT_AUTOMATED_PASS.md` |
| Any visible text/value/ref/net-label overlap is `VISUAL_FAIL`. | `09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md` |
| Notes must not be placed inside active circuitry. | `09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md` |
| Values must be short and readable; long review notes belong in hidden fields, notes zones, or review tables. | `09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md` |
| Review markers must not clutter values unless direct visibility is required. | `09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md` |
| Power symbols, net labels, and references must not be stacked or visually touching. | `09_ACCURACY_ENGINE/checklists/SCHEMATIC_HUMAN_READABILITY_CHECKLIST.md` |
| A schematic cannot be `READY_FOR_LJ_VISUAL_REVIEW` if any crop visibly overlaps text/symbol/wire content. | `09_ACCURACY_ENGINE/checklists/SCHEMATIC_HUMAN_READABILITY_CHECKLIST.md` |
| If rendered PNG/crops cannot be inspected, status is `VISUAL_NOT_VERIFIED`, not `PASS`. | `09_ACCURACY_ENGINE/verification_rules/VISUAL_PASS_IS_NOT_AUTOMATED_PASS.md` |
| File-level annotation pass is not enough when KiCad/rendered output still shows visible question-mark references. | `09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md` |

## Existing File Updates

- `03_TOOLS/kicad/VISUAL_VERIFICATION_WORKFLOW.md` now distinguishes `AUTOMATED_CROP_PASS_ONLY`, `VISUAL_PASS`, `VISUAL_FAIL`, and `VISUAL_NOT_VERIFIED`.
- `09_ACCURACY_ENGINE/verification_rules/CLOSE_UP_VISUAL_REVIEW_RULES.md` now blocks visible overlap, notes inside circuitry, long values, stacked power labels, and uninspected rendered crops.
- `09_ACCURACY_ENGINE/schematic_rules/SCHEMATIC_CREATION_STANDARD.md` now requires short visible values, notes outside circuitry, and readable spacing.
- `AGENTS.md` now requires human-readable visual inspection before treating close-up review as complete.
- `README_GPT.md` now documents the stricter schematic-to-PCB visual gate.
- `FOR CHAT GPT.MD` now records the strict visual gate patch for future handoff.
- `CURRENT_KNOWN_PROBLEMS.md` now flags this as a critical known failure mode.
- `01_MEMORY/AGENT_MISTAKES_TO_AVOID.md` now records the reusable mistake.
- `01_MEMORY/GLOBAL_HALLUCINATION_RISKS.md` now records the hallucination-risk pattern.

## Closeout Evidence

- User correction: `02_HISTORY/user_corrections/20260506_170041_Automated_schematic_visual_pass_was_not_human_readable.md`
- AI self-review: `02_HISTORY/ai_self_reviews/20260506_170041_Strict_human_readable_schematic_visual_gate_patch.md`
- Scorecard: `02_HISTORY/ai_scorecards/20260506_170041_Strict_visual_gate_patch_response_scorecard.md`
- Claim/evidence matrix: `02_HISTORY/claim_evidence_matrices/20260506_170057_Strict_visual_gate_patch_claim_evidence_matrix.md`
- Uncertainty log: `02_HISTORY/uncertainty_logs/20260506_170057_Strict_visual_gate_patch_uncertainty_log.md`
- Hallucination-risk log: `02_HISTORY/hallucination_risk_logs/20260506_170057_Risk_of_confusing_automated_visual_artifacts_with_human_readable_schematic_appro.md`

## Prevention Mechanism

Future agents must keep two separate statuses:

1. Automated crop generation/screening status.
2. Human-readable visual inspection status.

The schematic-to-PCB gate can use only the second status for visual approval.

If rendered evidence is not inspected, the result is `VISUAL_NOT_VERIFIED`.

If rendered evidence shows overlap, the result is `VISUAL_FAIL`.

## Current ESP32_CSI_WIFI_NODE Status

Current classification: `NOT_READY_NEEDS_MORE_REPAIR`

Evidence:

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/FINAL_SCHEMATIC_READINESS_AUDIT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/LJ_FINAL_VISUAL_REVIEW_PACKET.md`

PCB update allowed: `NO`

The ESP32 schematic remains blocked. It still needs visual cleanup plus high-risk part/footprint decisions before any schematic-to-PCB gate can pass.
