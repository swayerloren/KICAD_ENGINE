#!/usr/bin/env python3
"""Read-only deep inventory of an installed KiCad application folder.

The script writes JSON and Markdown reports into the selected output folder.
It never writes into the KiCad installation root.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import re
import shutil
import subprocess
from collections import Counter
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


THREE_D_SUFFIXES = {".step", ".stp", ".wrl", ".x3d", ".obj", ".iges", ".igs"}
EXECUTABLE_SUFFIXES = {".exe", ".bat", ".cmd", ".com", ""}


@dataclass
class FolderRecord:
    role: str
    path: str
    exists: bool
    file_count: int
    directory_count: int
    total_bytes: int
    extension_counts: dict[str, int]
    sample_children: list[str]


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def version_key(path: Path) -> tuple[int, ...]:
    parts = re.findall(r"\d+", path.name)
    return tuple(int(part) for part in parts) if parts else (0,)


def default_platform_name() -> str:
    system = platform.system().lower()
    if system.startswith("darwin"):
        return "macos"
    if system.startswith("windows"):
        return "windows"
    if system.startswith("linux"):
        return "linux"
    return system or "unknown"


def find_default_kicad_root() -> Path | None:
    if platform.system().lower().startswith("windows"):
        fixed = Path(r"C:\Program Files\KiCad\9.0")
        if fixed.exists():
            return fixed
        program_files = Path(os.environ.get("ProgramFiles", r"C:\Program Files"))
        kicad_root = program_files / "KiCad"
        if kicad_root.exists():
            candidates = [
                child
                for child in kicad_root.iterdir()
                if child.is_dir() and ((child / "bin" / "kicad-cli.exe").exists() or (child / "bin" / "kicad-cli").exists())
            ]
            if candidates:
                return sorted(candidates, key=version_key, reverse=True)[0]
    if platform.system().lower().startswith("darwin"):
        app = Path("/Applications/KiCad/KiCad.app")
        if app.exists():
            return app
    for candidate in [Path("/usr"), Path("/usr/local"), Path("/app")]:
        if (candidate / "bin" / "kicad-cli").exists() or (candidate / "share" / "kicad").exists():
            return candidate
    found = shutil.which("kicad-cli") or shutil.which("kicad-cli.exe")
    if found:
        cli = Path(found).resolve()
        if cli.parent.name in {"bin", "MacOS"}:
            if cli.parent.name == "MacOS":
                return cli.parents[1]
            return cli.parent.parent
    return None


def resolve_kicad_root(user_root: str | None) -> Path:
    if user_root:
        return Path(user_root).expanduser().resolve()
    detected = find_default_kicad_root()
    if detected:
        return detected.resolve()
    raise SystemExit("KiCad root not found. Supply --kicad-root.")


def candidate_paths(root: Path, *relative_paths: str) -> list[Path]:
    return [root / Path(rel) for rel in relative_paths]


def first_existing(paths: Iterable[Path]) -> Path | None:
    for path in paths:
        if path.exists():
            return path
    return None


def find_kicad_cli(root: Path) -> Path | None:
    candidates = candidate_paths(
        root,
        "bin/kicad-cli.exe",
        "bin/kicad-cli",
        "Contents/MacOS/kicad-cli",
        "usr/bin/kicad-cli",
    )
    found = first_existing(candidates)
    if found:
        return found
    on_path = shutil.which("kicad-cli") or shutil.which("kicad-cli.exe")
    return Path(on_path).resolve() if on_path else None


def find_bin_dir(root: Path) -> Path | None:
    return first_existing(candidate_paths(root, "bin", "Contents/MacOS", "usr/bin"))


def find_data_root(root: Path) -> Path | None:
    return first_existing(
        candidate_paths(
            root,
            "share/kicad",
            "share",
            "Contents/SharedSupport",
            "Contents/SharedSupport/kicad",
            "usr/share/kicad",
            "usr/share",
        )
    )


def find_resource_dir(root: Path, name: str) -> Path | None:
    candidates = candidate_paths(
        root,
        f"share/kicad/{name}",
        f"share/{name}",
        f"Contents/SharedSupport/{name}",
        f"Contents/SharedSupport/kicad/{name}",
        f"usr/share/kicad/{name}",
        f"usr/share/{name}",
    )
    return first_existing(candidates)


def count_files(path: Path, suffix: str | None = None) -> int:
    if not path or not path.exists():
        return 0
    if suffix is None:
        return sum(1 for item in path.rglob("*") if item.is_file())
    return sum(1 for item in path.rglob(f"*{suffix}") if item.is_file())


def count_dirs(path: Path, suffix: str | None = None) -> int:
    if not path or not path.exists():
        return 0
    if suffix is None:
        return sum(1 for item in path.rglob("*") if item.is_dir())
    return sum(1 for item in path.rglob(f"*{suffix}") if item.is_dir())


def folder_record(role: str, path: Path | None) -> FolderRecord:
    if path is None or not path.exists():
        return FolderRecord(
            role=role,
            path=str(path) if path else "",
            exists=False,
            file_count=0,
            directory_count=0,
            total_bytes=0,
            extension_counts={},
            sample_children=[],
        )
    file_count = 0
    directory_count = 0
    total_bytes = 0
    extensions: Counter[str] = Counter()
    samples: list[str] = []
    for item in path.rglob("*"):
        try:
            rel = item.relative_to(path).as_posix()
        except ValueError:
            rel = item.name
        if len(samples) < 40:
            samples.append(rel)
        if item.is_dir():
            directory_count += 1
            continue
        if item.is_file():
            file_count += 1
            try:
                total_bytes += item.stat().st_size
            except OSError:
                pass
            extensions[item.suffix.lower() or "<none>"] += 1
    return FolderRecord(
        role=role,
        path=str(path),
        exists=True,
        file_count=file_count,
        directory_count=directory_count,
        total_bytes=total_bytes,
        extension_counts=dict(extensions.most_common(40)),
        sample_children=samples,
    )


def run_command(args: list[str], timeout: int = 20) -> dict[str, object]:
    try:
        completed = subprocess.run(
            args,
            capture_output=True,
            text=True,
            errors="replace",
            timeout=timeout,
            check=False,
        )
        return {
            "command": args,
            "exit_code": completed.returncode,
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
        }
    except Exception as exc:  # noqa: BLE001 - reports should capture discovery failures.
        return {
            "command": args,
            "exit_code": None,
            "stdout": "",
            "stderr": f"{type(exc).__name__}: {exc}",
        }


def executable_inventory(root: Path, bin_dir: Path | None, kicad_cli: Path | None, run_cli_help: bool) -> dict[str, object]:
    files: list[dict[str, object]] = []
    dll_count = 0
    if bin_dir and bin_dir.exists():
        for item in sorted(bin_dir.iterdir(), key=lambda p: p.name.lower()):
            if not item.is_file():
                continue
            suffix = item.suffix.lower()
            if suffix == ".dll":
                dll_count += 1
            if suffix in EXECUTABLE_SUFFIXES or suffix in {".bat", ".cmd"}:
                files.append(
                    {
                        "name": item.name,
                        "path": str(item),
                        "suffix": suffix or "<none>",
                        "size_bytes": item.stat().st_size,
                        "role_hint": role_hint_for_executable(item.name),
                    }
                )
    command_behavior: dict[str, object] = {}
    if kicad_cli and kicad_cli.exists() and run_cli_help:
        cli = str(kicad_cli)
        command_behavior["version"] = run_command([cli, "version"])
        command_behavior["help"] = run_command([cli, "--help"])
        for subcommand in ["sch", "pcb", "fp", "sym", "jobset", "version"]:
            command_behavior[f"{subcommand}_help"] = run_command([cli, subcommand, "--help"])
    return {
        "schema_version": "1.0",
        "generated_at_utc": now_utc(),
        "kicad_root": str(root),
        "bin_dir": str(bin_dir) if bin_dir else "",
        "kicad_cli": str(kicad_cli) if kicad_cli else "",
        "dll_count": dll_count,
        "executables": files,
        "command_behavior": command_behavior,
    }


def role_hint_for_executable(name: str) -> str:
    lower = name.lower()
    hints = {
        "kicad.exe": "main KiCad project manager GUI",
        "kicad": "main KiCad project manager GUI",
        "kicad-cli.exe": "KiCad command-line automation entry point",
        "kicad-cli": "KiCad command-line automation entry point",
        "eeschema.exe": "schematic editor GUI",
        "eeschema": "schematic editor GUI",
        "pcbnew.exe": "PCB editor GUI",
        "pcbnew": "PCB editor GUI",
        "gerbview.exe": "Gerber viewer GUI",
        "gerbview": "Gerber viewer GUI",
        "bitmap2component.exe": "bitmap-to-component utility",
        "pcb_calculator.exe": "PCB calculator GUI",
        "pl_editor.exe": "page layout editor GUI",
        "python.exe": "bundled KiCad Python",
        "pythonw.exe": "bundled KiCad Python without console",
        "kicad-cmd.bat": "Windows KiCad command prompt environment helper",
    }
    return hints.get(lower, "runtime or helper executable")


def resource_summary(root: Path, data_root: Path | None) -> dict[str, object]:
    symbols = find_resource_dir(root, "symbols")
    footprints = find_resource_dir(root, "footprints")
    models = find_resource_dir(root, "3dmodels")
    template = find_resource_dir(root, "template")
    demos = find_resource_dir(root, "demos")
    scripting = find_resource_dir(root, "scripting")
    schemas = find_resource_dir(root, "schemas")
    resources = find_resource_dir(root, "resources")
    model_counts = Counter()
    if models and models.exists():
        for item in models.rglob("*"):
            if item.is_file() and item.suffix.lower() in THREE_D_SUFFIXES:
                model_counts[item.suffix.lower()] += 1
    summary = {
        "schema_version": "1.0",
        "generated_at_utc": now_utc(),
        "kicad_root": str(root),
        "data_root": str(data_root) if data_root else "",
        "symbols_dir": str(symbols) if symbols else "",
        "symbol_library_files": count_files(symbols, ".kicad_sym") if symbols else 0,
        "footprints_dir": str(footprints) if footprints else "",
        "footprint_library_dirs": count_dirs(footprints, ".pretty") if footprints else 0,
        "footprint_files": count_files(footprints, ".kicad_mod") if footprints else 0,
        "models_dir": str(models) if models else "",
        "model_library_dirs": count_dirs(models, ".3dshapes") if models else 0,
        "model_files": sum(model_counts.values()),
        "model_file_extensions": dict(sorted(model_counts.items())),
        "template_dir": str(template) if template else "",
        "template_dirs": sum(1 for item in template.iterdir() if item.is_dir()) if template and template.exists() else 0,
        "template_files": sum(1 for item in template.iterdir() if item.is_file()) if template and template.exists() else 0,
        "demos_dir": str(demos) if demos else "",
        "demo_dirs": sum(1 for item in demos.iterdir() if item.is_dir()) if demos and demos.exists() else 0,
        "scripting_dir": str(scripting) if scripting else "",
        "scripting_python_files": count_files(scripting, ".py") if scripting else 0,
        "schemas_dir": str(schemas) if schemas else "",
        "schema_files": count_files(schemas, ".json") if schemas else 0,
        "resources_dir": str(resources) if resources else "",
        "stock_sym_lib_table": str(template / "sym-lib-table") if template and (template / "sym-lib-table").exists() else "",
        "stock_fp_lib_table": str(template / "fp-lib-table") if template and (template / "fp-lib-table").exists() else "",
        "sample_symbol_libraries": sample_names(symbols, "*.kicad_sym", 40),
        "sample_footprint_libraries": sample_names(footprints, "*.pretty", 40),
        "sample_model_libraries": sample_names(models, "*.3dshapes", 40),
        "sample_templates": sample_top_level_dirs(template, 40),
        "sample_demos": sample_top_level_dirs(demos, 40),
    }
    return summary


def sample_names(path: Path | None, pattern: str, limit: int) -> list[str]:
    if not path or not path.exists():
        return []
    return [item.name for item in sorted(path.glob(pattern), key=lambda p: p.name.lower())[:limit]]


def sample_top_level_dirs(path: Path | None, limit: int) -> list[str]:
    if not path or not path.exists():
        return []
    return [item.name for item in sorted(path.iterdir(), key=lambda p: p.name.lower()) if item.is_dir()][:limit]


def folder_inventory(root: Path, bin_dir: Path | None, data_root: Path | None) -> dict[str, object]:
    folders = {
        "root": folder_record("install root", root),
        "bin": folder_record("executables and runtime DLLs", bin_dir),
        "share": folder_record("shared installed resources", root / "share"),
        "share_kicad_or_data_root": folder_record("KiCad stock libraries, templates, demos, scripts, schemas", data_root),
        "symbols": folder_record("stock symbol libraries", find_resource_dir(root, "symbols")),
        "footprints": folder_record("stock footprint libraries", find_resource_dir(root, "footprints")),
        "3dmodels": folder_record("stock 3D model libraries", find_resource_dir(root, "3dmodels")),
        "template": folder_record("stock project templates and library table templates", find_resource_dir(root, "template")),
        "demos": folder_record("installed demos and examples", find_resource_dir(root, "demos")),
        "scripting": folder_record("installed Python scripting helpers and footprint wizards", find_resource_dir(root, "scripting")),
        "schemas": folder_record("KiCad JSON schemas", find_resource_dir(root, "schemas")),
        "resources": folder_record("images and runtime resources", find_resource_dir(root, "resources")),
        "lib": folder_record("runtime/link libraries and ngspice code models", root / "lib"),
        "etc": folder_record("runtime configuration reference files", root / "etc"),
        "doc": folder_record("installed documentation", root / "share" / "doc"),
        "locale": folder_record("localization files", root / "share" / "locale"),
    }
    return {
        "schema_version": "1.0",
        "generated_at_utc": now_utc(),
        "kicad_root": str(root),
        "folders": {key: asdict(record) for key, record in folders.items()},
    }


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_markdown(path: Path, inventory: dict[str, object], executables: dict[str, object], resources: dict[str, object]) -> None:
    folders = inventory["folders"]
    lines = [
        "# Deep KiCad Folder Inventory",
        "",
        f"Generated UTC: `{inventory['generated_at_utc']}`",
        f"KiCad root: `{inventory['kicad_root']}`",
        "",
        "## Resource Counts",
        "",
        f"- Symbol library files: `{resources['symbol_library_files']}`",
        f"- Footprint library folders: `{resources['footprint_library_dirs']}`",
        f"- Footprint files: `{resources['footprint_files']}`",
        f"- 3D model library folders: `{resources['model_library_dirs']}`",
        f"- 3D model files: `{resources['model_files']}`",
        f"- Template folders: `{resources['template_dirs']}`",
        f"- Demo/example folders: `{resources['demo_dirs']}`",
        f"- Scripting Python files: `{resources['scripting_python_files']}`",
        "",
        "## Folder Summary",
        "",
        "| Key | Role | Exists | Files | Dirs | Path |",
        "| --- | --- | ---: | ---: | ---: | --- |",
    ]
    for key, record in folders.items():
        lines.append(
            f"| `{key}` | {record['role']} | {record['exists']} | {record['file_count']} | {record['directory_count']} | `{record['path']}` |"
        )
    lines.extend(
        [
            "",
            "## Executables",
            "",
            f"- KiCad CLI: `{executables.get('kicad_cli', '')}`",
            f"- Runtime DLL count: `{executables.get('dll_count', 0)}`",
            "",
            "| Name | Role | Size | Path |",
            "| --- | --- | ---: | --- |",
        ]
    )
    for item in executables.get("executables", []):
        lines.append(f"| `{item['name']}` | {item['role_hint']} | {item['size_bytes']} | `{item['path']}` |")
    lines.extend(
        [
            "",
            "## Command Behavior",
            "",
            "Only `kicad-cli` version/help discovery was run. No project commands, exports, ERC, or DRC were run by this inventory script.",
            "",
        ]
    )
    behavior = executables.get("command_behavior", {})
    for key, value in behavior.items():
        stdout = str(value.get("stdout", "")).replace("\r\n", "\n").strip()
        lines.append(f"### `{key}`")
        lines.append("")
        lines.append(f"Exit code: `{value.get('exit_code')}`")
        lines.append("")
        if stdout:
            lines.append("```text")
            lines.append(stdout[:4000])
            lines.append("```")
            lines.append("")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def assert_output_not_inside_kicad_root(output_dir: Path, kicad_root: Path) -> None:
    resolved_output = output_dir.resolve()
    resolved_root = kicad_root.resolve()
    if resolved_output == resolved_root or resolved_root in resolved_output.parents:
        raise SystemExit(f"Refusing to write reports inside the KiCad install root: {resolved_output}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kicad-root", help="Installed KiCad root path. Example: C:\\Program Files\\KiCad\\9.0")
    parser.add_argument(
        "--output-dir",
        default="03_TOOLS/kicad_app_intelligence/generated",
        help="Output folder for JSON and Markdown reports.",
    )
    parser.add_argument("--platform-name", default=default_platform_name(), help="Name used in output filenames.")
    parser.add_argument("--no-cli-help", action="store_true", help="Do not run kicad-cli version/help discovery.")
    args = parser.parse_args()

    root = resolve_kicad_root(args.kicad_root)
    if not root.exists():
        raise SystemExit(f"KiCad root does not exist: {root}")
    if root.is_file():
        raise SystemExit("This script inventories folders. For AppImage files, extract or mount first and pass that root.")

    output_dir = Path(args.output_dir).resolve()
    assert_output_not_inside_kicad_root(output_dir, root)
    kicad_cli = find_kicad_cli(root)
    bin_dir = find_bin_dir(root)
    data_root = find_data_root(root)

    inventory = folder_inventory(root, bin_dir, data_root)
    executables = executable_inventory(root, bin_dir, kicad_cli, run_cli_help=not args.no_cli_help)
    resources = resource_summary(root, data_root)

    platform_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", args.platform_name.lower())
    write_json(output_dir / f"kicad_folder_inventory.{platform_name}.json", inventory)
    write_json(output_dir / f"kicad_executables.{platform_name}.json", executables)
    write_json(output_dir / f"kicad_resource_summary.{platform_name}.json", resources)
    write_markdown(output_dir / f"kicad_folder_inventory.{platform_name}.md", inventory, executables, resources)

    print(f"KiCad root: {root}")
    print(f"KiCad CLI: {kicad_cli if kicad_cli else 'not found'}")
    print(f"Output dir: {output_dir}")
    print(f"Symbols: {resources['symbol_library_files']}")
    print(f"Footprint libraries: {resources['footprint_library_dirs']}")
    print(f"Footprints: {resources['footprint_files']}")
    print(f"3D model files: {resources['model_files']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
