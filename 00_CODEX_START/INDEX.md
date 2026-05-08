# 00_CODEX_START Index

## PURPOSE
AI-readable routing index for startup and control-plane documents. This file tells agents which control document to open for common task types before they inspect, edit, or generate anything.

## WHAT_BELONGS_HERE
- `START_HERE.md`
- `SESSION_START_CHECKLIST.md`
- `SESSION_CLOSEOUT_CHECKLIST.md`
- `STRUCTURE_STANDARD.md`
- `FOLDER_ROUTING_RULES.md`
- Generated startup indexes.

## WHAT_DOES_NOT_BELONG_HERE
- Raw command output.
- Project-specific design decisions.
- KiCad source files.

## AI_AGENT_RULES
- Use this folder before tool selection, structure edits, or KiCad work.
- Treat generated indexes as startup context, not engineering proof.
- If a task involves components, datasheets, footprints, suppliers, Playwright research, AI quality, schematic gates, PCB gates, or fab review, open the matching subsystem rules before planning edits.
- If an index is stale, use it as orientation only and verify the target file/folder directly.

## ROUTING BY TASK

| Task Type | Read Next |
| --- | --- |
| KiCad project edits | `START_HERE.md`, `CURRENT_PROJECT.md`, project memory/history, and relevant `09_ACCURACY_ENGINE` workflow. |
| Datasheet/source research | `06_DATASHEETS/00_INDEX/DATASHEET_LIBRARY_README.md` and source policy files. |
| Component record work | `08_COMPONENT_DATABASE/00_INDEX/COMPONENT_DATABASE_README.md`, `PART_SCHEMA.md`, and `DO_NOT_GUESS_RULES.md`. |
| Symbol/footprint decisions | `11_LIBRARY_FACTORY/README.md` and `08_COMPONENT_DATABASE/00_INDEX/KICAD_SYMBOL_FOOTPRINT_LINKING_RULES.md`. |
| Supplier metadata | `28_SUPPLIER_INGESTION/README.md` and `API_KEY_HANDLING.md`. |
| Footprint gaps | `29_FOOTPRINT_GAP_ANALYSIS/README.md` and high-risk gap reports. |
| Playwright research | `31_PLAYWRIGHT_RESEARCH_PIPELINE/PLAYWRIGHT_USAGE_RULES.md` and source profile. |
| Closeout | `SESSION_CLOSEOUT_CHECKLIST.md` and `26_AGENT_QUALITY` rules. |

## SAFE_EDIT_RULES
- Update `README_GPT.md` and `FOR CHAT GPT.MD` when startup or workflow rules change.
- Rebuild indexes after updates.

## PUBLIC_RELEASE_NOTES
- Public releases should make these rules clear enough for Codex, Claude, and similar agents.
