# Strict Human Readable Schematic Rule Commands

Status: `RECORDED`

Date: 2026-05-06

## Commands And Actions

| Command / action | Result | Notes |
| --- | --- | --- |
| Read required files with `Get-Content` | `PASS` | Read AGENTS, README_GPT, FOR CHAT GPT, START_HERE, visual workflow, schematic standard, close-up rules, ESP32 final audit, and LJ packet. |
| Created strict visual rule files with `apply_patch` | `PASS` | Added human-readable schematic rules, automated-pass distinction, and human readability checklist. |
| Updated existing visual/accuracy/startup docs with `apply_patch` | `PASS` | Updated workflow, close-up rules, schematic standard, AGENTS, README_GPT, FOR CHAT GPT, and current known problems. |
| Updated global memory with `apply_patch` | `PASS` | Added reusable mistake and hallucination-risk entries for confusing automated crop pass with visual pass. |
| `python 03_TOOLS\scripts\memory_history\create_user_correction.py ...` | `PASS` | Created global user-correction record for the visual gate failure mode. |
| `python 03_TOOLS\scripts\ai_quality\create_ai_self_review.py ...` | `PASS` | Created AI self-review record. |
| `python 03_TOOLS\scripts\ai_quality\create_response_scorecard.py ...` | `PASS` | Created AI response scorecard record. |
| `python 03_TOOLS\scripts\ai_quality\create_claim_evidence_matrix.py ...` | `PASS` | Created claim/evidence matrix record. |
| `python 03_TOOLS\scripts\ai_quality\create_uncertainty_log.py ...` | `PASS` | Created uncertainty log noting no fresh schematic render audit was run in this rule-only task. |
| `python 03_TOOLS\scripts\ai_quality\create_hallucination_risk_log.py ...` | `PASS` | Created hallucination-risk log for automated visual artifacts being mistaken as approval. |
| `python 03_TOOLS\scripts\indexing\build_memory_index.py --repo-root .` | `PASS` | Rebuilt memory index. |
| `python 03_TOOLS\scripts\indexing\build_history_index.py --repo-root .` | `PASS` | Rebuilt history index. |
| `python 03_TOOLS\scripts\ai_quality\build_ai_quality_index.py --repo-root .` | `PASS` | Rebuilt AI quality index. |
| `python 03_TOOLS\scripts\indexing\build_known_problems.py --repo-root .` | `PASS` | Rebuilt known-problems summary, then restored explicit critical startup note. |
| `git status --short` | `NOT_AVAILABLE` | Command reported this folder is not currently a Git repository. |
| `Test-Path ...` for new rule files | `PASS` | Confirmed all three new strict visual gate files exist. |
| `rg -n "AUTOMATED_CROP_PASS_ONLY|VISUAL_NOT_VERIFIED|..." ...` | `PASS` | Confirmed startup and visual workflow docs reference the new statuses/rules. |
| `Get-ChildItem ... *.kicad_sch,*.kicad_pcb,*.kicad_pro` | `PASS` | Inspected active project KiCad file timestamps only; no KiCad design edits were performed by this task. |
| KiCad schematic/PCB edits | `NOT_RUN` | No KiCad design files were edited. |
| PCB update | `NOT_RUN` | PCB update remains blocked. |

## Safety

- No `.kicad_sch` file was edited.
- No `.kicad_pcb` file was edited.
- No PCB update, routing, zone creation, DRC, or manufacturing export was run.
