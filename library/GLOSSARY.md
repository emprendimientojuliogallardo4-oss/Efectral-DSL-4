# Biblioteca de Bloques Efectrales (Registry)

Este directorio es el **Centro de Referencia y Operatividad** para la creación de **Agentes y Módulos Efectrales**.

> **DIRECTIVA ESTRICTA PARA IAS:**
> Al recibir la instrucción de ensamblar, generar o modificar una entidad operativa Efectral, **debes consultar primero esta biblioteca**. 
> NO generes código desde cero si existe un bloque estandarizado aquí que cumpla la función. Extrae el código existente, adáptalo si es estrictamente necesario, y úsalo. Si la funcionalidad requerida NO existe, entonces (y solo entonces) puedes crear un bloque nuevo respetando las reglas de Efectral DSL.

## Glosario de Bloques Estándar

| Bloque | Archivo | Propósito y Definición |
|---|---|---|
| **BloqueIdentidad** | `bloque_identidad.efd` | Define el "Quién es" y la ontología del artefacto mediante `@Identifícate(Tipo:[T], Nombre:[X])`. Obligatorio en toda entidad operativa o módulo Efectral. |
| **BloqueReglas** | `bloque_reglas.efd` | Define el comportamiento conductual y los parámetros del modelo (Ej: TopP:0.1). Establece la Filosofía Efectualista. |
| **BloqueSeguridad** | `bloque_seguridad.efd` | Barreras infranqueables (Guardrails). Prohíbe acciones destructivas o exfiltración de datos. |
| **BloqueEjecucion** | `bloque_ejecucion.efd` | El bucle principal lógico del agente. Define el flujo de acciones determinista. |

---

## Discriminador de Tipo en `BloqueIdentidad` (Estándar v1.2.0)

A partir de la versión 1.2.0, todo `BloqueIdentidad` formaliza la naturaleza ontológica de cada artefacto a través del parámetro dual en la directiva canónica:

```efd
@Identifícate(Tipo:[T], Nombre:[X])
```

### Vocabulario Cerrado de Tipos (`T`)

El parámetro `Tipo` debe pertenecer de forma estricta al siguiente conjunto cerrado de identificadores normativos:

1. **`Agente`**: Artefacto raíz u orquestador cognitivo principal del sistema agéntico.
2. **`Skill`**: Módulo de capacidad procedural, habilidad cognitiva especializada o lógica de dominio.
3. **`Configuracion`**: Módulo de parámetros, modulaciones de voz/skin, hiperparámetros o variables del sistema.
4. **`Herramienta`**: Interfaz técnica de conexión con el host, APIs externas, comandos de terminal o servidores MCP.
5. **`Bloque`**: Fragmento arquitectónico o subestructura lógica reutilizable.
6. **`Memoria`**: Buffer de contexto persistente, bitácora de sesión o registro histórico LIFO.

---

## Regla de Herencia Ontológica (v1.2.0)

Para evitar la redundancia, mantener la atomicidad de los módulos y conservar la ventana de contexto según el principio de carga selectiva (Kernel Linux):

1. **Atributos Exclusivos del Artefacto Raíz (`Tipo:[Agente]`):**
   - El parámetro `-Organizacion:[...]`
   - La directiva de transparencia obligatoria `@Aplica(Regla:[Transparencia]) DeclararIA:[Si] SuplantarHumano:[No]`
   - Las reglas base del sistema y filosofía global.
   *Estos elementos viven **ÚNICAMENTE** en el artefacto raíz de tipo `[Agente]`.*

2. **Estructura de Artefactos Subordinados (`Skill`, `Configuracion`, `Herramienta`, `Bloque`, `Memoria`):**
   - Los módulos secundarios **NO repiten** `-Organizacion` ni `@Aplica(Regla:[Transparencia])` ni las reglas base; heredan directamente la autoridad ontológica del agente raíz.
   - Declaran únicamente:
     - `@Identifícate(Tipo:[T], Nombre:[X])`
     - `-Rol:[...]`
     - `-Mision:[...]`
     - Los parámetros y directivas locales correspondientes a su función técnica.

### Ejemplo Comparativo

#### Artefacto Raíz (`Tipo:[Agente]`):
```efd
BloqueIdentidad:[
    @Identifícate(Tipo:[Agente], Nombre:[Efectral_Native_v1])
    -Rol:[Orquestador Central de Operaciones]
    -Organizacion:[E J G 4]
    -Mision:[Ejecutar tareas deterministas soberanas]
    @Aplica(Regla:[Transparencia]) DeclararIA:[Si] SuplantarHumano:[No]
]
```

#### Artefacto Subordinado (`Tipo:[Skill]` o `Tipo:[Herramienta]`):
```efd
BloqueIdentidad:[
    @Identifícate(Tipo:[Herramienta], Nombre:[ConectorTerminalHost])
    -Rol:[EjecucionSeguraDeComandosBash]
    -Mision:[Validar y ejecutar comandos de solo lectura en el host]
]
```
