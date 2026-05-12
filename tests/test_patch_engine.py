import pytest
from src.patch_engine import aplicar_cambio
from src.change_plan_parser import Cambio

def test_insertar_despues():
    contenido = "# Titulo\nTexto original"
    cambio = Cambio(id="1", tipo="insertar_despues", referencia="# Titulo", contenido="Texto nuevo")
    resultado = aplicar_cambio(contenido, cambio)
    assert "# Titulo" in resultado
    assert "Texto nuevo" in resultado

