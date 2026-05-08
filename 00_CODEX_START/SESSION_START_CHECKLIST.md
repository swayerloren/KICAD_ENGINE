# Session Start Checklist

Use this checklist at the beginning of every Codex session.

## Read Order
- Confirm root `AGENTS.md` has been read.
- Confirm root `README_GPT.md` has been read.
- Confirm root `FOR CHAT GPT.MD` has been read.
- Confirm `00_CODEX_START/START_HERE.md` has been read.
- Confirm `00_CODEX_START/SESSION_START_CHECKLIST.md` has been read.
- Confirm `00_CODEX_START/STRUCTURE_STANDARD.md` has been read.
- Confirm `00_CODEX_START/FOLDER_ROUTING_RULES.md` has been read.
- Confirm `00_CODEX_START/PATH_PORTABILITY_RULES.md` has been read.
- Confirm `00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md` has been read.
- Confirm `00_CODEX_START/MEMORY_INDEX.md` has been read.
- Confirm `00_CODEX_START/HISTORY_INDEX.md` has been read.
- Confirm `00_CODEX_START/KICAD_PIPELINE_STARTUP_RULES.md` has been read when KiCad project pipeline work is in scope.
- If working on a project, confirm active project memory/history has been read.
- Confirm `CONTROL_PLANES.md` has been read before selecting tools.
- Continue through task-relevant `00_CODEX_START/` files before making KiCad engineering claims or touching project files.

## Project Identification
- Read `CURRENT_PROJECT.md`.
- State the active project name.
- State the active project path.
- State the current task mode.
- If the active project is `NONE`, do not touch KiCad project files.

## Context Review
- Read relevant global memory files in `01_MEMORY/`.
- Read relevant global learning files such as `AGENT_LESSONS_LEARNED.md`, `AGENT_MISTAKES_TO_AVOID.md`, `USER_CORRECTIONS_MEMORY.md`, `VERIFIED_WORKFLOWS.md`, `FAILED_WORKFLOWS.md`, and `MEMORY_UPDATE_RULES.md`.
- Read relevant project memory in `04_KICAD_PROJECTS/active/PROJECT/memory/` when an active project exists.
- Read legacy project memory under `01_MEMORY/projects/<project-id>/` when it contains current project context.
- Read relevant session logs, reviews, command logs, ERC/DRC reports, correction records, failed attempts, issue logs, workflow runs, and fabrication reviews under `02_HISTORY/`.
- Read relevant project history in `04_KICAD_PROJECTS/active/PROJECT/history/` when an active project exists.
- Read `CURRENT_KNOWN_PROBLEMS.md`.
- Read relevant AI quality files and prior scorecards, self-reviews, hallucination-risk logs, claim/evidence matrices, quality-gate failures, and uncertainty logs.

## Control Plane Check
- State whether the task belongs primarily to the common, Windows, or Linux control plane.
- Confirm whether legacy paths are being used.
- Confirm older non-GitHub checkout paths are not used for edits unless they exist and the user explicitly selected them.
- Confirm whether GUI automation is needed or avoidable.
- If KiCad GUI work is requested, confirm whether KiCad is already open.
- Confirm whether the project context is an original finished PCB, copied reference project, or active design project.
- Confirm that a backup exists before edit/control actions.
- Prefer common project-intelligence tools before GUI automation.
- Use Windows GUI discovery before any Windows GUI control.
- Use Linux/headless workflows only in an explicitly selected Linux/WSL/VM/container environment.

## Before KiCad File Access
- Confirm files are under the active project path.
- Confirm whether the task is design, review, verification, tooling, documentation, or release preparation.
- Identify files likely to change.
- Prepare the verification plan.
- Prepare the rollback plan.
- Create or confirm a backup in `99_BACKUPS/pre_codex_edits/` before edits.

## Before PCB Update Or Layout Work
- Read `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`.
- Read `09_ACCURACY_ENGINE/checklists/FULL_PIPELINE_GATE_CHECKLIST.md`.
- Select the matching reusable prompt from `.prompts/kicad_pipeline/`.
- Read `09_ACCURACY_ENGINE/workflows/SCHEMATIC_TO_PCB_GATE_WORKFLOW.md`.
- Read `09_ACCURACY_ENGINE/checklists/SCHEMATIC_READY_FOR_PCB_CHECKLIST.md`.
- Read `09_ACCURACY_ENGINE/checklists/PCB_UPDATE_FROM_SCHEMATIC_CHECKLIST.md`.
- Read `09_ACCURACY_ENGINE/verification_rules/SCHEMATIC_TO_PCB_BLOCKERS.md`.
- Read `09_ACCURACY_ENGINE/verification_rules/NEEDS_REVIEW_BLOCKER_RULES.md`.
- Read `09_ACCURACY_ENGINE/verification_rules/SCHEMATIC_ANNOTATION_RULES.md`.
- Read `09_ACCURACY_ENGINE/verification_rules/SCHEMATIC_COMPLETENESS_RULES.md`.
- Confirm current reports exist for `03_TOOLS/scripts/kicad_schematic_checks/check_schematic_annotation.py`, `check_schematic_completeness.py`, `check_bom_lock_alignment.py`, and `check_needs_review_markers.py`.
- Read the active project's `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`.
- Confirm the gate result is exactly `PASS`.
- If the gate is missing, stale, blocked, failed, not run, or evidence is missing, do not update PCB from schematic, place parts, route traces, create zones, or generate PCB manufacturing outputs.
- Do not skip a full-pipeline gate unless the user explicitly approves the exception and the exception is logged with affected gate, reason, risk, evidence, and `HUMAN_REVIEW_REQUIRED`.

## Session Close
- Record meaningful work in `02_HISTORY/sessions/` or project `history/sessions/`.
- Put durable global lessons in `01_MEMORY/`.
- Put durable project decisions in project `memory/`.
- Put commands and command results in `02_HISTORY/command_logs/` or project `history/command_logs/`.
- Record failed attempts in the proper failed-attempt folder.
- Record user corrections in the proper user-corrections folder.
- Create an AI self-review.
- Create an AI response scorecard.
- Create a claim/evidence matrix for major engineering claims.
- Create uncertainty logs for anything not verified.
- Create hallucination-risk logs for guessed, inferred, or weakly sourced claims.
- Create quality-gate failure records when blocked or failed.
- Add unresolved problems to issue logs.
- Update repo, memory, history, AI-quality, and known-problem indexes.
- Rebuild `CURRENT_KNOWN_PROBLEMS.md`.
- Update `FOR CHAT GPT.MD` if repo structure or workflow changed.
- Do not record secrets or credentials.
