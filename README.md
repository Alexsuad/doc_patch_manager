# DocPatchManager v1.2.2

Herramienta determinista para la aplicación y verificación de parches sobre documentos Markdown.

Este sistema implementa un flujo de trabajo híbrido: la **IA propone** cambios y **Python valida y audita** la ejecución para garantizar la integridad estructural del documento.

## Componentes

1. **Aplicador de Parches (v1.1)**: Motor que aplica cambios quirúrgicos (`insertar`, `reemplazar`, `agregar`) basados en un plan JSON.
2. **Verificador Documental (v1.2.2)**: Auditor que compara el documento antes y después para detectar pérdida de encabezados, reducciones críticas o crecimientos inesperados.

## Instalación y Requisitos

- Python >= 3.10
- Gestor de dependencias: `uv` (recomendado)

```bash
uv sync
```

## Uso

### Modo A: Aplicación de Parches
Para aplicar un plan de cambios JSON:
```bash
uv run python -m src.main --plan input/planes_cambio/plan_v1.json
```

### Modo B: Verificación de Integridad
Para auditar cambios entre dos archivos:
```bash
uv run python -m src.verify_document_changes \
  --before input/documentos_base/guia_estudiante.md \
  --after output/documentos_generados/guia_estudiante_v2.md \
  --report output/reportes/verificacion_v12.md
```

## Calidad y Pruebas

El sistema cuenta con una suite de 23 tests automatizados que cubren validación estática, motor de parches, integración CLI y auditoría de seguridad.

```bash
uv run pytest
```
**Estado actual:** 23 passed.

## Protocolo de Seguridad
Consulte [docs/PROTOCOLO_EDICION_SEGURA.md](docs/PROTOCOLO_EDICION_SEGURA.md) para conocer las reglas de operación.
