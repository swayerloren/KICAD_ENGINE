# GitHub Dev Infrastructure Setup Commands

## Commands Run

```powershell
gh --version
gh auth status
git status -sb
git branch --show-current
Get-ChildItem -Recurse -File .github,.devcontainer,docs -ErrorAction SilentlyContinue | Select-Object -ExpandProperty FullName
Get-Content -Raw .github\PULL_REQUEST_TEMPLATE.md
Get-Content -Raw .github\ISSUE_TEMPLATE\bug_report.md
Get-Content -Raw .github\ISSUE_TEMPLATE\pcb_issue.md
Get-Content -Raw .github\ISSUE_TEMPLATE\feature_request.md
Get-Content -Raw .github\README.md
Get-Content -Raw docs\README.md
Get-Content -Raw docs\INDEX.md
python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --help
python 14_LAYOUT_AUTOMATION\scripts\routing_geometry_quality.py --help
python 14_LAYOUT_AUTOMATION\scripts\score_placement_readiness.py --help
Get-ChildItem 14_LAYOUT_AUTOMATION\test_fixtures\routing_geometry -File | Select-Object -ExpandProperty Name
Get-ChildItem 03_TOOLS\scripts\execution_contract\examples -File | Select-Object -ExpandProperty Name
python -  # tracked first-party Python compile check
python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --contract 03_TOOLS\scripts\execution_contract\examples\docs_only.json
python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --contract 03_TOOLS\scripts\execution_contract\examples\audit_only.json
python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --contract 03_TOOLS\scripts\execution_contract\examples\pcb_edit_required.json
python 03_TOOLS\scripts\execution_contract\validate_task_contract.py --contract 03_TOOLS\scripts\execution_contract\examples\routing_edit_required.json
python 14_LAYOUT_AUTOMATION\scripts\routing_geometry_quality.py 14_LAYOUT_AUTOMATION\test_fixtures\routing_geometry\good_45_degree_route.json T_E_M_P\routing_geom_test\good.json --markdown T_E_M_P\routing_geom_test\good.md
python 14_LAYOUT_AUTOMATION\scripts\routing_geometry_quality.py 14_LAYOUT_AUTOMATION\test_fixtures\routing_geometry\bad_90_degree_route.json T_E_M_P\routing_geom_test\bad_90.json
python 14_LAYOUT_AUTOMATION\scripts\routing_geometry_quality.py 14_LAYOUT_AUTOMATION\test_fixtures\routing_geometry\bad_acute_jog_route.json T_E_M_P\routing_geom_test\bad_acute.json
python 14_LAYOUT_AUTOMATION\scripts\routing_geometry_quality.py 14_LAYOUT_AUTOMATION\test_fixtures\routing_geometry\bad_pad_entry_route.json T_E_M_P\routing_geom_test\bad_pad.json
python 14_LAYOUT_AUTOMATION\scripts\routing_geometry_quality.py 14_LAYOUT_AUTOMATION\test_fixtures\routing_geometry\bad_zigzag_route.json T_E_M_P\routing_geom_test\bad_zigzag.json
python 14_LAYOUT_AUTOMATION\scripts\score_placement_readiness.py 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb T_E_M_P\placement_test\placement.json --markdown T_E_M_P\placement_test\placement.md
python -  # YAML validation with PyYAML
python -  # docs link validation for GitHub-facing docs
python -  # manufacturing artifact allowlist validation
git ls-files '*.lck' '~*.lck' '.env' '.env.*' 'secrets.*' 'api_keys.*' 'local_credentials.*' 'private_config.*'
git status --short
git diff --name-only
python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --reason "GitHub dev infrastructure setup session" --apply
python 03_TOOLS\scripts\indexing\build_memory_index.py --repo-root .
python 03_TOOLS\scripts\indexing\build_history_index.py --repo-root .
python 03_TOOLS\scripts\ai_quality\build_ai_quality_index.py --repo-root .
python 03_TOOLS\scripts\ai_quality\build_current_known_problems.py --repo-root .
git add ...
git commit -m "Add GitHub dev infrastructure and Codespaces setup"
git push origin hardening/execution-contract
gh pr view 1 --json url,headRefName,baseRefName,isDraft,commits
git rev-parse HEAD
```

## Notes

- Temporary validation outputs were written under ignored `T_E_M_P/` and not staged.
- No KiCad design files were modified during validation.
