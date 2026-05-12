import pytest
import subprocess
import os
from pathlib import Path

# File: tests/test_verify_document_changes.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Pruebas portables para el verificador v1.2.
# ──────────────────────────────────────────────────────────────────────

@pytest.fixture
def run_verify():
    def _run(before, after, report=None):
        # Calculamos el root de forma relativa al archivo de test
        root = Path(__file__).parent.parent
        cmd = ["python3", "-m", "src.verify_document_changes", "--before", str(before), "--after", str(after)]
        if report:
            cmd += ["--report", str(report)]
        return subprocess.run(cmd, capture_output=True, text=True, cwd=str(root))
    return _run

def test_verify_ok(tmp_path, run_verify):
    b = tmp_path / "before.md"
    a = tmp_path / "after.md"
    b.write_text("# Titulo\nContenido")
    a.write_text("# Titulo\nContenido extra")
    result = run_verify(b, a)
    assert result.returncode == 0
    assert "RESULTADO: VERIFY_OK" in result.stdout

def test_verify_blocked_missing_before(tmp_path, run_verify):
    b = tmp_path / "no_existe.md"
    a = tmp_path / "after.md"
    a.write_text("Algo")
    result = run_verify(b, a)
    assert result.returncode == 1
    assert "VERIFY_BLOCKED" in result.stdout

def test_verify_blocked_missing_after(tmp_path, run_verify):
    """Test obligatorio: After no existe."""
    b = tmp_path / "before.md"
    a = tmp_path / "no_existe_after.md"
    b.write_text("# Titulo")
    result = run_verify(b, a)
    assert result.returncode == 1
    assert "VERIFY_BLOCKED" in result.stdout

def test_verify_blocked_deleted_header(tmp_path, run_verify):
    b = tmp_path / "before.md"
    a = tmp_path / "after.md"
    b.write_text("# Seccion1\n# Seccion2")
    a.write_text("# Seccion1")
    result = run_verify(b, a)
    assert result.returncode == 1
    assert "VERIFY_BLOCKED" in result.stdout

def test_verify_warning_duplicates(tmp_path, run_verify):
    b = tmp_path / "before.md"
    a = tmp_path / "after.md"
    b.write_text("# Unico")
    a.write_text("# Unico\n# Unico")
    result = run_verify(b, a)
    assert result.returncode == 0
    assert "RESULTADO: VERIFY_WARNING" in result.stdout

def test_verify_blocked_empty_after(tmp_path, run_verify):
    b = tmp_path / "before.md"
    a = tmp_path / "after.md"
    b.write_text("# Contenido")
    a.write_text("")
    result = run_verify(b, a)
    assert result.returncode == 1
    assert "El documento de salida está vacío" in result.stdout

def test_verify_blocked_reduction_30(tmp_path, run_verify):
    b = tmp_path / "before.md"
    a = tmp_path / "after.md"
    b.write_text("\n".join([f"Linea {i}" for i in range(100)]))
    a.write_text("\n".join([f"Linea {i}" for i in range(60)]))
    result = run_verify(b, a)
    assert result.returncode == 1
    assert "Reducción crítica" in result.stdout

def test_verify_warning_growth_30(tmp_path, run_verify):
    b = tmp_path / "before.md"
    a = tmp_path / "after.md"
    b.write_text("\n".join([f"Linea {i}" for i in range(10)]))
    a.write_text("\n".join([f"Linea {i}" for i in range(20)]))
    result = run_verify(b, a)
    assert result.returncode == 0
    assert "RESULTADO: VERIFY_WARNING" in result.stdout

def test_verify_generate_report(tmp_path, run_verify):
    b = tmp_path / "before.md"
    a = tmp_path / "after.md"
    r = tmp_path / "report.md"
    b.write_text("# OK")
    a.write_text("# OK\nMas")
    result = run_verify(b, a, report=r)
    assert result.returncode == 0
    assert r.exists()
