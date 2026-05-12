import pytest
from src.patch_engine import aplicar_parches
from src.change_plan_parser import Cambio

def test_flujo_exito():
    contenido = "Inicio\nReferencia\nFin"
    cambios = [
        Cambio(id="c1", tipo="insertar_despues", referencia="Referencia", contenido="Intermedio")
    ]
    nuevo, resultados = aplicar_parches(contenido, cambios)
    assert "Intermedio" in nuevo
    assert resultados[0]["estado"] == "APLICADO"

