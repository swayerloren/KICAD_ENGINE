#!/usr/bin/env python3
"""Discover a local KiCad install without modifying the machine."""

from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterable


WINDOWS_VERSION_HINTS = ("9.0", "8.0", "7.0")
WINDOWS_ROOTS = (
    Path(r"C:\Program Files\KiCad"),
    Path(r"C:\Program Files (x86)\KiCad"),
)
MACOS_ROOTS = (
    Path("/Applications/KiCad/KiCad.app"),
    Path("/Applications/KiCad"),
)
LINUX_ROOTS = (
    Path("/usr"),
    Path("/usr/local"),
    Path("/opt/kicad"),
    Path("/app"),
)


def existing_file(path: Path | None) -> Path | None:
    if path and path.exists() and path.is_file():
        return path.resolve()
    return None


def existing_dir(path: Path | None) -> Path | None:
    if path and path.exists() and path.is_dir():
        return path.resolve()
    return None


def unique_paths(paths: Iterable[Path | None]) -> list[Path]:
    seen: set[str] = set()
    ordered: list[Path] = []
    for path in paths:
        if not path:
            continue
        key = str(path).lower()
        if key in seen:
            continue
        seen.add(key)
        ordered.append(path)
    return ordered


def normalized_root(candidate: Path) -> Path:
    path = candidate.resolve()
    if path.is_file():
        lower_name = path.name.lower()
        if lower_name in {"kicad-cli.exe", "kicad-cli", "kicad.exe", "kicad", "pcbnew.exe", "pcbnew"}:
            if path.parent.name.lower() == "bin" and len(path.parents) >= 2:
                return path.parent.parent
            if path.parent.name == "MacOS" and len(path.parents) >= 3:
                return path.parents[2]
        return path.parent
    return path


def common_install_roots(system_name: str) -> list[Path]:
    candidates: list[Path] = []
    if system_name == "windows":
        for base in WINDOWS_ROOTS:
            if base.exists():
                for version in WINDOWS_VERSION_HINTS:
                    candidates.append(base / version)
                candidates.extend(sorted((child for child in base.iterdir() if child.is_dir()), key=lambda item: item.name, reverse=True))
            candidates.append(base)
    elif system_name == "darwin":
        candidates.extend(MACOS_ROOTS)
    else:
        candidates.extend(LINUX_ROOTS)
    return unique_paths(candidates)


def build_root_candidates(explicit_root: str | None, explicit_cli: str | None, explicit_gui: str | None) -> list[Path]:
    system_name = platform.system().lower()
    candidates: list[Path | None] = []

    for raw in (explicit_root, os.environ.get("KICAD_ROOT"), os.environ.get("KICAD_HOME")):
        if raw:
            candidates.append(normalized_root(Path(raw)))

    for raw in (
        explicit_cli,
        explicit_gui,
        os.environ.get("KICAD_CLI"),
        os.environ.get("KICAD_EXE"),
        os.environ.get("KICAD"),
    ):
        if raw:
            candidates.append(normalized_root(Path(raw)))

    for command_name in ("kicad-cli", "kicad-cli.exe", "kicad", "kicad.exe"):
        found = shutil.which(command_name)
        if found:
            candidates.append(normalized_root(Path(found)))

    candidates.extend(common_install_roots(system_name))
    return unique_paths(existing_dir(path) for path in candidates)


def executable_from_roots(roots: Iterable[Path], relative_paths: Iterable[str]) -> Path | None:
    for root in roots:
        for relative_path in relative_paths:
            candidate = root / Path(relative_path)
            found = existing_file(candidate)
            if found:
                return found
    return None


def executable_search(
    explicit_path: str | None,
    env_vars: Iterable[str],
    path_names: Iterable[str],
    roots: Iterable[Path],
    relative_paths: Iterable[str],
) -> dict:
    for raw in [explicit_path, *(os.environ.get(name) for name in env_vars)]:
        if raw:
            candidate = existing_file(Path(raw))
            if candidate:
                return {"path": str(candidate), "source": "override", "on_path": bool(shutil.which(candidate.name))}

    for name in path_names:
        found = shutil.which(name)
        if found:
            candidate = existing_file(Path(found))
            if candidate:
                return {"path": str(candidate), "source": "PATH", "on_path": True}

    from_roots = executable_from_roots(roots, relative_paths)
    if from_roots:
        return {"path": str(from_roots), "source": "common_install_path", "on_path": False}

    return {"path": None, "source": "missing", "on_path": False}


def read_version(command: list[str]) -> str:
    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=15,
            check=False,
        )
    except Exception as exc:  # noqa: BLE001
        return f"version probe failed: {exc}"
    output = (completed.stdout or completed.stderr).strip()
    if output:
        return output.splitlines()[0]
    if completed.returncode == 0:
        return "version command succeeded without printable output"
    return f"version command exited with {completed.returncode}"


def guess_version_from_root(root: Path | None) -> str | None:
    if not root:
        return None
    if root.name in WINDOWS_VERSION_HINTS:
        return root.name
    if root.name == "KiCad.app":
        return "macOS app bundle"
    return None


def candidate_python_paths(root: Path | None) -> list[Path]:
    if not root:
        return []
    candidates = [
        root / "bin" / "Lib" / "site-packages",
        root / "bin" / "Lib",
        root / "lib" / "python3" / "dist-packages",
    ]
    if (root / "lib").exists():
        candidates.extend((root / "lib").glob("python*/site-packages"))
        candidates.extend((root / "lib").glob("python*/dist-packages"))
    return unique_paths(existing_dir(path) for path in candidates)


def pcbnew_probe_with_pythonpath(root: Path, python_paths: list[Path]) -> dict:
    path_entries = [str(path) for path in python_paths]
    script = f"""
import json
import os
import sys

root_bin = {json.dumps(str(root / 'bin'))}
for candidate in {json.dumps(path_entries)}:
    if candidate not in sys.path:
        sys.path.insert(0, candidate)
if os.path.isdir(root_bin):
    os.environ["PATH"] = root_bin + os.pathsep + os.environ.get("PATH", "")
    if hasattr(os, "add_dll_directory"):
        try:
            os.add_dll_directory(root_bin)
        except OSError:
            pass
try:
    import pcbnew  # type: ignore
    payload = {{
        "available": True,
        "status": "AVAILABLE_WITH_DISCOVERED_PYTHONPATH",
        "message": getattr(pcbnew, "__file__", "pcbnew import succeeded"),
    }}
except Exception as exc:  # noqa: BLE001
    payload = {{
        "available": False,
        "status": "IMPORT_FAILED_WITH_DISCOVERED_PYTHONPATH",
        "message": str(exc),
    }}
print(json.dumps(payload))
raise SystemExit(0 if payload["available"] else 1)
"""
    completed = subprocess.run(
        [sys.executable, "-c", script],
        capture_output=True,
        text=True,
        timeout=20,
        check=False,
    )
    try:
        payload = json.loads((completed.stdout or "{}").strip())
    except json.JSONDecodeError:
        payload = {
            "available": False,
            "status": "IMPORT_FAILED_WITH_DISCOVERED_PYTHONPATH",
            "message": (completed.stderr or completed.stdout).strip() or "pcbnew probe produced no parseable output",
        }
    payload["python"] = sys.executable
    payload["pythonpath_candidates"] = path_entries
    return payload


def detect_pcbnew(root: Path | None) -> dict:
    try:
        import pcbnew  # type: ignore

        return {
            "available": True,
            "status": "AVAILABLE_IN_CURRENT_PYTHON",
            "python": sys.executable,
            "message": getattr(pcbnew, "__file__", "pcbnew import succeeded"),
            "pythonpath_candidates": [],
        }
    except Exception as exc:  # noqa: BLE001
        failure_message = str(exc)

    python_paths = candidate_python_paths(root)
    if root and python_paths:
        payload = pcbnew_probe_with_pythonpath(root, python_paths)
        if payload["available"]:
            return payload
        failure_message = payload["message"]

    return {
        "available": False,
        "status": "MISSING_OR_NOT_IMPORTABLE",
        "python": sys.executable,
        "message": failure_message,
        "pythonpath_candidates": [str(path) for path in python_paths],
    }


def detected_root(cli_path: str | None, gui_path: str | None, roots: list[Path]) -> Path | None:
    for raw in (cli_path, gui_path):
        if raw:
            return normalized_root(Path(raw))
    return roots[0] if roots else None


def detect_kicad_environment(
    explicit_root: str | None = None,
    explicit_cli: str | None = None,
    explicit_gui: str | None = None,
    probe_pcbnew: bool = True,
) -> dict:
    roots = build_root_candidates(explicit_root=explicit_root, explicit_cli=explicit_cli, explicit_gui=explicit_gui)
    cli = executable_search(
        explicit_path=explicit_cli,
        env_vars=("KICAD_CLI",),
        path_names=("kicad-cli", "kicad-cli.exe"),
        roots=roots,
        relative_paths=("bin/kicad-cli.exe", "bin/kicad-cli", "Contents/MacOS/kicad-cli"),
    )
    gui = executable_search(
        explicit_path=explicit_gui,
        env_vars=("KICAD_EXE", "KICAD"),
        path_names=("kicad", "kicad.exe"),
        roots=roots,
        relative_paths=("bin/kicad.exe", "bin/kicad", "Contents/MacOS/kicad"),
    )

    root = detected_root(cli.get("path"), gui.get("path"), roots)
    version_hint = guess_version_from_root(root)
    cli["version"] = read_version([cli["path"], "version"]) if cli.get("path") else None
    gui["version"] = read_version([gui["path"], "--version"]) if gui.get("path") else None

    payload = {
        "platform": platform.platform(),
        "kicad_root": {
            "path": str(root) if root else None,
            "detected": bool(root),
            "source": "derived" if root else "missing",
            "version_hint": version_hint,
        },
        "kicad_cli": cli,
        "kicad_gui": gui,
        "pcbnew": detect_pcbnew(root) if probe_pcbnew else {
            "available": False,
            "status": "NOT_PROBED",
            "python": sys.executable,
            "message": "pcbnew probe skipped",
            "pythonpath_candidates": [],
        },
        "searched_roots": [str(item) for item in roots],
    }

    if not root and not cli.get("path") and not gui.get("path"):
        payload["missing_message"] = (
            "KiCad was not detected. Install KiCad locally for live schematic or PCB work, "
            "or keep using docs/scripts-only workflows without KiCad."
        )
    elif root and not cli.get("path"):
        payload["missing_message"] = (
            "A KiCad install root was detected, but kicad-cli was not resolved. "
            "Use --kicad-cli or add the KiCad bin folder to PATH."
        )
    else:
        payload["missing_message"] = ""
    return payload


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kicad-root", help="Optional KiCad install root override.")
    parser.add_argument("--kicad-cli", help="Optional kicad-cli override.")
    parser.add_argument("--kicad-exe", help="Optional kicad GUI executable override.")
    parser.add_argument("--no-pcbnew-probe", action="store_true", help="Skip pcbnew import checks.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payload = detect_kicad_environment(
        explicit_root=args.kicad_root,
        explicit_cli=args.kicad_cli,
        explicit_gui=args.kicad_exe,
        probe_pcbnew=not args.no_pcbnew_probe,
    )
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
