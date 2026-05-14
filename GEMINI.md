# GEMINI.md — Reglas del proyecto doc_patch_manager

## Identidad del proyecto

Este repositorio implementa `doc_patch_manager`, una herramienta local en Python para edición documental segura de archivos Markdown.

El objetivo del proyecto no es crear un agente autónomo complejo, sino apoyar un flujo híbrido:

1. El Agente o el USUARIO prepara instrucciones y estructura los cambios.
2. El Agente opera sobre el repositorio siguiendo protocolos estrictos.
3. Python aplica o verifica de forma determinista mediante el motor de parches.
4. El humano aprueba el resultado final basado en evidencias.

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

- v1.1: Aplicador seguro de parches documentales (incluye soporte para `eliminar_bloque`).
- v1.2.2: Verificador documental posterior.
- v1.2.3: Limpieza LEAN + 5S aprobada.
- Suite actual esperada: **44 tests pasando**.

## Reglas operativas globales

1. No declarar éxito sin evidencia real.
2. Antes de afirmar que algo funciona, ejecutar pruebas o mostrar salida verificable.
3. Para cambios relevantes, trabajar primero en Planning Mode.
4. No modificar documentos reales originales.
5. No sobrescribir archivos de trabajo sin aprobación explícita.
6. No guardar outputs, backups ni reportes como parte del repo limpio.
7. `output/` es temporal y debe estar ignorado por Git.
8. No pedir al usuario que escriba JSON manualmente si el agente puede generarlo.
9. El usuario solo debe revisar cambios y aprobar o rechazar resultados.
10. Si hay ambigüedad en una referencia documental, detenerse y reportar.
11. No ejecutar `git pull`, `git push`, `git reset`, `git clean`, `git checkout` destructivo ni `git push --force` sin aprobación explícita del usuario.

## Archivos críticos (no tocar sin justificación)

- `src/main.py`
- `src/patch_engine.py`
- `src/validator.py`
- `src/change_plan_parser.py`
- `src/verify_document_changes.py`
- `src/validate_markdown_structure.py`
- `GEMINI.md`
- `docs/PROTOCOLO_EDICION_SEGURA.md`
- `.agents/skills/skill_edicion_documental_segura/SKILL.md`
- `.agents/rules/01_operacion_lean.md`

Solo se pueden modificar si:
- Existe un fallo demostrado.
- Hay una mejora técnica aprobada explícitamente.
- Se garantiza la estabilidad mediante `uv run pytest`.
- Se entrega evidencia de la validación.

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

Responder de forma breve y con evidencia clara:
- Archivos modificados/eliminados.
- Comandos ejecutados.
- Resultado de las pruebas (`pytest`).
- Estado final y ubicación de reportes en `output/reportes/`.
- Advertencias o bloqueos detectados.

No escribir relatos largos si no aportan evidencia técnica.
