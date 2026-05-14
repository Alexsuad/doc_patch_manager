# DocPatchManager v1.3

Herramienta determinista para la aplicación y verificación de parches sobre documentos Markdown de alta criticidad.

Este sistema implementa un flujo de trabajo híbrido: la **IA propone** o estructura los cambios y **Python valida, aplica y audita** la ejecución de forma determinista para garantizar la integridad estructural del documento.

## Componentes principales

1.  **Aplicador de Parches**: Motor que aplica cambios quirúrgicos basados en un plan JSON. Soporta operaciones de:
    *   `insertar_antes`
    *   `insertar_despues`
    *   `reemplazar_bloque`
    *   `agregar_al_final_de_seccion`
    *   `eliminar_bloque`
2.  **Verificador Documental (Auditoría)**: Compara el documento antes y después (`before` vs `after`) para detectar anomalías, pérdida de encabezados o cambios inesperados.
3.  **Gate de Estructura**: Validador de salud estructural de archivos Markdown que detecta secciones vacías, errores de formato o bloqueos.

## Instalación y Requisitos

- Python >= 3.10
- Gestor de dependencias: `uv` (recomendado)

```bash
uv sync
```

## Uso

### 1. Aplicación de Parches
Para ejecutar un plan de cambios JSON:
```bash
uv run python -m src.main --plan input/planes_cambio/plan_v1.json
```

### 2. Auditoría de Diferencias (Before vs After)
Para auditar la integridad de los cambios entre dos archivos:
```bash
uv run python -m src.verify_document_changes \
  --before input/documentos_base/guia_estudiante.md \
  --after output/documentos_generados/guia_estudiante_v2.md \
  --report output/reportes/verificacion_v13.md
```

### 3. Validación de Estructura Markdown
Para verificar la salud estructural de un documento:
```bash
uv run python -m src.validate_markdown_structure \
  --document input/documentos_base/guia_estudiante.md \
  --report output/reportes/validacion_base.md
```

## Calidad y Pruebas

El sistema cuenta con una suite de **44 tests automatizados** que cubren validación estática, motor de parches, integración CLI, auditoría de seguridad y verificación estructural.

```bash
uv run pytest
```
**Estado actual esperado:** 44 passed.

## Protocolos y Agentes
- **Reglas para Agentes:** Consulte [GEMINI.md](GEMINI.md) para el marco operativo de IA.
- **Protocolo de Seguridad:** Consulte [docs/PROTOCOLO_EDICION_SEGURA.md](docs/PROTOCOLO_EDICION_SEGURA.md).
- **Skill Operativa:** Consulte [.agents/skills/skill_edicion_documental_segura/SKILL.md](.agents/skills/skill_edicion_documental_segura/SKILL.md).
