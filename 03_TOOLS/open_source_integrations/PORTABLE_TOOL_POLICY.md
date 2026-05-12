# Portable Tool Policy

KiCad Engine is intended to stay ZIP-portable. This policy explains how optional
tooling fits that goal.

## Core Portability Rule

The tracked repo must contain only first-party integration code, docs, small
metadata files, and safe wrappers. Large third-party tool payloads stay outside
Git by default.

## Portable Patterns

- Keep only requirements files, wrapper scripts, and source URLs in Git.
- Install lightweight optional packages into `.tools/venvs/`.
- Store temporary download caches under `.tool_cache/`.
- Record external-only tools as documented prerequisites instead of vendored
  repo content.
- Make verification scripts succeed with informative `NOT_INSTALLED` results.

## Non-Portable Patterns

- Committing `.venv/`, `venv/`, `node_modules/`, or large jar bundles
- Shipping upstream clones in the repo root
- Depending on machine-local absolute clone paths as if they were repo truth
- Requiring a large tool download for a docs-only or audit-only workflow

## Release Rule

ZIP release payloads may include:

- first-party wrappers
- requirements files
- tiny example configs
- attribution and license notes

ZIP release payloads must not include:

- optional third-party binaries
- external repo clones
- generated install environments
- local package-manager caches
