# Schematic Human Drafting Rule Patch Report

Generated: `2026-05-14`
Classification: `SCHEMATIC_HUMAN_DRAFTING_RULES_PATCHED`
Task type: `DOCS_ONLY`
Active repo: `C:\Users\LJ\GitHub\KICAD_ENGINE`
KiCad design-file edits: `NONE`

## Scope

Patch KICAD_ENGINE so future schematic creation, repair, visual cleanup, and
review tasks must apply human drafting rules before local net labels and before
gate claims.

## Inputs Used

- `05_OUTPUTS/release_readiness/SCHEMATIC_HUMAN_DRAFTING_ROOT_CAUSE_AUDIT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/USER_MANUAL_PRESENTATION_BASELINE_ANALYSIS.md`
- `34_SCHEMATIC_QUALITY_ENGINE/`
- `09_ACCURACY_ENGINE/schematic_rules/`
- `.prompts/kicad_pipeline/`
- `.prompts/codex/`
- `.prompts/claude/`
- `00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md`
- `00_CODEX_START/TASK_TYPE_TO_RULE_MAP.md`
- `00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md`

## Files Changed

### Rule And Gate Layer

- `34_SCHEMATIC_QUALITY_ENGINE/README.md`
- `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_WIRING_VS_LABEL_RULES.md`
- `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_READABILITY_STANDARD.md`
- `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_BLOCK_LAYOUT_RULES.md`
- `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_VISUAL_AUDIT_RULES.md`
- `34_SCHEMATIC_QUALITY_ENGINE/LOCAL_WIRING_STYLE_GUIDE.md`
- `09_ACCURACY_ENGINE/schematic_rules/WIRE_VS_NET_LABEL_RULES.md`
- `09_ACCURACY_ENGINE/schematic_rules/READABLE_SCHEMATIC_FLOW_RULES.md`
- `09_ACCURACY_ENGINE/schematic_rules/REFERENCE_VALUE_TEXT_PLACEMENT_RULES.md`
- `09_ACCURACY_ENGINE/schematic_rules/ESP32_BOOT_RESET_RULES.md`
- `09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md`
- `09_ACCURACY_ENGINE/checklists/SCHEMATIC_HUMAN_READABILITY_CHECKLIST.md`

### Routing And Blocker Maps

- `00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md`
- `00_CODEX_START/TASK_TYPE_TO_RULE_MAP.md`
- `00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md`

### Prompt Layer

- `.prompts/shared/HUMAN_DRAFTING_MODE.md`
- `.prompts/kicad_pipeline/02_schematic_visual_cleanup.md`
- `.prompts/kicad_pipeline/02_schematic_visual_closeup_audit.md`
- `.prompts/kicad_pipeline/03_schematic_visual_repair.md`
- `.prompts/kicad_pipeline/03_schematic_electrical_review.md`
- `.prompts/codex/05_PLAN_SCHEMATIC.md`
- `.prompts/codex/06_REVIEW_SCHEMATIC.md`
- `.prompts/claude/05_PLAN_SCHEMATIC.md`
- `.prompts/claude/06_REVIEW_SCHEMATIC.md`

### Startup Handoff

- `README_GPT.md`
- `FOR CHAT GPT.MD`

## Rules Added Or Strengthened

### `ORIENT_SYMBOLS_BEFORE_LABELS`

Strengthened in the rule layer and prompt layer so local labels are now a
fallback after rotate/flip/mirror/reposition decisions, not a shortcut for bad
symbol orientation.

### `LOCAL_WIRE_BEFORE_NET_LABEL`

Strengthened so short orthogonal same-block connections must prefer physical
wires, with explicit allowed label exceptions limited to rails, cross-block
nets, test/debug anchors, and cases where a wire would be worse.

### `MCU_LOCAL_SUPPORT_PHYSICAL_WIRING`

Added explicitly to the rule and prompt stack for local MCU/module support
circuits:

- `EN`, `RESET`, `ESP_EN`
- `BOOT0`, `IO0`, strap pins
- local reset/boot switches
- pullups/pulldowns
- local LEDs
- local decoupling

If a label remains in these local circuits, the reporting language now requires
justification.

### `GRAPHIC_LINES_ARE_NOT_ELECTRICAL_WIRES`

Added to the prompt and rule stack so visually emphasized rails or return paths
must be proven as real wire/net objects on the intended nets. Graphics may
separate or frame blocks, but they are not electrical proof.

### `RESET_BOOT_TOPOLOGY_SANITY`

Strengthened in `ESP32_BOOT_RESET_RULES.md`, the shared drafting prompt, the
electrical review prompt, the visual review rules, and the blockers:

- reset switch must not imply or create a direct `+3V3` to `GND` short path
- boot switch must not imply or create a direct `+3V3` to `GND` short path
- pullup/pulldown behavior must remain readable and intentional
- local capacitor return intent must remain visible

### `TEXT_OWNERSHIP_REQUIRED`

Strengthened in the text-placement rule, human-readability rule, checklist, and
prompt pack:

- no detached values in blank space
- no value closer to the wrong symbol
- no wire path running through text when a readable alternative exists

### `HUMAN_PRESENTATION_REVIEW_REQUIRED`

Strengthened so ERC pass, text-overlap pass, and crop generation are now
insufficient for visual or readiness claims by themselves. Critical local
drafting debt can no longer be normalized into a soft pass.

### `GROUND_AND_POWER_RAIL_PRESENTATION`

Added to the shared drafting prompt and the rule layer so power, ground, and
common-return presentation must read intentionally, use natural symbol
orientation, and be proven as real wires on the intended nets.

## Prompt Updates

Prompt templates now explicitly mention:

- orientation-before-label
- local-wire-before-label
- local MCU support physical wiring
- graphic-line vs electrical-wire verification
- reset/boot topology sanity
- text ownership
- ground/power/common-return presentation
- no gate claim from ERC or crop automation alone

Updated prompt surfaces:

- shared drafting mode
- pipeline visual cleanup / close-up audit / visual repair / electrical review
- Codex plan/review schematic prompts
- Claude plan/review schematic prompts

## Route And Blocker Updates

The schematic create/repair and schematic visual cleanup routes now explicitly
point to:

- `READABLE_SCHEMATIC_FLOW_RULES.md`
- `WIRE_VS_NET_LABEL_RULES.md`
- `REFERENCE_VALUE_TEXT_PLACEMENT_RULES.md`
- `ESP32_BOOT_RESET_RULES.md`

The blocker layer now explicitly blocks pass claims when:

- critical local labels remain because orientation or wiring was not improved
- emphasized rails are being used without object/net verification
- reset/boot or local control topology remains hidden, ambiguous, or visually
  misleading

## Validation

### Health Check

- Command: `python health_check.py --repo-root . --no-write`
- Result: `PASS=18 WARN=2 FAIL=0`

### Route Reference Check

Confirmed:

- `00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md` now includes the strengthened
  schematic rule files for `SCHEMATIC_CREATE_OR_REPAIR` and
  `SCHEMATIC_VISUAL_CLEANUP`.
- `00_CODEX_START/TASK_TYPE_TO_RULE_MAP.md` now points those routes at the
  updated flow, wiring, text-ownership, and boot/reset rule surfaces.
- `00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md` now blocks pass claims when the
  new drafting rules are not satisfied.

### Prompt Coverage Check

Confirmed prompt templates now mention:

- orientation-before-label
- local-wire-before-label
- graphic-line verification
- reset/boot topology sanity
- human presentation review

## Confirmation Of No KiCad Design / PCB / Fab Changes

This task changed only rule files, prompt files, startup handoff files, and
history/release-readiness records.

No files of these types were edited by this task:

- `.kicad_sch`
- `.kicad_pcb`
- `.kicad_pro`
- fabrication outputs
- PCB routing or zone outputs

## Remaining Gaps

This patch hardens the rule, prompt, and blocker layers. It does not yet add
the deeper automated schematic-quality scripts recommended in the root-cause
audit, such as dedicated checks for:

- graphic-vs-electrical rail truth
- local wire path quality
- text ownership geometry
- local MCU support wiring heuristics
- reset/boot topology sanity
- ground/common-return presentation

Those remain the next tooling follow-up.

## Final Result

`SCHEMATIC_HUMAN_DRAFTING_RULES_PATCHED`

The repo now requires the intended human drafting decisions in the rule and
prompt path before schematic create/repair and visual gate claims. The next gap
is script-level enforcement, not missing policy language.

