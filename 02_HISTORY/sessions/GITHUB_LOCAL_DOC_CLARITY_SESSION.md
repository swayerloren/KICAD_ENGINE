# GitHub Local Doc Clarity Session

Date/time: `2026-05-08T18:00:00-04:00`

Task:
- clarify repo wording so the root docs clearly present `KICAD_ENGINE` as the full local toolkit
- prevent `.github/README.md` from being misread as the whole project description
- improve ZIP-download and local VS Code guidance for Codex and Claude users

Actions taken:
1. Reviewed current `.github/README.md`, root `README.md`, root `START_HERE.md`, `00_CODEX_START/START_HERE.md`, and local/Codespaces docs.
2. Rewrote `.github/README.md` to explicitly scope it to the `.github/` folder only.
3. Updated root `README.md` with:
   - `Download ZIP / Local VS Code Use`
   - clearer startup/read-order guidance
   - explicit `What Is Included`
   - explicit `What Is Not Included`
   - stronger local KiCad and human-review warnings
4. Updated root `START_HERE.md` and `00_CODEX_START/START_HERE.md` to clarify local ZIP/clone use.
5. Updated `docs/CODESPACES_SETUP.md` and `docs/LOCAL_DEV_SETUP.md` so local use remains the default path and Codespaces stays optional.

Outcome:
- repo purpose is clearer for GitHub visitors
- local VS Code use is now explicitly documented
- no KiCad design files were edited

Status: `COMPLETE`
