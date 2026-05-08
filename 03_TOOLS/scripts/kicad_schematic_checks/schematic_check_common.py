#!/usr/bin/env python3
"""Shared read-only helpers for KiCad schematic checks.

The helpers parse enough of KiCad's S-expression schematic format to inspect
symbol instances, fields, labels, and text notes. They never write KiCad files.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


CHECK_STATUS_PASS = "PASS"
CHECK_STATUS_WARN = "WARN"
CHECK_STATUS_FAIL = "FAIL"

REFERENCE_PREFIXES = (
    "TP",
    "MH",
    "SW",
    "FB",
    "RV",
    "R",
    "C",
    "U",
    "D",
    "J",
    "F",
    "Q",
    "L",
    "Y",
    "X",
)

REQUIRED_FIELD_NAMES = {
    "Reference",
    "Value",
    "Footprint",
    "Datasheet",
    "Verification_Status",
}

HIGH_RISK_KEYWORDS = {
    "connector": ("connector", "usb-c", "usb_c", "receptacle", "jack", "terminal", "jst", "sma", "u.fl", "ufl"),
    "pmos": ("pmos", "p-channel", "p channel", "ao3401", "mosfet"),
    "esd": ("esd", "tvs", "transient", "usb protection", "surge"),
    "regulator": ("regulator", "buck", "ldo", "ap63203", "ams1117", "mp1584", "lm2596"),
}

VERIFICATION_TOKENS = (
    "VERIFIED",
    "VERIFIED_FROM_DATASHEET",
    "VERIFIED_FROM_KICAD_LIBRARY",
    "USER_CONFIRMED",
    "NEEDS_REVIEW",
    "BLOCKED",
    "UNVERIFIED",
    "UNVERIFIED_PLACEHOLDER",
)


def decode_atom(token: str) -> str:
    if token.startswith('"') and token.endswith('"'):
        try:
            return json.loads(token)
        except json.JSONDecodeError:
            return token[1:-1]
    return token


def tokenize_sexpr(text: str) -> list[str]:
    return re.findall(r'"(?:\\.|[^"\\])*"|[()]|[^\s()]+', text)


def parse_tokens(tokens: list[str]) -> list[Any]:
    index = 0

    def parse_one() -> Any:
        nonlocal index
        if index >= len(tokens):
            raise ValueError("unexpected end of token stream")
        token = tokens[index]
        index += 1
        if token == "(":
            node: list[Any] = []
            while index < len(tokens) and tokens[index] != ")":
                node.append(parse_one())
            if index >= len(tokens):
                raise ValueError("missing closing parenthesis")
            index += 1
            return node
        if token == ")":
            raise ValueError("unexpected closing parenthesis")
        return decode_atom(token)

    parsed: list[Any] = []
    while index < len(tokens):
        parsed.append(parse_one())
    return parsed[0] if len(parsed) == 1 else parsed


def load_schematic(path: Path) -> list[Any]:
    return parse_tokens(tokenize_sexpr(path.read_text(encoding="utf-8", errors="replace")))


def walk_lists(node: Any) -> list[list[Any]]:
    found: list[list[Any]] = []
    if isinstance(node, list):
        found.append(node)
        for child in node:
            found.extend(walk_lists(child))
    return found


def child_lists(node: list[Any], name: str) -> list[list[Any]]:
    return [child for child in node if isinstance(child, list) and child and child[0] == name]


def first_child_value(node: list[Any], name: str, index: int = 1, default: str = "") -> str:
    for child in child_lists(node, name):
        if len(child) > index and isinstance(child[index], str):
            return child[index]
    return default


def symbol_properties(symbol: list[Any]) -> dict[str, str]:
    props: dict[str, str] = {}
    for child in child_lists(symbol, "property"):
        if len(child) >= 3 and isinstance(child[1], str):
            props[child[1]] = child[2] if isinstance(child[2], str) else ""
    return props


def symbol_instances(root: list[Any]) -> list[dict[str, Any]]:
    symbols: list[dict[str, Any]] = []
    for node in walk_lists(root):
        if not node or node[0] != "symbol":
            continue
        lib_id = first_child_value(node, "lib_id")
        if not lib_id:
            continue
        props = symbol_properties(node)
        symbols.append(
            {
                "lib_id": lib_id,
                "reference": props.get("Reference", ""),
                "value": props.get("Value", ""),
                "footprint": props.get("Footprint", ""),
                "datasheet": props.get("Datasheet", ""),
                "properties": props,
                "raw": node,
            }
        )
    return symbols


def schematic_text_items(root: list[Any]) -> list[str]:
    texts: list[str] = []
    for node in walk_lists(root):
        if node and node[0] in {"text", "text_box", "label", "global_label", "hierarchical_label"}:
            if len(node) > 1 and isinstance(node[1], str):
                texts.append(node[1])
    return texts


def normalize_text(*parts: object) -> str:
    return " ".join(str(part or "") for part in parts).lower()


def reference_prefix(reference: str) -> str:
    ref = reference.strip().upper()
    for prefix in REFERENCE_PREFIXES:
        if ref.startswith(prefix):
            return prefix
    match = re.match(r"[A-Z]+", ref)
    return match.group(0) if match else ""


def is_power_symbol(symbol: dict[str, Any]) -> bool:
    ref = str(symbol.get("reference", "")).upper()
    lib_id = str(symbol.get("lib_id", "")).lower()
    return ref.startswith("#PWR") or ref.startswith("#FLG") or lib_id.startswith("power:")


def is_physical_symbol(symbol: dict[str, Any]) -> bool:
    ref = str(symbol.get("reference", "")).upper()
    lib_id = str(symbol.get("lib_id", "")).lower()
    if is_power_symbol(symbol):
        return False
    if ref.startswith("#"):
        return False
    if lib_id.startswith("mechanical:fiducial"):
        return True
    return True


def symbol_search_text(symbol: dict[str, Any]) -> str:
    props = symbol.get("properties", {})
    prop_text = " ".join(f"{key} {value}" for key, value in props.items())
    return normalize_text(symbol.get("reference"), symbol.get("value"), symbol.get("lib_id"), symbol.get("footprint"), prop_text)


def risk_categories(symbol: dict[str, Any]) -> list[str]:
    text = symbol_search_text(symbol)
    ref = str(symbol.get("reference", "")).upper()
    if ref.startswith("TP") or "testpoint" in text or "test point" in text:
        return []
    if ref.startswith("MH") or "mountinghole" in text or "mounting hole" in text:
        return []
    categories: list[str] = []
    for category, keywords in HIGH_RISK_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            categories.append(category)
    if ref.startswith("J") and "connector" not in categories:
        categories.append("connector")
    if ref.startswith("Q") and "pmos" in text and "pmos" not in categories:
        categories.append("pmos")
    return categories


def has_verification_status(symbol: dict[str, Any]) -> bool:
    props = symbol.get("properties", {})
    fields = [
        props.get("Verification_Status", ""),
        props.get("Verified_Status", ""),
        props.get("Status", ""),
        str(symbol.get("value", "")),
        props.get("Notes", ""),
    ]
    combined = normalize_text(*fields).upper()
    return any(token in combined for token in VERIFICATION_TOKENS)


def expected_category_for_reference(reference: str) -> str:
    prefix = reference_prefix(reference)
    return {
        "R": "resistor",
        "C": "capacitor",
        "U": "integrated-circuit-or-module",
        "D": "diode-led-tvs-esd",
        "J": "connector",
        "F": "fuse",
        "Q": "transistor-or-mosfet",
        "L": "inductor",
        "Y": "crystal-or-oscillator",
        "SW": "switch",
        "TP": "test-point",
        "MH": "mounting-hole",
        "FB": "ferrite-bead",
    }.get(prefix, "unknown")


def category_matches(symbol: dict[str, Any]) -> tuple[bool, str]:
    reference = str(symbol.get("reference", ""))
    expected = expected_category_for_reference(reference)
    text = symbol_search_text(symbol)
    if expected == "unknown" or not reference:
        return True, expected
    checks = {
        "resistor": ("resistor", "device:r", "ohm", "pull", "jumper"),
        "capacitor": ("capacitor", "device:c", "uf", "nf", "pf"),
        "integrated-circuit-or-module": ("mcu", "module", "regulator", "interface", "ic", "rf_module", "sensor", "driver", "usb", "esp32", "stm32"),
        "diode-led-tvs-esd": ("diode", "led", "tvs", "esd", "device:d"),
        "connector": ("connector", "receptacle", "jack", "terminal", "pinheader", "usb", "sma", "jst"),
        "fuse": ("fuse", "polyfuse", "ptc"),
        "transistor-or-mosfet": ("transistor", "mosfet", "pmos", "nmos", "device:q"),
        "inductor": ("inductor", "device:l", "ferrite"),
        "crystal-or-oscillator": ("crystal", "oscillator", "resonator"),
        "switch": ("switch", "button"),
        "test-point": ("testpoint", "test point", "testpad"),
        "mounting-hole": ("mountinghole", "mounting hole"),
        "ferrite-bead": ("ferrite", "bead"),
    }
    return any(keyword in text for keyword in checks.get(expected, ())), expected


def parse_bom_lock(path: Path | None) -> dict[str, Any]:
    if not path or not path.exists():
        return {
            "path": str(path) if path else "",
            "exists": False,
            "references": {},
            "mpns": set(),
            "raw_items": [],
        }
    text = path.read_text(encoding="utf-8", errors="replace")
    references: dict[str, dict[str, str]] = {}
    mpns: set[str] = set()
    raw_items: list[str] = []

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or set(stripped) <= {"|", "-", " ", ":"}:
            continue
        ref_matches = re.findall(r"\b(?:R|C|U|D|J|F|Q|L|Y|SW|TP|MH|FB)\d+[A-Z]?\b", stripped, flags=re.IGNORECASE)
        mpn_matches = re.findall(r"\b[A-Z0-9][A-Z0-9._/-]{3,}\b", stripped)
        if ref_matches or mpn_matches:
            raw_items.append(stripped)
        clean_mpns = {
            token
            for token in mpn_matches
            if not re.fullmatch(r"(PASS|FAIL|WARN|NEEDS_REVIEW|UNVERIFIED|VERIFIED|TRUE|FALSE)", token, flags=re.IGNORECASE)
            and not re.fullmatch(r"(R|C|U|D|J|F|Q|L|Y|SW|TP|MH|FB)\d+[A-Z]?", token, flags=re.IGNORECASE)
        }
        mpns.update(clean_mpns)
        for ref in ref_matches:
            references[ref.upper()] = {"line": stripped, "mpn_candidates": ", ".join(sorted(clean_mpns))}

    return {
        "path": str(path),
        "exists": True,
        "references": references,
        "mpns": mpns,
        "raw_items": raw_items,
    }


def check_record(status: str, code: str, message: str, reference: str = "", evidence: str = "") -> dict[str, str]:
    return {
        "status": status,
        "code": code,
        "reference": reference,
        "message": message,
        "evidence": evidence,
    }


def summarize_checks(checks: list[dict[str, str]]) -> dict[str, Any]:
    counts = Counter(item["status"] for item in checks)
    if counts.get(CHECK_STATUS_FAIL, 0):
        result = CHECK_STATUS_FAIL
    elif counts.get(CHECK_STATUS_WARN, 0):
        result = CHECK_STATUS_WARN
    else:
        result = CHECK_STATUS_PASS
    return {
        "result": result,
        "counts": {
            CHECK_STATUS_PASS: counts.get(CHECK_STATUS_PASS, 0),
            CHECK_STATUS_WARN: counts.get(CHECK_STATUS_WARN, 0),
            CHECK_STATUS_FAIL: counts.get(CHECK_STATUS_FAIL, 0),
        },
    }


def markdown_report(title: str, data: dict[str, Any]) -> str:
    summary = data["summary"]
    lines = [
        f"# {title}",
        "",
        f"Status: `{summary['result']}`",
        "",
        f"Generated: `{data['generated_at']}`",
        f"Schematic: `{data.get('schematic', '')}`",
    ]
    if data.get("bom_lock"):
        lines.append(f"BOM lock: `{data['bom_lock']}`")
    lines.extend(
        [
            "",
            "## Summary",
            "",
            f"- Pass: {summary['counts'][CHECK_STATUS_PASS]}",
            f"- Warn: {summary['counts'][CHECK_STATUS_WARN]}",
            f"- Fail: {summary['counts'][CHECK_STATUS_FAIL]}",
            "",
            "## Findings",
            "",
            "| Status | Code | Reference | Message | Evidence |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in data["checks"]:
        lines.append(
            "| `{status}` | `{code}` | `{reference}` | {message} | `{evidence}` |".format(
                status=item["status"],
                code=item["code"],
                reference=item.get("reference", ""),
                message=str(item["message"]).replace("|", "\\|"),
                evidence=str(item.get("evidence", "")).replace("|", "\\|"),
            )
        )
    lines.extend(
        [
            "",
            "## Safe Use",
            "",
            "- This is an automated screening report, not final engineering approval.",
            "- Failures or warnings must be resolved or explicitly carried as schematic-to-PCB gate blockers.",
            "- Do not update PCB from schematic unless the active project's schematic-to-PCB gate is `PASS`.",
            "",
        ]
    )
    return "\n".join(lines)


def write_optional_reports(args: argparse.Namespace, title: str, data: dict[str, Any]) -> None:
    if args.json_output:
        json_path = Path(args.json_output)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        json_ready = dict(data)
        json_ready["bom_mpn_count"] = len(data.get("bom_mpns", []))
        json_path.write_text(json.dumps(json_ready, indent=2, sort_keys=True), encoding="utf-8")
    markdown = markdown_report(title, data)
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown, encoding="utf-8")
    else:
        print(markdown)


def common_parser(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--schematic", required=True, help="Path to .kicad_sch file.")
    parser.add_argument("--bom-lock", default="", help="Optional BOM lock or ready-parts markdown file.")
    parser.add_argument("--output", default="", help="Optional markdown report output path.")
    parser.add_argument("--json-output", default="", help="Optional JSON report output path.")
    parser.add_argument("--no-fail", action="store_true", help="Return exit code 0 even when findings fail.")
    return parser


def build_report_data(args: argparse.Namespace, checks: list[dict[str, str]], extra: dict[str, Any] | None = None) -> dict[str, Any]:
    data: dict[str, Any] = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "schematic": str(Path(args.schematic)),
        "bom_lock": str(Path(args.bom_lock)) if args.bom_lock else "",
        "checks": checks,
        "summary": summarize_checks(checks),
    }
    if extra:
        data.update(extra)
    return data


def exit_code_for(data: dict[str, Any], no_fail: bool) -> int:
    if no_fail:
        return 0
    return 1 if data["summary"]["result"] == CHECK_STATUS_FAIL else 0
