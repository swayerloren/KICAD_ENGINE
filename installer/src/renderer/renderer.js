"use strict";

const api = window.kicadEngineInstaller;

const elements = {
  platformLabel: document.getElementById("platformLabel"),
  payloadStatus: document.getElementById("payloadStatus"),
  workspacePath: document.getElementById("workspacePath"),
  choosePathButton: document.getElementById("choosePathButton"),
  refreshDepsButton: document.getElementById("refreshDepsButton"),
  dependencySummary: document.getElementById("dependencySummary"),
  dependencyRows: document.getElementById("dependencyRows"),
  installButton: document.getElementById("installButton"),
  openWorkspaceButton: document.getElementById("openWorkspaceButton"),
  openVsCodeCheckbox: document.getElementById("openVsCodeCheckbox"),
  installStatus: document.getElementById("installStatus"),
  logOutput: document.getElementById("logOutput")
};

let currentDependencyReport = null;

function appendLog(message) {
  const line = `[${new Date().toLocaleTimeString()}] ${message}`;
  elements.logOutput.textContent += `${line}\n`;
  elements.logOutput.scrollTop = elements.logOutput.scrollHeight;
}

function setBusy(isBusy) {
  elements.installButton.disabled = isBusy;
  elements.refreshDepsButton.disabled = isBusy;
  elements.choosePathButton.disabled = isBusy;
  elements.openWorkspaceButton.disabled = isBusy;
  elements.installStatus.textContent = isBusy ? "Working" : "Idle";
}

function statusBadge(found, required) {
  const cls = found ? "status-found" : required ? "status-missing" : "status-warn";
  const text = found ? "Found" : required ? "Missing" : "Optional";
  return `<span class="status ${cls}">${text}</span>`;
}

function renderDependencies(report) {
  currentDependencyReport = report;
  const missingRequired = report.dependencies.filter((item) => item.required && !item.found);
  const missingOptional = report.dependencies.filter((item) => !item.required && !item.found);
  elements.dependencySummary.textContent = `${missingRequired.length} required missing, ${missingOptional.length} optional missing`;

  elements.dependencyRows.innerHTML = "";
  for (const dependency of report.dependencies) {
    const row = document.createElement("tr");
    const actionCell = document.createElement("td");

    if (!dependency.found && dependency.installPlan.available) {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "small-button";
      button.textContent = `Install with ${dependency.installPlan.label}`;
      button.addEventListener("click", () => installDependency(dependency));
      actionCell.appendChild(button);
    } else if (!dependency.found) {
      const manual = document.createElement("span");
      manual.className = "manual";
      manual.textContent = dependency.installPlan.manual.join(" | ") || "Manual install";
      actionCell.appendChild(manual);
    } else {
      actionCell.textContent = dependency.detail || "Available";
    }

    row.innerHTML = `
      <td><strong>${dependency.displayName}</strong></td>
      <td>${statusBadge(dependency.found, dependency.required)}</td>
      <td>${dependency.purpose || ""}</td>
    `;
    row.appendChild(actionCell);
    elements.dependencyRows.appendChild(row);
  }
}

async function refreshDependencies() {
  setBusy(true);
  try {
    appendLog("Checking dependencies.");
    const report = await api.checkDependencies();
    renderDependencies(report);
    appendLog("Dependency check complete.");
  } catch (error) {
    appendLog(`Dependency check failed: ${error.message || error}`);
  } finally {
    setBusy(false);
  }
}

async function installDependency(dependency) {
  const command = dependency.installPlan.command
    ? `${dependency.installPlan.command} ${dependency.installPlan.args.join(" ")}`.trim()
    : "manual install";
  const confirmed = window.confirm(`Install ${dependency.displayName}?\n\nCommand:\n${command}\n\nThe installer will not collect credentials or run this silently.`);
  if (!confirmed) {
    appendLog(`Skipped install for ${dependency.displayName}.`);
    return;
  }
  setBusy(true);
  try {
    appendLog(`Installing ${dependency.displayName} with ${dependency.installPlan.label}.`);
    const result = await api.installDependency({ dependencyId: dependency.id, confirmed: true });
    appendLog(result.ok ? `Install command completed for ${dependency.displayName}.` : `Install command did not complete cleanly for ${dependency.displayName}.`);
    if (result.stderr) appendLog(result.stderr);
    await refreshDependencies();
  } catch (error) {
    appendLog(`Install failed: ${error.message || error}`);
  } finally {
    setBusy(false);
  }
}

async function createAndCheckWorkspace() {
  const workspacePath = elements.workspacePath.value.trim();
  if (!workspacePath) {
    appendLog("Choose a workspace path first.");
    return;
  }
  setBusy(true);
  try {
    appendLog(`Creating workspace: ${workspacePath}`);
    const createResult = await api.createWorkspace({ targetPath: workspacePath });
    appendLog(`Workspace copied files: ${createResult.copied.length}; skipped existing files: ${createResult.skipped.length}.`);
    appendLog(`Setup log: ${createResult.setupLog}`);

    appendLog("Running health check.");
    const healthResult = await api.runHealthCheck({ workspacePath });
    appendLog(healthResult.stdout || healthResult.stderr || "Health check finished.");

    if (elements.openVsCodeCheckbox.checked) {
      appendLog("Opening VS Code or workspace folder.");
      const openResult = await api.openVSCode({ workspacePath });
      appendLog(openResult.ok ? "VS Code open command completed." : (openResult.stderr || "Open command returned a warning."));
    }
  } catch (error) {
    appendLog(`Install failed: ${error.message || error}`);
  } finally {
    setBusy(false);
  }
}

async function openWorkspaceFolder() {
  const workspacePath = elements.workspacePath.value.trim();
  if (!workspacePath) {
    appendLog("Choose a workspace path first.");
    return;
  }
  const result = await api.openVSCode({ workspacePath });
  appendLog(result.ok ? "Open command completed." : (result.stderr || "Open command returned a warning."));
}

async function boot() {
  setBusy(true);
  try {
    const state = await api.getInitialState();
    elements.platformLabel.textContent = `${state.platform.label} - default workspace ${state.defaultWorkspacePath}`;
    elements.payloadStatus.textContent = "Clean payload available";
    elements.workspacePath.value = state.defaultWorkspacePath;
    appendLog(`Installer version ${state.installerVersion}.`);
    appendLog(`Payload root: ${state.payloadRoot}`);
  } catch (error) {
    appendLog(`Startup failed: ${error.message || error}`);
  } finally {
    setBusy(false);
  }
  await refreshDependencies();
}

elements.choosePathButton.addEventListener("click", async () => {
  const chosen = await api.chooseWorkspacePath();
  if (chosen) elements.workspacePath.value = chosen;
});
elements.refreshDepsButton.addEventListener("click", refreshDependencies);
elements.installButton.addEventListener("click", createAndCheckWorkspace);
elements.openWorkspaceButton.addEventListener("click", openWorkspaceFolder);

boot();
