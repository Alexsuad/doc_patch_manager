# Protocolo de Edición Segura (v1.3)

Este protocolo define los procedimientos obligatorios para interactuar con los documentos del repositorio, garantizando la trazabilidad y evitando la pérdida accidental de información.

## Jerarquía de seguridad
1.  **Documento Maestro / Crítico:** Requiere obligatoriamente **Modo A** (JSON Patch).
2.  **Documentos de soporte:** Pueden usar **Modo B** bajo supervisión.
3.  **Documentos corruptos:** Requieren obligatoriamente **Modo C** (Recuperación).

---

## Modo A: Edición Determinista (Plan JSON)
*Vía preferente para documentos maestros y cambios estructurales.*

1.  **Gate de Entrada:** Verificar la salud del documento base:
    `uv run python -m src.validate_markdown_structure --document <archivo_original>`
2.  **Planificación:** Generar el plan de cambios en `input/planes_cambio/*.json`.
3.  **Ejecución:** Aplicar el motor de parches:
    `uv run python -m src.main --plan <plan.json>`
4.  **Gate de Diferencia:** Generar reporte de métricas before/after con `src.verify_document_changes`.
5.  **Gate de Salida:** Validar la estructura del documento generado:
    `uv run python -m src.validate_markdown_structure --document <archivo_generado>`
6.  **Consolidación:** Aprobación humana y reemplazo del archivo original.

---

## Modo B: Auditoría de cambios manuales autorizados
*Solo para documentos no críticos o previa autorización explícita del usuario.*

1.  **Autorización:** El agente debe solicitar permiso antes de realizar una edición manual directa sobre el Markdown.
2.  **Edición:** Se realiza el cambio puntual autorizado.
3.  **Auditoría Obligatoria:** Ejecutar inmediatamente el verificador:
    `uv run python -m src.verify_document_changes --before <original> --after <editado> --report <reporte.md>`
4.  **Validación de Salud:** Ejecutar `src.validate_markdown_structure` para asegurar que no se introdujeron errores de formato.
5.  **Decisión Final:**
    *   **VERIFY_OK:** Cambio aceptado.
    *   **VERIFY_WARNING:** Revisión humana obligatoria.
    *   **VERIFY_BLOCKED:** Reversión inmediata.

---

## Modo C: Recuperación controlada
*Uso exclusivo cuando el documento base falla el gate inicial con estado `MARKDOWN_BLOCKED`.*

1.  **Diagnóstico:** Identificar el error estructural mediante `src.validate_markdown_structure`.
2.  **Intervención Mínima:** Corregir **únicamente** los problemas que causan el bloqueo (ej. cerrar bloques de código, arreglar encabezados rotos). Está prohibido realizar cambios editoriales o de contenido no relacionados.
3.  **Validación de Salida:** El documento debe pasar el gate con estado `MARKDOWN_OK` o `MARKDOWN_WARNING` aprobado explícitamente por el usuario. Si el resultado es `MARKDOWN_BLOCKED`, la recuperación no se considera válida.
4.  **Aprobación Humana:** Mostrar el `diff` y el reporte de validación antes de consolidar el cambio.

---

## Reglas de Oro
- **No sobrescribir a ciegas:** Nunca eliminar el archivo original sin confirmar que el nuevo documento es válido y completo.
- **Evidencia Técnica:** Todo cambio debe estar respaldado por un reporte en `output/reportes/`.
- **Prevalencia del Plan:** Si un cambio puede hacerse mediante un plan JSON, se debe priorizar ese método sobre la edición manual.
