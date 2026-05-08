# Routing Geometry Hard Fail Limitations

Date: `2026-05-08`
Status: `OPEN`

## Limitation

Pad-entry quality is currently inferred from straight-run length before the
first or last bend because the planning fixture schema does not yet include full
pad-shape entry geometry.

## Impact

The current detector is effective for planning fixtures and obvious bad exits,
but a future real-board bridge can improve fidelity by using real pad shape and
orientation data.
