# Guía Canónica de Composición Agéntica Efectual
> **Organización:** E J G 4 — Startup Fintech  
> **Estándar:** Efectral Native v1.0.0  

Esta guía establece el protocolo operativo para construir agentes de software deterministas, aplicando ingeniería inversa a los frameworks de agentes existentes para erradicar la prosa informal en la ventana de contexto.

---

## 1. La Separación Arquitectónica de Responsabilidades

Un agente de software moderno consta de dos capas claramente delimitadas:

1. **La Capa de Infraestructura (El Runtime del Host):**
   - Ejecutada en el sistema operativo (Python, Node.js, C#, Aethir Claw, shell scripts).
   - Administra el sistema de archivos, los sockets de red, los puertos de APIs (ej. cTrader, GitHub) y los demonios de cron.
   - Su trabajo es leer los archivos de definición del agente e inyectarlos a la API de inferencia neuronal.

2. **La Capa Cognitiva (Los Prompts del Agente):**
   - Es el texto que efectivamente ingresa a la ventana de contexto de la IA.
   - En sistemas tradicionales, se llena de prosa conversacional (`.md`), lo que degrada el determinismo.
   - **En Efectral Native v1, se compone exclusivamente de archivos `.efd`**, convirtiendo los prompts en código de instrucciones de máquina semántica (APL).

---

## 2. Anatomía de los Archivos de Prompt en `.efd`

```
Directorios del Agente /
│
├── IDENTITY.efd    <-- ¿Quién soy? (Metadatos, rol formal, reglas de transparencia)
├── SOUL.efd        <-- ¿Cómo hablo? (Voz directa, brevedad extrema, cero relleno)
├── AGENTS.efd      <-- ¿Cómo opero? (Pipeline de procesamiento, memoria, seguridad)
├── TOOLS.efd       <-- ¿Qué uso? (Catálogo formal de herramientas y precondiciones)
└── HEARTBEAT.efd   <-- ¿Qué hago periódicamente? (Mantenimiento, depuración de memoria)
```

### 2.1. `IDENTITY.efd` (Cédula de Identidad)
Reemplaza la ficha descriptiva en prosa por una declaración estructurada:
- Nombre formal y alias.
- Versión operativa y organización a la que sirve.
- Política de transparencia estricta: Declarar siempre condición de IA; nunca suplantar identidad humana.

### 2.2. `SOUL.efd` (Personalidad y Límites)
Reemplaza los párrafos de "psicología del agente" por directivas duras:
- `@Fija(Voz:[Directa] - Intro:[Prohibida] - Saludo:[Prohibido] - MaximoOraciones:[2])`.
- `@Prohíbe(Relleno:[MenúsDeOpcionesNoPedidas] - Alucinación:[PreciosNoVerificados])`.
- Principio: **Brevedad es Respeto**. El valor radica en el resultado, no en la cortesía.

### 2.3. `AGENTS.efd` (Gobernanza y Pipeline Operativo)
Define el algoritmo neuronal paso a paso:
1. **Pipeline de Trabajo:**
   `Entrada -> VerificaciónFuente -> BúsquedaMemoria -> Procesamiento -> ValidaciónSalida -> Salida`.
2. **Mono-tarea Estricta:** Un solo trabajo por sección. Si el usuario cambia de contexto o genera ambigüedad: detener la ejecución, señalar la discrepancia y esperar instrucciones explícitas.
3. **Manejo de Fallas:** Todo error activa cortocircuito:
   `SiFalla:[Detén - EmiteAlerta - EsperaInstrucciones]`.

### 2.4. `TOOLS.efd` (Ruteo Funcional)
Catálogo de capacidades reales conectadas en la máquina. Prohíbe invocar funciones sin preverificación física en el host.

### 2.5. `HEARTBEAT.efd` (Rutina de Latido)
Instrucciones ejecutivas que el cron del host dispara periódicamente para depuración de memoria y comprobación de estado.

---

## 3. Protocolo de Memoria Persistente y Resiliencia ante Caídas

La persistencia del agente opera bajo una jerarquía de tres niveles gestionada por el runtime:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          JERARQUÍA DE MEMORIA EFECTUAL                      │
├───────────┬──────────────────────────────┬──────────────────────────────────┤
│ Nivel     │ Ubicación                    │ Función                          │
├───────────┼──────────────────────────────┼──────────────────────────────────┤
│ 1. HOT    │ Registros léxicos ($Var)     │ Memoria de trabajo en la sesión  │
│           │ y `working-buffer.md`        │ activa; registra cada decisión.  │
├───────────┼──────────────────────────────┼──────────────────────────────────┤
│ 2. WARM   │ `MEMORY.md` y                │ Hechos estables, preferencias    │
│           │ `SESSION-STATE.md`           │ consolidadas y snapshot de crash │
├───────────┼──────────────────────────────┼──────────────────────────────────┤
│ 3. COLD   │ `memory/YYYY-MM-DD.md`       │ Archivo histórico comprimido y   │
│           │                              │ registros de auditoría.          │
└───────────┴──────────────────────────────┴──────────────────────────────────┘
```

* **Blindaje ante Caídas (`working-buffer.md`):** Cada vez que el operador toma una decisión clave o se ejecuta una orden, el runtime registra una línea temporal. Si la sesión se interrumpe, el agente recupera el hilo exacto leyendo el buffer antes de responder.
