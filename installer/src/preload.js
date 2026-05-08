"use strict";

const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("kicadEngineInstaller", {
  getInitialState: () => ipcRenderer.invoke("installer:getInitialState"),
  chooseWorkspacePath: () => ipcRenderer.invoke("installer:chooseWorkspacePath"),
  checkDependencies: () => ipcRenderer.invoke("installer:checkDependencies"),
  installDependency: (payload) => ipcRenderer.invoke("installer:installDependency", payload),
  createWorkspace: (payload) => ipcRenderer.invoke("installer:createWorkspace", payload),
  runHealthCheck: (payload) => ipcRenderer.invoke("installer:runHealthCheck", payload),
  openVSCode: (payload) => ipcRenderer.invoke("installer:openVSCode", payload)
});
