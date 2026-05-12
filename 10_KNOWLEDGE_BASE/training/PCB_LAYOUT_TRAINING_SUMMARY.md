# PCB Layout Training Summary

Status: `SUMMARY_ONLY`

## What Training Material Is Good For

- Explaining left-to-right signal flow and block layout thinking
- Showing why return paths matter
- Showing why connector orientation mistakes are expensive
- Teaching staged review instead of single-pass layout claims

## What Training Material Is Not Good For

- Replacing exact package drawings
- Approving USB, RF, or power layouts without part-specific evidence
- Defining fab-ready status
- Proving a board is routable

## Durable Lessons Promoted From This Phase

- Training sources are best used to generate review questions, not answers.
- Repeated lessons about short high-current loops, compact USB clusters, and
  readable block grouping reinforce existing repo rules but do not supersede
  them.
- Mixed training corpora easily contaminate confidence unless separated from
  official-source summaries.

## Review Prompts

- Is this lesson traceable to an official KiCad, vendor, or datasheet source?
- Does the lesson still apply to the exact part, package, stackup, and fab?
- Is the lesson only a style cue rather than a verifiable requirement?

