# GitHub README Workflow Rewrite Session

- Date: `2026-05-08`
- Repo: `C:\Users\LJ\GitHub\KICAD_ENGINE`
- Branch: `hardening/execution-contract`
- Task type: `GITHUB_DOCS_ONLY`
- Design-file edits: `NONE`

## Goal

Rewrite the GitHub-facing root README so the repo clearly explains the AI-assisted KiCad workflow, routing rules, manufacturing/export guardrails, and how humans plus VS Code AI agents should use the workspace.

## Work Performed

- Ran the required maintenance cycle because the active-project prompt counter was due.
- Reviewed the current root README, `.github/README.md`, active-project status files, and final PCB review packet.
- Rewrote `README.md` as the repo front door for humans and AI agents.
- Narrowed `.github/README.md` to GitHub-collaboration metadata and pointed it back to the canonical root docs.
- Validated relative Markdown links in the changed docs.
- Recorded a remaining workflow gap: no schematic-specific execution-contract task type exists yet.

## Outcome

- Root README now explains what the repo is, what it is not, why it exists, how the workflow works, how to use it with Codex/Claude, the routing rules, manufacturing/export workflow, current project state, safety rules, and example prompts.
- No KiCad design files were changed.
- Repo documentation is clearer for first-open GitHub readers, but the repo remains private and not public-release-ready.
