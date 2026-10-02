# Especificación Formal de Efectral DSL

> **Versión Normativa:** 1.2.0 (Edición Estándar)  
> **Estado:** Aprobado / Cerrado  
> **Autoría:** E J G 4 — Julio César Gallardo  

---

## 0. Especificación de Archivos y Formato

Para garantizar la interoperabilidad, portabilidad y ejecución libre de ambigüedades entre distintos entornos y modelos, todo código fuente de Efectral DSL se rige por los siguientes estándares de archivo:

* **Extensión Canónica de Archivo:** `.efd` (*Efectral Formal Definition* / *Efectral DSL File*). Todo archivo fuente modular o programa autónomo debe utilizar exclusivamente esta extensión.
* **Codificación de Caracteres:** `UTF-8` estricta sin BOM. Obligatoria para la representación exacta de diacríticos y caracteres normativos del idioma español (`Á-Ú`, `á-ú`, `Ñ`, `ñ`).
* **Identificador de Bloque de Código (*Syntax Highlighting Tag*):** `efd`. En documentos Markdown, editores de código y plataformas web, los bloques deben delimitarse como ````efd ... ````.
* **Tipo MIME Recomendado:** `text/vnd.efectral` (alternativa estándar: `text/plain; charset=utf-8`).
* **Organización Modular:** Los archivos `.efd` deben ser atómicos, cohesivos e independientes, permitiendo su precarga e inclusión mediante directivas operativas (`!Aplica(CargaModulos:[...])`).

---

## 1. Léxico y Símbolos del Lenguaje

Efectral DSL se rige por un conjunto cerrado de símbolos delimitadores y operadores:

| Símbolo | Denominación | Regla Semántica |
| :---: | :--- | :--- |
| `:` | Dos puntos | **Asignación / Parámetro**: Vincula un identificador con su valor (`Clave:[Valor]`). |
| `[` `]` | Corchetes | **Delimitador Universal**: Todo dato, referencia, lista o estado debe estar envuelto en corchetes. |
| `(` `)` | Paréntesis | **Argumentos de Verbo**: Delimita los objetos directos de una acción (`Verifica(Archivo:[X])`). |
| `->` | Tubería | **Flujo Secuencial**: Transfiere el resultado de una instrucción al siguiente paso o variable. |
| `$` | Dólar | **Variable de Contexto**: Almacén léxico que transporta datos entre instrucciones (`$Datos`). |
| `-` | Guión | **Conector**: Elemento de lista en nueva línea; operador de secuencia entre `[A]-[B]`. |
| `,` | Coma | **Separador Posicional**: Separa argumentos dentro de paréntesis o listas de parámetros. |
| `"` `"` | Comillas | **Texto Literal Extenso**: Delimita cadenas de lenguaje natural descriptivas. |
| `#` | Numeral | **Encabezado / Comentario**: Marcador de bloque de metadatos o comentario estructural. |
| `@` | Arroba | **Prefijo de Directiva / Regla Dura**: Instrucción de sistema inviolable (`@Regla:[...]`). |
| `!` | Admiración | **Prefijo de Acción Imperativa**: Orden ejecutiva que la IA debe ejecutar activamente (`!Ejecuta(...)`). |

---

## 2. Tipos de Datos y Valores

Todo valor contenido en `[ ]` debe corresponder a una de las siguientes categorías tipadas:

1. **Identificador / Símbolo:** Formato `PascalCase` sin espacios (`[Efectral]`, `[Produccion]`).
2. **Numérico:** Enteros o decimales (`[0.2]`, `[100]`, `[1.0.0]`).
3. **Booleano:** Representado formalmente por `[Si]` o `[No]`.
4. **Secuencia Conectada:** Pasos concatenados por guiones (`[Entrada]-[Proceso]-[Salida]`).
5. **Parámetro Compuesto:** Propiedades agrupadas (`[PrecisionTecnica-AlucinacionMinima]`).
6. **Literal de Texto:** Texto delimitado por comillas dentro o fuera de corchetes (`Contx:"Cadena"`).

---

## 3. Morfología Operativa: Acciones Imperativas (`!`) y Directivas (`@`)

Efectral DSL no limita artificialmente el léxico a un diccionario cerrado mecánico. Como lenguaje diseñado específicamente para **procesadores neuronales (LLMs)**, el poder determinista de Efectral reside en su **morfología y delimitación estructural**, aprovechando la comprensión semántica profunda de la IA:

* **El Prefijo Imperativo `!` (Acción Ejecutiva Inmediata):** Cualquier verbo o identificador precedido por `!` indica una orden activa que la IA debe ejecutar (`!Verifica`, `!Revisa`, `!Comprueba`, `!Audita`, `!Extrae`, `!Obtén`, `!Escribe`, `!Ejecuta`, `!Emite`, `!EsperaInstrucciones`).
* **El Prefijo de Directiva `@` (Regla Dura Inviolable):** Cualquier verbo o identificador precedido por `@` establece una ley de sistema o restricción permanente de comportamiento (`@Identifícate`, `@Aplica`, `@Fija`, `@Prohíbe`, `@Exige`, `@Restringe`, `@Garantiza`).

### 3.1. Núcleo Canónico de Referencia (Estándar Recomendado)
Para maximizar la interoperabilidad entre agentes y herramientas, se establece el siguiente núcleo canónico de referencia:
* `@Identifícate(Tipo:[T], Nombre:[...])`: Fija la ontología y naturaleza del artefacto (con `T` perteneciente al vocabulario cerrado `{Agente, Skill, Configuracion, Herramienta, Bloque, Memoria}`), su identificador unívoco, rol y misión.
* `@Aplica(Regla:[...])`: Carga hiperparámetros, restricciones o directivas operativas.
* `@Fija(Skin:[...])`: Configura el estilo de salida, límite de oraciones y tono.
* `@Prohíbe(Accion:[...])`: Bloquea acciones de riesgo (borrado de datos, movimientos de fondos).
* `!Verifica(Recurso:[...])`: Comprueba existencia e integridad de archivos o servicios (sinónimos semánticos válidos: `!Revisa`, `!Comprueba`, `!Inspecciona`).
* `!Extrae(Fuente:[...])`: Recupera datos o campos específicos de un archivo o API (sinónimos semánticos válidos: `!Obtén`, `!Lee`).
* `!Escribe(Destino:[...])`: Almacena información o genera código en disco o memoria.
* `!Ejecuta(Herramienta:[...])`: Invoca una función externa, comando de terminal o subproceso.
* `!Emite(Resultado:[...])`: Entrega la respuesta final formateada.
* `!EsperaInstrucciones`: Finaliza el turno del agente y cede el control al operador.

### 3.2. Modo Infinitivo (Declaración Diferida / Rutina / Capacidad)
`Identificar()`, `Aplicar()`, `Fijar()`, `Verificar()`, `Extraer()`, `Escribir()`, `Ejecutar()`, `Emitir()`, `Prohibir()`, `Esperar()`.
Se emplean para catalogar herramientas o rutinas en bibliotecas de capacidades.

---

## 4. Estructuras de Control y Guardarraíles

### 4.1. Tuberías de Datos (`->` y `$`)
Garantiza que la información fluya directamente sin depender de la memoria probabilística del modelo:
```efd
1) !Extrae(Archivo:[Config.efd]) Campos:[Host, Puerto] -> $Conexion
2) !Ejecuta(Conectar:$Conexion)
```

### 4.2. Contratos de Salida Explícita (`ContratoSalida:[...]`)
Fuerza a la IA a colapsar la respuesta en un esquema verificable:
```efd
!Emite(Reporte:[Auditoria]) ContratoSalida:[Tipo:DSL - MaxLineas:2 - Delimitadores:Obligatorios]
```

### 4.3. Cortocircuito y Control de Excepciones (`SiFalla:[...]`)
Ruta de salida obligatoria ante fallas, evitando que la IA intente improvisar o alucinar:
```efd
!Verifica(Archivo:[Claves.efd]) SiFalla:[Detén - EmiteAlerta:[ArchivoCriticoFaltante] - EsperaInstrucciones]
```

### 4.4. Bifurcación Condicional y Coincidencia de Patrones (`[Patrón] -> !Acción`)
Efectral DSL estandariza la evaluación de estados y el enrutamiento de tareas mediante el operador de bifurcación condicional:
```efd
[Demanda:AuditoriaCodigo]    -> !Aplica(Montar:[TOOLS_BASH.efd, SKILLS_GIT.efd])
[Demanda:AnalisisFinanciero] -> !Aplica(Montar:[TOOLS_CSV.efd, SKILLS_MATH.efd])
[Demanda:ConsultaGeneral]    -> !Aplica(MontarMinimo:[IDENTITY.efd, SOUL.efd])
[Si: $Saldo < 0]             -> !Emite(Alerta:[SaldoNegativo])
```
Garantiza que la IA adopte de forma determinista la rama correspondiente a la intención activa sin recurrir a divagaciones condicionales en prosa.

### 4.5. Componentes Primitivos del Sistema Operativo Agéntico
Los bloques en Efectral DSL no son etiquetas textuales arbitrarias; representan **componentes arquitectónicos de primera clase** formalizados por la norma:
1. `BloqueIdentidad:[...]`: Raíz ontológica y discriminador de tipo (`@Identifícate(Tipo:[T], Nombre:[...])`), rol y misión. En el artefacto raíz de tipo `[Agente]`, define organización y directiva de transparencia. En componentes subordinados (`Skill`, `Configuracion`, `Herramienta`, `Bloque`, `Memoria`), rige la Regla de Herencia omitiendo redundancias.
2. `BloqueReglas:[...]`: Hiperparámetros de inferencia, skin, restricciones y directivas permanentes `@`.
3. `BloqueSeguridad:[...]`: Anillo de protección dura, listas de prohibición y cortocircuitos `SiFalla`.
4. `BloqueCargaSelectiva:[...]`: Despachador de recursos estilo Kernel Linux; monta módulos bajo demanda activa según la tarea.
5. `BloqueEjecucion:[...]`: Secuencia ordenada de instrucciones imperativas (`!`), tuberías (`->`) y contratos de salida.
6. `BloqueMemoria:[...]`: Esquema LIFO de persistencia estructurada y auditoría de eventos.
7. `BloqueLatido:[...]`: Ciclos proactivos, cron autónomo y monitoreo periódico de salud.

### 4.6. Discriminador de Tipo y Regla de Herencia (Estándar v1.2.0)
Para estructurar sistemas agénticos modulares sin ambigüedad ontológica y preservar la ventana de atención:

1. **Esquema de Identificación:**
   Todo `BloqueIdentidad` formaliza el tipo y nombre del artefacto:
   `@Identifícate(Tipo:[T], Nombre:[X])`
   donde `T` pertenece obligatoriamente al vocabulario cerrado:
   - `Agente`: Entidad operativa u orquestador raíz del sistema agéntico.
   - `Skill`: Módulo de capacidad procedimental o habilidad cognitiva especializada.
   - `Configuracion`: Parámetros, variables y modulaciones de entorno/voz.
   - `Herramienta`: Conector o enrutador técnico de ejecución externa (host, APIs, MCP).
   - `Bloque`: Fragmento o subestructura lógica reutilizable.
   - `Memoria`: Buffer de contexto persistente o bitácora de sesión.

2. **Regla de Herencia:**
   - El parámetro `-Organizacion:[...]`, la directiva de transparencia obligatoria `@Aplica(Regla:[Transparencia])` y las reglas base del sistema viven **exclusivamente** en el artefacto raíz de tipo `[Agente]`.
   - Los artefactos subordinados (`Skill`, `Configuracion`, `Herramienta`, `Bloque`, `Memoria`) **no repiten** estos atributos; heredan la ontología y autoridad del agente raíz y declaran únicamente `Tipo` + `Nombre` + `Rol` + `Mision` más sus directivas técnicas locales.

---

## 5. Reglas de Validación de Conformidad

Cualquier programa en Efectral DSL debe cumplir las siguientes 5 reglas:
1. **Regla de No-Prosa:** No se admiten frases de cortesía humana antes o después de los bloques.
2. **Regla de Delimitación Estricta:** Ningún valor puede quedar huérfano fuera de corchetes `[ ]` o comillas `" "`.
3. **Regla de Prefijos:** Toda regla permanente de sistema debe llevar `@`; toda orden ejecutiva activa debe llevar `!`.
4. **Regla de Determinismo:** Prohibido inferir datos faltantes; ante ambigüedad, el agente debe detenerse y emitir una alerta.
5. **Regla de Carga Selectiva (Principio Kernel Linux / Anti-Saturación):** Queda terminantemente prohibida la carga monolítica e indiscriminada de herramientas, habilidades o memorias extensas sin vinculación activa con la tarea del turno. Todo sistema agéntico modular debe implementar carga selectiva por demanda (`BloqueCargaSelectiva` o `@Aplica(CargaSelectiva:[PorDemanda])`), manteniendo la ventana de atención en su mínima expresión operativa necesaria.

---

## 6. Modelo de Compilación y Tolerancia Cero (Zero-Tolerance Syntax Enforcement)

A diferencia de los prompts en lenguaje natural donde el modelo tolera errores o improvisa sobre texto ambiguo, Efectral DSL opera bajo el principio de **Compilación y Validación Estricta**:

1. **Invalidez de Módulo ante Error de Sintaxis:** Cualquier archivo `.efd` que contenga una sola línea de prosa suelta, corchetes o paréntesis desbalanceados, comillas huérfanas o ausencia de prefijos normativos (`@` o `!`) es considerado **inválido de forma fatal (`SYNTAX_ERROR`)**. La rigidez del lenguaje reside en su morfología y delimitación estricta; la semántica del verbo es libremente interpretada por la IA en todo su esplendor.
2. **Prohibición de Ejecución / Cero Tolerancia:** Ante un error sintáctico, el agente o entorno de ejecución tiene terminantemente prohibido intentar inferir, reparar o ejecutar el módulo. Debe abortar la inicialización y emitir una alerta de sintaxis con la línea exacta del fallo.
3. **Ciclo de Vida de Software Agéntico:** Todo agente Efectral debe cumplir el ciclo estricto de ingeniería:
   `Edición (.efd) -> Validación Sintáctica (Linter EFC) -> Carga en Runtime -> Ejecución Determinista`.

---

## 7. Modelo Canónico de Despliegue en Proyectos: Submódulo Fuente (Source Vendor)

Para garantizar la inmunidad total contra alucinaciones y asegurar que cualquier IDE agéntico (Antigravity, Cursor, Copilot) o entorno servidor (Aethir Claw, OpenClaw) comprenda la sintaxis y las reglas de Efectral DSL sin depender de configuraciones externas, se establece como **Estándar Canónico de Proyecto** la integración del repositorio como **submódulo fuente**:

```bash
mkdir MiProyectoAgente
cd MiProyectoAgente
git init
git submodule add https://github.com/emprendimientojuliogallardo4-oss/Efectral-DSL-4.git Efectral-DSL-4
```

### Principios del Estándar de Submódulo Fuente:
1. **Contexto In-Workspace Inmutable:** Al residir la carpeta `Efectral-DSL-4/` dentro del árbol del proyecto, la IA indexa automáticamente la especificación formal, la gramática EBNF, los ejemplos canónicos y las reglas de forja (`.agents/rules/`).
2. **Cero Alucinaciones:** La IA no requiere deducir sintaxis ni inventar lenguajes ajenos; toma el compilador y los estándares directamente de su propio árbol local.
3. **Autosuficiencia y Portabilidad (Vendor Pattern):** El proyecto agéntico es 100% autocontenido y reproducible en cualquier servidor o máquina sin requerir dependencias globales previas.
