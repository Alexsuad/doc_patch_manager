import pytest
from pathlib import Path
from src.validator import validar_plan_completo
from src.change_plan_parser import PlanCambios

def test_v10_output_exists(tmp_path):
    # Simular que el archivo de salida ya existe
    out_file = tmp_path / "salida.md"
    out_file.write_text("existe")
    
    plan = PlanCambios(
        documento_base="base.md",
        documento_salida="salida.md",
        crear_backup=False,
        generar_reporte=False,
        cambios=[]
    )
    errores = validar_plan_completo(plan, tmp_path)
    assert any("V10" in e for e in errores)

