#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
====================================================================
  Efectral DSL — DESINSTALADOR / LIMPIEZA TOTAL DE ENTORNO
  Organización: E J G 4 — Startup Fintech
  Autor: Julio César Gallardo
  Licencia: MIT
====================================================================
Elimina la extensión instalada en todos los editores y los artefactos
generados, dejando el sistema en estado completamente limpio.
(Conserva intactos todos los archivos fuente del proyecto).
"""

import sys
import os
import shutil

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

EXTENSION_ID = "efectral-dsl-support-1.0.0"

def get_target_directories():
    home = os.path.expanduser("~")
    candidates = [
        ("VS Code", os.path.join(home, ".vscode", "extensions")),
        ("Cursor", os.path.join(home, ".cursor", "extensions")),
        ("Antigravity IDE", os.path.join(home, ".antigravity-ide", "extensions")),
        ("Antigravity App", os.path.join(home, ".gemini", "antigravity", "extensions")),
        ("VSCodium", os.path.join(home, ".vscode-oss", "extensions")),
        ("Windsurf", os.path.join(home, ".windsurf", "extensions")),
    ]
    return candidates

def clean_system():
    print("=" * 72)
    print("  Efectral DSL — DESINSTALACIÓN Y LIMPIEZA DE ENTORNO")
    print("  E J G 4 — Julio César Gallardo")
    print("=" * 72)

    removed_count = 0
    targets = get_target_directories()

    print("\n1. Eliminando extensión de los editores...")
    for name, base_path in targets:
        dest_folder = os.path.join(base_path, EXTENSION_ID)
        if os.path.exists(dest_folder):
            try:
                shutil.rmtree(dest_folder)
                print(f"  [-] Eliminado de {name}: {dest_folder}")
                removed_count += 1
            except Exception as e:
                print(f"  [!] Error al eliminar de {name}: {e}")

    # Limpiar artefactos generados en la raíz del repositorio para prueba pura
    repo_root = os.path.abspath(os.path.dirname(__file__))
    print("\n2. Limpiando binarios y accesos generados temporalmente...")
    
    dist_dir = os.path.join(repo_root, "dist")
    if os.path.exists(dist_dir):
        try:
            shutil.rmtree(dist_dir)
            print(f"  [-] Directorio dist/ eliminado: {dist_dir}")
        except Exception as e:
            print(f"  [!] Error al eliminar dist/: {e}")

    efc_cmd = os.path.join(repo_root, "efc.cmd")
    if os.path.exists(efc_cmd):
        try:
            os.remove(efc_cmd)
            print(f"  [-] Acceso directo efc.cmd eliminado.")
        except Exception as e:
            pass

    for item in os.listdir(repo_root):
        if item.endswith(".egg-info"):
            full_egg = os.path.join(repo_root, item)
            try:
                shutil.rmtree(full_egg)
                print(f"  [-] Carpeta {item} eliminada.")
            except Exception:
                pass

    print("\n" + "=" * 72)
    print("  ¡LIMPIEZA COMPLETADA CON ÉXITO!")
    print(f"  - Extensiones eliminadas en {removed_count} editor(es).")
    print("  - El sistema ha quedado completamente limpio (estado virgen).")
    print("  - Los archivos fuente y especificaciones de Efectral DSL están intactos.")
    print("  - Reinicia tu editor para que descargue la memoria de la extensión.")
    print("=" * 72 + "\n")

if __name__ == "__main__":
    clean_system()
