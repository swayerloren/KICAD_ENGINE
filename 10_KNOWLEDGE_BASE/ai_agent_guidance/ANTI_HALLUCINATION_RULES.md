# Anti-Hallucination Rules

Status: `MANDATORY_FOR_ENGINEERING_CLAIMS`

## Core Rule

Do not create engineering certainty from memory, similar part names, package names, generated output, or a search result title. A KiCad Engine claim is usable only when it has evidence and the evidence type is named.

## Claim Classes

| Claim Type | Minimum Evidence | If Evidence Is Missing |
| --- | --- | --- |
| Exact electrical value or limit | Datasheet, reference manual, vendor design guide, or user-provided requirement | Mark `TODO_SOURCE_REQUIRED`. |
| Pinout or symbol mapping | Datasheet pin table plus symbol inspection | Mark `NEEDS_HUMAN_REVIEW` for high-risk parts. |
| Footprint or package match | Exact package drawing plus KiCad footprint pad review | Keep as candidate; block PCB/fab approval. |
| Connector orientation | Exact connector drawing, mating part, board edge direction, and human review | Block with `BLOCKED_UNTIL_HUMAN_REVIEW`. |
| ERC/DRC pass | Actual command output saved to history/report path | Say it was not run. |
| Fab readiness | Full verification gate plus human review | Export only `NOT_FINAL`, or stop. |
| Stock, price, lifecycle | Current authorized supplier/API/public source with retrieval date | Mark `SOURCE_LINK_ONLY` or `UNVERIFIED`. |

## Required Agent Behavior

- State the evidence type before making an engineering claim.
- Use exact source documents for exact values.
- Keep family-level guidance separate from part-specific proof.
- Keep generated dry-run records marked `UNVERIFIED`.
- Mark missing values as `Unknown - requires source verification` or `TODO_SOURCE_REQUIRED`.
- Record uncertainty in the AI closeout logs.
- Stop rather than guess when connector, footprint, PMOS, ESD, regulator, RF, USB, CAN, power, or manufacturing decisions are involved.

## Dangerous Phrases

Avoid unsupported statements such as:

- "This footprint is correct."
- "This pinout matches."
- "This is ready for fabrication."
- "The datasheet says..." without a cited source.
- "Standard USB-C wiring" without role, CC, VBUS, shield, and ESD evidence.
- "KiCad has this footprint" as if library presence proves package compatibility.

## Safe Replacement Language

Use language such as:

- "Candidate only; package drawing not verified."
- "Requires source verification."
- "Requires human connector orientation review."
- "General pattern, not part-specific proof."
- "ERC/DRC not run in this session."
- "NOT_FINAL review output."

## Closeout Requirement

If any claim is based on inference, generated output, source-link capture, or weak evidence, create a hallucination-risk log and include the claim in the claim/evidence matrix.
