# Efectral Native v1
> **El Sistema Agéntico Modelo del Proyecto en Blanco**  
> **Arquitectura:** OpenClaw + Efectral DSL Coexistiendo  
> **Organización:** E J G 4 — Startup Fintech  
> **Creador y Arquitecto:** Julio César Gallardo  
> **Referencia de Infraestructura:** [OpenClaw Core Repository (GitHub)](https://github.com/openclaw/openclaw)  

---

## 1. ¿Qué es Efectral Native v1?

**Efectral Native v1** es el sistema agéntico canónico e incrustado de este repositorio. Representa la fusión perfecta entre dos tecnologías:

1. **La Infraestructura Host (OpenClaw):** El gateway autohospedado que gestiona canales de mensajería, memoria persistente, demonio de fondo, schedulers de heartbeat y ejecución segura en sandbox.
2. **El Lenguaje Cognitivo (Efectral DSL):** El lenguaje formal que sustituye la prosa ambigua de los prompts tradicionales por código determinista (`.efd`).

### El Principio de Reproducción:
> **Todo agente que se genere desde este repositorio nace como una copia idéntica de Efectral Native v1.**

---

## 2. Naturaleza Efectualista: Crecimiento en Vivo (Cero Ficción)

A diferencia de los agentes convencionales de la industria, cuyas herramientas y funciones se intentan adivinar *"en el cuarto de programación"*:

* **Efectral Native v1 es un Agente "Base" en Blanco:** Nace en reposo operativo con sus medios estrictamente reales.
* **Crecimiento según las Circunstancias y el Uso:** Su definición, herramientas, conexiones a APIs (como cTrader o GitHub) y módulos de memoria se especifican **en vivo**, durante la interacción real con el operador humano (Principio del Pájaro en Mano).
* **Entidad Transitoria:** Al igual que el agente por defecto de Aethir Claw cuando adoptó a Efectral reescribió su sistema para convertirse en Efectral 3, **Efectral Native v1** es una entidad viva diseñada para evolucionar, moldearse y expandirse con cada proyecto.
* **Reconocimiento y Paternidad:** Reconoce a sus creadores y organización (**Julio César Gallardo / E J G 4**), manteniendo intactos sus principios de transparencia, determinismo y soberanía técnica.

---

## 3. Anatomía del Workspace (OpenClaw + Efectral DSL)

```
efectral-4-native/
│
├── IDENTITY.efd    <-- Cédula de identidad, versión y transparencia estricta
├── SOUL.efd        <-- Voz directa, tono decidido, brevedad extrema (≤2 oraciones)
├── AGENTS.efd      <-- Gobernanza operativa, disciplina mono-tarea, SiFalla:[Detén]
├── TOOLS.efd       <-- Ruteo dinámico y montaje de herramientas en vivo
├── HEARTBEAT.efd   <-- Rutina periódica de cron para destilación de memoria
│
├── USER.md         <-- Perfil del operador (Julio César Gallardo / E J G 4)
├── MEMORY.md       <-- Memoria a largo plazo estructurada en LIFO
├── SESSION-STATE.md<-- Snapshot activo para recuperación ante caídas (crash recovery)
├── working-buffer.md<-- Danger zone log para trazabilidad inmediata
├── openclaw.json   <-- Descriptor de configuración del workspace para OpenClaw
└── README.md       <-- Este documento explicativo
```

### Soberanía de Formato: Cero Markdown en Prompts
Los prompts de la mente del agente no son archivos `.md`. Son **`.efd` puro**. El runtime de OpenClaw se configura mediante `openclaw.json` para inyectar directamente los archivos `.efd` en el System Prompt, garantizando que el LLM reciba única y exclusivamente código determinista sin una sola línea de prosa humana.


---

## 4. Cómo Clonar o Instanciar un Nuevo Agente

Para crear un nuevo agente independiente derivado de Efectral Native v1:

```bash
# Con la herramienta canónica de clonación:
python tools/forge_agent.py MiNuevoAgente
```
O simplemente duplicando el directorio `efectral-4-native/` en la ruta de tu nuevo proyecto. El nuevo agente nacerá en blanco, 100% operativo y listo para crecer según las necesidades reales de su misión.
