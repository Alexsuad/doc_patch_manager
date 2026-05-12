import pytest
from src.patch_engine import aplicar_cambio, PatchBloqueado
from src.change_plan_parser import Cambio, PlanCambios
from src.validator import validar_plan_completo

@pytest.fixture
def plan_base():
    return PlanCambios("base.md", "out.md", False, False, [])

def test_1_plan_valido(plan_base, tmp_path):
    (tmp_path / "base.md").write_text("# Titulo")
    plan_base.cambios = [Cambio("1", "insertar_despues", "Contenido", "# Titulo")]
    assert not validar_plan_completo(plan_base, tmp_path)

def test_2_no_base(plan_base, tmp_path):
    assert any("V1" in e for e in validar_plan_completo(plan_base, tmp_path))

def test_3_tipo_invalido(plan_base, tmp_path):
    plan_base.cambios = [Cambio("1", "tipo_loco", "C", "# T")]
    assert any("V6" in e for e in validar_plan_completo(plan_base, tmp_path))

def test_4_ref_no_encontrada():
    with pytest.raises(PatchBloqueado):
        aplicar_cambio("# T", Cambio("1", "insertar_antes", "C", "NO_EXISTE"))

def test_5_ref_duplicada():
    with pytest.raises(PatchBloqueado):
        aplicar_cambio("# T\n# T", Cambio("1", "insertar_antes", "C", "# T"))

def test_6_insertar_antes():
    res = aplicar_cambio("B", Cambio("1", "insertar_antes", "A", "B"))
    assert res.startswith("A\nB")

def test_7_insertar_despues():
    res = aplicar_cambio("A", Cambio("1", "insertar_despues", "B", "A"))
    assert "A\nB" in res

def test_8_reemplazar_bloque_conserva_fin():
    cont = "INICIO\nBORRAME\nFIN"
    res = aplicar_cambio(cont, Cambio("1", "reemplazar_bloque", "NUEVO", referencia_inicio="INICIO", referencia_fin="FIN"))
    assert "INICIO" not in res
    assert "BORRAME" not in res
    assert "FIN" in res
    assert "NUEVO" in res

def test_9_agregar_final_seccion():
    cont = "# S1\nContenido\n# S2"
    res = aplicar_cambio(cont, Cambio("1", "agregar_al_final_de_seccion", "EXTRA", referencia="# S1"))
    # El motor inserta la línea. El join con \n genera el resultado esperado.
    assert "# S1\nContenido\nEXTRA\n# S2" in res

def test_10_v10_salida_existe(plan_base, tmp_path):
    (tmp_path / "out.md").write_text("ya estoy")
    assert any("V10" in e for e in validar_plan_completo(plan_base, tmp_path))
