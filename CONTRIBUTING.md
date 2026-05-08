# Contributing

Contributions are welcome if they improve KiCad Engine while preserving local-first safety and KiCad-native workflows.

## Before Contributing

Read:

1. `README.md`
2. `AGENTS.md`
3. `DISCLAIMER.md`
4. `SECURITY.md`
5. `PUBLIC_RELEASE_CHECKLIST.md`

## Good Contributions

- Safer validation scripts.
- Better KiCad CLI workflows.
- Better datasheet metadata and source links.
- Verified component records with citations.
- Clearer prompt packs.
- Cross-platform setup improvements.
- Public-release hygiene.
- Documentation that reduces unsafe AI assumptions.

## Do Not Contribute

- Secrets, credentials, tokens, API keys, private license keys, or `.env` files.
- Copyrighted datasheet PDFs unless redistribution permission is confirmed.
- Fabrication outputs labeled final without full verification evidence.
- Scripts that silently install tools.
- Scripts that modify installed KiCad folders.
- Unverified footprint approvals.
- Fake datasheet values or unsupported component claims.

## Engineering Standards

- Keep scripts read-only by default.
- Ask before installing anything.
- Write reports under `02_HISTORY/` or `05_OUTPUTS/`.
- Keep generated manufacturing-style outputs labeled `NOT_FINAL`.
- Mark unknown specifications as `Unknown - requires source verification`.
- Prefer official vendor sources for component research.
- Treat connector orientation, package drawing, and footprint matching as high risk.

## KiCad Project File Policy

Do not edit KiCad project files unless the active project, target files, backup path, rollback plan, and verification plan are confirmed.

Protected files include:

- `.kicad_sch`
- `.kicad_pcb`
- `.kicad_pro`
- `.kicad_sym`
- `.kicad_mod`
- Gerber, drill, pick-and-place, STEP, and other manufacturing output files

## Testing

At minimum, run:

```bash
python health_check.py
```

On Windows, also run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\health_check.ps1
```

For script changes, run syntax or compile checks appropriate to the language.

## Pull Request Notes

Describe:

- What changed.
- Why it changed.
- What was tested.
- Any remaining warnings.
- Whether any KiCad project files were touched.
- Whether any datasheet or third-party redistribution rights are involved.
