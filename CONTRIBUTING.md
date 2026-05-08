# Contributing

KiCad Engine accepts contributions that improve safety, clarity, repeatability, and honest engineering evidence. This repo is still an internal/private alpha, so the contribution bar is correctness first, convenience second.

## Read Before Opening A PR

1. [README.md](README.md)
2. [START_HERE.md](START_HERE.md)
3. [REPO_INDEX.md](REPO_INDEX.md)
4. [WORKFLOWS_INDEX.md](WORKFLOWS_INDEX.md)
5. [SECURITY.md](SECURITY.md)
6. [PUBLIC_RELEASE_STATUS.md](PUBLIC_RELEASE_STATUS.md)
7. [PUBLIC_RELEASE_CHECKLIST.md](PUBLIC_RELEASE_CHECKLIST.md)

## Good Contributions

- Safer validation scripts and wrappers
- Better memory/history maintenance
- Clearer repo navigation and documentation
- Verified component, symbol, and footprint records with evidence
- Better KiCad CLI or report-generation workflows
- Clearer project state, stale-report, and gate-reconciliation tooling
- Public-release hygiene improvements

## Do Not Contribute

- Secrets, tokens, passwords, API keys, `.env` files, or local credentials
- KiCad lock files or temporary process locks
- Raw caches, large local rehearsal artifacts, or backup folders
- Fabrication files marked final without complete verification evidence
- Unsupported engineering claims, guessed values, or fake benchmark results
- Copyrighted datasheets or vendor documents unless redistribution rights are confirmed

## KiCad Design File Policy

Protected file classes include:

- `.kicad_sch`
- `.kicad_pcb`
- `.kicad_pro`
- project libraries
- generated fabrication outputs

Do not edit those files unless:

1. the active project is identified,
2. the target files are inside that project,
3. a backup exists,
4. the relevant phase gates are satisfied or the exception is explicitly logged,
5. verification evidence will be produced after the change.

## Pull Request Expectations

Every PR should state:

- what changed
- why it changed
- what was tested
- whether any KiCad design files were touched
- whether any generated or local-only files were intentionally excluded
- remaining risks, blockers, or human-review needs

Use the repository issue and PR templates in `.github/`.

## Testing

At minimum, run the checks appropriate to your change:

```powershell
python -m py_compile <changed_python_files>
git status
```

Useful repo-level validation entry points:

- `python 03_TOOLS/scripts/maintenance/run_maintenance_cycle.py --project <ACTIVE_PROJECT_PATH>`
- `python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project <ACTIVE_PROJECT_PATH> --phase <PHASE>`
- `python 03_TOOLS/scripts/project_state/build_live_project_state.py --project <ACTIVE_PROJECT_PATH> --apply`

## Commit Scope

- Stage safe files only.
- Do not stage ignored or local-only content.
- Do not force unrelated history cleanup into a feature PR.
- Prefer small, reviewable documentation and tooling commits over mixed-purpose changes.
