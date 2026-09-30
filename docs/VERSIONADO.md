# Gestión de Versiones en Efectral DSL

Desde el Reinicio Histórico (Clean Slate), el proyecto Efectral DSL adopta un modelo de versionado estricto y transparente.

## ¿Qué determina la versión actual?
La versión oficial del lenguaje y del repositorio público se rige por tres anclas:

1. **El archivo `VERSION` (Raíz del Repositorio):**
   - Es la fuente de verdad absoluta a nivel de archivos. Contiene únicamente el número semántico actual (ej. `1.0.0`). Cualquier herramienta automatizada o IA debe leer este archivo para saber en qué versión está trabajando.

2. **Git Tags (Etiquetas de Repositorio):**
   - Cada iteración estable está marcada en el historial de Git con una etiqueta inmutable (ej. `v1.0.0`, `v1.1.0`). Los *releases* de GitHub se basan exclusivamente en estos tags.

3. **La Nomenclatura del Protocolo (Dentro del DSL):**
   - Cuando un agente declara su arquitectura dentro de un archivo `.efd`, la versión del lenguaje se inyecta nativamente como un parámetro de protocolo: `-Protocolo:[Efectral_Native_v1]`.

## Reglas de Actualización (SemVer)
- **Cambios Mayores (v2.0.0):** Cuando se alteran los símbolos base del lenguaje (ej. cambiar el uso de `@` o `!`).
- **Cambios Menores (v1.1.0):** Adición de nuevas plantillas, directivas de conversión o mejoras en el GLOSSARY.
- **Parches (v1.0.1):** Corrección de errores tipográficos o enlaces rotos en la documentación.
