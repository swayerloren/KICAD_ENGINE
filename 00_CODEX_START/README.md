# 00_CODEX_START

Status: `MANDATORY_AGENT_CONTROL_PLANE`

This folder is the startup and closeout control plane for KiCad Engine. It tells Codex, Claude, and similar VS Code-based agents what must be read before work, where information belongs, which workflows are allowed, and when engineering work is blocked.

## Purpose

Use this folder to prevent agents from treating the repo as a generic documentation tree. KiCad Engine has strict gates for source evidence, KiCad file edits, schematic-to-PCB movement, footprint verification, supplier research, and manufacturing output labels. The files here are the first layer of those gates.

## Required Startup Path

Every meaningful session must start with:

1. `AGENTS.md`
2. `00_CODEX_START/START_HERE.md`
3. `00_CODEX_START/SESSION_START_CHECKLIST.md`
4. `00_CODEX_START/STRUCTURE_STANDARD.md`
5. `00_CODEX_START/FOLDER_ROUTING_RULES.md`
6. `00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md`
7. `00_CODEX_START/MEMORY_INDEX.md`
8. `00_CODEX_START/HISTORY_INDEX.md`
9. Active project memory/history when a project is involved

If any required file is missing or contradicts the user request, stop and record the blocker before editing project files.

## What Belongs Here

- Startup and session closeout checklists.
- Repo structure standards and folder-routing rules.
- Current project, memory, history, tool, and workflow indexes.
- KiCad automation safety gates.
- AI quality, truthfulness, evidence, uncertainty, and hallucination-risk rules.
- Pipeline startup rules for schematic, PCB, routing, and fabrication workflows.

## What Does Not Belong Here

- KiCad design files such as `.kicad_sch`, `.kicad_pcb`, `.kicad_pro`, symbols, footprints, or manufacturing outputs.
- Command transcripts, screenshots, and verification artifacts. Put those in `02_HISTORY/`, project `history/`, or `05_OUTPUTS/`.
- Datasheet PDFs or vendor documents. Put link-only/source records under `06_DATASHEETS/`.
- API keys, tokens, supplier credentials, cookies, private browser profiles, or secrets.

## How Agents Should Use This Folder

Before planning work, read the startup files and identify which subsystem owns the request. During work, use the matching workflow or checklist instead of inventing a process. At closeout, create the required history and AI-quality records before writing the final response.

When a user asks to edit a KiCad project, the agent must confirm the active project, create or confirm a backup, and read project memory/history before touching design files. When a user asks for research, the agent must keep source-link records separate from verified component facts. When a user asks for fabrication exports, outputs remain `NOT_FINAL` unless the full verification gate and human review pass.

## Required Status Labels

| Label | Meaning |
| --- | --- |
| `VERIFIED_BY_FILE` | Confirmed by local file inspection. |
| `VERIFIED_BY_COMMAND` | Confirmed by command output saved in history. |
| `VERIFIED_BY_DATASHEET` | Confirmed against a cited authoritative document. |
| `SOURCE_LINK_ONLY` | A source URL exists but the data has not been extracted and verified. |
| `UNVERIFIED` | Present as a placeholder, draft, or candidate only. |
| `TODO_SOURCE_REQUIRED` | A field or file needs authoritative source research. |
| `NEEDS_HUMAN_REVIEW` | AI cannot safely approve the item. |
| `BLOCKED_UNTIL_HUMAN_REVIEW` | Work cannot proceed without human decision or verification. |

## Safe Edit Rules

- Do not weaken startup, backup, KiCad edit, footprint, ERC/DRC, or human-review gates.
- Do not mark generated indexes or dry-run research outputs as verified.
- Do not remove uncertainty markers unless source evidence is added in the same change.
- Do not replace detailed workflow rules with generic agent advice.
- Keep path examples portable. If local paths are shown, mark them as examples and prefer repo-relative paths.

## Public Release Notes

This folder is public-facing agent control documentation. It must not claim KiCad Engine is complete, production-certified, or fabrication-approved. The current realistic posture is local-first, KiCad-native engineering assistance with strict verification and human review requirements.
