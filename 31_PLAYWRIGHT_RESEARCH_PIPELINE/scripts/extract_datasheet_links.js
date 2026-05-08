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
  const data = JSON.parse(fs.readFileSync(args.input, "utf8"));
  const links = [];
  if (data.datasheet_url) links.push(data.datasheet_url);
  if (Array.isArray(data.links)) {
    for (const link of data.links) {
      const url = typeof link === "string" ? link : link.url;
      if (url && /datasheet|data-sheet|pdf|document/i.test(url)) links.push(url);
    }
  }
  const output = {
    status: "DATASHEET_LINK_EXTRACTION",
    source_url: data.source_url || "UNKNOWN",
    retrieved_at: data.retrieved_at || new Date().toISOString(),
    datasheet_links: [...new Set(links)],
    pdfs_downloaded: false,
    redistribution_status: "LINK_ONLY",
    verification_status: "UNVERIFIED",
    human_review_required: true
  };
  const outPath = args.out ? path.resolve(args.out) : path.resolve(path.dirname(args.input), "datasheet_links.normalized.json");
  fs.writeFileSync(outPath, JSON.stringify(output, null, 2) + "\n");
  console.log(`Datasheet links written: ${outPath}`);
}

main();
