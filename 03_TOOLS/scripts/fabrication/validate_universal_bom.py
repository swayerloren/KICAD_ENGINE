import sys

from fabrication_validator_common import run_csv_validator


if __name__ == "__main__":
    sys.exit(
        run_csv_validator(
            "Validate universal BOM CSV structure. Does not edit KiCad files or upload anything.",
            ["Line #", "Comment", "Quantity", "Designator", "Footprint", "Package", "Type", "LCSC Part #", "Manufacturer", "Manufacturer Part Number", "Distributor", "Distributor Part Number", "Part Description", "Notes", "DNP"],
            ["Comment", "Quantity", "Designator", "Footprint", "Package"],
            quantity_column="Quantity",
            designator_column="Designator",
        )
    )
