# Guía de Inicio Rápido: Efectral DSL
> **Uso Inmediato para Desarrolladores y Agentes IA**

---

## 1. El Rol de este Submódulo en tu Proyecto

Este directorio proporciona el estándar oficial de sintaxis para **programar la mente (prompts) de tus agentes** en archivos `.efd`:
- Reemplaza la prosa humana ambigua por directivas `@`, acciones `!` y flujos `-> $Registro`.
- Permite a la IA de tu entorno autovalidarse con `python linter/efc_validator.py`.

---

## 2. Anatomía de un Prompt Agéntico en Efectral DSL

```efd
# ================================================================
# EJEMPLO DE DIRECTIVA CANÓNICA
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

---

## 3. Las 3 Reglas de Oro

1. **Todo valor lleva corchetes:** `Version:[1.0.0]`, nunca `Version: 1.0.0`.
2. **Las directivas de sistema llevan `@`:** `@Aplica(Regla:[Determinismo])`.
3. **Las órdenes activas llevan `!`:** `!Verifica(...)` o `!Ejecuta(...)`.

---

## 4. Validación Sintáctica Inmediata

Para certificar que un archivo `.efd` está libre de errores de sintaxis y sin prosa:
```bash
python linter/efc_validator.py ruta/a/tu_archivo.efd
```
