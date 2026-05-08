#!/usr/bin/env python3
"""Build safe local metadata indexes for KiCad Engine."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[2]


def relative(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return str(path)


def write_component_index(repo_root: Path, output_dir: Path) -> tuple[Path, Path, int]:
    component_root = repo_root / "08_COMPONENT_DATABASE"
    files = sorted(
        [
            path
            for pattern in ("*.md", "*.json")
            for path in component_root.rglob(pattern)
            if path.is_file()
        ],
        key=lambda path: relative(path, repo_root).lower(),
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    markdown = output_dir / "component_database_file_index.md"
    json_path = output_dir / "component_database_file_index.json"
    lines = [
        "# Component Database File Index",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "This generated index is for navigation only. It does not prove component, datasheet, pinout, package, lifecycle, or footprint verification.",
        "",
        "| File | Size | Last Modified |",
        "| --- | ---: | --- |",
    ]
    records = []
    for path in files:
        rel = relative(path, repo_root)
        stat = path.stat()
        records.append(
            {
                "relative_path": rel,
                "size_bytes": stat.st_size,
                "last_modified": datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds"),
            }
        )
        lines.append(f"| `{rel}` | {stat.st_size} | {records[-1]['last_modified']} |")
    markdown.write_text("\n".join(lines) + "\n", encoding="utf-8")
    json_path.write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
    return markdown, json_path, len(records)


def write_prompt_index(repo_root: Path, output_dir: Path) -> tuple[Path, Path, int]:
    prompt_root = repo_root / ".prompts"
    files = sorted(prompt_root.rglob("*.md"), key=lambda path: relative(path, repo_root).lower())
    markdown = output_dir / "prompt_pack_file_index.md"
    json_path = output_dir / "prompt_pack_file_index.json"
    records = []
    lines = [
        "# Prompt Pack File Index",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "| File | Size |",
        "| --- | ---: |",
    ]
    for path in files:
        rel = relative(path, repo_root)
        size = path.stat().st_size
        records.append({"relative_path": rel, "size_bytes": size})
        lines.append(f"| `{rel}` | {size} |")
    markdown.write_text("\n".join(lines) + "\n", encoding="utf-8")
    json_path.write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
    return markdown, json_path, len(records)


def build_datasheet_index(repo_root: Path, output_dir: Path) -> tuple[int, str]:
    script = repo_root / "03_TOOLS" / "scripts" / "datasheets" / "build_datasheet_index.py"
    if not script.exists():
        return 2, f"Missing datasheet index script: {script}"
    output = output_dir / "datasheet_source_index.md"
    command = [
        sys.executable,
        str(script),
        str(repo_root / "06_DATASHEETS" / "00_INDEX" / "source_lists"),
        "--output",
        str(output),
    ]
    completed = subprocess.run(command, cwd=repo_root, text=True, capture_output=True, check=False)
    message = (completed.stdout or completed.stderr).strip()
    return completed.returncode, message


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=str(repo_root_from_script()))
    parser.add_argument("--output-dir", default="05_OUTPUTS/setup_indexes")
    parser.add_argument("--skip-datasheets", action="store_true")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    output_dir = repo_root / args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    component_md, component_json, component_count = write_component_index(repo_root, output_dir)
    prompt_md, prompt_json, prompt_count = write_prompt_index(repo_root, output_dir)

    failures = 0
    datasheet_message = "Skipped."
    if not args.skip_datasheets:
        code, datasheet_message = build_datasheet_index(repo_root, output_dir)
        if code != 0:
            failures += 1

    summary = output_dir / "setup_index_summary.md"
    lines = [
        "# Setup Index Summary",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"Repo root: `{repo_root}`",
        "",
        "No downloads were performed. No KiCad project files were modified.",
        "",
        "## Outputs",
        "",
        f"- Component database markdown index: `{component_md}`",
        f"- Component database JSON index: `{component_json}`",
        f"- Component database files indexed: {component_count}",
        f"- Prompt pack markdown index: `{prompt_md}`",
        f"- Prompt pack JSON index: `{prompt_json}`",
        f"- Prompt pack files indexed: {prompt_count}",
        f"- Datasheet index result: {datasheet_message}",
    ]
    summary.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {summary}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
