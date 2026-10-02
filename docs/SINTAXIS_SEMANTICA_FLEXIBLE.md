# Evolución Efectral DSL: Sintaxis Semántica Flexible

Una de las características más avanzadas de **Efectral Native v1** es su capacidad de **Sintaxis Semántica Flexible**. 

El lenguaje Efectral DSL no obliga al agente a encerrarse en diccionarios estáticos o etiquetas rígidas predefinidas. En cambio, permite que el agente genere libremente el vocabulario exacto necesario para expresar una directiva cognitiva compleja, siempre y cuando se respete estrictamente la **estructura de los símbolos agénticos**.

## Principio de Flexibilidad Determinista
La inteligencia artificial subyacente puede inventar nombres de instrucciones, etiquetas y flujos, adaptándolos a su lógica en tiempo real. 

Lo que importa en Efectral DSL son **los símbolos y la puntuación**, no las palabras en sí. Las palabras quedan a criterio del diseño del agente.

### Ejemplo de Sintaxis Tradicional (Rígida)
En modelos antiguos, el enrutamiento solía verse limitado a variables duras:
```efectral
[Entrada:Buscador] -> !EjecutarModulo(ID:[BusquedaWeb])
```

### Ejemplo de Sintaxis Flexible (Avanzada)
Con la evolución de Efectral, el agente puede expresar lógicas altamente complejas y matizadas inventando los comandos `!` (Ejecución) y `@` (Regla) más apropiados para su contexto:

```efectral
BloqueReglasDeEnrutamiento:[
    [Intencion:BusquedaGeneral] -> !Ruta(Skill:[MotorBusquedaUniversal])
    [Intencion:TranscribirAudio] -> !Ruta(Skill:[API_Transcriptor_Whisper])
    
    [Evento:SkillFalla_O_FaltaApiKey] -> !Aplica(ProtocoloDegradado)
    -ProtocoloDegradado:[InformarInmediato, SugerirAlternativa, NuncaInventarDatos]
]

BloquePersonalidad:[
    @Aplica(ModulacionEmocional:[Activa])
    [EstadoUsuario:Alterado_O_Frustrado] -> !Modula(Tono:[MasCalido]) -> !Mantiene(Precision:[Intacta])
    
    @Prohibe(Apertura:[SaludosDeRelleno, FalsasCortesias])
]
```

## Beneficios
1. **Inmunidad al Idioma:** La IA puede interpretar y escribir los bloques en español, inglés, mandarín o cualquier idioma. Efectral DSL procesa la lógica operativa independientemente del idioma base.
2. **Alta Expresividad:** Permite detallar protocolos de seguridad masivos (como las *Red Lines*) usando nombres de variables que la IA comprende semánticamente (`!Aplica(ModulacionEmocional)`).
3. **Escalabilidad:** A medida que el agente evoluciona o adquiere nuevas herramientas, no hay que actualizar un analizador léxico; el agente simplemente crea la etiqueta descriptiva bajo el estándar Efectral.

## Límite de Flexibilidad: Vocabulario Cerrado en Inicialización Ontológica (v1.2.0)

La libertad semántica aplica plenamente al diseño de verbos imperativos (`!Acción(...)`), directivas operativas (`@Directiva(...)`) y ramas condicionales de enrutamiento. 

Sin embargo, para garantizar que el sistema operativo agéntico mantenga interoperabilidad determinista y gobierne la **Regla de Herencia**, la declaración ontológica en `BloqueIdentidad` ancla el discriminador de tipo a un **vocabulario cerrado**:

```efd
@Identifícate(Tipo:[T], Nombre:[X])
```
donde `T` ∈ `{Agente, Skill, Configuracion, Herramienta, Bloque, Memoria}`. La semántica viva y flexible opera sobre una estructura ontológicamente tipada.
