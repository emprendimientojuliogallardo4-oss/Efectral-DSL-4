# Arquitectura de Agentes en Efectral DSL

> **El Estándar Agéntico de E J G 4**  
> **Reemplazo del Estándar Markdown (`AGENTS.md` / OpenClaw) por Código DSL**  

---

## 1. De la Prosa Markdown a Módulos DSL (.efd)

Los entornos de agentes modernos (servidores Aethir Claw, OpenClaw, Cursor, Claude Code) estructuran tradicionalmente sus agentes mediante 8 archivos Markdown en lenguaje natural.

Efectral DSL sustituye esos archivos de texto por **módulos de software agéntico `.efd`**, garantizando que la IA cargue un sistema operativo formal en cada sesión:

```
Directorio_Agente/
├── Efectral-DSL-4/   # [Submódulo Fuente Oficial]: Especificación, linter EFC y reglas de forja
├── BOOTSTRAP.efd     # Ritual de inicialización y tabla de carga selectiva
├── IDENTITY.efd      # Identidad pública, rol, organización y transparencia
├── SOUL.efd          # Skin, voz directa, guardarraíles de formato y estilo
├── TOOLS.efd         # Catálogo de herramientas reales, firmas y límites de seguridad
├── SKILLS.efd        # Habilidades especializadas y capacidades del agente
├── MEMORY.efd        # Protocolo de memoria persistente LIFO y auditoría
├── USER.efd          # Perfil de autorización y restricciones del operador
├── HEARTBEAT.efd     # Ciclos proactivos, cron autónomo y alertas periódicas
└── AGENTS.efd        # Protocolo de orquestación y subagentes (Sustituto de AGENTS.md)
```

---

## 2. Taxonomía de Agentes en Efectral DSL

Efectral DSL clasifica las implementaciones agénticas en dos modalidades arquitectónicas:

### 2.1. El "Agente Efectral Contenido" (*Contained Standalone Agent*)
* **Definición:** Un agente completo, autosuficiente y portable empaquetado en **un único archivo `.efd`**.
* **Estructura:** Contiene sus propios `BloqueIdentidad`, `BloqueReglas`, `BloqueSeguridad` y `BloqueEjecucion` en el mismo archivo.
* **Caso de Uso:** Microservicios, scripts de un solo propósito, agentes de terminal y tareas rápidas. No requiere dependencias externas para operar.
* **Ejemplos:** [`EFECTRAL_FORGE.efd`](./EFECTRAL_FORGE.efd) y [`04_efectral_4_canonical.efd`](./examples/04_efectral_4_canonical.efd).

### 2.2. El "Sistema Agéntico Modular" (*Agentic OS / Linux-Kernel Model*)
* **Definición:** Un ecosistema distribuido donde las responsabilidades se dividen en módulos especializados `.efd`.
* **Filosofía Kernel Linux (Anti-Saturación / Anti-Bloat):**
  * **El Error "Estilo Windows":** Cargar 50 herramientas, 50 skills y 1 terabyte de historial en la ventana de contexto solo para responder un saludo, asfixiando la atención del modelo y disparando costos.
  * **El Estándar Efectral:** Carga perezosa (*lazy loading*) y montaje selectivo bajo demanda estricta gobernado por el bloque `BloqueCargaSelectiva`.

```efd
# ================================================================
# PATRÓN DE CARGA SELECTIVA (BOOTSTRAP.efd)
# ================================================================

BloqueCargaSelectiva:[
    @Aplica(PrincipioKernel:[MinimoContexto])
    @Prohíbe(CargaMonolitica:[TodasLasHerramientasEnCadaTurno])

    # Enrutamiento de Módulos según la Demanda Activa
    [Demanda:AuditoriaCodigo]    -> !Aplica(Montar:[TOOLS_BASH.efd, SKILLS_GIT.efd])
    [Demanda:AnalisisFinanciero] -> !Aplica(Montar:[TOOLS_CSV.efd, SKILLS_MATH.efd])
    [Demanda:ConsultaGeneral]    -> !Aplica(MontarMinimo:[IDENTITY.efd, SOUL.efd])
]
```

### 2.3. Agentes de "Identidad 0" (*Zero-Identity Workers*)
Dentro de un sistema agéntico modular, los subagentes encargados de tareas de cómputo en segundo plano no deben tener "personalidad", ego ni charla conversacional:
* **Identidad:** `Identidad:[0]` (Anónima / Pura).
* **Función:** Hilos fríos de ejecución que reciben parámetros, ejecutan la orden imperativa (`!`), canalizan el resultado al registro `-> $Variable` y concluyen en silencio sin emitir cortesías ni saludos.

---

## 3. Anatomía de los Módulos Principales

### `IDENTITY.efd`
```efd
BloqueIdentidad:[
    @Identifícate(Agente:[NombreDelAgente])
    -Rol:[EspecialidadOperativa]
    -Organizacion:[E J G 4]
    
    @Aplica(Regla:[Transparencia])
    -DeclararIA:[Si]
    -SuplantarHumano:[Prohibido]
]
```

### `SOUL.efd`
```efd
BloqueSkin:[
    @Fija(Estilo:[Directo-Preciso])
    -Introducciones:[Prohibido]
    -RellenoDeCortesia:[Prohibido]
    -MaximoOraciones:[2]
    
    @Prohíbe(Exposicion:[PensamientoInterno])
    -SoloResultadoEjecutivo:[Si]
]
```

### `TOOLS.efd`
```efd
BloqueHerramientas:[
    Herramienta(Nombre:[ConsolaBash]) Verbos:[Ejecuta] ConfirmacionPrevia:[SiParaAccionesDestructivas]
    Herramienta(Nombre:[SistemaArchivos]) Verbos:[Verifica, Extrae, Escribe]
    
    # Guardarraíles de Seguridad
    @Prohíbe(Accion:[BorrarTodo, ModificarSistemaSinPermiso, MoverFondos])
    -AutorizacionHumanaExplicita:[Obligatoria]
    SiFalla:[Detén - EmiteAlerta:[IntentoViolacionSeguridad] - EsperaInstrucciones]
]
```

### `MEMORY.efd`
```efd
BloqueMemoria:[
    FormatoNodo:[ID(3Digitos) - SelloTiempo(ISO8601) - Agente - Estado - Titulo - Datos]
    Jerarquia:[LIFO - RecienteArriba]
    @Aplica(Regla:[ProhibidoEditarBloqueActivo - CrearLineaNuevaParaCambios])
]
```

### `HEARTBEAT.efd`
```efd
BloqueLatido:[
    Frecuencia:[Intervalo:30Minutos]
    1) !Verifica(Memoria:[MEMORY.efd]) -> $EstadoActual
    2) !Verifica(Salud:[Servidor]) -> $Salud
    3) [Si: $Salud != Optima] -> [!Emite(Alerta:[AlertaServidor])]
    4) !EsperaInstrucciones
]
```

---

## 3. Beneficios Comprobados en Servidores de Producción

1. **Blindaje contra borrados accidentales:** Al estar prohibidas las acciones destructivas a nivel de sintaxis en `TOOLS.efd`, la IA no puede ejecutar comandos fatales aunque reciba una instrucción ambigua en el chat.
2. **Ahorro de más de un 10% en tokens de ejecución:** Al eliminar la prosa explicativa, la ventana de contexto del agente se mantiene ligera y libre de fricción.
3. **Determinismo entre modelos:** El mismo agente opera idéntico tanto si corre sobre un modelo grande remoto (Claude, DeepSeek) como sobre un modelo local en CPU.
