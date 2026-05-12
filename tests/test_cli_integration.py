import pytest
import subprocess
import sys
import json
from pathlib import Path

# File: tests/test_cli_integration.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Test de integración autónomo para la CLI (v1.2.3).
# Blindado con aserción de returncode == 1.
# ──────────────────────────────────────────────────────────────────────

@pytest.fixture
def root_dir():
    return Path(__file__).parent.parent

def test_cli_v10_protection_autonomous(tmp_path, root_dir):
    """Verifica la protección V10 usando archivos temporales dinámicos."""
    
    # 1. Crear documento de salida ficticio en carpeta temporal
    temp_output = tmp_path / "salida_ficticia.md"
    temp_output.write_text("contenido que bloquea la sobrescritura")
    
    # 2. Crear un plan de parches temporal
    plan_data = {
        "documento_base": "input/documentos_base/guia_estudiante.md",
        "documento_salida": str(temp_output),
        "cambios": [
            {
                "id": "cambio_test",
                "tipo": "insertar_despues",
                "referencia": "## Introducción",
                "contenido": "Test"
            }
        ]
    }
    
    plan_file = tmp_path / "plan_temp.json"
    plan_file.write_text(json.dumps(plan_data))

    # 3. Ejecutar CLI
    cmd = [sys.executable, "-m", "src.main", "--plan", str(plan_file)]
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(root_dir))
    
    # 4. Validaciones
    # Debe imprimir PATCH_BLOQUEADO y devolver código 1 (error controlado)
    assert result.returncode == 1
    assert "PATCH_BLOQUEADO" in result.stdout
    assert temp_output.read_text() == "contenido que bloquea la sobrescritura"
