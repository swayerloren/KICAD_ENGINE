#!/usr/bin/env python3
"""Generate close-up schematic visual review crops from a KiCad SVG export.

This script is read-only with respect to KiCad project files. It writes only
configured visual review outputs: crop SVG/PNG files, Markdown review stubs,
and optional JSON summaries.
"""

from __future__ import annotations

import argparse
import html
import json
import math
import os
import re
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import quote


DEFAULT_BLOCKS = [
    ("input_power", "Input Power", 0.02, 0.06, 0.22, 0.24),
    ("reverse_polarity", "Reverse Polarity", 0.22, 0.06, 0.23, 0.24),
    ("tvs_input_cap", "TVS And Input Cap", 0.02, 0.28, 0.23, 0.24),
    ("buck_regulator", "Buck Regulator", 0.24, 0.28, 0.27, 0.26),
    ("esp32_module", "ESP32 Module", 0.50, 0.12, 0.30, 0.42),
    ("usb_c_connector", "USB-C Connector", 0.02, 0.56, 0.22, 0.24),
    ("usb_esd", "USB ESD", 0.23, 0.56, 0.18, 0.22),
    ("cc_resistors", "CC Resistors", 0.39, 0.56, 0.18, 0.22),
    ("reset_boot", "Reset And Boot", 0.50, 0.56, 0.22, 0.22),
    ("leds", "LEDs", 0.71, 0.56, 0.23, 0.22),
    ("test_pads", "Test Pads", 0.49, 0.76, 0.22, 0.18),
    ("mounting_holes", "Mounting Holes", 0.70, 0.76, 0.24, 0.18),
    ("mechanical_notes", "Mechanical Notes", 0.02, 0.78, 0.44, 0.18),
]

UNANNOTATED_RE = re.compile(r"\b(?:R|C|U|D|J|F|Q|L|Y|SW|TP|MH|FB)\?\b", re.IGNORECASE)
FIELD_RE = re.compile(
    r"(?:\bFootprint\b|\bDatasheet\b|\bki_fp_filters\b|\bki_keywords\b|\bLibrary\b|\bLibId\b|\blib_id\b|Device:|Connector:|Regulator_|RF_Module:|\bSimulation_SPICE\b|\bexclude_from_bom\b|\bexclude_from_board\b)",
    re.IGNORECASE,
)


def default_config() -> dict[str, Any]:
    return {
        "schema": "kicad_engine.schematic_visual_blocks.v1",
        "coordinate_system": "normalized",
        "notes": "Default normalized blocks are starter review windows. Adjust x/y/width/height per project after checking crops.",
        "blocks": [
            {
                "name": name,
                "title": title,
                "units": "normalized",
                "x": x,
                "y": y,
                "width": width,
                "height": height,
                "review_required": True,
                "notes": "Default starter crop. Human may need to adjust coordinates.",
            }
            for name, title, x, y, width, height in DEFAULT_BLOCKS
        ],
    }


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


def load_or_create_config(path: Path, create_default: bool) -> tuple[dict[str, Any], bool]:
    if path.exists():
        return read_json(path), False
    if not create_default:
        raise SystemExit(f"VISUAL_REVIEW_INCOMPLETE: visual block config missing: {path}")
    config = default_config()
    write_json(path, config)
    return config, True


def extract_svg_parts(svg_text: str) -> tuple[str, str, tuple[float, float, float, float]]:
    match = re.search(r"<svg\b([^>]*)>(.*)</svg>\s*$", svg_text, flags=re.IGNORECASE | re.DOTALL)
    if not match:
        raise SystemExit("VISUAL_REVIEW_INCOMPLETE: input SVG root element not found.")
    attrs = match.group(1)
    content = match.group(2)
    viewbox_match = re.search(r'viewBox\s*=\s*"([^"]+)"', attrs, flags=re.IGNORECASE)
    if not viewbox_match:
        raise SystemExit("VISUAL_REVIEW_INCOMPLETE: SVG viewBox not found.")
    values = [float(value) for value in re.split(r"[\s,]+", viewbox_match.group(1).strip()) if value]
    if len(values) != 4:
        raise SystemExit("VISUAL_REVIEW_INCOMPLETE: SVG viewBox is not four numeric values.")
    return attrs, content, (values[0], values[1], values[2], values[3])


def text_items(svg_text: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for match in re.finditer(r"<text\b([^>]*)>(.*?)</text>", svg_text, flags=re.IGNORECASE | re.DOTALL):
        attrs = match.group(1)
        body = match.group(2)
        x_match = re.search(r'\bx\s*=\s*"([^"]+)"', attrs)
        y_match = re.search(r'\by\s*=\s*"([^"]+)"', attrs)
        if not x_match or not y_match:
            continue
        try:
            x = float(x_match.group(1).split()[0])
            y = float(y_match.group(1).split()[0])
        except ValueError:
            continue
        clean = re.sub(r"<[^>]+>", "", body)
        clean = html.unescape(clean).strip()
        if clean:
            items.append({"x": x, "y": y, "text": clean})
    return items


def normalize_rect(block: dict[str, Any], viewbox: tuple[float, float, float, float]) -> tuple[float, float, float, float]:
    vb_x, vb_y, vb_w, vb_h = viewbox
    units = str(block.get("units", "") or "").lower()
    coord_system = units or "normalized"
    x = float(block.get("x", 0))
    y = float(block.get("y", 0))
    width = float(block.get("width", 0))
    height = float(block.get("height", 0))
    if coord_system == "normalized":
        x = vb_x + x * vb_w
        y = vb_y + y * vb_h
        width *= vb_w
        height *= vb_h
    elif coord_system not in {"svg", "viewbox"}:
        raise SystemExit(f"VISUAL_REVIEW_INCOMPLETE: unsupported block coordinate units: {coord_system}")
    if width <= 0 or height <= 0:
        raise SystemExit(f"VISUAL_REVIEW_INCOMPLETE: invalid crop size for block {block.get('name', '')}")
    x = max(vb_x, min(x, vb_x + vb_w))
    y = max(vb_y, min(y, vb_y + vb_h))
    width = min(width, vb_x + vb_w - x)
    height = min(height, vb_y + vb_h - y)
    return x, y, width, height


def safe_name(value: str) -> str:
    name = re.sub(r"[^A-Za-z0-9_.-]+", "_", value.strip()).strip("_")
    return name or "block"


def crop_svg(attrs: str, content: str, rect: tuple[float, float, float, float], width_px: int) -> str:
    x, y, width, height = rect
    height_px = max(1, int(round(width_px * height / width)))
    clean_attrs = re.sub(r'\b(width|height|viewBox)\s*=\s*"[^"]*"', "", attrs, flags=re.IGNORECASE)
    return f"""<?xml version="1.0" standalone="no"?>
<svg{clean_attrs} width="{width_px}px" height="{height_px}px" viewBox="{x:.4f} {y:.4f} {width:.4f} {height:.4f}">
{content}
</svg>
"""


def find_browser_renderer() -> Path | None:
    candidates = [
        shutil.which("msedge"),
        shutil.which("chrome"),
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return Path(candidate)
    return None


def file_url(path: Path) -> str:
    return "file:///" + quote(str(path.resolve()).replace("\\", "/"))


def render_with_browser(renderer: Path, svg_path: Path, png_path: Path, width: int, height: int) -> tuple[bool, str]:
    png_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(renderer),
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--screenshot={png_path}",
        f"--window-size={width},{height}",
        file_url(svg_path),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=45)
    except Exception as exc:
        return False, str(exc)
    if result.returncode != 0:
        return False, (result.stderr or result.stdout or f"renderer exit {result.returncode}").strip()
    return png_path.exists() and png_path.stat().st_size > 0, "browser renderer completed"


def render_with_tool(svg_path: Path, png_path: Path, width: int, height: int) -> tuple[bool, str]:
    if shutil.which("magick"):
        cmd = ["magick", str(svg_path), str(png_path)]
    elif shutil.which("rsvg-convert"):
        cmd = ["rsvg-convert", "-w", str(width), "-h", str(height), "-o", str(png_path), str(svg_path)]
    elif shutil.which("inkscape"):
        cmd = ["inkscape", str(svg_path), f"--export-filename={png_path}", f"--export-width={width}", f"--export-height={height}"]
    else:
        renderer = find_browser_renderer()
        if renderer:
            return render_with_browser(renderer, svg_path, png_path, width, height)
        return False, "no SVG-to-PNG renderer found"
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=45)
    except Exception as exc:
        return False, str(exc)
    if result.returncode != 0:
        return False, (result.stderr or result.stdout or f"renderer exit {result.returncode}").strip()
    return png_path.exists() and png_path.stat().st_size > 0, "renderer completed"


def texts_in_rect(items: list[dict[str, Any]], rect: tuple[float, float, float, float]) -> list[str]:
    x, y, width, height = rect
    x2 = x + width
    y2 = y + height
    return [str(item["text"]) for item in items if x <= float(item["x"]) <= x2 and y <= float(item["y"]) <= y2]


def block_findings(texts: list[str]) -> tuple[list[str], list[str]]:
    joined = "\n".join(texts)
    unannotated = sorted(set(match.group(0) for match in UNANNOTATED_RE.finditer(joined)))
    field_risks = sorted(set(match.group(0) for match in FIELD_RE.finditer(joined)))
    return unannotated, field_risks


def build_review_markdown(data: dict[str, Any]) -> str:
    lines = [
        "# Close-Up Schematic Visual Review",
        "",
        f"Status: `{data['status']}`",
        "",
        f"Generated: `{data['generated_at']}`",
        f"Source SVG: `{data['source_svg']}`",
        f"Config: `{data['config_path']}`",
        f"Crops folder: `{data['crops_dir']}`",
        f"Full-page PNG: `{data.get('full_png', '') or 'NOT_AVAILABLE'}`",
        "",
        "## Summary",
        "",
        f"- Blocks configured: {data['block_count']}",
        f"- Crops generated: {data['crop_count']}",
        f"- PNG crops generated: {data['png_count']}",
        f"- Blocks with unannotated visible references: {data['blocks_with_unannotated_refs']}",
        f"- Blocks with visible footprint/library-field risks: {data['blocks_with_field_risks']}",
        f"- Renderer: `{data['renderer_status']}`",
        "",
        "## Block Table",
        "",
        "| Block | Status | SVG Crop | PNG Crop | Visible unannotated refs | Visible field risks | Notes |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for block in data["blocks"]:
        lines.append(
            "| `{name}` | `{status}` | `{svg}` | `{png}` | {refs} | {fields} | {notes} |".format(
                name=block["name"],
                status=block["status"],
                svg=block["svg_crop"],
                png=block.get("png_crop") or "NOT_AVAILABLE",
                refs=", ".join(block["unannotated_refs"]) or "None detected",
                fields=", ".join(block["field_risks"]) or "None detected",
                notes=str(block.get("notes", "")).replace("|", "\\|"),
            )
        )
    lines.extend(
        [
            "",
            "## Crop Review Sections",
            "",
            "Each crop must be reviewed by a human or an agent using visual evidence. Mark every section `PASS`, `FAIL`, or `NEEDS_REVIEW` in the project gate file.",
            "",
        ]
    )
    for block in data["blocks"]:
        lines.extend(
            [
                f"### {block['title']}",
                "",
                f"- Block name: `{block['name']}`",
                f"- Status: `{block['status']}`",
                f"- SVG crop: `{block['svg_crop']}`",
                f"- PNG crop: `{block.get('png_crop') or 'NOT_AVAILABLE'}`",
                f"- Visible unannotated refs: {', '.join(block['unannotated_refs']) or 'None detected'}",
                f"- Visible footprint/library fields: {', '.join(block['field_risks']) or 'None detected'}",
                "- Human visual result: `NOT_REVIEWED`",
                "- Notes:",
                "",
            ]
        )
        if block.get("png_crop"):
            lines.append(f"![{block['title']}]({block['png_crop']})")
        else:
            lines.append(f"[Open SVG crop]({block['svg_crop']})")
        lines.append("")
    lines.extend(
        [
            "## Limits",
            "",
            "- This report detects visible text in the SVG; it is not OCR for arbitrary raster images.",
            "- Close-up crops do not prove electrical correctness, footprint correctness, connector orientation, ERC, DRC, or fabrication readiness.",
            "- If a crop misses the intended block, adjust `_verification/schematic_visual/visual_blocks.json` and regenerate.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate schematic close-up crops and visual review markdown from a KiCad SVG export.")
    parser.add_argument("--source-svg", required=True, help="Full-page KiCad schematic SVG export.")
    parser.add_argument("--config", required=True, help="Project visual block config JSON.")
    parser.add_argument("--crops-dir", required=True, help="Output folder for close-up crop files.")
    parser.add_argument("--review-output", required=True, help="Output CLOSE_UP_REVIEW.md path.")
    parser.add_argument("--json-output", default="", help="Optional JSON summary path.")
    parser.add_argument("--full-png-output", default="", help="Optional full-page PNG output path.")
    parser.add_argument("--create-default-config", action="store_true", help="Create default visual_blocks.json if missing.")
    parser.add_argument("--crop-width-px", type=int, default=1600, help="Nominal PNG/SVG viewport width for each crop.")
    parser.add_argument("--full-width-px", type=int, default=2400, help="Nominal PNG viewport width for full-page render.")
    parser.add_argument("--no-fail", action="store_true", help="Return 0 even when visual findings are present.")
    args = parser.parse_args()

    source_svg = Path(args.source_svg).resolve()
    config_path = Path(args.config).resolve()
    crops_dir = Path(args.crops_dir).resolve()
    review_output = Path(args.review_output).resolve()
    if not source_svg.exists():
        raise SystemExit(f"VISUAL_REVIEW_INCOMPLETE: source SVG missing: {source_svg}")

    config, created_config = load_or_create_config(config_path, args.create_default_config)
    blocks = list(config.get("blocks", []))
    default_names = {item[0] for item in DEFAULT_BLOCKS}
    present_names = {str(block.get("name", "")) for block in blocks}
    missing_default_blocks = sorted(default_names - present_names)
    if not blocks:
        raise SystemExit("VISUAL_REVIEW_INCOMPLETE: no visual blocks configured.")

    svg_text = source_svg.read_text(encoding="utf-8", errors="replace")
    attrs, content, viewbox = extract_svg_parts(svg_text)
    all_text_items = text_items(svg_text)
    crops_dir.mkdir(parents=True, exist_ok=True)

    generated_blocks: list[dict[str, Any]] = []
    png_count = 0
    crop_count = 0
    renderer_messages: list[str] = []

    for block in blocks:
        name = safe_name(str(block.get("name", "")))
        title = str(block.get("title") or name)
        rect = normalize_rect(block, viewbox)
        crop_path = crops_dir / f"{name}.svg"
        crop_path.write_text(crop_svg(attrs, content, rect, args.crop_width_px), encoding="utf-8")
        crop_count += 1
        crop_texts = texts_in_rect(all_text_items, rect)
        unannotated, fields = block_findings(crop_texts)
        height_px = max(1, int(round(args.crop_width_px * rect[3] / rect[2])))
        png_path = crops_dir / f"{name}.png"
        rendered, renderer_msg = render_with_tool(crop_path, png_path, args.crop_width_px, height_px)
        renderer_messages.append(renderer_msg)
        if rendered:
            png_count += 1
        status = "AUTOMATED_SCREEN_PASS"
        notes = str(block.get("notes", ""))
        if unannotated or fields:
            status = "FAIL"
        if not crop_texts:
            status = "WARN" if status == "AUTOMATED_SCREEN_PASS" else status
            notes = (notes + " Text extraction found no visible text in this crop.").strip()
        generated_blocks.append(
            {
                "name": name,
                "title": title,
                "status": status,
                "rect": {"x": rect[0], "y": rect[1], "width": rect[2], "height": rect[3]},
                "svg_crop": str(crop_path),
                "png_crop": str(png_path) if rendered else "",
                "visible_text_count": len(crop_texts),
                "unannotated_refs": unannotated,
                "field_risks": fields,
                "notes": notes,
            }
        )

    full_png = ""
    if args.full_png_output:
        vb_x, vb_y, vb_w, vb_h = viewbox
        full_height = max(1, int(round(args.full_width_px * vb_h / vb_w)))
        rendered, renderer_msg = render_with_tool(source_svg, Path(args.full_png_output), args.full_width_px, full_height)
        renderer_messages.append(renderer_msg)
        if rendered:
            full_png = str(Path(args.full_png_output).resolve())

    blocks_with_refs = sum(1 for block in generated_blocks if block["unannotated_refs"])
    blocks_with_fields = sum(1 for block in generated_blocks if block["field_risks"])
    status = "AUTOMATED_CROP_PASS_ONLY"
    if crop_count < len(blocks) or not generated_blocks:
        status = "VISUAL_REVIEW_INCOMPLETE"
    elif missing_default_blocks:
        status = "VISUAL_REVIEW_INCOMPLETE"
    elif blocks_with_refs or blocks_with_fields:
        status = "FAIL"
    elif png_count == 0:
        status = "WARN"

    data = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "status": status,
        "source_svg": str(source_svg),
        "config_path": str(config_path),
        "config_created": created_config,
        "missing_default_blocks": missing_default_blocks,
        "crops_dir": str(crops_dir),
        "review_output": str(review_output),
        "full_png": full_png,
        "renderer_status": "; ".join(sorted(set(renderer_messages))) or "not run",
        "block_count": len(blocks),
        "crop_count": crop_count,
        "png_count": png_count,
        "blocks_with_unannotated_refs": blocks_with_refs,
        "blocks_with_field_risks": blocks_with_fields,
        "text_items_found": len(all_text_items),
        "blocks": generated_blocks,
    }

    review_output.parent.mkdir(parents=True, exist_ok=True)
    review_output.write_text(build_review_markdown(data), encoding="utf-8")
    if args.json_output:
        write_json(Path(args.json_output), data)

    if not review_output.exists() or crop_count == 0:
        print("VISUAL_REVIEW_INCOMPLETE: crops or review output missing")
        return 20
    print(f"Close-up visual review status: {status}")
    if status == "AUTOMATED_CROP_PASS_ONLY":
        print("Human-readable visual status: NOT_VERIFIED. Inspect rendered full-page PNG and every crop before claiming VISUAL_PASS.")
    print(f"Review: {review_output}")
    print(f"Crops: {crops_dir}")
    if args.no_fail:
        return 0
    if status == "VISUAL_REVIEW_INCOMPLETE":
        return 20
    if status == "FAIL":
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
