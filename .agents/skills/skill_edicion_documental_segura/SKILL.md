---
name: edicion-documental-segura
description: Usa esta skill cuando el usuario pida editar, actualizar, auditar o aplicar cambios a documentos Markdown grandes, especialmente Documento Maestro, documentos base, documentos candidatos o lotes de cambios documentales que requieran preservar estructura, numeración, tono, trazabilidad y validación con Python.
---

# Edición documental segura

## Objetivo
Estandarizar el flujo de edición, actualización y auditoría de documentos Markdown de alta criticidad, garantizando que todos los cambios sean validados de forma determinista mediante herramientas Python antes de ser aprobados.

## Cuándo usar esta skill
- Cuando el usuario pida aplicar cambios a documentos Markdown grandes.
- Cuando haya lotes de cambios documentales.
- Cuando se trabaje con Documento Maestro, documentos base, documentos candidatos o versiones finales.
- Cuando se requiera preservar estructura, numeración, tono y trazabilidad.

## Cuándo no usar esta skill
- Para editar archivos pequeños de código.
- Para cambios triviales en README.
- Para documentos no Markdown.
- Para generación creativa sin documento base.

## Principios obligatorios
- **IA propone:** La inteligencia artificial estructura los cambios y prepara los planes.
- **Python valida, aplica y verifica:** El motor determinista en Python es la única autoridad para ejecutar y auditar los cambios.
- **Humano aprueba:** El resultado final requiere validación humana basada en la evidencia de los gates.
- **No se modifica el documento original:** Siempre se trabaja sobre copias o documentos candidatos.
- **No se declara éxito sin evidencia:** Todo estado "OK" debe estar respaldado por reportes de validación.
- **No se maquilla el documento:** Si un documento no pasa el gate, se corrige el sistema o el parche, nunca el resultado a mano.

## Modos de operación
- **Modo auditoría:** El objetivo es exclusivamente revisar la salud estructural y normativa del documento.
  - Se ejecuta el gate de estructura.
  - Se entrega diagnóstico detallado.
  - No se generan planes de cambio ni se aplican parches.
- **Modo parche:** Flujo estándar para aplicar cambios validados.
  - Se utiliza un plan JSON (preparado por el agente y aprobado por el usuario).
  - Se ejecutan los gates de entrada, aplicación, diferencia y salida.
- **Modo recuperación:** Uso exclusivo cuando el documento base devuelve un estado `MARKDOWN_BLOCKED`.
  - El objetivo único es corregir el bloqueo estructural detectado.
  - No se permiten cambios editoriales o de contenido adicionales no relacionados con el bloqueo.

## Flujo obligatorio
1. **Contextualización:** Leer `GEMINI.md` y reglas del proyecto.
2. **Identificación:** Definir claramente el documento base, el documento candidato y el lote de cambios deseados.
3. **Gate de Entrada:** Ejecutar `src/validate_markdown_structure.py` sobre el documento base.
   - Si el resultado es `MARKDOWN_BLOCKED`, detener la edición normal. Solo se puede continuar en **Modo recuperación** si el objetivo explícito es corregir dicho bloqueo.
4. **Planificación:** El agente prepara el plan JSON de cambios. El usuario revisa y aprueba el plan antes de proceder.
5. **Aplicación:** Ejecutar `src/main.py` utilizando el plan JSON aprobado.
6. **Gate de Diferencia:** Ejecutar `src/verify_document_changes.py` comparando before vs after.
7. **Gate de Salida:** Ejecutar `src/validate_markdown_structure.py` sobre el candidato final.
8. **Consolidación:** Si todos los gates pasan, entregar evidencia y solicitar aprobación humana.

## Comandos estándar
- `uv run pytest` (Solo para verificar el entorno antes de operar).
- `uv run python -m src.validate_markdown_structure --document <documento> --report <reporte>`
- `uv run python -m src.main --plan <plan>`
- `uv run python -m src.verify_document_changes --before <before> --after <after> --report <reporte>`

## Estados de salida
- **OK**: Todos los gates pasan (patch exitosa, diff válida, estructura MD limpia).
- **WARNING**: No hay bloqueos, pero hay advertencias (erratas, secciones sin MD) que requieren revisión.
- **BLOCKED**: Cualquier fallo detectado por el motor de parches, el verificador de cambios o el gate de estructura.
- **ERROR**: Fallo técnico en la ejecución del entorno o scripts.

## Evidencia obligatoria
- Lista de archivos involucrados.
- Listado de comandos ejecutados.
- Estado detallado de cada gate (Patch, Verify, Validate).
- Resultado de `pytest` si aplica.
- Rutas exactas de los reportes generados en `output/reportes/`.

## Prohibiciones
- Prohibido editar el documento original directamente.
- Prohibido saltarse cualquier gate de validación.
- Prohibido pedir al usuario que redacte el JSON manualmente.
- Prohibido declarar éxito si existe cualquier estado `BLOCKED`.
- Prohibido corregir errores estructurales "a mano" en el candidato sin pasar por el flujo de parches.

## Criterio de cierre
La tarea se considera finalizada según el modo activo:
- **Modo auditoría:** Entrega de reporte de gate estructural y diagnóstico detallado de hallazgos.
- **Modo parche o recuperación:** Entrega de evidencia de aplicación del patch, reporte de verificación before/after y gate de salida con estado `MARKDOWN_OK` o `MARKDOWN_WARNING` aprobado explícitamente.
