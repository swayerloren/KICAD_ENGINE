"use strict";

const fs = require("fs");
const path = require("path");

function parseArgs(argv) {
  const args = { input: "", out: "" };
  for (let i = 2; i < argv.length; i += 1) {
    if (argv[i] === "--input") args.input = argv[++i] || "";
    else if (argv[i] === "--out") args.out = argv[++i] || "";
  }
  return args;
}

function main() {
  const args = parseArgs(process.argv);
  if (!args.input) {
    console.error("Missing --input JSON file.");
    process.exit(2);
  }
  const input = JSON.parse(fs.readFileSync(args.input, "utf8"));
  const record = {
    manufacturer: input.manufacturer || "UNKNOWN",
    manufacturer_part_number: input.manufacturer_part_number || input.part_number || "UNKNOWN",
    supplier: input.supplier || input.source_name || "UNKNOWN",
    supplier_sku: input.supplier_sku || "UNKNOWN",
    family: input.family || "UNKNOWN",
    category: input.category || "UNKNOWN",
    package: input.package || input.package_name_from_source || "UNKNOWN",
    source_url: input.source_url || "UNKNOWN",
    retrieved_at: input.retrieved_at || new Date().toISOString(),
    verification_status: "UNVERIFIED",
    human_review_required: true
  };
  const outPath = args.out ? path.resolve(args.out) : path.resolve(path.dirname(args.input), "part_metadata.normalized.json");
  fs.writeFileSync(outPath, JSON.stringify(record, null, 2) + "\n");
  console.log(`Part metadata written: ${outPath}`);
}

main();
