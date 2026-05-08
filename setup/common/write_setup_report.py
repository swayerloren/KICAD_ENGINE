#!/usr/bin/env python3
"""Write a setup report for KiCad Engine without installing anything."""

from __future__ import annotations

import argparse
import json
import platform
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[2]


def command_version(command: list[str]) -> dict[str, str]:
    exe = shutil.which(command[0])
    if not exe:
        return {"available": "false", "path": "", "version": ""}
    try:
        completed = subprocess.run(command, text=True, capture_output=True, timeout=20, check=False)
        output = (completed.stdout or completed.stderr).strip().splitlines()
        return {"available": "true", "path": exe, "version": output[0] if output else ""}
    except Exception as exc:  # noqa: BLE001
        return {"available": "true", "path": exe, "version": f"ERROR: {exc}"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=str(repo_root_from_script()))
    parser.add_argument("--output-dir", default="05_OUTPUTS/setup_reports")
    parser.add_argument("--include-health-check", action="store_true")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    output_dir = repo_root / args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    markdown = output_dir / f"KICAD_ENGINE_SETUP_REPORT_{stamp}.md"
    json_path = output_dir / f"KICAD_ENGINE_SETUP_REPORT_{stamp}.json"

    tools = {
        "git": command_version(["git", "--version"]),
        "python": command_version([sys.executable, "--version"]),
        "node": command_version(["node", "--version"]),
        "code": command_version(["code", "--version"]),
        "kicad-cli": command_version(["kicad-cli", "version"]),
    }
    key_paths = [
        "AGENTS.md",
        "START_HERE_FOR_USERS.md",
        "START_HERE_FOR_AI_AGENTS.md",
        ".vscode/tasks.json",
        ".prompts/README.md",
        "06_DATASHEETS/00_INDEX",
        "08_COMPONENT_DATABASE/00_INDEX",
        "03_TOOLS/scripts/kicad_engine_health_check.ps1",
        "health_check.py",
        "health_check.ps1",
    ]
    path_rows = [{"path": path, "exists": (repo_root / path).exists()} for path in key_paths]

    health_result = "Not run."
    if args.include_health_check:
        health_script = repo_root / "health_check.py"
        if health_script.exists():
            completed = subprocess.run(
                [sys.executable, str(health_script), "--repo-root", str(repo_root)],
                text=True,
                capture_output=True,
                check=False,
            )
            health_result = f"Exit code {completed.returncode}. {(completed.stdout or completed.stderr).strip()}"
        else:
            health_result = "Skipped because health_check.py is missing."

    data = {
        "generated": datetime.now().isoformat(timespec="seconds"),
        "repo_root": str(repo_root),
        "platform": platform.platform(),
        "python_executable": sys.executable,
        "tools": tools,
        "paths": path_rows,
        "health_check": health_result,
        "safety": {
            "installs_tools": False,
            "stores_secrets": False,
            "modifies_kicad_projects": False,
            "assumes_ai_authentication": False,
        },
    }

    lines = [
        "# KiCad Engine Setup Report",
        "",
        f"Generated: {data['generated']}",
        f"Repo root: `{repo_root}`",
        f"Platform: `{data['platform']}`",
        "",
        "This report does not install tools, store secrets, configure AI authentication, or modify KiCad project files.",
        "",
        "## Tool Check",
        "",
        "| Tool | Available | Path | Version |",
        "| --- | --- | --- | --- |",
    ]
    for name, info in tools.items():
        lines.append(f"| {name} | {info['available']} | `{info['path']}` | `{info['version']}` |")
    lines += ["", "## Key Paths", "", "| Path | Exists |", "| --- | --- |"]
    for row in path_rows:
        lines.append(f"| `{row['path']}` | {row['exists']} |")
    lines += [
        "",
        "## AI Tool Authentication",
        "",
        "- Users must install and log in to Codex, Claude, or another AI coding agent themselves.",
        "- This repo must not store API keys, passwords, tokens, or license keys.",
        "",
        "## Health Check",
        "",
        health_result,
        "",
        "## Safety",
        "",
        "- Setup scripts must ask before installing anything.",
        "- Fabrication-style outputs must remain `NOT_FINAL` until the full verification gate passes.",
    ]
    markdown.write_text("\n".join(lines) + "\n", encoding="utf-8")
    json_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {markdown}")
    print(f"Wrote {json_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
