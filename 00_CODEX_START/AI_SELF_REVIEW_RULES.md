# AI Self Review Rules

Every meaningful KiCad Engine session must include an AI self-review before closeout.

The self-review is not a confidence ritual. It is a strict check for unsupported engineering claims, hidden uncertainty, missing verification, and incorrect memory/history routing.

## Required Questions

Before closeout, the agent must answer:

1. Did I make any factual claim that was not backed by a source, file inspection, command output, KiCad file evidence, datasheet, or user-provided fact?
2. Did I guess any datasheet value, pinout, footprint, package, symbol, voltage, current, clearance, or manufacturing rule?
3. Did I claim something passed ERC/DRC without actual command output?
4. Did I claim a fabrication package is ready without human review?
5. Did I modify or recommend modifying KiCad files without backup/verification?
6. Did I confuse global memory with project memory?
7. Did I update history and memory in the correct locations?
8. Did I clearly mark uncertainty?
9. Did I create or update open issues for unresolved problems?
10. Did I update `FOR CHAT GPT.MD` if repo structure/workflow changed?

## Required Outputs

- AI self-review.
- AI response scorecard.
- Claim/evidence matrix for major engineering claims.
- Uncertainty log for unverified items.
- Hallucination-risk log for guessed, inferred, weakly sourced, or high-risk claims.
- Quality-gate failure record when the work is blocked.

## Pass Standard

The self-review passes only when the response is evidence-backed, uncertainty is visible, unresolved issues are logged, and the final answer does not overstate readiness.

