#!/usr/bin/env python3
"""Safe JLCPCB supplier connector stub.

Default behavior is offline DRY_RUN normalization. This connector does not
scrape JLCPCB or download files. LIVE_MODE is blocked until an official or
approved API/data-feed path is reviewed.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SUPPLIER = "JLCPCB"
SUPPLIER_SLUG = "jlcpcb"
SCHEMA_VERSION = "supplier_part_normalized_v0.1"
OPTIONAL_FUTURE_ENV = ("JLCPCB_API_KEY",)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def safe_text(value: Any, default: str = "") -> str:
    if value is None:
        return default
    return str(value)


def load_input(path: Path | None) -> dict[str, Any]:
    if path is None:
        return {}
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if isinstance(data, list):
        return data[0] if data else {}
    if isinstance(data, dict):
        records = data.get("records")
        if isinstance(records, list) and records:
            return records[0] if isinstance(records[0], dict) else {}
        return data
    raise ValueError("Input JSON must be an object, an object with records, or a list of objects.")


def first_value(source: dict[str, Any], *keys: str, default: Any = "") -> Any:
    for key in keys:
        if key in source and source[key] not in (None, ""):
            return source[key]
    return default


def normalize_record(source: dict[str, Any], query: str, source_url: str) -> dict[str, Any]:
    mpn = first_value(source, "manufacturer_part_number", "mpn", "part_number", default=query)
    supplier_sku = first_value(source, "supplier_sku", "jlcpcb_part_number", "jlc_part_number", "part_number")
    lcsc_number = first_value(source, "lcsc_part_number", "LCSC Part", "lcsc")
    datasheet_url = first_value(source, "datasheet_url", "datasheet")
    product_url = first_value(source, "supplier_part_url", "product_url", "url", default=source_url)
    price_breaks = first_value(source, "price_breaks", "pricing", default=[])
    if not isinstance(price_breaks, list):
        price_breaks = []

    return {
        "schema_version": SCHEMA_VERSION,
        "verification_status": "UNVERIFIED",
        "mode": "DRY_RUN",
        "live_call_made": False,
        "pdfs_downloaded": False,
        "source": {
            "supplier": SUPPLIER,
            "source_type": first_value(source, "source_type", default="dry_run_sample_or_user_export"),
            "source_url": source_url,
            "source_file": safe_text(first_value(source, "source_file")),
            "retrieved_at": utc_now(),
            "terms_review_status": "UNVERIFIED",
        },
        "manufacturer": {
            "name": safe_text(first_value(source, "manufacturer", "manufacturer_name")),
            "manufacturer_part_number": safe_text(mpn),
            "lifecycle_status": safe_text(first_value(source, "lifecycle_status"), "UNKNOWN") or "UNKNOWN",
        },
        "supplier_part": {
            "supplier_sku": safe_text(supplier_sku),
            "supplier_part_url": safe_text(product_url),
            "description": safe_text(first_value(source, "description")),
            "category": safe_text(first_value(source, "category")),
            "jlc_lcsc_part_number": safe_text(lcsc_number),
        },
        "package": {
            "supplier_package": safe_text(first_value(source, "supplier_package", "package")),
            "manufacturer_package": safe_text(first_value(source, "manufacturer_package")),
            "pin_count": safe_text(first_value(source, "pin_count")),
            "package_confidence": "UNVERIFIED",
        },
        "inventory_price": {
            "currency": safe_text(first_value(source, "currency")),
            "stock_quantity": first_value(source, "stock_quantity", default=None),
            "minimum_order_quantity": first_value(source, "minimum_order_quantity", default=None),
            "price_breaks": price_breaks,
        },
        "datasheets": [
            {
                "title": "JLCPCB datasheet link",
                "url": safe_text(datasheet_url),
                "downloaded": False,
                "redistribution_status": "LINK_ONLY_UNVERIFIED",
            }
        ]
        if datasheet_url
        else [],
        "footprint_risk": {
            "kicad_symbol_candidates": [],
            "kicad_footprint_candidates": [],
            "footprint_status": "UNVERIFIED",
            "risk_notes": [
                "JLCPCB/LCSC package text is not footprint verification.",
                "Assembly availability does not prove symbol, pinout, footprint, or PNP orientation correctness.",
            ],
        },
        "notes": [
            "DRY_RUN connector output only. No JLCPCB API call or scrape was made.",
            "Datasheet PDFs are not downloaded by this connector.",
        ],
    }


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, indent=2, sort_keys=False)
        handle.write("\n")


def cache_payload(cache_dir: Path, payload: dict[str, Any]) -> Path:
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = cache_dir / f"{SUPPLIER_SLUG}_normalized_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    write_json(path, payload)
    return path


def live_mode_guard() -> int:
    present = [name for name in OPTIONAL_FUTURE_ENV if os.environ.get(name)]
    if present:
        sys.stderr.write(
            "LIVE_MODE requested and optional JLCPCB credential variable names are present, "
            "but this connector has no approved live API implementation. No network call was made.\n"
        )
        return 3
    sys.stderr.write(
        "LIVE_MODE requested for JLCPCB, but no approved live API/data-feed connector is implemented. "
        "Use user-provided CSV/export files or manual source-link records. No network call was made.\n"
    )
    return 3


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Normalize JLCPCB supplier data in safe DRY_RUN mode.")
    parser.add_argument("--query", default="", help="Part number or search term for dry-run metadata.")
    parser.add_argument("--input-json", type=Path, help="Optional local JSON sample to normalize.")
    parser.add_argument("--source-url", default="", help="Optional source URL to preserve in normalized output.")
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    parser.add_argument("--cache", action="store_true", help="Cache normalized non-secret output under normalized/jlcpcb.")
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "normalized" / SUPPLIER_SLUG,
        help="Cache directory for normalized non-secret output.",
    )
    parser.add_argument("--live", action="store_true", help="Request LIVE_MODE. Blocked until approved API/data-feed support exists.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.live:
        return live_mode_guard()

    source = load_input(args.input_json)
    payload = {
        "connector": SUPPLIER_SLUG,
        "mode": "DRY_RUN",
        "live_call_made": False,
        "pdfs_downloaded": False,
        "records": [normalize_record(source, args.query, args.source_url)],
        "safety": {
            "scraping_performed": False,
            "api_keys_read": False,
            "api_keys_printed": False,
            "api_keys_saved": False,
            "datasheet_pdf_downloads": False,
        },
    }

    if args.output:
        write_json(args.output, payload)
    else:
        json.dump(payload, sys.stdout, indent=2, sort_keys=False)
        sys.stdout.write("\n")

    if args.cache:
        cache_payload(args.cache_dir, payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
