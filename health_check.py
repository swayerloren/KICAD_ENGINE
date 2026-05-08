#!/usr/bin/env python3
"""KiCad Engine health check.

This script is read-only except for optional reports written under 05_OUTPUTS.
It does not install tools, store secrets, or modify KiCad project files.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Iterable


STATUSES = ("PASS", "WARN", "FAIL")

REQUIRED_REPO_FOLDERS = [
    ".vscode",
    ".prompts",
    ".prompts/codex",
    ".prompts/claude",
    ".prompts/shared",
    "00_CODEX_START",
    "01_MEMORY",
    "02_HISTORY",
    "03_TOOLS",
    "03_TOOLS/scripts",
    "04_KICAD_PROJECTS",
    "05_OUTPUTS",
    "06_DATASHEETS",
    "08_COMPONENT_DATABASE",
    "09_ACCURACY_ENGINE",
    "09_ACCURACY_ENGINE/schematic_rules",
    "09_ACCURACY_ENGINE/pcb_rules",
    "09_ACCURACY_ENGINE/verification_rules",
    "09_ACCURACY_ENGINE/workflows",
    "10_KNOWLEDGE_BASE",
    "10_KNOWLEDGE_BASE/circuits",
    "10_KNOWLEDGE_BASE/design_patterns",
    "10_KNOWLEDGE_BASE/checklists",
    "10_KNOWLEDGE_BASE/common_mistakes",
    "10_KNOWLEDGE_BASE/manufacturing",
    "10_KNOWLEDGE_BASE/ai_agent_guidance",
    "11_LIBRARY_FACTORY",
    "11_LIBRARY_FACTORY/symbols",
    "11_LIBRARY_FACTORY/footprints",
    "11_LIBRARY_FACTORY/mapping",
    "11_LIBRARY_FACTORY/scripts",
    "12_REFERENCE_DESIGN_LIBRARY",
    "12_REFERENCE_DESIGN_LIBRARY/00_INDEX",
    "12_REFERENCE_DESIGN_LIBRARY/ESP32",
    "12_REFERENCE_DESIGN_LIBRARY/STM32",
    "12_REFERENCE_DESIGN_LIBRARY/PIC_AVR",
    "12_REFERENCE_DESIGN_LIBRARY/POWER",
    "12_REFERENCE_DESIGN_LIBRARY/USB",
    "12_REFERENCE_DESIGN_LIBRARY/CAN",
    "12_REFERENCE_DESIGN_LIBRARY/RF",
    "12_REFERENCE_DESIGN_LIBRARY/AUTOMOTIVE",
    "13_PART_INGESTION",
    "13_PART_INGESTION/scripts",
    "14_LAYOUT_AUTOMATION",
    "15_BENCHMARKS",
    "15_BENCHMARKS/tasks",
    "15_BENCHMARKS/scoring",
    "15_BENCHMARKS/results",
    "99_BACKUPS",
    "setup",
    "setup/windows",
    "setup/macos",
    "setup/linux",
    "setup/common",
]

REQUIRED_DATASHEET_FOLDERS = [
    "06_DATASHEETS/00_INDEX",
    "06_DATASHEETS/01_MICROCONTROLLERS",
    "06_DATASHEETS/02_DEV_BOARDS_AND_MODULES",
    "06_DATASHEETS/03_POWER",
    "06_DATASHEETS/04_COMMUNICATION",
    "06_DATASHEETS/05_CONNECTORS",
    "06_DATASHEETS/06_PROTECTION",
    "06_DATASHEETS/07_SENSORS",
    "06_DATASHEETS/08_ANALOG",
    "06_DATASHEETS/09_DRIVERS",
    "06_DATASHEETS/10_DISPLAYS",
    "06_DATASHEETS/11_PASSIVES",
    "06_DATASHEETS/12_RF_AND_ANTENNAS",
    "06_DATASHEETS/13_MEMORY_STORAGE",
    "06_DATASHEETS/14_CLOCKS_TIMING",
    "06_DATASHEETS/15_SWITCHES_BUTTONS_RELAYS",
    "06_DATASHEETS/16_FAB_ASSEMBLY_REFERENCES",
    "06_DATASHEETS/17_APPLICATION_NOTES",
    "06_DATASHEETS/18_REFERENCE_DESIGNS",
    "06_DATASHEETS/19_VENDOR_PORTALS",
    "06_DATASHEETS/99_UNSORTED_INBOX",
]

REQUIRED_COMPONENT_FOLDERS = [
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

REQUIRED_PROMPT_FILES = [
    ".prompts/README.md",
    ".prompts/codex/00_START_SESSION.md",
    ".prompts/claude/00_START_SESSION.md",
    ".prompts/shared/SAFETY_GATES.md",
    ".prompts/shared/COMPONENT_RESEARCH_STANDARD.md",
    ".prompts/shared/KICAD_VERIFICATION_STANDARD.md",
]

REQUIRED_PUBLIC_RELEASE_DOCS = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "CHANGELOG.md",
    "ROADMAP.md",
    "DISCLAIMER.md",
    "PUBLIC_RELEASE_CHECKLIST.md",
    "START_HERE_FOR_USERS.md",
]

REQUIRED_SCRIPT_FILES = [
    "03_TOOLS/scripts/kicad_engine_health_check.ps1",
    "03_TOOLS/scripts/kicad_app_audit/audit_kicad_windows.ps1",
    "03_TOOLS/scripts/datasheets/build_datasheet_index.py",
    "03_TOOLS/scripts/project_validation/validate_kicad_project.ps1",
    "03_TOOLS/scripts/project_validation/validate_kicad_project.py",
    "03_TOOLS/scripts/run_erc.ps1",
    "03_TOOLS/scripts/run_drc.ps1",
    "03_TOOLS/scripts/full_verify_project.ps1",
    "health_check.py",
    "health_check.ps1",
    "setup/common/create_repo_folders.py",
    "setup/common/build_indexes.py",
    "setup/common/write_setup_report.py",
]

SECRET_FILENAME_PATTERNS = [
    ".env",
    ".env.local",
    "id_rsa",
    "id_dsa",
    "id_ecdsa",
    "id_ed25519",
    "private_key.pem",
]

SECRET_CONTENT_PATTERNS = [
    re.compile(r"-----BEGIN (RSA |DSA |EC |OPENSSH |)?PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
]

SECRET_ASSIGNMENT_PATTERN = re.compile(
    r"(?i)\b(openai|anthropic|github|gitlab|aws|azure|google)?[_-]?"
    r"(api[_-]?key|access[_-]?token|secret|password)\b[ \t]*[:=][ \t]*['\"]?"
    r"(?P<value>[A-Za-z0-9_./+=-]{12,})"
)

PLACEHOLDER_SECRET_VALUE = re.compile(
    r"^(\$\{\{.*\}\}|YOUR[_-].*|REPLACE[_-]?ME|CHANGEME|EXAMPLE[_-].*|[A-Z0-9_:-]+)$"
)

TEXT_SCAN_SUFFIXES = {
    ".md",
    ".txt",
    ".json",
    ".toml",
    ".yaml",
    ".yml",
    ".py",
    ".ps1",
    ".sh",
    ".csv",
}

SCAN_EXCLUDE_PARTS = {
    ".git",
    "__pycache__",
    "node_modules",
    "build",
    "dist",
    "03_TOOLS/python_envs",
    "03_TOOLS/node_envs",
    "03_TOOLS/repos",
    "03_TOOLS/windows/repos",
    "03_TOOLS/linux/repos",
    "03_TOOLS/common/repos",
    "05_OUTPUTS",
    "99_BACKUPS",
}

FAB_SUFFIXES = {
    ".gbr",
    ".gbl",
    ".gtl",
    ".gbs",
    ".gts",
    ".gbo",
    ".gto",
    ".gm1",
    ".drl",
    ".xln",
    ".pos",
    ".zip",
    ".step",
    ".stp",
}


@dataclass
class CheckResult:
    status: str
    category: str
    name: str
    detail: str


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parent


def add(results: list[CheckResult], status: str, category: str, name: str, detail: str) -> None:
    if status not in STATUSES:
        raise ValueError(status)
    results.append(CheckResult(status=status, category=category, name=name, detail=detail))


def command_output(command: list[str]) -> tuple[bool, str, str]:
    exe = shutil.which(command[0])
    if not exe:
        return False, "", ""
    try:
        completed = subprocess.run(command, text=True, capture_output=True, timeout=20, check=False)
        output = (completed.stdout or completed.stderr).strip()
        first_line = output.splitlines()[0] if output.splitlines() else ""
        return completed.returncode == 0, exe, first_line
    except Exception as exc:  # noqa: BLE001
        return False, exe, f"ERROR: {exc}"


def check_command(results: list[CheckResult], label: str, command: list[str], fail_if_missing: bool = False) -> None:
    ok, path, version = command_output(command)
    if ok:
        add(results, "PASS", "Tool", label, f"Found: {path}; {version}")
    elif path:
        add(results, "WARN", "Tool", label, f"Found but version check failed: {path}; {version}")
    else:
        status = "FAIL" if fail_if_missing else "WARN"
        add(results, status, "Tool", label, f"Not found on PATH using command: {' '.join(command)}")


def find_kicad_install() -> str:
    system = platform.system().lower()
    candidates: list[Path] = []
    if system == "windows":
        candidates.extend(
            [
                Path(r"C:\Program Files\KiCad\9.0"),
                Path(r"C:\Program Files\KiCad"),
                Path(r"C:\Program Files (x86)\KiCad"),
            ]
        )
    elif system == "darwin":
        candidates.extend([Path("/Applications/KiCad/KiCad.app"), Path("/Applications/KiCad")])
    else:
        for command in ("kicad", "kicad-cli"):
            found = shutil.which(command)
            if found:
                return found
        candidates.extend([Path("/usr/share/kicad"), Path("/usr/local/share/kicad"), Path("/app/share/kicad")])
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return ""


def find_vscode() -> str:
    found = shutil.which("code")
    if found:
        return found
    if platform.system().lower() == "windows":
        local = os.environ.get("LOCALAPPDATA", "")
        candidates = [
            Path(local) / "Programs" / "Microsoft VS Code" / "Code.exe",
            Path(r"C:\Program Files\Microsoft VS Code\Code.exe"),
        ]
    elif platform.system().lower() == "darwin":
        candidates = [Path("/Applications/Visual Studio Code.app")]
    else:
        candidates = [Path("/usr/bin/code"), Path("/snap/bin/code"), Path("/var/lib/flatpak/exports/bin/com.visualstudio.code")]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return ""


def check_kicad(results: list[CheckResult]) -> None:
    install = find_kicad_install()
    if install:
        add(results, "PASS", "Tool", "KiCad installed", f"Found: {install}")
    else:
        add(results, "FAIL", "Tool", "KiCad installed", "KiCad install was not detected.")
    check_command(results, "kicad-cli available", ["kicad-cli", "version"], fail_if_missing=True)


def check_basic_tools(results: list[CheckResult]) -> None:
    check_command(results, "Git installed", ["git", "--version"], fail_if_missing=True)
    check_command(results, "Python installed", [sys.executable, "--version"], fail_if_missing=True)
    check_command(results, "Node installed", ["node", "--version"], fail_if_missing=False)
    vscode = find_vscode()
    if vscode:
        add(results, "PASS", "Tool", "VS Code installed", f"Found: {vscode}")
    else:
        add(results, "WARN", "Tool", "VS Code installed", "VS Code was not detected. Users may still open the repo manually.")


def check_paths(results: list[CheckResult], repo_root: Path, category: str, paths: Iterable[str]) -> None:
    for rel in paths:
        path = repo_root / rel
        if path.exists():
            add(results, "PASS", category, rel, "Found.")
        else:
            add(results, "FAIL", category, rel, "Missing.")


def check_prompt_pack(results: list[CheckResult], repo_root: Path) -> None:
    check_paths(results, repo_root, "Prompt Pack", REQUIRED_PROMPT_FILES)
    codex_count = len(list((repo_root / ".prompts" / "codex").glob("*.md"))) if (repo_root / ".prompts" / "codex").exists() else 0
    claude_count = len(list((repo_root / ".prompts" / "claude").glob("*.md"))) if (repo_root / ".prompts" / "claude").exists() else 0
    shared_count = len(list((repo_root / ".prompts" / "shared").glob("*.md"))) if (repo_root / ".prompts" / "shared").exists() else 0
    add(results, "PASS" if codex_count >= 13 else "FAIL", "Prompt Pack", "Codex prompt count", f"{codex_count} markdown files.")
    add(results, "PASS" if claude_count >= 13 else "FAIL", "Prompt Pack", "Claude prompt count", f"{claude_count} markdown files.")
    add(results, "PASS" if shared_count >= 5 else "FAIL", "Prompt Pack", "Shared standard count", f"{shared_count} markdown files.")


def is_excluded(path: Path, repo_root: Path) -> bool:
    rel = path.resolve().relative_to(repo_root.resolve()).as_posix()
    parts = set(rel.split("/"))
    if parts & SCAN_EXCLUDE_PARTS:
        return True
    for excluded in SCAN_EXCLUDE_PARTS:
        if rel.startswith(excluded + "/"):
            return True
    return False


def check_secrets(results: list[CheckResult], repo_root: Path) -> None:
    findings: list[str] = []
    for path in repo_root.rglob("*"):
        if not path.is_file() or is_excluded(path, repo_root):
            continue
        if path.name in SECRET_FILENAME_PATTERNS:
            findings.append(f"Sensitive filename: {path.relative_to(repo_root)}")
            continue
        if path.suffix.lower() not in TEXT_SCAN_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for pattern in SECRET_CONTENT_PATTERNS:
            if pattern.search(text):
                findings.append(f"Potential secret pattern: {path.relative_to(repo_root)}")
                break
        else:
            for match in SECRET_ASSIGNMENT_PATTERN.finditer(text):
                value = match.group("value").strip().strip("'\"")
                if PLACEHOLDER_SECRET_VALUE.match(value):
                    continue
                findings.append(f"Potential secret assignment: {path.relative_to(repo_root)}")
                break
    if findings:
        detail = "; ".join(findings[:20])
        if len(findings) > 20:
            detail += f"; plus {len(findings) - 20} more"
        add(results, "FAIL", "Security", "No secrets accidentally present", detail)
    else:
        add(results, "PASS", "Security", "No secrets accidentally present", "No likely secret files or assignment-style secret patterns found in scanned repo text.")


def check_final_fab_labels(results: list[CheckResult], repo_root: Path) -> None:
    search_roots = [repo_root / "05_OUTPUTS", repo_root / "04_KICAD_PROJECTS", repo_root / "99_01 Finished PCBs"]
    suspicious: list[str] = []
    final_pattern = re.compile(r"(?<!NOT_)FINAL", re.IGNORECASE)
    for root in search_roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            suffix = path.suffix.lower()
            rel = path.relative_to(repo_root).as_posix()
            upper_rel = rel.upper()
            if suffix in FAB_SUFFIXES and "NOT_FINAL" not in upper_rel and final_pattern.search(upper_rel):
                suspicious.append(rel)
    if suspicious:
        detail = "; ".join(suspicious[:20])
        add(results, "WARN", "Fabrication Outputs", "No final fab outputs mislabeled as final", detail)
    else:
        add(results, "PASS", "Fabrication Outputs", "No final fab outputs mislabeled as final", "No suspicious final-labeled fabrication files found.")


def summarize(results: list[CheckResult]) -> dict[str, int]:
    return {status: sum(1 for row in results if row.status == status) for status in STATUSES}


def write_reports(repo_root: Path, output_dir: Path, results: list[CheckResult]) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    markdown = output_dir / f"KICAD_ENGINE_HEALTH_CHECK_{stamp}.md"
    json_path = output_dir / f"KICAD_ENGINE_HEALTH_CHECK_{stamp}.json"
    summary = summarize(results)
    generated = datetime.now().isoformat(timespec="seconds")
    lines = [
        "# KiCad Engine Health Check Report",
        "",
        f"Generated: {generated}",
        f"Repo root: `{repo_root}`",
        f"Platform: `{platform.platform()}`",
        "",
        "This report is generated locally. It does not install tools, store secrets, or modify KiCad project files.",
        "",
        "## Summary",
        "",
        f"- PASS: {summary['PASS']}",
        f"- WARN: {summary['WARN']}",
        f"- FAIL: {summary['FAIL']}",
        "",
        "## Results",
        "",
        "| Status | Category | Name | Detail |",
        "| --- | --- | --- | --- |",
    ]
    for row in sorted(results, key=lambda item: (item.status != "FAIL", item.status != "WARN", item.category, item.name)):
        detail = row.detail.replace("|", "\\|")
        lines.append(f"| {row.status} | {row.category} | {row.name} | {detail} |")
    lines += [
        "",
        "## Safety Notes",
        "",
        "- Missing tools should be installed only by the user or by opt-in installer scripts after confirmation.",
        "- Do not store API keys, passwords, tokens, private keys, or license keys in this repo.",
        "- Keep generated manufacturing-style outputs labeled `NOT_FINAL` until all verification gates pass.",
    ]
    markdown.write_text("\n".join(lines) + "\n", encoding="utf-8")
    data = {
        "generated": generated,
        "repo_root": str(repo_root),
        "platform": platform.platform(),
        "summary": summary,
        "results": [asdict(row) for row in results],
    }
    json_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return markdown, json_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=str(repo_root_from_script()))
    parser.add_argument("--output-dir", default="05_OUTPUTS/health_checks")
    parser.add_argument("--no-write", action="store_true")
    parser.add_argument("--fail-on-fail", action="store_true")
    parser.add_argument("--fail-on-warn", action="store_true")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    results: list[CheckResult] = []

    check_kicad(results)
    check_basic_tools(results)
    check_paths(results, repo_root, "Repo Structure", REQUIRED_REPO_FOLDERS)
    check_paths(results, repo_root, "Datasheets", REQUIRED_DATASHEET_FOLDERS)
    check_paths(results, repo_root, "Component Database", REQUIRED_COMPONENT_FOLDERS)
    check_paths(results, repo_root, "Public Release Docs", REQUIRED_PUBLIC_RELEASE_DOCS)
    check_prompt_pack(results, repo_root)
    check_paths(results, repo_root, "Scripts", REQUIRED_SCRIPT_FILES)
    check_secrets(results, repo_root)
    check_final_fab_labels(results, repo_root)

    summary = summarize(results)
    print("KiCad Engine Health Check")
    print(f"Repo root: {repo_root}")
    print(f"PASS={summary['PASS']} WARN={summary['WARN']} FAIL={summary['FAIL']}")

    if not args.no_write:
        markdown, json_path = write_reports(repo_root, repo_root / args.output_dir, results)
        print(f"Report: {markdown}")
        print(f"JSON: {json_path}")

    if args.fail_on_warn and summary["WARN"] > 0:
        return 1
    if args.fail_on_fail and summary["FAIL"] > 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
