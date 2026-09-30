# Biblioteca de Bloques Efectrales (Registry)

Este directorio es el **Centro de Referencia y Operatividad** para la creación de **Agentes Efectrales**.

> **DIRECTIVA ESTRICTA PARA IAS:**
> Al recibir la instrucción de ensamblar, generar o modificar un entidad operativa Efectral, **debes consultar primero esta biblioteca**. 
> NO generes código desde cero si existe un bloque estandarizado aquí que cumpla la función. Extrae el código existente, adáptalo si es estrictamente necesario, y úsalo. Si la funcionalidad requerida NO existe, entonces (y solo entonces) puedes crear un bloque nuevo respetando las reglas de Efectral DSL.

## Glosario de Bloques Estándar

| Bloque | Archivo | Propósito y Definición |
|---|---|---|
| **BloqueIdentidad** | `bloque_identidad.efd` | Define el "Quién es" del Agente. Contiene nombre, rol, organización y misión. Obligatorio en todo entidad operativa Efectral. |
| **BloqueReglas** | `bloque_reglas.efd` | Define el comportamiento conductual y los parámetros del modelo (Ej: TopP:0.1). Establece la Filosofía Efectualista. |
| **BloqueSeguridad** | `bloque_seguridad.efd` | Barreras infranqueables (Guardrails). Prohíbe acciones destructivas o exfiltración de datos. |
| **BloqueEjecucion** | `bloque_ejecucion.efd` | El bucle principal lógico del agente. Define el flujo de acciones determinista. |
