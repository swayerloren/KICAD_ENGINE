# FreeRouting Feasibility Integration Commands

Date: `2026-05-07`

## Commands Run

1. Read-first and startup-context inspection:

```powershell
Get-Content AGENTS.md
Get-Content README_GPT.md
Get-Content "FOR CHAT GPT.MD"
Get-Content 14_LAYOUT_AUTOMATION\README.md
Get-Content 34_PCB_LAYOUT_SANDBOX\ROUTING_FEASIBILITY_RULES.md
Get-Content 34_PCB_LAYOUT_SANDBOX\VARIANT_SCORING_RULES.md
Get-Content 00_CODEX_START\CURRENT_PROJECT.md
Get-Content 00_CODEX_START\PROMPT_COUNTER_RULES.md
```

2. Prompt-counter and maintenance gate:

```powershell
python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
python 03_TOOLS/scripts/memory_maintenance/run_memory_maintenance.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS/scripts/memory_maintenance/reset_prompt_counter_after_maintenance.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply
```

Result:

- Prompt counter hit the maintenance threshold.
- Maintenance ran successfully.
- Prompt counter reset to `0`.

3. Baseline no-design-file hash capture:

```powershell
Get-FileHash '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro' | ForEach-Object { "$($_.Path)|$($_.Hash)" }
```

4. Existing FreeRouting-plan and reference discovery:

```powershell
Get-Content 14_LAYOUT_AUTOMATION\FREEROUTING_INTEGRATION_PLAN.md
Get-Content 14_LAYOUT_AUTOMATION\KICAD_AUTOROUTER_OPTIONS.md
Get-Content 14_LAYOUT_AUTOMATION\ROUTING_ASSISTANCE_PLAN.md
rg --files -g '*freerouting.py' -g '*freerouting*' 03_TOOLS
Get-Content 03_TOOLS\repos\kicad-mcp-pro\src\kicad_mcp\utils\freerouting.py
Get-Content 03_TOOLS\repos\KiCAD-MCP-Server\src\tools\freerouting.ts
Get-Content 03_TOOLS\repos\kicad-mcp-pro\tests\unit\test_freerouting.py
```

5. Style and handoff-reference inspection:

```powershell
Get-Content 02_HISTORY\design_reviews\PCB_VARIANT_SCORING_SYSTEM_AUDIT.md
Get-Content 02_HISTORY\sessions\PCB_LAYOUT_SANDBOX_LAYER_CREATED.md
Get-Content 02_HISTORY\command_logs\PCB_VARIANT_SCORING_SYSTEM_COMMANDS.md
Get-Content 34_PCB_LAYOUT_SANDBOX\INDEX.md
Get-Content 14_LAYOUT_AUTOMATION\INDEX.md
Get-Content 34_PCB_LAYOUT_SANDBOX\PCB_VARIANT_WORKFLOW.md
Get-Content 34_PCB_LAYOUT_SANDBOX\templates\VARIANT_SCORECARD_TEMPLATE.md
Get-Content 01_MEMORY\DESIGN_RULES_MEMORY.md
```

6. Validation:

```powershell
python -m py_compile 03_TOOLS/scripts/routing_feasibility/run_freerouting_dry_run.py 03_TOOLS/scripts/routing_feasibility/import_route_result_for_review.py 03_TOOLS/scripts/routing_feasibility/score_routing_feasibility.py 03_TOOLS/scripts/routing_feasibility/parse_unrouted_and_vias.py
$null = [System.Management.Automation.Language.Parser]::ParseFile('03_TOOLS/scripts/routing_feasibility/export_dsn_for_feasibility.ps1',[ref]$null,[ref]$null)
rg -n "FREEROUTING_FEASIBILITY_INTEGRATION|FREEROUTING_AS_VARIANT_SCORER|routing_feasibility_evidence_mode|REVIEW_ONLY" 14_LAYOUT_AUTOMATION 34_PCB_LAYOUT_SANDBOX README_GPT.md "FOR CHAT GPT.MD" 01_MEMORY\DESIGN_RULES_MEMORY.md
Get-FileHash '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro' | ForEach-Object { "$($_.Path)|$($_.Hash)" }
```

Result:

- Python syntax check passed.
- PowerShell parse check passed.
- Reference scan confirmed the new rule is wired into sandbox, layout-automation, handoff, and memory files.
- Final KiCad design-file hashes matched the baseline.

7. AI-quality closeout and index rebuild:

```powershell
python 03_TOOLS/scripts/ai_quality/create_ai_self_review.py --repo-root . --scope global --title "FreeRouting Feasibility Integration Self Review" --summary "Created an optional FreeRouting dry-run feasibility layer, scripts, and sandbox scoring integration without touching KiCad design files." --details "The task stayed in repo-doc, sandbox-rule, script, and handoff-memory scope. The new layer treats FreeRouting as REVIEW_ONLY congestion and feasibility evidence, not final routing. The scripts stage DSN inputs, run optional dry-run routing, parse coarse metrics, score feasibility, and stage SES bundles for review without modifying the canonical board." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_FILE --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "Created 14_LAYOUT_AUTOMATION/FREEROUTING_FEASIBILITY_INTEGRATION.md, 34_PCB_LAYOUT_SANDBOX/FREEROUTING_AS_VARIANT_SCORER.md, and 03_TOOLS/scripts/routing_feasibility/*; updated sandbox workflow, scoring rules, template, memory, and handoff docs; python -m py_compile passed; PowerShell parse check passed; final KiCad hash recheck matched the baseline." --issue "The new FreeRouting layer still needs a first live dry run on a copied or sandbox board candidate."
python 03_TOOLS/scripts/ai_quality/create_response_scorecard.py --repo-root . --scope global --title "FreeRouting Feasibility Integration AI Response Scorecard" --summary "An optional FreeRouting feasibility layer was added with conservative review-only boundaries, helper scripts, and sandbox integration." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_FILE --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "Direct file reads, patch results, py_compile validation, PowerShell parse validation, reference scans, and pre/post KiCad file hashes." --issue "No first live dry run has been captured yet for the new scripts." --overall-score 97 --evidence-support 19 --kicad-correctness 20 --datasheet-accuracy 15 --safety-compliance 15 --memory-routing 10 --uncertainty-disclosure 8 --usefulness 10
python 03_TOOLS/scripts/ai_quality/create_claim_evidence_matrix.py --repo-root . --scope global --title "FreeRouting Feasibility Integration Claim Evidence Matrix" --summary "KiCad Engine now has an optional FreeRouting-based routing-feasibility layer for sandbox layout comparison and congestion scoring." --details "The patch added design docs, routing-feasibility scripts, sandbox scoring/template hooks, memory updates, and handoff notes while keeping all FreeRouting outputs review-only and leaving KiCad design files untouched." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_FILE --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "14_LAYOUT_AUTOMATION/FREEROUTING_FEASIBILITY_INTEGRATION.md, 34_PCB_LAYOUT_SANDBOX/FREEROUTING_AS_VARIANT_SCORER.md, 03_TOOLS/scripts/routing_feasibility/*, 34_PCB_LAYOUT_SANDBOX/VARIANT_SCORING_RULES.md, templates/VARIANT_SCORECARD_TEMPLATE.md, README_GPT.md, FOR CHAT GPT.MD, and 01_MEMORY/DESIGN_RULES_MEMORY.md." --issue "The script layer is syntax-checked but not yet proven by a first live dry run."
python 03_TOOLS/scripts/ai_quality/create_uncertainty_log.py --repo-root . --scope global --title "FreeRouting Feasibility Integration Uncertainty Log" --summary "The FreeRouting feasibility layer is implemented and validated structurally, but its scripts have not yet been exercised on a real copied board candidate." --details "The main residual uncertainty is operational: DSN export ergonomics, FreeRouting output variability, and SES metric parsing may need small adjustments after the first live dry run. The current validation scope covers file inspection, syntax checks, PowerShell parse validation, reference scans, and final KiCad hash confirmation only." --severity MEDIUM --confidence HIGH --claim-status PARTIALLY_VERIFIED --risk-label LOW_RISK --gate-result PASS_WITH_WARNINGS --human-review-required NO --evidence "py_compile passed for the Python scripts; the PowerShell script parsed successfully; readback and rg scans confirmed the docs and memory links; final KiCad hashes matched the baseline." --issue "First live dry-run evidence is still required for end-to-end confidence."
python 03_TOOLS/scripts/ai_quality/create_hallucination_risk_log.py --repo-root . --scope global --title "FreeRouting Feasibility Integration Hallucination Risk Log" --summary "This task had low hallucination risk because it was constrained to local repo files, explicit workflow boundaries, and syntax or parse validation." --details "The main risk was overstating FreeRouting readiness. That was controlled by keeping the feature explicitly optional, review-only, and unproven until a first live dry run exists. A second risk was implying KiCad design-file edits; that was controlled by pre/post hash checks on the active project's .kicad_pcb, .kicad_sch, and .kicad_pro files." --severity LOW --confidence HIGH --claim-status VERIFIED_BY_COMMAND --risk-label LOW_RISK --gate-result PASS --human-review-required NO --evidence "Local file patches, direct readback, py_compile output, PowerShell parse validation, rg reference scan, and final KiCad hash recheck." --issue "No unresolved hallucination blocker was identified."
python 03_TOOLS/scripts/memory_maintenance/rebuild_history_indexes.py --repo-root . --apply
python 03_TOOLS/scripts/memory_maintenance/rebuild_memory_indexes.py --repo-root . --apply
python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_repo_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_known_problems.py --repo-root .
```

8. Failed-attempt capture:

```powershell
apply_patch
```

Result:

- One patch-context mismatch occurred while updating `34_PCB_LAYOUT_SANDBOX/PCB_VARIANT_WORKFLOW.md`.
- The file was read back, the patch context was corrected, and the next patch succeeded.
- Failure record: `02_HISTORY/failed_attempts/FREEROUTING_FEASIBILITY_INTEGRATION_APPLYPATCH_CONTEXT_MISMATCH.md`
