#!/usr/bin/env python3
"""Shared read-only helpers for schematic layout planning and scoring."""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[3]
QUALITY_DIR = SCRIPT_DIR.parent / "schematic_quality"
if str(QUALITY_DIR) not in sys.path:
    sys.path.insert(0, str(QUALITY_DIR))

from schematic_quality_common import (  # type: ignore  # noqa: E402
    BLOCK_DEFINITIONS,
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    CHECK_STATUS_WARN,
    assign_blocks,
    detect_native_annotation_status,
    extract_symbols,
    extract_text_items,
    extract_wire_segments,
    find_project_schematic,
    heading_positions,
    is_power_symbol,
    line_box_with_margin,
    load_schematic,
    rect_distance,
    rects_overlap,
    run_erc,
    symbol_search_text,
)


LABEL_KINDS = {"label", "global_label", "hierarchical_label"}

LAYOUT_TEMPLATE_ESP32_DEV_BOARD = {
    "template_id": "esp32_dev_board",
    "title": "ESP32 Dev Board",
    "blocks": {
        "input_power_protection": {
            "desired_region": "upper_left",
            "allowed_horizontal": {"left"},
            "allowed_vertical": {"upper", "middle"},
            "flow_notes": ["J1 -> fuse -> PMOS protection -> TVS/input caps -> regulator input"],
        },
        "buck_regulator": {
            "desired_region": "upper_left_to_center",
            "allowed_horizontal": {"left", "center"},
            "allowed_vertical": {"upper", "middle"},
            "flow_notes": ["U1 centered in block", "C6 tight to BST/SW", "L1 tight to SW", "C7/C8 at output"],
        },
        "esp32_module": {
            "desired_region": "center_or_upper_center",
            "allowed_horizontal": {"center", "right"},
            "allowed_vertical": {"upper", "middle"},
            "flow_notes": ["Leave whitespace around pins", "Keep local support readable"],
        },
        "usb_c_data": {
            "desired_region": "lower_left_or_center",
            "allowed_horizontal": {"left", "center"},
            "allowed_vertical": {"lower", "middle"},
            "flow_notes": ["J2 -> ESD -> R8/R9 -> ESP32 USB pins", "CC resistors near J2"],
        },
        "reset_boot": {
            "desired_region": "near_esp32",
            "allowed_horizontal": {"center", "right"},
            "allowed_vertical": {"upper", "middle", "lower"},
            "flow_notes": ["Keep EN/BOOT local to ESP32", "Prefer short wires or minimal labels"],
        },
        "leds": {
            "desired_region": "right_or_lower_right",
            "allowed_horizontal": {"center", "right"},
            "allowed_vertical": {"middle", "lower"},
            "flow_notes": ["Group LEDs together", "Keep resistors next to LEDs"],
        },
        "test_debug": {
            "desired_region": "lower_grouped_service_area",
            "allowed_horizontal": {"left", "center", "right"},
            "allowed_vertical": {"lower"},
            "flow_notes": ["Group test pads as one service/debug block"],
        },
        "mechanical_notes": {
            "desired_region": "separate_mechanical_area",
            "allowed_horizontal": {"left", "center", "right"},
            "allowed_vertical": {"upper", "middle", "lower"},
            "flow_notes": ["Keep mounting/mechanical notes separate from active circuitry"],
        },
    },
}

VISUAL_SCORE_WEIGHTS = {
    "block_grouping": 12,
    "local_wire_clarity": 10,
    "label_usage_balance": 8,
    "overlap_count": 10,
    "reference_readability": 8,
    "power_flow_readability": 12,
    "usb_path_readability": 10,
    "esp32_pin_readability": 10,
    "erc_status": 10,
    "annotation_status": 5,
    "footprint_status": 5,
}

SCHEMATIC_LAYOUT_PASS_SCORE = 85
SCHEMATIC_LAYOUT_WARN_SCORE = 70


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def timestamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def common_parser(description: str, allow_apply: bool = False) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--project", default="", help="Active project path containing a kicad/ folder.")
    parser.add_argument("--schematic", default="", help="Exact .kicad_sch path.")
    parser.add_argument("--output", default="", help="Optional Markdown output path.")
    parser.add_argument("--json-output", default="", help="Optional JSON output path.")
    parser.add_argument("--report-dir", default="", help="Optional report directory for companion outputs.")
    parser.add_argument("--no-fail", action="store_true", help="Return exit code 0 even when the result is FAIL.")
    if allow_apply:
        parser.add_argument("--apply", action="store_true", help="Allow schematic-writing mode.")
    return parser


def resolve_project_and_schematic(project_arg: str, schematic_arg: str) -> tuple[Path | None, Path]:
    if schematic_arg:
        schematic = Path(schematic_arg).resolve()
        project_root = Path(project_arg).resolve() if project_arg else None
        return project_root, schematic
    if not project_arg:
        raise SystemExit("Either --project or --schematic is required.")
    project_root = Path(project_arg).resolve()
    return project_root, find_project_schematic(project_root)


def point_in_bbox(x: float, y: float, bbox: dict[str, float], margin: float = 3.0) -> bool:
    return (bbox["x1"] - margin) <= x <= (bbox["x2"] + margin) and (bbox["y1"] - margin) <= y <= (bbox["y2"] + margin)


def schematic_bbox(symbols: list[dict[str, Any]]) -> dict[str, float]:
    non_power = [symbol for symbol in symbols if not is_power_symbol(symbol)]
    if not non_power:
        return {"x1": 0.0, "y1": 0.0, "x2": 1.0, "y2": 1.0}
    x1 = min(symbol["bbox"]["x1"] for symbol in non_power)
    y1 = min(symbol["bbox"]["y1"] for symbol in non_power)
    x2 = max(symbol["bbox"]["x2"] for symbol in non_power)
    y2 = max(symbol["bbox"]["y2"] for symbol in non_power)
    return {"x1": x1, "y1": y1, "x2": x2, "y2": y2}


def classify_region(x: float, y: float, bbox: dict[str, float]) -> dict[str, str]:
    width = max(1.0, bbox["x2"] - bbox["x1"])
    height = max(1.0, bbox["y2"] - bbox["y1"])
    x_ratio = (x - bbox["x1"]) / width
    y_ratio = (y - bbox["y1"]) / height
    horizontal = "left" if x_ratio < 0.34 else "right" if x_ratio > 0.67 else "center"
    vertical = "upper" if y_ratio < 0.34 else "lower" if y_ratio > 0.67 else "middle"
    return {"horizontal": horizontal, "vertical": vertical, "region": f"{vertical}_{horizontal}"}


def distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def find_symbols_in_block(block: dict[str, Any], keyword: str) -> list[dict[str, Any]]:
    keyword_lower = keyword.lower()
    return [symbol for symbol in block.get("symbols", []) if keyword_lower in symbol_search_text(symbol)]


def count_block_stats(blocks: dict[str, dict[str, Any]], text_items: list[dict[str, Any]], wires: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    label_items = [item for item in text_items if item["kind"] in LABEL_KINDS]
    stats: dict[str, dict[str, Any]] = {}
    for block_id, block in blocks.items():
        bbox = block["bbox"]
        block_labels = [item for item in label_items if point_in_bbox(item["at"]["x"], item["at"]["y"], bbox)]
        block_wires = [segment for segment in wires if point_in_bbox(segment["midpoint"]["x"], segment["midpoint"]["y"], bbox)]
        repeated = {
            label: count
            for label, count in Counter(item["text"] for item in block_labels).items()
            if count >= 3
        }
        pin_label_hits = 0
        for item in block_labels:
            point = (item["at"]["x"], item["at"]["y"])
            for symbol in block["symbols"]:
                if any(distance(point, (pin["x"], pin["y"])) <= 2.5 for pin in symbol.get("pin_points", [])):
                    pin_label_hits += 1
                    break
        stats[block_id] = {
            "label_count": len(block_labels),
            "wire_count": len(block_wires),
            "repeated_labels": repeated,
            "pin_label_hits": pin_label_hits,
            "symbol_count": block["symbol_count"],
            "references": [symbol.get("reference", "") for symbol in block["symbols"]],
        }
    return stats


def find_reference_readability_metrics(symbols: list[dict[str, Any]], text_items: list[dict[str, Any]], wires: list[dict[str, Any]]) -> dict[str, Any]:
    reference_items = [item for item in text_items if item["kind"] == "property:Reference"]
    overlapping: list[str] = []
    for item in reference_items:
        owner = item.get("owner_reference", "")
        collision = False
        for segment in wires:
            if rects_overlap(item["bbox"], line_box_with_margin(segment, margin=0.35)):
                collision = True
                break
        if not collision:
            for symbol in symbols:
                if symbol.get("reference") == owner:
                    continue
                if rects_overlap(item["bbox"], symbol["bbox"], margin=0.0):
                    collision = True
                    break
        if collision:
            overlapping.append(owner)
    return {
        "visible_reference_count": len(reference_items),
        "overlapping_reference_count": len(overlapping),
        "overlapping_references": sorted(reference for reference in overlapping if reference),
    }


def find_esp32_metrics(symbols: list[dict[str, Any]], text_items: list[dict[str, Any]]) -> dict[str, Any]:
    esp_symbols = [symbol for symbol in symbols if "esp32" in symbol_search_text(symbol) or "wroom" in symbol_search_text(symbol)]
    if not esp_symbols:
        return {"status": CHECK_STATUS_FAIL, "message": "No ESP32 module symbol was detected.", "whitespace_mm": 0.0, "text_collisions": 0}
    esp = esp_symbols[0]
    others = [symbol for symbol in symbols if not is_power_symbol(symbol) and symbol is not esp]
    whitespace = min((rect_distance(esp["bbox"], other["bbox"]) for other in others), default=10.0)
    text_collisions = 0
    for item in text_items:
        if item.get("owner_reference") == esp.get("reference"):
            continue
        if rects_overlap(item["bbox"], esp["bbox"], margin=0.0):
            text_collisions += 1
    if whitespace >= 3.0 and text_collisions == 0:
        status = CHECK_STATUS_PASS
        message = "ESP32 module has reasonable whitespace and no estimated foreign-text overlap."
    elif whitespace >= 1.5 and text_collisions <= 2:
        status = CHECK_STATUS_WARN
        message = "ESP32 module readability is usable but still tight."
    else:
        status = CHECK_STATUS_FAIL
        message = "ESP32 module area is visually crowded or text-overlapped."
    return {
        "status": status,
        "message": message,
        "reference": esp.get("reference", ""),
        "whitespace_mm": round(whitespace, 2),
        "text_collisions": text_collisions,
    }


def find_usb_metrics(context: dict[str, Any]) -> dict[str, Any]:
    usb_block = context["blocks"]["usb_c_data"]
    stats = context["block_stats"]["usb_c_data"]
    if usb_block["symbol_count"] == 0:
        return {"status": CHECK_STATUS_FAIL, "message": "USB block is missing.", "support_symbol_count": 0}
    connector_count = len([symbol for symbol in usb_block["symbols"] if symbol.get("reference", "").startswith("J") or "usb" in symbol_search_text(symbol)])
    support_symbols = [
        symbol
        for symbol in usb_block["symbols"]
        if symbol.get("reference", "").startswith("R") or "esd" in symbol_search_text(symbol) or "tvs" in symbol_search_text(symbol)
    ]
    if connector_count >= 1 and len(support_symbols) >= 3 and stats["wire_count"] >= max(2, stats["label_count"] // 2):
        status = CHECK_STATUS_PASS
        message = "USB connector and local support path look grouped and locally readable."
    elif connector_count >= 1 and len(support_symbols) >= 2:
        status = CHECK_STATUS_WARN
        message = "USB block exists but still relies on label-heavy or sparse support placement."
    else:
        status = CHECK_STATUS_FAIL
        message = "USB block is incomplete or not grouped clearly enough."
    return {
        "status": status,
        "message": message,
        "connector_count": connector_count,
        "support_symbol_count": len(support_symbols),
        "wire_count": stats["wire_count"],
        "label_count": stats["label_count"],
    }


def fraction_from_status(status: str) -> float:
    if status == CHECK_STATUS_PASS:
        return 1.0
    if status == CHECK_STATUS_WARN:
        return 0.6
    return 0.0


def default_report_dir(project_root: Path | None, schematic: Path) -> Path:
    if project_root is not None:
        return project_root / "reports" / "schematic_layout" / timestamp()
    return schematic.parent / "reports" / "schematic_layout" / timestamp()


def infer_project_root(schematic: Path) -> Path | None:
    resolved = schematic.resolve()
    parents = list(resolved.parents)
    for index, parent in enumerate(parents):
        if parent.name.lower() == "kicad" and index + 1 < len(parents):
            candidate = parents[index + 1]
            if (candidate / "kicad").exists():
                return candidate
    for parent in parents:
        if (parent / "kicad").exists():
            return parent
    return None


def ensure_report_dir(project_root: Path | None, schematic: Path, report_dir_arg: str) -> Path:
    return Path(report_dir_arg).resolve() if report_dir_arg else default_report_dir(project_root, schematic)


def load_layout_context(schematic: Path) -> dict[str, Any]:
    root = load_schematic(schematic)
    symbols = extract_symbols(root)
    text_items = extract_text_items(root, symbols)
    wires = extract_wire_segments(root)
    headings = heading_positions(text_items)
    blocks, unassigned = assign_blocks(symbols, headings)
    block_stats = count_block_stats(blocks, text_items, wires)
    diagram_bbox = schematic_bbox(symbols)
    block_regions = {
        block_id: classify_region(block["centroid"]["x"], block["centroid"]["y"], diagram_bbox)
        for block_id, block in blocks.items()
    }
    return {
        "generated_at": now_iso(),
        "schematic": str(schematic),
        "template_id": "esp32_dev_board" if any("esp32" in symbol_search_text(symbol) for symbol in symbols) else "generic",
        "diagram_bbox": diagram_bbox,
        "symbols": symbols,
        "text_items": text_items,
        "wires": wires,
        "headings": headings,
        "blocks": blocks,
        "block_regions": block_regions,
        "block_stats": block_stats,
        "unassigned_symbols": unassigned,
        "reference_metrics": find_reference_readability_metrics(symbols, text_items, wires),
        "esp32_metrics": find_esp32_metrics(symbols, text_items),
        "usb_metrics": find_usb_metrics(
            {
                "blocks": blocks,
                "block_stats": block_stats,
            }
        ),
    }


def serializable_blocks(context: dict[str, Any]) -> dict[str, Any]:
    payload: dict[str, Any] = {}
    for block_id, block in context["blocks"].items():
        payload[block_id] = {
            "title": block["title"],
            "heading_text": block["heading_text"],
            "heading_at": block["heading_at"],
            "bbox": block["bbox"],
            "centroid": block["centroid"],
            "symbol_count": block["symbol_count"],
            "references": [symbol.get("reference", "") for symbol in block["symbols"]],
            "region": context["block_regions"][block_id],
            "stats": context["block_stats"][block_id],
        }
    return payload


def layout_summary_markdown(title: str, schematic: Path, sections: list[str]) -> str:
    lines = [
        f"# {title}",
        "",
        f"Generated: `{now_iso()}`",
        f"Schematic: `{schematic}`",
        "",
    ]
    lines.extend(sections)
    lines.append("")
    return "\n".join(lines)


def write_markdown_and_json(markdown: str, data: dict[str, Any], output: Path | None, json_output: Path | None) -> None:
    if json_output:
        json_output.parent.mkdir(parents=True, exist_ok=True)
        json_output.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(markdown, encoding="utf-8")
    else:
        print(markdown)


def points_for_status(status: str, weight: int) -> float:
    if status == CHECK_STATUS_PASS:
        return float(weight)
    if status == CHECK_STATUS_WARN:
        return round(weight * 0.6, 2)
    return 0.0


def numeric_score_from_status(status: str) -> int:
    if status == CHECK_STATUS_PASS:
        return 100
    if status == CHECK_STATUS_WARN:
        return 60
    return 0


def summarize_counts(findings: list[dict[str, Any]]) -> dict[str, int]:
    counts = {CHECK_STATUS_PASS: 0, CHECK_STATUS_WARN: 0, CHECK_STATUS_FAIL: 0}
    for item in findings:
        status = item.get("status", "")
        if status in counts:
            counts[status] += 1
    return counts


def overall_status_from_scores(category_statuses: dict[str, str], total_score: int) -> str:
    hard_fail_categories = {
        "block_grouping",
        "local_wire_clarity",
        "overlap_count",
        "power_flow_readability",
        "erc_status",
        "annotation_status",
        "footprint_status",
    }
    if any(category_statuses.get(name) == CHECK_STATUS_FAIL for name in hard_fail_categories):
        return CHECK_STATUS_FAIL
    if total_score < SCHEMATIC_LAYOUT_WARN_SCORE:
        return CHECK_STATUS_FAIL
    if CHECK_STATUS_FAIL in category_statuses.values():
        return CHECK_STATUS_WARN
    if total_score < SCHEMATIC_LAYOUT_PASS_SCORE or CHECK_STATUS_WARN in category_statuses.values():
        return CHECK_STATUS_WARN
    return CHECK_STATUS_PASS
