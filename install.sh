#!/usr/bin/env bash
# ====================================================================
# Efectral DSL — INSTALADOR RÁPIDO PARA LINUX / MACOS (BASH)
# Organización: E J G 4 — Julio César Gallardo
# ====================================================================

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Iniciando instalación del entorno Efectral DSL..."

if command -v python3 &>/dev/null; then
    python3 "$DIR/install.py"
elif command -v python &>/dev/null; then
    python "$DIR/install.py"
else
    echo "[ERROR] No se encontró Python 3 en el sistema."
    exit 1
fi
