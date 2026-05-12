# GitHub Push Security Scan

Generated: `2026-05-12`

Status: `PASS_WITH_FALSE_POSITIVE_CONTEXT`

## Preconditions

- branch: `main`
- remote: `https://github.com/swayerloren/KICAD_ENGINE.git`
- `gh` installed: `YES`
- `gh` authenticated: `YES`

## Checks Run

1. requested broad token/secret scan
2. `.env` / secret-like filename scan
3. `.sfdx/` presence check
4. staged-file count check
5. staged KiCad-design-file check

## Results

### Requested broad token/secret scan

Result: `FALSE_POSITIVE_HEAVY`

The required patterns:

- `ghp_`
- `github_pat_`
- `sk-`
- `API_KEY`
- `SECRET`
- `TOKEN`
- `PASSWORD`
- `.env`

still match many expected non-secret contexts, including:

- security-policy docs
- installer/build workflow docs
- supplier connector environment-variable docs
- masked historical audit summaries
- migration/source-registry historical path metadata
- command logs that mention placeholder token names

No high-confidence live credential was identified.

### `.env` / secret-like filename scan

Result: `PASS_WITH_LOCAL_TOOLING_CERT_FILES`

No committed `.env` files were found.

Observed local files were:

- ignored local dev SSL key under `03_TOOLS/node_envs/...`
- cert bundles under ignored Python environments
- `.env.example` under `03_TOOLS/repos/kicad-mcp-pro/`

These are outside the intended push scope.

### `.sfdx/`

Result: `PASS`

- `.sfdx/` exists on disk: `NO`
- `.gitignore` rule present: `YES`

### Staged-file status

Result: `PASS`

- staged file count after safe staging cleanup: `1009`
- staged KiCad design files after safe staging cleanup: `0`
- staged raw extraction capture files: `0`
- staged `.sfdx/` paths: `0`
- staged files over `50 MB`: `0`

## Conclusion

No high-confidence secrets were found for the intended push scope.

Push may proceed only with explicit safe staging and with KiCad design files
remaining unstaged.
