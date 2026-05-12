# Post-Knowledge-Migration Security Scan

Generated: `2026-05-12`

Status: `PASS_WITH_FALSE_POSITIVE_CONTEXT`

## Checks Run

1. `.env` / key / cert filename scan
2. broad secret-pattern scan with heavy local-tooling exclusions
3. public-payload quarantine-reference scan
4. `.sfdx/` hygiene check
5. staged-file / staged-large-file scan

## Results

### 1. `.env` / key / cert filename scan

Result: `PASS_WITH_LOCAL_TOOLING_CERT_FILES`

No committed `.env` files were found.

Observed local files were:

- cert bundles under ignored Python environments
- one ignored local dev SSL key under `03_TOOLS/node_envs/...`
- one `.env.example` under `03_TOOLS/repos/kicad-mcp-pro/`

These do not represent live committed secrets for the push scope.

### 2. Broad secret-pattern scan

Result: `FALSE_POSITIVE_HEAVY`

The requested patterns:

- `ghp_`
- `github_pat_`
- `sk-`
- `API_KEY`
- `SECRET`
- `TOKEN`
- `PASSWORD`
- `.env`

still hit many expected non-secret contexts, including:

- security policies
- payload exclusion rules
- masked audit summaries
- supplier connector docs naming required environment variables
- migration/source-registry historical path metadata

No high-confidence live credential was identified.

### 3. Public-payload quarantine-reference scan

Result: `PASS`

Targeted scan bases:

- `17_RELEASE_BUILD/`
- `18_PUBLIC_DOCS/`
- `23_PACKAGE_PROFILES/`
- `24_FAB_PROFILES/`
- `docs/`

Hits for `knowledge_scrape_quarantine`, `license_risk_reviews`, or
`rejected_low_value`: `0`

### 4. `.sfdx/` hygiene check

Result: `PASS`

- `.sfdx/` exists on disk: `NO`
- `.gitignore` still contains `.sfdx/` at line `95`
- no `.sfdx/` files are staged

### 5. Staged-file / staged-large-file scan

Result: `PASS`

- staged file count: `0`
- staged files over `50 MB`: `0`

## Large Local Files Present

Large local/generated files still exist under ignored or local-only trees, such
as:

- `installer/build/`
- `installer/node_modules/`
- `03_TOOLS/python_envs/`
- `05_OUTPUTS/clean_sample_candidate_tests/`

This is not a push blocker because they are not staged.

## Conclusion

No high-confidence live secrets were found, `.sfdx/` is no longer a blocker,
and the security scan does not block a later explicit-staging commit/push
workflow.
