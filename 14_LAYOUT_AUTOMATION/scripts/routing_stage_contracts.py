#!/usr/bin/env python3
"""Shared stage contracts and report-parsing helpers for staged routing."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = next((path for path in [SCRIPT_DIR, *SCRIPT_DIR.parents] if (path / "AGENTS.md").exists()), SCRIPT_DIR).resolve()

STAGE_ORDER = [
    "placement_readiness",
    "power_critical",
    "ground_strategy",
    "USB_support",
    "boot_enable_control",
    "USB_data",
    "low_speed_remaining",
    "trace_geometry_cleanup",
    "final_connectivity",
    "final_visual_review",
]

STAGE_INDEX = {name: index for index, name in enumerate(STAGE_ORDER)}

POWER_NETS = {"/+5V_IN", "/+5V_FUSED", "/+5V_PROTECTED", "/BUCK_SW", "/BUCK_BST", "+3V3", "3V3", "GND"}
USB_SUPPORT_NETS = {"/CC1", "/CC2", "/SHIELD"}
BOOT_ENABLE_NETS = {"/BOOT0", "/ESP_EN", "/U0RXD", "/U0TXD"}
USB_DATA_NETS = {"/DP_C", "/DP_E", "/DM_C", "/DM_E"}
LOW_SPEED_NETS = {"/PLED", "/SLED", "/STATUS_LED", "TP", "LED", "BUTTON"}
GEOMETRY_HARD_FAIL_STATUSES = {
    "RIGHT_ANGLE_FOUND",
    "ACUTE_JOG_FOUND",
    "PAD_ENTRY_GEOMETRY_POOR",
    "UNNECESSARY_ZIGZAG_FOUND",
    "CRITICAL_LOOP_DETOUR_FOUND",
    "KEEP_OUT_CROSSING_FOUND",
    "UNJUSTIFIED_VIA_FOUND",
    "TRACE_WIDTH_MISMATCH_FOUND",
}
BLOCKER_SECTION_KEYWORDS = {
    "deferred nets",
    "remaining unrouted nets",
    "affected nets",
    "remaining blockers",
    "remaining must-route buckets",
    "unconnected bucket summary",
    "exact stop reason",
    "remaining connectivity buckets",
    "remaining nets before edit",
}
REPORT_GLOBS = [
    "reports/PCB_BATCH_*_REPORT.md",
    "reports/REAL_PCB_*_REPORT.md",
    "reports/PCB_FINAL_CONNECTIVITY_CLEANUP_REPORT.md",
    "reports/FINAL_TRACE_BY_TRACE_AUDIT_REPORT.md",
]


@dataclass(frozen=True)
class RoutingStageContract:
    name: str
    required_input_files: list[str]
    allowed_nets: list[str]
    forbidden_nets: list[str]
    drc_requirement: str
    geometry_requirement: str
    hash_delta_required: bool
    copied_board_rehearsal_required: bool
    pass_output: str
    fail_outputs: list[str]
    next_allowed_stage: str | None


STAGE_CONTRACTS: dict[str, RoutingStageContract] = {
    "placement_readiness": RoutingStageContract(
        name="placement_readiness",
        required_input_files=[
            "reports/LIVE_PROJECT_STATE.json",
            "reports/PLACEMENT_READINESS_SCORECARD.md",
            "reports/PCB_PLACEMENT_CURRENT_STATE_REPORT.md",
        ],
        allowed_nets=[],
        forbidden_nets=["ALL_ROUTING_EDITS"],
        drc_requirement="No new routing edits; placement evidence may still show unconnected items.",
        geometry_requirement="Placement scorecard must be exact PLACEMENT_READY_FOR_ROUTING.",
        hash_delta_required=False,
        copied_board_rehearsal_required=False,
        pass_output="PLACEMENT_READY_FOR_ROUTING",
        fail_outputs=["PLACEMENT_REPAIR_REQUIRED", "PLACEMENT_BLOCKED_HUMAN_REVIEW"],
        next_allowed_stage="power_critical",
    ),
    "power_critical": RoutingStageContract(
        name="power_critical",
        required_input_files=[
            "reports/LIVE_PROJECT_STATE.json",
            "reports/PLACEMENT_READINESS_SCORECARD.md",
            "reports/REAL_PCB_ROUTING_PLAN.md",
            "reports/ROUTING_PRECHECK_SCORECARD.md",
            "routing_work/*/ROUTING_MASTER_LOG.md",
        ],
        allowed_nets=sorted(POWER_NETS - {"GND"}),
        forbidden_nets=sorted(USB_SUPPORT_NETS | BOOT_ENABLE_NETS | USB_DATA_NETS),
        drc_requirement="No new DRC violations; unconnected and unrouted counts must not worsen.",
        geometry_requirement="No power-path geometry hard fail or critical-loop detour.",
        hash_delta_required=True,
        copied_board_rehearsal_required=True,
        pass_output="POWER_CRITICAL_STAGE_PASS",
        fail_outputs=["POWER_CRITICAL_STAGE_BLOCKED", "BLOCKED_REPAIR_MODE"],
        next_allowed_stage="ground_strategy",
    ),
    "ground_strategy": RoutingStageContract(
        name="ground_strategy",
        required_input_files=[
            "reports/LIVE_PROJECT_STATE.json",
            "reports/ROUTING_START_BLOCKERS.md",
            "reports/PCB_BATCH_01_DRC_AND_GND_REPAIR_REPORT.md",
        ],
        allowed_nets=["GND"],
        forbidden_nets=sorted((POWER_NETS - {"GND"}) | USB_SUPPORT_NETS | BOOT_ENABLE_NETS | USB_DATA_NETS),
        drc_requirement="No new DRC violations; GND disconnect bucket must reduce or be explicitly accepted.",
        geometry_requirement="No antenna-keepout or return-path hard fail.",
        hash_delta_required=True,
        copied_board_rehearsal_required=True,
        pass_output="GROUND_STRATEGY_STAGE_PASS",
        fail_outputs=["GROUND_STRATEGY_STAGE_BLOCKED", "BLOCKED_REPAIR_MODE"],
        next_allowed_stage="USB_support",
    ),
    "USB_support": RoutingStageContract(
        name="USB_support",
        required_input_files=[
            "reports/LIVE_PROJECT_STATE.json",
            "reports/REAL_PCB_ROUTING_PLAN.md",
            "reports/PCB_BATCH_03_USB_CONTROL_ROUTING_REPORT.md",
        ],
        allowed_nets=sorted(USB_SUPPORT_NETS),
        forbidden_nets=sorted((POWER_NETS - {"GND"}) | BOOT_ENABLE_NETS | USB_DATA_NETS),
        drc_requirement="No new DRC violations; USB support branches may reduce unconnected items without starting D+/D-.",
        geometry_requirement="No USB support geometry hard fail; no ugly shield/CC detours.",
        hash_delta_required=True,
        copied_board_rehearsal_required=True,
        pass_output="USB_SUPPORT_STAGE_PASS",
        fail_outputs=["USB_SUPPORT_STAGE_BLOCKED", "BLOCKED_REPAIR_MODE"],
        next_allowed_stage="boot_enable_control",
    ),
    "boot_enable_control": RoutingStageContract(
        name="boot_enable_control",
        required_input_files=[
            "reports/LIVE_PROJECT_STATE.json",
            "reports/PCB_BATCH_04_CONTROL_NET_ROUTING_REPORT.md",
        ],
        allowed_nets=sorted(BOOT_ENABLE_NETS),
        forbidden_nets=sorted(USB_DATA_NETS),
        drc_requirement="No new DRC violations; BOOT0 and ESP_EN blockers must reduce before USB data starts.",
        geometry_requirement="No crude control-net jogs or same-blocker replay without targeted repair.",
        hash_delta_required=True,
        copied_board_rehearsal_required=True,
        pass_output="BOOT_ENABLE_CONTROL_STAGE_PASS",
        fail_outputs=["BOOT_ENABLE_CONTROL_STAGE_BLOCKED", "BLOCKED_REPAIR_MODE"],
        next_allowed_stage="USB_data",
    ),
    "USB_data": RoutingStageContract(
        name="USB_data",
        required_input_files=[
            "reports/LIVE_PROJECT_STATE.json",
            "reports/PCB_BATCH_05_USB_DATA_ROUTING_REPORT.md",
        ],
        allowed_nets=sorted(USB_DATA_NETS),
        forbidden_nets=["UNRELATED_NETS"],
        drc_requirement="Must preserve zero new DRC violations while reducing USB data unrouted buckets.",
        geometry_requirement="Must pass geometry hard-fail checker with no DP/DM pair degradation.",
        hash_delta_required=True,
        copied_board_rehearsal_required=True,
        pass_output="USB_DATA_STAGE_PASS",
        fail_outputs=["USB_DATA_STAGE_BLOCKED", "BLOCKED_REPAIR_MODE"],
        next_allowed_stage="low_speed_remaining",
    ),
    "low_speed_remaining": RoutingStageContract(
        name="low_speed_remaining",
        required_input_files=[
            "reports/LIVE_PROJECT_STATE.json",
            "reports/REAL_PCB_FULL_ROUTING_PASS_REPORT.md",
        ],
        allowed_nets=["LOW_SPEED_REMAINING", "LEDS", "BUTTONS", "TEST_PADS"],
        forbidden_nets=sorted(USB_DATA_NETS),
        drc_requirement="No new DRC violations; remaining low-speed nets should only start after critical stages are stable.",
        geometry_requirement="No geometry hard fails on any new low-speed work.",
        hash_delta_required=True,
        copied_board_rehearsal_required=True,
        pass_output="LOW_SPEED_REMAINING_STAGE_PASS",
        fail_outputs=["LOW_SPEED_REMAINING_STAGE_BLOCKED", "BLOCKED_REPAIR_MODE"],
        next_allowed_stage="trace_geometry_cleanup",
    ),
    "trace_geometry_cleanup": RoutingStageContract(
        name="trace_geometry_cleanup",
        required_input_files=[
            "reports/LIVE_PROJECT_STATE.json",
            "reports/FINAL_TRACE_BY_TRACE_AUDIT_REPORT.md",
        ],
        allowed_nets=["ANY_EXISTING_ROUTED_NET"],
        forbidden_nets=["NEW_SCOPE_EXPANSION"],
        drc_requirement="No new DRC violations; cleanup may leave connectivity unchanged if geometry improves.",
        geometry_requirement="Must remove hard-fail geometry from existing traces.",
        hash_delta_required=True,
        copied_board_rehearsal_required=True,
        pass_output="TRACE_GEOMETRY_CLEANUP_STAGE_PASS",
        fail_outputs=["TRACE_GEOMETRY_CLEANUP_STAGE_BLOCKED", "BLOCKED_REPAIR_MODE"],
        next_allowed_stage="final_connectivity",
    ),
    "final_connectivity": RoutingStageContract(
        name="final_connectivity",
        required_input_files=[
            "reports/LIVE_PROJECT_STATE.json",
            "reports/PCB_FINAL_CONNECTIVITY_CLEANUP_REPORT.md",
            "reports/PCB_FINAL_UNCONNECTED_ITEMS_REVIEW.md",
        ],
        allowed_nets=["REMAINING_SAFE_MUST_ROUTE", "INTENTIONAL_OPEN_CLASSIFICATION"],
        forbidden_nets=["BROAD_RESTART"],
        drc_requirement="No new DRC violations; remaining unconnected items must reduce or be explicitly classified.",
        geometry_requirement="No geometry regressions while closing remaining safe connectivity gaps.",
        hash_delta_required=True,
        copied_board_rehearsal_required=True,
        pass_output="FINAL_CONNECTIVITY_STAGE_PASS",
        fail_outputs=["FINAL_CONNECTIVITY_STAGE_BLOCKED", "BLOCKED_REPAIR_MODE"],
        next_allowed_stage="final_visual_review",
    ),
    "final_visual_review": RoutingStageContract(
        name="final_visual_review",
        required_input_files=[
            "reports/FINAL_PCB_VISUAL_REVIEW_PACKET.md",
            "reports/LJ_FINAL_PCB_REVIEW_CHECKLIST.md",
        ],
        allowed_nets=[],
        forbidden_nets=["ALL_ROUTING_EDITS"],
        drc_requirement="Read-only review stage. No new routing edits allowed.",
        geometry_requirement="Visual review package must exist and remaining risks must be explicit.",
        hash_delta_required=False,
        copied_board_rehearsal_required=False,
        pass_output="FINAL_VISUAL_REVIEW_READY",
        fail_outputs=["FINAL_VISUAL_REVIEW_BLOCKED"],
        next_allowed_stage=None,
    ),
}


def load_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def dump_json(path: str | Path, payload: dict[str, Any]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def dump_markdown(path: str | Path, text: str) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(text.rstrip() + "\n", encoding="utf-8")


def repo_root_from(repo_root: str | Path | None = None) -> Path:
    return Path(repo_root).resolve() if repo_root else REPO_ROOT


def resolve_project_path(repo_root: str | Path | None, project: str | Path) -> Path:
    root = repo_root_from(repo_root)
    candidate = Path(project)
    return candidate.resolve() if candidate.is_absolute() else (root / candidate).resolve()


def stage_contract(stage_name: str) -> RoutingStageContract:
    key = stage_name.strip()
    if key not in STAGE_CONTRACTS:
        raise KeyError(f"Unknown routing stage: {stage_name}")
    return STAGE_CONTRACTS[key]


def next_stage_name(stage_name: str) -> str | None:
    return stage_contract(stage_name).next_allowed_stage


def expand_required_matches(project: Path, patterns: list[str]) -> dict[str, list[str]]:
    matches: dict[str, list[str]] = {}
    for pattern in patterns:
        found = [str(path.relative_to(project)) for path in sorted(project.glob(pattern)) if path.exists()]
        matches[pattern] = found
    return matches


def extract_status(text: str) -> str:
    match = re.search(r"Status:\s*`([^`]+)`", text)
    return match.group(1).strip() if match else "STATUS_NOT_FOUND"


def parse_datetime(text: str) -> str | None:
    patterns = [
        r"Generated(?: date/time)?:\s*`([^`]+)`",
        r"Date:\s*`([^`]+)`",
        r"Timestamp:\s*`([^`]+)`",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1).strip()
    return None


def sort_key_for_timestamp(value: str | None) -> tuple[int, str]:
    if not value:
        return (1, "")
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d %H:%M:%S %z", "%Y-%m-%d"):
        try:
            parsed = datetime.strptime(value, fmt)
            return (0, parsed.isoformat())
        except ValueError:
            continue
    return (0, value)


def extract_hash(text: str, which: str) -> str | None:
    patterns = {
        "before": [
            r"(?:PCB|Live PCB) hash before(?: [A-Za-z ]+)?:\s*`([0-9A-Fa-f]{64})`",
            r"PCB SHA256 before:\s*`([0-9A-Fa-f]{64})`",
            r"Live PCB hash at resume:\s*`([0-9A-Fa-f]{64})`",
        ],
        "after": [
            r"(?:PCB|Live PCB) hash after(?: [A-Za-z ]+)?:\s*`([0-9A-Fa-f]{64})`",
            r"PCB SHA256 after:\s*`([0-9A-Fa-f]{64})`",
        ],
    }
    for pattern in patterns[which]:
        match = re.search(pattern, text)
        if match:
            return match.group(1).upper()
    return None


def extract_changed_flag(text: str) -> bool | None:
    match = re.search(r"(?:Live )?PCB changed:\s*`(YES|NO)`", text)
    if not match:
        return None
    return match.group(1) == "YES"


def split_markdown_sections(text: str) -> list[tuple[str, list[str]]]:
    sections: list[tuple[str, list[str]]] = []
    current_heading = "__preamble__"
    current_lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("## "):
            sections.append((current_heading, current_lines))
            current_heading = line[3:].strip().lower()
            current_lines = []
            continue
        current_lines.append(line)
    sections.append((current_heading, current_lines))
    return sections


def text_for_sections(text: str, keywords: tuple[str, ...]) -> str:
    chunks: list[str] = []
    for heading, lines in split_markdown_sections(text):
        if any(keyword in heading for keyword in keywords):
            chunks.append("\n".join(lines))
    return "\n".join(chunks)


def first_int(value: str) -> int | None:
    match = re.search(r"`?(\d+)`?", value)
    return int(match.group(1)) if match else None


def labeled_value(text: str, labels: list[str]) -> int | None:
    for label in labels:
        pattern = rf"{label}\s*:\s*`?(\d+)`?"
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return int(match.group(1))
    return None


def labeled_count(text: str, labels: list[str], unit_pattern: str) -> int | None:
    for label in labels:
        pattern = rf"{label}\s*:\s*[^\n]*?`?(\d+)`?\s+{unit_pattern}"
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return int(match.group(1))
    return None


def labeled_pair_count(text: str, labels: list[str], second_unit_pattern: str) -> int | None:
    for label in labels:
        pattern = rf"{label}\s*:\s*[^\n]*?`?\d+`?\s+[A-Za-z ]+,\s*`?(\d+)`?\s+{second_unit_pattern}"
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return int(match.group(1))
    return None


def section_list_items(text: str, section_keywords: tuple[str, ...]) -> list[str]:
    items: list[str] = []
    current_enabled = False
    for line in text.splitlines():
        if line.startswith("## "):
            heading = line[3:].strip().lower()
            current_enabled = any(keyword in heading for keyword in section_keywords)
            continue
        if not current_enabled:
            continue
        stripped = line.strip()
        if stripped.startswith("- "):
            items.append(stripped[2:].strip())
    return items


def extract_net_tokens(text: str) -> list[str]:
    raw = re.findall(r"(?:/(?:[A-Za-z0-9_+\-]{2,})|\+3V3|3V3|GND|VBUS)", text)
    return sorted(set(item.upper() for item in raw))


def extract_blocker_tokens(text: str) -> list[str]:
    tokens: set[str] = set()
    for heading, lines in split_markdown_sections(text):
        if not any(keyword in heading for keyword in BLOCKER_SECTION_KEYWORDS):
            continue
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("- ") or stripped.startswith("|"):
                tokens.update(extract_net_tokens(stripped))
    return sorted(tokens)


def infer_stage_from_report(name: str, text: str) -> str:
    upper_name = name.upper()
    if "PLACEMENT_READINESS" in upper_name:
        return "placement_readiness"
    if "BATCH_01" in upper_name or "GND_REPAIR" in upper_name or "REPAIR_PASS_1" in upper_name:
        return "ground_strategy"
    if "BATCH_02" in upper_name or "POWER_ROUTING" in upper_name or "CRITICAL_ROUTING_PASS" in upper_name:
        return "power_critical"
    if "FULL_ROUTING" in upper_name:
        return "low_speed_remaining"
    if "FINAL_CONNECTIVITY" in upper_name:
        return "final_connectivity"
    if "FINAL_TRACE" in upper_name or "TRACE_BY_TRACE" in upper_name:
        return "trace_geometry_cleanup"
    if "BATCH_03" in upper_name or "USB_CONTROL" in upper_name:
        return "USB_support"
    if "BATCH_04" in upper_name or "BOOT_EN" in upper_name or "CONTROL_NET" in upper_name:
        return "boot_enable_control"
    if "BATCH_05" in upper_name or "USB_DATA" in upper_name:
        return "USB_data"
    return "low_speed_remaining"


def report_candidate_paths(project: Path) -> list[Path]:
    candidates: set[Path] = set()
    for pattern in REPORT_GLOBS:
        candidates.update(path.resolve() for path in project.glob(pattern) if path.is_file())
    excluded_markers = (
        "_DRC_REPORT.md",
        "_UNROUTED_NETS.md",
        "_TRACE_CHANGE_SUMMARY.md",
        "_TRACE_AUDIT.md",
    )
    return sorted(path for path in candidates if not any(path.name.upper().endswith(marker.upper()) for marker in excluded_markers))


def parse_routing_report(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="replace")
    changed = extract_changed_flag(text)
    hash_before = extract_hash(text, "before")
    hash_after = extract_hash(text, "after")
    status = extract_status(text)
    generated = parse_datetime(text)
    if changed is None and hash_before and hash_after:
        changed = hash_before != hash_after

    preferred_metric_text = "\n".join(
        filter(
            None,
            [
                text_for_sections(text, ("verification", "drc result", "result", "final result", "live preconditions", "audit scope")),
                text,
            ],
        )
    )

    violations_before = labeled_value(
        text,
        [
            r"DRC violations before",
            r"Violations before",
        ],
    )
    if violations_before is None:
        violations_before = labeled_count(
        text,
        [
            r"DRC before repair",
            r"Pre-edit live DRC",
            r"Fresh DRC before edit",
            r"DRC before cleanup",
            r"Critical-pass DRC did not get worse",
        ],
        "violations",
    )
    violations_after = labeled_value(
        preferred_metric_text,
        [
            r"DRC violations(?: after)?",
            r"Violations",
        ],
    )
    if violations_after is None:
        violations_after = labeled_count(
        preferred_metric_text,
        [
            r"Post-edit DRC",
            r"DRC after repair",
            r"Post-edit live DRC",
            r"Current live DRC",
            r"DRC before repair",
            r"Pre-audit DRC",
        ],
        "violations",
    )

    unconnected_before = labeled_value(
        text,
        [
            r"Unconnected before",
            r"Unconnected items before",
        ],
    )
    if unconnected_before is None:
        unconnected_before = labeled_count(
        text,
        [
            r"Pre-edit live DRC",
            r"Fresh DRC before edit",
            r"Pre-edit live DRC",
            r"Fresh DRC before edit",
            r"DRC before cleanup",
            r"Critical-pass DRC did not get worse",
            r"DRC before repair",
        ],
        "unconnected items",
    )
    unconnected_after = labeled_value(
        preferred_metric_text,
        [
            r"Unconnected items after",
            r"Unconnected after",
            r"DRC unconnected items",
            r"Unconnected items",
        ],
    )
    if unconnected_after is None:
        unconnected_after = labeled_count(
        preferred_metric_text,
        [
            r"Post-edit DRC",
            r"DRC after repair",
            r"Post-edit live DRC",
            r"Current live DRC",
            r"DRC before repair",
            r"Pre-audit DRC",
        ],
        "unconnected items",
    )

    unrouted_before = labeled_value(
        text,
        [
            r"Detectable unrouted nets before",
            r"Current detectable unrouted nets before",
        ],
    )
    if unrouted_before is None:
        unrouted_before = labeled_count(
        text,
        [
            r"Current detectable unrouted nets before",
        ],
        "detectable unrouted nets",
    )
    if unrouted_before is None:
        before_items = section_list_items(text, ("remaining nets before edit",))
        if before_items:
            unrouted_before = len([item for item in before_items if extract_net_tokens(item)])

    unrouted_after = labeled_value(
        preferred_metric_text,
        [
            r"Detectable unrouted nets after",
            r"Detectable unrouted nets remaining",
            r"Current detectable unrouted nets",
        ],
    )
    if unrouted_after is None:
        unrouted_after = labeled_count(
        preferred_metric_text,
        [
            r"Current detectable unrouted nets",
        ],
        "detectable unrouted nets",
    )
    if unrouted_after is None:
        remaining_items = section_list_items(text, ("remaining unrouted nets",))
        if remaining_items:
            unrouted_after = len([item for item in remaining_items if extract_net_tokens(item)])

    blocker_tokens = extract_blocker_tokens(text)
    geometry_failures = sorted({item for item in GEOMETRY_HARD_FAIL_STATUSES if item in text})

    record = {
        "file": str(path),
        "name": path.name,
        "stage": infer_stage_from_report(path.name, text),
        "generated_at": generated,
        "status": status,
        "pcb_hash_before": hash_before,
        "pcb_hash_after": hash_after,
        "pcb_changed": changed,
        "drc_violations_before": violations_before,
        "drc_violations_after": violations_after,
        "unconnected_before": unconnected_before,
        "unconnected_after": unconnected_after,
        "unrouted_before": unrouted_before,
        "unrouted_after": unrouted_after,
        "blocker_tokens": blocker_tokens,
        "geometry_failures": geometry_failures,
        "metrics_confident": bool(
            hash_before
            or hash_after
            or isinstance(unconnected_after, int)
            or isinstance(unrouted_after, int)
            or isinstance(violations_after, int)
        ),
        "text": text,
    }
    return record


def discover_edit_required_runs(project: Path) -> list[dict[str, Any]]:
    runs = [parse_routing_report(path) for path in report_candidate_paths(project)]
    runs = [
        run
        for run in runs
        if run["pcb_hash_before"] or run["pcb_hash_after"] or run["pcb_changed"] is not None or run["metrics_confident"]
    ]
    runs.sort(key=lambda item: (sort_key_for_timestamp(item["generated_at"]), item["name"]))
    previous_after_hash: str | None = None
    previous_unconnected: int | None = None
    previous_unrouted: int | None = None
    previous_violations: int | None = None
    for run in runs:
        if run["pcb_hash_before"] is None:
            run["pcb_hash_before"] = previous_after_hash
        if run["pcb_hash_after"] is None:
            run["pcb_hash_after"] = run["pcb_hash_before"]
        if run["pcb_changed"] is None and run["pcb_hash_before"] and run["pcb_hash_after"]:
            run["pcb_changed"] = run["pcb_hash_before"] != run["pcb_hash_after"]
        if run["unconnected_before"] is None:
            run["unconnected_before"] = previous_unconnected
        if run["unrouted_before"] is None:
            run["unrouted_before"] = previous_unrouted
        if run["drc_violations_before"] is None:
            run["drc_violations_before"] = previous_violations
        run["hash_changed"] = bool(run["pcb_changed"])
        run["unconnected_delta"] = (
            run["unconnected_after"] - run["unconnected_before"]
            if isinstance(run["unconnected_before"], int) and isinstance(run["unconnected_after"], int)
            else None
        )
        run["unrouted_delta"] = (
            run["unrouted_after"] - run["unrouted_before"]
            if isinstance(run["unrouted_before"], int) and isinstance(run["unrouted_after"], int)
            else None
        )
        run["drc_worsened"] = (
            run["drc_violations_after"] > run["drc_violations_before"]
            if isinstance(run["drc_violations_before"], int) and isinstance(run["drc_violations_after"], int)
            else False
        )
        run["progress_comparable"] = bool(
            isinstance(run["unconnected_delta"], int) or isinstance(run["unrouted_delta"], int)
        )
        run["drc_comparable"] = bool(
            isinstance(run["drc_violations_before"], int) and isinstance(run["drc_violations_after"], int)
        )
        run["made_progress"] = bool(
            (isinstance(run["unconnected_delta"], int) and run["unconnected_delta"] < 0)
            or (isinstance(run["unrouted_delta"], int) and run["unrouted_delta"] < 0)
        )
        previous_after_hash = run["pcb_hash_after"] or previous_after_hash
        previous_unconnected = run["unconnected_after"] if isinstance(run["unconnected_after"], int) else previous_unconnected
        previous_unrouted = run["unrouted_after"] if isinstance(run["unrouted_after"], int) else previous_unrouted
        previous_violations = run["drc_violations_after"] if isinstance(run["drc_violations_after"], int) else previous_violations
    return runs


def latest_live_state(project: Path) -> dict[str, Any] | None:
    path = project / "reports" / "LIVE_PROJECT_STATE.json"
    return load_json(path) if path.exists() else None


def latest_placement_scorecard_status(project: Path) -> str | None:
    path = project / "reports" / "PLACEMENT_READINESS_SCORECARD.md"
    if not path.exists():
        return None
    return extract_status(path.read_text(encoding="utf-8", errors="replace"))


def stale_report_count(project: Path) -> int:
    path = project / "reports" / "STALE_REPORTS_AUDIT.json"
    if not path.exists():
        return 0
    payload = load_json(path)
    return len(payload.get("stale_rows", []))


def reroute_revert_metrics(project: Path) -> dict[str, int]:
    routing_work_root = project / "routing_work"
    trace_log = next(iter(sorted(routing_work_root.glob("*/TRACE_CHANGE_LOG.md"))), None)
    decision_log = next(iter(sorted(routing_work_root.glob("*/ROUTING_DECISION_LOG.md"))), None)
    reroute_count = 0
    revert_count = 0
    if trace_log and trace_log.exists():
        text = trace_log.read_text(encoding="utf-8", errors="replace")
        reroute_count = len(re.findall(r"track reroute|trace cleanup|zone settings", text, flags=re.IGNORECASE))
    if decision_log and decision_log.exists():
        text = decision_log.read_text(encoding="utf-8", errors="replace")
        revert_count = len(re.findall(r"rejected|rollback|revert", text, flags=re.IGNORECASE))
    return {"reroute_count": reroute_count, "revert_count": revert_count}


def repeated_blocker_signature(run: dict[str, Any]) -> tuple[str, ...]:
    if run["blocker_tokens"]:
        return tuple(sorted(set(run["blocker_tokens"])))
    return tuple()


def recommended_stage_for_blockers(blockers: list[str]) -> tuple[str, str]:
    upper = {item.upper() for item in blockers}
    if {"GND"} & upper:
        return (
            "ground_strategy",
            "Repair the GND strategy only: close the return-path blocker or explicitly accept the remaining GND disconnect bucket before broad routing resumes.",
        )
    if upper & {item.upper() for item in POWER_NETS if item != "GND"}:
        return (
            "power_critical",
            "Repair the power/protection cluster only and confirm the current-loop geometry before any unrelated routing stage resumes.",
        )
    if upper & {item.upper() for item in BOOT_ENABLE_NETS}:
        return (
            "boot_enable_control",
            "Run one copied-board rehearsal focused only on /BOOT0 and /ESP_EN, then apply that targeted repair before revisiting USB data or broad routing.",
        )
    if upper & {item.upper() for item in USB_SUPPORT_NETS}:
        return (
            "USB_support",
            "Repair only the USB support cluster (/CC1, /CC2, /SHIELD) before escalating to later routing stages.",
        )
    if upper & {item.upper() for item in USB_DATA_NETS}:
        return (
            "USB_data",
            "Run a copied-board D+/D- rehearsal only after all earlier blockers are cleared, then apply only the clean paired USB data geometry.",
        )
    return (
        "trace_geometry_cleanup",
        "Stop broad routing and perform one targeted geometry cleanup pass on the repeated failing area before resuming stage progression.",
    )
