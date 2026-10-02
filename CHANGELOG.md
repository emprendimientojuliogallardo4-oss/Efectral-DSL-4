# Registro de Cambios (Changelog) - Efectral DSL

Todas las actualizaciones notables de la Arquitectura Efectral DSL se documentarán en este archivo.
El formato sigue el estándar de registro histórico para facilitar la lectura de agentes y humanos.

---

## [1.2.0] - Discriminador de Tipo y Regla de Herencia Ontológica - (Versión Actual)

### 🚀 Cambio (Qué cambió y Cómo)
- **Discriminador de Tipo en `BloqueIdentidad`:** Evolución del esquema canónico de identificación de `@Identifícate(Agente:[X])` a `@Identifícate(Tipo:[T], Nombre:[X])`.
- **Vocabulario Cerrado de Tipos:** Se define formalmente el conjunto cerrado de identificadores ontológicos para `Tipo`: `{Agente, Skill, Configuracion, Herramienta, Bloque, Memoria}`.
- **Regla de Herencia Ontológica:** Los metadatos de gobernanza global (`-Organizacion`), la directiva de transparencia (`@Aplica(Regla:[Transparencia])`) y las reglas base del sistema viven **exclusivamente** en el artefacto raíz de tipo `[Agente]`. Los artefactos secundarios (`Skill`, `Configuracion`, `Herramienta`, `Bloque`, `Memoria`) heredan la autoridad ontológica raíz y no duplican estos campos, declarando únicamente `Tipo` + `Nombre` + `Rol` + `Mision` y sus especificaciones técnicas locales.
- **Actualización de Plantillas y Ejemplos:** Estandarización de `library/bloque_identidad.efd`, la cédula raíz `efectral-native-v1/IDENTITY.efd`, y la totalidad de los ejemplos canónicos en `examples/*.efd` y `core/examples/*.efd`.
- **Evolución Documental:** Actualización normativa en `SPECIFICATION.md` (secciones 3.1, 4.5 y 4.6), `library/GLOSSARY.md` y delimitación en `docs/SINTAXIS_SEMANTICA_FLEXIBLE.md`.

### 🧠 Motivo (Por qué y Resultado)
- **¿Por qué?** En sistemas agénticos modulares avanzados (principio Kernel Linux), los submódulos auxiliares no deben tratarse ontológicamente como agentes raíz ni saturar la ventana de contexto repitiendo declaraciones organizacionales o de transparencia. Se requería una distinción formal e inequívoca de la naturaleza de cada artefacto sin perder el determinismo estructural.
- **Resultado:** Jerarquía limpia, atómica y altamente escalable. Los LLMs y validadores identifican instantáneamente el rol del archivo en la arquitectura global, preservando la ventana de atención al eliminar redundancias de gobernanza en componentes subordinados.

### 📁 Archivos Afectados
- `VERSION`
- `CHANGELOG.md`
- `SPECIFICATION.md`
- `library/GLOSSARY.md`
- `library/bloque_identidad.efd`
- `docs/SINTAXIS_SEMANTICA_FLEXIBLE.md`
- `efectral-native-v1/IDENTITY.efd`
- `examples/01_hello_agent.efd`
- `examples/02_safe_guardrails.efd`
- `examples/03_pipeline_data.efd`
- `examples/04_efectral_4_canonical.efd`
- `examples/05_agente_funcional_en_blanco.efd`
- `examples/06_agente_contenido.efd`
- `core/examples/01_hello_agent.efd`
- `core/examples/02_safe_guardrails.efd`
- `core/examples/03_pipeline_data.efd`
- `core/examples/04_efectral_4_canonical.efd`
- `core/examples/05_agente_funcional_en_blanco.efd`

---

## [1.1.0] - Evolución Semántica y Estandarización

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
