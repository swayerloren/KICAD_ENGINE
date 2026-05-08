# Learning Loop Rules

KiCad Engine uses a deliberate learning loop so AI agents improve without inventing durable facts.

## Required Closeout Behavior

At the end of every meaningful AI session, Codex or Claude must:

1. Write a session log.
2. Write command logs if commands were run.
3. Write failed-attempt records if anything failed.
4. Write user-correction records if the user says something did not work, was wrong, or needs to be redone.
5. Create an AI self-review.
6. Create an AI response scorecard.
7. Create a claim/evidence matrix for major engineering claims.
8. Create an uncertainty log for anything not verified.
9. Create hallucination-risk log if any claim was guessed, inferred, or weakly sourced.
10. Create/update open issues for unresolved risks.
11. Update project memory only with durable project-specific lessons.
12. Update global memory only with reusable lessons.
13. Rebuild memory/history/AI-quality indexes.
14. Rebuild `CURRENT_KNOWN_PROBLEMS.md`.
15. Update `FOR CHAT GPT.MD` if repo structure, workflow, tool status, active project status, known blockers, or scoring rules changed.

## Learning Loop

1. Capture the event in history.
2. Classify it as session evidence, command evidence, user correction, failed attempt, issue, lesson, or durable memory.
3. Route it to the correct global or project location.
4. Mark it `UNVERIFIED` unless human-confirmed or verified by repeatable workflow evidence.
5. Promote only durable, reusable facts into memory.
6. Score the response honestly.
7. Keep indexes current.

## Anti-Hallucination Rule

Do not convert a guess into memory. If source evidence is missing, write `Unknown - requires source verification`.

## Quality Gate Rule

If a high-risk engineering claim is not source-backed, the quality gate must be `BLOCKED_UNTIL_HUMAN_REVIEW`.
