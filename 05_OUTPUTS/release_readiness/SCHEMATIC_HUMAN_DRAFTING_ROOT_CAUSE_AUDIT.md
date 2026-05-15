# Schematic Human Drafting Root Cause Audit

Generated: `2026-05-14`
Classification: `HUMAN_DRAFTING_ROOT_CAUSE_CONFIRMED_REPAIR_READY`
Task type: `AUDIT_ONLY`
Active project referenced: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
KiCad design-file edits: `NONE`

## Scope

Audit why KICAD_ENGINE allowed Codex to produce ERC-clean but visually weak schematics, using the ESP32_CSI_WIFI_NODE history as the main failure case.

## Evidence Reviewed

- `34_SCHEMATIC_QUALITY_ENGINE/README.md`
- `34_SCHEMATIC_QUALITY_ENGINE/README_FOR_CODEX_AND_CLAUDE.md`
- `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_WIRING_VS_LABEL_RULES.md`
- `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_READABILITY_STANDARD.md`
- `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_BLOCK_LAYOUT_RULES.md`
- `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_VISUAL_AUDIT_RULES.md`
- `34_SCHEMATIC_QUALITY_ENGINE/LOCAL_WIRING_STYLE_GUIDE.md`
- `34_SCHEMATIC_QUALITY_ENGINE/VISUAL_READABILITY_SCORECARD.md`
- `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_LAYOUT_ALGORITHM.md`
- `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_COMMON_FAILURES.md`
- `09_ACCURACY_ENGINE/schematic_rules/WIRE_VS_NET_LABEL_RULES.md`
- `09_ACCURACY_ENGINE/schematic_rules/READABLE_SCHEMATIC_FLOW_RULES.md`
- `09_ACCURACY_ENGINE/schematic_rules/REFERENCE_VALUE_TEXT_PLACEMENT_RULES.md`
- `09_ACCURACY_ENGINE/schematic_rules/ESP32_BOOT_RESET_RULES.md`
- `09_ACCURACY_ENGINE/schematic_rules/MCU_BOOT_STRAP_RULES.md`
- `09_ACCURACY_ENGINE/schematic_rules/DECOUPLING_SCHEMATIC_RULES.md`
- `09_ACCURACY_ENGINE/schematic_rules/BUCK_REGULATOR_SCHEMATIC_RULES.md`
- `09_ACCURACY_ENGINE/checklists/SCHEMATIC_HUMAN_READABILITY_CHECKLIST.md`
- `09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md`
- `03_TOOLS/scripts/schematic_quality/README.md`
- `03_TOOLS/scripts/schematic_quality/run_schematic_quality_gate.py`
- `03_TOOLS/scripts/schematic_quality/audit_wire_vs_label_balance.py`
- `03_TOOLS/scripts/schematic_quality/audit_schematic_block_layout.py`
- `03_TOOLS/scripts/schematic_quality/audit_schematic_text_overlaps.py`
- `03_TOOLS/scripts/schematic_quality/schematic_quality_common.py`
- `.prompts/shared/HUMAN_DRAFTING_MODE.md`
- `.prompts/kicad_pipeline/02_schematic_visual_cleanup.md`
- `.prompts/kicad_pipeline/02_schematic_visual_closeup_audit.md`
- `.prompts/kicad_pipeline/03_schematic_visual_repair.md`
- `.prompts/kicad_pipeline/03_schematic_electrical_review.md`
- `.prompts/codex/05_PLAN_SCHEMATIC.md`
- `.prompts/codex/06_REVIEW_SCHEMATIC.md`
- `.prompts/claude/05_PLAN_SCHEMATIC.md`
- `.prompts/claude/06_REVIEW_SCHEMATIC.md`
- `00_CODEX_START/TASK_TYPE_TO_RULE_MAP.md`
- `00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/FINAL_STRICT_SCHEMATIC_PRESENTATION_REVIEW.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/FINAL_HUMAN_DRAFTING_CLEANUP_REPORT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/USER_MANUAL_LAYOUT_LESSONS_AND_RULES.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/USER_MANUAL_PRESENTATION_BASELINE_ANALYSIS.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_quality/20260513_154721/schematic_quality_report.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_quality/20260513_154721/wire_vs_label.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_quality/20260513_154721/block_layout.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_quality/20260513_154721/text_overlaps.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_visual_cleanup_20260510_1319/quality_gate/schematic_quality_report.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_visual_cleanup_20260510_1319/quality_gate/wire_vs_label.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_visual_cleanup_20260510_1319/quality_gate/block_layout.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_visual_cleanup_20260510_1319/readability/schematic_readability_score.md`

## Root-Cause Summary

KICAD_ENGINE did not fail because it lacked all readability language. It failed because the repo weighted the wrong signals and enforced them too softly.

Primary causes:

1. The rule layer contains prose about readable wiring, but no hard rule chain that forces symbol orientation, local physical support wiring, topology honesty, and net/object verification before labels are accepted.
2. The tool layer measures overlap, block presence, and coarse label counts, but not drafting intent, local wire path quality, detached text ownership, graphic-vs-electrical object truth, or reset/boot topology sanity.
3. The report layer tolerated `WARN` and `PASS_WITH_MINOR_WARNINGS` for critical human-drafting debt, which let weak layouts be described as presentation-safe.
4. The prompt layer historically allowed or at least did not strongly prevent label-first cleanup; current prompts are now partially hardened, but the hard gate logic still does not enforce that drafting standard.
5. The repo separated visual review from electrical/topology truth too weakly. The user manual baseline later proved that a schematic can look much better and still contain electrical mistakes in the local control cluster.

## Exact Failed Behavior Observed

- Codex repeatedly overused local net labels instead of short physical wires.
- Codex preserved weak symbol orientation and then used labels to compensate.
- Codex created loopback or S-shaped local wiring in the reset/boot area.
- Codex allowed support parts to read as detached text islands instead of local subcircuits.
- Codex left USB and support-part orientation weaker than a human drafter would choose.
- Codex allowed references/values to remain technically non-overlapping while still visually detached from symbol ownership.
- The user then manually improved:
  - physical `ESP_EN` routing into `U2 EN`
  - physical `BOOT0` routing toward `U2 IO0`
  - USB/support orientation
  - decoupling grouping
  - ground/common-return presentation
  - reduction of unnecessary local labels

## Why ERC And Text-Overlap Were Insufficient

- ERC proves electrical rule consistency, not presentation quality.
- `audit_schematic_text_overlaps.py` only checks estimated collisions. It does not check whether text still belongs to the right symbol visually.
- `audit_schematic_block_layout.py` checks block presence, broad heading flow, and rough spacing, not drafting quality inside a local control cluster.
- `audit_wire_vs_label_balance.py` counts labels and wires per block, but cannot tell whether the remaining local labels were avoidable, whether a short wire would have been better, or whether a control path was drawn like a human engineer.
- `USER_MANUAL_PRESENTATION_BASELINE_ANALYSIS.md` proved the deeper failure mode: the improved dark control rail was made of real wires, yet the local return net was wrong and a switch topology could short `+3V3` to `GND`. ERC-clean visual review alone was therefore not enough.

## Current Rules That Mention Local Wires Vs Labels

The repo already contains local-wire guidance in these files:

- `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_WIRING_VS_LABEL_RULES.md`
- `34_SCHEMATIC_QUALITY_ENGINE/LOCAL_WIRING_STYLE_GUIDE.md`
- `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_READABILITY_STANDARD.md`
- `09_ACCURACY_ENGINE/schematic_rules/WIRE_VS_NET_LABEL_RULES.md`
- `09_ACCURACY_ENGINE/schematic_rules/READABLE_SCHEMATIC_FLOW_RULES.md`
- `09_ACCURACY_ENGINE/schematic_rules/ESP32_BOOT_RESET_RULES.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/USER_MANUAL_LAYOUT_LESSONS_AND_RULES.md`

What is missing is not mention. What is missing is strict enforcement.

## Why Existing Wire-Vs-Label Rules Were Insufficient

- The rules are mostly qualitative, not tied to hard failure conditions.
- The current automation mostly reduces the problem to counts.
- `wire_vs_label.md` from `20260513_154721` reported `PASS` for `Reset / Boot` with `labels=2, wires=24`, even though the later baseline analysis found the local control cluster had wrong saved-net truth and unsafe switch behavior.
- The `20260510_1319` wire-vs-label audit only warns when the same label repeats several times or when labels outnumber wires. That misses smaller but still ugly local-label abuse.
- No current wire-vs-label check asks:
  - could a short direct wire replace this label?
  - was the symbol rotated/flipped/repositioned first?
  - is this an MCU support circuit that should be locally physical?
  - is the wire path an ugly local loopback?

## Missing Orientation-Before-Label Rule

This is the clearest hard-gap in the rule engine.

- Current prompt files now mention orientation-first behavior.
- The core `34_SCHEMATIC_QUALITY_ENGINE` rules and scorecard do not strongly encode orientation-before-label as a mandatory drafting gate.
- `VISUAL_READABILITY_SCORECARD.md` scores local wire clarity and label balance, but does not score symbol orientation quality or label-avoidance by reorientation.
- `SCHEMATIC_BLOCK_LAYOUT_RULES.md` and `SCHEMATIC_LAYOUT_ALGORITHM.md` do not require an agent to prove it tried rotate/flip/reposition before adding labels.

Result: symbol orientation remained a soft preference instead of a hard drafting discipline.

## Prompt-Layer Findings

Historical root cause:

- The repo previously allowed Codex to reach readability conclusions without a strict enough human-drafting sequence.
- Surviving project reports show that label-heavy and presentation-weak states were still treated as acceptable or nearly acceptable.

Current state:

- `.prompts/shared/HUMAN_DRAFTING_MODE.md`
- `.prompts/kicad_pipeline/02_schematic_visual_cleanup.md`
- `.prompts/kicad_pipeline/02_schematic_visual_closeup_audit.md`
- `.prompts/kicad_pipeline/03_schematic_visual_repair.md`
- `.prompts/kicad_pipeline/03_schematic_electrical_review.md`
- `.prompts/codex/05_PLAN_SCHEMATIC.md`
- `.prompts/codex/06_REVIEW_SCHEMATIC.md`
- `.prompts/claude/05_PLAN_SCHEMATIC.md`
- `.prompts/claude/06_REVIEW_SCHEMATIC.md`

already contain improved human-drafting language, including local-wire-before-label and orientation-before-label guidance.

Remaining prompt gaps:

- no explicit post-cleanup object-type proof for dark/black rails
- no explicit saved-net truth proof for visually important local rails
- no explicit reset/boot switch topology sanity proof after visual cleanup
- no explicit ground/common-return presentation review
- no explicit ban on local S-shaped or loopback wiring for short control paths
- no explicit instruction that `PASS_WITH_MINOR_WARNINGS` is not acceptable when critical local control clusters still rely on avoidable labels or weak physical flow

## Tool-Layer Gaps

### Local-label abuse

Current gap:

- `audit_wire_vs_label_balance.py` only catches obvious repetition or label-heavy blocks.
- It misses 1-2 bad local labels that a human would still reject.

### Floating labels

Current gap:

- no dedicated detector for visually floating local labels that attach technically but still read as drafting shortcuts

### Graphic lines masquerading as wires

Current gap:

- `schematic_quality_common.py` extracts `wire` geometry but does not audit graphic-line objects near active nets
- no script verifies that visually important black rails are electrical wires instead of graphics

### S-shaped or loopback local wiring

Current gap:

- no current script scores local wire path quality
- no detector for unnecessary local loopbacks in short control connections

### Text/value detached from symbols

Current gap:

- `audit_schematic_text_overlaps.py` checks collision only
- it does not verify ownership distance, field anchoring, or whether text visually appears to belong to the wrong component

### Local MCU support circuits that should be physically wired

Current gap:

- no audit distinguishes cross-block label usage from nearby local MCU support nets that should be shown physically
- reset, boot, decoupling, local LEDs, and enable support all need stronger heuristics

### Reset/boot topology sanity

Current gap:

- no schematic-quality audit proves the saved topology is safe when buttons are pressed
- `USER_MANUAL_PRESENTATION_BASELINE_ANALYSIS.md` showed why this matters: the improved-looking control cluster still had a direct `+3V3` to `GND` short path through `SW2`

### Ground/common-return presentation

Current gap:

- no rule or script scores whether ground/common-return rails are both electrically true and presentation-quality
- dark return rails can improve flow, but the repo has no dedicated truth check or drafting standard for them

## Why Earlier Reports Allowed PASS_WITH_MINOR_WARNINGS

The repo exposed three soft-pass flaws:

1. `FINAL_STRICT_SCHEMATIC_PRESENTATION_REVIEW.md` concluded `PASS_WITH_MINOR_WARNINGS` while still recording full-sheet `WARN` and while the separate schematic-quality gate remained `FAIL`.
2. `SCHEMATIC_TO_PCB_GATE_STATUS.md` carried `Human visual schematic review | PASS_WITH_MINOR_WARNINGS`, which normalized a soft visual pass in the gate surface.
3. The local block reviews focused on whether a block looked non-disastrous in a crop, not whether the drafting was human-strong enough to become a protected baseline.

This let reports say, in effect, "not perfect, but acceptable" even when the user could still immediately spot drafting choices a human engineer would not keep.

## Checklist Items That Are Too Vague For Codex

- `SCHEMATIC_HUMAN_READABILITY_CHECKLIST.md`
  - `Boot/reset/programming labels are readable.`
  - `D+/D- labels readable and visually traceable.`
  - `Decoupling capacitors are readable and not jammed into the module symbol.`

These are readability checks, not drafting-judgment checks.

- `HUMAN_READABLE_SCHEMATIC_RULES.md`
  - strong on crowding and proof-of-visual-review
  - weak on when a short local wire is mandatory
  - weak on orientation-first discipline
  - weak on control-topology honesty

- `SCHEMATIC_VISUAL_AUDIT_RULES.md`
  - broad readability intent exists
  - explicit "draft like a human engineer" pass/fail criteria remain too loose

## Missing Rules That Need To Exist Explicitly

1. Missing orientation-before-label rule
   - a local label is not allowed until rotate/flip/reposition has been tried or clearly rejected

2. Missing graphic-line/electrical-wire verification rule
   - visually important black rails must be proven as `wire` objects, not graphics

3. Missing local MCU support physical-wiring rule
   - nearby `ESP_EN`, `BOOT0`, decoupling, local LEDs, and other short support nets should default to physical wires, not labels

4. Missing topology sanity rule for reset/boot circuits
   - no direct `+3V3` to `GND` short path through switches
   - required pull-up/pull-down intent must be proven

5. Missing presentation-quality rule for ground/common return rails
   - local return rails may be stylistically emphasized only when saved-net truth is verified

6. Missing local wire-path quality rule
   - avoid S-shaped and loopback short paths when a direct readable wire exists

7. Missing text-ownership rule
   - text must be visibly attached to the correct part, not merely non-overlapping

## Prompt Files Needing Updates

These files now contain improved drafting language, but still need narrow tightening:

- `.prompts/shared/HUMAN_DRAFTING_MODE.md`
- `.prompts/kicad_pipeline/02_schematic_visual_cleanup.md`
- `.prompts/kicad_pipeline/02_schematic_visual_closeup_audit.md`
- `.prompts/kicad_pipeline/03_schematic_visual_repair.md`
- `.prompts/kicad_pipeline/03_schematic_electrical_review.md`
- `.prompts/codex/05_PLAN_SCHEMATIC.md`
- `.prompts/codex/06_REVIEW_SCHEMATIC.md`
- `.prompts/claude/05_PLAN_SCHEMATIC.md`
- `.prompts/claude/06_REVIEW_SCHEMATIC.md`

Exact prompt additions needed:

- require explicit rotate/flip/reposition attempt before local labels
- require label-keep justification for each remaining local control label
- require object-type proof for dark rails
- require net-map truth proof for critical local rails
- require switch-press topology proof for reset/boot
- require explicit rejection of local loopback/S-path wiring

## Tool Files Needing Updates

- `03_TOOLS/scripts/schematic_quality/run_schematic_quality_gate.py`
- `03_TOOLS/scripts/schematic_quality/audit_wire_vs_label_balance.py`
- `03_TOOLS/scripts/schematic_quality/audit_schematic_block_layout.py`
- `03_TOOLS/scripts/schematic_quality/audit_schematic_text_overlaps.py`
- `03_TOOLS/scripts/schematic_quality/schematic_quality_common.py`

Recommended new scripts:

- `03_TOOLS/scripts/schematic_quality/audit_graphic_vs_electrical_lines.py`
- `03_TOOLS/scripts/schematic_quality/audit_local_wire_path_quality.py`
- `03_TOOLS/scripts/schematic_quality/audit_text_ownership.py`
- `03_TOOLS/scripts/schematic_quality/audit_local_mcu_support_wiring.py`
- `03_TOOLS/scripts/schematic_quality/audit_reset_boot_topology_sanity.py`
- `03_TOOLS/scripts/schematic_quality/audit_ground_return_presentation.py`

## Blocker-Map And Gate Files Needing Updates

- `00_CODEX_START/TASK_TYPE_TO_RULE_MAP.md`
- `00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md`
- `00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md`
- `34_SCHEMATIC_QUALITY_ENGINE/VISUAL_READABILITY_SCORECARD.md`
- `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_LAYOUT_ALGORITHM.md`
- `09_ACCURACY_ENGINE/checklists/SCHEMATIC_HUMAN_READABILITY_CHECKLIST.md`
- `09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md`

Required gate behavior change:

- block schematic visual cleanup from closing as effectively acceptable when critical local blocks still have avoidable local labels, weak orientation, or unproven topology
- do not allow `PASS_WITH_MINOR_WARNINGS` to stand as a protected drafting baseline for reset/boot, MCU support, or power-return areas

## Recommended Repair Plan

| Repair item | Why | Files | Safe to auto-fix |
| --- | --- | --- | --- |
| Add explicit orientation-before-label rule to the core schematic-quality engine | Current prompt language is not enough without core rule support. | `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_READABILITY_STANDARD.md`, `SCHEMATIC_BLOCK_LAYOUT_RULES.md`, `VISUAL_READABILITY_SCORECARD.md`, `SCHEMATIC_LAYOUT_ALGORITHM.md` | `YES` |
| Harden prompt pack with mandatory post-cleanup truth proof | Current prompts are improved but still do not force object/net/topology proof. | `.prompts/shared/HUMAN_DRAFTING_MODE.md`, pipeline/codex/claude schematic prompts | `YES` |
| Upgrade wire-vs-label audit from crude counts to drafting heuristics | Current `PASS`/`WARN` logic misses avoidable local labels. | `audit_wire_vs_label_balance.py`, `schematic_quality_common.py` | `YES` |
| Add graphic-vs-electrical line audit | Dark rails can visually pass while hiding object-type mistakes. | new `audit_graphic_vs_electrical_lines.py`, `run_schematic_quality_gate.py` | `YES` |
| Add reset/boot topology sanity audit | Visual cleanup can still leave unsafe switch behavior. | new `audit_reset_boot_topology_sanity.py`, `ESP32_BOOT_RESET_RULES.md`, `run_schematic_quality_gate.py` | `YES` |
| Add local MCU support physical-wiring audit | Nearby support circuits should usually be shown physically, not label-first. | new `audit_local_mcu_support_wiring.py`, `SCHEMATIC_WIRING_VS_LABEL_RULES.md` | `YES` |
| Add local wire-path quality audit for loopbacks/S-shapes | Human drafting rejects many short-path loopbacks that current scripts ignore. | new `audit_local_wire_path_quality.py`, `SCHEMATIC_LAYOUT_ALGORITHM.md` | `YES` |
| Add text-ownership audit | Non-overlap is not enough when fields visually drift. | new `audit_text_ownership.py`, `audit_schematic_text_overlaps.py` | `YES` |
| Add ground/common-return presentation rule and audit | Ground rails should be both electrically true and visually intentional. | new `audit_ground_return_presentation.py`, `SCHEMATIC_READABILITY_STANDARD.md` | `YES` |
| Tighten gate language so critical local blocks cannot close as `PASS_WITH_MINOR_WARNINGS` | This was the report-level leak. | `TASK_TYPE_TO_BLOCKERS.md`, `HUMAN_READABLE_SCHEMATIC_RULES.md`, `SCHEMATIC_HUMAN_READABILITY_CHECKLIST.md`, gate report writers | `YES` |
| Reconstruct historical prompt diffs for precise blame assignment | Useful for repo archaeology, not necessary for the repair itself. | git history only | `NO` |

## Exact Repo Workflow Flaws Exposed

1. The repo had readability guidance, but not a hard drafting sequence.
2. The repo scored geometry more strongly than schematic drafting judgment.
3. The repo treated local-control topology truth as separate from visual cleanup instead of mandatory inside it.
4. The repo allowed soft visual-pass language to coexist with unresolved drafting debt.
5. The repo did not protect good manual baselines quickly enough after the user improved them.

## Recommended Next Step

Run a narrow repo-hardening pass, not a design-edit pass.

Suggested next prompt:

```text
Active repo:
C:\Users\LJ\GitHub\KICAD_ENGINE

TASK:
Repair the schematic human-drafting workflow gaps identified in
05_OUTPUTS\release_readiness\SCHEMATIC_HUMAN_DRAFTING_ROOT_CAUSE_AUDIT.md
without editing any KiCad design files.

Scope:
- tighten the schematic-quality rule layer
- tighten the schematic prompt layer
- add or upgrade schematic-quality scripts
- update blocker/gate mapping so critical local drafting debt cannot close as PASS_WITH_MINOR_WARNINGS

Required repairs:
1. Add an explicit orientation-before-label rule.
2. Add graphic-line vs electrical-wire verification for visually important rails.
3. Add local MCU support physical-wiring guidance and warnings.
4. Add reset/boot topology sanity checks.
5. Add ground/common-return presentation-quality rules.
6. Add local loopback/S-path drafting warnings.
7. Add text-ownership checks beyond overlap.
8. Make these checks visible in run_schematic_quality_gate.py and blocker maps.

Validation:
- run the updated repo scripts in no-write mode where possible
- create a repair report
- do not edit .kicad_sch or .kicad_pcb
```

