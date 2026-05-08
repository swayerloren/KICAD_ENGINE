#!/usr/bin/env python3
"""Import a user-provided supplier CSV without web scraping or downloads."""

from __future__ import annotations

import argparse
from pathlib import Path

from normalize_supplier_part import normalize_record, read_records, safe_stem, write_outputs


def main() -> int:
    parser = argparse.ArgumentParser(description="Import a manual supplier CSV export.")
    parser.add_argument("--input-csv", required=True, help="User-provided CSV export.")
    parser.add_argument("--output-dir", default="28_SUPPLIER_INGESTION/normalized/manual_csv")
    args = parser.parse_args()

    input_path = Path(args.input_csv).resolve()
    if input_path.suffix.lower() != ".csv":
        raise SystemExit("--input-csv must point to a CSV file")
    rows = read_records(input_path)
    records = [
        normalize_record(row, source_file=str(input_path), default_source_type="user_csv")
        for row in rows
    ]
    json_path, md_path = write_outputs(records, Path(args.output_dir), safe_stem(input_path))
    print(json_path)
    print(md_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
