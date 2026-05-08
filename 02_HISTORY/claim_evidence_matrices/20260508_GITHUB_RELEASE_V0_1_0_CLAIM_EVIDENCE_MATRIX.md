# Claim / Evidence Matrix

| Claim | Evidence |
|---|---|
| Working tree was clean before release notes were added | `git status --short` returned empty |
| Release-notes commit hash is `43445274e48d0a0ed3fb6739deedd65fc865c5f6` | `git rev-parse HEAD` immediately after release-note commit and `git rev-list -n 1 v0.1.0` |
| Tag `v0.1.0` was created and pushed | `git push origin v0.1.0` succeeded |
| GitHub release exists | `gh release create ...` returned the release URL |
| Release remains private/internal in posture and not fabrication-ready | `RELEASE_v0.1.0_NOTES.md` contents and current repo visibility state |
| No KiCad design files were edited | No `.kicad_sch`, `.kicad_pcb`, or `.kicad_pro` files were touched in the session |
