# ESP32 Dev Board Layout Intelligence Claim Evidence Matrix

Record kind: `claim_evidence_matrix`
Created: `2026-05-07T17:27:33`
Scope: `global`
Project: `N/A`
Severity: `LOW`
Confidence: `HIGH`
Claim status: `VERIFIED_BY_FILE`
Risk label: `LOW_RISK`
Gate result: `PASS`
Human review required: `NO`

## Matrix

| Claim | Evidence | Claim Status | Confidence | Risk | Human Review Required | Issue |
| --- | --- | --- | --- | --- | --- | --- |
| KiCad Engine now has reusable placement-intelligence guidance for ESP32-style boards, STM32-style dev boards, connector edge placement, RF module keepouts, and common placement mistakes. | 10_KNOWLEDGE_BASE/design_patterns/ESP32_DEV_BOARD_LAYOUT_PATTERN.md, STM32_DEV_BOARD_LAYOUT_PATTERN.md, CONNECTOR_EDGE_PLACEMENT_PATTERN.md, RF_MODULE_ANTENNA_KEEP_OUT_PATTERN.md; 10_KNOWLEDGE_BASE/common_mistakes/ESP32_LAYOUT_COMMON_MISTAKES.md, USB_C_CONNECTOR_LAYOUT_COMMON_MISTAKES.md, BARREL_JACK_LAYOUT_COMMON_MISTAKES.md; 34_PCB_LAYOUT_SANDBOX/ESP32_STYLE_BOARD_PLACEMENT_RULES.md and DEV_BOARD_SHAPE_REASONING_RULES.md; README_GPT.md; FOR CHAT GPT.MD; 01_MEMORY/DESIGN_RULES_MEMORY.md. | `VERIFIED_BY_FILE` | `HIGH` | `LOW_RISK` | `NO` | The guidance is documented but not yet exercised on a real project-local sandbox study. |

## Details

The patch created new design-pattern and common-mistake documents, added new sandbox rule files, and updated global memory and handoff docs so future agents can find the new placement guidance during planning.
