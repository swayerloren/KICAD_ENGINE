# Reference Sample System Commands

Date: `2026-05-10`

## Commands Run

- Read startup and routing docs plus the current sample-intake/reference docs.
- Inspected existing `32_OPEN_KICAD_SAMPLE_INTAKE/` scripts and templates.
- Syntax check:
  `Get-ChildItem 03_TOOLS\scripts\sample_intake -Filter *.py -File | ForEach-Object { python -m py_compile $_.FullName }`
- Candidate registration dry-run:
  `python 03_TOOLS\scripts\sample_intake\register_sample_candidate.py --project-name "Dry Run Reference Sample" --source-url "https://example.com/reference-sample" --source-host "example.com" --source-owner "example-owner" --license-name "UNKNOWN" --license-status "NEEDS_HUMAN_LICENSE_REVIEW" --notes "Dry-run validation for the reference sample learning system."`
- Reference-style index dry-run:
  `python 03_TOOLS\scripts\sample_intake\build_reference_style_index.py`
- Task-contract validation and report generation:
  `python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --contract 02_HISTORY\sessions\2026-05-10_reference_sample_system_task_contract.json`
  `python 03_TOOLS\scripts\execution_contract\write_task_contract_report.py --contract 02_HISTORY\sessions\2026-05-10_reference_sample_system_task_contract.json --output 02_HISTORY\sessions\2026-05-10_reference_sample_system_task_contract_report.md`
- Index rebuild:
  `python 03_TOOLS\scripts\indexing\build_repo_index.py --repo-root .`
  `python 03_TOOLS\scripts\indexing\build_memory_index.py --repo-root .`
  `python 03_TOOLS\scripts\indexing\build_history_index.py --repo-root .`
  `python 03_TOOLS\scripts\indexing\build_known_problems.py --repo-root .`
  `python 03_TOOLS\scripts\ai_quality\build_ai_quality_index.py --repo-root .`
- KiCad file diff checks:
  `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'`
  `git diff --cached --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'`
  `git status --short --untracked-files=no -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'`
