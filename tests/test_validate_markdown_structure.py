# File: tests/test_validate_markdown_structure.py
import pytest
from pathlib import Path
from src.validate_markdown_structure import MarkdownValidator

def test_documento_correcto(tmp_path):
    doc = tmp_path / "correcto.md"
    doc.write_text("# DOCUMENTO MAESTRO DE CRITERIOS DE ARQUITECTURA HÍBRIDA AGÉNTICA\n\nContenido normal.", encoding="utf-8")
    v = MarkdownValidator(doc)
    v.validate()
    assert v.status == "MARKDOWN_OK"

def test_archivo_inexistente(tmp_path):
    doc = tmp_path / "no_existe.md"
    v = MarkdownValidator(doc)
    v.validate()
    assert v.status == "MARKDOWN_BLOCKED"
    assert any("ARCHIVO_INEXISTENTE" in b for b in v.blocks)

def test_documento_vacio(tmp_path):
    doc = tmp_path / "vacio.md"
    doc.write_text("   ", encoding="utf-8")
    v = MarkdownValidator(doc)
    v.validate()
    assert v.status == "MARKDOWN_BLOCKED"
    assert any("ARCHIVO_VACIO" in b for b in v.blocks)

def test_generacion_reporte(tmp_path):
    doc = tmp_path / "doc.md"
    doc.write_text("# Titulo", encoding="utf-8")
    rep = tmp_path / "reporte.md"
    v = MarkdownValidator(doc)
    v.validate()
    v.generate_report(rep)
    assert rep.exists()
    assert "Estado final" in rep.read_text(encoding="utf-8")

def test_titulo_duplicado_plano(tmp_path):
    doc = tmp_path / "dup_plano.md"
    doc.write_text("# DOCUMENTO MAESTRO DE CRITERIOS DE ARQUITECTURA HÍBRIDA AGÉNTICA\n\nDOCUMENTO MAESTRO DE CRITERIOS DE ARQUITECTURA HÍBRIDA AGÉNTICA", encoding="utf-8")
    v = MarkdownValidator(doc)
    v.validate()
    assert v.status == "MARKDOWN_BLOCKED"
    assert any("TITULO_DUPLICADO" in b for b in v.blocks)

def test_secciones_base_sin_md(tmp_path):
    doc = tmp_path / "sec_base.md"
    doc.write_text("# DOCUMENTO MAESTRO DE CRITERIOS DE ARQUITECTURA HÍBRIDA AGÉNTICA\n\n0. Propósito\n\n1. Principio central\n\n24. Checklist final", encoding="utf-8")
    v = MarkdownValidator(doc)
    v.validate()
    assert v.status == "MARKDOWN_WARNING"
    assert v.metrics["secciones_sin_md"] == 3

def test_regla_aplicable_rota_con_header(tmp_path):
    doc = tmp_path / "regla_header.md"
    doc.write_text("# Titulo\n\nRegla aplicable\n\n## 19.8 Naming", encoding="utf-8")
    v = MarkdownValidator(doc)
    v.validate()
    assert v.status == "MARKDOWN_BLOCKED"
    assert any("REGLA_APLICABLE_ROTA" in b for b in v.blocks)

def test_fences_variables(tmp_path):
    doc = tmp_path / "fences.md"
    doc.write_text("# Titulo\n\n````python\n```python\nprint(1)\n```\n````", encoding="utf-8")
    v = MarkdownValidator(doc)
    v.validate()
    assert v.status == "MARKDOWN_OK"
    
    doc2 = tmp_path / "fences_fail.md"
    doc2.write_text("````python\nprint(1)", encoding="utf-8")
    v2 = MarkdownValidator(doc2)
    v2.validate()
    assert v2.status == "MARKDOWN_BLOCKED"

def test_restos_editoriales_bloqueo(tmp_path):
    # Probar los tres casos de bloqueo editorial
    doc = tmp_path / "basura.md"
    doc.write_text("# Titulo\n\nMi recomendación inmediata\n\nNota de prueba controlada\n\nOrden de trabajo recomendado", encoding="utf-8")
    v = MarkdownValidator(doc)
    v.validate()
    assert v.status == "MARKDOWN_BLOCKED"
    # Verificar que detectó los 3 restos específicos
    bloqueos_str = "".join(v.blocks)
    assert "Mi recomendación inmediata" in bloqueos_str
    assert "Nota de prueba controlada" in bloqueos_str
    assert "Orden de trabajo recomendado" in bloqueos_str

def test_erratas_warning(tmp_path):
    doc = tmp_path / "erratas.md"
    doc.write_text("# Titulo\n\naprobación humana explícitamente\n\nhallagzos\n\nand evidencia", encoding="utf-8")
    v = MarkdownValidator(doc)
    v.validate()
    assert v.status == "MARKDOWN_WARNING"
    warnings_str = "".join(v.warnings)
    assert "aprobación humana explícitamente" in warnings_str
    assert "hallagzos" in warnings_str
    assert "and evidencia" in warnings_str

def test_h1_en_seccion_22(tmp_path):
    doc = tmp_path / "sec22.md"
    doc.write_text("# DOCUMENTO MAESTRO DE CRITERIOS DE ARQUITECTURA HÍBRIDA AGÉNTICA\n\n22. Plantillas\n\n# H1 Interno", encoding="utf-8")
    v = MarkdownValidator(doc)
    v.validate()
    assert v.status == "MARKDOWN_WARNING"
    assert v.metrics["h1_count"] == 1
