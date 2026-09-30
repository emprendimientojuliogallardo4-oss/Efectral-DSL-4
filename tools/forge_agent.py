#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
====================================================================
  EFECTRAL FORGE AGENT — GENERADOR CANÓNICO DE AGENTES NATIVOS
  Organización: E J G 4 — Startup Fintech
  Autor: Julio César Gallardo
  Licencia: MIT
====================================================================
Clona e instancia un nuevo agente derivado de Efectral Native v1
(OpenClaw + Efectral DSL) en blanco, listo para ser definido en el uso.
"""

import sys
import os
import shutil
import argparse
import subprocess

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def forge_new_agent(target_path: str, agent_name: str = None):
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    template_dir = os.path.join(repo_root, "efectral-4-native")
    
    if not os.path.exists(template_dir):
        print(f"[ERROR] No se encontró el agente modelo en: {template_dir}")
        sys.exit(1)

    dest_dir = os.path.abspath(target_path)
    if os.path.exists(dest_dir):
        print(f"[AVISO] El directorio destino ya existe: {dest_dir}")
    else:
        os.makedirs(dest_dir, exist_ok=True)

    if not agent_name:
        agent_name = os.path.basename(dest_dir)

    print("=" * 70)
    print(f"  FORJANDO AGENTE: {agent_name}")
    print("  Modelo Base: Efectral Native v1 (OpenClaw + Efectral DSL)")
    print("  E J G 4 — Julio César Gallardo")
    print("=" * 70)

    # Copiar estructura completa
    for item in os.listdir(template_dir):
        s = os.path.join(template_dir, item)
        d = os.path.join(dest_dir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

    # Personalizar IDENTITY.efd con el nombre solicitado
    ident_efd = os.path.join(dest_dir, "IDENTITY.efd")
    if os.path.exists(ident_efd):
        with open(ident_efd, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("Agente:[Efectral_4_Native]", f"Agente:[{agent_name}]")
        with open(ident_efd, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"  [+] Workspace agéntico copiado exitosamente en: {dest_dir}")

    # Validar integridad sintáctica del nuevo agente
    validator_path = os.path.join(repo_root, "tools", "efc_validator.py")
    if os.path.exists(validator_path):
        res = subprocess.run([sys.executable, validator_path, dest_dir], capture_output=True, text=True)
        if res.returncode == 0:
            print("  [OK] Todos los módulos .efd certificados con 0 errores de sintaxis.")
        else:
            print(f"  [!] Diagnóstico: {res.stdout}")

    print("\n" + "=" * 70)
    print("  ¡AGENTE EN BLANCO GENERADO EXITOSAMENTE!")
    print(f"  Ruta: {dest_dir}")
    print("  Metodología: Efectualista (Definición en el propio uso).")
    print("=" * 70 + "\n")

def main():
    parser = argparse.ArgumentParser(
        description="Generador y clonador de agentes Efectral Native v1 (OpenClaw + Efectral DSL)."
    )
    parser.add_argument("destino", help="Ruta o nombre del nuevo agente")
    parser.add_argument("--name", "-n", default=None, help="Nombre del agente (por defecto el nombre de la carpeta)")

    args = parser.parse_args()
    forge_new_agent(args.destino, args.name)

if __name__ == "__main__":
    main()
