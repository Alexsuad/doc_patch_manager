# GEMINI.md — Reglas del proyecto doc_patch_manager

## Identidad del proyecto

Este repositorio implementa `doc_patch_manager`, una herramienta local en Python para edición documental segura de archivos Markdown.

El objetivo del proyecto no es crear un agente autónomo complejo, sino apoyar un flujo híbrido:

1. ChatGPT u otra IA o el USUARIO prepara instrucciones.
2. Antigravity opera sobre el repositorio.
3. Python aplica o verifica de forma determinista.
4. El humano aprueba.

## Principio central

IA propone o estructura.
Python valida, aplica y verifica.
Humano aprueba.

## Metodología

Aplicar siempre LEAN + 5S.

- No guardar basura.
- No conservar archivos temporales sin propósito.
- No crear carpetas o scripts “por si acaso”.
- No duplicar lógica.
- No hacer refactors grandes si basta un cambio pequeño.
- No tocar lógica aprobada salvo necesidad justificada.

## Estado actual aprobado

- v1.1: aplicador seguro de parches documentales.
- v1.2.2: verificador documental posterior.
- v1.2.3: limpieza LEAN + 5S aprobada.
- Suite actual esperada: 23 tests pasando.

## Reglas operativas

1. No declarar éxito sin evidencia real.
2. Antes de afirmar que algo funciona, ejecutar pruebas o mostrar salida verificable.
3. Para cambios relevantes, trabajar primero en Planning Mode.
4. No modificar documentos reales originales.
5. No sobrescribir archivos de trabajo sin aprobación explícita.
6. No guardar outputs, backups ni reportes como parte del repo limpio.
7. `output/` es temporal y debe estar ignorado.
8. No pedir al usuario que escriba JSON manualmente si Antigravity puede generarlo.
9. El usuario solo debe pegar cambios y aprobar o rechazar resultados.
10. Si hay ambigüedad en una referencia documental, detenerse y reportar.

## Archivos que no deben tocarse sin justificación previa

- `src/main.py`
- `src/patch_engine.py`
- `src/validator.py`
- `src/verify_document_changes.py`

Solo se pueden modificar si:
- existe un fallo demostrado;
- hay una mejora aprobada;
- se ejecuta `uv run pytest`;
- se entrega evidencia.

## Comandos de verificación obligatorios

Después de cambios en código:

```bash
uv run pytest
```

Después de edición documental:

```bash
uv run python -m src.verify_document_changes --before <archivo_antes> --after <archivo_despues> --report <reporte.md>
```

## Formato de respuesta esperado

Responder breve y con evidencia:

- Archivos modificados.
- Archivos eliminados, si aplica.
- Comando ejecutado.
- Resultado de pruebas.
- Estado final.
- Advertencias.

No escribir relatos largos si no aportan evidencia.
