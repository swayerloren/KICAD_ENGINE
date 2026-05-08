# Claim / Evidence Matrix

| Claim | Evidence |
|---|---|
| Starting branch was `hardening/execution-contract` | `git branch --show-current` |
| Only real pending repo change was `.github/workflows/ci.yml` plus local `.ci/` temp files | `git status --short --untracked-files=all` |
| No KiCad design files were changed unexpectedly | `git diff --name-only origin/main..HEAD -- "*.kicad_sch" "*.kicad_pcb" "*.kicad_pro"` returned empty |
| Hardening branch was pushed successfully | `git push origin hardening/execution-contract` |
| `main` merged the hardening branch cleanly | `git merge hardening/execution-contract --no-ff ...` succeeded with no conflicts |
| `main` push succeeded | `git push origin main` |
| PR `#1` is already merged | `gh pr view 1 --json url,state,mergedAt,headRefName,baseRefName` returned `state: MERGED` |
