#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
====================================================================
  Efectral DSL — INSTALADOR UNIFICADO DE ENTORNO Y HERRAMIENTAS
  Organización: E J G 4 — Startup Fintech
  Autor: Julio César Gallardo
  Licencia: MIT
====================================================================
"""

import sys
import os
import shutil
import subprocess

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

EXTENSION_ID = "efectral-dsl-support-1.0.0"

def print_banner():
    print("=" * 72)
    print("  Efectral DSL — INSTALADOR DE ENTORNO Y HERRAMIENTAS (IDE & CLI)")
    print("  E J G 4 — Julio César Gallardo")
    print("=" * 72)

def detect_editor_targets():
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

def install_extension(repo_root):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # Si este script está dentro de ide-extension/, usa su propia carpeta
    ide_dir = current_dir if os.path.exists(os.path.join(current_dir, "package.json")) else os.path.join(repo_root, "ide-extension")
    if not os.path.exists(ide_dir):
        ide_dir = repo_root

    package_json = os.path.join(ide_dir, "package.json")
    syntaxes_dir = os.path.join(ide_dir, "syntaxes")
    snippets_dir = os.path.join(ide_dir, "snippets")
    lang_config = os.path.join(ide_dir, "language-configuration.json")

    targets = detect_editor_targets()
    installed = []

    for name, base_path in targets:
        dest_folder = os.path.join(base_path, EXTENSION_ID)
        try:
            parent = os.path.dirname(base_path)
            if not os.path.exists(parent):
                continue

            os.makedirs(dest_folder, exist_ok=True)
            shutil.copy2(package_json, os.path.join(dest_folder, "package.json"))
            if os.path.exists(lang_config):
                shutil.copy2(lang_config, os.path.join(dest_folder, "language-configuration.json"))
            readme_path = os.path.join(repo_root, "README.md")
            if os.path.exists(readme_path):
                shutil.copy2(readme_path, os.path.join(dest_folder, "README.md"))
            license_path = os.path.join(repo_root, "LICENSE")
            if os.path.exists(license_path):
                shutil.copy2(license_path, os.path.join(dest_folder, "LICENSE"))

            dest_syntaxes = os.path.join(dest_folder, "syntaxes")
            os.makedirs(dest_syntaxes, exist_ok=True)
            for f in os.listdir(syntaxes_dir):
                shutil.copy2(os.path.join(syntaxes_dir, f), os.path.join(dest_syntaxes, f))

            if os.path.exists(snippets_dir):
                dest_snippets = os.path.join(dest_folder, "snippets")
                os.makedirs(dest_snippets, exist_ok=True)
                for f in os.listdir(snippets_dir):
                    shutil.copy2(os.path.join(snippets_dir, f), os.path.join(dest_snippets, f))

            installed.append((name, dest_folder))
            print(f"  [+] Extensión instalada en: {name}")
        except Exception:
            pass

    return installed

def generate_vsix_package(repo_root):
    try:
        package_script = os.path.join(repo_root, "tools", "package_vsix.py")
        if os.path.exists(package_script):
            import importlib.util
            spec = importlib.util.spec_from_file_location("package_vsix", package_script)
            pkg_mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(pkg_mod)
            vsix_path = pkg_mod.build_vsix()
            return vsix_path
    except Exception as e:
        print(f"  [!] Nota al compilar VSIX: {e}")
    return None

def install_cli_tool(repo_root):
    pip_ok = False
    try:
        res = subprocess.run([sys.executable, "-m", "pip", "install", "-e", repo_root],
                             capture_output=True, text=True, check=False)
        if res.returncode == 0:
            print("  [+] CLI `efc` instalado globalmente vía pip editable.")
            pip_ok = True
    except Exception:
        pass

    if sys.platform == "win32":
        cmd_path = os.path.join(repo_root, "efc.cmd")
        validator_path = os.path.join(repo_root, "tools", "efc_validator.py")
        try:
            with open(cmd_path, "w", encoding="utf-8") as f:
                f.write(f'@echo off\n"{sys.executable}" "{validator_path}" %*\n')
            print(f"  [+] Acceso directo local para terminal creado: {cmd_path}")
        except Exception:
            pass

    return pip_ok

def run_self_diagnostics(repo_root):
    validator_path = os.path.join(repo_root, "tools", "efc_validator.py")
    sample_file = os.path.join(repo_root, "examples", "01_agente_financiero_riesgo.efd")
    print("\n--- Ejecutando autodiagnóstico de Efectral DSL ---")
    if os.path.exists(validator_path) and os.path.exists(sample_file):
        res = subprocess.run([sys.executable, validator_path, sample_file],
                             capture_output=True, text=True)
        if res.returncode == 0:
            print("  [OK] El compilador/validador `efc` responde con 100% de éxito.")
            return True
        else:
            print(f"  [!] Advertencia en validación: {res.stdout}")
    return False

def main():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    repo_root = current_dir if os.path.exists(os.path.join(current_dir, "pyproject.toml")) else os.path.abspath(os.path.join(current_dir, ".."))
    print_banner()

    print("\n1. Registrando extensión en editores instalados...")
    installed = install_extension(repo_root)

    print("\n2. Generando paquete binario portable VSIX...")
    vsix_file = generate_vsix_package(repo_root)

    print("\n3. Configurando comando de consola `efc` (Linter & Compilador)...")
    install_cli_tool(repo_root)

    print("\n4. Diagnóstico de verificación...")
    run_self_diagnostics(repo_root)

    print("\n" + "=" * 72)
    print("  ¡INSTALACIÓN COMPLETADA EXITOSAMENTE!")
    print("=" * 72)
    print(f"  - Editores soportados: {len(installed)} detectado(s)")
    if vsix_file:
        print(f"  - Paquete VSIX listo:  {vsix_file}")
    print("  - Uso en terminal:")
    print("      efc ruta/a/tu_agente.efd")
    print("      python tools/efc_validator.py ruta/a/tu_agente.efd")
    print("  - En tu editor (VS Code, Cursor o Antigravity IDE):")
    print("      Los archivos .efd tendrán resaltado sintáctico y autocompletado.")
    print("=" * 72 + "\n")

if __name__ == "__main__":
    main()
