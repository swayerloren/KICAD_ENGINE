# AUTO_PCB_START_WORKFLOW_AUDIT

## Summary

Date: `2026-05-07`

Classification: `WORKFLOW_PATCH_COMPLETE`

This patch adds the explicit workflow gate that allows Codex/Claude to continue from an auto-approved sandbox layout plan into real KiCad PCB setup work without waiting for generic LJ approval.

## Files Created

- `09_ACCURACY_ENGINE/workflows/AUTO_PCB_START_WORKFLOW.md`
- `09_ACCURACY_ENGINE/checklists/AUTO_PCB_START_CHECKLIST.md`
- `34_PCB_LAYOUT_SANDBOX/templates/AUTO_PCB_START_REPORT_TEMPLATE.md`

## Files Updated

- `34_PCB_LAYOUT_SANDBOX/PCB_WORK_AUTO_START_RULES.md`
- `09_ACCURACY_ENGINE/workflows/CREATE_PCB_WORKFLOW.md`
- `09_ACCURACY_ENGINE/workflows/SCHEMATIC_TO_PCB_GATE_WORKFLOW.md`
- `09_ACCURACY_ENGINE/checklists/FULL_PIPELINE_GATE_CHECKLIST.md`
- `.prompts/kicad_pipeline/07_update_pcb_from_schematic.md`
- `.prompts/kicad_pipeline/08_pcb_mechanical_setup.md`
- `.prompts/kicad_pipeline/09_pcb_placement_pass_1.md`
- `AGENTS.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `00_CODEX_START/START_HERE.md`
- `01_MEMORY/DESIGN_RULES_MEMORY.md`

## Rule Outcome

The workflow now states that Codex/Claude may automatically proceed into:

1. PCB update from schematic
2. real `.kicad_pcb` creation/update
3. board outline application
4. fixed mechanical placement
5. main component-group placement
6. DRC
7. placement/mechanical visual review export

only when all auto-start preconditions pass.

## Mandatory Auto-Start Preconditions

- `SCHEMATIC_TO_PCB_GATE_STATUS.md` exact `PASS`
- footprint/package gate `PASS` or `SAFE_CANDIDATE_WITH_EVIDENCE`
- selected layout plan exists
- auto-approval report says `AUTO_APPROVED_FOR_PCB_WORK`
- board dimensions exist
- connector-orientation plan exists
- antenna-keepout plan exists when RF is present
- routing-feasibility plan exists

## Block Behavior

If any precondition fails, the required status is now `AUTO_PCB_START_BLOCKED` with exact blockers.

The patch removes generic approval language for this transition.

## Boundaries Preserved

This patch does not auto-approve:

- final routing
- fab output generation
- fabrication-ready classification
- DRC bypass
- ignoring connector, antenna, USB, RF, or power-path risks

## Validation

- Active project KiCad hashes were rechecked after the workflow patch.
- No `.kicad_pcb`, `.kicad_sch`, or `.kicad_pro` files changed.
- Repo, memory, history, AI-quality, and known-problem indexes were rebuilt.

## Residual Risk

The workflow is documented and wired into startup and prompt-pack files, but it still needs a first live run on a copied or active project task where all objective gates actually pass.
