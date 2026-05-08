"use strict";

const fs = require("fs");
const path = require("path");
const { runCommand, commandExists } = require("./commandRunner");
const { detectPlatform, expandPathVariables, pathExists } = require("./platformDetect");

function manifestFileName(platformKey) {
  return `dependencies.${platformKey}.json`;
}

function loadManifest(manifestsRoot, platformKey = detectPlatform().key) {
  const manifestPath = path.join(manifestsRoot, manifestFileName(platformKey));
  const raw = fs.readFileSync(manifestPath, "utf8");
  return JSON.parse(raw);
}

async function detectPackageManagers(manifest) {
  const found = [];
  for (const manager of manifest.packageManagers || []) {
    const exists = await commandExists(manager.command);
    found.push({
      id: manager.id,
      label: manager.label,
      command: manager.command,
      found: exists.found,
      path: exists.path,
      installPriority: manager.installPriority || 100
    });
  }
  return found.sort((a, b) => a.installPriority - b.installPriority);
}

async function checkCandidate(candidate) {
  if (candidate.type === "path") {
    const expanded = expandPathVariables(candidate.path);
    return {
      ok: pathExists(candidate.path),
      method: "path",
      detail: expanded
    };
  }

  const result = await runCommand({
    command: candidate.command,
    args: candidate.args || [],
    timeoutMs: candidate.timeoutMs || 10000
  });
  return {
    ok: result.ok,
    method: "command",
    detail: result.stdout || result.stderr || `${candidate.command} ${(candidate.args || []).join(" ")}`.trim(),
    exitCode: result.exitCode
  };
}

function selectInstallPlan(dependency, packageManagers) {
  const strategies = dependency.install || {};
  for (const manager of packageManagers) {
    if (manager.found && strategies[manager.id]) {
      return {
        available: true,
        manager: manager.id,
        label: manager.label,
        command: strategies[manager.id].command,
        args: strategies[manager.id].args || [],
        manual: dependency.manual || []
      };
    }
  }
  return {
    available: false,
    manager: null,
    label: "Manual install required",
    command: null,
    args: [],
    manual: dependency.manual || []
  };
}

async function checkDependencies(options = {}) {
  const platform = detectPlatform();
  const manifest = loadManifest(options.manifestsRoot, options.platformKey || platform.key);
  const packageManagers = await detectPackageManagers(manifest);
  const dependencies = [];

  for (const dependency of manifest.dependencies || []) {
    const checks = [];
    for (const candidate of dependency.detect || []) {
      checks.push(await checkCandidate(candidate));
    }
    const foundCheck = checks.find((check) => check.ok);
    dependencies.push({
      id: dependency.id,
      displayName: dependency.displayName,
      required: Boolean(dependency.required),
      purpose: dependency.purpose || "",
      found: Boolean(foundCheck),
      status: foundCheck ? "found" : "missing",
      detail: foundCheck ? foundCheck.detail : checks.map((check) => check.detail).filter(Boolean).join(" | "),
      installPlan: selectInstallPlan(dependency, packageManagers)
    });
  }

  return {
    platform,
    manifestVersion: manifest.version,
    packageManagers,
    dependencies
  };
}

async function installDependency(options = {}) {
  if (!options.confirmed) {
    throw new Error("Install was not confirmed by the user.");
  }
  const platform = detectPlatform();
  const manifest = loadManifest(options.manifestsRoot, options.platformKey || platform.key);
  const packageManagers = await detectPackageManagers(manifest);
  const dependency = (manifest.dependencies || []).find((item) => item.id === options.dependencyId);
  if (!dependency) {
    throw new Error(`Unknown dependency: ${options.dependencyId}`);
  }
  const plan = selectInstallPlan(dependency, packageManagers);
  if (!plan.available) {
    return {
      ok: false,
      manualOnly: true,
      message: "No supported package manager is available. Use manual install instructions.",
      manual: plan.manual
    };
  }
  const result = await runCommand({
    command: plan.command,
    args: plan.args,
    timeoutMs: options.timeoutMs || 60 * 60 * 1000,
    shell: false
  });
  return {
    ok: result.ok,
    manualOnly: false,
    dependencyId: dependency.id,
    displayName: dependency.displayName,
    manager: plan.manager,
    command: `${plan.command} ${plan.args.join(" ")}`.trim(),
    stdout: result.stdout,
    stderr: result.stderr,
    exitCode: result.exitCode,
    timedOut: result.timedOut
  };
}

module.exports = {
  checkDependencies,
  installDependency,
  loadManifest
};
