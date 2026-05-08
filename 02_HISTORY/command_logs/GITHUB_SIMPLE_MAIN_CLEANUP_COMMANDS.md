# GitHub Simple Main Cleanup Commands

Date/time: `2026-05-08T17:45:00-04:00`

Executed commands:

```powershell
git status --short --untracked-files=all
git branch --show-current
gh pr view 1 --json url,state,mergedAt,headRefName,baseRefName
git fetch origin
git checkout main
git pull origin main
git rev-list --left-right --count main...origin/hardening/execution-contract
git merge-base --is-ancestor origin/hardening/execution-contract main
git merge origin/hardening/execution-contract --no-ff -m "Merge hardening and GitHub repo updates"
git status --short
git diff --name-only origin/main..HEAD -- "*.kicad_sch" "*.kicad_pcb" "*.kicad_pro"
git push origin main
gh pr close 1 --comment "Merged into main directly and closing PR because this private repo is using simple owner-direct updates for now."
git push origin --delete hardening/execution-contract
git branch -d hardening/execution-contract
git branch
git branch -r
git ls-remote --heads origin
git rev-parse HEAD
```

Notes:
- The PR close command returned a non-zero exit because PR `#1` was already in `MERGED` state, not because cleanup failed.
