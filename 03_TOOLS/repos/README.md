# 03_TOOLS/repos

## PURPOSE

Local-only clones of third-party tool repositories used for inspection, safe local testing, and isolated integration work.

## WHAT_BELONGS_HERE

- Approved external helper repos such as `kicad-mcp-pro`, `kicad-happy`, `KiBot`, `InteractiveHtmlBom`, `PcbDraw`, and `kicanvas`.
- Their local `.git/` metadata and clean working trees.
- No active KiCad project source files.

## WHY_CONTENTS_ARE_IGNORED

- These folders are vendored clones, not first-party repo source.
- Including them would bloat the GitHub payload with third-party history, duplicated licenses, and nested Git metadata.
- The tracked repo already records the expected upstream sources and local usage in `00_CODEX_START/REPO_MAP.md` and `00_CODEX_START/TOOL_INDEX.md`.

## HOW_TO_RECREATE_LOCALLY

1. Use the upstream URLs and local path guidance recorded in `00_CODEX_START/REPO_MAP.md`.
2. Clone only the approved third-party repos that are actually needed for the local workflow.
3. Keep those working trees clean and read-only by default.
4. If a tool needs tracked documentation, add or update a first-party note or manifest instead of committing the clone itself.

## WHAT_SHOULD_NEVER_BE_COMMITTED

- cloned third-party working trees
- nested `.git/` directories
- local patches that belong in upstream or a separate reviewed fork
- build outputs, caches, logs, secrets, or credentials

## PUBLIC_RELEASE_NOTES

GitHub should show this folder as a placeholder only. The actual local clones remain ignored on purpose.
