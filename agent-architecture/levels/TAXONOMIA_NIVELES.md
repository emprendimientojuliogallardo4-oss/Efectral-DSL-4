# Taxonomía Operativa de Agentes Efectral por Niveles
> **Organización:** E J G 4 — Startup Fintech  
> **Estándar:** Efectral Native v1.0.0  

La metodología efectualista clasifica la construcción de agentes en cuatro niveles de madurez funcional para evitar el sobredimensionamiento (*bloat*) de contexto:

```
                  ┌──────────────────────────────────────────────┐
                  │    NIVEL 4: Enjambre Modular / Ecosistema    │
                  ├──────────────────────────────────────────────┤
                  │    NIVEL 3: Agente Autónomo Persistente      │
                  ├──────────────────────────────────────────────┤
                  │    NIVEL 2: Agente Táctico Especializado     │
                  ├──────────────────────────────────────────────┤
                  │    NIVEL 1: Cómputo Frío / Identidad 0       │
                  └──────────────────────────────────────────────┘
```

---

## Nivel 1: Hilo de Cómputo Frío / Identidad 0 (`Identidad:[0]`)

* **Definición:** Subproceso atómico de cómputo neuronal puro. No tiene personalidad, no saluda, no posee ego ni mantiene memoria persistente.
* **Composición:** Un único archivo `.efd` autocontenido.
* **Propósito:** Recibir un dato, ejecutar una transformación matemática o semántica rígida y volcar el resultado a un registro `-> $Var` en silencio.
* **Directiva Clave:** `@Identifícate(Agente:[Identidad_0] - Nivel:[1])`.
* **Casos de Uso:** Validadores de sintaxis, extractores de parámetros numéricos, auditores de formato, parsers.

---

## Nivel 2: Agente Táctico Especializado

* **Definición:** Agente con rol funcional acotado y herramientas locales específicas para una misión técnica concreta.
* **Composición:** `IDENTITY.efd` + `TOOLS.efd` + archivo de ejecución `.efd`.
* **Propósito:** Resolver una tarea mono-hilo bajo demanda (on-demand), sin mantener estado entre sesiones largas ni ejecutar latidos periódicos.
* **Casos de Uso:** Asistente de compilación, generador de reportes de riesgo financiero para cTrader, auditor de seguridad de dependencias.

---

## Nivel 3: Agente Autónomo Persistente (Canónico Efectral Native v1)

* **Definición:** El estándar operativo industrial completo de E J G 4. Posee identidad institucional, voz definida, pipeline de guardarraíles, gestión de memoria multicapa y rutinas de fondo.
* **Composición:**
  - `IDENTITY.efd` (Cédula y transparencia).
  - `SOUL.efd` (Directivas de voz, brevedad y valores).
  - `AGENTS.efd` (Gobernanza de mono-tarea, pipeline y cortocircuitos).
  - `TOOLS.efd` (Catálogo y ruteo de herramientas reales).
  - `HEARTBEAT.efd` (Rutina de latido periódico y mantenimiento).
  - Infraestructura host: `working-buffer.md`, `SESSION-STATE.md`, `MEMORY.md`.
* **Propósito:** Operación continua, colaboración diaria con el operador, orquestación de flujos de trabajo e interacción con servicios externos sin degradación de contexto.
* **Caso Canónico:** **Efectral Native v1**.

---

## Nivel 4: Ecosistema Orquestado / Enjambre Modular (Filosofía Kernel Linux)

* **Definición:** Red distribuida de agentes gobernada por un Kernel de Carga Selectiva (`BloqueCargaSelectiva`).
* **Arquitectura:**
  1. Un **Agente Maestro Nivel 3** recibe la demanda del operador y evalúa el plan de acción.
  2. El Maestro no ejecuta todo en su propia ventana de contexto; invoca dinámicamente agentes subordinados **Nivel 1** o **Nivel 2** pasándoles únicamente los parámetros necesarios.
  3. Los agentes subordinados ejecutan su cómputo en paralelo y devuelven datos limpios al bus central.
  4. Una vez concluida la tarea, los subordinados se descargan de la memoria (*lazy unmount*), manteniendo el contexto del Maestro limpio y ligero.
* **Beneficio Industrial:** Resuelve de raíz el problema de saturación de atención (evita el "bloat" de cargar 50 herramientas y 100 páginas de manual en una sola llamada).
