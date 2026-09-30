# Efectral DSL — ESPECIFICACIÓN NORMATIVA Y PROTOCOLO APL
> **Organización:** E J G 4 — Startup Fintech  
> **Autor y Arquitecto:** Julio César Gallardo  
> **Versión Normativa:** 1.0.0 — Edición Soberana  
> **Estado:** Estándar Oficial en Producción  

---

## 0. Manifiesto Soberano y Principio Efectualista Fundacional

> [!IMPORTANT]
> **DECLARACIÓN SOBERANA DE DISEÑO Y LÍMITES:**  
> Esta especificación, su sintaxis y su arquitectura fueron concebidas y estructuradas por y para el propio proyecto **E J G 4**. Sus límites actuales están rigurosamente sesgados a la incertidumbre presente, como todo sistema construido bajo la **Metodología Efectualista** (Principio del Pájaro en Mano y Pérdida Asequible).  
> 
> Lo que aquí se presenta es tal cual lo que a nosotros, como organización fintech y de investigación agéntica, nos resuelve el problema operativo en la práctica real. **Punto y fin.**  
> 
> Efectral DSL se publica bajo código abierto para la comunidad mundial, pero **no** se somete ni pretende complacer requerimientos cosméticos, burocráticos o marcos conceptuales de terceros. Si a tu organización le es útil, tómalo y ejecútalo; si necesitas adaptarlo a tu propio contexto, forja tus propios módulos.

---

## 1. Naturaleza Ontológica: ¿Qué es y qué NO es Efectral DSL?

### 1.1. Lo que ES:
1. **Un Lenguaje de Programación Agéntica (APL):** Es una Arquitectura de Conjunto de Instrucciones (ISA) diseñada para gobernar unidades de cómputo neuronal (LLMs) de forma matemática, rígida y determinista.
2. **El Compilador de Prompts del Agente:** Efectral DSL reemplaza la prosa informal en los prompts del agente. Todo archivo `.efd` es una matriz de directivas (`@`), acciones ejecutivas (`!`), variables (`$`), tuberías de datos (`->`) y cortocircuitos (`SiFalla`).
3. **Una Fuente Universal Citada Remotamente o en Local:** Puede ser leída e interpretada en tiempo real por cualquier IA conectada a la web o mediante submódulo embebido.

### 1.2. Lo que NO es:
1. **NO es el agente completo:** Efectral DSL no construye la infraestructura del sistema operativo ni los demonios de red. Efectral DSL **escribe los prompts** de la mente del agente (`AGENTS.efd`, `SOUL.efd`, `IDENTITY.efd`, `TOOLS.efd`, `HEARTBEAT.efd`).
2. **NO es un framework pesado en Python:** No compite con runtime hosts como LangChain o CrewAI ni busca crear wrappers de código. La IA misma es el motor de parseo e inferencia.

---

## 2. Modalidades Operativas de Uso del Repositorio

El repositorio está diseñado para operar bajo 4 modalidades precisas según la finalidad del operador o de la IA:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   MODALIDADES DE USO DE Efectral DSL                   │
├────────────────────────────────┬────────────────────────────────────────────┤
│ Modalidad                      │ Mecanismo de Aplicación                   │
├────────────────────────────────┼────────────────────────────────────────────┤
│ 1. Consulta Remota por IA      │ La IA cita el repositorio público vía web  │
│    (Sin descargas)             │ y asimila la gramática al instante.        │
├────────────────────────────────┼────────────────────────────────────────────┤
│ 2. Submódulo de Proyecto       │ Se clona/copia la carpeta `submodule/`     │
│    (Librería Portable)         │ dentro del repositorio de agentes host.    │
├────────────────────────────────┼────────────────────────────────────────────┤
│ 3. Soporte de Entorno IDE      │ Instalación en VS Code, Cursor, Windsurf o │
│    (Desarrollo y Sintaxis)     │ Antigravity mediante `ide-extension/`.     │
├────────────────────────────────┼────────────────────────────────────────────┤
│ 4. Arquitectura de Agente      │ Se implementa la anatomía por niveles      │
│    (Ingeniería Inversa .efd)   │ sustituyendo Markdown por archivos `.efd`. │
└────────────────────────────────┴────────────────────────────────────────────┘
```

---

## 3. Especificación de Archivos y Formato

1. **Extensión Oficial:** `.efd` (*Efectral Formal Definition* / *Efectral DSL File*).
2. **Codificación:** Obligatoriamente `UTF-8` estricto sin BOM. Saltos de línea canónicos `LF` (`\n`).
3. **Identificador Markdown:** En bloques de código markdown, el identificador formal es ````efd`.

---

## 4. Gramática y Morfología Sintáctica

### 4.1. Primitivas de Delimitación:
* **Parámetros y Claves:** Todo valor o lista debe estar rigurosamente delimitado entre corchetes: `Clave:[Valor]`.
* **Directivas de Sistema (`@`):** Comandos estructurales de alto nivel:
  - `@Identifícate`: Declara rol, versión y naturaleza ontológica.
  - `@Aplica`: Impone un estándar o política normativa.
  - `@Fija`: Establece variables de entorno cognitivo (temperatura, modo, brevedad).
  - `@Prohíbe`: Barreras infranqueables (anillos de seguridad / kernel ring 0).
  - `@Exige`: Precondiciones de datos obligatorias.

* **Acciones Ejecutivas (`!`):** Operaciones atómicas de inferencia o interacción:
  - `!Verifica`, `!Extrae`, `!Evalúa`, `!Calcula`, `!Escribe`, `!Ejecuta`, `!Emite`, `!EsperaInstrucciones`.
  - La semántica del verbo es viva (comprensión profunda del LLM), pero su morfología es rígida (`!Acción`).

* **Flujo de Datos y Registros (`->`):**
  - El paso de información entre instrucciones se realiza canalizando la salida a registros léxicos:
    `!Extrae(Dato:[Precio]) -> $PrecioActual`

* **Manejo Determinista de Fallas (`SiFalla`):**
  - Toda acción crítica debe contener su cortocircuito:
    `SiFalla:[Detén - EmiteAlerta:[Fallo en Datos] - EsperaInstrucciones]`

---

## 5. Arquitectura de Bloques Canónicos

Todo archivo `.efd` se compone de 4 bloques elementales:

```efd
# ====================================================================
# AGENTE EFECTRAL CANÓNICO — ESTRUCTURA ESTÁNDAR 4.0
# ====================================================================

BloqueIdentidad:[
  @Identifícate(Nombre:[Agente_Ejemplo] - Version:[1.0.0])
  @Fija(Voz:[Directa] - Brevedad:[Extrema] - Prosa:[Prohibida])
]

BloqueReglas:[
  @Prohíbe(Alucinación:[DatosNoVerificados] - Cortesías:[CeroProsa])
  @Exige(Entrada:[UTF-8_Valido])
]

BloqueEjecucion:[
  1) !Verifica(Condicion:[DatosPresentes]) -> SiFalla:[Detén - EsperaInstrucciones]
  2) !Procesa(Entrada:[$Datos]) -> $Resultado
  3) !Emite(Salida:[$Resultado])
]

BloqueSeguridad:[
  @Prohíbe(Exfiltración:[DatosSensibles])
  @Aplica(Protocolo:[ParadaInmediata])
]
```

---

## 6. La Ley de la Metodología Efectualista: El Agente Funcional en Blanco

1. **Cero Herramientas Ficticias:** Queda terminantemente prohibido asumir o inventar dependencias, APIs o servidores inexistentes.
2. **Definición en el Uso (Pájaro en Mano):** El agente nace en reposo operativo con sus medios estrictamente reales. Solo adquiere herramientas o capacidades cuando el operador humano o el entorno las suministra físicamente.
