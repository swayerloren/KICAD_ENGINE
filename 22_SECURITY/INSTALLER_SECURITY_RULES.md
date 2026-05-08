# Installer Security Rules

Status: `ACTIVE_POLICY`

## Rules

- Ask before installing anything.
- Use official package managers where possible.
- Do not request or store credentials.
- Do not modify KiCad installation folders.
- Do not modify user-global library tables.
- Write setup logs without secrets.
- Document unsigned builds clearly.
- Generate checksums for release artifacts.

## Blockers

Block release if the installer silently installs tools, writes into KiCad app folders, stores credentials, or copies unreviewed private files.

