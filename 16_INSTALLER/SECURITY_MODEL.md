# Installer Security Model

Status: `PLANNED_SECURITY_MODEL`

## Threat Model

Primary risks:

- Silent dependency installation.
- Credential capture.
- Writing into installed KiCad folders.
- Copying unsafe or private files into the payload.
- Unsigned or tampered installer artifacts.
- Logs accidentally containing secrets.

## Security Rules

- Ask before installing dependencies.
- Never request or store AI provider credentials.
- Never write to installed KiCad app folders.
- Never modify user-global KiCad libraries or library tables.
- Keep logs local and scrub obvious secrets.
- Generate checksums for release artifacts.
- Document signing and notarization status.

## Installer Permissions

The installer should run with normal user permissions whenever possible. It should avoid elevation unless a dependency installer explicitly requires it and the user approves.

## Public Release Gate

Public installer release requires:

- Secret scan.
- Payload manifest review.
- Dependency install prompt review.
- Native platform smoke test.
- Checksum generation.
- Security policy updated.

