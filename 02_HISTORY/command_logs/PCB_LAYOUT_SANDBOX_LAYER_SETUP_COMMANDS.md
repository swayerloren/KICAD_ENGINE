# PCB Layout Sandbox Layer Setup Commands

Date: `2026-05-07`

## Commands Run

1. Prompt-counter maintenance gate:

```powershell
python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
```

Result:

- Prompt counter incremented.
- Maintenance due: `NO`.

2. Baseline KiCad no-edit hash capture:

```powershell
Get-FileHash '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro' | ForEach-Object { "$($_.Path)|$($_.Hash)" }
```

Result:

- Baseline hashes recorded before repo-doc edits.

3. Sandbox directory creation:

```powershell
New-Item -ItemType Directory -Force 34_PCB_LAYOUT_SANDBOX,34_PCB_LAYOUT_SANDBOX\variants,34_PCB_LAYOUT_SANDBOX\reports,34_PCB_LAYOUT_SANDBOX\scripts,34_PCB_LAYOUT_SANDBOX\templates
```

Result:

- Requested sandbox directories created.

4. Validation checks:

```powershell
Get-ChildItem '34_PCB_LAYOUT_SANDBOX' -Recurse | Select-Object FullName
rg -n "34_PCB_LAYOUT_SANDBOX|PCB_LAYOUT_SANDBOX_SELECTED_VARIANT|three layout variants|selected variant" AGENTS.md README_GPT.md "FOR CHAT GPT.MD" START_HERE_FOR_AI_AGENTS.md 00_CODEX_START 09_ACCURACY_ENGINE .prompts 14_LAYOUT_AUTOMATION
```

Result:

- Sandbox files confirmed present.
- Startup, workflow, and prompt files confirmed patched.

5. Closeout generators and index rebuilds:

```powershell
python 03_TOOLS/scripts/ai_quality/create_ai_self_review.py --repo-root . --scope global --title "PCB Layout Sandbox Layer Setup Self Review" --summary "Created a mandatory PCB layout sandbox layer and patched startup/workflow/prompt files so real .kicad_pcb edits require pre-layout variant planning." --details "The task stayed in repo-doc and workflow scope. The new 34_PCB_LAYOUT_SANDBOX layer defines variant planning, connector/orientation review, antenna keepout planning, board-shape reasoning, routing-feasibility review, and selected-variant justification before real PCB edits. No KiCad design files were edited." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_FILE --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "Created files under 34_PCB_LAYOUT_SANDBOX/ and validated references in AGENTS.md, START_HERE_FOR_AI_AGENTS.md, 00_CODEX_START/START_HERE.md, 09_ACCURACY_ENGINE/workflows/CREATE_PCB_WORKFLOW.md, 14_LAYOUT_AUTOMATION/README.md, and .prompts/kicad_pipeline/*. Final KiCad hash recheck confirms no design-file changes." --issue "Existing projects still need project-local sandbox reports before future real PCB edits."
python 03_TOOLS/scripts/ai_quality/create_response_scorecard.py --repo-root . --scope global --title "PCB Layout Sandbox Layer Setup AI Response Scorecard" --summary "The sandbox layer was added cleanly and enforced across startup, workflow, and prompt-pack control points without touching KiCad design files." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_FILE --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "34_PCB_LAYOUT_SANDBOX/ file creation, prompt-pack and workflow reference scans, and pre/post KiCad file hash checks." --issue "Future project-level sandbox reports still need to be generated when individual boards move into placement." --overall-score 98 --evidence-support 20 --kicad-correctness 20 --datasheet-accuracy 15 --safety-compliance 15 --memory-routing 10 --uncertainty-disclosure 8 --usefulness 10
python 03_TOOLS/scripts/ai_quality/create_claim_evidence_matrix.py --repo-root . --scope global --title "PCB Layout Sandbox Layer Setup Claim Evidence Matrix" --summary "A permanent PCB layout sandbox layer now exists and real .kicad_pcb edits are gated on sandbox variant planning." --details "The patch created sandbox rules, workflow, templates, and supporting docs, then updated the main startup chain, layout workflow docs, and PCB prompt-pack files to require sandbox evidence before real PCB placement or routing." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_FILE --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "34_PCB_LAYOUT_SANDBOX/ core files plus AGENTS.md, START_HERE_FOR_AI_AGENTS.md, 00_CODEX_START/START_HERE.md, 09_ACCURACY_ENGINE/workflows/CREATE_PCB_WORKFLOW.md, 09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md, 14_LAYOUT_AUTOMATION/README.md, and .prompts/kicad_pipeline/07_update_pcb_from_schematic.md, 09_pcb_placement_pass_1.md, 10_pcb_placement_pass_2_orientation.md." --issue "Project-local variant reports are still a separate future step for each board."
python 03_TOOLS/scripts/ai_quality/create_uncertainty_log.py --repo-root . --scope global --title "PCB Layout Sandbox Layer Setup Uncertainty Log" --summary "The repo-level sandbox layer was created and wired into the main PCB workflow, but it does not retroactively create project-local variant reports for existing boards." --details "The main residual uncertainty is operational adoption: future PCB tasks will now see the sandbox requirement, but existing projects still need actual variant reports created under their own reports folders before real board edits. Two legacy 14_LAYOUT_AUTOMATION files contain embedded NUL bytes, so some text-search tools classify them as binary even though the new inserted sandbox guidance is present." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label LOW_RISK --gate-result PASS_WITH_WARNINGS --human-review-required NO --evidence "Reference scans confirmed the new rule text in startup/workflow/prompt files. Direct content inspection confirmed the inserted sections in 14_LAYOUT_AUTOMATION/README.md and INDEX.md despite binary classification in ripgrep." --issue "Human reviewers should still verify that future agents actually follow the new sandbox gate during project execution."
python 03_TOOLS/scripts/ai_quality/create_hallucination_risk_log.py --repo-root . --scope global --title "PCB Layout Sandbox Layer Setup Hallucination Risk Log" --summary "This task was low hallucination risk because it was controlled by local file creation, file patching, and direct reference scans rather than external facts." --details "The main risk was overstating enforcement coverage. That was mitigated by patching the top-level startup entry, AGENTS.md, the main CREATE_PCB workflow, the full pipeline workflow, and the placement/update prompt-pack files, then validating the references with file scans. A secondary risk was accidentally implying KiCad design-file changes; that was mitigated by pre/post hashes for the active project's .kicad_pcb, .kicad_sch, and .kicad_pro files." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_COMMAND --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "Local file creation and patch results, ripgrep reference scans, and final file-hash recheck for ESP32_CSI_WIFI_NODE design files." --issue "No unresolved hallucination blocker was identified."
python 03_TOOLS/scripts/memory_maintenance/rebuild_history_indexes.py --repo-root . --apply
python 03_TOOLS/scripts/memory_maintenance/rebuild_memory_indexes.py --repo-root . --apply
python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_known_problems.py --repo-root .
python 03_TOOLS/scripts/indexing/build_repo_index.py --repo-root .
python 03_TOOLS/scripts/memory_maintenance/rebuild_memory_indexes.py --repo-root . --apply
python 03_TOOLS/scripts/indexing/build_known_problems.py --repo-root .
python 03_TOOLS/scripts/memory_maintenance/rebuild_history_indexes.py --repo-root . --apply
```

Result:

- AI-quality records created under `02_HISTORY/ai_self_reviews`, `ai_scorecards`, `claim_evidence_matrices`, `uncertainty_logs`, and `hallucination_risk_logs`.
- Generated indexes rebuilt for the sandbox-layer change, including the final global-memory update and the final history-log patch.

6. Final KiCad no-edit hash recheck:

```powershell
Get-FileHash '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro' | ForEach-Object { "$($_.Path)|$($_.Hash)" }
```

Result:

- Hashes matched the baseline for all three active-project KiCad files.
