# Memory And History Routing Rules

## Global Memory

Use `01_MEMORY/` for reusable, durable behavior and engineering lessons:

- Repo-wide workflow lessons.
- Common AI mistakes to avoid.
- Verified workflow rules.
- User corrections that apply across projects.
- Cross-project KiCad review and automation lessons.
- Global AI reliability rules, hallucination risks, unverified claim categories, and quality-gate rules.

## Global History

Use `02_HISTORY/` for repo-wide evidence:

- Session logs.
- Command logs.
- Failed attempts.
- User correction evidence.
- Issue logs.
- Workflow runs.
- Design and release audits.
- AI self-reviews.
- AI response scorecards.
- Claim/evidence matrices.
- Uncertainty logs.
- Hallucination-risk logs.
- Quality-gate failures.

## Project Memory

Use `04_KICAD_PROJECTS/active/PROJECT/memory/` for durable project facts:

- Component decisions.
- Footprint decisions.
- Datasheet status.
- Project-specific design rules.
- Project-specific user corrections.
- Project-specific mistakes to avoid.
- Open design risks.
- Project AI reliability rules.
- Project hallucination risks.
- Project unverified claims.
- Project quality-gate rules.

## Project History

Use `04_KICAD_PROJECTS/active/PROJECT/history/` for project evidence:

- Sessions.
- Command logs.
- Failed attempts.
- User corrections.
- Design decisions.
- Issue logs.
- Workflow runs.
- Verification runs.
- AI self-reviews.
- AI response scorecards.
- Claim/evidence matrices.
- Uncertainty logs.
- Hallucination-risk logs.
- Quality-gate failures.

## Promotion Test

Before updating memory, answer:

1. Will this still matter in a future session?
2. Is it durable rather than just a command result?
3. Does it belong globally or only in one project?
4. Is it verified, user-confirmed, or clearly marked `UNVERIFIED`?
5. Is there a history record that explains where it came from?
6. Is there an AI quality scorecard or uncertainty/risk log if the fact affects engineering quality?
