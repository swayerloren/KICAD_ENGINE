# Direct Main Update Commands

Date/time: `2026-05-08T17:30:00-04:00`

Executed commands:

```powershell
git status --short
git branch --show-current
Remove-Item -Recurse -Force .ci
git add .github/workflows/ci.yml
git commit -m "Save latest repo documentation and infrastructure updates"
git push origin hardening/execution-contract
git checkout main
git pull origin main
git merge hardening/execution-contract --no-ff -m "Merge hardening and GitHub documentation updates"
git status --short
git diff --name-only origin/main..HEAD -- "*.kicad_sch" "*.kicad_pcb" "*.kicad_pro"
python - <<'PY'  # workflow YAML parse equivalent run from PowerShell via inline script
...
PY
python - <<'PY'  # tracked first-party compile check equivalent run from PowerShell via inline script
...
PY
python 03_TOOLS/scripts/execution_contract/validate_task_contract.py --contract 03_TOOLS/scripts/execution_contract/examples/docs_only.json
python 03_TOOLS/scripts/execution_contract/validate_task_contract.py --contract 03_TOOLS/scripts/execution_contract/examples/audit_only.json
python 03_TOOLS/scripts/execution_contract/validate_task_contract.py --contract 03_TOOLS/scripts/execution_contract/examples/pcb_edit_required.json
python 03_TOOLS/scripts/execution_contract/validate_task_contract.py --contract 03_TOOLS/scripts/execution_contract/examples/routing_edit_required.json
git push origin main
gh pr view 1 --json url,state,mergedAt,headRefName,baseRefName
git rev-parse HEAD
git ls-remote origin main
```

Notes:
- A Bash-style `&&` was attempted once in PowerShell and rejected by the shell parser.
- A parallel `git status` + `git commit` attempt created a temporary Git index-lock conflict; subsequent git operations were run serially.
