$ErrorActionPreference = "Stop"

Write-Host "KiCad Engine devcontainer bootstrap"
Write-Host "----------------------------------"

python --version
git --version

if (Get-Command gh -ErrorAction SilentlyContinue) {
    gh --version | Select-Object -First 2
}

if (Get-Command node -ErrorAction SilentlyContinue) {
    node --version
}

if (Get-Command npm -ErrorAction SilentlyContinue) {
    npm --version
    npm install --global markdownlint-cli | Out-Host
}

Write-Host ""
Write-Host "KiCad Engine note:"
Write-Host "- This container is for repo scripts, documentation, review automation, and safe validation."
Write-Host "- It does not assume KiCad GUI is available."
Write-Host "- KiCad schematic and PCB GUI review still happens locally on Windows with KiCad installed."
Write-Host "- Do not treat Codespaces or the devcontainer as fabrication approval."
