# PCBNEW API Safe Usage

Status: `NORMALIZED_REFERENCE`

## Purpose

Define the repo-safe subset of `pcbnew` scripting patterns.

## Safe Defaults

- read-only extraction first
- detect KiCad Python context before importing `pcbnew`
- use helper wrappers instead of direct method assumptions
- mark missing attributes as unavailable, not as zero or guessed values
- prefer CLI for validation and export when object-level API access is not
  needed

## Unsafe Patterns To Avoid

- assuming repo Python can always import `pcbnew`
- treating `import pcbnew` success in one interpreter as portable proof
- assuming every board item exposes the same methods across KiCad versions
- directly calling fragile accessors without a wrapper, for example raw
  `via.GetWidth()` in scripts that must tolerate object/type differences
- mutating live boards when the task only needs extraction

## Required Workflow

1. run `kicad_python_context.py`
2. run `pcbnew_import_check.py` when needed
3. enter KiCad Python context for board-aware work
4. use `safe_pcbnew_helpers.py` wrappers for object access
5. keep DRC/ERC truth from KiCad, not from the helper layer

## Source Registry References

- `url_000015`
- `url_000950`
- `url_000951`
- `url_000956`
- `url_000959`
- `url_000960`
- `url_000962`
