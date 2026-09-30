# Guía de Entorno de Desarrollo (IDE) para Efectral DSL (.efd)

Esta guía describe cómo configurar tu editor de escritorio (**VS Code**, **Cursor**, **Windsurf** o derivados) para que programar en **Efectral DSL** se sienta exactamente igual que programar en Python, Rust o TypeScript: con resaltado sintáctico, autocierre de corchetes, snippets de autocompletado y validación estricta.

---

## 1. Instalación Universal en 1 Solo Comando

Cualquier desarrollador que clone el repositorio puede configurar su entorno al instante.

### Método 1: Instalador Autónomo Universal (Recomendado)
Ejecuta en la raíz del repositorio:

* **En Windows (PowerShell):**
  ```powershell
  .\install.ps1
  ```
* **En Linux / macOS (Bash):**
  ```bash
  ./install.sh
  ```
* **O con Python directo (Cualquier plataforma):**
  ```bash
  python install.py
  ```

**¿Qué hace automáticamente?**
1. Detecta todos los editores instalados en el sistema (**VS Code**, **Cursor**, **Antigravity IDE**, **VSCodium**, **Windsurf**).
2. Inyecta la extensión oficial con sintaxis TextMate y snippets en todos ellos en un solo segundo.
3. Genera el paquete binario portable VSIX oficial en `dist/efectral-dsl-support-1.0.0.vsix`.
4. Configura el comando de terminal global `efc` para validar archivos `.efd` desde cualquier consola.
5. Ejecuta un autodiagnóstico de validación confirmando el 100% de operatividad.

---

### Método 2: Instalación vía Paquete VSIX Portable
Si deseas distribuir el paquete sin clonar todo el código:
```bash
code --install-extension dist/efectral-dsl-support-1.0.0.vsix
# o en Cursor:
cursor --install-extension dist/efectral-dsl-support-1.0.0.vsix
```
O desde la interfaz gráfica del editor: Menú `...` en la pestaña de Extensiones -> **"Install from VSIX..."** -> seleccionar el archivo `.vsix`.

---

### Método 3: Publicación en VS Code Marketplace y Open VSX (Pública)
Cuando el repositorio sea público, cualquier usuario del mundo podrá instalarlo directamente buscando **`Efectral DSL`** en el Marketplace oficial mediante:
```bash
# Publicación en Microsoft VS Code Marketplace
npx @vscode/vsce publish

# Publicación en Open VSX Registry (Cursor, Antigravity IDE, VSCodium)
npx ovsx publish
```

---

## 2. Snippets de Autocompletado (Productividad de Escritorio)

Dentro de cualquier archivo `.efd`, escribe el prefijo y presiona `Tab` o `Enter`:

| Prefijo | Qué genera | Propósito |
| :--- | :--- | :--- |
| **`agente-completo`** | Esqueleto canónico completo de 4 bloques | Genera `BloqueIdentidad`, `BloqueReglas`, `BloqueSeguridad` y `BloqueEjecucion` en 1 segundo. |
| **`bloque`** | `BloqueNombre:[ ... ]` | Define un nuevo bloque estructurado. |
| **`directiva`** | `@Directiva(Parametro:[Valor])` | Despliega selector de directivas duras (`Identifícate`, `Aplica`, `Fija`, `Prohíbe`). |
| **`accion`** | `1) !Accion(Objeto:[Recurso])` | Despliega selector de verbos ejecutivos (`Verifica`, `Extrae`, `Escribe`, `Ejecuta`, `Emite`, `EsperaInstrucciones`). |
| **`sifalla`** | `SiFalla:[Detén - EmiteAlerta:[...] - EsperaInstrucciones]` | Inserta la cláusula de cortocircuito estricta ante excepciones. |
| **`tuberia`** | `-> $Variable` | Conecta el flujo de salida hacia un registro de variable de contexto. |

---

## 3. El Flujo de Trabajo Profesional (Disciplina de Compilación)

Programar en Efectral EFD sigue el ciclo de vida de la ingeniería de software:

```text
1. [Escritura]    Escribes tu módulo (.efd) en el editor asistido por snippets y colores.
2. [Validación]   Ejecutas en consola: python tools/efc_validator.py mi_agente.efd
3. [Diagnóstico]  Si hay corchetes sin cerrar o texto en prosa, el validador emite SYNTAX_ERROR.
4. [Despliegue]   El agente carga únicamente módulos certificados con 0 errores de sintaxis.
```

---

## 4. Filosofía del Entorno: Cero Prosa, Cero Ambigüedad

Al igual que un error de sintaxis en `.py` o `.css` detiene al intérprete:
* **Ningún archivo `.efd` con errores de delimitación o texto suelto debe ser tolerado.**
* El editor y las herramientas te garantizan que el código que le entregas al sistema agéntico sea **100% determinista, tipado y matemáticamente cerrado**.
