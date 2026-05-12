import pytest
from src.patch_engine import aplicar_cambio, PatchBloqueado
from src.change_plan_parser import Cambio

def test_eliminar_bloque_excluyendo_fin():
    contenido = 'A\nB\nC\nD\nE'
    cambio = Cambio(id='t1', tipo='eliminar_bloque', referencia_inicio='B', referencia_fin='D', incluir_referencia_fin=False)
    resultado = aplicar_cambio(contenido, cambio)
    assert resultado == 'A\nD\nE\n'

def test_eliminar_bloque_incluyendo_fin():
    contenido = 'A\nB\nC\nD\nE'
    cambio = Cambio(id='t2', tipo='eliminar_bloque', referencia_inicio='B', referencia_fin='D', incluir_referencia_fin=True)
    resultado = aplicar_cambio(contenido, cambio)
    assert resultado == 'A\nE\n'

def test_falla_si_referencia_inicio_no_existe():
    contenido = 'A\nC\nD'
    cambio = Cambio(id='t3', tipo='eliminar_bloque', referencia_inicio='B', referencia_fin='D')
    with pytest.raises(PatchBloqueado, match='V9'):
        aplicar_cambio(contenido, cambio)

def test_falla_si_referencia_fin_no_existe():
    contenido = 'A\nB\nC'
    cambio = Cambio(id='t4', tipo='eliminar_bloque', referencia_inicio='B', referencia_fin='D')
    with pytest.raises(PatchBloqueado, match='V9'):
        aplicar_cambio(contenido, cambio)

def test_falla_si_referencia_inicio_duplicada():
    contenido = 'B\nA\nB\nD'
    cambio = Cambio(id='t5', tipo='eliminar_bloque', referencia_inicio='B', referencia_fin='D')
    with pytest.raises(PatchBloqueado, match='encontrada 2 veces'):
        aplicar_cambio(contenido, cambio)

def test_falla_si_referencia_fin_duplicada():
    contenido = 'B\nA\nD\nE\nD'
    cambio = Cambio(id='t6', tipo='eliminar_bloque', referencia_inicio='B', referencia_fin='D')
    with pytest.raises(PatchBloqueado, match='encontrada 2 veces'):
        aplicar_cambio(contenido, cambio)

def test_falla_si_orden_invalido():
    contenido = 'D\nA\nB'
    cambio = Cambio(id='t7', tipo='eliminar_bloque', referencia_inicio='B', referencia_fin='D')
    with pytest.raises(PatchBloqueado, match='Orden inválido'):
        aplicar_cambio(contenido, cambio)

def test_no_exige_contenido():
    contenido = 'A\nB\nC'
    cambio = Cambio(id='t8', tipo='eliminar_bloque', referencia_inicio='A', referencia_fin='C', contenido='')
    resultado = aplicar_cambio(contenido, cambio)
    assert resultado == 'C\n'

def test_no_rompe_tipos_existentes():
    contenido = 'A\n# S1\nB'
    c1 = Cambio(id='c1', tipo='insertar_despues', referencia='A', contenido='X')
    res1 = aplicar_cambio(contenido, c1)
    assert 'A\nX\n# S1' in res1

def test_integracion_basica_plan_json(tmp_path):
    from src.change_plan_parser import parsear_plan
    from src.validator import validar_plan_completo
    datos = {
        'documento_base': 'base.md',
        'documento_salida': 'salida.md',
        'crear_backup': False,
        'generar_reporte': False,
        'cambios': [{'id': 'elim1', 'tipo': 'eliminar_bloque', 'referencia_inicio': 'START', 'referencia_fin': 'END', 'incluir_referencia_fin': True}]
    }
    plan = parsear_plan(datos)
    (tmp_path / 'base.md').write_text('START\nMIDDLE\nEND')
    errores = validar_plan_completo(plan, tmp_path)
    assert not errores
