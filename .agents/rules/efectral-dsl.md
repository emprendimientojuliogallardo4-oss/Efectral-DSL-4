# Regla Oficial de Proyecto: Desarrollo y Ejecución en Efectral DSL (.efd)

Esta regla gobierna de manera automática a Antigravity cada vez que opere en este repositorio o interactúe con archivos `.efd`:

## 1. Disciplina Sintáctica Obligatoria
* Todo valor, lista o estado debe estar delimitado estrictamente entre corchetes: `Clave:[Valor]`.
* Las directivas de sistema duras usan el prefijo `@` (`@Identifícate`, `@Aplica`, `@Fija`, `@Prohíbe`, `@Exige`).
* Las acciones ejecutivas usan el prefijo `!` (`!Verifica`, `!Extrae`, `!Escribe`, `!Ejecuta`, `!Emite`, `!EsperaInstrucciones`).
* El paso de datos entre instrucciones se realiza exclusivamente mediante tuberías y registros léxicos: `-> $Variable`.
* Toda ruta de excepción debe implementar cortocircuito explícito: `SiFalla:[Detén - EmiteAlerta:[...] - EsperaInstrucciones]`.

## 2. Principio Kernel Linux (Anti-Saturación de Contexto)
* Queda terminantemente prohibido generar o estructurar agentes que carguen herramientas masivas sin demanda activa (`CargaMonolítica`).
* Todo sistema agéntico debe implementar `BloqueCargaSelectiva` montando módulos bajo demanda activa según la tarea.
* Los subagentes de cómputo en segundo plano deben estructurarse como Agentes de Identidad 0 (`Identidad:[0]`), sin personalidad ni cortesías.

## 3. Auto-Certificación y Cero Prosa
* Queda terminantemente prohibido emitir prosa humana, saludos o relleno conversacional dentro de bloques `.efd`.
* Tras crear o modificar cualquier archivo `.efd`, Antigravity debe ejecutar automáticamente:
  `python tools/efc_validator.py <archivo_modificado>`
  para certificar 0 errores de sintaxis antes de dar la tarea por concluida.

## 4. Ley de la Metodología Efectualista (El Agente Funcional en Blanco)
* **Prohibición de Herramientas Ficticias:** Ante una orden abierta o ambigua (ej. *"Crea un agente"*, *"Nuevo agente"*), la IA tiene terminantemente prohibido inventar herramientas imaginarias, servidores MCP no existentes en la máquina o dependencias de fantasía.
* **El Agente Funcional en Blanco:** En su lugar, debe devolver un **Agente Funcional en Blanco (Núcleo Efectualista Canónico)**: un agente operativo puro con sus 4 bloques canónicos que arranca en `!EsperaInstrucciones`, diseñado para **ser definido en el propio uso**.
* **Emergencia Operativa:** El agente adquiere herramientas solo cuando el operador en su diálogo se las solicita expresamente (ej. *"Configura un servidor MCP"*). En ese instante, el agente inspecciona el entorno real, evalúa los medios disponibles (Principio Pájaro en Mano) y monta la herramienta real, pero **nunca en su nacimiento previo**.
