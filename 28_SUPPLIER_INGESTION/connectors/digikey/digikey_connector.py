#!/usr/bin/env python3
"""Safe Digi-Key supplier connector stub.

Default behavior is offline DRY_RUN normalization. LIVE_MODE is guarded by
an explicit --live flag and required environment variables, but this stub does
not perform live API calls yet.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SUPPLIER = "Digi-Key"
SUPPLIER_SLUG = "digikey"
SCHEMA_VERSION = "supplier_part_normalized_v0.1"
REQUIRED_LIVE_ENV = ("DIGIKEY_CLIENT_ID", "DIGIKEY_CLIENT_SECRET")


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
    mpn = first_value(source, "manufacturer_part_number", "manufacturerPartNumber", "mpn", "part_number", default=query)
    supplier_sku = first_value(source, "supplier_sku", "digiKeyPartNumber", "digikey_part_number", "sku")
    datasheet_url = first_value(source, "datasheet_url", "datasheetUrl", "datasheet")
    product_url = first_value(source, "supplier_part_url", "productUrl", "product_url", "url", default=source_url)
    price_breaks = first_value(source, "price_breaks", "pricing", "standardPricing", default=[])
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
            "source_type": first_value(source, "source_type", default="dry_run_sample"),
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
            "description": safe_text(first_value(source, "description", "productDescription")),
            "category": safe_text(first_value(source, "category", "productCategory")),
        },
        "package": {
            "supplier_package": safe_text(first_value(source, "supplier_package", "package")),
            "manufacturer_package": safe_text(first_value(source, "manufacturer_package")),
            "pin_count": safe_text(first_value(source, "pin_count")),
            "package_confidence": "UNVERIFIED",
        },
        "inventory_price": {
            "currency": safe_text(first_value(source, "currency")),
            "stock_quantity": first_value(source, "stock_quantity", "quantityAvailable", default=None),
            "minimum_order_quantity": first_value(source, "minimum_order_quantity", "minimumOrderQuantity", default=None),
            "price_breaks": price_breaks,
        },
        "datasheets": [
            {
                "title": "Digi-Key datasheet link",
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
                "Supplier package text is not footprint verification.",
                "Exact package drawing and pinout review are required before KiCad footprint approval.",
            ],
        },
        "notes": [
            "DRY_RUN connector output only. No Digi-Key API call was made.",
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
    missing = [name for name in REQUIRED_LIVE_ENV if not os.environ.get(name)]
    if missing:
        sys.stderr.write(
            "LIVE_MODE requested for Digi-Key, but required environment variables are missing: "
            + ", ".join(missing)
            + "\nNo API key or secret value was printed or saved.\n"
        )
        return 2
    sys.stderr.write(
        "LIVE_MODE requested and required Digi-Key environment variable names are present, "
        "but live API calls are not implemented in this safe stub. No network call was made.\n"
    )
    return 3


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Normalize Digi-Key supplier data in safe DRY_RUN mode.")
    parser.add_argument("--query", default="", help="Part number or search term for dry-run metadata.")
    parser.add_argument("--input-json", type=Path, help="Optional local JSON sample to normalize.")
    parser.add_argument("--source-url", default="", help="Optional source URL to preserve in normalized output.")
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    parser.add_argument("--cache", action="store_true", help="Cache normalized non-secret output under normalized/digikey.")
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "normalized" / SUPPLIER_SLUG,
        help="Cache directory for normalized non-secret output.",
    )
    parser.add_argument("--live", action="store_true", help="Request LIVE_MODE. Requires env vars and is not implemented yet.")
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
