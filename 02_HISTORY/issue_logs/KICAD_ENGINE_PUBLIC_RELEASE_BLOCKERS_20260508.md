# KICAD_ENGINE Public Release Blockers

Date: `2026-05-08`

Status: `OPEN`

Current blockers preventing a safe public release:

- `README.md` still marks public GitHub release as `NOT_READY`
- `PUBLIC_RELEASE_CHECKLIST.md` is not complete
- `21_LICENSE_ATTRIBUTION/LICENSE_AUDIT.md` remains `REQUIRES_HUMAN_REVIEW`
- historical docs and logs still contain placeholder-token or workflow-secret reference strings that need public-hygiene cleanup even though they are not live secrets
- intentionally ignored local-only content remains outside Git, including backups, copied-board rehearsal trees, raw imported originals, tool caches, env/config files, and large build artifacts

Current disposition:

- private GitHub push is complete
- public GitHub publication should remain blocked until these items are resolved
