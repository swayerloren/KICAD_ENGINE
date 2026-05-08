# KiCad Knowledge Base Data Layer Status

Date: 2026-05-03

## Purpose

Created `10_KNOWLEDGE_BASE/` as an additional AI-readable data layer for practical schematic and PCB creation. This layer is intended to make KiCad Engine stronger for local-first KiCad users by giving agents reusable circuit patterns, design patterns, checklists, common mistake lists, manufacturing rules, and explicit stop/verify guidance.

## Created Structure

- `10_KNOWLEDGE_BASE/README.md`
- `10_KNOWLEDGE_BASE/circuits/`
- `10_KNOWLEDGE_BASE/design_patterns/`
- `10_KNOWLEDGE_BASE/checklists/`
- `10_KNOWLEDGE_BASE/common_mistakes/`
- `10_KNOWLEDGE_BASE/manufacturing/`
- `10_KNOWLEDGE_BASE/ai_agent_guidance/`

## Coverage

- Circuit blocks: USB-C power-only, USB-C USB2 device, ESP32-S3 minimum system, STM32 minimum system, PIC minimum system, CAN, CAN FD, LIN, RS485, 12 V to 5 V buck, 5 V to 3.3 V LDO, automotive 12 V input protection, ESD-protected USB, RF antenna/U.FL module, and status LED/button/reset.
- Design patterns: MCU minimum system, modular schematic blocks, power tree, connector interface, test point, mounting hole, grounding, and net naming.
- Checklists: pre-schematic, pre-PCB, pre-fab, connector, power, MCU, RF, and automotive review.
- Common mistakes: MCU, ESP32, STM32, USB-C, CAN, regulator, connector, and footprint failures.
- Manufacturing rules: JLCPCB, PCBWay, generic Gerber/drill, pick-and-place, BOM for assembly, and assembly notes.
- AI guidance: anti-hallucination rules, source citation rules, when to stop and ask a human, when to mark unverified, and when to require human review.

## Integration Updates

- Updated `AGENTS.md` to define `10_KNOWLEDGE_BASE/` ownership and require relevant knowledge-base reads before common circuit, layout, connector, power tree, or manufacturing package proposals.
- Updated `README.md`, `README_GPT.md`, `FOR CHAT GPT.MD`, `START_HERE_FOR_AI_AGENTS.md`, and `00_CODEX_START/REPO_MAP.md`.
- Updated `health_check.py` to include the new folder structure.
- Updated installer payload rules and builder allowlist so clean workspaces can include `10_KNOWLEDGE_BASE/`.

## Safety Notes

- No exact datasheet values were fabricated.
- Knowledge-base files are explicitly marked as planning aids, not datasheet proof.
- Connector orientation, footprints, package drawings, RF, USB-C, CAN/LIN/RS485, automotive, power, PNP, and manufacturing package decisions still require source evidence and human review.
- No KiCad project source files were edited.
- No tools were installed.

