# Benchmark Methodology

## Core Principles

KiCad Engine benchmarks must be reproducible, evidence-backed, and conservative.

- Use the same task prompt, constraints, source policy, and time limit for each compared tool.
- Record the KiCad version, operating system, AI tool, model or agent name when available, and repo revision or snapshot date.
- Record every output artifact used for scoring.
- Do not allow hidden human fixes before scoring.
- Do not score guesses as correct unless they are backed by cited sources or verified KiCad project evidence.
- Treat all fabrication-style outputs as `NOT_FINAL`.
- Require human review for connector orientation, footprint geometry, polarity, RF, USB, CAN, automotive, and manufacturing-package claims.

## Required Run Metadata

Each benchmark run should record:

- Task ID and task file.
- Date and local time.
- Runner name or reviewer.
- AI tool and model/agent, if known.
- KiCad version and `kicad-cli` version if used.
- Operating system.
- Workspace path.
- Input prompt.
- Allowed source files and web policy.
- Whether web research was allowed.
- Time limit and actual elapsed time.
- Whether KiCad project files were created, copied, or only reviewed.
- Verification commands attempted.
- Output artifact paths.

## Required Evidence

A valid run should include:

- Source citations or link records for every exact electrical/package claim.
- Datasheet or reference-manual revision/date when available.
- KiCad symbol candidate and selection evidence.
- KiCad footprint candidate and package-drawing evidence, or an explicit `UNVERIFIED_FOOTPRINT` flag.
- ERC result or reason ERC was not applicable.
- DRC result or reason DRC was not applicable.
- BOM or component list when the task creates or reviews a schematic.
- Human review flags for high-risk items.
- A no-hallucination self-audit listing unknowns.

## Scoring Model

Default total: 100 points.

- Datasheet and source evidence: 15
- Component selection: 10
- Schematic correctness: 20
- Symbol and footprint correctness: 20
- PCB/layout review or planning: 15
- Verification and manufacturing-package discipline: 15
- Safety, uncertainty, and no hallucinated specs: 5

Task files may adjust emphasis, but they must keep explicit scoring for source citations, symbol/footprint correctness, ERC/DRC evidence, BOM completeness, human review flags, and no hallucinated specs.

## Score Caps

Apply these caps before final scoring:

- Missing source citations for exact values: maximum 70.
- Unverified footprint marked as approved: maximum 50.
- Connector orientation not flagged for human review: maximum 60.
- Fabrication output labeled final without full verification: maximum 40.
- Hallucinated datasheet value or fake source URL: maximum 40.
- KiCad project file edited without active project and backup gate: invalid run unless the benchmark explicitly uses a disposable copied project.

## Result Publication Rules

Do not publish benchmark comparisons unless:

- The benchmark task definition is public.
- The same source policy and constraints were used for each compared tool.
- All artifacts needed for scoring are preserved or summarized without violating licenses.
- Datasheet and vendor document redistribution rules are respected.
- Scores include reviewer notes and uncertainty.
- The result clearly states that AI review is not fabrication approval.

## No Fake Results Rule

`15_BENCHMARKS/results/` starts empty except for its README. A benchmark result can be added only after an actual run with artifacts, metadata, scoring notes, and review status.
