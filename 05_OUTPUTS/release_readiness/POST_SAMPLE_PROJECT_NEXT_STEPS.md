# Post Sample Project Next Steps

Date: `2026-05-06`

## Recommended Sequence

1. Build `17_RELEASE_BUILD/build_public_payload.py` with dry-run default.
2. Run dry-run payload build and prove raw imports, normalized samples,
   backups, history, generated outputs, PDFs, and `FAB_READY` files are absent.
3. Complete human license/release review for the ATtiny85 fixture.
4. Decide whether the first public release should include the sample source
   files or remain `LINK_ONLY_PLUS_DOCS`.
5. Resolve or formally accept the ATtiny85 `J1` shield ERC blocker.
6. Resolve DRC violations and schematic/footprint parity issues.
7. Complete human footprint/package/orientation review for `J1`, `J2`, and
   `U2`.
8. Complete human visual review sections for schematic and PCB close-ups.
9. Rerun the one-command gate runner and require `PASS` or a documented
   human-accepted exception before calling it a clean demo.
10. Run a focused public release dry-run audit after payload builder exists.

## Do Not Do Yet

- Do not call the fixture a clean golden path.
- Do not include sample KiCad source files in a public payload.
- Do not generate a fabrication package from the fixture.
- Do not claim public release readiness.
