#!/usr/bin/env python3
"""Read-only KiCad project validation for AI-assisted review.

This script does not edit KiCad source files. It parses project files and
library metadata, checks available validation paths, and writes Markdown/JSON
reports outside the project folder by default.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
DISCOVERY_DIR = SCRIPT_DIR.parent / "kicad_discovery"
if str(DISCOVERY_DIR) not in sys.path:
    sys.path.insert(0, str(DISCOVERY_DIR))

try:
    from find_kicad import detect_kicad_environment  # type: ignore
except Exception:  # noqa: BLE001
    detect_kicad_environment = None


STATUS_RANK = {"PASS": 0, "WARN": 1, "FAIL": 2}
CHECK_IDS = [
    "project_files",
    "project_libraries",
    "missing_footprints",
    "missing_3d_models",
    "cli_availability",
    "unconnected_power",
    "bom_datasheets",
    "component_database_matches",
    "connector_orientation",
    "polarity_review",
    "rf_layout_review",
    "interface_rule_review",
]


@dataclass
class ProjectContext:
    repo_root: Path
    project_input: Path
    project_dir: Path | None
    project_file: Path | None
    project_name: str
    schematic_files: list[Path]
    pcb_files: list[Path]
    main_schematic: Path | None
    main_pcb: Path | None
    kicad_cli: Path | None
    kicad_root: Path | None
    kicad_version: str
    output_dir: Path
    component_db_root: Path
    datasheet_root: Path


def repo_root() -> Path:
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "AGENTS.md").exists():
            return parent
    return Path.cwd().resolve()


def now_stamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_markdown(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def is_relative_to(path: Path, base: Path) -> bool:
    try:
        path.resolve().relative_to(base.resolve())
        return True
    except ValueError:
        return False


def safe_output_dir(output_dir: Path, project_dir: Path | None, allow_project_output: bool) -> Path:
    resolved = output_dir.resolve()
    if project_dir and is_relative_to(resolved, project_dir) and not allow_project_output:
        raise SystemExit(f"Refusing to write validation output inside project folder: {resolved}")
    resolved.mkdir(parents=True, exist_ok=True)
    return resolved


def detect_kicad_cli(explicit: str | None = None, explicit_root: str | None = None) -> Path | None:
    if detect_kicad_environment is not None:
        try:
            payload = detect_kicad_environment(explicit_root=explicit_root, explicit_cli=explicit, probe_pcbnew=False)
            detected = payload.get("kicad_cli", {}).get("path")
            if detected:
                return Path(detected).resolve()
        except Exception:
            pass
    candidates: list[Path] = []
    if explicit:
        candidates.append(Path(explicit))
    env_cli = os.environ.get("KICAD_CLI")
    if env_cli:
        candidates.append(Path(env_cli))
    install_root = Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "KiCad"
    if install_root.exists():
        for child in sorted(install_root.iterdir(), key=lambda p: p.name, reverse=True):
            candidates.append(child / "bin" / "kicad-cli.exe")
    found = shutil.which("kicad-cli") or shutil.which("kicad-cli.exe")
    if found:
        candidates.append(Path(found))
    for candidate in candidates:
        if candidate.exists() and candidate.is_file():
            return candidate.resolve()
    return None


def detect_kicad_root(explicit_root: str | None = None, explicit_cli: str | None = None) -> Path | None:
    if detect_kicad_environment is not None:
        try:
            payload = detect_kicad_environment(explicit_root=explicit_root, explicit_cli=explicit_cli, probe_pcbnew=False)
            detected = payload.get("kicad_root", {}).get("path")
            if detected:
                return Path(detected).resolve()
        except Exception:
            pass
    return None


def kicad_root_from_cli(kicad_cli: Path | None) -> Path | None:
    if not kicad_cli:
        return None
    try:
        return kicad_cli.parent.parent.resolve()
    except OSError:
        return None


def detect_kicad_version(kicad_root: Path | None) -> str:
    if not kicad_root:
        return "9.0"
    name = kicad_root.name
    if re.match(r"^\d+\.\d+$", name):
        return name
    return "9.0"


def run_kicad_version(kicad_cli: Path | None) -> dict[str, Any]:
    if not kicad_cli:
        return {"available": False, "path": None, "version_output": "", "error": "kicad-cli not found"}
    try:
        completed = subprocess.run(
            [str(kicad_cli), "version"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=20,
            check=False,
        )
        return {
            "available": completed.returncode == 0,
            "path": str(kicad_cli),
            "exit_code": completed.returncode,
            "version_output": (completed.stdout or completed.stderr).strip(),
            "error": "" if completed.returncode == 0 else (completed.stderr or completed.stdout).strip(),
        }
    except Exception as exc:  # noqa: BLE001
        return {"available": False, "path": str(kicad_cli), "version_output": "", "error": str(exc)}


def resolve_project(input_path: Path) -> tuple[Path | None, Path | None, list[Path], list[Path], Path | None, Path | None, list[str]]:
    warnings: list[str] = []
    if not input_path.exists():
        return None, None, [], [], None, None, [f"Project path does not exist: {input_path}"]

    if input_path.is_file() and input_path.suffix == ".kicad_pro":
        project_dir = input_path.parent.resolve()
        project_file = input_path.resolve()
    elif input_path.is_dir():
        project_dir = input_path.resolve()
        project_files = sorted(project_dir.glob("*.kicad_pro"))
        if not project_files:
            return project_dir, None, [], [], None, None, [f"No .kicad_pro file found in {project_dir}"]
        if len(project_files) > 1:
            warnings.append("Multiple .kicad_pro files found; using the first sorted path.")
        project_file = project_files[0].resolve()
    else:
        return None, None, [], [], None, None, [f"Project input is not a .kicad_pro file or directory: {input_path}"]

    stem = project_file.stem if project_file else ""
    schematic_files = sorted(project_dir.glob("*.kicad_sch")) if project_dir else []
    pcb_files = sorted(project_dir.glob("*.kicad_pcb")) if project_dir else []
    main_schematic = project_dir / f"{stem}.kicad_sch" if project_dir and (project_dir / f"{stem}.kicad_sch").exists() else (schematic_files[0] if schematic_files else None)
    main_pcb = project_dir / f"{stem}.kicad_pcb" if project_dir and (project_dir / f"{stem}.kicad_pcb").exists() else (pcb_files[0] if pcb_files else None)
    return project_dir, project_file, schematic_files, pcb_files, main_schematic, main_pcb, warnings


def make_context(args: argparse.Namespace) -> tuple[ProjectContext, list[str]]:
    root = repo_root()
    project_input = Path(args.project).resolve()
    project_dir, project_file, schematics, pcbs, main_sch, main_pcb, warnings = resolve_project(project_input)
    project_name = project_file.stem if project_file else project_input.stem
    kicad_cli = detect_kicad_cli(args.kicad_cli, args.kicad_root)
    kicad_root = detect_kicad_root(args.kicad_root, args.kicad_cli) or kicad_root_from_cli(kicad_cli)
    kicad_version = args.kicad_version or detect_kicad_version(kicad_root)
    default_output = root / "05_OUTPUTS" / "project_validation" / f"{now_stamp()}_{safe_name(project_name)}"
    output_dir = safe_output_dir(Path(args.output_dir).resolve() if args.output_dir else default_output, project_dir, args.allow_project_output)
    return (
        ProjectContext(
            repo_root=root,
            project_input=project_input,
            project_dir=project_dir,
            project_file=project_file,
            project_name=project_name,
            schematic_files=schematics,
            pcb_files=pcbs,
            main_schematic=main_sch,
            main_pcb=main_pcb,
            kicad_cli=kicad_cli,
            kicad_root=kicad_root,
            kicad_version=kicad_version,
            output_dir=output_dir,
            component_db_root=Path(args.component_db_root).resolve() if args.component_db_root else root / "08_COMPONENT_DATABASE",
            datasheet_root=Path(args.datasheet_root).resolve() if args.datasheet_root else root / "06_DATASHEETS",
        ),
        warnings,
    )


def safe_name(value: str) -> str:
    name = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("_")
    return name or "project"


def result(check_id: str, title: str, status: str, summary: str, details: list[Any] | None = None, next_steps: list[str] | None = None) -> dict[str, Any]:
    return {
        "check_id": check_id,
        "title": title,
        "status": status,
        "summary": summary,
        "details": details or [],
        "recommended_next_steps": next_steps or [],
    }


def split_lib_id(value: str) -> tuple[str, str]:
    if ":" not in value:
        return "", value
    left, right = value.split(":", 1)
    return left, right


def extract_balanced_block(text: str, start: int) -> str:
    depth = 0
    in_string = False
    escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == "\"":
                in_string = False
            continue
        if char == "\"":
            in_string = True
        elif char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return text[start : index + 1]
    return text[start:]


PROPERTY_RE = re.compile(r"\(property\s+\"([^\"]+)\"\s+\"([^\"]*)\"")
LIB_ID_RE = re.compile(r"\(lib_id\s+\"([^\"]+)\"")


def parse_schematic_symbols(files: list[Path]) -> list[dict[str, Any]]:
    symbols: list[dict[str, Any]] = []
    for path in files:
        text = read_text(path)
        for match in re.finditer(r"\(\s*symbol\b", text):
            block = extract_balanced_block(text, match.start())
            lib_id_match = LIB_ID_RE.search(block)
            if not lib_id_match:
                continue
            props = {p.group(1): p.group(2) for p in PROPERTY_RE.finditer(block)}
            lib_id = lib_id_match.group(1)
            lib, symbol = split_lib_id(lib_id)
            symbols.append(
                {
                    "file": str(path),
                    "lib_id": lib_id,
                    "library": lib,
                    "symbol": symbol,
                    "reference": props.get("Reference", ""),
                    "value": props.get("Value", ""),
                    "footprint": props.get("Footprint", ""),
                    "datasheet": props.get("Datasheet", ""),
                    "in_bom": "in_bom yes" in block,
                    "on_board": "on_board yes" in block,
                    "exclude_from_bom": "in_bom no" in block,
                    "raw_properties": props,
                }
            )
    return symbols


def parse_pcb_footprints(path: Path | None) -> list[dict[str, Any]]:
    if not path or not path.exists():
        return []
    text = read_text(path)
    footprints: list[dict[str, Any]] = []
    for match in re.finditer(r"\(\s*footprint\s+\"([^\"]+)\"", text):
        block = extract_balanced_block(text, match.start())
        footprint_id = match.group(1)
        lib, footprint = split_lib_id(footprint_id)
        props = {p.group(1): p.group(2) for p in PROPERTY_RE.finditer(block)}
        models = re.findall(r"\(model\s+\"([^\"]+)\"", block)
        pad_names = re.findall(r"\(pad\s+\"?([^\"\s\)]+)\"?", block)
        layer_match = re.search(r"\(layer\s+\"?([^\"\s\)]+)\"?", block)
        footprints.append(
            {
                "file": str(path),
                "footprint_id": footprint_id,
                "library": lib,
                "footprint": footprint,
                "reference": props.get("Reference", ""),
                "value": props.get("Value", ""),
                "layer": layer_match.group(1) if layer_match else "",
                "pad_count": len(pad_names),
                "pad_names_sample": sorted(set(pad_names))[:80],
                "model_paths": models,
            }
        )
    return footprints


def parse_lib_table(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    text = read_text(path)
    entries: list[dict[str, str]] = []
    pattern = re.compile(
        r'\(lib\s+\(name\s+(?:"([^"]+)"|([^\s\)]+))\).*?\(uri\s+(?:"([^"]+)"|([^\s\)]+))\)',
        re.S,
    )
    for match in pattern.finditer(text):
        name = match.group(1) or match.group(2)
        uri = match.group(3) or match.group(4)
        entries.append({"name": name, "uri": uri, "table": str(path)})
    return entries


def variable_map(ctx: ProjectContext) -> dict[str, str]:
    project_dir = ctx.project_dir or Path.cwd()
    mapping = {
        "KIPRJMOD": str(project_dir),
    }
    if ctx.kicad_root:
        share = ctx.kicad_root / "share" / "kicad"
        mapping.update(
            {
                "KICAD9_SYMBOL_DIR": str(share / "symbols"),
                "KICAD9_FOOTPRINT_DIR": str(share / "footprints"),
                "KICAD9_3DMODEL_DIR": str(share / "3dmodels"),
                "KICAD_SYMBOL_DIR": str(share / "symbols"),
                "KICAD_FOOTPRINT_DIR": str(share / "footprints"),
                "KICAD_3DMODEL_DIR": str(share / "3dmodels"),
            }
        )
    for key in (
        "KICAD9_SYMBOL_DIR",
        "KICAD9_FOOTPRINT_DIR",
        "KICAD9_3DMODEL_DIR",
        "KICAD_SYMBOL_DIR",
        "KICAD_FOOTPRINT_DIR",
        "KICAD_3DMODEL_DIR",
    ):
        value = os.environ.get(key)
        if value:
            mapping[key] = value
    return mapping


def resolve_uri(uri: str, ctx: ProjectContext) -> Path | None:
    resolved = uri
    for key, value in variable_map(ctx).items():
        resolved = resolved.replace("${" + key + "}", value)
    resolved = os.path.expandvars(resolved)
    if "${" in resolved:
        return None
    path = Path(resolved)
    if not path.is_absolute() and ctx.project_dir:
        path = ctx.project_dir / path
    return path.resolve()


def library_tables(ctx: ProjectContext) -> dict[str, Any]:
    project_dir = ctx.project_dir
    share = ctx.kicad_root / "share" / "kicad" if ctx.kicad_root else None
    appdata = os.environ.get("APPDATA")
    user_root = Path(appdata) / "kicad" / ctx.kicad_version if appdata else Path.home() / "AppData" / "Roaming" / "kicad" / ctx.kicad_version
    paths = {
        "project_sym": project_dir / "sym-lib-table" if project_dir else None,
        "project_fp": project_dir / "fp-lib-table" if project_dir else None,
        "project_design_block": project_dir / "design-block-lib-table" if project_dir else None,
        "user_sym": user_root / "sym-lib-table",
        "user_fp": user_root / "fp-lib-table",
        "user_design_block": user_root / "design-block-lib-table",
        "stock_sym": share / "template" / "sym-lib-table" if share else None,
        "stock_fp": share / "template" / "fp-lib-table" if share else None,
    }
    sym_entries = []
    fp_entries = []
    for key in ("project_sym", "user_sym", "stock_sym"):
        path = paths[key]
        if path:
            sym_entries.extend(parse_lib_table(path))
    for key in ("project_fp", "user_fp", "stock_fp"):
        path = paths[key]
        if path:
            fp_entries.extend(parse_lib_table(path))
    return {"paths": paths, "sym_entries": sym_entries, "fp_entries": fp_entries}


def entry_map(entries: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    mapped: dict[str, dict[str, str]] = {}
    for entry in entries:
        mapped.setdefault(entry["name"], entry)
    return mapped


def check_project_files(ctx: ProjectContext, startup_warnings: list[str]) -> dict[str, Any]:
    details = list(startup_warnings)
    status = "PASS"
    if not ctx.project_file:
        status = "FAIL"
    elif not ctx.main_schematic:
        status = "FAIL"
    elif not ctx.main_pcb:
        status = "WARN"
    details.extend(
        [
            {"project_input": str(ctx.project_input)},
            {"project_dir": str(ctx.project_dir) if ctx.project_dir else None},
            {"project_file": str(ctx.project_file) if ctx.project_file else None},
            {"schematic_files": [str(p) for p in ctx.schematic_files]},
            {"pcb_files": [str(p) for p in ctx.pcb_files]},
        ]
    )
    next_steps = []
    if not ctx.project_file:
        next_steps.append("Point the validator at a folder containing one .kicad_pro file or at an explicit .kicad_pro file.")
    if not ctx.main_schematic:
        next_steps.append("Confirm the main schematic exists before running ERC or BOM checks.")
    if not ctx.main_pcb:
        next_steps.append("Confirm whether this is schematic-only or create/locate the PCB before DRC and footprint placement checks.")
    return result("project_files", "Project File Presence", status, "Checked project, schematic, and PCB source file presence.", details, next_steps)


def check_project_libraries(ctx: ProjectContext, symbols: list[dict[str, Any]]) -> dict[str, Any]:
    tables = library_tables(ctx)
    sym_map = entry_map(tables["sym_entries"])
    used_libs = sorted({s["library"] for s in symbols if s.get("library")})
    missing_used = [lib for lib in used_libs if lib not in sym_map]
    unresolved_entries = []
    for entry in tables["sym_entries"]:
        resolved = resolve_uri(entry["uri"], ctx)
        if resolved is None or not resolved.exists():
            unresolved_entries.append({**entry, "resolved_path": str(resolved) if resolved else "Unresolved variable"})

    project_local = []
    for key in ("project_sym", "project_fp", "project_design_block"):
        path = tables["paths"].get(key)
        project_local.append({"table": key, "path": str(path) if path else None, "exists": bool(path and path.exists())})

    status = "PASS"
    if missing_used:
        status = "FAIL"
    elif unresolved_entries or not any(row["exists"] for row in project_local):
        status = "WARN"

    details = [
        {"project_local_tables": project_local},
        {"symbol_libraries_used": used_libs},
        {"missing_symbol_libraries_used": missing_used},
        {"unresolved_symbol_table_entries": unresolved_entries[:100]},
    ]
    next_steps = []
    if missing_used:
        next_steps.append("Resolve missing symbol library nicknames through project-local, user-global, or stock library tables before editing.")
    if unresolved_entries:
        next_steps.append("Document unresolved symbol library table URIs; do not patch global tables automatically unless the user requests it.")
    if status == "WARN":
        next_steps.append("Consider project-local library tables for reproducible projects that should not depend silently on global config.")
    return result("project_libraries", "Project Library Tables And Symbol Libraries", status, "Checked project-local tables and symbol library resolution.", details, next_steps)


def check_missing_footprints(ctx: ProjectContext, symbols: list[dict[str, Any]], pcb_footprints: list[dict[str, Any]]) -> dict[str, Any]:
    tables = library_tables(ctx)
    fp_map = entry_map(tables["fp_entries"])
    assignments = []
    for sym in symbols:
        fp = sym.get("footprint") or ""
        if fp and fp != "~":
            lib, name = split_lib_id(fp)
            assignments.append({"source": "schematic", "reference": sym.get("reference"), "footprint_id": fp, "library": lib, "footprint": name})
    for fp in pcb_footprints:
        assignments.append({"source": "pcb", "reference": fp.get("reference"), "footprint_id": fp.get("footprint_id"), "library": fp.get("library"), "footprint": fp.get("footprint")})

    unresolved_libraries = []
    missing_files = []
    unresolved_table_entries = []
    for entry in tables["fp_entries"]:
        resolved = resolve_uri(entry["uri"], ctx)
        if resolved is None or not resolved.exists():
            unresolved_table_entries.append({**entry, "resolved_path": str(resolved) if resolved else "Unresolved variable"})
    for item in assignments:
        lib = item.get("library") or ""
        footprint = item.get("footprint") or ""
        if not lib or not footprint:
            continue
        entry = fp_map.get(lib)
        if not entry:
            unresolved_libraries.append(item)
            continue
        lib_path = resolve_uri(entry["uri"], ctx)
        if not lib_path or not lib_path.exists():
            unresolved_libraries.append({**item, "library_uri": entry["uri"]})
            continue
        candidate = lib_path / f"{footprint}.kicad_mod"
        if not candidate.exists():
            missing_files.append({**item, "expected_path": str(candidate)})

    status = "PASS"
    if unresolved_libraries or missing_files:
        status = "FAIL"
    elif unresolved_table_entries or not assignments:
        status = "WARN"
    next_steps = []
    if unresolved_libraries:
        next_steps.append("Resolve missing footprint library nicknames before layout or manufacturing review.")
    if missing_files:
        next_steps.append("Verify footprint names and project/global footprint tables; do not auto-reassign footprints.")
    if not assignments:
        next_steps.append("No footprint assignments were found; export/check BOM and schematic properties before PCB work.")
    details = [
        {"footprint_assignments_checked": len(assignments)},
        {"unresolved_footprint_libraries": unresolved_libraries[:100]},
        {"missing_footprint_files": missing_files[:100]},
        {"unresolved_footprint_table_entries": unresolved_table_entries[:100]},
    ]
    return result("missing_footprints", "Missing Footprint Libraries Or Footprints", status, "Checked footprint libraries and assigned footprint files.", details, next_steps)


def check_missing_3d_models(ctx: ProjectContext, pcb_footprints: list[dict[str, Any]]) -> dict[str, Any]:
    model_refs = []
    missing = []
    unresolved = []
    for fp in pcb_footprints:
        for model in fp.get("model_paths", []):
            resolved = resolve_uri(model, ctx)
            row = {"reference": fp.get("reference"), "footprint_id": fp.get("footprint_id"), "model": model, "resolved_path": str(resolved) if resolved else None}
            model_refs.append(row)
            if resolved is None:
                unresolved.append(row)
            elif not resolved.exists():
                missing.append(row)
    status = "PASS"
    if missing:
        status = "FAIL"
    elif unresolved or not model_refs:
        status = "WARN"
    next_steps = []
    if missing:
        next_steps.append("Resolve missing 3D model files or document why mechanical review does not depend on them.")
    if unresolved:
        next_steps.append("Resolve unknown 3D model variables before relying on visual/mechanical review.")
    if not model_refs:
        next_steps.append("No PCB 3D model references were found; mechanical review may be incomplete.")
    return result(
        "missing_3d_models",
        "Missing 3D Models",
        status,
        "Checked 3D model references in the PCB.",
        [{"model_references_checked": len(model_refs)}, {"missing_models": missing[:100]}, {"unresolved_model_paths": unresolved[:100]}],
        next_steps,
    )


def check_cli_availability(ctx: ProjectContext, cli_info: dict[str, Any]) -> dict[str, Any]:
    checks = {
        "kicad_cli": cli_info,
        "erc_available": bool(cli_info.get("available") and ctx.main_schematic),
        "drc_available": bool(cli_info.get("available") and ctx.main_pcb),
        "bom_export_available": bool(cli_info.get("available") and ctx.main_schematic),
        "erc_wrapper": str(ctx.repo_root / "03_TOOLS" / "scripts" / "run_erc.ps1"),
        "drc_wrapper": str(ctx.repo_root / "03_TOOLS" / "scripts" / "run_drc.ps1"),
        "bom_wrapper": str(ctx.repo_root / "03_TOOLS" / "scripts" / "export_bom.ps1"),
    }
    status = "PASS" if checks["erc_available"] and checks["drc_available"] and checks["bom_export_available"] else "WARN"
    if not cli_info.get("available"):
        status = "FAIL"
    next_steps = []
    if not cli_info.get("available"):
        next_steps.append("Install or locate kicad-cli, or pass --kicad-cli to the validator.")
    if not checks["erc_available"]:
        next_steps.append("ERC is not available until kicad-cli and a schematic are available.")
    if not checks["drc_available"]:
        next_steps.append("DRC is not available until kicad-cli and a PCB are available.")
    if not checks["bom_export_available"]:
        next_steps.append("BOM export is not available until kicad-cli and a schematic are available.")
    return result("cli_availability", "ERC, DRC, And BOM Export Availability", status, "Checked whether standard KiCad CLI validation/export commands can be run.", [checks], next_steps)


def check_unconnected_power(ctx: ProjectContext, symbols: list[dict[str, Any]]) -> dict[str, Any]:
    power_symbols = [s for s in symbols if s.get("library", "").lower() == "power" or s.get("lib_id", "").lower().startswith("power:")]
    pwr_flags = [s for s in power_symbols if "pwr_flag" in (s.get("symbol", "") + s.get("value", "")).lower()]
    no_connect_count = 0
    for path in ctx.schematic_files:
        no_connect_count += len(re.findall(r"\(\s*no_connect\b", read_text(path)))
    status = "WARN"
    if not ctx.main_schematic:
        status = "FAIL"
    elif power_symbols and pwr_flags:
        status = "PASS"
    next_steps = [
        "Run ERC before trusting power connectivity; static text inspection cannot prove every power pin is driven.",
        "Review hidden power pins and PWR_FLAG placement manually for regulators, connectors, and MCU power rails.",
    ]
    details = [
        {"power_symbols_found": len(power_symbols)},
        {"pwr_flags_found": len(pwr_flags)},
        {"no_connect_markers_found": no_connect_count},
        {"sample_power_symbols": power_symbols[:50]},
    ]
    return result("unconnected_power", "Unconnected Power Review", status, "Performed static power-symbol and no-connect inventory; ERC is still required.", details, next_steps)


def normalize(value: str) -> str:
    return re.sub(r"[^A-Z0-9]+", "", value.upper())


def load_component_database(root: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    if not root.exists():
        return records
    for path in sorted(root.rglob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        items = data if isinstance(data, list) else data.get("records", []) if isinstance(data, dict) else []
        for item in items:
            if isinstance(item, dict):
                item = dict(item)
                item["_source_file"] = str(path)
                records.append(item)
    return records


def component_matches(value: str, records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    target = normalize(value)
    if len(target) < 3:
        return []
    matches = []
    for record in records:
        part = normalize(str(record.get("part_number", "")))
        record_id = normalize(str(record.get("record_id", "")))
        if not part and not record_id:
            continue
        if target == part or target == record_id or (len(part) >= 5 and part in target) or (len(target) >= 5 and target in part):
            matches.append(record)
    return matches[:10]


def local_datasheet_hits(value: str, datasheet_root: Path) -> list[str]:
    target = normalize(value)
    if len(target) < 5 or not datasheet_root.exists():
        return []
    hits = []
    for path in datasheet_root.rglob("*"):
        if not path.is_file():
            continue
        if target in normalize(path.name):
            hits.append(str(path))
            if len(hits) >= 10:
                break
    return hits


def bom_relevant(symbol: dict[str, Any]) -> bool:
    ref = symbol.get("reference", "")
    if not ref or ref.startswith("#"):
        return False
    if symbol.get("exclude_from_bom"):
        return False
    return True


def check_bom_has_datasheets(ctx: ProjectContext, symbols: list[dict[str, Any]], records: list[dict[str, Any]]) -> dict[str, Any]:
    missing = []
    with_datasheet = 0
    for sym in symbols:
        if not bom_relevant(sym):
            continue
        value = sym.get("value", "")
        datasheet = sym.get("datasheet", "")
        matches = component_matches(value, records)
        local_hits = local_datasheet_hits(value, ctx.datasheet_root)
        has_data = bool(datasheet and datasheet != "~") or bool(matches) or bool(local_hits)
        if has_data:
            with_datasheet += 1
        else:
            missing.append({"reference": sym.get("reference"), "value": value, "footprint": sym.get("footprint"), "library": sym.get("library")})
    status = "PASS" if not missing else "WARN"
    if not ctx.main_schematic:
        status = "FAIL"
    next_steps = []
    if missing:
        next_steps.append("Add source links, component database records, or local datasheet references for BOM components before release.")
    return result(
        "bom_datasheets",
        "BOM Datasheet Coverage",
        status,
        "Checked schematic components for datasheet fields, component database matches, or local datasheet filename hits.",
        [{"components_with_datasheet_evidence": with_datasheet}, {"components_missing_datasheet_evidence": missing[:200]}],
        next_steps,
    )


def check_component_database_matches(ctx: ProjectContext, symbols: list[dict[str, Any]], records: list[dict[str, Any]]) -> dict[str, Any]:
    matched = []
    unmatched = []
    for sym in symbols:
        if not bom_relevant(sym):
            continue
        value = sym.get("value", "")
        matches = component_matches(value, records)
        if matches:
            matched.append(
                {
                    "reference": sym.get("reference"),
                    "value": value,
                    "matches": [
                        {
                            "record_id": m.get("record_id"),
                            "part_number": m.get("part_number"),
                            "verified_status": m.get("verified_status"),
                            "source_file": m.get("_source_file"),
                        }
                        for m in matches
                    ],
                }
            )
        else:
            unmatched.append({"reference": sym.get("reference"), "value": value, "footprint": sym.get("footprint")})
    status = "PASS" if not unmatched else "WARN"
    next_steps = []
    if unmatched:
        next_steps.append("Create or update component database records for unmatched BOM values before relying on AI part intelligence.")
    return result(
        "component_database_matches",
        "Component Database Matches",
        status,
        f"Matched {len(matched)} schematic components against {len(records)} component database records.",
        [{"matched_components": matched[:200]}, {"unmatched_components": unmatched[:200]}],
        next_steps,
    )


CONNECTOR_KEYWORDS = ["connector", "conn", "usb", "jst", "molex", "header", "terminal", "barrel", "ufl", "u.fl", "sma", "harness", "automotive", "jack"]
POLARITY_KEYWORDS = ["diode", "led", "tvs", "zener", "bridge", "battery", "polar", "electrolytic", "tantalum", "mosfet", "transistor"]
RF_KEYWORDS = ["rf", "antenna", "ant", "u.fl", "ufl", "sma", "esp32", "wifi", "wi-fi", "bluetooth", "ble", "lora", "gnss", "radio", "nrf"]
USB_CAN_AUTO_KEYWORDS = ["usb", "type-c", "type c", "can", "canfd", "can-fd", "lin", "automotive", "12v", "load dump", "obd"]


def item_text(item: dict[str, Any]) -> str:
    return " ".join(str(item.get(k, "")) for k in ("reference", "value", "footprint", "footprint_id", "lib_id", "library", "symbol")).lower()


def check_keyword_review(check_id: str, title: str, symbols: list[dict[str, Any]], pcb_footprints: list[dict[str, Any]], keywords: list[str], warning: str, next_step: str) -> dict[str, Any]:
    hits = []
    for item in symbols + pcb_footprints:
        text = item_text(item)
        matched = [kw for kw in keywords if kw in text]
        ref = item.get("reference", "")
        if matched and ref and not ref.startswith("#"):
            hits.append({"reference": ref, "value": item.get("value", ""), "footprint": item.get("footprint") or item.get("footprint_id", ""), "matched_keywords": matched})
    dedup = {}
    for hit in hits:
        dedup.setdefault((hit["reference"], hit["value"], hit["footprint"]), hit)
    hits = list(dedup.values())
    status = "WARN" if hits else "PASS"
    return result(check_id, title, status, warning if hits else "No static keyword review hits found.", hits[:200], [next_step] if hits else [])


def check_connector_orientation(symbols: list[dict[str, Any]], pcb_footprints: list[dict[str, Any]]) -> dict[str, Any]:
    return check_keyword_review(
        "connector_orientation",
        "Connector Orientation Review Needed",
        symbols,
        pcb_footprints,
        CONNECTOR_KEYWORDS,
        "Connector-like components require human pinout, mating, orientation, and mechanical review.",
        "Review every listed connector against exact manufacturer drawing, mating connector, pin 1, and cable exit direction.",
    )


def check_polarity_review(symbols: list[dict[str, Any]], pcb_footprints: list[dict[str, Any]]) -> dict[str, Any]:
    return check_keyword_review(
        "polarity_review",
        "Polarity-Sensitive Parts Review Needed",
        symbols,
        pcb_footprints,
        POLARITY_KEYWORDS,
        "Polarity-sensitive components require human orientation and assembly review.",
        "Review polarity marks, pin 1/cathode/anode/source-drain orientation, and silkscreen for every listed item.",
    )


def check_rf_layout_review(symbols: list[dict[str, Any]], pcb_footprints: list[dict[str, Any]]) -> dict[str, Any]:
    return check_keyword_review(
        "rf_layout_review",
        "RF Layout Review Needed",
        symbols,
        pcb_footprints,
        RF_KEYWORDS,
        "RF-like components require controlled impedance, keepout, antenna, and mechanical review.",
        "Review RF feedline geometry, antenna keepout, stackup, connector orientation, and matching network before release.",
    )


def check_interface_rule_review(symbols: list[dict[str, Any]], pcb_footprints: list[dict[str, Any]], ctx: ProjectContext) -> dict[str, Any]:
    hits_result = check_keyword_review(
        "interface_rule_review",
        "USB/CAN/Automotive Rule Review Needed",
        symbols,
        pcb_footprints,
        USB_CAN_AUTO_KEYWORDS,
        "USB, CAN, LIN, or automotive-like items require protocol-specific review.",
        "Apply USB, CAN/LIN, and automotive power/protection rules from the component database before release.",
    )
    pcb_text = read_text(ctx.main_pcb).lower() if ctx.main_pcb and ctx.main_pcb.exists() else ""
    schematic_text = "\n".join(read_text(p).lower() for p in ctx.schematic_files if p.exists())
    net_hits = sorted({kw for kw in USB_CAN_AUTO_KEYWORDS if kw in pcb_text or kw in schematic_text})
    if net_hits:
        hits_result["status"] = "WARN"
        hits_result["details"].append({"net_or_text_keyword_hits": net_hits})
    return hits_result


def run_checks(ctx: ProjectContext, selected: list[str], startup_warnings: list[str]) -> dict[str, Any]:
    symbols = parse_schematic_symbols(ctx.schematic_files)
    pcb_footprints = parse_pcb_footprints(ctx.main_pcb)
    records = load_component_database(ctx.component_db_root)
    cli_info = run_kicad_version(ctx.kicad_cli)
    output_results: list[dict[str, Any]] = []
    selected_set = set(selected)

    def enabled(check_id: str) -> bool:
        return check_id in selected_set

    if enabled("project_files"):
        output_results.append(check_project_files(ctx, startup_warnings))
    if enabled("project_libraries"):
        output_results.append(check_project_libraries(ctx, symbols))
    if enabled("missing_footprints"):
        output_results.append(check_missing_footprints(ctx, symbols, pcb_footprints))
    if enabled("missing_3d_models"):
        output_results.append(check_missing_3d_models(ctx, pcb_footprints))
    if enabled("cli_availability"):
        output_results.append(check_cli_availability(ctx, cli_info))
    if enabled("unconnected_power"):
        output_results.append(check_unconnected_power(ctx, symbols))
    if enabled("bom_datasheets"):
        output_results.append(check_bom_has_datasheets(ctx, symbols, records))
    if enabled("component_database_matches"):
        output_results.append(check_component_database_matches(ctx, symbols, records))
    if enabled("connector_orientation"):
        output_results.append(check_connector_orientation(symbols, pcb_footprints))
    if enabled("polarity_review"):
        output_results.append(check_polarity_review(symbols, pcb_footprints))
    if enabled("rf_layout_review"):
        output_results.append(check_rf_layout_review(symbols, pcb_footprints))
    if enabled("interface_rule_review"):
        output_results.append(check_interface_rule_review(symbols, pcb_footprints, ctx))

    overall = "PASS"
    for item in output_results:
        if STATUS_RANK[item["status"]] > STATUS_RANK[overall]:
            overall = item["status"]
    summary = {
        "PASS": sum(1 for item in output_results if item["status"] == "PASS"),
        "WARN": sum(1 for item in output_results if item["status"] == "WARN"),
        "FAIL": sum(1 for item in output_results if item["status"] == "FAIL"),
    }
    next_steps = []
    for item in output_results:
        for step in item.get("recommended_next_steps", []):
            if step not in next_steps:
                next_steps.append(step)
    if overall != "PASS":
        next_steps.append("Do not treat this project as release-ready until FAIL/WARN items are reviewed.")
    next_steps.append("Do not apply automatic fixes; make changes only after active project approval, backup, and verification plan.")

    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "tool": "project_validation",
        "status": overall,
        "summary": summary,
        "project": {
            "input": str(ctx.project_input),
            "project_dir": str(ctx.project_dir) if ctx.project_dir else None,
            "project_file": str(ctx.project_file) if ctx.project_file else None,
            "main_schematic": str(ctx.main_schematic) if ctx.main_schematic else None,
            "main_pcb": str(ctx.main_pcb) if ctx.main_pcb else None,
        },
        "kicad_cli": cli_info,
        "output_dir": str(ctx.output_dir),
        "checks": output_results,
        "recommended_next_steps": next_steps,
        "safety": [
            "Read-only validation only.",
            "No automatic fixes attempted.",
            "Reports are written outside the project folder by default.",
            "A PASS/WARN/FAIL report does not replace human review for high-risk PCB design items.",
        ],
    }


def render_markdown(report: dict[str, Any]) -> list[str]:
    project = report["project"]
    lines = [
        "# KiCad Project Validation Report",
        "",
        f"Generated: {report['generated_at']}",
        f"Status: `{report['status']}`",
        "",
        "## Project",
        "",
        f"- Input: `{project['input']}`",
        f"- Project file: `{project['project_file']}`",
        f"- Schematic: `{project['main_schematic']}`",
        f"- PCB: `{project['main_pcb']}`",
        "",
        "## Summary",
        "",
        f"- PASS: {report['summary']['PASS']}",
        f"- WARN: {report['summary']['WARN']}",
        f"- FAIL: {report['summary']['FAIL']}",
        "",
        "## Checks",
        "",
        "| Status | Check | Summary |",
        "| --- | --- | --- |",
    ]
    for check in report["checks"]:
        lines.append(f"| `{check['status']}` | {check['title']} | {check['summary']} |")
    lines.extend(["", "## Details", ""])
    for check in report["checks"]:
        lines.extend([f"### {check['title']}", "", f"Status: `{check['status']}`", "", check["summary"], ""])
        if check.get("details"):
            lines.append("```json")
            lines.append(json.dumps(check["details"], indent=2, sort_keys=True))
            lines.append("```")
            lines.append("")
        if check.get("recommended_next_steps"):
            lines.append("Recommended next steps:")
            lines.extend(f"- {step}" for step in check["recommended_next_steps"])
            lines.append("")
    lines.extend(["## Recommended Next Steps", ""])
    lines.extend(f"- {step}" for step in report["recommended_next_steps"])
    lines.extend(
        [
            "",
            "## Safety",
            "",
            "- This validation report is read-only.",
            "- No automatic fixes were attempted.",
            "- KiCad ERC/DRC and human review are still required before release.",
        ]
    )
    return lines


def selected_checks(args: argparse.Namespace, default_checks: list[str] | None) -> list[str]:
    if args.list_checks:
        for check_id in CHECK_IDS:
            print(check_id)
        raise SystemExit(0)
    if args.checks:
        checks = []
        for value in args.checks:
            checks.extend(part.strip() for part in value.split(",") if part.strip())
    elif default_checks:
        checks = ["project_files"] + default_checks
    else:
        checks = list(CHECK_IDS)
    invalid = [check for check in checks if check not in CHECK_IDS]
    if invalid:
        raise SystemExit(f"Unknown check ids: {', '.join(invalid)}")
    return list(dict.fromkeys(checks))


def build_parser(description: str | None = None) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description or "Validate a KiCad project read-only and write Markdown/JSON reports.")
    parser.add_argument("project", nargs="?", help="Path to a KiCad project folder or .kicad_pro file.")
    parser.add_argument("--output-dir", help="Report output directory. Defaults to 05_OUTPUTS/project_validation/<timestamp>_<project>.")
    parser.add_argument("--allow-project-output", action="store_true", help="Allow writing reports inside the project folder. Avoid unless explicitly approved.")
    parser.add_argument("--kicad-root", help="Optional KiCad install root.")
    parser.add_argument("--kicad-cli", help="Path to kicad-cli.exe.")
    parser.add_argument("--kicad-version", default="", help="KiCad config version for user-global paths. Default inferred from install root or 9.0.")
    parser.add_argument("--component-db-root", help="Component database root. Default: 08_COMPONENT_DATABASE.")
    parser.add_argument("--datasheet-root", help="Datasheet root. Default: 06_DATASHEETS.")
    parser.add_argument("--checks", action="append", help="Comma-separated check IDs. Use --list-checks to see choices.")
    parser.add_argument("--list-checks", action="store_true")
    parser.add_argument("--fail-on-fail", action="store_true", help="Exit nonzero when the overall report status is FAIL.")
    return parser


def run_cli(default_checks: list[str] | None = None, description: str | None = None) -> int:
    parser = build_parser(description)
    args = parser.parse_args()
    checks = selected_checks(args, default_checks)
    if not args.project:
        parser.error("project is required unless --list-checks is used")
    ctx, startup_warnings = make_context(args)
    report = run_checks(ctx, checks, startup_warnings)
    json_path = ctx.output_dir / "project_validation_report.json"
    md_path = ctx.output_dir / "project_validation_report.md"
    write_json(json_path, report)
    write_markdown(md_path, render_markdown(report))
    print(f"Status: {report['status']}")
    print(f"Markdown report: {md_path}")
    print(f"JSON report: {json_path}")
    if args.fail_on_fail and report["status"] == "FAIL":
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(run_cli())
