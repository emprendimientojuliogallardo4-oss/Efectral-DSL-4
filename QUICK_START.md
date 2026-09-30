# Guía de Inicio Rápido: Efectral DSL

Aprende a usar Efectral DSL en **2 minutos**, ya sea pegándolo en una ventana de chat o cargándolo en un servidor agéntico.

## 0. Instalación del Entorno de Desarrollo (1 Solo Comando)

Si clonaste este repositorio, puedes activar el soporte en todos tus editores (VS Code, Cursor, Antigravity IDE) y el comando CLI `efc` ejecutando:

* **En Windows (PowerShell):** `.\install.ps1`
* **En Linux / macOS (Bash):** `./install.sh`
* **Con Python:** `python install.py`

¡Y listo! Tu editor reconocerá los archivos `.efd` con resaltado sintáctico, snippets y validación.

---

## 0.1. Creación de un Nuevo Proyecto Agéntico (Estándar Oficial: Submódulo Fuente)

Para crear un nuevo proyecto o sistema agéntico independiente (como un bot de inversión, un sistema de cTrader o un agente soberano) integrando el motor de Efectral DSL como fuente:

```bash
mkdir MiProyectoAgente
cd MiProyectoAgente
git init
git submodule add https://github.com/emprendimientojuliogallardo4-oss/Efectral-DSL-4.git Efectral-DSL-4
```

### ¿Por qué este es el estándar oficial?
Al tener `Efectral-DSL-4` como submódulo fuente dentro de tu proyecto:
1. **La IA del IDE (Antigravity, Cursor, Copilot) detecta inmediatamente la especificación**, la gramática y las reglas de forja (`.agents/rules/`) dentro de tu propio espacio de trabajo.
2. **Cero alucinaciones:** La IA no inventará sintaxis en otros lenguajes; seguirá el estándar `.efd` formalmente.
3. **El proyecto es 100% autocontenido y portable:** cualquier desarrollador o servidor que clone tu proyecto tiene el compilador (`efc`) y el validador listo para operar.

---

## 1. Uso Directo en Chat (ChatGPT, Claude, DeepSeek)

Para convertir inmediatamente cualquier modelo en un agente determinista de Efectral, copia y pega el siguiente bloque en la primera línea de tu conversación:

```efd
# ================================================================
# ACTIVACIÓN DETERMINISTA EN CHAT
# ================================================================

BloqueIdentidad:[
    @Identifícate(Agente:[AsistenteDeterminista])
    -Proyecto:[E J G 4]
    -Objetivo:[MaximaPrecision-SinRelleno]
]

BloqueReglas:[
    @Aplica(Hiperparametros:[Temperatura:0.2 - TopP:0.0])
    @Fija(Skin:[Directo]) Intro:[No] Saludo:[No] Relleno:[No] MaximoOraciones:[2]
    @Prohíbe(Exposicion:[Razonamiento]) SoloResultado:[Si]
]

BloqueEjecucion:[
    !EsperaInstrucciones
]
```

### Qué notarás inmediatamente:
* El modelo dejará de saludarte con preámbulos tipo *"¡Hola! Con mucho gusto te ayudo con..."*.
* Tus respuestas serán directas, precisas y de máximo 2 oraciones, entregando solo la solución técnica.

---

## 2. Uso en Servidores y Sistemas Agénticos (OpenClaw / Aethir Claw)

1. En el directorio raíz de tu agente, crea tu archivo `IDENTITY.efd` y tu `CORE_RULES.efd`.
2. En tu archivo de inicialización (`BOOTSTRAP.efd`), define el orden de carga:
   ```efd
   BloqueBootstrap:[
       1) !Aplica(CargaModulos:[IDENTITY.efd, CORE_RULES.efd, TOOLS.efd])
       2) !Emite(Estado:[AgenteListo])
       3) !EsperaInstrucciones
   ]
   ```
3. Ejecuta tu runtime. El agente leerá los bloques de reglas antes de atender cualquier petición del usuario.

---

## 3. Las 3 Reglas de Oro para Escribir en Efectral DSL

1. **Todo valor lleva corchetes:** `Version:[1.0.0]`, nunca `Version: 1.0.0`.
2. **Las reglas de sistema llevan `@`:** `@Aplica(Regla:[Determinismo])`.
3. **Las órdenes activas llevan `!`:** `!Verifica(...)` o `!Ejecuta(...)`.
