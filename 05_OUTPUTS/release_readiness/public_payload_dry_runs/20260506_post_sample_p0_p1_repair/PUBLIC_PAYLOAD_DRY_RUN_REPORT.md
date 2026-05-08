# Public Payload Dry-Run Report

Generated UTC: `2026-05-06T19:10:25.306199+00:00`

Builder: `17_RELEASE_BUILD/build_public_payload.py`

Builder version: `0.1.0`

Mode: `dry_run`

Final classification: `DRY_RUN_PASS_WITH_WARNINGS`

Public release status: `BLOCKED_PENDING_HUMAN_RELEASE_REVIEW`

Sample payload decision: `LINK_ONLY_PLUS_DOCS`

## Summary

| Metric | Value |
| --- | ---: |
| Included files | 2329 |
| Included bytes | 12495904 |
| Excluded files | 946 |
| Warning records | 2 |

## Warnings

- `SAMPLE_SOURCE_EXCLUDED`: Controlled sample source remains excluded until human public-bundle status is exactly PUBLIC_BUNDLE_ALLOWED. Count: 5
- `PRUNED_EXCLUDED_ROOTS`: Large or unsafe roots were pruned instead of scanned file-by-file. Count: 47

## Included Examples

- `.prompts/claude/00_START_SESSION.md` (2501 bytes)
- `.prompts/claude/01_AUDIT_KICAD_INSTALL.md` (2340 bytes)
- `.prompts/claude/02_CREATE_NEW_PROJECT_WORKSPACE.md` (1983 bytes)
- `.prompts/claude/03_RESEARCH_COMPONENT.md` (2255 bytes)
- `.prompts/claude/04_ADD_COMPONENT_TO_DATABASE.md` (2140 bytes)
- `.prompts/claude/05_PLAN_SCHEMATIC.md` (2160 bytes)
- `.prompts/claude/06_REVIEW_SCHEMATIC.md` (1966 bytes)
- `.prompts/claude/07_REVIEW_PCB.md` (1999 bytes)
- `.prompts/claude/08_RUN_ERC_DRC.md` (1809 bytes)
- `.prompts/claude/09_EXPORT_NOT_FINAL_PACKAGE.md` (1795 bytes)
- `.prompts/claude/10_REVIEW_FAB_PACKAGE.md` (1956 bytes)
- `.prompts/claude/11_DEBUG_KICAD_ISSUE.md` (1924 bytes)
- `.prompts/claude/12_UPDATE_REPO_MEMORY_HISTORY.md` (1664 bytes)
- `.prompts/codex/00_START_SESSION.md` (1729 bytes)
- `.prompts/codex/01_AUDIT_KICAD_INSTALL.md` (1927 bytes)
- `.prompts/codex/02_CREATE_NEW_PROJECT_WORKSPACE.md` (1861 bytes)
- `.prompts/codex/03_RESEARCH_COMPONENT.md` (1956 bytes)
- `.prompts/codex/04_ADD_COMPONENT_TO_DATABASE.md` (1906 bytes)
- `.prompts/codex/05_PLAN_SCHEMATIC.md` (1885 bytes)
- `.prompts/codex/06_REVIEW_SCHEMATIC.md` (1943 bytes)
- `.prompts/codex/07_REVIEW_PCB.md` (1928 bytes)
- `.prompts/codex/08_RUN_ERC_DRC.md` (1654 bytes)
- `.prompts/codex/09_EXPORT_NOT_FINAL_PACKAGE.md` (1672 bytes)
- `.prompts/codex/10_REVIEW_FAB_PACKAGE.md` (1806 bytes)
- `.prompts/codex/11_DEBUG_KICAD_ISSUE.md` (1843 bytes)
- `.prompts/codex/12_UPDATE_REPO_MEMORY_HISTORY.md` (1779 bytes)
- `.prompts/INDEX.md` (837 bytes)
- `.prompts/kicad_pipeline/01_schematic_annotation_and_completeness.md` (1362 bytes)
- `.prompts/kicad_pipeline/02_schematic_visual_closeup_audit.md` (1081 bytes)
- `.prompts/kicad_pipeline/03_schematic_visual_repair.md` (1313 bytes)
- `.prompts/kicad_pipeline/04_schematic_electrical_audit.md` (1137 bytes)
- `.prompts/kicad_pipeline/05_footprint_package_audit.md` (1192 bytes)
- `.prompts/kicad_pipeline/06_schematic_to_pcb_gate.md` (1145 bytes)
- `.prompts/kicad_pipeline/07_update_pcb_from_schematic.md` (938 bytes)
- `.prompts/kicad_pipeline/08_pcb_mechanical_setup.md` (1143 bytes)
- `.prompts/kicad_pipeline/09_pcb_placement_pass_1.md` (1108 bytes)
- `.prompts/kicad_pipeline/10_pcb_placement_pass_2_orientation.md` (1097 bytes)
- `.prompts/kicad_pipeline/11_holes_pads_vias_strategy.md` (1063 bytes)
- `.prompts/kicad_pipeline/12_copper_zones_setup.md` (946 bytes)
- `.prompts/kicad_pipeline/13_routing_plan_only.md` (987 bytes)

## Excluded Examples

- `.codex/config.example.toml` - not in public payload allowlist
- `.codex/config.toml` - not in public payload allowlist
- `.codex/INDEX.md` - not in public payload allowlist
- `.codex/prompts/CREATE_REAL_KICAD_PROJECT_FROM_REQUIREMENTS.md` - not in public payload allowlist
- `.codex/prompts/INSTALL_KICAD_TOOLS.md` - not in public payload allowlist
- `.codex/prompts/NEW_KICAD_PROJECT.md` - not in public payload allowlist
- `.codex/prompts/REVIEW_EXISTING_PROJECT.md` - not in public payload allowlist
- `.codex/prompts/START_CODEX_KICAD_ENGINE.md` - not in public payload allowlist
- `.codex/prompts/VERIFY_BEFORE_FAB.md` - not in public payload allowlist
- `.codex/README.md` - not in public payload allowlist
- `.github/INDEX.md` - not in public payload allowlist
- `.github/README.md` - not in public payload allowlist
- `.github/RELEASE_WORKFLOW_README.md` - not in public payload allowlist
- `.github/workflows/build-all-installers.yml` - not in public payload allowlist
- `.github/workflows/build-installer-linux.yml` - not in public payload allowlist
- `.github/workflows/build-installer-macos.yml` - not in public payload allowlist
- `.github/workflows/build-installer-windows.yml` - not in public payload allowlist
- `.github/workflows/build-linux-installer.yml` - not in public payload allowlist
- `.github/workflows/build-macos-installer.yml` - not in public payload allowlist
- `.github/workflows/release-draft.yml` - not in public payload allowlist
- `.gitignore` - not in public payload allowlist
- `01_MEMORY/AGENT_LESSONS_LEARNED.md` - not in public payload allowlist
- `01_MEMORY/AGENT_MISTAKES_TO_AVOID.md` - not in public payload allowlist
- `01_MEMORY/AI_RELIABILITY_MEMORY.md` - not in public payload allowlist
- `01_MEMORY/CODING_AND_SCRIPTING_RULES.md` - not in public payload allowlist
- `01_MEMORY/COMPONENT_PREFERENCES.md` - not in public payload allowlist
- `01_MEMORY/DESIGN_RULES_MEMORY.md` - not in public payload allowlist
- `01_MEMORY/EXAMPLE_ONLY_UNVERIFIED_CONNECTOR_FOOTPRINT_WARNING.md` - not in public payload allowlist
- `01_MEMORY/FAB_HOUSE_PREFERENCES.md` - not in public payload allowlist
- `01_MEMORY/FAILED_WORKFLOWS.md` - not in public payload allowlist
- `01_MEMORY/GLOBAL_HALLUCINATION_RISKS.md` - not in public payload allowlist
- `01_MEMORY/GLOBAL_MEMORY.md` - not in public payload allowlist
- `01_MEMORY/GLOBAL_QUALITY_GATE_RULES.md` - not in public payload allowlist
- `01_MEMORY/GLOBAL_UNVERIFIED_CLAIMS.md` - not in public payload allowlist
- `01_MEMORY/INDEX.md` - not in public payload allowlist
- `01_MEMORY/MASTER_MEMORY_INDEX.md` - not in public payload allowlist
- `01_MEMORY/MEMORY_UPDATE_RULES.md` - not in public payload allowlist
- `01_MEMORY/projects/CLEAN_KICAD_PASSING_SAMPLE/PROJECT_MEMORY.md` - not in public payload allowlist
- `01_MEMORY/projects/COMMAND_LINK_VERIFIED_REFERENCE/PROJECT_MEMORY.md` - not in public payload allowlist
- `01_MEMORY/projects/ESP32_CSI_WIFI_NODE/PROJECT_MEMORY.md` - not in public payload allowlist
- `01_MEMORY/projects/SAMPLE_KICAD_TEST_PROJECT/PROJECT_MEMORY.md` - not in public payload allowlist
- `01_MEMORY/README.md` - not in public payload allowlist
- `01_MEMORY/USER_CORRECTIONS_MEMORY.md` - not in public payload allowlist
- `01_MEMORY/VERIFIED_WORKFLOWS.md` - not in public payload allowlist
- `03_TOOLS/common/README.md` - not in public payload allowlist
- `03_TOOLS/INDEX.md` - not in public payload allowlist
- `03_TOOLS/kicad/run_schematic_visual_check.ps1` - not in public payload allowlist
- `03_TOOLS/kicad/VISUAL_BLOCK_CONFIG_STANDARD.md` - not in public payload allowlist
- `03_TOOLS/kicad/VISUAL_VERIFICATION_WORKFLOW.md` - not in public payload allowlist
- `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/footprint_index.json` - file exceeds size limit (14765426 bytes > 5242880 bytes)
- `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/symbol_index.json` - file exceeds size limit (11617024 bytes > 5242880 bytes)
- `03_TOOLS/linux/docs/LINUX_AUTOMATION_README.md` - not in public payload allowlist
- `03_TOOLS/linux/docs/LINUX_KICAD_HEADLESS_PLAN.md` - not in public payload allowlist
- `03_TOOLS/linux/docs/LINUX_TOOL_INSTALL_COMMANDS_DRAFT.md` - not in public payload allowlist
- `03_TOOLS/linux/docs/WSL_SETUP_NOTES.md` - not in public payload allowlist
- `03_TOOLS/linux/README.md` - not in public payload allowlist
- `03_TOOLS/linux/scripts/check_linux_kicad_env.sh` - not in public payload allowlist
- `03_TOOLS/linux/scripts/wmctrl/list_windows.sh` - not in public payload allowlist
- `03_TOOLS/linux/scripts/xdotool/list_windows.sh` - not in public payload allowlist
- `03_TOOLS/linux/scripts/xvfb/run_kicad_headless_check.sh` - not in public payload allowlist

## Release Judgment

This dry-run does not create a public release artifact and does not approve
public distribution. The repo remains blocked pending human release review,
sample public-bundle review, and the remaining ATtiny85 engineering gate
blockers.
