# Prompt Pack System Status

Date: 2026-05-02

Workspace: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Summary

Created a reusable VS Code prompt pack for Codex, Claude, and similar AI coding agents working in KiCad Engine.

The prompt pack is local-first and repo-native. It is intended to help agents start safely, read the correct repo context, avoid unsafe KiCad edits, research components honestly, run verification, and keep generated fabrication-style outputs clearly marked as `NOT_FINAL`.

## Files Created

- `.prompts\README.md`
- `.prompts\codex\00_START_SESSION.md`
- `.prompts\codex\01_AUDIT_KICAD_INSTALL.md`
- `.prompts\codex\02_CREATE_NEW_PROJECT_WORKSPACE.md`
- `.prompts\codex\03_RESEARCH_COMPONENT.md`
- `.prompts\codex\04_ADD_COMPONENT_TO_DATABASE.md`
- `.prompts\codex\05_PLAN_SCHEMATIC.md`
- `.prompts\codex\06_REVIEW_SCHEMATIC.md`
- `.prompts\codex\07_REVIEW_PCB.md`
- `.prompts\codex\08_RUN_ERC_DRC.md`
- `.prompts\codex\09_EXPORT_NOT_FINAL_PACKAGE.md`
- `.prompts\codex\10_REVIEW_FAB_PACKAGE.md`
- `.prompts\codex\11_DEBUG_KICAD_ISSUE.md`
- `.prompts\codex\12_UPDATE_REPO_MEMORY_HISTORY.md`
- `.prompts\claude\00_START_SESSION.md`
- `.prompts\claude\01_AUDIT_KICAD_INSTALL.md`
- `.prompts\claude\02_CREATE_NEW_PROJECT_WORKSPACE.md`
- `.prompts\claude\03_RESEARCH_COMPONENT.md`
- `.prompts\claude\04_ADD_COMPONENT_TO_DATABASE.md`
- `.prompts\claude\05_PLAN_SCHEMATIC.md`
- `.prompts\claude\06_REVIEW_SCHEMATIC.md`
- `.prompts\claude\07_REVIEW_PCB.md`
- `.prompts\claude\08_RUN_ERC_DRC.md`
- `.prompts\claude\09_EXPORT_NOT_FINAL_PACKAGE.md`
- `.prompts\claude\10_REVIEW_FAB_PACKAGE.md`
- `.prompts\claude\11_DEBUG_KICAD_ISSUE.md`
- `.prompts\claude\12_UPDATE_REPO_MEMORY_HISTORY.md`
- `.prompts\shared\SAFETY_GATES.md`
- `.prompts\shared\COMPONENT_RESEARCH_STANDARD.md`
- `.prompts\shared\DATASHEET_SUMMARY_STANDARD.md`
- `.prompts\shared\KICAD_VERIFICATION_STANDARD.md`
- `.prompts\shared\GITHUB_RELEASE_STANDARD.md`

## Files Updated

- `README.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`

Backups for handoff files:

- `99_BACKUPS\pre_codex_edits\README_GPT_PROMPT_PACK_20260502_190006\README_GPT.md`
- `99_BACKUPS\pre_codex_edits\README_GPT_PROMPT_PACK_20260502_190006\FOR CHAT GPT.MD`

## Safety Coverage

Every task prompt is intended to require:

- Reading `AGENTS.md` and relevant startup/context files first.
- No KiCad project source edits unless active project, target files, backup, verification plan, and rollback plan are confirmed.
- History logging under `02_HISTORY`.
- Verification reports or explicit explanations when checks cannot run.
- No fabricated datasheet, package, electrical, lifecycle, ERC, DRC, BOM, footprint, or release claims.
- No approved footprint selection without exact part package and manufacturer drawing verification.
- `NOT_FINAL` labels for generated manufacturing-style outputs until the full verification gate passes.

## Scope Boundary

This was a documentation and prompt-system task only.

No KiCad project source files, symbol libraries, footprint libraries, project-local libraries, Gerbers, drill files, pick-and-place files, or other manufacturing outputs were intentionally edited.

## Verification

- Prompt pack markdown files present: 32.
- Codex task prompts present: 13.
- Claude task prompts present: 13.
- Shared standard files present: 5.
- All Codex and Claude task prompts include the required direct safety terms checked during validation: startup read via `AGENTS.md`, backup, history, verification, datasheet, footprint, and `NOT_FINAL`.
- No protected KiCad project/design/manufacturing files were modified after `2026-05-02 18:55`.
- A pre-existing/recent schematic timestamp was observed at `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`, last written `2026-05-02 15:20:52`; it predates this prompt-pack edit window and was not changed here.

## Follow-Up

- Consider adding `.vscode` snippets or task links that expose these prompts inside VS Code.
- Consider adding release documentation that names the prompt pack as a supported interface for Codex and Claude.
- Consider adding a lint script that checks prompt files for required safety phrases.
