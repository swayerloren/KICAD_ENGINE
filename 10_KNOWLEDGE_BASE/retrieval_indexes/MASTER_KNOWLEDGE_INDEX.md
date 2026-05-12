# Master Knowledge Index

Status: `CANONICAL_POST_MIGRATION_KNOWLEDGE_INDEX`

Generated: `2026-05-12`

## Canonical Startup And Retrieval Entry Points

- `START_HERE_FOR_AI_AGENTS.md`
- `00_CODEX_START/TASK_ROUTER.md`
- `00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md`
- `00_CODEX_START/TASK_TYPE_TO_ALLOWED_ACTIONS.md`
- `00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md`
- `00_CODEX_START/TASK_TYPE_TO_OUTPUTS.md`
- `00_CODEX_START/TASK_TYPE_TO_KNOWLEDGE_MAP.md`
- `00_CODEX_START/TASK_TYPE_TO_TOOL_MAP.md`
- `00_CODEX_START/TASK_TYPE_TO_RULE_MAP.md`
- `10_KNOWLEDGE_BASE/retrieval_indexes/TASK_TO_KNOWLEDGE_MAP.md`
- `10_KNOWLEDGE_BASE/retrieval_indexes/TASK_TO_TOOL_MAP.md`
- `10_KNOWLEDGE_BASE/retrieval_indexes/TASK_TO_RULE_MAP.md`
- `10_KNOWLEDGE_BASE/retrieval_indexes/KNOWLEDGE_SOURCE_INDEX.md`
- `10_KNOWLEDGE_BASE/source_registry/SOURCE_REGISTRY.csv`
- `10_KNOWLEDGE_BASE/source_registry/SOURCE_REGISTRY.json`

## Canonical Knowledge Areas

- `10_KNOWLEDGE_BASE/kicad_core/`
- `10_KNOWLEDGE_BASE/kicad_python_api/`
- `10_KNOWLEDGE_BASE/kicad_file_formats/`
- `10_KNOWLEDGE_BASE/kicad_libraries/`
- `10_KNOWLEDGE_BASE/calculators/`
- `10_KNOWLEDGE_BASE/dfm_assembly/`
- `10_KNOWLEDGE_BASE/compliance_emc_safety/`
- `10_KNOWLEDGE_BASE/training/`
- `10_KNOWLEDGE_BASE/peer_review/`
- `10_KNOWLEDGE_BASE/case_studies/`
- `10_KNOWLEDGE_BASE/pcb_layout/`
- `10_KNOWLEDGE_BASE/usb_c/`
- `10_KNOWLEDGE_BASE/power_integrity/`
- `10_KNOWLEDGE_BASE/rf_wifi/`
- `10_KNOWLEDGE_BASE/thermal_mechanical/`

## Canonical Tool And Validation Surfaces

- `03_TOOLS/calculators/`
- `03_TOOLS/open_source_integrations/`
- `03_TOOLS/scripts/kicad_api/`
- `03_TOOLS/scripts/schematic_quality/`
- `03_TOOLS/scripts/schematic_layout/`
- `03_TOOLS/scripts/footprint_package/`
- `03_TOOLS/scripts/mechanical_orientation/`
- `03_TOOLS/scripts/pcb_prelayout/`
- `03_TOOLS/scripts/pcb_geometry/`
- `03_TOOLS/scripts/pcb_quality/`
- `09_ACCURACY_ENGINE/workflows/EDA_AUTOMATION_VERIFICATION_WORKFLOW.md`
- `09_ACCURACY_ENGINE/verification_rules/CALCULATOR_RESULT_EVIDENCE_RULES.md`
- `09_ACCURACY_ENGINE/verification_rules/AUTOMATION_TOOL_RESULT_VALIDATION_RULES.md`

## Use Pattern

1. Start from `START_HERE_FOR_AI_AGENTS.md` and the `00_CODEX_START` task maps.
2. Use canonical `10_KNOWLEDGE_BASE` summaries, rule maps, and tool maps before
   consulting historical provenance.
3. Treat calculators and automation helpers as aids, not proof.
4. Validate engineering claims with KiCad ERC/DRC, parity, geometry, source
   evidence, or another independent check.
5. Treat release-readiness migration reports and repo history as provenance and
   audit evidence, not as the live routing path.

## Legacy Migration Note

- The old `knowledge_scrape/` source folder has now been fully drained and
  removed from the live repo tree.
- Remaining `knowledge_scrape` mentions belong only to migration history,
  quarantine records, release-readiness audits, or backup evidence.
