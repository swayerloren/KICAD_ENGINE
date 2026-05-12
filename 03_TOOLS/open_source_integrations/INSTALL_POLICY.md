# Optional Tool Install Policy

This policy governs optional tool integration in KiCad Engine.

## Hard Rules

1. Default repo behavior must remain usable after ZIP extraction without
   mandatory large downloads.
2. Optional tools install into `.tools/` or a user-local cache, not into tracked
   repo folders.
3. Never commit generated virtual environments, `node_modules`, build folders,
   cloned external repos, or downloaded binaries unless LJ explicitly approves
   that exact payload.
4. Use requirements files for lightweight Python packages whenever practical.
5. Use submodules only when license, size, update burden, and portability have
   all been reviewed and accepted.
6. Any large external tool must be documented as an optional external dependency
   instead of being silently bundled.
7. Every optional tool must have either an offline fallback or a graceful
   `not installed` failure mode.

## Default Behavior

- Install wrappers must be dry-run by default.
- Applying installs requires an explicit user or task request.
- External-only tools must print manual setup guidance instead of attempting a
  blind clone.

## Allowed Install Targets

- `.tools/venvs/<category>`
- `.tool_cache/`
- user-local package-manager caches

## Not Allowed

- Silent tool installation during unrelated engineering tasks
- Unreviewed vendoring of upstream repos into the repo root
- Committing downloaded jars, app bundles, `node_modules`, or Python envs
- Treating tool output as valid engineering proof without the normal repo gates
