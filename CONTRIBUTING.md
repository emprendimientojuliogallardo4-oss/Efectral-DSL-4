# Contribución a Efectral DSL

Gracias por tu interés en contribuir a **Efectral DSL**, el meta-lenguaje determinista para Inteligencias Artificiales de **E J G 4**.

---

## 1. Principio Fundamental de Contribución

Todo cambio o extensión propuesta para el lenguaje debe adherirse a su principio rector:
> **Determinismo absoluto y reducción a cero de la ambigüedad.**
> No se aceptarán adiciones sintácticas que introduzcan interpretación abierta o relajen la delimitación estricta de valores.

---

## 2. Flujo de Trabajo

1. **Revisa la Especificación:** Consulta [`SPECIFICATION.md`](./SPECIFICATION.md) antes de proponer nuevos verbos u operadores.
2. **Propón Mejoras mediante Issues:** Abre una discusión técnica detallando el caso de uso y el impacto en la ventana de contexto de los modelos.
3. **Validación EBNF:** Toda modificación a la sintaxis debe actualizar y validar contra [`grammar/efectral-dsl.ebnf`](./grammar/efectral-dsl.ebnf).
4. **Cero Prosa en Ejemplos:** Todos los programas de ejemplo aportados en `examples/` deben ser código `.efd` puro.

---

## 3. Créditos y Gobernanza

Efectral DSL es un proyecto de código abierto fundado y mantenido por **E J G 4** (Julio César Gallardo).
