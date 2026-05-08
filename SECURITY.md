# Security Policy

## No Secrets In The Repo

Do not store secrets in this repository.

Do not commit:

- API keys.
- Passwords.
- Private tokens.
- SSH private keys.
- License keys.
- AI service credentials.
- Distributor or fab-house credentials.
- `.env` files with real values.

Users must log in to Codex, Claude, GitHub, package managers, and other tools through their own local setup. KiCad Engine must not capture or store those credentials.

## Installer And Setup Script Safety

Setup and installer scripts must:

- Ask before installing anything.
- Show the package manager command before running it.
- Use official package managers where possible.
- Never silently install paid tools.
- Never collect credentials.
- Never write into installed KiCad application folders.
- Never edit KiCad project files without explicit project-edit approval and backup.

## Reporting Unsafe Scripts

Report scripts or workflows that:

- Delete files unexpectedly.
- Modify KiCad project files without backup.
- Modify installed KiCad folders.
- Install tools silently.
- Request or store credentials.
- Download restricted datasheets without permission review.
- Label fabrication outputs final without verification.

Use GitHub issues or the repository's security reporting channel when available. If the issue involves a real secret, do not paste the secret into a public issue.

## Supported Security Checks

Run:

```bash
python health_check.py
```

The health check includes a heuristic scan for likely secret files and assignment-style secret patterns. It is not a substitute for a dedicated secret scanner before a public release.

## No Silent Credential Capture

KiCad Engine must not capture:

- OpenAI credentials.
- Anthropic credentials.
- Codex session tokens.
- Claude session tokens.
- GitHub tokens.
- KiCad user configuration secrets.
- Vendor or distributor API keys.

Any future integration requiring authentication must keep credentials outside the repo and document the storage location and revocation path.
