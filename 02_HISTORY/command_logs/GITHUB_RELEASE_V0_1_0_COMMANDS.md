# GitHub Release v0.1.0 Commands

Date/time: `2026-05-08T17:36:00-04:00`

Executed commands:

```powershell
git checkout main
git pull origin main
git status --short
gh auth status
git add 05_OUTPUTS/release_readiness/RELEASE_v0.1.0_NOTES.md
git commit -m "Add v0.1.0 release notes"
git push origin main
git tag v0.1.0
git push origin v0.1.0
gh release create v0.1.0 --title "KiCad Engine v0.1.0" --notes-file 05_OUTPUTS/release_readiness/RELEASE_v0.1.0_NOTES.md
gh api repos/swayerloren/KICAD_ENGINE/releases/tags/v0.1.0
git rev-parse HEAD
git rev-list -n 1 v0.1.0
```

Notes:
- A parallel `git status` + `git add` attempt briefly caused a transient Git index-lock condition during the session. Subsequent git steps were run serially.
