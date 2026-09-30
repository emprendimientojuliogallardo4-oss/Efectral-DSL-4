---
name: efectral-forge
description: Forja, valida y genera agentes y módulos en Efectral DSL (.efd) conforme al estándar 1.0.0. Úsalo cuando el usuario pida crear nuevos agentes, módulos agénticos, o auditar sintaxis en Efectral.
---

# Efectral Forge: Generador y Validador de Agentes

Esta habilidad equipa a Antigravity con los protocolos de ingeniería para forjar sistemas agénticos en **Efectral DSL (EFD)**:

## Procedimiento de Forja:
1. **Analizar Requerimientos bajo Metodología Efectualista:**
   * **Instrucción Abierta o Ambigua (ej. *"Crea un agente"*):** PROHIBIDO inventar herramientas ficticias, servidores MCP imaginarios o bases de datos no existentes. Debe forjar un **Agente Funcional en Blanco (Núcleo Efectualista)** listo para ser **definido en el propio uso**, cuyo `BloqueEjecucion` comience en `!EsperaInstrucciones`.
   * **Requerimientos Específicos:** Extraer objetivo, dominio real y herramientas verificables.
2. **Determinar Arquitectura:**
   * Si es una tarea aislada o microservicio -> Generar un **Agente Efectral Contenido** (un solo archivo `.efd` con los 4 bloques).
   * Si es un ecosistema complejo -> Generar un **Sistema Agéntico Modular (Kernel Linux)** con `BOOTSTRAP.efd` (usando `BloqueCargaSelectiva`), módulos dedicados y subagentes de `Identidad:[0]`.
3. **Escribir Código Formal:** Emplear delimitación estricta `Clave:[Valor]`, prefijos `@` y `!`, tuberías `-> $Var` y cortocircuitos `SiFalla`.
4. **Auto-Auditoría Obligatoria:** Ejecutar `python tools/efc_validator.py <archivo.efd>` en la terminal. Solo entregar el resultado cuando la auditoría arroje 0 errores.
