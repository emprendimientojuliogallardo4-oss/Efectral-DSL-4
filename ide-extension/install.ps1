# ====================================================================
# Efectral DSL — INSTALADOR RÁPIDO PARA WINDOWS (POWERSHELL)
# Organización: E J G 4 — Julio César Gallardo
# ====================================================================

Write-Host "Iniciando instalación del entorno Efectral DSL..." -ForegroundColor Cyan

if (Get-Command python -ErrorAction SilentlyContinue) {
    python "$PSScriptRoot\install.py"
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    py "$PSScriptRoot\install.py"
} else {
    Write-Host "[ERROR] No se encontró Python en el sistema. Por favor instala Python 3.8 o superior." -ForegroundColor Red
    Exit 1
}
