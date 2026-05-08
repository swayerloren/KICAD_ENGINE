# Master Scoring Rubric

Default score: 100 points.

## Categories

| Category | Points | Measures |
| --- | ---: | --- |
| Datasheet and source evidence | 15 | Correct source citations, revision awareness, exact value provenance, no fake URLs |
| Component selection | 10 | Fit to requirements, voltage/current/interface/package/lifecycle awareness |
| Schematic correctness | 20 | Nets, power, decoupling, boot/debug, connectors, interface circuits, ERC discipline |
| Symbol and footprint correctness | 20 | Correct symbol, pinout evidence, exact footprint/package drawing, 3D/mechanical status |
| PCB/layout review or planning | 15 | Placement risks, routing risks, high-risk nets, connector/polarity/RF/USB/CAN layout flags, DRC discipline |
| Verification and manufacturing discipline | 15 | ERC, DRC, BOM, Gerber/drill/PNP/STEP/output manifest, `NOT_FINAL` labels |
| Safety and uncertainty | 5 | Human review flags, no hallucinated specs, unknowns marked clearly |

## Required Scoring Topics

Every task score must account for:

- Correct component selection.
- Source citations.
- Correct symbol.
- Correct footprint.
- Power design correctness.
- Decoupling completeness.
- Boot/debug correctness when MCU-related.
- Connector orientation verification.
- ERC result or scoped reason absent.
- DRC result or scoped reason absent.
- BOM completeness when components are involved.
- Manufacturing output completeness when outputs are involved.
- Human review flags.
- No hallucinated specs.

## Severity Levels

- `Critical`: can cause fabrication failure, board damage, safety risk, or false public claim.
- `Major`: can cause design malfunction, wrong footprint, incomplete verification, or misleading score.
- `Minor`: clarity, formatting, or non-blocking evidence weakness.
- `Observation`: useful note with no immediate score penalty.

## Score Caps

- Fake source URL or hallucinated exact datasheet value: maximum 40.
- Missing citations for exact electrical/package claims: maximum 70.
- Unverified footprint marked approved: maximum 50.
- Connector orientation not reviewed: maximum 60.
- Polarity-sensitive part not flagged: maximum 70.
- ERC/DRC omitted without explanation when applicable: maximum 80.
- Manufacturing outputs labeled final without full gate: maximum 40.
- Hidden human fix before scoring: invalid run.

## Result Wording

Allowed result wording:

- "The run scored X/Y under the documented rubric."
- "The run is not fabrication approval."
- "The run requires human review for listed items."

Disallowed result wording:

- "Fab ready" unless a separate verified fabrication-release process exists.
- "Beats another tool" unless the same task and scoring evidence are shown for both.
- "Verified footprint" without exact package/connector drawing evidence and human review where required.
