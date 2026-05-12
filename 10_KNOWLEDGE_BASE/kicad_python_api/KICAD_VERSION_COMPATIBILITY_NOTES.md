# KiCad Version Compatibility Notes

Status: `NORMALIZED_REFERENCE`

## Main Risk

`pcbnew` bindings are version- and runtime-sensitive. A helper that works with
one KiCad/Python combination may fail on another if the DLL/runtime pairing is
wrong or if bindings changed.

## Repo Expectations

- detect context before board-aware work
- tolerate missing methods and changed bindings
- avoid assuming Doxygen examples map 1:1 onto the current runtime
- prefer stable read-only extraction patterns over fragile deep mutation flows

## Practical Rule

When a script only needs proof of ERC/DRC/export status, prefer `kicad-cli`.
Reserve `pcbnew` for object-level inspection and carefully bounded helper
workflows.

## Source Registry References

- `url_000950`
- `url_000963`
- `url_002920`
- `url_002929`
- `url_002931`
