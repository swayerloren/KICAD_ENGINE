# Security Policy

Status: `ACTIVE_POLICY`

## Scope

Security concerns include unsafe scripts, credential handling, installer behavior, release artifacts, dependency usage, and accidental secret commits.

## Core Rules

- Do not store secrets in the repo.
- Do not collect AI provider credentials.
- Do not silently install tools.
- Do not modify installed KiCad folders.
- Do not modify user-global KiCad libraries.
- Do not publish artifacts without checksums.

## Reporting

Use `22_SECURITY/REPORTING_SECURITY_ISSUES.md` and root `SECURITY.md`.

