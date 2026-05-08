# Auto Variant Scoring Engine Commands

Date: `2026-05-07`

Workdir: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Commands Run

```powershell
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply
Get-Content AGENTS.md
Get-Content README_GPT.md
Get-Content 'FOR CHAT GPT.MD'
Get-Content 00_CODEX_START\START_HERE.md
Get-Content 00_CODEX_START\CURRENT_PROJECT.md
Get-Content 34_PCB_LAYOUT_SANDBOX\AUTO_SANDBOX_APPROVAL_RULES.md
Get-Content 34_PCB_LAYOUT_SANDBOX\AUTO_LAYOUT_DECISION_ENGINE.md
Get-Content 34_PCB_LAYOUT_SANDBOX\VARIANT_SCORING_RULES.md
Get-ChildItem 34_PCB_LAYOUT_SANDBOX\scripts
Get-Content 34_PCB_LAYOUT_SANDBOX\scripts\score_layout_variant.py
Get-Content 34_PCB_LAYOUT_SANDBOX\scripts\compare_layout_variants.py
Get-Content 34_PCB_LAYOUT_SANDBOX\AUTO_APPROVAL_STATUS_CODES.md
python -m py_compile 34_PCB_LAYOUT_SANDBOX/scripts/score_layout_variant.py 34_PCB_LAYOUT_SANDBOX/scripts/compare_layout_variants.py 34_PCB_LAYOUT_SANDBOX/scripts/auto_select_best_variant.py 34_PCB_LAYOUT_SANDBOX/scripts/auto_approve_selected_variant.py
python 34_PCB_LAYOUT_SANDBOX/scripts/score_layout_variant.py 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_a.json --format json --output 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_a.score.json
python 34_PCB_LAYOUT_SANDBOX/scripts/score_layout_variant.py 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_b.json --format json --output 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_b.score.json
python 34_PCB_LAYOUT_SANDBOX/scripts/score_layout_variant.py 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_c.json --format json --output 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_c.score.json
python 34_PCB_LAYOUT_SANDBOX/scripts/compare_layout_variants.py 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_a.json 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_b.json 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_c.json --format json --output 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_compare.json
python 34_PCB_LAYOUT_SANDBOX/scripts/auto_select_best_variant.py 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_a.json 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_b.json 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_c.json --format json --output 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/auto_selected.json
python 34_PCB_LAYOUT_SANDBOX/scripts/auto_approve_selected_variant.py 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/auto_selected.json 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/approval_context_pass.json --format json --output 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/auto_approved.json
Get-FileHash '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro' | ForEach-Object { "$($_.Path)|$($_.Hash)" }
```

## Notes

- Two failed dry-run attempts are recorded separately: one dependency race from parallel execution order, and one context-schema bug in the first approval-script pass.

