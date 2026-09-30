# Arquitectura de Agentes Efectral Native v1.0: Metodología Efectualista e Ingeniería Inversa
> **Organización:** E J G 4 — Startup Fintech  
> **Arquitecto y Diseñador:** Julio César Gallardo  
> **Evolución:** Ingeniería Inversa sobre Efectral 3 (Aethir Claw)  

---

## 1. Declaración Soberana y Posición de Diseño

> [!IMPORTANT]
> **ESTÁNDAR SOBERANO DE E J G 4:**  
> Esta arquitectura fue concebida y seleccionada estrictamente para responder a las necesidades operativas reales de **E J G 4** ante la incertidumbre presente de los sistemas de IA. Se fundamenta en la **Metodología Efectualista** (Principio del Pájaro en Mano: medios reales, cero ficción).  
> 
> Lo que aquí se establece es tal cual lo que a nosotros como organización nos resuelve el problema en producción. Se publica como contribución de código abierto, pero **no se modifica para complacer requerimientos, modas o marcos burocráticos de terceros**.

---

## 2. La Gran Transición: De la Prosa en Markdown a `.efd` Puro

En los sistemas agénticos de la industria (incluyendo **Efectral 3**, derivado por ingeniería inversa desde la infraestructura de servidores como Aethir Claw), la infraestructura del agente alimenta a la IA con archivos de instrucciones.

En el estándar tradicional de la industria, esos archivos se escribían en **prosa de Markdown**:
* `AGENTS.md` (Reglas y protocolos en texto libre).
* `SOUL.md` (Tono y personalidad redactados como un ensayo).
* `IDENTITY.md` (Ficha descriptiva en párrafos).
* `TOOLS.md` (Instrucciones conversacionales sobre herramientas).
* `HEARTBEAT.md` (Rutinas descritas en viñetas informales).

### El Descubrimiento Crítico de Julio César Gallardo:
> *"El prompt es lo que va directamente a la ventana de contexto de la IA, no el código del runtime. Alimentar a la IA con prosa humana introduce relleno, cortesías no deseadas, ambigüedad probabilística y alto consumo de tokens. La solución es hacer ingeniería inversa a la estructura y sustituir cada archivo de prompt por código determinista en Efectral DSL (`.efd`)."*

```
┌─────────────────────────────────┐           ┌─────────────────────────────────┐
│       EFECTRAL 3 (Markdown)     │           │      Efectral Native v1 (.efd Puro)     │
├─────────────────────────────────┼───────────┼─────────────────────────────────┤
│ AGENTS.md   (Prosa humana)      │    ──►    │ AGENTS.efd   (Directivas @ y !) │
│ SOUL.md     (Ensayo de tono)    │    ──►    │ SOUL.efd     (Fijación de voz)  │
│ IDENTITY.md (Ficha descriptiva) │    ──►    │ IDENTITY.efd (Metadatos duros)  │
│ TOOLS.md    (Rutas en prosa)    │    ──►    │ TOOLS.efd    (Ruteo funcional)  │
│ HEARTBEAT.md(Viñetas sueltas)   │    ──►    │ HEARTBEAT.efd(Rutina ejecutiva) │
└─────────────────────────────────┘           └─────────────────────────────────┘
```

---

## 3. Estructura de este Directorio

* **`guidelines/`**:
  * [`COMPOSICION_AGENTICA_EFECTUAL.md`](guidelines/COMPOSICION_AGENTICA_EFECTUAL.md): Guía normativa completa de cómo interactúan los componentes.
* **`levels/`**:
  * [`TAXONOMIA_NIVELES.md`](levels/TAXONOMIA_NIVELES.md): Clasificación de agentes según 4 niveles de madurez técnica (desde Identidad 0 hasta Enjambre).
* **`templates/`**:
  * Archivos canónicos listos para instanciar en cualquier agente: `IDENTITY.efd`, `SOUL.efd`, `AGENTS.efd`, `TOOLS.efd` y `HEARTBEAT.efd`.
