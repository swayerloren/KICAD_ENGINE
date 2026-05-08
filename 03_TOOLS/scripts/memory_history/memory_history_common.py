#!/usr/bin/env python3
"""Shared helpers for KiCad Engine memory/history scripts.

These helpers only write markdown or JSON records into memory/history folders.
They do not edit KiCad design files.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Iterable


RECORD_DIRS = {
    "session": ("02_HISTORY/sessions", "history/sessions"),
    "failed_attempt": ("02_HISTORY/failed_attempts", "history/failed_attempts"),
    "user_correction": ("02_HISTORY/user_corrections", "history/user_corrections"),
    "issue_log": ("02_HISTORY/issue_logs", "history/issue_logs"),
    "lesson_learned": ("02_HISTORY/lessons_learned", "history/design_decisions"),
    "workflow_run": ("02_HISTORY/workflow_runs", "history/workflow_runs"),
    "verification_run": ("02_HISTORY/workflow_runs", "history/verification_runs"),
}

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |)PRIVATE KEY-----", re.I),
    re.compile(r"(?i)\b(password|api[_-]?key|access[_-]?token|secret)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{12,}"),
    re.compile(r"\bsk-[A-Za-z0-9_\-]{20,}\b"),
]


def now_stamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def slugify(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", value.strip()).strip("_")
    return cleaned[:80] or "record"


def repo_root_from_args(value: str | None) -> Path:
    return Path(value or ".").resolve()


def repo_relative(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve())).replace("\\", "/")
    except ValueError:
        return str(path.resolve()).replace("\\", "/")


def ensure_no_secret_text(text: str) -> None:
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            raise SystemExit("Refusing to write record because the content looks like it may contain a secret.")


def ensure_safe_output_path(path: Path) -> None:
    lower_name = path.name.lower()
    if lower_name.endswith((".kicad_sch", ".kicad_pcb", ".kicad_pro", ".kicad_sym", ".kicad_mod")):
        raise SystemExit(f"Refusing to write KiCad design/library file: {path}")
    if path.suffix.lower() not in {".md", ".json"}:
        raise SystemExit(f"Refusing to write unsupported output type: {path}")


def ensure_project_root(project_path: Path) -> None:
    if project_path.name.lower() == "kicad":
        raise SystemExit("Project path appears to be the KiCad source subfolder. Use the project root instead.")
    if any(part.lower().endswith((".kicad_sch", ".kicad_pcb", ".kicad_pro")) for part in project_path.parts):
        raise SystemExit("Project path must be a folder, not a KiCad design file.")


def common_record_parser(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--repo-root", default=".", help="KiCad Engine repo root.")
    parser.add_argument("--scope", choices=["global", "project"], default="global")
    parser.add_argument("--project-name", default="")
    parser.add_argument("--project-path", default="")
    parser.add_argument("--title", required=True)
    parser.add_argument("--summary", default="")
    parser.add_argument("--details", default="")
    parser.add_argument("--status", default="UNVERIFIED")
    parser.add_argument("--source", default="")
    return parser


def record_target(repo_root: Path, scope: str, project_path: str, kind: str) -> Path:
    if kind not in RECORD_DIRS:
        raise SystemExit(f"Unknown record kind: {kind}")
    global_dir, project_dir = RECORD_DIRS[kind]
    if scope == "project":
        if not project_path:
            raise SystemExit("--project-path is required for project scope.")
        project_root = Path(project_path).resolve()
        ensure_project_root(project_root)
        return project_root / project_dir
    return repo_root / global_dir


def build_record_markdown(kind: str, args: argparse.Namespace) -> str:
    title = args.title.strip()
    summary = args.summary.strip() or "Unknown - requires source verification."
    details = args.details.strip() or "None recorded."
    source = args.source.strip() or "Unknown - requires source verification."
    status = args.status.strip() or "UNVERIFIED"
    scope = args.scope
    project_name = args.project_name.strip() or "N/A"
    text = f"""# {title}

Record kind: `{kind}`
Status: `{status}`
Created: `{datetime.now().isoformat(timespec="seconds")}`
Scope: `{scope}`
Project: `{project_name}`

## Summary

{summary}

## Details

{details}

## Source Or Evidence

{source}

## Verification Status

Mark this record `USER_CONFIRMED` or `VERIFIED_WORKFLOW` only after human confirmation or repeatable evidence exists.

## Secret Check

No secrets should be stored in this record.
"""
    ensure_no_secret_text(text)
    return text


def write_record(kind: str, args: argparse.Namespace) -> Path:
    repo_root = repo_root_from_args(args.repo_root)
    target_dir = record_target(repo_root, args.scope, args.project_path, kind)
    target_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{now_stamp()}_{slugify(args.title)}.md"
    output = target_dir / filename
    ensure_safe_output_path(output)
    content = build_record_markdown(kind, args)
    output.write_text(content, encoding="utf-8")
    return output


def scan_markdown(paths: Iterable[Path], *, repo_root: Path | None = None) -> list[dict]:
    records: list[dict] = []
    resolved_root = repo_root.resolve() if repo_root is not None else None
    for root in paths:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.md")):
            try:
                first_line = path.read_text(encoding="utf-8", errors="replace").splitlines()[0:1]
            except OSError:
                continue
            records.append({
                "path": repo_relative(path, resolved_root) if resolved_root is not None else str(path.resolve()).replace("\\", "/"),
                "name": path.name,
                "title": first_line[0].lstrip("# ").strip() if first_line else path.stem,
                "size_bytes": path.stat().st_size,
                "modified": datetime.fromtimestamp(path.stat().st_mtime).isoformat(timespec="seconds"),
            })
    return records


def write_json(path: Path, data: object) -> None:
    ensure_safe_output_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
