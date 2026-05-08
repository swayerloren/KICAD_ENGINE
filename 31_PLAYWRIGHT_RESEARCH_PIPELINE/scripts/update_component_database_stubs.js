"use strict";

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");

function hasFlag(flag) {
  return process.argv.includes(flag);
}

function main() {
  const apply = hasFlag("--apply");
  if (apply) {
    console.error("--apply is not implemented. Review output manually before editing 08_COMPONENT_DATABASE.");
    process.exit(2);
  }
  const outDir = path.join(ROOT, "reports");
  fs.mkdirSync(outDir, { recursive: true });
  const outPath = path.join(outDir, "COMPONENT_DATABASE_UPDATE_DRY_RUN.md");
  const lines = [
    "# Component Database Update Dry Run",
    "",
    `Generated: ${new Date().toISOString()}`,
    "Status: `DRY_RUN_ONLY`",
    "",
    "No files in `08_COMPONENT_DATABASE` were modified.",
    "",
    "Future apply mode must preserve `UNVERIFIED` status until official source or human review evidence exists."
  ];
  fs.writeFileSync(outPath, `${lines.join("\n")}\n`);
  console.log(`Dry-run report written: ${outPath}`);
}

main();
