# Supplier Datasheet Footprint Next Steps

Date: 2026-05-03
Current classification: `INTERNAL_ALPHA`

## Next Steps To Reach Public Alpha

1. Move the two legacy Espressif PDFs out of public payload scope or document confirmed redistribution permission.
2. Add a release guard script that fails when unapproved PDFs are present under public payload folders.
3. Add a public-facing policy note that the datasheet library is primarily link-only unless redistribution rights are confirmed.
4. Keep all generated footprint candidates marked `UNVERIFIED` until package drawings and human review exist.
5. Add a small, curated "real records" set that is explicitly not example-only but still `UNVERIFIED` until reviewed.

## Next Steps To Reach Public Beta

1. Implement one official live supplier connector, preferably Digi-Key or Mouser, using environment variables only.
2. Add mocked API fixtures and normalized expected outputs for connector tests.
3. Add CI syntax and dry-run tests for:
   - `28_SUPPLIER_INGESTION`
   - `29_FOOTPRINT_GAP_ANALYSIS`
   - `30_SUPPLIER_FOOTPRINT_MATCHES`
4. Build a package-drawing verification pilot for 5 to 10 high-risk parts:
   - USB-C connector
   - AO3401A PMOS
   - AP63203 regulator
   - TPD2EUSB30ADRTR ESD array
   - STM32F103C8T6 LQFP-48
   - ESP32-S3-WROOM-1 module
5. Add human-review signoff fields to the supplier-footprint match reports.

## Next Steps To Reach Public Release Ready

1. Run a full license and redistribution audit on every bundled PDF, schematic, drawing, vendor document, and example record.
2. Ensure payload builder excludes any restricted PDFs or private supplier data by default.
3. Confirm the working tree is a real Git repository and all release workflows can run from GitHub Actions.
4. Demonstrate at least one end-to-end component ingestion path:
   source link or API record -> normalized supplier record -> component database record -> footprint candidate -> package drawing review -> human-reviewed match.
5. Publish clear limitations:
   - supplier data is time-sensitive
   - prices and stock are not guaranteed
   - footprint candidates are not approvals
   - manufacturing outputs remain `NOT_FINAL` until human review

