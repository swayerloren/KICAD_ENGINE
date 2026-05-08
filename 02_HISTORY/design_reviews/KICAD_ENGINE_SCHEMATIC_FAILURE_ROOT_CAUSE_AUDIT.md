# KiCad Engine Schematic Failure Root-Cause Audit

Date: 2026-05-06  
Scope: root cause of unreadable `ESP32_CSI_WIFI_NODE` schematic despite rules, reports, and gates  
KiCad design files edited: NO

## Executive Summary

Exact root cause: KiCad Engine had many rules and reports, but the decisive visual gate relied on generated evidence and narrow text checks instead of requiring actual rendered-image readability judgment before using pass-like language.

The failure was not that ERC, annotation, or crop generation were useless. The failure was that their status labels were allowed to sound broader than the evidence supported. `PASS` from the crop generator meant "crops exist and no limited regex findings were found," but later reports and prompts treated that as a sign the schematic was visually improved or ready for LJ review.

The repo had bureaucracy around gates, but the operational gate did not force the agent to inspect rendered images block-by-block before saying the schematic was visually acceptable.

## Evidence Reviewed

- `09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/EMERGENCY_CURRENT_SCHEMATIC_TRUTH_AUDIT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/FINAL_SCHEMATIC_READINESS_AUDIT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_HUMAN_READABILITY_REPAIR_REPORT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/STRICT_VISUAL_READABILITY_REAUDIT.md`
- `03_TOOLS/scripts/visual/generate_schematic_closeups.py`
- `03_TOOLS/kicad/run_schematic_visual_check.ps1`
- `.prompts/kicad_pipeline/02_schematic_visual_closeup_audit.md`
- `.prompts/kicad_pipeline/03_schematic_visual_repair.md`
- `.prompts/kicad_pipeline/06_schematic_to_pcb_gate.md`

## 1. Repo Rules That Failed

| Rule area | Failure | Impact |
|---|---|---|
| Visual gate wording | Earlier workflow wording allowed `PASS` to mean crop generation/text screening, not human readability. | Reports sounded stronger than the evidence. |
| Close-up review workflow | `CLOSE_UP_REVIEW.md` was treated like a completed review, although generated sections still said human result `NOT_REVIEWED`. | The review worksheet became pseudo-evidence. |
| Schematic-to-PCB gate | The gate checked that visual artifacts existed but did not require a separate rendered-image judgment row before status language drifted. | The project stayed PCB-blocked, but human-review readiness was overclaimed. |
| Prompt pack | Prompt 02 returned `SCHEMATIC_VISUAL_PASS` without explicitly banning automated-only pass. | Future agents could repeat the same shortcut. |
| AI quality closeout | Scorecards existed, but they did not reject the overbroad visual claim at the moment it happened. | The quality layer recorded uncertainty after the fact instead of preventing the claim. |

## 2. Scripts That Gave Misleading PASS

| Script | Misleading status | Actual meaning | Required change |
|---|---|---|---|
| `03_TOOLS/scripts/visual/generate_schematic_closeups.py` | `Close-up visual review status: PASS` | Crop files were created and limited checks found no visible `?` refs or visible field-risk strings. It did not inspect overlap, crop framing, label/wire contact, or readability. | Use `AUTOMATED_CROP_PASS_ONLY` for non-failing automated evidence generation. |
| `03_TOOLS/kicad/run_schematic_visual_check.ps1` | Propagated the Python script's status. | Wrapper completed export/crop generation. | Treat wrapper completion as evidence-generation success only. |

## 3. Prompt Wording That Allowed Overclaim

Problem patterns:

- "Generate close-up crops" was too easy to treat as "complete visual review."
- "Review every crop" did not require the agent to open/render/inspect every image and fill a pass/fail table.
- `SCHEMATIC_VISUAL_PASS` was listed without a hard definition requiring rendered-image readability.
- Visual repair prompt allowed `SCHEMATIC_VISUAL_REPAIR_PASS` without explicitly requiring human-readability checklist completion.
- Schematic-to-PCB gate prompt said "visual close-ups" instead of "human-readable rendered-image visual inspection."

These prompts are now patched to ban automated-only visual pass.

## 4. Files That Were Mostly Bureaucracy For This Failure

These files are useful as routing and safety scaffolding, but they did not directly stop the failure because they were not enforced by the visual script or prompt status language:

| File or system | Why it did not stop this failure |
|---|---|
| Multiple startup indexes | They tell agents what to read, but they do not validate visual claims. |
| AI scorecards/self-reviews | They record quality after work; they did not force image inspection before pass-like wording. |
| Broad folder standards | They route artifacts correctly, but do not define schematic drawing quality. |
| Generated `CLOSE_UP_REVIEW.md` | It looked official, but it was a worksheet with `Human visual result: NOT_REVIEWED`. |
| Old pipeline prompts | They were process-heavy but lacked the one decisive rule: automated crop evidence is not human readability. |

The useful engineering guidance is the new strict visual-readability rule set, but it must be operationally enforced by scripts and prompts.

## 5. Visual Checker Improvements Needed

Immediate fix made:

- `generate_schematic_closeups.py` now uses `AUTOMATED_CROP_PASS_ONLY` instead of a bare `PASS` for automated-only success.

Still needed:

- Add an explicit `human_review_status` field to `CLOSE_UP_REVIEW.json`.
- Add a `VISUAL_NOT_VERIFIED` top-level status when no human-readable inspection table exists.
- Add image/opening instructions in the generated markdown for every crop.
- Add optional simple image/OCR heuristics for crop clipping, dense text clusters, and text near wires, but keep these as screening aids only.
- Refuse `VISUAL_PASS` unless a separate report provides block-by-block rendered-image inspection.

## 6. Close-Up Crop Process Gap

The crop process must be two-stage:

1. Automated evidence generation: exports/crops/report stubs.
2. Manual or visually inspected image review: actual readability judgment per block.

The failure happened because stage 1 was treated as if it completed stage 2.

## 7. Gate Status Wording That Must Change

Use these statuses:

- `AUTOMATED_CROP_PASS_ONLY`: exports/crops/basic screens succeeded.
- `VISUAL_NOT_VERIFIED`: rendered images were not inspected.
- `VISUAL_FAIL`: rendered images show any readability blocker.
- `VISUAL_PASS`: rendered full-page and crop images were inspected and no readability blocker remains.

Do not use bare `PASS` for visual readiness.

## 8. Future Prompts To Ban Or Rewrite

Ban prompts that ask for:

- "Run visual check and mark PASS if the script passes."
- "Generate close-up crops and proceed if crops exist."
- "Fix readability and mark ready if ERC/annotation/crops pass."
- "Treat no visible footprint fields or no question marks as visual pass."
- "Create a human review packet from automated evidence without inspecting rendered images."

Rewrite all visual prompts to require rendered-image inspection and a block-by-block fail table.

## 9. Rule That Would Have Stopped This Earlier

This rule would have stopped the failure before overclaiming:

> A schematic visual gate cannot pass unless a rendered full-page image and every close-up crop were actually inspected for human readability, and every block has an explicit `VISUAL_PASS`. Any automated crop status without that inspection is `AUTOMATED_CROP_PASS_ONLY` and blocks readiness claims.

## 10. Exact Files Updated In This Session

- `03_TOOLS/scripts/visual/generate_schematic_closeups.py`
- `09_ACCURACY_ENGINE/verification_rules/VISUAL_PASS_IS_NOT_AUTOMATED_PASS.md`
- `03_TOOLS/kicad/VISUAL_VERIFICATION_WORKFLOW.md`
- `.prompts/kicad_pipeline/02_schematic_visual_closeup_audit.md`
- `.prompts/kicad_pipeline/03_schematic_visual_repair.md`
- `.prompts/kicad_pipeline/06_schematic_to_pcb_gate.md`
- `00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md`
- `01_MEMORY/AGENT_MISTAKES_TO_AVOID.md`
- `01_MEMORY/USER_CORRECTIONS_MEMORY.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`

## Files Still Needing Future Updates

- `09_ACCURACY_ENGINE/checklists/SCHEMATIC_READY_FOR_PCB_CHECKLIST.md`: add a separate row for `AUTOMATED_CROP_PASS_ONLY` vs `VISUAL_PASS`.
- `09_ACCURACY_ENGINE/workflows/SCHEMATIC_TO_PCB_GATE_WORKFLOW.md`: make human-readable visual status an explicit blocking row.
- `03_TOOLS/scripts/visual/generate_schematic_closeups.py`: add JSON schema fields for manual review status.
- `03_TOOLS/scripts/project_gate/gates/schematic_visual_gate.py`: if present, ensure it rejects automated-only visual status.

## Final Root Cause

The root cause was evidence/status mismatch: KiCad Engine produced useful evidence, but its scripts and prompts used pass-like language for evidence generation. That let Codex overclaim human readability without completing actual visual inspection.

Final classification: `ROOT_CAUSE_CONFIRMED`

Production readiness impact: KiCad Engine is not production-ready for schematic visual approval until this gate model is fully enforced in scripts, prompts, and project gate runners.
