# Soporte Oficial de Entorno IDE para Efectral DSL (.efd)
> **Organización:** E J G 4 — Startup Fintech  
> **Editores Compatibles:** VS Code, Cursor, Windsurf, Antigravity IDE, VSCodium  

Este subdirectorio contiene la infraestructura oficial de lenguaje, gramática TextMate, snippets e instaladores para entornos de desarrollo.

---

## 1. Instalación Rápida (1 Solo Comando)

Para instalar y activar automáticamente la extensión en todos los editores detectados en tu equipo:

* **En Windows (PowerShell):**
  ```powershell
  .\install.ps1
  ```
* **En Linux / macOS (Bash):**
  ```bash
  ./install.sh
  ```
* **Con Python (Multiplataforma):**
  ```bash
  python install.py
  ```

---

## 2. Contenido del Paquete

* **`syntaxes/efectral.tmLanguage.json`**: Gramática TextMate con resaltado completo para directivas `@`, acciones `!`, variables `$`, corchetes y cortocircuitos `SiFalla`.
* **`snippets/efectral.json`**: Plantillas rápidas para agentes completos, bloques y bifurcaciones.
* **`language-configuration.json`**: Reglas de autocierre de delimitadores y plegado de código.
* **`package.json`**: Manifiesto oficial de extensión para empaquetado binario `.vsix`.
* **`install.py` / `uninstall.py`**: Scripts de instalación y desinstalación desatendida.
