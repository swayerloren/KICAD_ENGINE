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

function normalize(item) {
  return {
    manufacturer: item.manufacturer || item.vendor || "UNKNOWN",
    manufacturer_part_number: item.manufacturer_part_number || item.part_number || "UNKNOWN",
    supplier: item.supplier || "UNKNOWN",
    supplier_sku: item.supplier_sku || "UNKNOWN",
    family: item.family || "UNKNOWN",
    category: item.category || "UNKNOWN",
    description: item.description || "UNVERIFIED",
    package: item.package || item.package_name_from_source || "UNKNOWN",
    lifecycle_status: item.lifecycle_status || "UNKNOWN_REQUIRES_SOURCE",
    stock_status: item.stock_status || "UNKNOWN_REQUIRES_SOURCE",
    price_breaks_summary: item.price_breaks_summary || "UNKNOWN_REQUIRES_SOURCE",
    datasheet_url: item.datasheet_url || "UNKNOWN",
    product_url: item.product_url || item.source_url || "UNKNOWN",
    source_url: item.source_url || "UNKNOWN",
    source_type: item.source_type || "UNKNOWN",
    retrieved_at: item.retrieved_at || new Date().toISOString(),
    source_confidence: item.source_confidence || "UNKNOWN",
    redistribution_status: item.redistribution_status || "LINK_ONLY",
    verification_status: item.verification_status || "UNVERIFIED",
    kicad_symbol_candidates: item.kicad_symbol_candidates || [],
    kicad_footprint_candidates: item.kicad_footprint_candidates || [],
    package_drawing_status: item.package_drawing_status || "UNVERIFIED",
    footprint_match_status: item.footprint_match_status || "UNVERIFIED",
    human_review_required: true,
    notes: item.notes || "Normalized from research evidence. Not verified."
  };
}

function main() {
  const args = parseArgs(process.argv);
  if (!args.input) {
    console.error("Missing --input JSON file.");
    process.exit(2);
  }
  const raw = JSON.parse(fs.readFileSync(args.input, "utf8"));
  let normalized;
  if (Array.isArray(raw)) {
    normalized = raw.map(normalize);
  } else if (Array.isArray(raw.records)) {
    normalized = raw.records.map((record) => normalize({
      ...record,
      source_type: record.mode || raw.status || "DRY_RUN",
      retrieved_at: raw.generated_at || record.retrieved_at
    }));
  } else {
    normalized = normalize(raw);
  }
  const outPath = args.out ? path.resolve(args.out) : path.resolve(path.dirname(args.input), "normalized_research_output.json");
  fs.writeFileSync(outPath, JSON.stringify(normalized, null, 2) + "\n");
  console.log(`Normalized output written: ${outPath}`);
}

main();
