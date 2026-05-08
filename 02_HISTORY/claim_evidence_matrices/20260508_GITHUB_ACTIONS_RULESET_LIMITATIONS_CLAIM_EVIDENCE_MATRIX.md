# Claim / Evidence Matrix - GitHub Actions And Ruleset Limitations

| Claim | Evidence | Status |
| --- | --- | --- |
| The docs now explicitly say rulesets may not enforce on this private personal repo. | `.github/BRANCH_PROTECTION_RECOMMENDATIONS.md`, `docs/GITHUB_SETUP.md` | `VERIFIED_BY_FILE` |
| The intended ruleset target branch pattern is documented as `main`. | `.github/BRANCH_PROTECTION_RECOMMENDATIONS.md`, `docs/GITHUB_SETUP.md` | `VERIFIED_BY_FILE` |
| The repo-hygiene workflow now scans for obvious live secret-token patterns. | `.github/workflows/kicad-engine-checks.yml` | `VERIFIED_BY_FILE` |
| No KiCad design files were changed in this task. | `git diff --name-only`, `git status --short` | `VERIFIED_BY_COMMAND` |
