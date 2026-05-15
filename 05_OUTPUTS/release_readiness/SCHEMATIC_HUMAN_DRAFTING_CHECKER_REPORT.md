# Schematic Human Drafting Checker Report

Generated: `2026-05-14`
Classification: `HUMAN_DRAFTING_CHECKER_ADDED`
Task type: `DOCS_ONLY`
Active repo: `C:\Users\LJ\GitHub\KICAD_ENGINE`
KiCad design-file edits by this task: `NONE`

## Scope

Add a read-only schematic human-drafting checker that flags drafting and
topology-risk problems earlier than ERC, text-overlap, and coarse
wire-vs-label checks, without editing any KiCad design files.

## Files Changed

- `03_TOOLS/scripts/schematic_quality/check_schematic_human_drafting_quality.py`
- `03_TOOLS/scripts/schematic_quality/README.md`
- `34_SCHEMATIC_QUALITY_ENGINE/README.md`
- `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_READABILITY_STANDARD.md`
- `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_VISUAL_AUDIT_RULES.md`
- `.prompts/shared/HUMAN_DRAFTING_MODE.md`
- `.prompts/kicad_pipeline/02_schematic_visual_cleanup.md`
- `.prompts/kicad_pipeline/03_schematic_visual_repair.md`
- `.prompts/codex/06_REVIEW_SCHEMATIC.md`
- `.prompts/claude/06_REVIEW_SCHEMATIC.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `05_OUTPUTS/release_readiness/SCHEMATIC_HUMAN_DRAFTING_CHECKER_REPORT.md`
- `02_HISTORY/sessions/SCHEMATIC_HUMAN_DRAFTING_CHECKER_SESSION.md`
- `02_HISTORY/command_logs/SCHEMATIC_HUMAN_DRAFTING_CHECKER_COMMANDS.md`
- `02_HISTORY/ai_self_reviews/SCHEMATIC_HUMAN_DRAFTING_CHECKER_AI_SELF_REVIEW.md`
- `02_HISTORY/ai_scorecards/SCHEMATIC_HUMAN_DRAFTING_CHECKER_SCORECARD.md`
- `02_HISTORY/claim_evidence_matrices/SCHEMATIC_HUMAN_DRAFTING_CHECKER_CLAIM_EVIDENCE_MATRIX.md`
- `02_HISTORY/uncertainty_logs/SCHEMATIC_HUMAN_DRAFTING_CHECKER_UNCERTAINTY_LOG.md`
- `02_HISTORY/hallucination_risk_logs/SCHEMATIC_HUMAN_DRAFTING_CHECKER_HALLUCINATION_RISK_LOG.md`
- `02_HISTORY/failed_attempts/SCHEMATIC_HUMAN_DRAFTING_CHECKER_FAILED_ATTEMPTS.md`
- `02_HISTORY/issue_logs/SCHEMATIC_HUMAN_DRAFTING_CHECKER_FOLLOWUP.md`
- `05_OUTPUTS/release_readiness/SCHEMATIC_HUMAN_DRAFTING_CHECKER_TASK_CONTRACT.json`
- `05_OUTPUTS/release_readiness/SCHEMATIC_HUMAN_DRAFTING_CHECKER_TASK_CONTRACT_REPORT.md`

Closeout also regenerated:

- `00_CODEX_START/REPO_INDEX.generated.json`
- `00_CODEX_START/REPO_INDEX.generated.md`
- `01_MEMORY/MASTER_MEMORY_INDEX.md`
- `00_CODEX_START/MEMORY_INDEX.generated.json`
- `00_CODEX_START/MEMORY_INDEX.generated.md`
- `02_HISTORY/MASTER_HISTORY_INDEX.md`
- `00_CODEX_START/HISTORY_INDEX.generated.json`
- `00_CODEX_START/HISTORY_INDEX.generated.md`
- `00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md`

## Checker Capabilities

The new checker parses `.kicad_sch` geometry directly and, when `kicad-cli` is
available, exports a temporary read-only XML netlist for saved-net truth.

Implemented checks:

1. Graphic-line electrical-risk check
   - Detects top-level graphic items.
   - Warns when a graphic item looks like a rail near electrical content.

2. Local label overuse check
   - Classifies labels as:
     - `KEEP_POWER_RAIL`
     - `KEEP_CROSS_BLOCK_SIGNAL`
     - `KEEP_DEBUG_LABEL`
     - `REVIEW_LOCAL_LABEL`
     - `POSSIBLE_REPLACE_WITH_WIRE`

3. Orientation-before-label heuristic
   - Flags repeated compact local labels that suggest symbol orientation or
     local physical wiring should be reviewed first.

4. MCU local support check
   - Reviews `ESP_EN`, `BOOT0`, and `STATUS_LED` style local nets.
   - Warns when compact MCU support nets still rely on label shortcuts.
   - Warns when `STATUS_LED` naming is not preserved in the saved netlist.

5. Reset/boot topology sanity
   - Detects direct `+3V3` to `GND` switch short paths.
   - Detects reset switch topology that does not actually pull `ESP_EN` to
     `GND`.
   - Detects EN support capacitor return mistakes.
   - Warns on local `+3V3` decoupling capacitors that do not return to `GND`.

6. Text ownership check
   - Flags visible reference/value text that appears detached from its owner or
     closer to the wrong symbol.

7. Wire path quality heuristic
   - Flags suspicious local loopback or S-shaped wire paths when detectable.

8. Ground/power rail presentation
   - Flags suspicious local return-style clusters that visually read like a
     common return but are not actually on `GND`.

## ESP32 Validation Result

Validation output:

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_quality/20260514_165956/human_drafting_quality.json`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_quality/20260514_165956/human_drafting_quality.md`

Checker result on `ESP32_CSI_WIFI_NODE.kicad_sch`:

- Overall status: `FAIL`
- Counts: `FAIL=4`, `WARN=9`, `INFO=9`

Key useful findings:

- `SW1` does not resolve to the expected `ESP_EN -> GND` reset topology.
- `SW2` directly shorts `+3V3` to `GND` when pressed.
- `C3` does not return `ESP_EN` to `GND`.
- `C4` and `C6` are local `+3V3` decoupling capacitors that do not return to
  `GND`.
- The local return-style cluster `Net-(D1-K)` is not actually `GND`.
- The saved netlist does not preserve a named `STATUS_LED` net.
- `ESP_EN` and `BOOT0` labels are now explicitly reported as local MCU support
  label shortcuts that deserve physical-wiring review.
- No top-level graphic line objects were found, so the dark-return concern in
  this sheet is saved-net truth, not fake graphics.

This means the checker is useful on the exact failure class that motivated the
task, not just on generic overlap cleanup.

## Prompt And Documentation Integration

Updated repo docs and prompt surfaces now point future schematic cleanup/review
work at the checker:

- script-layer README
- schematic-quality engine README
- schematic readability standard
- schematic visual audit rules
- shared human drafting prompt
- pipeline cleanup/repair prompts
- Codex and Claude schematic review prompts
- startup handoff docs (`README_GPT.md`, `FOR CHAT GPT.MD`)

## Validation

### Checker execution

- `python 03_TOOLS/scripts/schematic_quality/check_schematic_human_drafting_quality.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --warn-only`
  - result: reports written successfully
- same command without `--warn-only`
  - result: exit code `1` on `FAIL`, as required

### Health check

- `python health_check.py --repo-root . --no-write`
  - result: `PASS=18 WARN=2 FAIL=0`

### No KiCad design / PCB / fab edits

- This task did not edit `.kicad_sch`, `.kicad_pcb`, `.kicad_pro`, or
  fabrication outputs.
- The repo worktree already contains unrelated and pre-existing KiCad/project
  modifications outside this task; they were not reverted or altered here.
- The task contract remains `DOCS_ONLY`.

## Known Limitations

- The checker is heuristic and may produce false positives.
- Block attribution still depends on coarse functional-block geometry, not a
  full human intent model.
- It does not replace human rendered-page review.
- It does not replace ERC, native annotation proof, datasheet proof, or
  footprint/package verification.
- It is documented and prompt-routed now, but not yet wired into
  `run_schematic_quality_gate.py` as a first-class gate audit.

## Recommended Next Prompt

```text
Read START_HERE_FOR_AI_AGENTS.md and route yourself correctly.

Active repo:
C:\Users\LJ\GitHub\KICAD_ENGINE

TASK:
Integrate the new read-only schematic human-drafting checker into the schematic
quality gate layer without editing KiCad design files.

READ FIRST:
- 05_OUTPUTS\release_readiness\SCHEMATIC_HUMAN_DRAFTING_CHECKER_REPORT.md
- 03_TOOLS\scripts\schematic_quality\check_schematic_human_drafting_quality.py
- 03_TOOLS\scripts\schematic_quality\run_schematic_quality_gate.py
- 34_SCHEMATIC_QUALITY_ENGINE\
- .prompts/shared/HUMAN_DRAFTING_MODE.md

IMPLEMENT:
1. add the checker to run_schematic_quality_gate.py as a read-only audit
2. decide which findings should be WARN vs FAIL at gate level
3. update combined schematic quality reporting
4. keep unrelated workflows stable

VALIDATE:
- run the updated gate on ESP32_CSI_WIFI_NODE in no-write mode
- run health_check.py --repo-root . --no-write
- confirm no KiCad design files changed
```
