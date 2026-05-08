#!/usr/bin/env python3
"""Shared live-project-state and stale-report helpers."""

from __future__ import annotations

import json
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = next((path for path in [SCRIPT_DIR, *SCRIPT_DIR.parents] if (path / "AGENTS.md").exists()), SCRIPT_DIR)
LAYOUT_SCRIPTS = REPO_ROOT / "14_LAYOUT_AUTOMATION" / "scripts"
if str(LAYOUT_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(LAYOUT_SCRIPTS))

from _kicad_pcb_bridge_common import require_pcbnew_for_cli  # type: ignore  # noqa: E402
from _kicad_pcb_bridge_extract import build_routing_schema  # type: ignore  # noqa: E402


PHASE_NAMES = {
    0: "Project Intake",
    1: "Schematic Gate",
    2: "PCB Creation / Update From Schematic",
    3: "Placement Planning",
    4: "Mechanical Setup",
    5: "Component Placement",
    6: "Placement Audit",
    7: "Zones / Ground Strategy",
    8: "Routing",
    9: "Final PCB Audit",
    10: "JLCPCB / Production Review",
    11: "NOT_FINAL Export",
    12: "JLC Upload Feedback",
    13: "Final Prototype Signoff",
}

KEY_OPERATIONAL_REPORTS = {
    "SCHEMATIC_TO_PCB_GATE_STATUS.md",
    "PCB_LAYOUT_SANDBOX_GATE_STATUS.md",
    "AUTO_PCB_START_REPORT.md",
    "REAL_PCB_UPDATE_FROM_SCHEMATIC_REPORT.md",
    "PCB_PLACEMENT_PASS_1_REPORT.md",
    "PCB_PLACEMENT_ORIENTATION_REVIEW.md",
    "REAL_PCB_ROUTING_PLAN.md",
    "PCB_SYNC_STATUS.md",
    "PCB_FILE_CURRENT_STATE.md",
    "LIVE_PCB_TRUTH_AUDIT.md",
    "PCB_PLACEMENT_CURRENT_STATE_REPORT.md",
    "ROUTING_CURRENT_STATE_REPORT.md",
    "ROUTING_START_BLOCKERS.md",
    "CURRENT_EXISTING_TRACE_AUDIT.md",
    "CURRENT_PCB_PLACEMENT_REJECTION_REPORT.md",
    "PCB_INTELLIGENCE_BASED_PLACEMENT_REPAIR_REPORT.md",
    "PCB_INTELLIGENCE_BASED_DRC_REPORT.md",
}

PCB_HASH_RE = re.compile(r"(?:PCB hash(?: before| after| in this audit)?|Board hash(?: before| after| in this audit)?|SHA256)\s*[:|]\s*`?([A-Fa-f0-9]{64})`?")
SCHEMATIC_HASH_RE = re.compile(r"Schematic hash(?: before| after| in this audit)?\s*[:|]\s*`?([A-Fa-f0-9]{64})`?", re.I)
STATUS_RE = re.compile(r"^(?:Gate result|Final result|Result|Status|Classification|Current classification|Action chosen)\s*:\s*`?([^`\n]+)`?", re.M)
DATE_RE = re.compile(r"^(?:Generated(?: date/time)?|Date|Updated|Timestamp|Last modified)\s*[:|]\s*`?([^`\n]+)`?", re.M)


def repo_root_from(repo_root: str | Path | None = None) -> Path:
    if repo_root:
        return Path(repo_root).resolve()
    return REPO_ROOT.resolve()


def resolve_project_path(repo_root: Path, project: str | Path) -> Path:
    candidate = Path(project)
    if candidate.is_absolute():
        return candidate.resolve()
    cwd_candidate = (Path.cwd() / candidate).resolve()
    if cwd_candidate.exists():
        return cwd_candidate
    return (repo_root / candidate).resolve()


def repo_rel(path: str | Path, repo_root: Path) -> str:
    candidate = Path(path)
    try:
        return str(candidate.resolve().relative_to(repo_root.resolve())).replace("/", "\\")
    except Exception:
        return str(candidate.resolve())


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def iso_timestamp_from_path(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime).astimezone().isoformat(timespec="seconds")


def file_metadata(path: Path | None, repo_root: Path) -> dict[str, Any]:
    if path is None:
        return {
            "exists": False,
            "path": "",
            "sha256": "",
            "timestamp": "",
            "size_bytes": 0,
        }
    resolved = path.resolve()
    if not resolved.exists():
        return {
            "exists": False,
            "path": repo_rel(resolved, repo_root),
            "sha256": "",
            "timestamp": "",
            "size_bytes": 0,
        }
    return {
        "exists": True,
        "path": repo_rel(resolved, repo_root),
        "sha256": sha256_file(resolved),
        "timestamp": iso_timestamp_from_path(resolved),
        "size_bytes": resolved.stat().st_size,
    }


def find_one(project: Path, patterns: list[str]) -> Path | None:
    for pattern in patterns:
        for match in sorted(project.glob(pattern), key=lambda item: str(item).lower()):
            if match.is_file():
                return match.resolve()
    return None


def preferred_project_file(project: Path, suffix: str) -> Path | None:
    for candidate in [
        project / "kicad" / f"{project.name}{suffix}",
        project / f"{project.name}{suffix}",
    ]:
        if candidate.exists() and candidate.is_file():
            return candidate.resolve()
    return None


def build_board_schema(project_name: str, pcb_path: Path) -> dict[str, Any]:
    pcbnew = require_pcbnew_for_cli()
    board = pcbnew.LoadBoard(str(pcb_path))
    return build_routing_schema(project_name, str(pcb_path), board, pcbnew)


def live_support_dir(project: Path) -> Path:
    return project / "reports" / "live_project_state"


def drc_candidate_paths(project: Path) -> list[Path]:
    support_dir = live_support_dir(project)
    return [
        support_dir / "LIVE_PROJECT_STATE_DRC.json",
        project / "reports" / "current_existing_trace_audit" / "drc.json",
        project / "reports" / "live_pcb_truth_audit" / "LIVE_PCB_TRUTH_AUDIT_DRC.json",
        project / "reports" / "live_pcb_truth_audit" / "real_board_routing_audit" / "drc.json",
    ]


def valid_drc_candidate(path: Path, pcb_timestamp: float) -> bool:
    if not path.exists() or path.stat().st_mtime < pcb_timestamp:
        return False
    try:
        data = load_json(path)
    except Exception:
        return False
    return isinstance(data, dict) and "violations" in data and "unconnected_items" in data


def run_kicad_drc_json(pcb_path: Path, output_path: Path) -> tuple[dict[str, Any] | None, dict[str, Any]]:
    command = [
        "kicad-cli",
        "pcb",
        "drc",
        "--format",
        "json",
        "--severity-all",
        "--output",
        str(output_path),
        str(pcb_path),
    ]
    result = {
        "command": command,
        "returncode": None,
        "stdout": "",
        "stderr": "",
        "used_existing": False,
    }
    try:
        completed = subprocess.run(command, capture_output=True, text=True, check=False)
    except FileNotFoundError:
        result["returncode"] = 127
        result["stderr"] = "kicad-cli not found on PATH"
        return None, result
    result["returncode"] = completed.returncode
    result["stdout"] = completed.stdout
    result["stderr"] = completed.stderr
    if completed.returncode != 0 or not output_path.exists():
        return None, result
    try:
        return load_json(output_path), result
    except Exception as exc:
        result["stderr"] = (result["stderr"] + f"\nfailed to parse DRC JSON: {exc}").strip()
        return None, result


def load_or_run_drc(project: Path, pcb_path: Path, write_supporting: bool) -> tuple[dict[str, Any] | None, dict[str, Any]]:
    pcb_timestamp = pcb_path.stat().st_mtime
    target = live_support_dir(project) / "LIVE_PROJECT_STATE_DRC.json"
    for candidate in drc_candidate_paths(project):
        if valid_drc_candidate(candidate, pcb_timestamp):
            data = load_json(candidate)
            info = {
                "command": [],
                "returncode": 0,
                "stdout": "",
                "stderr": "",
                "used_existing": True,
                "source_path": str(candidate),
            }
            if write_supporting and candidate.resolve() != target.resolve():
                dump_json(target, data)
            return data, info

    if write_supporting:
        target.parent.mkdir(parents=True, exist_ok=True)
        return run_kicad_drc_json(pcb_path, target)

    with tempfile.NamedTemporaryFile(prefix="kicad_engine_live_state_drc_", suffix=".json", delete=False) as handle:
        temp_path = Path(handle.name)
    try:
        return run_kicad_drc_json(pcb_path, temp_path)
    finally:
        try:
            temp_path.unlink(missing_ok=True)
        except OSError:
            pass


def summarize_drc(drc_data: dict[str, Any] | None) -> dict[str, Any]:
    if not drc_data:
        return {
            "runnable": False,
            "result": "NOT_RUN",
            "violation_count": None,
            "unconnected_count": None,
            "violation_types": {},
            "primary_violation_items": [],
        }
    violations = drc_data.get("violations", []) or []
    unconnected = drc_data.get("unconnected_items", []) or []
    type_counter = Counter(str(item.get("type", "UNKNOWN")) for item in violations)
    primary_items: list[str] = []
    for violation in violations[:12]:
        for item in violation.get("items", []) or []:
            description = str(item.get("description", "")).strip()
            if description and description not in primary_items:
                primary_items.append(description)
    return {
        "runnable": True,
        "result": "PASS" if not violations and not unconnected else "FAIL",
        "violation_count": len(violations),
        "unconnected_count": len(unconnected),
        "violation_types": dict(type_counter),
        "primary_violation_items": primary_items,
    }


def operational_report_paths(project: Path) -> list[Path]:
    reports_dir = project / "reports"
    paths: list[Path] = []
    for name in sorted(KEY_OPERATIONAL_REPORTS):
        path = reports_dir / name
        if path.exists():
            paths.append(path)
    return paths


def line_count(text: str, needle: str) -> int:
    return sum(1 for line in text.splitlines() if needle in line)


def live_file_summary(live_state: dict[str, Any]) -> str:
    pcb = live_state["pcb"]
    return (
        f"PCB exists={pcb['exists']}, footprints={pcb['footprint_count']}, tracks={pcb['track_count']}, "
        f"vias={pcb['via_count']}, zones={pcb['zone_count']}, placement={pcb['placement_exists']}, "
        f"routing={pcb['routing_exists']}, unrouted={pcb['unrouted_net_count']}, "
        f"drc={live_state['drc']['result']}"
    )


def report_status_summary(text: str) -> str:
    match = STATUS_RE.search(text)
    if match:
        return match.group(1).strip()
    return "UNSPECIFIED"


def report_source_hashes(text: str) -> dict[str, str]:
    pcb_match = PCB_HASH_RE.search(text)
    sch_match = SCHEMATIC_HASH_RE.search(text)
    return {
        "pcb_hash": pcb_match.group(1).upper() if pcb_match else "",
        "schematic_hash": sch_match.group(1).upper() if sch_match else "",
    }


def report_primary_date(text: str) -> str:
    match = DATE_RE.search(text)
    return match.group(1).strip() if match else ""


def report_expected_sources(path: Path) -> list[str]:
    explicit = {
        "SCHEMATIC_TO_PCB_GATE_STATUS.md": ["schematic"],
        "PCB_LAYOUT_SANDBOX_GATE_STATUS.md": ["pcb"],
        "AUTO_PCB_START_REPORT.md": ["pcb", "schematic"],
        "REAL_PCB_UPDATE_FROM_SCHEMATIC_REPORT.md": ["pcb", "schematic"],
        "PCB_PLACEMENT_PASS_1_REPORT.md": ["pcb"],
        "PCB_PLACEMENT_CURRENT_STATE_REPORT.md": ["pcb"],
        "PCB_PLACEMENT_ORIENTATION_REVIEW.md": ["pcb"],
        "REAL_PCB_ROUTING_PLAN.md": ["pcb"],
        "ROUTING_CURRENT_STATE_REPORT.md": ["pcb"],
        "ROUTING_START_BLOCKERS.md": ["pcb"],
        "CURRENT_EXISTING_TRACE_AUDIT.md": ["pcb"],
        "PCB_FILE_CURRENT_STATE.md": ["pcb"],
        "LIVE_PCB_TRUTH_AUDIT.md": ["pcb"],
        "PCB_SYNC_STATUS.md": ["pcb", "schematic"],
        "PCB_INTELLIGENCE_BASED_PLACEMENT_REPAIR_REPORT.md": ["pcb"],
        "PCB_INTELLIGENCE_BASED_DRC_REPORT.md": ["pcb"],
        "CURRENT_PCB_PLACEMENT_REJECTION_REPORT.md": ["pcb"],
    }
    if path.name in explicit:
        return explicit[path.name]
    name = path.name.upper()
    expected: list[str] = []
    if any(token in name for token in ("PCB", "PLACEMENT", "ROUTING", "TRACE")):
        expected.append("pcb")
    if "SCHEMATIC" in name:
        expected.append("schematic")
    return expected


def report_claims(text: str) -> dict[str, Any]:
    def last_int(patterns: list[str]) -> int | None:
        for pattern in patterns:
            matches = re.findall(pattern, text, flags=re.I)
            if matches:
                try:
                    return int(matches[-1])
                except ValueError:
                    return None
        return None

    claims = {
        "status": report_status_summary(text),
        "says_no_pcb": False,
        "says_no_routing": False,
        "says_no_placement": False,
        "says_phase2_not_done": False,
        "footprint_count": last_int(
            [
                r"Footprints present on PCB\s*[:|]\s*`?(\d+)`?",
                r"Footprints on PCB\s*[:|]\s*`?(\d+)`?",
                r"Footprints imported\s*[:|]\s*`?(\d+)`?",
                r"Footprint count\s*[:|]\s*`?(\d+)`?",
                r"Live footprint count\s*[:|]\s*`?(\d+)`?",
            ]
        ),
        "track_count": last_int(
            [
                r"Track segments?\s*[:|]\s*`?(\d+)`?",
                r"Track count\s*[:|]\s*`?(\d+)`?",
            ]
        ),
        "via_count": last_int(
            [
                r"Via count\s*[:|]\s*`?(\d+)`?",
                r"Vias extracted\s*[:|]\s*`?(\d+)`?",
            ]
        ),
        "zone_count": last_int(
            [
                r"Zone count\s*[:|]\s*`?(\d+)`?",
                r"Zones extracted\s*[:|]\s*`?(\d+)`?",
            ]
        ),
    }

    if re.search(r"^\s*(?:PCB exists(?: now)?|\.kicad_pcb exists|Real \.kicad_pcb exists)\s*[:|]\s*`?NO`?\s*$", text, flags=re.I | re.M):
        claims["says_no_pcb"] = True
    if re.search(r"^\s*(?:Status|Classification|Result)\s*:\s*`?[^`\n]*NO_PCB[^`\n]*`?\s*$", text, flags=re.I | re.M):
        claims["says_no_pcb"] = True
    if re.search(r"^\s*Placement exists\s*[:|]\s*`?NO`?\s*$", text, flags=re.I | re.M):
        claims["says_no_placement"] = True
    if re.search(r"^\s*(?:Status|Classification|Result)\s*:\s*`?[^`\n]*(?:NO_PLACEMENT|PLACEMENT_FAIL)[^`\n]*`?\s*$", text, flags=re.I | re.M):
        claims["says_no_placement"] = True
    if re.search(r"^\s*Routing exists\s*[:|]\s*`?NO`?\s*$", text, flags=re.I | re.M):
        claims["says_no_routing"] = True
    if re.search(r"^\s*Routing performed\s*[:|]\s*`?NO`?\s*$", text, flags=re.I | re.M):
        claims["says_no_routing"] = True
    if re.search(r"^\s*(?:Status|Classification|Result)\s*:\s*`?[^`\n]*NO_ROUTING[^`\n]*`?\s*$", text, flags=re.I | re.M):
        claims["says_no_routing"] = True
    if re.search(r"^\s*(?:Status|Classification|Result)\s*:\s*`?[^`\n]*PHASE[_ ]?2[^`\n]*INCOMPLETE[^`\n]*`?\s*$", text, flags=re.I | re.M):
        claims["says_phase2_not_done"] = True
    if re.search(r"^\s*Missing PCB file", text, flags=re.I | re.M):
        claims["says_phase2_not_done"] = True
    return claims


def classify_live_board(pcb: dict[str, Any], drc: dict[str, Any]) -> str:
    if not pcb["exists"]:
        return "PCB_BLOCKED_FATAL_BOARD_STATE"
    if pcb["routing_exists"] and (pcb["unrouted_net_count"] or drc["result"] == "FAIL"):
        return "PCB_EXISTS_PARTIAL_ROUTING_EXISTS_NEEDS_AUDIT"
    if pcb["placement_exists"] and not pcb["routing_exists"]:
        if drc["result"] == "FAIL":
            return "PCB_EXISTS_PLACEMENT_NEEDS_REPAIR_BEFORE_ROUTING"
        return "PCB_READY_FOR_ROUTING_PLAN"
    if pcb["placement_exists"]:
        return "PCB_EXISTS_PLACEMENT_EXISTS_ROUTING_NOT_READY"
    return "PCB_BLOCKED_FATAL_BOARD_STATE"


def component_is_mounting_hole(component: dict[str, Any]) -> bool:
    ref = str(component.get("ref", "")).upper()
    footprint_name = str(component.get("footprint_name", "")).upper()
    value = str(component.get("value", "")).upper()
    if ref.startswith("MH"):
        return True
    if "MOUNTINGHOLE" in footprint_name or "MOUNTING_HOLE" in footprint_name:
        return True
    if value.startswith("MH"):
        return True
    return False


def build_live_project_state_data(project: Path, repo_root: Path, write_supporting: bool) -> dict[str, Any]:
    kicad_pro = preferred_project_file(project, ".kicad_pro") or find_one(project, ["kicad/*.kicad_pro", "*.kicad_pro"])
    kicad_sch = preferred_project_file(project, ".kicad_sch") or find_one(project, ["kicad/*.kicad_sch", "*.kicad_sch"])
    kicad_pcb = preferred_project_file(project, ".kicad_pcb") or find_one(project, ["kicad/*.kicad_pcb", "*.kicad_pcb"])

    files = {
        "kicad_pro": file_metadata(kicad_pro, repo_root),
        "kicad_sch": file_metadata(kicad_sch, repo_root),
        "kicad_pcb": file_metadata(kicad_pcb, repo_root),
    }

    pcb_state: dict[str, Any] = {
        "exists": bool(kicad_pcb and kicad_pcb.exists()),
        "board_outline_exists": False,
        "board_width_mm": 0.0,
        "board_height_mm": 0.0,
        "footprint_count": 0,
        "mounting_hole_count": 0,
        "track_count": 0,
        "via_count": 0,
        "zone_count": 0,
        "keepout_count": 0,
        "net_count": 0,
        "routed_nets": [],
        "unrouted_nets": [],
        "unrouted_net_count": 0,
        "components_inside_outline_count": 0,
        "components_outside_outline_count": 0,
        "components_outside_outline_refs": [],
        "placement_exists": False,
        "routing_exists": False,
        "zones_present": False,
        "tracks_present": False,
        "vias_present": False,
        "mounting_holes_present": False,
        "outline_bbox_mm": {},
    }
    routing_schema: dict[str, Any] | None = None
    if kicad_pcb and kicad_pcb.exists():
        routing_schema = build_board_schema(project.name, kicad_pcb)
        if write_supporting:
            support_dir = live_support_dir(project)
            dump_json(support_dir / "LIVE_PROJECT_STATE_ROUTING_SCHEMA.json", routing_schema)

        components = routing_schema.get("components", []) or []
        traces = routing_schema.get("traces", []) or []
        nets = routing_schema.get("nets", []) or []
        outline = routing_schema.get("board_outline", {}) or {}
        outline_bbox = {
            "xmin": outline.get("xmin", 0.0),
            "xmax": outline.get("xmax", 0.0),
            "ymin": outline.get("ymin", 0.0),
            "ymax": outline.get("ymax", 0.0),
        }

        inside_count = 0
        outside_refs: list[str] = []
        if routing_schema.get("edge_cuts"):
            for component in components:
                x = float(component.get("x_mm", 0.0))
                y = float(component.get("y_mm", 0.0))
                if outline_bbox["xmin"] <= x <= outline_bbox["xmax"] and outline_bbox["ymin"] <= y <= outline_bbox["ymax"]:
                    inside_count += 1
                else:
                    outside_refs.append(str(component.get("ref", "")))

        routed_nets = sorted(
            {
                str(trace.get("net", "")).strip()
                for trace in traces
                if str(trace.get("net", "")).strip()
                and (trace.get("segments") or trace.get("via_count", 0))
            }
        )
        unrouted_nets = sorted(
            str(net.get("name", "")).strip()
            for net in nets
            if str(net.get("routing_status", "")).upper() == "UNROUTED" and str(net.get("name", "")).strip()
        )

        pcb_state.update(
            {
                "board_outline_exists": bool(routing_schema.get("edge_cuts")),
                "board_width_mm": outline.get("width_mm", 0.0) or 0.0,
                "board_height_mm": outline.get("height_mm", 0.0) or 0.0,
                "footprint_count": len(routing_schema.get("footprints", []) or []),
                "mounting_hole_count": sum(1 for item in components if component_is_mounting_hole(item)),
                "track_count": len(routing_schema.get("tracks", []) or []),
                "via_count": len(routing_schema.get("vias", []) or []),
                "zone_count": len(routing_schema.get("zones", []) or []),
                "keepout_count": len(routing_schema.get("keepouts", []) or []),
                "net_count": len(nets),
                "routed_nets": routed_nets,
                "unrouted_nets": unrouted_nets,
                "unrouted_net_count": len(unrouted_nets),
                "components_inside_outline_count": inside_count,
                "components_outside_outline_count": len(outside_refs),
                "components_outside_outline_refs": outside_refs,
                "placement_exists": len(components) > 0 and inside_count > 0,
                "routing_exists": bool(routed_nets),
                "zones_present": len(routing_schema.get("zones", []) or []) > 0,
                "tracks_present": len(routing_schema.get("tracks", []) or []) > 0,
                "vias_present": len(routing_schema.get("vias", []) or []) > 0,
                "mounting_holes_present": sum(1 for item in components if component_is_mounting_hole(item)) > 0,
                "outline_bbox_mm": outline_bbox,
            }
        )

    drc_data, drc_run_info = (None, {"returncode": None, "used_existing": False, "stdout": "", "stderr": "", "command": []})
    if kicad_pcb and kicad_pcb.exists():
        drc_data, drc_run_info = load_or_run_drc(project, kicad_pcb, write_supporting)
    drc_summary = summarize_drc(drc_data)

    classification = classify_live_board(pcb_state, drc_summary)
    next_action = (
        "Repair or explicitly accept the current routed geometry, approve live placement/orientation, and resolve GND strategy plus critical unrouted nets before new routing."
        if classification == "PCB_EXISTS_PARTIAL_ROUTING_EXISTS_NEEDS_AUDIT"
        else "Use live file evidence and refreshed gates before advancing PCB work."
    )

    state = {
        "schema_version": "1.0",
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "project": {
            "name": project.name,
            "path": repo_rel(project, repo_root),
            "reports_path": repo_rel(project / "reports", repo_root),
        },
        "source_files": files,
        "pcb": pcb_state,
        "drc": drc_summary,
        "drc_source": drc_run_info,
        "classification": classification,
        "current_real_phase": {
            "pcb_created": pcb_state["exists"],
            "placement_exists": pcb_state["placement_exists"],
            "routing_exists": pcb_state["routing_exists"],
            "placement_repair_needed": pcb_state["placement_exists"] and (drc_summary["result"] == "FAIL" or pcb_state["unrouted_net_count"] > 0),
            "routing_plan_may_continue": False,
        },
        "next_action": next_action,
    }
    if routing_schema is not None:
        state["routing_schema_summary"] = {
            "not_extracted": routing_schema.get("not_extracted", []) or [],
            "ground_strategy": routing_schema.get("ground_strategy", {}) or {},
        }
    return state


def render_live_project_state_markdown(live_state: dict[str, Any]) -> str:
    pcb = live_state["pcb"]
    drc = live_state["drc"]
    files = live_state["source_files"]
    lines = [
        "# Live Project State",
        "",
        f"Generated: `{live_state['generated_at']}`",
        "",
        f"Project: `{live_state['project']['name']}`",
        "",
        f"Classification: `{live_state['classification']}`",
        "",
        "## Source Files",
        "",
        "| File | Exists | SHA256 | Timestamp |",
        "| --- | --- | --- | --- |",
    ]
    for key in ("kicad_pro", "kicad_sch", "kicad_pcb"):
        meta = files[key]
        lines.append(
            f"| `{key}` | `{meta['exists']}` | `{meta['sha256'] or 'MISSING'}` | `{meta['timestamp'] or 'MISSING'}` |"
        )
    lines.extend(
        [
            "",
            "## Live PCB Truth",
            "",
            "| Item | Result |",
            "| --- | --- |",
            f"| PCB exists | `{pcb['exists']}` |",
            f"| Board outline exists | `{pcb['board_outline_exists']}` |",
            f"| Board size | `{pcb['board_width_mm']} mm x {pcb['board_height_mm']} mm` |",
            f"| Footprints | `{pcb['footprint_count']}` |",
            f"| Mounting holes | `{pcb['mounting_hole_count']}` |",
            f"| Tracks | `{pcb['track_count']}` |",
            f"| Vias | `{pcb['via_count']}` |",
            f"| Zones | `{pcb['zone_count']}` |",
            f"| Placed inside outline bbox | `{pcb['components_inside_outline_count']} / {pcb['footprint_count']}` |",
            f"| Routing exists | `{pcb['routing_exists']}` |",
            f"| Detectable unrouted nets | `{pcb['unrouted_net_count']}` |",
            "",
            "## DRC",
            "",
            "| Item | Result |",
            "| --- | --- |",
            f"| Runnable | `{drc['runnable']}` |",
            f"| Result | `{drc['result']}` |",
            f"| Violations | `{drc['violation_count']}` |",
            f"| Unconnected items | `{drc['unconnected_count']}` |",
            "",
            "## Routed Nets",
            "",
        ]
    )
    if pcb["routed_nets"]:
        for net in pcb["routed_nets"]:
            lines.append(f"- `{net}`")
    else:
        lines.append("- None detected")
    lines.extend(["", "## Unrouted Nets", ""])
    if pcb["unrouted_nets"]:
        for net in pcb["unrouted_nets"]:
            lines.append(f"- `{net}`")
    else:
        lines.append("- None detected")
    lines.extend(["", "## Next Action", "", live_state["next_action"], ""])
    return "\n".join(lines)


def build_live_state_outputs(project: Path, repo_root: Path, write_supporting: bool) -> dict[str, Any]:
    live_state = build_live_project_state_data(project, repo_root, write_supporting=write_supporting)
    json_path = project / "reports" / "LIVE_PROJECT_STATE.json"
    md_path = project / "reports" / "LIVE_PROJECT_STATE.md"
    if write_supporting:
        dump_json(json_path, live_state)
        write_text(md_path, render_live_project_state_markdown(live_state))
    live_state["_output_json"] = repo_rel(json_path, repo_root)
    live_state["_output_markdown"] = repo_rel(md_path, repo_root)
    return live_state


def detect_stale_reports_data(project: Path, repo_root: Path, live_state: dict[str, Any]) -> dict[str, Any]:
    reports_dir = project / "reports"
    files = live_state["source_files"]
    pcb_meta = files["kicad_pcb"]
    sch_meta = files["kicad_sch"]
    live_summary = live_file_summary(live_state)
    live_pcb_path = preferred_project_file(project, ".kicad_pcb") or find_one(project, ["kicad/*.kicad_pcb", "*.kicad_pcb"])
    live_sch_path = preferred_project_file(project, ".kicad_sch") or find_one(project, ["kicad/*.kicad_sch", "*.kicad_sch"])
    rows: list[dict[str, Any]] = []
    stale_rows: list[dict[str, Any]] = []

    for path in operational_report_paths(project):
        text = read_text(path)
        hashes = report_source_hashes(text)
        claims = report_claims(text)
        expected_sources = report_expected_sources(path)
        reasons: list[str] = []

        if "pcb" in expected_sources and hashes["pcb_hash"] and hashes["pcb_hash"] != pcb_meta["sha256"]:
            reasons.append("PCB hash mismatch versus live board")
        if "schematic" in expected_sources and hashes["schematic_hash"] and hashes["schematic_hash"] != sch_meta["sha256"]:
            reasons.append("Schematic hash mismatch versus live schematic")

        report_is_older_than_pcb = bool(live_pcb_path and live_pcb_path.exists() and path.stat().st_mtime < live_pcb_path.stat().st_mtime)
        report_is_older_than_schematic = bool(live_sch_path and live_sch_path.exists() and path.stat().st_mtime < live_sch_path.stat().st_mtime)

        if "pcb" in expected_sources and not hashes["pcb_hash"] and report_is_older_than_pcb:
            reasons.append("No PCB hash and report is older than live PCB file")
        if "schematic" in expected_sources and not hashes["schematic_hash"] and report_is_older_than_schematic:
            reasons.append("No schematic hash and report is older than live schematic file")

        if claims["says_no_pcb"] and live_state["pcb"]["footprint_count"] > 0:
            reasons.append("Report says NO_PCB but live PCB contains footprints")
        if claims["footprint_count"] == 0 and live_state["pcb"]["footprint_count"] > 0:
            reasons.append("Report says 0 footprints but live PCB has footprints")
        if claims["says_no_routing"] and live_state["pcb"]["track_count"] > 0:
            reasons.append("Report says routing missing but live PCB has tracks")
        if claims["track_count"] == 0 and live_state["pcb"]["track_count"] > 0:
            reasons.append("Report says 0 tracks but live PCB has tracks")
        if claims["says_no_placement"] and live_state["pcb"]["placement_exists"]:
            reasons.append("Report says placement missing but live PCB shows placed footprints")
        if claims["says_phase2_not_done"] and live_state["pcb"]["footprint_count"] > 0:
            reasons.append("Report says phase 2 not done but live PCB and footprints exist")

        stale = bool(reasons)
        weak = bool(expected_sources and not hashes["pcb_hash"] and "pcb" in expected_sources) or bool(expected_sources and not hashes["schematic_hash"] and "schematic" in expected_sources)
        source_hash_status = "MATCH"
        if "pcb" in expected_sources and hashes["pcb_hash"] and hashes["pcb_hash"] != pcb_meta["sha256"]:
            source_hash_status = "MISMATCH"
        elif "schematic" in expected_sources and hashes["schematic_hash"] and hashes["schematic_hash"] != sch_meta["sha256"]:
            source_hash_status = "MISMATCH"
        elif ("pcb" in expected_sources and not hashes["pcb_hash"]) or ("schematic" in expected_sources and not hashes["schematic_hash"]):
            source_hash_status = "MISSING"

        row = {
            "file": repo_rel(path, repo_root),
            "status": claims["status"],
            "report_timestamp": report_primary_date(text) or iso_timestamp_from_path(path),
            "source_hash_status": source_hash_status,
            "pcb_hash_in_report": hashes["pcb_hash"] or "MISSING",
            "schematic_hash_in_report": hashes["schematic_hash"] or "MISSING",
            "says": ", ".join(
                item
                for item in [
                    claims["status"],
                    "NO_PCB" if claims["says_no_pcb"] else "",
                    f"footprints={claims['footprint_count']}" if claims["footprint_count"] is not None else "",
                    f"tracks={claims['track_count']}" if claims["track_count"] is not None else "",
                    "NO_PLACEMENT" if claims["says_no_placement"] else "",
                    "NO_ROUTING" if claims["says_no_routing"] else "",
                ]
                if item
            ),
            "live_pcb_says": live_summary,
            "stale": "YES" if stale else "NO",
            "weak_or_stale_prone": "YES" if weak else "NO",
            "action_needed": "IGNORE_AS_BLOCKER_AND_REFRESH_FROM_LIVE_STATE" if stale else ("ADD_SOURCE_HASHES_ON_NEXT_UPDATE" if weak else "USE_AS_CONTEXT_ONLY"),
            "reasons": reasons,
        }
        rows.append(row)
        if stale:
            stale_rows.append(row)

    return {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "project": project.name,
        "live_pcb_hash": pcb_meta["sha256"],
        "live_schematic_hash": sch_meta["sha256"],
        "rows": rows,
        "stale_rows": stale_rows,
    }


def render_stale_reports_markdown(audit: dict[str, Any]) -> str:
    lines = [
        "# Stale Reports Audit",
        "",
        f"Generated: `{audit['generated_at']}`",
        "",
        f"Project: `{audit['project']}`",
        "",
        f"Live PCB hash: `{audit['live_pcb_hash'] or 'MISSING'}`",
        f"Live schematic hash: `{audit['live_schematic_hash'] or 'MISSING'}`",
        "",
        "| File | Says | Live PCB Says | Stale | Weak/Stale-Prone | Action Needed |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in audit["rows"]:
        lines.append(
            f"| `{row['file']}` | {row['says'] or 'UNSPECIFIED'} | {row['live_pcb_says']} | `{row['stale']}` | `{row['weak_or_stale_prone']}` | `{row['action_needed']}` |"
        )
    lines.extend(["", "## Stale Findings", ""])
    if audit["stale_rows"]:
        for row in audit["stale_rows"]:
            lines.append(f"- `{row['file']}`")
            for reason in row["reasons"]:
                lines.append(f"  - {reason}")
    else:
        lines.append("- No stale operational reports detected.")
    lines.append("")
    return "\n".join(lines)


def write_stale_reports_outputs(project: Path, repo_root: Path, audit: dict[str, Any]) -> None:
    dump_json(project / "reports" / "STALE_REPORTS_AUDIT.json", audit)
    write_text(project / "reports" / "STALE_REPORTS_AUDIT.md", render_stale_reports_markdown(audit))


def parse_hash_from_report(path: Path) -> str:
    hashes = report_source_hashes(read_text(path))
    return hashes["pcb_hash"]


def parse_trace_audit_blockers(project: Path, repo_root: Path, live_state: dict[str, Any]) -> list[dict[str, str]]:
    path = project / "reports" / "CURRENT_EXISTING_TRACE_AUDIT.md"
    if not path.exists():
        return []
    text = read_text(path)
    report_hash = parse_hash_from_report(path)
    if report_hash and report_hash != live_state["source_files"]["kicad_pcb"]["sha256"]:
        return []
    rows: list[dict[str, str]] = []
    for line in text.splitlines():
        if line.startswith("| `") and any(token in line for token in ("right_angle_turn", "acute_or_nonstandard_angle", "clean in current audit")):
            parts = [item.strip() for item in line.strip("|").split("|")]
            if len(parts) >= 4:
                net = parts[0].strip(" `")
                finding = parts[3].strip()
                if "clean" not in finding.lower():
                    rows.append({"net": net, "finding": finding})
    return rows


def report_fresh_for_live_pcb(path: Path, live_state: dict[str, Any]) -> bool:
    if not path.exists():
        return False
    live_hash = live_state["source_files"]["kicad_pcb"]["sha256"]
    report_hash = parse_hash_from_report(path)
    if report_hash:
        return report_hash == live_hash
    pcb_path = path.parents[1] / "kicad" / f"{path.parents[1].name}.kicad_pcb"
    return pcb_path.exists() and path.stat().st_mtime >= pcb_path.stat().st_mtime


def reconcile_gate_data(project: Path, repo_root: Path, live_state: dict[str, Any], stale_audit: dict[str, Any]) -> dict[str, Any]:
    stale_files = {row["file"] for row in stale_audit["stale_rows"]}
    schematic_gate = project / "reports" / "SCHEMATIC_TO_PCB_GATE_STATUS.md"
    sandbox_gate = project / "reports" / "PCB_LAYOUT_SANDBOX_GATE_STATUS.md"
    trace_audit = project / "reports" / "CURRENT_EXISTING_TRACE_AUDIT.md"
    schematic_gate_rel = repo_rel(schematic_gate, repo_root)
    sandbox_gate_rel = repo_rel(sandbox_gate, repo_root)

    trace_blockers = parse_trace_audit_blockers(project, repo_root, live_state)
    phase_results: dict[str, Any] = {}

    live_pcb_exists = bool(live_state["pcb"]["exists"])
    live_placement_exists = bool(live_state["pcb"]["placement_exists"])
    live_routing_exists = bool(live_state["pcb"]["routing_exists"])
    drc_fail = live_state["drc"]["result"] == "FAIL"
    unrouted_count = int(live_state["pcb"]["unrouted_net_count"])
    zone_count = int(live_state["pcb"]["zone_count"])

    phase_results["2"] = {
        "phase": 2,
        "name": PHASE_NAMES[2],
        "result": "ALLOWED" if live_pcb_exists else "BLOCKED",
        "phase_status": "ALREADY_DONE_BY_LIVE_FILE_EVIDENCE" if live_pcb_exists else "UPSTREAM_GATE_REQUIRED",
        "next_required_phase": 3 if live_pcb_exists else 2,
        "blockers": [] if live_pcb_exists else ["No live PCB file exists yet."],
        "evidence_decisions": [
            {
                "source": "LIVE_FILE_EVIDENCE",
                "message": f"Live PCB exists with {live_state['pcb']['footprint_count']} footprints."
            }
        ] if live_pcb_exists else [],
        "warnings": [
            "Live PCB existence proves Phase 2 already occurred even though upstream schematic gate remains FAIL."
        ] if live_pcb_exists and schematic_gate.exists() else [],
    }

    phase3_warnings: list[str] = []
    phase3_decisions = []
    if schematic_gate.exists():
        phase3_decisions.append(
            {
                "source": "STALE_REPORT_IGNORED" if schematic_gate_rel in stale_files else "FRESH_GATE_REPORT",
                "message": "SCHEMATIC_TO_PCB_GATE_STATUS.md still records a formal schematic gate FAIL." if schematic_gate_rel not in stale_files else "SCHEMATIC_TO_PCB_GATE_STATUS.md is older than the live schematic and cannot overrule live-state reconciliation."
            }
        )
    if live_placement_exists:
        phase3_warnings.append("Placement planning is already superseded by live placement evidence on the current board.")
        phase3_decisions.append(
            {
                "source": "LIVE_FILE_EVIDENCE",
                "message": f"Live PCB shows placed footprints inside outline bbox ({live_state['pcb']['components_inside_outline_count']} / {live_state['pcb']['footprint_count']})."
            }
        )
    phase_results["3"] = {
        "phase": 3,
        "name": PHASE_NAMES[3],
        "result": "ALLOWED" if live_pcb_exists else "BLOCKED",
        "phase_status": "ALREADY_DONE_OR_SUPERSEDED_BY_LIVE_PLACEMENT" if live_placement_exists else ("READY_FOR_PLACEMENT_PLANNING" if live_pcb_exists else "PHASE_2_REQUIRED"),
        "next_required_phase": 4 if live_pcb_exists else 2,
        "blockers": [] if live_pcb_exists else ["Live PCB evidence is missing, so placement planning cannot start."],
        "evidence_decisions": phase3_decisions,
        "warnings": phase3_warnings,
    }

    routing_blockers: list[str] = []
    evidence_decisions: list[dict[str, str]] = []
    warnings: list[str] = []
    if live_routing_exists:
        evidence_decisions.append(
            {
                "source": "LIVE_FILE_EVIDENCE",
                "message": f"Live PCB contains routing: tracks={live_state['pcb']['track_count']}, vias={live_state['pcb']['via_count']}."
            }
        )
    if str(repo_rel(project / "reports" / "REAL_PCB_UPDATE_FROM_SCHEMATIC_REPORT.md", repo_root)) in stale_files:
        evidence_decisions.append(
            {
                "source": "STALE_REPORT_IGNORED",
                "message": "REAL_PCB_UPDATE_FROM_SCHEMATIC report is stale and does not control routing gating."
            }
        )
    if schematic_gate.exists():
        evidence_decisions.append(
            {
                "source": "STALE_REPORT_IGNORED" if schematic_gate_rel in stale_files else "FRESH_GATE_REPORT",
                "message": "SCHEMATIC_TO_PCB_GATE_STATUS.md still records a formal FAIL and remains upstream context." if schematic_gate_rel not in stale_files else "SCHEMATIC_TO_PCB_GATE_STATUS.md is stale against the live schematic and is not used as a direct routing blocker."
            }
        )
        warnings.append("Human review is required because historical schematic-gate evidence conflicts with the existence of a live PCB.")
    if sandbox_gate.exists():
        evidence_decisions.append(
            {
                "source": "STALE_REPORT_IGNORED" if sandbox_gate_rel in stale_files else "FRESH_GATE_REPORT",
                "message": "PCB_LAYOUT_SANDBOX_GATE_STATUS.md remains BLOCKED as a PCB-edit permission gate, not as proof that no board exists." if sandbox_gate_rel not in stale_files else "PCB_LAYOUT_SANDBOX_GATE_STATUS.md is stale and cannot be used to claim NO_PCB or missing placement."
            }
        )
    if trace_blockers and report_fresh_for_live_pcb(trace_audit, live_state):
        evidence_decisions.append(
            {
                "source": "FRESH_GATE_REPORT",
                "message": f"CURRENT_EXISTING_TRACE_AUDIT.md matches the live PCB hash and reports {len(trace_blockers)} routed-geometry issues."
            }
        )
    if drc_fail:
        routing_blockers.append(f"Live DRC is FAIL with {live_state['drc']['violation_count']} violations and {live_state['drc']['unconnected_count']} unconnected items.")
    if unrouted_count > 0:
        routing_blockers.append(f"{unrouted_count} detectable unrouted nets remain.")
    if zone_count == 0:
        routing_blockers.append("No zones or accepted GND strategy exist on the current live board.")
    if trace_blockers:
        routing_blockers.append("Existing routed geometry is not fully verified for continuation.")
    warnings.append("Human review is required before routing continuation because the live board exists despite stale or conflicting formal gate history.")

    phase_results["8"] = {
        "phase": 8,
        "name": PHASE_NAMES[8],
        "result": "BLOCKED" if routing_blockers else "ALLOWED",
        "phase_status": "PARTIAL_ROUTING_EXISTS_NEEDS_AUDIT" if routing_blockers else "READY_FOR_ROUTING",
        "next_required_phase": 8 if routing_blockers else 9,
        "blockers": routing_blockers,
        "evidence_decisions": evidence_decisions,
        "warnings": warnings,
    }

    return {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "project": project.name,
        "stale_reports_ignored": sorted(stale_files),
        "trace_geometry_blockers": trace_blockers,
        "phase_results": phase_results,
        "next_action": phase_results["8"]["blockers"][0] if phase_results["8"]["blockers"] else "Routing may continue with live evidence.",
    }


def render_gate_reconciliation_markdown(data: dict[str, Any]) -> str:
    lines = [
        "# Gate Reconciliation Report",
        "",
        f"Generated: `{data['generated_at']}`",
        "",
        f"Project: `{data['project']}`",
        "",
        "## Phase Results",
        "",
        "| Phase | Name | Result | Phase Status | Next Required Phase |",
        "| --- | --- | --- | --- | --- |",
    ]
    for key in ("2", "3", "8"):
        result = data["phase_results"][key]
        lines.append(
            f"| `{result['phase']}` | {result['name']} | `{result['result']}` | `{result['phase_status']}` | `{result['next_required_phase']}` |"
        )
    lines.extend(["", "## Evidence Decisions", ""])
    for key in ("2", "3", "8"):
        result = data["phase_results"][key]
        lines.append(f"### Phase `{key}`")
        for decision in result["evidence_decisions"]:
            lines.append(f"- `{decision['source']}`: {decision['message']}")
        if result["warnings"]:
            lines.append("Warnings:")
            for warning in result["warnings"]:
                lines.append(f"- {warning}")
        if result["blockers"]:
            lines.append("Blockers:")
            for blocker in result["blockers"]:
                lines.append(f"- {blocker}")
        lines.append("")
    lines.extend(["## Stale Reports Ignored", ""])
    if data["stale_reports_ignored"]:
        for path in data["stale_reports_ignored"]:
            lines.append(f"- `{path}`")
    else:
        lines.append("- None.")
    lines.append("")
    return "\n".join(lines)


def write_gate_reconciliation_outputs(project: Path, data: dict[str, Any]) -> None:
    dump_json(project / "reports" / "GATE_RECONCILIATION_REPORT.json", data)
    write_text(project / "reports" / "GATE_RECONCILIATION_REPORT.md", render_gate_reconciliation_markdown(data))


def current_state_markdown(live_state: dict[str, Any], reconciliation: dict[str, Any], repo_root: Path) -> str:
    pcb = live_state["pcb"]
    phase8 = reconciliation["phase_results"]["8"]
    lines = [
        "# Current Project State",
        "",
        "Status: `ACTIVE_EVIDENCE`",
        "",
        f"Generated date/time: `{live_state['generated_at']}`",
        "",
        f"Project: `{live_state['project']['name']}`",
        "",
        "Current relevance: authoritative project-state summary compiled from live KiCad files first, then reconciled fresh reports.",
        "",
        "## Current Truth",
        "",
        f"- Live PCB file exists with hash `{live_state['source_files']['kicad_pcb']['sha256']}`.",
        f"- Live board outline exists: `{pcb['board_width_mm']} mm x {pcb['board_height_mm']} mm`.",
        f"- Live footprint count: `{pcb['footprint_count']}`.",
        f"- Live mounting-hole count: `{pcb['mounting_hole_count']}`.",
        f"- Live routing inventory: `{pcb['track_count']}` tracks, `{pcb['via_count']}` vias, `{pcb['zone_count']}` zones.",
        f"- Detectable unrouted nets: `{pcb['unrouted_net_count']}`.",
        f"- Current DRC: `{live_state['drc']['result']}` with `{live_state['drc']['violation_count']}` violations and `{live_state['drc']['unconnected_count']}` unconnected items.",
        f"- Phase 2 status: `{reconciliation['phase_results']['2']['phase_status']}`.",
        f"- Phase 3 status: `{reconciliation['phase_results']['3']['phase_status']}`.",
        f"- Phase 8 status: `{reconciliation['phase_results']['8']['phase_status']}`.",
        "",
        "## Gates",
        "",
        f"- Routing allowed: `{'YES' if phase8['result'] == 'ALLOWED' else 'NO'}`",
        f"- Next allowed phase: `{reconciliation['phase_results']['8']['next_required_phase']} - {PHASE_NAMES[reconciliation['phase_results']['8']['next_required_phase']]}`",
        f"- Exact next action: `{live_state['next_action']}`",
        "",
        "## Authoritative Files",
        "",
        f"- `reports/LIVE_PROJECT_STATE.json`",
        f"- `reports/STALE_REPORTS_AUDIT.md`",
        f"- `reports/GATE_RECONCILIATION_REPORT.md`",
        "",
    ]
    return "\n".join(lines)


def current_blockers_markdown(live_state: dict[str, Any], reconciliation: dict[str, Any]) -> str:
    phase8 = reconciliation["phase_results"]["8"]
    lines = [
        "# Current Blockers",
        "",
        "Status: `ACTIVE_BLOCKER`",
        "",
        f"Generated date/time: `{live_state['generated_at']}`",
        "",
        f"Project: `{live_state['project']['name']}`",
        "",
        "| blocker | evidence | status |",
        "|---|---|---|",
    ]
    for blocker in phase8["blockers"]:
        lines.append(f"| {blocker} | `LIVE_PROJECT_STATE.json`; `GATE_RECONCILIATION_REPORT.md` | ACTIVE_BLOCKER |")
    for warning in phase8["warnings"]:
        lines.append(f"| {warning} | `GATE_RECONCILIATION_REPORT.md` | HUMAN_REVIEW_REQUIRED |")
    lines.append("")
    return "\n".join(lines)


def next_allowed_phase_markdown(reconciliation: dict[str, Any]) -> str:
    phase8 = reconciliation["phase_results"]["8"]
    lines = [
        "# Next Allowed Phase",
        "",
        "Status: `ACTIVE_EVIDENCE`",
        "",
        f"Generated date/time: `{reconciliation['generated_at']}`",
        "",
        "| next_allowed_phase | routing_allowed |",
        "|---|---|",
        f"| `{phase8['next_required_phase']} - {PHASE_NAMES[phase8['next_required_phase']]}` | `{'YES' if phase8['result'] == 'ALLOWED' else 'NO'}` |",
        "",
    ]
    return "\n".join(lines)


def update_phase_status_outputs(project: Path, repo_root: Path, live_state: dict[str, Any], reconciliation: dict[str, Any]) -> None:
    memory_dir = project / "memory"
    write_text(memory_dir / "CURRENT_PROJECT_STATE.md", current_state_markdown(live_state, reconciliation, repo_root))
    write_text(memory_dir / "CURRENT_BLOCKERS.md", current_blockers_markdown(live_state, reconciliation))
    write_text(memory_dir / "NEXT_ALLOWED_PHASE.md", next_allowed_phase_markdown(reconciliation))
