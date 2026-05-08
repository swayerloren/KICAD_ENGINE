# Claim / Evidence Matrix

| Claim | Evidence |
|---|---|
| Worktree was clean at task start | `git status --short --untracked-files=all` returned empty |
| Current branch at task start was `main` | `git branch --show-current` |
| PR `#1` was already merged | `gh pr view 1 --json url,state,mergedAt,headRefName,baseRefName` |
| Hardening branch was already fully merged into `main` | `git merge-base --is-ancestor origin/hardening/execution-contract main` and `git merge ...` returned `Already up to date.` |
| No KiCad design files changed unexpectedly | `git diff --name-only origin/main..HEAD -- "*.kicad_sch" "*.kicad_pcb" "*.kicad_pro"` returned empty |
| Remote hardening branch was deleted | `git push origin --delete hardening/execution-contract` |
| Local hardening branch was deleted | `git branch -d hardening/execution-contract` |
| Only `main` remains locally and remotely | `git branch`, `git branch -r`, and `git ls-remote --heads origin` |
