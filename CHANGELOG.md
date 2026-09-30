# Registro de Cambios (Changelog) - Efectral DSL

Todas las actualizaciones notables de la Arquitectura Efectral DSL se documentarán en este archivo.
El formato sigue el estándar de registro histórico para facilitar la lectura de agentes y humanos.

---

## [1.1.0] - Evolución Semántica y Estandarización - (Versión Actual)

### 🚀 Añadido (Qué cambió y Cómo)
- **Sintaxis Semántica Flexible:** Se integró el documento `docs/SINTAXIS_SEMANTICA_FLEXIBLE.md` que establece la inmunidad al idioma y la capacidad de la IA para inventar etiquetas deterministas en tiempo real (ej. `!Ruta`, `!ModulaTono`).
- **Traductor Universal NLP a DSL:** Creación de `directives/NL_TO_DSL_PROMPT.md`. Un metaprompt estandarizado para inyectar en cualquier LLM, ordenándole actuar como Arquitecto Efectral.
- **Sistema de Versionado:** Creación del archivo raíz `VERSION` y `docs/VERSIONADO.md` para anclar el estado del proyecto.

### 🧠 Propósito (Por qué y Resultado)
- **¿Por qué?** Porque el repositorio público necesitaba ser 100% modular y reproducible. Los usuarios e IAs externas estaban limitados a "copiar" plantillas rígidas en lugar de "programar" lógicas fluidas basadas en el lenguaje natural.
- **Resultado:** Efectral DSL ya no es solo una plantilla, es un *Lenguaje de Programación Agéntica Dinámico*. Cualquier IA puede leer el metaprompt y generar capas cognitivas masivas y personalizadas sin romper el estándar.

---

## [1.0.0] - Génesis (Clean Slate)

### 🚀 Añadido
- **Lanzamiento de Efectral Native v1:** Despliegue oficial de la arquitectura.
- **Reinicio Histórico (Clean Slate):** Eliminación total del historial de Git anterior para establecer una base pura y auditable.
- **Purga de Vestigios:** Erradicación de las dependencias y terminología heredada de las versiones no oficiales (Efectral 4).
- **Estructura Base:** Consolidación de los bloques fundamentales (`BloqueIdentidad`, `BloqueReglas`, `BloqueEjecucion`) y el glosario central.
