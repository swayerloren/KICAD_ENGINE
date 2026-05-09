#!/usr/bin/env python3
"""Detect KiCad-compatible Python context for pcbnew workflows."""

from __future__ import annotations

import argparse
import json
import os
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable


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
REEXEC_ENV = "KICAD_ENGINE_PCBNEW_CONTEXT_ACTIVE"


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


def build_root_candidates(explicit_root: str | None = None) -> list[Path]:
    system_name = platform.system().lower()
    candidates: list[Path | None] = []

    for raw in (
        explicit_root,
        os.environ.get("KICAD_ROOT"),
        os.environ.get("KICAD_HOME"),
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


def detect_kicad_root(explicit_root: str | None = None) -> Path | None:
    roots = build_root_candidates(explicit_root=explicit_root)
    return roots[0] if roots else None


def candidate_python_paths(root: Path | None) -> list[Path]:
    if not root:
        return []
    candidates = [
        root / "bin" / "Lib" / "site-packages",
        root / "bin" / "Lib",
        root / "bin" / "DLLs",
        root / "lib" / "python3" / "dist-packages",
    ]
    if (root / "lib").exists():
        candidates.extend((root / "lib").glob("python*/site-packages"))
        candidates.extend((root / "lib").glob("python*/dist-packages"))
    return unique_paths(existing_dir(path) for path in candidates)


def detect_kicad_python(root: Path | None) -> Path | None:
    if not root:
        return None
    candidates = [
        root / "bin" / "python.exe",
        root / "bin" / "python3.exe",
        root / "bin" / "python",
        root / "python.exe",
    ]
    for candidate in candidates:
        found = existing_file(candidate)
        if found:
            return found
    return None


def parse_major_minor(version: str | None) -> str | None:
    if not version:
        return None
    match = re.match(r"(?P<major>\d+)\.(?P<minor>\d+)", version)
    if not match:
        return None
    return f"{match.group('major')}.{match.group('minor')}"


def detect_embedded_python(root: Path | None) -> dict[str, Any]:
    payload = {"dll_path": None, "version": None, "major_minor": None}
    if not root:
        return payload
    for candidate in sorted((root / "bin").glob("python*.dll")):
        match = re.fullmatch(r"python(?P<major>\d)(?P<minor>\d{2})\.dll", candidate.name.lower())
        if not match:
            continue
        version = f"{match.group('major')}.{int(match.group('minor'))}"
        return {
            "dll_path": str(candidate.resolve()),
            "version": version,
            "major_minor": version,
        }
    return payload


def current_python_info() -> dict[str, Any]:
    version = sys.version.split()[0]
    return {
        "executable": sys.executable,
        "version": version,
        "major_minor": parse_major_minor(version),
    }


def probe_python_info(executable: Path | None) -> dict[str, Any]:
    if not executable:
        return {
            "path": None,
            "detected": False,
            "version": None,
            "major_minor": None,
            "message": "KiCad-bundled Python executable not detected.",
        }
    script = "import json, sys; print(json.dumps({'version': sys.version.split()[0], 'executable': sys.executable}))"
    try:
        completed = subprocess.run(
            [str(executable), "-c", script],
            capture_output=True,
            text=True,
            timeout=15,
            check=False,
        )
    except Exception as exc:  # noqa: BLE001
        return {
            "path": str(executable),
            "detected": True,
            "version": None,
            "major_minor": None,
            "message": str(exc),
        }
    output = (completed.stdout or completed.stderr).strip()
    if completed.returncode != 0:
        return {
            "path": str(executable),
            "detected": True,
            "version": None,
            "major_minor": None,
            "message": output or f"python probe exited with {completed.returncode}",
        }
    try:
        payload = json.loads(output)
    except json.JSONDecodeError:
        return {
            "path": str(executable),
            "detected": True,
            "version": None,
            "major_minor": None,
            "message": output or "python probe returned unreadable output",
        }
    version = str(payload.get("version") or "")
    return {
        "path": str(executable),
        "detected": True,
        "version": version or None,
        "major_minor": parse_major_minor(version),
        "message": f"KiCad Python {version}" if version else "KiCad Python detected",
    }


def root_bin(root: Path | None) -> Path | None:
    if not root:
        return None
    return existing_dir(root / "bin")


def run_import_probe(executable: str, root: Path | None, python_paths: list[Path], add_discovered_paths: bool) -> dict[str, Any]:
    root_bin_path = str(root_bin(root)) if root_bin(root) else ""
    script = """
import json
import os
import sys

root_bin = ROOT_BIN
python_paths = PYTHON_PATHS
add_discovered_paths = ADD_DISCOVERED_PATHS

if add_discovered_paths:
    for candidate in python_paths:
        if candidate not in sys.path:
            sys.path.insert(0, candidate)
    if root_bin and os.path.isdir(root_bin):
        os.environ["PATH"] = root_bin + os.pathsep + os.environ.get("PATH", "")
        if hasattr(os, "add_dll_directory"):
            try:
                os.add_dll_directory(root_bin)
            except OSError:
                pass

payload = {
    "python_executable": sys.executable,
    "python_version": sys.version.split()[0],
}
try:
    import pcbnew  # type: ignore
    payload.update(
        {
            "available": True,
            "error_type": "",
            "message": getattr(pcbnew, "__file__", "pcbnew import succeeded"),
        }
    )
except Exception as exc:  # noqa: BLE001
    payload.update(
        {
            "available": False,
            "error_type": type(exc).__name__,
            "message": str(exc),
        }
    )
print(json.dumps(payload))
raise SystemExit(0 if payload["available"] else 1)
""".replace("ROOT_BIN", json.dumps(root_bin_path)).replace(
        "PYTHON_PATHS",
        json.dumps([str(path) for path in python_paths]),
    ).replace("ADD_DISCOVERED_PATHS", "True" if add_discovered_paths else "False")

    try:
        completed = subprocess.run(
            [executable, "-c", script],
            capture_output=True,
            text=True,
            timeout=20,
            check=False,
        )
    except Exception as exc:  # noqa: BLE001
        return {
            "available": False,
            "error_type": type(exc).__name__,
            "message": str(exc),
            "python_executable": executable,
            "python_version": None,
        }

    output = (completed.stdout or completed.stderr).strip()
    try:
        payload = json.loads(output) if output else {}
    except json.JSONDecodeError:
        payload = {
            "available": False,
            "error_type": "JSONDecodeError",
            "message": output or "pcbnew probe returned unreadable output",
            "python_executable": executable,
            "python_version": None,
        }
    payload.setdefault("available", completed.returncode == 0)
    payload.setdefault("error_type", "")
    payload.setdefault("message", "pcbnew import probe returned no message")
    payload.setdefault("python_executable", executable)
    payload.setdefault("python_version", None)
    return payload


def build_guidance(
    current: dict[str, Any],
    kicad_python: dict[str, Any],
    embedded_python: dict[str, Any],
    current_probe: dict[str, Any],
    discovered_probe: dict[str, Any],
    kicad_probe: dict[str, Any],
) -> list[str]:
    guidance: list[str] = []
    current_major_minor = current.get("major_minor")
    kicad_major_minor = kicad_python.get("major_minor") or embedded_python.get("major_minor")

    if current_probe.get("available"):
        guidance.append("Current Python can import pcbnew directly.")
    else:
        guidance.append("Normal Python may not import pcbnew even when KiCad is installed locally.")

    if current_major_minor and kicad_major_minor and current_major_minor != kicad_major_minor:
        guidance.append(
            f"Current Python {current_major_minor} does not match KiCad Python {kicad_major_minor}; "
            "injecting KiCad site-packages into the wrong interpreter can fail with a python DLL conflict."
        )

    if kicad_probe.get("available"):
        guidance.append("Board-aware scripts should re-enter through the KiCad-bundled python.exe when pcbnew is needed.")
    elif discovered_probe.get("available"):
        guidance.append("The current interpreter can load pcbnew only after KiCad-specific path injection.")
    else:
        guidance.append("If pcbnew is required, rerun the workflow after KiCad is installed or provide an explicit KiCad root override.")

    guidance.append("KiCad GUI and kicad-cli are enough for many docs, audit, ERC/DRC, and export-adjacent tasks.")
    guidance.append("Do not make pcbnew a hard requirement for basic ZIP onboarding or CI.")
    return guidance


def build_kicad_python_context(explicit_root: str | None = None) -> dict[str, Any]:
    root = detect_kicad_root(explicit_root=explicit_root)
    current = current_python_info()
    python_paths = candidate_python_paths(root)
    kicad_python_executable = detect_kicad_python(root)
    kicad_python = probe_python_info(kicad_python_executable)
    embedded_python = detect_embedded_python(root)

    current_probe = run_import_probe(current["executable"], root, [], add_discovered_paths=False)
    discovered_probe = run_import_probe(current["executable"], root, python_paths, add_discovered_paths=True) if root else {
        "available": False,
        "error_type": "",
        "message": "KiCad root not detected; discovered-path probe skipped.",
        "python_executable": current["executable"],
        "python_version": current["version"],
    }
    kicad_probe = run_import_probe(str(kicad_python_executable), root, [], add_discovered_paths=False) if kicad_python_executable else {
        "available": False,
        "error_type": "",
        "message": "KiCad-bundled Python executable not detected.",
        "python_executable": None,
        "python_version": None,
    }

    if current_probe["available"]:
        pcbnew_status = "AVAILABLE_IN_CURRENT_PYTHON"
        recommended_context = "CURRENT_PYTHON"
        status = "PASS"
        message = f"pcbnew imports in the current Python interpreter: {current_probe['message']}"
    elif discovered_probe["available"]:
        pcbnew_status = "AVAILABLE_WITH_DISCOVERED_PYTHONPATH"
        recommended_context = "CURRENT_PYTHON_WITH_DISCOVERED_PATHS"
        status = "WARN"
        message = "pcbnew imports only after injecting KiCad-specific paths into the current interpreter."
    elif kicad_probe["available"]:
        pcbnew_status = "AVAILABLE_IN_KICAD_PYTHON"
        recommended_context = "KICAD_PYTHON"
        status = "WARN"
        message = (
            f"Current Python cannot import pcbnew ({current_probe['error_type'] or 'import failure'}: {current_probe['message']}). "
            f"KiCad Python can import it: {kicad_probe['message']}"
        )
    else:
        pcbnew_status = "MISSING_OR_NOT_IMPORTABLE"
        recommended_context = "NOT_AVAILABLE"
        status = "FAIL"
        failure = kicad_probe["message"] if kicad_python_executable else current_probe["message"]
        message = f"pcbnew is not available in the current Python context: {failure}"

    guidance = build_guidance(current, kicad_python, embedded_python, current_probe, discovered_probe, kicad_probe)

    return {
        "status": status,
        "platform": platform.platform(),
        "kicad_root": {
            "path": str(root) if root else None,
            "detected": bool(root),
        },
        "current_python": current,
        "kicad_python": kicad_python,
        "embedded_python": embedded_python,
        "discovered_python_paths": [str(path) for path in python_paths],
        "pcbnew": {
            "available": bool(current_probe["available"] or discovered_probe["available"] or kicad_probe["available"]),
            "current_python_available": bool(current_probe["available"]),
            "discovered_path_available": bool(discovered_probe["available"]),
            "kicad_python_available": bool(kicad_probe["available"]),
            "status": pcbnew_status,
            "recommended_context": recommended_context,
            "message": message,
            "current_probe": current_probe,
            "discovered_path_probe": discovered_probe,
            "kicad_python_probe": kicad_probe,
            "guidance": guidance,
        },
    }


def prepare_current_process_for_kicad(root: Path | None, python_paths: list[Path]) -> None:
    for candidate in python_paths:
        text = str(candidate)
        if text not in sys.path:
            sys.path.insert(0, text)
    bin_dir = root_bin(root)
    if not bin_dir:
        return
    bin_text = str(bin_dir)
    path_entries = os.environ.get("PATH", "")
    if bin_text not in path_entries.split(os.pathsep):
        os.environ["PATH"] = bin_text + os.pathsep + path_entries
    if hasattr(os, "add_dll_directory"):
        try:
            os.add_dll_directory(bin_text)
        except OSError:
            pass


def require_pcbnew_module(explicit_root: str | None = None) -> Any:
    try:
        import pcbnew  # type: ignore

        return pcbnew
    except Exception as direct_exc:  # noqa: BLE001
        direct_error = direct_exc

    if os.environ.get(REEXEC_ENV) == "1":
        raise RuntimeError(f"pcbnew import failed even after entering KiCad Python context: {direct_error}") from direct_error

    report = build_kicad_python_context(explicit_root=explicit_root)
    recommended = report["pcbnew"]["recommended_context"]
    root_path = report["kicad_root"]["path"]
    root = Path(root_path) if root_path else None

    if recommended == "CURRENT_PYTHON_WITH_DISCOVERED_PATHS" and root:
        prepare_current_process_for_kicad(root, candidate_python_paths(root))
        import pcbnew  # type: ignore

        return pcbnew

    kicad_python_path = report["kicad_python"]["path"]
    if report["pcbnew"]["kicad_python_available"] and kicad_python_path:
        script_path = Path(sys.argv[0]).resolve()
        env = os.environ.copy()
        env[REEXEC_ENV] = "1"
        completed = subprocess.run([kicad_python_path, str(script_path), *sys.argv[1:]], env=env)
        raise SystemExit(completed.returncode)

    raise RuntimeError(report["pcbnew"]["message"])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kicad-root", help="Optional KiCad install root override.")
    parser.add_argument("--require-pcbnew", action="store_true", help="Return non-zero if no KiCad-compatible pcbnew context is available.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payload = build_kicad_python_context(explicit_root=args.kicad_root)
    print(json.dumps(payload, indent=2))
    if args.require_pcbnew and not payload["pcbnew"]["available"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
