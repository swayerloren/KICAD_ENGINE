#!/usr/bin/env python3
"""Create the expected KiCad Engine folder skeleton without deleting anything."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


REQUIRED_FOLDERS = [
    ".vscode",
    ".prompts",
    ".prompts/codex",
    ".prompts/claude",
    ".prompts/shared",
    "00_CODEX_START",
    "01_MEMORY",
    "01_MEMORY/projects",
    "02_HISTORY",
    "02_HISTORY/sessions",
    "02_HISTORY/command_logs",
    "02_HISTORY/design_reviews",
    "02_HISTORY/erc_drc_reports",
    "02_HISTORY/fabrication_reviews",
    "02_HISTORY/project_history",
    "03_TOOLS",
    "03_TOOLS/scripts",
    "03_TOOLS/tool_logs",
    "03_TOOLS/common",
    "03_TOOLS/windows",
    "03_TOOLS/linux",
    "04_KICAD_PROJECTS",
    "04_KICAD_PROJECTS/active",
    "04_KICAD_PROJECTS/templates",
    "04_KICAD_PROJECTS/archive",
    "05_OUTPUTS",
    "05_OUTPUTS/setup_reports",
    "05_OUTPUTS/health_checks",
    "06_DATASHEETS",
    "06_DATASHEETS/00_INDEX",
    "08_COMPONENT_DATABASE",
    "08_COMPONENT_DATABASE/00_INDEX",
    "99_BACKUPS",
    "99_BACKUPS/pre_codex_edits",
    "setup",
    "setup/windows",
    "setup/macos",
    "setup/linux",
    "setup/common",
]


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[2]


def write_reports(repo_root: Path, rows: list[dict[str, str]], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    markdown = output_dir / f"CREATE_REPO_FOLDERS_{stamp}.md"
    json_path = output_dir / f"CREATE_REPO_FOLDERS_{stamp}.json"
    lines = [
        "# Create Repo Folders Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"Repo root: `{repo_root}`",
        "",
        "This script only creates missing directories. It does not delete files, install tools, or modify KiCad project files.",
        "",
        "| Status | Path |",
        "| --- | --- |",
    ]
    for row in rows:
        lines.append(f"| {row['status']} | `{row['path']}` |")
    markdown.write_text("\n".join(lines) + "\n", encoding="utf-8")
    json_path.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {markdown}")
    print(f"Wrote {json_path}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=str(repo_root_from_script()))
    parser.add_argument("--dry-run", action="store_true", help="Report missing folders without creating them.")
    parser.add_argument("--no-report", action="store_true", help="Do not write markdown/JSON reports.")
    parser.add_argument("--output-dir", default="05_OUTPUTS/setup_reports")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    rows: list[dict[str, str]] = []

    for rel in REQUIRED_FOLDERS:
        path = repo_root / rel
        if path.exists():
            status = "EXISTS"
        elif args.dry_run:
            status = "WOULD_CREATE"
        else:
            path.mkdir(parents=True, exist_ok=True)
            status = "CREATED"
        rows.append({"status": status, "path": rel})

    created = sum(1 for row in rows if row["status"] == "CREATED")
    missing = sum(1 for row in rows if row["status"] == "WOULD_CREATE")
    print(f"Repo root: {repo_root}")
    print(f"Created: {created}")
    print(f"Would create: {missing}")

    if not args.no_report:
        write_reports(repo_root, rows, repo_root / args.output_dir)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
