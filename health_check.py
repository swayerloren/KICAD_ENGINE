#!/usr/bin/env python3
"""Portable, read-only KiCad Engine health check."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
DISCOVERY_DIR = SCRIPT_DIR / "03_TOOLS" / "scripts" / "kicad_discovery"
TOOLS_DIR = SCRIPT_DIR / "03_TOOLS" / "scripts"
KICAD_API_DIR = SCRIPT_DIR / "03_TOOLS" / "scripts" / "kicad_api"
if str(DISCOVERY_DIR) not in sys.path:
    sys.path.insert(0, str(DISCOVERY_DIR))
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))
if str(KICAD_API_DIR) not in sys.path:
    sys.path.insert(0, str(KICAD_API_DIR))

from find_kicad import detect_kicad_environment  # type: ignore  # noqa: E402
from kicad_python_context import build_kicad_python_context  # type: ignore  # noqa: E402
from python_env_check import build_python_environment_report  # type: ignore  # noqa: E402


STATUSES = ("PASS", "WARN", "FAIL")

REQUIRED_DOCS = [
    "README.md",
    "START_HERE.md",
    "ONE_PROMPT_START.md",
    "DOWNLOAD_ZIP_START_HERE.md",
    "AGENT_STARTER_PROMPTS.md",
    "LOCAL_SETUP_REQUIREMENTS.md",
    "SELF_CONTAINED_REPO_CHECKLIST.md",
    "EXTERNAL_DEPENDENCIES.md",
    "PORTABILITY_AUDIT.md",
    "03_TOOLS/README.md",
    "03_TOOLS/TOOLS_INDEX.md",
    "00_CODEX_START/START_HERE.md",
    "docs/LOCAL_DEV_SETUP.md",
    "docs/CODESPACES_SETUP.md",
    "docs/GITHUB_SETUP.md",
    "docs/PYTHON_SETUP.md",
    "docs/HEALTH_CHECK.md",
    "docs/KICAD_PYTHON_CONTEXT.md",
]

KNOWN_LOCAL_ONLY_PLACEHOLDERS = [
    "03_TOOLS/node_envs/README.md",
    "03_TOOLS/python_envs/README.md",
    "03_TOOLS/repos/README.md",
    "03_TOOLS/tool_logs/README.md",
    "99_BACKUPS/README.md",
    "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work/README.md",
    "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_rehearsals/README.md",
]

KEY_SCRIPT_COMMANDS = [
    ("KiCad discovery", ["python", "03_TOOLS/scripts/kicad_discovery/find_kicad.py", "--help"]),
    ("KiCad install validator", ["python", "03_TOOLS/scripts/kicad_discovery/validate_kicad_install.py", "--help"]),
    ("KiCad Python context", ["python", "03_TOOLS/scripts/kicad_api/kicad_python_context.py", "--help"]),
    ("pcbnew import check", ["python", "03_TOOLS/scripts/kicad_api/pcbnew_import_check.py", "--help"]),
    ("Python environment check", ["python", "03_TOOLS/scripts/python_env_check.py", "--help"]),
    ("Task contract validator", ["python", "03_TOOLS/scripts/execution_contract/validate_task_contract.py", "--help"]),
    ("Routing geometry checker", ["python", "14_LAYOUT_AUTOMATION/scripts/routing_geometry_quality.py", "--help"]),
]

OPTIONAL_TOOLS = {
    "VS Code": ["code"],
    "Node.js": ["node"],
    "npm": ["npm"],
    "GitHub CLI": ["gh"],
    "Docker": ["docker"],
    "Java": ["java"],
}


@dataclass
class CheckResult:
    status: str
    category: str
    name: str
    detail: str


def add(results: list[CheckResult], status: str, category: str, name: str, detail: str) -> None:
    if status not in STATUSES:
        raise ValueError(status)
    results.append(CheckResult(status=status, category=category, name=name, detail=detail))


def repo_root_from_args(repo_root: str | None) -> Path:
    if repo_root:
        return Path(repo_root).resolve()
    return SCRIPT_DIR


def run_command(command: list[str], repo_root: Path) -> tuple[bool, str]:
    expanded = command[:]
    if expanded and expanded[0] == "python":
        expanded[0] = sys.executable
    try:
        completed = subprocess.run(
            expanded,
            cwd=repo_root,
            capture_output=True,
            text=True,
            timeout=20,
            check=False,
        )
    except Exception as exc:  # noqa: BLE001
        return False, str(exc)
    output = (completed.stdout or completed.stderr).strip().splitlines()
    detail = output[0] if output else "command completed without output"
    return completed.returncode == 0, detail


def first_path(commands: list[str]) -> str | None:
    for command in commands:
        found = shutil.which(command)
        if found:
            return found
    return None


def parse_active_project(repo_root: Path) -> str | None:
    path = repo_root / "00_CODEX_START" / "CURRENT_PROJECT.md"
    if not path.exists():
        return None
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        prefix = "Active project path:"
        if line.startswith(prefix):
            candidate = line.split(prefix, 1)[1].strip()
            return candidate if candidate and candidate != "NONE" else None
    return None


def summarize(results: list[CheckResult]) -> dict[str, int]:
    return {status: sum(1 for row in results if row.status == status) for status in STATUSES}


def user_actions(results: list[CheckResult]) -> list[str]:
    actions: list[str] = []
    for row in results:
        if row.name == "KiCad detected" and row.status != "PASS":
            actions.append("Install KiCad locally if you need live schematic, PCB, or pcbnew workflows.")
        elif row.name == "kicad-cli detected" and row.status != "PASS":
            actions.append("Add the KiCad bin folder to PATH or pass an explicit KiCad CLI path when a workflow requires it.")
        elif row.name == "pcbnew workflow availability" and row.status != "PASS":
            actions.append("Keep using docs or kicad-cli workflows until a KiCad-compatible pcbnew context is available.")
        elif row.name == "pcbnew direct import" and row.status == "WARN":
            actions.append("Board-aware scripts should re-enter through KiCad Python when normal Python cannot import pcbnew directly.")
        elif row.category == "Docs" and row.status == "FAIL":
            actions.append(f"Restore the required onboarding doc: {row.name}.")
        elif row.category == "Portability" and row.status == "FAIL":
            actions.append(f"Restore the local-only placeholder doc: {row.name}.")
        elif row.category == "Scripts" and row.status == "FAIL":
            actions.append(f"Fix the setup script entry point: {row.name}.")
    return list(dict.fromkeys(actions))


def write_reports(repo_root: Path, output_dir: Path, results: list[CheckResult], actions: list[str]) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    markdown_path = output_dir / f"KICAD_ENGINE_HEALTH_CHECK_{stamp}.md"
    json_path = output_dir / f"KICAD_ENGINE_HEALTH_CHECK_{stamp}.json"
    summary = summarize(results)
    generated = datetime.now().isoformat(timespec="seconds")
    lines = [
        "# KICAD_ENGINE Health Check",
        "",
        f"- Generated: `{generated}`",
        f"- Repo root: `{repo_root}`",
        "",
        "## Summary",
        "",
        f"- PASS: `{summary['PASS']}`",
        f"- WARN: `{summary['WARN']}`",
        f"- FAIL: `{summary['FAIL']}`",
        "",
        "## Results",
        "",
        "| Status | Category | Name | Detail |",
        "| --- | --- | --- | --- |",
    ]
    for row in results:
        lines.append(f"| {row.status} | {row.category} | {row.name} | {row.detail.replace('|', '\\|')} |")
    lines += [
        "",
        "## User Action Needed",
        "",
    ]
    if actions:
        lines.extend([f"- {action}" for action in actions])
    else:
        lines.append("- None for the basic docs/script workflow.")
    markdown_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    json_path.write_text(
        json.dumps(
            {
                "generated": generated,
                "repo_root": str(repo_root),
                "summary": summary,
                "results": [asdict(row) for row in results],
                "user_action_needed": actions,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return markdown_path, json_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", help="Override repo root.")
    parser.add_argument("--output-dir", default="05_OUTPUTS/health_checks", help="Report output directory relative to repo root.")
    parser.add_argument("--no-write", action="store_true", help="Do not write report files.")
    parser.add_argument("--fail-on-fail", action="store_true", help="Return non-zero if any FAIL result is present.")
    parser.add_argument("--fail-on-warn", action="store_true", help="Return non-zero if any WARN result is present.")
    parser.add_argument("--require-kicad", action="store_true", help="Treat missing KiCad and kicad-cli as FAIL instead of WARN.")
    parser.add_argument("--require-pcbnew", action="store_true", help="Treat missing KiCad-compatible pcbnew workflow support as FAIL.")
    args = parser.parse_args()

    repo_root = repo_root_from_args(args.repo_root)
    results: list[CheckResult] = []

    if (repo_root / "AGENTS.md").exists():
        add(results, "PASS", "Repo", "Repo root detected", str(repo_root))
    else:
        add(results, "FAIL", "Repo", "Repo root detected", f"AGENTS.md not found under {repo_root}")

    python_report = build_python_environment_report()
    add(results, "PASS", "Toolchain", "Python detected", f"{python_report['python_executable']} ({python_report['python_version']})")
    add(
        results,
        "PASS" if python_report["python_version_ok"] else "FAIL",
        "Toolchain",
        "Python version readiness",
        "Python 3.11+ is required for the standard repo workflow.",
    )
    add(
        results,
        "PASS" if python_report["pip"]["available"] else "WARN",
        "Toolchain",
        "pip availability",
        str(python_report["pip"]["detail"]),
    )

    git_path = first_path(["git"])
    add(results, "PASS" if git_path else "WARN", "Toolchain", "Git detected", git_path or "Git not found. ZIP users can still use the repo locally.")

    kicad = detect_kicad_environment(probe_pcbnew=False)
    pcbnew_context = build_kicad_python_context(explicit_root=kicad["kicad_root"]["path"])
    kicad_required = args.require_kicad
    add(
        results,
        "PASS" if kicad["kicad_root"]["detected"] else ("FAIL" if kicad_required else "WARN"),
        "Toolchain",
        "KiCad detected",
        kicad["kicad_root"]["path"] or kicad["missing_message"],
    )
    add(
        results,
        "PASS" if kicad["kicad_cli"]["path"] else ("FAIL" if kicad_required else "WARN"),
        "Toolchain",
        "kicad-cli detected",
        kicad["kicad_cli"]["path"] or kicad["missing_message"],
    )
    add(
        results,
        "PASS" if pcbnew_context["pcbnew"]["available"] else ("FAIL" if args.require_pcbnew else "WARN"),
        "Toolchain",
        "pcbnew workflow availability",
        str(pcbnew_context["pcbnew"]["message"]),
    )
    add(
        results,
        "PASS" if pcbnew_context["pcbnew"]["current_python_available"] else "WARN",
        "Toolchain",
        "pcbnew direct import",
        "Current Python can import pcbnew directly."
        if pcbnew_context["pcbnew"]["current_python_available"]
        else "Current Python cannot import pcbnew directly; board-aware scripts should use KiCad Python context.",
    )

    missing_docs = [path for path in REQUIRED_DOCS if not (repo_root / path).exists()]
    add(
        results,
        "PASS" if not missing_docs else "FAIL",
        "Docs",
        "Required onboarding docs",
        "All required onboarding docs are present." if not missing_docs else ", ".join(missing_docs),
    )

    active_project = parse_active_project(repo_root)
    if active_project and (repo_root / active_project).exists():
        add(results, "PASS", "Repo", "Active project exists", active_project)
    else:
        add(results, "FAIL", "Repo", "Active project exists", active_project or "No active project path found in 00_CODEX_START/CURRENT_PROJECT.md")

    missing_placeholders = [path for path in KNOWN_LOCAL_ONLY_PLACEHOLDERS if not (repo_root / path).exists()]
    add(
        results,
        "PASS" if not missing_placeholders else "FAIL",
        "Portability",
        "Local-only folders documented",
        "Placeholder docs exist for known local-only folders." if not missing_placeholders else ", ".join(missing_placeholders),
    )

    for label, command in KEY_SCRIPT_COMMANDS:
        ok, detail = run_command(command, repo_root)
        add(results, "PASS" if ok else "FAIL", "Scripts", label, detail)

    missing_optional: list[str] = []
    for label, commands in OPTIONAL_TOOLS.items():
        found = first_path(commands)
        if not found:
            missing_optional.append(label)
    add(
        results,
        "PASS" if not missing_optional else "WARN",
        "Toolchain",
        "Optional tools missing",
        "None." if not missing_optional else ", ".join(missing_optional),
    )

    actions = user_actions(results)
    summary = summarize(results)
    print("KICAD_ENGINE health check")
    print(f"Repo root: {repo_root}")
    print(f"PASS={summary['PASS']} WARN={summary['WARN']} FAIL={summary['FAIL']}")
    if actions:
        print("User action needed:")
        for action in actions:
            print(f"- {action}")

    if not args.no_write:
        markdown_path, json_path = write_reports(repo_root, repo_root / args.output_dir, results, actions)
        print(f"Report: {markdown_path}")
        print(f"JSON: {json_path}")

    if args.fail_on_warn and summary["WARN"] > 0:
        return 1
    if args.fail_on_fail and summary["FAIL"] > 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
