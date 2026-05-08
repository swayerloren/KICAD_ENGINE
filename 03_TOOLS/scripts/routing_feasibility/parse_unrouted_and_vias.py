from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


UNROUTED_RE = re.compile(
    r"(?:unrouted|failed)\s+(?:net|connection)\s+['\"]?([A-Za-z0-9_.$:+/-]+)",
    flags=re.IGNORECASE,
)
PERCENT_RE = re.compile(r"(\d+(?:\.\d+)?)\s*%\s*(?:routed|completed)", flags=re.IGNORECASE)
PASS_RE = re.compile(r"\bpass(?:es)?\s*[:#]?\s*(\d+)", flags=re.IGNORECASE)
TRACE_LENGTH_RE = re.compile(
    r"(?:trace|wire)\s+length\s*[:=]?\s*(\d+(?:\.\d+)?)\s*mm",
    flags=re.IGNORECASE,
)
TEXT_VIA_RE = re.compile(r"\bvia(?:s)?\s*[:=]?\s*(\d+)", flags=re.IGNORECASE)
SES_VIA_RE = re.compile(r"\(\s*via\b", flags=re.IGNORECASE)
DSN_NET_RE = re.compile(r"\(\s*net\b", flags=re.IGNORECASE)
CONGESTION_RE = re.compile(
    r"\b(congestion|crowded|blocked|cannot\s+route|failed\s+connection|detour)\b",
    flags=re.IGNORECASE,
)


def read_text(path: Path | None) -> str:
    if path is None:
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def count_dsn_nets(dsn_text: str) -> int:
    return len(DSN_NET_RE.findall(dsn_text))


def parse_unrouted_nets(text: str) -> list[str]:
    names: list[str] = []
    for match in UNROUTED_RE.finditer(text):
        name = match.group(1)
        if name not in names:
            names.append(name)
    return names


def parse_pass_count(text: str) -> int:
    values = [int(match.group(1)) for match in PASS_RE.finditer(text)]
    return max(values) if values else 0


def parse_trace_length_mm(text: str) -> float | None:
    match = TRACE_LENGTH_RE.search(text)
    if match is None:
        return None
    return round(float(match.group(1)), 3)


def parse_via_count(text: str, ses_text: str) -> int | None:
    if ses_text:
        return len(SES_VIA_RE.findall(ses_text))
    match = TEXT_VIA_RE.search(text)
    if match is None:
        return None
    return int(match.group(1))


def parse_routed_pct(text: str, total_nets: int, unrouted_nets: list[str], ses_exists: bool) -> float | None:
    match = PERCENT_RE.search(text)
    if match is not None:
        return round(float(match.group(1)), 2)
    if total_nets > 0:
        return round(((total_nets - len(unrouted_nets)) / total_nets) * 100.0, 2)
    if ses_exists:
        return 100.0
    return None


def build_metrics(log_text: str = "", dsn_text: str = "", ses_text: str = "") -> dict[str, Any]:
    combined = "\n".join(part for part in [log_text, ses_text] if part)
    unrouted_nets = parse_unrouted_nets(combined)
    total_nets = count_dsn_nets(dsn_text)
    ses_exists = bool(ses_text.strip())
    return {
        "review_status": "REVIEW_ONLY",
        "total_nets": total_nets,
        "unrouted_nets": unrouted_nets,
        "unrouted_net_count": len(unrouted_nets),
        "routed_pct": parse_routed_pct(combined, total_nets, unrouted_nets, ses_exists),
        "via_count": parse_via_count(combined, ses_text),
        "pass_count": parse_pass_count(combined),
        "reported_trace_length_mm": parse_trace_length_mm(combined),
        "congestion_mentions": len(CONGESTION_RE.findall(combined)),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Parse coarse FreeRouting dry-run metrics.")
    parser.add_argument("--log", type=Path, help="Path to a combined or stdout FreeRouting log.")
    parser.add_argument("--dsn", type=Path, help="Path to the Specctra DSN input.")
    parser.add_argument("--ses", type=Path, help="Path to the Specctra SES output.")
    parser.add_argument("--output-json", type=Path, help="Optional JSON output path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.log is None and args.dsn is None and args.ses is None:
        raise SystemExit("At least one of --log, --dsn, or --ses is required.")

    log_text = read_text(args.log)
    dsn_text = read_text(args.dsn)
    ses_text = read_text(args.ses)
    result = {
        "tool": "parse_unrouted_and_vias",
        "review_status": "REVIEW_ONLY",
        "log_path": str(args.log.resolve()) if args.log else None,
        "dsn_path": str(args.dsn.resolve()) if args.dsn else None,
        "ses_path": str(args.ses.resolve()) if args.ses else None,
        "metrics": build_metrics(log_text=log_text, dsn_text=dsn_text, ses_text=ses_text),
    }

    payload = json.dumps(result, indent=2)
    if args.output_json is not None:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
