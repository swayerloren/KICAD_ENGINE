#!/usr/bin/env python3
"""Report Python readiness for portable KiCad Engine workflows."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path


OPTIONAL_MODULES = {
    "pcbnew": "Provided by a local KiCad install for board-aware workflows.",
    "PIL": "Optional Windows screenshot helper dependency.",
    "psutil": "Optional Windows process inspection dependency.",
    "pyautogui": "Optional Windows screenshot and GUI helper dependency.",
    "pygetwindow": "Optional Windows window discovery dependency.",
    "pywinauto": "Optional Windows GUI automation dependency.",
}


def repo_root() -> Path:
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "AGENTS.md").exists():
            return parent
    return Path.cwd().resolve()


def pip_status() -> dict:
    try:
        completed = subprocess.run(
            [sys.executable, "-m", "pip", "--version"],
            capture_output=True,
            text=True,
            timeout=15,
            check=False,
        )
    except Exception as exc:  # noqa: BLE001
        return {"available": False, "detail": str(exc)}
    output = (completed.stdout or completed.stderr).strip()
    return {"available": completed.returncode == 0, "detail": output}


def optional_modules() -> dict[str, dict[str, str | bool]]:
    result: dict[str, dict[str, str | bool]] = {}
    for name, note in OPTIONAL_MODULES.items():
        spec = importlib.util.find_spec(name)
        result[name] = {
            "available": spec is not None,
            "note": note,
        }
    return result


def build_python_environment_report() -> dict:
    root = repo_root()
    return {
        "python_executable": sys.executable,
        "python_version": sys.version.split()[0],
        "python_version_ok": sys.version_info >= (3, 11),
        "virtualenv_active": sys.prefix != getattr(sys, "base_prefix", sys.prefix),
        "pip": pip_status(),
        "requirements_txt": (root / "requirements.txt").exists(),
        "pyproject_toml": (root / "pyproject.toml").exists(),
        "hidden_repo_env_required": False,
        "optional_modules": optional_modules(),
        "guidance": [
            "Basic health checks and portability audits run with the Python standard library only.",
            "A hidden repo venv under 03_TOOLS/python_envs is not required for basic use.",
            "KiCad-provided pcbnew is only needed for board-aware workflows.",
            "Normal Python may not import pcbnew directly; use 03_TOOLS/scripts/kicad_api/pcbnew_import_check.py when board-aware work is requested.",
        ],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Emit JSON output.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payload = build_python_environment_report()
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print("Python environment readiness")
        print(f"- Python: `{payload['python_executable']}`")
        print(f"- Version: `{payload['python_version']}`")
        print(f"- Python >= 3.11: `{payload['python_version_ok']}`")
        print(f"- Virtualenv active: `{payload['virtualenv_active']}`")
        print(f"- pip available: `{payload['pip']['available']}`")
        print(f"- requirements.txt present: `{payload['requirements_txt']}`")
        print(f"- pyproject.toml present: `{payload['pyproject_toml']}`")
        print(f"- Hidden repo env required: `{payload['hidden_repo_env_required']}`")
        print("- Optional modules:")
        for name, info in payload["optional_modules"].items():
            print(f"  - {name}: {info['available']} ({info['note']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
