"use strict";

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");

function main() {
  if (process.argv.includes("--apply")) {
    console.error("--apply is not implemented. Review link-only output manually before editing 06_DATASHEETS.");
    process.exit(2);
  }
  const outDir = path.join(ROOT, "reports");
  fs.mkdirSync(outDir, { recursive: true });
  const outPath = path.join(outDir, "DATASHEET_SOURCE_INDEX_UPDATE_DRY_RUN.md");
  fs.writeFileSync(outPath, [
    "# Datasheet Source Index Update Dry Run",
    "",
    `Generated: ${new Date().toISOString()}`,
    "Status: `DRY_RUN_ONLY`",
    "",
    "No files in `06_DATASHEETS` were modified.",
    "",
    "Future apply mode must keep documents link-only unless redistribution rights are confirmed."
  ].join("\n") + "\n");
  console.log(`Dry-run report written: ${outPath}`);
}

main();
