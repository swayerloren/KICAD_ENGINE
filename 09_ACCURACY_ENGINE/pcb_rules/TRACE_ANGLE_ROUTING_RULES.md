# Trace Angle Routing Rules

## Scope

These rules apply to all routed PCB copper unless a stricter project-specific rule exists.

## Mandatory Rules

- Avoid 90-degree trace corners where practical.
- Never use acute-angle trace bends sharper than 90 degrees unless there is no alternative and the exception is documented.
- Use 45-degree bends for normal routing.
- Use rounded, filleted, or otherwise smooth routing where practical for high-speed, RF, or other sensitive signals.
- USB `D+`/`D-` and other signal pairs should use clean, smooth, parallel routing where practical.
- Power traces may be wide, but must still use clean 45-degree transitions instead of crude square turns.
- `BUCK_SW` and regulator switching loops must be short, compact, and cleanly routed.
- Do not keep bad routing just because DRC does not flag it.
- A routed PCB is not ready for review if it visually has crude 90-degree, acute-angle, or awkward routing.
- If component placement causes ugly routing, move the local components instead of forcing ugly traces.

## Interpretation

- Two 45-degree bends are the default best-practice turn for normal routing.
- 90-degree turns may be manufacturable on modern processes, but they are still discouraged for professional routing quality.
- Acute angles can create poor copper geometry, manufacturing risk, and signal-quality problems.
- High-speed and high-frequency routing should prefer smoother geometry over blocky directional changes when the layout allows it.

## Required Review Flags

- `TRACE_ANGLE_REVIEW_REQUIRED`
- `NO_ACUTE_TRACE_BENDS_REQUIRED`
- `DRC_PASS_NOT_ROUTING_QUALITY_APPROVAL`

