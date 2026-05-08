import argparse
import csv
import sys
from pathlib import Path


ORIENTATION_WARNING = (
    "WARN: connector orientation, polarity, pin 1, and pick-and-place rotation "
    "review is still required; CSV validation is not assembly approval"
)


def split_designators(value):
    return [part.strip() for part in value.replace(";", ",").split(",") if part.strip()]


def is_number(value):
    try:
        float(str(value).strip())
        return True
    except ValueError:
        return False


def read_csv(path):
    with Path(path).open("r", newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)


def validate_csv(
    path,
    required_columns,
    required_nonblank,
    numeric_columns=None,
    layer_column=None,
    quantity_column=None,
    designator_column="Designator",
):
    numeric_columns = numeric_columns or []
    errors = []
    warnings = [ORIENTATION_WARNING]
    fieldnames, rows = read_csv(path)

    missing = [column for column in required_columns if column not in fieldnames]
    if missing:
        errors.append("missing required columns: " + ", ".join(missing))
        return errors, warnings, 0

    if not rows:
        errors.append("CSV has no data rows")
        return errors, warnings, 0

    for index, row in enumerate(rows, start=2):
        for column in required_nonblank:
            if not str(row.get(column, "")).strip():
                errors.append(f"row {index}: {column} is blank")

        for column in numeric_columns:
            if not is_number(row.get(column, "")):
                errors.append(f"row {index}: {column} is not numeric")

        if layer_column:
            layer = str(row.get(layer_column, "")).strip()
            if layer not in {"Top", "Bottom"}:
                errors.append(f"row {index}: {layer_column} must be Top or Bottom")

        if quantity_column and designator_column:
            quantity_raw = str(row.get(quantity_column, "")).strip()
            designators = split_designators(row.get(designator_column, ""))
            if quantity_raw:
                if not quantity_raw.isdigit():
                    errors.append(f"row {index}: {quantity_column} is not an integer")
                elif int(quantity_raw) != len(designators):
                    errors.append(
                        f"row {index}: {quantity_column}={quantity_raw} does not match "
                        f"designator count {len(designators)}"
                    )

    return errors, warnings, len(rows)


def print_result(errors, warnings, rows_checked):
    if errors:
        print("FAIL")
        for error in errors:
            print(f"ERROR: {error}")
        for warning in warnings:
            print(warning)
        return 1

    for warning in warnings:
        print(warning)
    print(f"PASS: checked {rows_checked} row(s)")
    return 0


def run_csv_validator(
    description,
    required_columns,
    required_nonblank,
    numeric_columns=None,
    layer_column=None,
    quantity_column=None,
    designator_column="Designator",
):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("csv_path", help="CSV file to validate")
    args = parser.parse_args()
    errors, warnings, rows = validate_csv(
        args.csv_path,
        required_columns,
        required_nonblank,
        numeric_columns=numeric_columns,
        layer_column=layer_column,
        quantity_column=quantity_column,
        designator_column=designator_column,
    )
    return print_result(errors, warnings, rows)


if __name__ == "__main__":
    sys.exit(2)
