# Protocolo de Edición Segura (v1.2)

Este protocolo define cómo interactuar con los documentos maestros del repositorio para evitar la pérdida de información y asegurar la trazabilidad.

## Modo A: Edición Mecánica (JSON Patch)
*Ideal para cambios estructurales complejos o múltiples secciones.*

1. **Planificación**: Se redacta un plan de cambios en `input/planes_cambio/*.json`.
2. **Aplicación**: Se ejecuta el parcheador:
   `uv run python -m src.main --plan <plan.json>`
3. **Validación Automática**: El parcheador bloquea el cambio si detecta inconsistencias (Reglas V1-V10).
4. **Verificación Posterior**: Auditoría de métricas con el verificador.

## Modo B: Edición Directa + Auditoría
*Ideal para ediciones rápidas, corrección de estilo o ampliación de contenido.*

1. **Edición**: La IA (Antigravity) o el usuario editan directamente el archivo Markdown.
2. **Auditoría Obligatoria**: Se ejecuta inmediatamente el verificador:
   `uv run python -m src.verify_document_changes --before <archivo_original> --after <archivo_editado> --report <reporte.md>`
3. **Decisión**:
   - **VERIFY_OK**: El cambio se acepta.
   - **VERIFY_WARNING**: El usuario debe revisar el reporte (crecimiento alto o duplicados).
   - **VERIFY_BLOCKED**: **ERROR CRÍTICO**. El cambio debe revertirse (se han perdido encabezados o hay una reducción masiva).

---

## Reglas de Oro
- **No sobrescribir**: Nunca borrar el archivo original sin un backup exitoso.
- **Evidencia**: Cada cambio debe dejar un reporte de verificación en `output/reportes/`.
- **Higiene**: Mantener la carpeta `input/` libre de archivos temporales.
