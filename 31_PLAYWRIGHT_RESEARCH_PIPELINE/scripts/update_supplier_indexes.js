"use strict";

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");

function main() {
  if (process.argv.includes("--apply")) {
    console.error("--apply is not implemented. Review normalized supplier output manually before editing 28_SUPPLIER_INGESTION.");
    process.exit(2);
  }
  const outDir = path.join(ROOT, "reports");
  fs.mkdirSync(outDir, { recursive: true });
  const outPath = path.join(outDir, "SUPPLIER_INDEX_UPDATE_DRY_RUN.md");
  fs.writeFileSync(outPath, [
    "# Supplier Index Update Dry Run",
    "",
    `Generated: ${new Date().toISOString()}`,
    "Status: `DRY_RUN_ONLY`",
    "",
    "No files in `28_SUPPLIER_INGESTION` were modified.",
    "",
    "Future apply mode must not store credentials, private quotes, raw restricted API responses, or scraped HTML."
  ].join("\n") + "\n");
  console.log(`Dry-run report written: ${outPath}`);
}

main();
