# KiCad Engine Knowledge Base

Status: first-pass AI-readable engineering data layer.

This folder stores reusable circuit knowledge, design patterns, review checklists, common mistakes, manufacturing rules, and AI-agent decision rules.

It complements:

- `06_DATASHEETS/`: source links, metadata, and document summaries.
- `08_COMPONENT_DATABASE/`: part-level records and KiCad symbol/footprint candidates.
- `09_ACCURACY_ENGINE/`: strict accuracy, evidence, and verification gates.

## Purpose

`10_KNOWLEDGE_BASE/` helps Codex, Claude, and similar VS Code-based agents avoid starting from blank memory when planning schematics and PCBs.

Use it to:

- Choose known circuit blocks.
- Identify required external parts.
- Recognize high-risk interfaces.
- Ask better questions before editing KiCad files.
- Build schematic and PCB review plans.
- Avoid common engineering mistakes.

## Source Policy

These files are not datasheets.

Agents must not treat a pattern here as proof that a design is correct. Before creating or approving a schematic, PCB, symbol, footprint, BOM, or manufacturing package, verify against:

- The exact component datasheet.
- Vendor reference design or application note.
- Exact connector mechanical drawing.
- Exact package drawing.
- KiCad ERC/DRC output.
- Human review for connector orientation, polarity, RF, USB, CAN, automotive, and fabrication outputs.

Use `Unknown - requires source verification` when an exact value is not verified.

## Folder Map

- `circuits/`: reusable schematic/PCB circuit blocks.
- `design_patterns/`: generic design organization patterns.
- `checklists/`: review gates before schematic, PCB, and fabrication work.
- `common_mistakes/`: recurring errors agents must watch for.
- `manufacturing/`: fab and assembly package rules.
- `ai_agent_guidance/`: anti-hallucination and human-review decision rules.

## Agent Workflow

Before proposing a circuit:

1. Read the matching circuit file in `10_KNOWLEDGE_BASE/circuits/`.
2. Read the matching rules in `09_ACCURACY_ENGINE/`.
3. Check `08_COMPONENT_DATABASE/` for candidate parts.
4. Check `06_DATASHEETS/` for source status.
5. Mark every unverified value explicitly.
6. Do not edit KiCad project files until the active project, backup, rollback, and verification plan are confirmed.


## PURPOSE

Store reusable circuit patterns, design patterns, checklists, common mistakes, and practical review guidance.

## WHAT_BELONGS_HERE

Circuit guides, design patterns, review checklists, manufacturing rules, and AI stop/verify guidance.

## WHAT_DOES_NOT_BELONG_HERE

Datasheet replacements, active KiCad projects, exact specs without sources, or generated outputs.

## AI_AGENT_RULES

- Read this folder's README.md and INDEX.md before adding or relying on content here.
- Mark unverified engineering claims explicitly.
- Keep source links, verification status, and human-review requirements visible.
- Route generated logs and reports to 2_HISTORY/, 5_OUTPUTS/, or project history/ unless this folder explicitly calls for generated indexes.

## SAFE_EDIT_RULES

- Preserve existing user work.
- Do not delete or overwrite files without explicit approval.
- Do not edit KiCad design files from this folder.
- Do not store secrets or credentials.

## PUBLIC_RELEASE_NOTES

- Review this folder for secrets, personal paths, copyrighted documents, unsupported claims, and large generated files before public release.
- Folder existence is not a completeness or production-readiness claim.

## Prompt 4 Core Knowledge Update

The reusable engineering knowledge base includes:

- Circuit patterns under `circuits/`.
- Common mistake lists under `common_mistakes/`.
- Design patterns under `design_patterns/`.
- Review checklists under `checklists/`.
- Manufacturing rules under `manufacturing/`.
- AI-agent source and anti-hallucination guidance under `ai_agent_guidance/`.

All circuit patterns are `AI_GUIDANCE_ONLY`. They are not datasheet replacements and must not be used to approve schematics, footprints, BOMs, or fab outputs without the `09_ACCURACY_ENGINE` gate.

## Required Agent Use

Before proposing a circuit pattern, an agent must state:

- which knowledge-base file was used,
- which source documents still need verification,
- which component records apply,
- which schematic and PCB rules apply,
- which human-review gates remain.
