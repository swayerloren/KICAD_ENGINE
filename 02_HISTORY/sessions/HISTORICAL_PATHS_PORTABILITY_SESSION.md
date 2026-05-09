# Historical Paths Portability Session

Date: `2026-05-09`
Task type: `DOCS_ONLY`
Project context: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`

## Summary

Audited tracked absolute-path findings and fixed the live portability surface without rewriting archival evidence.

## Work Performed

- scanned tracked files for maintainer-machine paths and absolute Windows KiCad paths
- classified findings into onboarding, active script/config, generated index, example-only, and historical evidence buckets
- strengthened startup and public path-portability guidance
- updated audit prompts to use live discovery first instead of one fixed Windows KiCad path
- removed a remaining fixed-path bias from two live Python helpers
- preserved historical records unchanged and documented why

## Key Decisions

- historical reports remain evidence and should not be rewritten blindly
- portable truth for new work must come from repo-relative docs plus live discovery on the current machine
- common `C:\Program Files\KiCad\*` paths may still appear as examples in docs and scripts, but they must not be treated as required setup truth

## Validation

- no `.kicad_sch`, `.kicad_pcb`, or `.kicad_pro` files changed
- onboarding docs now warn about historical local paths
- path portability rules now exist in both startup and public-doc form
- changed Python helpers were syntax-checked

## Remaining Risk

- large volumes of preserved evidence still include historical local paths
- some generated inventory under `29_FOOTPRINT_GAP_ANALYSIS/GENERATED_INDEXES/` remains machine-specific and should be cleaned separately
