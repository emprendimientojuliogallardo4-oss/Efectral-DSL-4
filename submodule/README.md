# Submódulo / Librería Portable Efectral DSL
> **Organización:** E J G 4 — Startup Fintech  
> **Patrón de Arquitectura:** Submódulo Fuente Embebido  

Este directorio es la **librería portable de Efectral DSL**. Se incluye dentro de cualquier repositorio de agentes (como submódulo Git o como carpeta copiada directamente) para que cualquier IA que interactúe con el proyecto entienda y pueda programar en Efectral DSL (`.efd`) sin dependencias externas.

---

## 1. ¿Cómo se instala en un proyecto huésped?

### Opción A: Como Submódulo Git (Recomendado)
Desde la raíz del repositorio de tu agente:
```bash
git submodule add https://github.com/emprendimientojuliogallardo4-oss/Efectral-DSL-4.git efectral/
```

### Opción B: Como Carpeta Fuente Local
Copia el contenido íntegro de este directorio `submodule/` dentro de tu proyecto en la ruta `efectral/` o `lib/efectral/`.

---

## 2. Contenido del Submódulo

* **`EFECTRAL_FORGE.efd`**: La matriz autodescriptiva que permite a la IA actuar como arquitecto y forjador de agentes en `.efd`.
* **`QUICK_START.md`**: Guía canónica compacta para que el modelo aprenda la sintaxis en segundos.
* **`grammar/efectral-dsl.ebnf`**: Gramática formal en notación EBNF.
* **`linter/efc_validator.py`**: Validador sintáctico en Python puro de ejecución inmediata sin dependencias externas.
* **`rules/efectral-dsl.md`**: Reglas de gobernanza que imponen rigor sintáctico y metodología efectualista a los asistentes IA.

---

## 3. ¿Cómo lo utiliza la IA en el proyecto huésped?

Cuando una IA (Antigravity, Cursor, Windsurf, Claude Code, GPT) abre tu proyecto, basta con indicarle:

> *"Actúa bajo las reglas de `efectral/rules/efectral-dsl.md` y forja los prompts del agente usando `efectral/EFECTRAL_FORGE.efd`."*

La IA leerá la gramática y el validador, y generará archivos `.efd` con 0 errores de sintaxis y sin alucinación.
