# Security Policy

KiCad Engine is a local-first engineering repo. Security here mostly means preventing accidental publication of secrets, preventing unsafe automation, and keeping local-only artifacts out of GitHub.

## No Secrets In The Repo

Never commit:

- API keys
- passwords
- private tokens
- GitHub auth codes
- `.env` files with live values
- license keys
- distributor or vendor credentials
- local credential snapshots

The current `.gitignore` protects the common classes, but contributors are still responsible for verifying what is staged.

## Security Checks Before Push

Before pushing, verify:

1. `git status`
2. no `.env` files are staged
3. no `*.lck` files are staged
4. no obvious secret strings are staged
5. no local-only backups or copied-board rehearsal trees are staged

Reference records:

- [05_OUTPUTS/release_readiness/GITHUB_PUSH_SECURITY_SCAN.md](05_OUTPUTS/release_readiness/GITHUB_PUSH_SECURITY_SCAN.md)
- [05_OUTPUTS/release_readiness/GITHUB_PUSH_FILE_INCLUDE_EXCLUDE_AUDIT.md](05_OUTPUTS/release_readiness/GITHUB_PUSH_FILE_INCLUDE_EXCLUDE_AUDIT.md)

## Protected Content Classes

Do not publish:

- `99_BACKUPS/`
- copied-board routing rehearsals
- raw imported sample originals
- caches and temp folders
- local env or credentials files
- manufacturing artifacts unless the release workflow explicitly approves them

## Unsafe Automation

Unsafe behaviors include:

- silent tool installation
- credential capture
- editing KiCad design files without backup or phase confirmation
- publishing final/fabrication-ready claims without verification evidence
- GUI automation without the required safety gates

## Reporting

If you find a security problem:

- do not paste secrets into an issue
- rotate the credential first if a real secret is exposed
- open a private report path if available, or a sanitized internal issue

Current policy references:

- [22_SECURITY/SECURITY_POLICY.md](22_SECURITY/SECURITY_POLICY.md)
- [AGENTS.md](AGENTS.md)
- [PUBLIC_RELEASE_STATUS.md](PUBLIC_RELEASE_STATUS.md)
