# Checksum Rules

Status: `ACTIVE_RULES`

## Required Algorithm

Use SHA256 for release artifacts.

## Required File

`SHA256SUMS.txt`

## Scope

Include every uploaded release artifact:

- installer artifacts
- payload zip
- relevant build reports if uploaded as artifacts

## Verification

Release notes must tell users to compare downloaded artifact hashes against `SHA256SUMS.txt`.

## Security Note

Checksums help detect accidental corruption and simple tampering. They do not replace signing, notarization, or trusted release channels.

