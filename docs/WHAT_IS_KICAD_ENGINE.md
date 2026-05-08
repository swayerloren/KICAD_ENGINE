# What Is KiCad Engine

KiCad Engine is a local-first workspace for AI-assisted KiCad engineering.

It combines repo rules, VS Code tasks, prompt packs, component metadata, datasheet metadata, KiCad app discovery, validation scripts, and review-output workflows.

## Core Idea

AI coding agents work best when they can read a structured workspace instead of guessing. KiCad Engine gives Codex, Claude, and similar agents a clear operating manual for KiCad tasks:

- Read context first.
- Prefer CLI and file inspection.
- Use installed KiCad instead of replacing it.
- Avoid unsafe GUI automation.
- Keep reports and history.
- Mark uncertain data clearly.
- Treat manufacturing outputs as `NOT_FINAL` until reviewed.

## Not A Replacement For KiCad

KiCad remains the EDA tool. KiCad Engine is the surrounding workspace that helps with:

- Research
- Planning
- Review
- Validation
- Output organization
- AI-agent safety
- Public-release hygiene

The user still makes final engineering and manufacturing decisions.
