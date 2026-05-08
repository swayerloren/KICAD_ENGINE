# AI Truthfulness Scoring

Truthfulness scoring measures how well an AI response is supported by evidence and how honestly it reports uncertainty.

## Overall Score

Overall score: `0-100`

Categories:

- Evidence support: `0-20`
- KiCad-specific correctness: `0-20`
- Datasheet/component accuracy: `0-15`
- Safety/compliance with repo rules: `0-15`
- Memory/history routing correctness: `0-10`
- Uncertainty disclosure: `0-10`
- End-user usefulness: `0-10`

## Evidence Support

High score requires claims backed by:

- inspected files,
- command output,
- KiCad source-file evidence,
- datasheets or package drawings,
- user-provided facts,
- documented repo rules.

Penalize:

- unsupported engineering claims,
- claims from memory alone,
- missing citations to local evidence,
- unlogged commands.

## KiCad-Specific Correctness

Reward:

- exact file paths,
- correct KiCad source/output distinctions,
- actual ERC/DRC command evidence,
- correct `NOT_FINAL` manufacturing status.

Penalize:

- claiming ERC/DRC pass without output,
- editing protected files without backup,
- treating review outputs as fabrication approval.

## Datasheet And Component Accuracy

Reward exact source-backed values. Penalize guessed datasheet values, inferred pinouts, guessed footprints, or package assumptions.

## Score Labels

- `90-100`: strong evidence, low uncertainty, correct routing.
- `75-89`: usable but has limited uncertainty or evidence gaps.
- `50-74`: mixed evidence; requires review before relying on engineering details.
- `25-49`: high risk; major claims are unsupported.
- `0-24`: blocked; unsafe or mostly unsupported.

