#!/usr/bin/env python3
"""Validate datasheet source-list URLs without downloading documents."""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


REQUIRED_COLUMNS = [
    "vendor",
    "family",
    "part_number",
    "document_type",
    "title",
    "source_url",
    "local_target_folder",
    "public_redistribution_status",
    "notes",
]


def read_records(paths: Iterable[Path]) -> List[Dict[str, str]]:
    records: List[Dict[str, str]] = []
    for path in paths:
        if path.suffix.lower() == ".csv":
            with path.open("r", encoding="utf-8-sig", newline="") as handle:
                for row in csv.DictReader(handle):
                    row["_source_file"] = str(path)
                    records.append({k: (v or "").strip() for k, v in row.items()})
        elif path.suffix.lower() == ".json":
            with path.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
            items = data.get("records", data) if isinstance(data, dict) else data
            if not isinstance(items, list):
                raise ValueError(f"JSON source list must contain a list: {path}")
            for item in items:
                if not isinstance(item, dict):
                    raise ValueError(f"JSON record is not an object in {path}")
                row = {str(k): str(v) if v is not None else "" for k, v in item.items()}
                row["_source_file"] = str(path)
                records.append(row)
        else:
            continue
    return records


def discover_inputs(args: argparse.Namespace) -> List[Path]:
    paths: List[Path] = []
    for raw in args.inputs:
        path = Path(raw)
        if path.is_dir():
            paths.extend(sorted(path.glob("*.csv")))
            paths.extend(sorted(path.glob("*.json")))
        elif path.exists():
            paths.append(path)
        else:
            raise FileNotFoundError(path)
    return paths


def validate_url(url: str, timeout: float) -> Tuple[str, str, str]:
    if not url:
        return "MISSING_URL", "", "No source_url provided."
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return "INVALID_URL", "", "URL is not http(s) or has no host."

    headers = {"User-Agent": "KICAD_ENGINE datasheet link validator (metadata only)"}
    for method in ("HEAD", "GET"):
        try:
            request = Request(url, method=method, headers=headers)
            with urlopen(request, timeout=timeout) as response:
                status = getattr(response, "status", "")
                content_type = response.headers.get("Content-Type", "")
                return "REACHABLE", str(status), content_type
        except HTTPError as exc:
            if method == "HEAD" and exc.code in {403, 405, 501}:
                continue
            return "HTTP_ERROR", str(exc.code), str(exc.reason)
        except URLError as exc:
            return "URL_ERROR", "", str(exc.reason)
        except TimeoutError:
            return "TIMEOUT", "", "Request timed out."
    return "UNKNOWN_ERROR", "", "URL validation failed."


def write_report(records: List[Dict[str, str]], output: Path, timeout: float, delay: float) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Datasheet Link Validation Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "Downloads: disabled",
        "",
        "| Status | HTTP | Vendor | Family | Part / Topic | Document Type | URL | Notes |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for index, record in enumerate(records):
        status, http_status, detail = validate_url(record.get("source_url", ""), timeout)
        notes = record.get("notes", "")
        if detail:
            notes = f"{notes} Validation detail: {detail}".strip()
        lines.append(
            "| {status} | {http} | {vendor} | {family} | {part} | {doctype} | {url} | {notes} |".format(
                status=status,
                http=http_status,
                vendor=record.get("vendor", ""),
                family=record.get("family", ""),
                part=record.get("part_number", ""),
                doctype=record.get("document_type", ""),
                url=record.get("source_url", ""),
                notes=notes.replace("|", "\\|"),
            )
        )
        if delay > 0 and index < len(records) - 1:
            time.sleep(delay)
    lines.extend(
        [
            "",
            "## Policy",
            "",
            "This report validates links only. It does not download or redistribute documents.",
        ]
    )
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "inputs",
        nargs="*",
        default=["06_DATASHEETS/00_INDEX/source_lists"],
        help="CSV/JSON source list files or directories.",
    )
    parser.add_argument(
        "--output",
        default="05_OUTPUTS/datasheet_research/link_validation_report.md",
        help="Markdown report output path.",
    )
    parser.add_argument("--timeout", type=float, default=10.0, help="URL timeout in seconds.")
    parser.add_argument("--delay", type=float, default=0.25, help="Delay between URL checks.")
    parser.add_argument(
        "--download",
        action="store_true",
        help="Reserved for a future gated workflow. Currently disabled.",
    )
    args = parser.parse_args()

    if args.download:
        print("--download is disabled. Review license and redistribution policy first.", file=sys.stderr)
        return 2

    paths = discover_inputs(args)
    records = read_records(paths)
    write_report(records, Path(args.output), args.timeout, args.delay)
    print(f"Wrote {args.output} for {len(records)} records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
