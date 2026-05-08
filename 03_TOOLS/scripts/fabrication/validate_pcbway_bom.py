import sys

from fabrication_validator_common import run_csv_validator


if __name__ == "__main__":
    sys.exit(
        run_csv_validator(
            "Validate PCBWay BOM CSV structure. Does not edit KiCad files or upload anything.",
            ["Line #", "Quantity Per Part Number", "Reference Designator", "Part Number", "Part Description", "Package", "Type", "Manufacturer Name", "Manufacturer Part Number", "Distributor Part Number", "Notes"],
            ["Quantity Per Part Number", "Reference Designator", "Part Number", "Part Description", "Package", "Type"],
            quantity_column="Quantity Per Part Number",
            designator_column="Reference Designator",
        )
    )
