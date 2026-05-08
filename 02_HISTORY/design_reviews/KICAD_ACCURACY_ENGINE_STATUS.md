# KiCad Accuracy Engine Status

Date: 2026-05-03

## Scope

Created `09_ACCURACY_ENGINE` as an AI-readable accuracy and anti-hallucination rule system for KiCad schematic creation, PCB creation, component adds, symbol selection, pinout verification, footprint verification, and release-package review.

No KiCad project source files were intentionally edited.

## Created Structure

- `09_ACCURACY_ENGINE/README.md`
- `09_ACCURACY_ENGINE/schematic_rules/`
- `09_ACCURACY_ENGINE/pcb_rules/`
- `09_ACCURACY_ENGINE/verification_rules/`
- `09_ACCURACY_ENGINE/workflows/`

Created 37 markdown files total.

## Core Rules Added

- Every component must have a source or be marked source-missing.
- Every symbol must map to verified pinout evidence or remain unverified.
- Every footprint must map to an exact package drawing or remain `UNVERIFIED_FOOTPRINT`.
- Every connector orientation requires human review unless exact drawing, mating, footprint, and mechanical evidence are verified.
- Every polarity-sensitive part must be flagged.
- Every RF, USB, and CAN part must trigger layout-specific review.
- Manufacturing-style outputs remain `NOT_FINAL` until final human review.

## Updated References

- `AGENTS.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `00_CODEX_START/KICAD_AGENT_OPERATING_MANUAL.md`
- `00_CODEX_START/REPO_MAP.md`
- `health_check.py`
- `installer/payload/build_payload.py`
- `installer/payload/PAYLOAD_CONTENT_RULES.md`

## Validation

Commands run:

```powershell
python health_check.py --repo-root . --no-write
python installer\payload\build_payload.py --source-root . --payload-root installer\payload --max-file-size-mb 5
python health_check.py --repo-root installer\payload\repo-template --no-write
rg -n "api[_-]?key|access[_-]?token|secret\s*[:=]|password\s*[:=]|C:\\Users\\LJ|C:/Users/LJ|COMMAND_LINK|ESP32_CSI_WIFI_NODE" 09_ACCURACY_ENGINE installer\payload\repo-template\09_ACCURACY_ENGINE
```

Results:

- Root health check: `PASS=102 WARN=0 FAIL=0`.
- Payload build: completed successfully.
- Payload health check: `PASS=102 WARN=0 FAIL=0`.
- Accuracy-engine private-marker scan: no matches.
- Payload includes `09_ACCURACY_ENGINE` with 37 files.
- Clean payload handoff files and `00_CODEX_START/REPO_MAP.md` reference `09_ACCURACY_ENGINE`.

## Safety

- Did not edit `.kicad_sch`, `.kicad_pcb`, `.kicad_pro`, symbols, footprints, or manufacturing output source files.
- Did not install tools.
- Did not download datasheets.
- Did not write into installed KiCad folders.

## Next Work

- Wire `09_ACCURACY_ENGINE` into future prompt-pack task prompts.
- Add scriptable checklists that can verify component records, symbol evidence, and footprint evidence before schematic/PCB edits.
- Add example accuracy reports for a copied sample project only after user approval.
