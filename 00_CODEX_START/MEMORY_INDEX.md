# Memory Index

Memory files store durable preferences, constraints, and design decisions. They are not command logs.

## Template Notation

Paths containing `<project-id>` are templates for real project names. Do not treat them as literal folders. For the current active project, use the path recorded in `CURRENT_PROJECT.md`.

## Current Active Project Memory

- Active project path: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE`
- Current project memory folder: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory`
- Current project remains blocked before PCB update; memory entries must not imply PCB, footprint, or fabrication readiness.

## Required Memory Files
- `01_MEMORY\GLOBAL_MEMORY.md`
- `01_MEMORY\DESIGN_RULES_MEMORY.md`
- `01_MEMORY\COMPONENT_PREFERENCES.md`
- `01_MEMORY\FAB_HOUSE_PREFERENCES.md`
- `01_MEMORY\AGENT_LESSONS_LEARNED.md`
- `01_MEMORY\AGENT_MISTAKES_TO_AVOID.md`
- `01_MEMORY\AI_RELIABILITY_MEMORY.md`
- `01_MEMORY\GLOBAL_HALLUCINATION_RISKS.md`
- `01_MEMORY\GLOBAL_UNVERIFIED_CLAIMS.md`
- `01_MEMORY\GLOBAL_QUALITY_GATE_RULES.md`
- `01_MEMORY\USER_CORRECTIONS_MEMORY.md`
- `01_MEMORY\VERIFIED_WORKFLOWS.md`
- `01_MEMORY\FAILED_WORKFLOWS.md`
- `01_MEMORY\MEMORY_UPDATE_RULES.md`
- `01_MEMORY\projects\<project-id>\PROJECT_MEMORY.md`
- `04_KICAD_PROJECTS\active\<project-id>\memory\PROJECT_MEMORY.md`
- `04_KICAD_PROJECTS\active\<project-id>\memory\COMPONENT_DECISIONS.md`
- `04_KICAD_PROJECTS\active\<project-id>\memory\FOOTPRINT_DECISIONS.md`
- `04_KICAD_PROJECTS\active\<project-id>\memory\DATASHEET_DECISIONS.md`
- `04_KICAD_PROJECTS\active\<project-id>\memory\DESIGN_RULES.md`
- `04_KICAD_PROJECTS\active\<project-id>\memory\USER_CORRECTIONS.md`
- `04_KICAD_PROJECTS\active\<project-id>\memory\AGENT_MISTAKES_TO_AVOID.md`
- `04_KICAD_PROJECTS\active\<project-id>\memory\OPEN_DESIGN_RISKS.md`
- `04_KICAD_PROJECTS\active\<project-id>\memory\MEMORY_UPDATE_RULES.md`
- `04_KICAD_PROJECTS\active\<project-id>\memory\AI_RELIABILITY_MEMORY.md`
- `04_KICAD_PROJECTS\active\<project-id>\memory\PROJECT_HALLUCINATION_RISKS.md`
- `04_KICAD_PROJECTS\active\<project-id>\memory\PROJECT_UNVERIFIED_CLAIMS.md`
- `04_KICAD_PROJECTS\active\<project-id>\memory\PROJECT_QUALITY_GATE_RULES.md`

## Use Rules
- Read relevant memory before touching KiCad files.
- Store durable decisions in memory.
- Do not store command transcripts in memory.
- Do not store passwords, API keys, license keys, private tokens, or credentials in memory.
- Mark memory entries `UNVERIFIED` unless human-confirmed or verified by repeatable workflow evidence.
- Create history evidence before promoting a fact into memory.
- Keep global memory reusable across projects.
- Keep project memory specific to one active project.
- Keep AI reliability, hallucination-risk, unverified-claim, and quality-gate memory concise and evidence-linked.

## Scope
- `GLOBAL_MEMORY.md`: workspace-wide durable context.
- `DESIGN_RULES_MEMORY.md`: electrical, PCB, fabrication, and review rules that apply across projects.
- `COMPONENT_PREFERENCES.md`: preferred parts, alternates, sourcing constraints, and avoided components.
- `FAB_HOUSE_PREFERENCES.md`: manufacturer capabilities, process preferences, and release requirements.
- `AGENT_LESSONS_LEARNED.md`: reusable lessons for future agents.
- `AGENT_MISTAKES_TO_AVOID.md`: recurring AI mistakes and avoidance rules.
- `AI_RELIABILITY_MEMORY.md`: reusable AI quality and reliability lessons.
- `GLOBAL_HALLUCINATION_RISKS.md`: repo-wide hallucination risk patterns.
- `GLOBAL_UNVERIFIED_CLAIMS.md`: claim categories that must remain unverified until evidence exists.
- `GLOBAL_QUALITY_GATE_RULES.md`: mandatory AI quality-gate blockers.
- `USER_CORRECTIONS_MEMORY.md`: cross-project user corrections that change global behavior.
- `VERIFIED_WORKFLOWS.md`: workflows with evidence.
- `FAILED_WORKFLOWS.md`: workflows that failed and should not be repeated unchanged.
- `MEMORY_UPDATE_RULES.md`: routing and promotion rules.
- `projects\<project-id>\PROJECT_MEMORY.md`: durable project-specific decisions and constraints.
- `active\<project-id>\memory\`: current local project memory, including components, footprints, datasheets, corrections, risks, and project rules.
- `active\<project-id>\memory\AI_RELIABILITY_MEMORY.md`: project-specific AI reliability rules.
- `active\<project-id>\memory\PROJECT_HALLUCINATION_RISKS.md`: project-specific hallucination risks.
- `active\<project-id>\memory\PROJECT_UNVERIFIED_CLAIMS.md`: project-specific unverified claim categories.
- `active\<project-id>\memory\PROJECT_QUALITY_GATE_RULES.md`: project-specific quality-gate rules.

## Generated Indexes
- `01_MEMORY\MASTER_MEMORY_INDEX.md`
- `00_CODEX_START\MEMORY_INDEX.generated.md`
- `00_CODEX_START\MEMORY_INDEX.generated.json`

## Index Builder

Use `python 03_TOOLS/scripts/indexing/build_memory_index.py --repo-root .` to rebuild the master memory index and startup generated memory indexes.

The builder is non-destructive. It scans `01_MEMORY/` and active project `memory/` folders, then writes only:

- `01_MEMORY/MASTER_MEMORY_INDEX.md`
- `00_CODEX_START/MEMORY_INDEX.generated.md`
- `00_CODEX_START/MEMORY_INDEX.generated.json`

