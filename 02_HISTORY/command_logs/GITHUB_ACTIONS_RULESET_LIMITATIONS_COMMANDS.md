# GitHub Actions And Ruleset Limitations Commands

## Commands Run

```powershell
gh --version
gh auth status
git status -sb
git branch --show-current
Get-Content -Raw .github\workflows\ci.yml
Get-Content -Raw .github\workflows\docs-check.yml
Get-Content -Raw .github\BRANCH_PROTECTION_RECOMMENDATIONS.md
Get-Content -Raw docs\GITHUB_SETUP.md
Get-Content -Raw docs\CODESPACES_SETUP.md
Get-Content -Raw docs\BRANCH_AND_PR_WORKFLOW.md
python -  # YAML validation for workflow files
python -  # GitHub-facing docs link validation
python -  # obvious-secret token scan on tracked files
git status --short
git diff --name-only
python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --reason "GitHub Actions and ruleset limitations session" --apply
python 03_TOOLS\scripts\indexing\build_memory_index.py --repo-root .
python 03_TOOLS\scripts\indexing\build_history_index.py --repo-root .
python 03_TOOLS\scripts\ai_quality\build_ai_quality_index.py --repo-root .
python 03_TOOLS\scripts\ai_quality\build_current_known_problems.py --repo-root .
git add ...
git commit -m "Add GitHub Actions and branch workflow docs"
git push origin hardening/execution-contract
gh pr view 1 --json url,headRefName,baseRefName,isDraft,commits
git rev-parse HEAD
```

## Notes

- This task reused the GitHub infrastructure added on the same branch and focused only on the remaining private-repo limitation guidance and hygiene scan.
- No KiCad design files were modified.
