#!/usr/bin/env python3
"""Build the clean KiCad Engine installer repo-template payload."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from collections import Counter
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath


ROOT_FILES = [
    "AGENTS.md",
    "README.md",
    "README_GPT.md",
    "FOR CHAT GPT.MD",
    "START_HERE_FOR_USERS.md",
    "START_HERE_FOR_AI_AGENTS.md",
    "QUICKSTART_WINDOWS.md",
    "QUICKSTART_MACOS.md",
    "QUICKSTART_LINUX.md",
    "health_check.py",
    "health_check.ps1",
    "HEALTH_CHECK_REPORT_TEMPLATE.md",
    "LICENSE",
    "DISCLAIMER.md",
    "SECURITY.md",
]

ROOT_OPTIONAL_PUBLIC_FILES = [
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "CHANGELOG.md",
    "ROADMAP.md",
    "PUBLIC_RELEASE_CHECKLIST.md",
    "INSTALLER_USER_GUIDE.md",
    "USER_MANUAL.md",
    "FAQ.md",
    "TROUBLESHOOTING.md",
]

COPY_DIRS = [
    ".vscode",
    ".codex",
    ".prompts",
    "docs",
    "00_CODEX_START",
    "03_TOOLS",
    "06_DATASHEETS",
    "08_COMPONENT_DATABASE",
    "09_ACCURACY_ENGINE",
    "10_KNOWLEDGE_BASE",
    "11_LIBRARY_FACTORY",
    "12_REFERENCE_DESIGN_LIBRARY",
    "13_PART_INGESTION",
    "14_LAYOUT_AUTOMATION",
    "15_BENCHMARKS",
    "setup",
]

GENERATED_SCAFFOLD_DIRS = [
    ".claude",
    "01_MEMORY/projects",
    "02_HISTORY/sessions",
    "02_HISTORY/command_logs",
    "02_HISTORY/design_reviews",
    "02_HISTORY/erc_drc_reports",
    "02_HISTORY/fabrication_reviews",
    "02_HISTORY/project_history",
    "04_KICAD_PROJECTS/active",
    "04_KICAD_PROJECTS/archive",
    "04_KICAD_PROJECTS/templates",
    "05_OUTPUTS/health_checks",
    "05_OUTPUTS/setup_reports",
    "05_OUTPUTS/setup_indexes",
    "05_OUTPUTS/review_packages",
    "05_OUTPUTS/datasheet_research",
    "99_BACKUPS/pre_codex_edits",
    "08_COMPONENT_DATABASE/00_INDEX",
    "08_COMPONENT_DATABASE/01_MICROCONTROLLERS",
    "08_COMPONENT_DATABASE/02_POWER",
    "08_COMPONENT_DATABASE/03_COMMUNICATION",
    "08_COMPONENT_DATABASE/04_CONNECTORS",
    "08_COMPONENT_DATABASE/05_PROTECTION",
    "08_COMPONENT_DATABASE/06_SENSORS",
    "08_COMPONENT_DATABASE/07_ANALOG",
    "08_COMPONENT_DATABASE/08_DRIVERS",
    "08_COMPONENT_DATABASE/09_PASSIVES",
    "08_COMPONENT_DATABASE/10_RF_AND_ANTENNAS",
    "08_COMPONENT_DATABASE/11_DEV_BOARDS_AND_MODULES",
    "08_COMPONENT_DATABASE/12_KICAD_SYMBOL_FOOTPRINT_MATCHES",
    "08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS",
    "08_COMPONENT_DATABASE/14_PART_SELECTION_GUIDES",
    "08_COMPONENT_DATABASE/99_UNVERIFIED_INBOX",
]

SPECIFIC_EXCLUDED_DIRS = {
    "03_TOOLS/repos",
    "03_TOOLS/python_envs",
    "03_TOOLS/node_envs",
    "03_TOOLS/tool_logs",
    "03_TOOLS/common/repos",
    "03_TOOLS/windows/repos",
    "03_TOOLS/windows/logs",
    "03_TOOLS/linux/logs",
    "03_TOOLS/linux/repos",
    "03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES",
    "06_DATASHEETS/99_UNSORTED_INBOX/LEGACY_MIGRATION_20260502_161444",
}

SENSITIVE_GENERATED_DIRS = {
    "01_MEMORY",
    "02_HISTORY",
    "04_KICAD_PROJECTS/active",
    "04_KICAD_PROJECTS/archive",
    "05_OUTPUTS",
    "99_BACKUPS",
    "installer/payload",
}

EXCLUDED_DIR_NAMES = {
    ".git",
    ".github",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".venv",
    "venv",
    "node_modules",
    "dist",
    "build",
}

EXCLUDED_SUFFIXES = {
    ".pdf",
    ".zip",
    ".7z",
    ".rar",
    ".exe",
    ".dll",
    ".pyd",
    ".so",
    ".dylib",
    ".pyc",
    ".pyo",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".bmp",
    ".ico",
    ".stl",
    ".step",
    ".stp",
    ".wrl",
    ".gbr",
    ".drl",
    ".xln",
    ".kicad_pcb",
    ".kicad_sch",
    ".kicad_pro",
    ".kicad_prl",
    ".kicad_sym",
    ".kicad_mod",
    ".kicad_wks",
    ".wbk",
}

EXCLUDED_FILE_NAMES = {
    ".env",
    ".env.local",
    ".env.production",
    "config.toml",  # .codex/config.toml is local-machine state; generated example replaces it.
    "payload.manifest.json",
    "PAYLOAD_BUILD_REPORT.md",
}

TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".py",
    ".ps1",
    ".sh",
    ".json",
    ".toml",
    ".yaml",
    ".yml",
    ".csv",
    ".ini",
    ".cfg",
    ".gitignore",
}

BLOCKING_SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|access[_-]?token|secret|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"),
    re.compile(r"-----BEGIN (RSA |DSA |EC |OPENSSH |PGP )?PRIVATE KEY-----"),
    re.compile(r"(?i)sk-[A-Za-z0-9]{20,}"),
]

PRIVATE_CONTENT_MARKERS = [
    "COMMAND_LINK",
    "COMMAND LINK",
    "ESP32_CSI_WIFI_NODE",
    "CLEAN_KICAD_PASSING_SAMPLE",
    "SAMPLE_KICAD_TEST_PROJECT",
]


@dataclass
class ExcludedItem:
    path: str
    reason: str


class PayloadBuilder:
    def __init__(self, source_root: Path, payload_root: Path, max_file_size_mb: int, clean: bool) -> None:
        self.source_root = source_root.resolve()
        self.payload_root = payload_root.resolve()
        self.template_root = self.payload_root / "repo-template"
        self.max_file_size = max_file_size_mb * 1024 * 1024
        self.clean = clean
        self.excluded: list[ExcludedItem] = []
        self.generated_files: list[str] = []
        self.copied_files = 0

    def rel_posix(self, path: Path) -> str:
        return path.relative_to(self.source_root).as_posix()

    def target_rel_posix(self, path: Path) -> str:
        return path.relative_to(self.template_root).as_posix()

    def normalize_rel(self, rel: str | Path) -> str:
        return Path(rel).as_posix().strip("/")

    def exclude(self, rel: str, reason: str) -> None:
        self.excluded.append(ExcludedItem(self.normalize_rel(rel), reason))

    def assert_safe_clean_target(self) -> None:
        payload = self.payload_root.resolve()
        target = self.template_root.resolve()
        if target == payload:
            raise RuntimeError("Refusing to clean payload root directly.")
        if payload not in target.parents:
            raise RuntimeError(f"Refusing to clean target outside payload root: {target}")

    def prepare_target(self) -> None:
        self.payload_root.mkdir(parents=True, exist_ok=True)
        if self.clean and self.template_root.exists():
            self.assert_safe_clean_target()
            shutil.rmtree(self.template_root)
        self.template_root.mkdir(parents=True, exist_ok=True)

    def should_skip_dir(self, rel_dir: str, name: str) -> str | None:
        norm = self.normalize_rel(rel_dir)
        if name in EXCLUDED_DIR_NAMES:
            return f"excluded directory name {name}"
        if norm in SPECIFIC_EXCLUDED_DIRS:
            return "explicit excluded development/vendor/generated directory"
        if norm in SENSITIVE_GENERATED_DIRS:
            return "generated clean scaffold replaces source state"
        if name.startswith("LEGACY_MIGRATION"):
            return "legacy migrated local content excluded"
        return None

    def should_skip_file(self, rel_file: str, source_file: Path) -> str | None:
        norm = self.normalize_rel(rel_file)
        suffix = source_file.suffix.lower()
        if source_file.name in EXCLUDED_FILE_NAMES:
            return f"excluded file name {source_file.name}"
        if suffix in EXCLUDED_SUFFIXES:
            return f"excluded file type {suffix}"
        if (
            "NOT_FINAL" in source_file.name.upper()
            and not norm.startswith(".prompts/")
            and not norm.startswith("docs/")
        ):
            return "generated NOT_FINAL output excluded"
        if source_file.stat().st_size > self.max_file_size:
            return f"file exceeds max size {self.max_file_size} bytes"
        if any(part.lower().endswith("-backups") for part in source_file.parts):
            return "backup folder/file excluded"
        if "PRIVATE" in source_file.name.upper():
            return "private-marked file excluded"
        if self.is_text_file(source_file) and self.source_text_has_blocking_secret(source_file):
            return "blocking secret-like pattern"
        return None

    def is_text_file(self, path: Path) -> bool:
        return path.suffix.lower() in TEXT_SUFFIXES or path.name in {"AGENTS.md", "FOR CHAT GPT.MD"}

    def source_text_has_blocking_secret(self, path: Path) -> bool:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            return True
        return any(pattern.search(text) for pattern in BLOCKING_SECRET_PATTERNS)

    def sanitize_text(self, text: str) -> str:
        replacements = {
            str(self.source_root): "<KICAD_ENGINE_WORKSPACE>",
            str(self.source_root).replace("\\", "\\\\"): "<KICAD_ENGINE_WORKSPACE>",
            "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE": "<KICAD_ENGINE_WORKSPACE>",
            "C:\\Users\\LJ\\KICAD_ENGINE": "<KICAD_ENGINE_WORKSPACE>",
            "C:\\\\Users\\\\LJ\\\\GitHub\\\\KICAD_ENGINE": "<KICAD_ENGINE_WORKSPACE>",
            "C:\\\\Users\\\\LJ\\\\KICAD_ENGINE": "<KICAD_ENGINE_WORKSPACE>",
            "C:/Users/LJ/GitHub/KICAD_ENGINE": "<KICAD_ENGINE_WORKSPACE>",
            "C:/Users/LJ/KICAD_ENGINE": "<KICAD_ENGINE_WORKSPACE>",
            "C:\\Users\\LJ": "<USER_HOME>",
            "C:\\\\Users\\\\LJ": "<USER_HOME>",
            "C:/Users/LJ": "<USER_HOME>",
            "ESP32_CSI_WIFI_NODE": "EXAMPLE_PROJECT",
            "COMMAND_LINK_VERIFIED_REFERENCE": "REFERENCE_PROJECT",
            "COMMAND_LINK": "REFERENCE_PROJECT",
            "COMMAND LINK": "REFERENCE PROJECT",
            "CLEAN_KICAD_PASSING_SAMPLE": "CLEAN_SAMPLE_PROJECT",
            "SAMPLE_KICAD_TEST_PROJECT": "SAMPLE_TEST_PROJECT",
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        text = re.sub(r"\bLJ\b", "the user", text)
        text = text.replace("\u00e2\u20ac\u201d", "-")
        text = text.replace("\u2014", "-")
        return text

    def copy_file(self, source_file: Path, rel_file: str) -> None:
        target_file = self.template_root / rel_file
        target_file.parent.mkdir(parents=True, exist_ok=True)
        if self.is_text_file(source_file):
            text = source_file.read_text(encoding="utf-8", errors="replace")
            target_file.write_text(self.sanitize_text(text), encoding="utf-8")
        else:
            shutil.copy2(source_file, target_file)
        self.copied_files += 1

    def copy_allowed_file(self, rel_file: str, optional: bool = False) -> None:
        source_file = self.source_root / rel_file
        if not source_file.exists():
            if not optional:
                self.exclude(rel_file, "required source file missing")
            return
        reason = self.should_skip_file(rel_file, source_file)
        if reason:
            self.exclude(rel_file, reason)
            return
        self.copy_file(source_file, rel_file)

    def copy_tree(self, rel_dir: str) -> None:
        source_dir = self.source_root / rel_dir
        if not source_dir.exists():
            self.exclude(rel_dir, "source directory missing")
            return
        for item in source_dir.rglob("*"):
            rel = self.rel_posix(item)
            if item.is_dir():
                reason = self.should_skip_dir(rel, item.name)
                if reason:
                    self.exclude(rel, reason)
                continue
            if any(self.normalize_rel(parent) in SPECIFIC_EXCLUDED_DIRS for parent in self.parent_rels(item)):
                self.exclude(rel, "inside explicit excluded directory")
                continue
            if any(self.normalize_rel(parent) in SENSITIVE_GENERATED_DIRS for parent in self.parent_rels(item)):
                self.exclude(rel, "inside generated scaffold area")
                continue
            if any(part in EXCLUDED_DIR_NAMES for part in item.relative_to(self.source_root).parts[:-1]):
                self.exclude(rel, "inside excluded cache/build directory")
                continue
            if any(part.startswith("LEGACY_MIGRATION") for part in item.relative_to(self.source_root).parts):
                self.exclude(rel, "inside legacy migrated local content")
                continue
            reason = self.should_skip_file(rel, item)
            if reason:
                self.exclude(rel, reason)
                continue
            self.copy_file(item, rel)

    def parent_rels(self, item: Path) -> list[str]:
        rel = item.relative_to(self.source_root)
        parents = []
        current = Path()
        for part in rel.parts[:-1]:
            current = current / part
            parents.append(current.as_posix())
        return parents

    def write_generated(self, rel_file: str, text: str) -> None:
        target = self.template_root / rel_file
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(self.sanitize_text(text).rstrip() + "\n", encoding="utf-8")
        self.generated_files.append(Path(rel_file).as_posix())

    def create_scaffold_dirs(self) -> None:
        for rel_dir in GENERATED_SCAFFOLD_DIRS:
            (self.template_root / rel_dir).mkdir(parents=True, exist_ok=True)

        (self.template_root / "03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES").mkdir(parents=True, exist_ok=True)
        (self.template_root / "06_DATASHEETS/99_UNSORTED_INBOX").mkdir(parents=True, exist_ok=True)

    def generate_clean_state_files(self) -> None:
        self.write_generated(
            ".codex/README.md",
            """# Codex Workspace Folder

This folder is for workspace-local Codex prompts and optional local configuration.

Do not store API keys, account tokens, passwords, or private credentials here.

`config.example.toml` is a placeholder only. Copy it to `config.toml` only after the user chooses to configure local MCP tools and updates every placeholder path for their own machine.
""",
        )
        self.write_generated(
            ".codex/config.example.toml",
            """# Example Codex workspace-local configuration.
# This file is not active until copied to config.toml and edited by the user.
# Do not store secrets here.

[mcp_servers.kicad_mcp_pro_analysis]
command = "<path-to-kicad-mcp-pro-executable>"
args = ["serve", "--transport", "stdio", "--profile", "analysis"]
startup_timeout_sec = 20
tool_timeout_sec = 120

[mcp_servers.kicad_mcp_pro_analysis.env]
KICAD_MCP_PROFILE = "analysis"
KICAD_MCP_TRANSPORT = "stdio"
KICAD_MCP_WORKSPACE_ROOT = "<KICAD_ENGINE_WORKSPACE>"
KICAD_MCP_PROJECT_DIR = "<KICAD_ENGINE_WORKSPACE>/04_KICAD_PROJECTS/active"
KICAD_MCP_OUTPUT_DIR = "<KICAD_ENGINE_WORKSPACE>/05_OUTPUTS/kicad-mcp-pro-analysis"
KICAD_MCP_KICAD_CLI = "<path-to-kicad-cli>"
KICAD_MCP_ENABLE_EXPERIMENTAL_TOOLS = "false"
""",
        )
        self.write_generated(
            ".claude/README.md",
            """# Claude Workspace Folder

This folder is reserved for local Claude/VS Code workspace notes or configuration.

Do not store account credentials, API keys, tokens, or private project data here.

Use `.prompts/claude/` for reusable Claude task prompts.
""",
        )
        self.write_generated(
            "README_GPT.md",
            """# KiCad Engine AI Agent Context

This is the clean installer payload context for ChatGPT, Codex, Claude, and similar VS Code-based agents.

KiCad Engine is a local-first workspace for AI-assisted KiCad engineering. It uses the user's installed KiCad app and makes schematic, PCB, datasheet, BOM, footprint, symbol, ERC, DRC, Gerber, drill, STEP, and review workflows easier for AI agents to inspect and automate safely.

`09_ACCURACY_ENGINE` is the anti-hallucination ruleset. Before schematic creation, PCB creation, component adds, symbol selection, footprint selection, or release-package work, agents must read the relevant rules there. Every component needs a source, every symbol needs pinout evidence, every footprint needs exact package drawing evidence or `UNVERIFIED_FOOTPRINT`, and manufacturing-style outputs stay `NOT_FINAL`.

`10_KNOWLEDGE_BASE` is the reusable engineering knowledge layer for circuit blocks, design patterns, review checklists, common mistakes, manufacturing rules, and AI stop/verify guidance. It is a planning aid, not datasheet proof.

`11_LIBRARY_FACTORY` is the symbol/footprint/library standards layer. It guides project-local symbol and footprint creation, package-to-footprint mapping, connector footprint review, and basic read-only library QA scripts.

`12_REFERENCE_DESIGN_LIBRARY` is the link-first reference design layer. It stores public-source reference design records, license notes, verification levels, and category checklists. Reference designs are evidence, not automatic approval or permission to copy.

`13_PART_INGESTION` is the new-part ingestion layer. It generates placeholder datasheet summaries, component records, symbol checklists, and footprint checklists from user-provided metadata without scraping, downloading, or redistributing PDFs.

`14_LAYOUT_AUTOMATION` is the placement/routing reality-check layer. It documents what KiCad, `kicad-cli`, `pcbnew` Python, IPC, and FreeRouting can realistically support without claiming complete AI auto-layout or autorouting.

`15_BENCHMARKS` is the benchmark methodology layer. It defines benchmark tasks, scoring rubrics, and future result rules without bundling fake scores or unsupported comparison claims.

## Startup

Agents must read:

1. `AGENTS.md`
2. `00_CODEX_START/START_HERE.md`
3. `00_CODEX_START/SESSION_START_CHECKLIST.md`
4. `00_CODEX_START/WORKFLOW_RULES.md`
5. `00_CODEX_START/SAFETY_RULES.md`
6. `00_CODEX_START/CONTROL_PLANES.md`
7. `00_CODEX_START/CURRENT_PROJECT.md`

If `CURRENT_PROJECT.md` says `NONE`, agents may work on documentation, tooling, prompts, indexes, setup, datasheet metadata, and component metadata, but must not edit KiCad design files.

## Clean Payload State

- No active KiCad project is selected.
- No user projects are bundled.
- No generated manufacturing outputs are bundled.
- No downloaded datasheet PDFs are bundled.
- No third-party cloned repositories or virtual environments are bundled.
- Codex and Claude prompts are included under `.prompts/`.
- `.codex/config.example.toml` is an inactive placeholder.

## Verification Rule

AI review is not fabrication approval. Treat all manufacturing-style outputs as `NOT_FINAL` until ERC, DRC, BOM, footprint, netlist, datasheet, connector, polarity/orientation, mechanical, and visual review are complete.
""",
        )
        self.write_generated(
            "FOR CHAT GPT.MD",
            """# KiCad Engine Handoff

This is a fresh installer payload workspace. It intentionally does not include private project history, user-specific KiCad projects, downloaded PDFs, generated outputs, or third-party cloned repositories.

## Read First

1. `README_GPT.md`
2. `AGENTS.md`
3. `00_CODEX_START/START_HERE.md`
4. `00_CODEX_START/CONTROL_PLANES.md`
5. `00_CODEX_START/CURRENT_PROJECT.md`
6. `.prompts/README.md`

## Current State

- Active project: `NONE`.
- KiCad app: use the user's installed KiCad app; do not modify installed KiCad folders.
- AI tools: users must log in to their own Codex, Claude, or similar tools.
- Datasheets: link-only and metadata-first by default.
- Component records: verify before use; placeholders are not approved design data.
- Accuracy engine: read `09_ACCURACY_ENGINE` before schematic, PCB, symbol, footprint, or release-package work.
- Knowledge base: read `10_KNOWLEDGE_BASE` before proposing common circuit blocks, design patterns, connector interfaces, power trees, or manufacturing packages.
- Library factory: read `11_LIBRARY_FACTORY` before creating, selecting, verifying, or mapping KiCad symbols and footprints.
- Reference designs: read `12_REFERENCE_DESIGN_LIBRARY` before using examples as evidence or adapting a reference pattern.
- Part ingestion: read `13_PART_INGESTION` before adding new parts from datasheets, source URLs, or local documents.
- Layout automation: read `14_LAYOUT_AUTOMATION` before suggesting placement/routing automation, FreeRouting, or layout DRC comparison workflows.
- Benchmarks: read `15_BENCHMARKS` before running, scoring, or comparing benchmark tasks.
- Fabrication: no output is final without the full verification gate.
""",
        )
        self.write_generated(
            "00_CODEX_START/CURRENT_PROJECT.md",
            """Active project name: NONE
Active project path: NONE
Current task mode: FRESH_INSTALL_WORKSPACE
Current priority: Run health check, audit installed KiCad, and create or select a project before design edits.

# Current Project

This file controls whether AI agents may inspect or edit KiCad project files.

## Rules

- If active project name is `NONE`, do not edit KiCad project files.
- If active project path is `NONE`, do not edit KiCad project files.
- Before protected edits, confirm backups in `99_BACKUPS/pre_codex_edits/`.
- Before design changes, state files likely to change, verification plan, and rollback plan.

## Fresh Payload State

No active project is selected in the installer payload.
""",
        )
        self.write_generated(
            "00_CODEX_START/PROJECT_INDEX.md",
            """# Project Index

KiCad projects belong in `04_KICAD_PROJECTS/active`.

Project templates belong in `04_KICAD_PROJECTS/templates`.

## Current State

- Active project: `NONE`.
- No user project files are bundled in the installer payload.
- `04_KICAD_PROJECTS/active` is intentionally empty.
- `04_KICAD_PROJECTS/archive` is intentionally empty.
- Standard templates are included under `04_KICAD_PROJECTS/templates`.

## Project Work Rule

Before editing any KiCad design file, update `00_CODEX_START/CURRENT_PROJECT.md`, confirm the active project path, create or confirm a backup, and define ERC/DRC verification steps.
""",
        )
        self.write_generated(
            "00_CODEX_START/TOOL_INDEX.md",
            """# Tool Index

This is the fresh installer payload tool index.

## Current State

- Third-party cloned tool repositories are not bundled.
- Python and Node virtual environments are not bundled.
- Users should run `health_check.py` and installed-KiCad audit scripts locally.
- Optional tools should be installed only after explicit user confirmation through setup scripts or official package managers.

## Included Tool Areas

- `03_TOOLS/scripts`: first-party read-only and review-oriented scripts.
- `03_TOOLS/kicad_app_intelligence`: installed-KiCad path and CLI guidance.
- `03_TOOLS/kicad_library_intelligence`: KiCad library inspection guidance and indexer scripts.
- `03_TOOLS/common`, `03_TOOLS/windows`, `03_TOOLS/linux`: platform strategy, docs, and safe starter scripts.
""",
        )
        self.write_generated(
            "00_CODEX_START/REPO_MAP.md",
            """# Repository Map

The installer payload does not bundle third-party repositories.

## Fresh Payload Policy

- `03_TOOLS/repos` is not included with cloned third-party sources.
- `03_TOOLS/windows/repos` is not included with cloned GUI helper sources.
- `03_TOOLS/python_envs` and `03_TOOLS/node_envs` are not included.
- Users may add external tools later only after reviewing license, setup, and safety requirements.

## Accuracy Engine

`09_ACCURACY_ENGINE` is included as first-party rules and workflows. Agents must read the relevant accuracy-engine files before schematic creation, PCB creation, symbol selection, footprint selection, pinout verification, or release-package work.

## Knowledge Base

`10_KNOWLEDGE_BASE` is included as first-party reusable engineering guidance. It provides circuit patterns, design patterns, checklists, common mistakes, manufacturing package rules, and AI-agent guidance. It does not replace datasheet, connector drawing, package drawing, ERC/DRC, or human review evidence.

## Library Factory

`11_LIBRARY_FACTORY` is included as first-party symbol and footprint standards. It defines source-backed symbol creation, footprint creation, package mapping, project-local library rules, and basic read-only validators. Its scripts do not replace human/source review.

## Reference Design Library

`12_REFERENCE_DESIGN_LIBRARY` is included as first-party reference design guidance. It keeps records link-first, tracks license and verification level, and prevents blind copying of vendor or open hardware examples.

## Part Ingestion

`13_PART_INGESTION` is included as first-party new-part ingestion guidance. It supports user-provided datasheet links and local paths, produces structured placeholder records, and requires uncertainty to stay explicit until source review is complete.

## Layout Automation

`14_LAYOUT_AUTOMATION` is included as first-party placement/routing planning guidance. It supports realistic local-first layout assistance, not untested claims of complete AI autorouting.

## Benchmarks

`15_BENCHMARKS` is included as first-party benchmark methodology. It supports honest progress measurement with task definitions and scoring rubrics, not fake results or unsupported public comparison claims.
""",
        )
        self.generate_memory_files()
        self.generate_history_files()
        self.generate_project_output_files()

    def generate_memory_files(self) -> None:
        self.write_generated(
            "01_MEMORY/GLOBAL_MEMORY.md",
            """# Global Memory

Durable workspace-wide rules for AI-assisted KiCad engineering.

- Use the user's installed KiCad app.
- Do not modify installed KiCad folders.
- Do not store secrets.
- Do not edit KiCad project files unless the active project is selected and backed up.
- Treat AI review as assistance, not fabrication approval.
""",
        )
        self.write_generated(
            "01_MEMORY/DESIGN_RULES_MEMORY.md",
            """# Design Rules Memory

Record durable cross-project design rules here only after they are verified.

Fresh payload defaults are `TBD`; do not invent trace, clearance, voltage, current, thermal, connector, or fab rules.
""",
        )
        self.write_generated(
            "01_MEMORY/COMPONENT_PREFERENCES.md",
            """# Component Preferences

Record preferred parts only after datasheet, footprint, sourcing, lifecycle, and project-fit checks are complete.

Fresh payload state: no preferred parts are approved.
""",
        )
        self.write_generated(
            "01_MEMORY/FAB_HOUSE_PREFERENCES.md",
            """# Fabrication House Preferences

Record board-house constraints only after checking the selected fab's current capabilities.

Fresh payload state: no board house is selected.
""",
        )
        self.write_generated(
            "01_MEMORY/CODING_AND_SCRIPTING_RULES.md",
            """# Coding And Scripting Rules

- Prefer read-only checks before edits.
- Scripts must fail safely when tools are missing.
- Do not silently install tools.
- Do not store secrets in scripts, reports, memory, or history.
""",
        )
        self.write_generated(
            "01_MEMORY/projects/README.md",
            """# Project Memory

Create `PROJECT_NAME/PROJECT_MEMORY.md` after a real project is selected.

Do not store credentials or private tokens here.
""",
        )

    def generate_history_files(self) -> None:
        self.write_generated(
            "02_HISTORY/README.md",
            """# History

This folder starts empty in the installer payload.

Use it for session logs, command logs, design reviews, ERC/DRC reports, fabrication reviews, and project-specific history created on the user's machine.
""",
        )
        for rel_dir in [
            "02_HISTORY/sessions",
            "02_HISTORY/command_logs",
            "02_HISTORY/design_reviews",
            "02_HISTORY/erc_drc_reports",
            "02_HISTORY/fabrication_reviews",
            "02_HISTORY/project_history",
        ]:
            self.write_generated(
                f"{rel_dir}/README.md",
                f"""# {Path(rel_dir).name}

Fresh installer payload scaffold. Add user-local records here as work is performed.
""",
            )

    def generate_project_output_files(self) -> None:
        self.write_generated(
            "04_KICAD_PROJECTS/README.md",
            """# KiCad Projects

Use `active/` for user projects and `templates/` for project templates.

The installer payload does not include private user projects.
""",
        )
        self.write_generated("04_KICAD_PROJECTS/active/README.md", "# Active Projects\n\nCreate or copy user projects here after selection.\n")
        self.write_generated("04_KICAD_PROJECTS/archive/README.md", "# Archived Projects\n\nArchived user projects are not bundled in the installer payload.\n")
        self.write_generated(
            "05_OUTPUTS/README.md",
            """# Outputs

Generated reports and review outputs belong here.

No generated outputs are bundled in the installer payload. Manufacturing-style outputs must stay `NOT_FINAL` until the full verification gate passes.
""",
        )
        self.write_generated(
            "06_DATASHEETS/99_UNSORTED_INBOX/README.md",
            """# Unsorted Datasheet Inbox

Place user-local datasheets here only after checking redistribution and project policy.

Public releases should prefer link-only metadata unless document redistribution is confirmed.
""",
        )
        self.write_generated(
            "03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/README.md",
            """# Generated Indexes

Generated KiCad library indexes are not bundled in the installer payload.

Run the index scripts locally against the user's installed KiCad app.
""",
        )
        self.write_generated(
            "99_BACKUPS/README.md",
            """# Backups

Pre-edit backups are generated locally before protected project edits.

No backups are bundled in the installer payload.
""",
        )

    def preserve_empty_scaffold_dirs(self) -> None:
        """Put a small file in generated empty dirs so packaged payloads keep them."""
        scaffold_dirs = sorted({
            *GENERATED_SCAFFOLD_DIRS,
            "03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES",
            "06_DATASHEETS/99_UNSORTED_INBOX",
        })
        for rel_dir in scaffold_dirs:
            directory = self.template_root / rel_dir
            if not directory.exists() or any(directory.iterdir()):
                continue
            title = Path(rel_dir).name.replace("_", " ").title()
            self.write_generated(
                f"{rel_dir}/README.md",
                f"""# {title}

Fresh installer payload scaffold. Add user-local files here when needed.
""",
            )

    def build(self) -> None:
        self.prepare_target()
        for rel_file in ROOT_FILES:
            self.copy_allowed_file(rel_file)
        for rel_file in ROOT_OPTIONAL_PUBLIC_FILES:
            self.copy_allowed_file(rel_file, optional=True)
        for rel_dir in COPY_DIRS:
            self.copy_tree(rel_dir)
        self.create_scaffold_dirs()
        self.copy_project_templates()
        self.generate_clean_state_files()
        self.preserve_empty_scaffold_dirs()
        self.scan_payload_for_blockers()
        self.write_manifest_and_report()

    def copy_project_templates(self) -> None:
        rel_dir = "04_KICAD_PROJECTS/templates"
        source_dir = self.source_root / rel_dir
        if not source_dir.exists():
            self.exclude(rel_dir, "project templates missing")
            return
        for item in source_dir.rglob("*"):
            rel = self.rel_posix(item)
            if item.is_dir():
                continue
            reason = self.should_skip_file(rel, item)
            if reason:
                self.exclude(rel, reason)
                continue
            self.copy_file(item, rel)

    def scan_payload_for_blockers(self) -> None:
        blockers: list[str] = []
        for file in self.template_root.rglob("*"):
            if not file.is_file() or not self.is_text_file(file):
                continue
            text = file.read_text(encoding="utf-8", errors="replace")
            rel = self.target_rel_posix(file)
            if any(pattern.search(text) for pattern in BLOCKING_SECRET_PATTERNS):
                blockers.append(f"{rel}: blocking secret-like pattern")
            for marker in PRIVATE_CONTENT_MARKERS:
                if marker in text:
                    blockers.append(f"{rel}: private marker {marker}")
            if "C:\\Users\\LJ" in text or "C:/Users/LJ" in text:
                blockers.append(f"{rel}: developer-specific path")
        if blockers:
            raise RuntimeError("Payload blocker(s) found:\n" + "\n".join(blockers[:50]))

    def manifest_files(self) -> list[dict[str, object]]:
        files: list[dict[str, object]] = []
        for path in sorted(self.template_root.rglob("*")):
            if not path.is_file():
                continue
            rel = self.target_rel_posix(path)
            data = path.read_bytes()
            files.append(
                {
                    "path": rel,
                    "size_bytes": len(data),
                    "sha256": hashlib.sha256(data).hexdigest(),
                }
            )
        return files

    def write_manifest_and_report(self) -> None:
        files = self.manifest_files()
        total_bytes = sum(int(item["size_bytes"]) for item in files)
        excluded_counter = Counter(item.reason for item in self.excluded)
        manifest = {
            "schema_version": "1.0",
            "payload_name": "KICAD_ENGINE repo-template",
            "built_at_utc": datetime.now(timezone.utc).isoformat(),
            "source_root": "<local build workspace omitted>",
            "template_root": "installer/payload/repo-template",
            "file_count": len(files),
            "total_bytes": total_bytes,
            "max_file_size_bytes": self.max_file_size,
            "generated_files": sorted(self.generated_files),
            "excluded_summary": dict(sorted(excluded_counter.items())),
            "excluded_count": len(self.excluded),
            "files": files,
        }
        manifest_path = self.payload_root / "payload.manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        manifests_dir = self.payload_root / "manifests"
        manifests_dir.mkdir(parents=True, exist_ok=True)
        (manifests_dir / "payload.manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

        report_path = self.payload_root / "PAYLOAD_BUILD_REPORT.md"
        report_path.write_text(self.render_report(files, total_bytes, excluded_counter), encoding="utf-8")

    def render_report(self, files: list[dict[str, object]], total_bytes: int, excluded_counter: Counter[str]) -> str:
        lines = [
            "# Payload Build Report",
            "",
            f"Build time UTC: `{datetime.now(timezone.utc).isoformat()}`",
            "",
            "## Summary",
            "",
            f"- Template root: `installer/payload/repo-template`",
            f"- Files included: `{len(files)}`",
            f"- Total bytes: `{total_bytes}`",
            f"- Generated clean files: `{len(self.generated_files)}`",
            f"- Excluded items recorded: `{len(self.excluded)}`",
            f"- Maximum file size: `{self.max_file_size}` bytes",
            "",
            "## Exclusion Summary",
            "",
            "| Reason | Count |",
            "|---|---:|",
        ]
        for reason, count in sorted(excluded_counter.items()):
            lines.append(f"| {reason} | {count} |")
        if not excluded_counter:
            lines.append("| none | 0 |")
        lines.extend(
            [
                "",
                "## Generated Clean State",
                "",
                "The builder generated clean state for `.codex`, `.claude`, `README_GPT.md`, `FOR CHAT GPT.MD`, `00_CODEX_START/CURRENT_PROJECT.md`, memory, history, empty project areas, empty outputs, backup scaffold, and generated index placeholders.",
                "",
                "## Release Notes",
                "",
                "- No third-party cloned repositories are bundled.",
                "- No Python or Node environments are bundled.",
                "- No PDFs are bundled.",
                "- No active or archived user KiCad projects are bundled.",
                "- No generated output folders are bundled.",
                "- `payload.manifest.json` contains relative paths and hashes only.",
                "",
            ]
        )
        return "\n".join(lines) + "\n"


def default_source_root() -> Path:
    return Path(__file__).resolve().parents[2]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", default=str(default_source_root()))
    parser.add_argument("--payload-root", default=str(Path(__file__).resolve().parent))
    parser.add_argument("--max-file-size-mb", type=int, default=5)
    parser.add_argument("--no-clean", action="store_true")
    args = parser.parse_args()

    builder = PayloadBuilder(
        source_root=Path(args.source_root),
        payload_root=Path(args.payload_root),
        max_file_size_mb=args.max_file_size_mb,
        clean=not args.no_clean,
    )
    builder.build()
    print(f"Payload template built: {builder.template_root}")
    print(f"Manifest: {builder.payload_root / 'payload.manifest.json'}")
    print(f"Report: {builder.payload_root / 'PAYLOAD_BUILD_REPORT.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
