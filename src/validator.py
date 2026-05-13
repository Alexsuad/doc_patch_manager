# src/validator.py

"""
Validador estático de planes de cambio.

Este módulo revisa si un plan de parches tiene una estructura mínima segura
antes de cargar el documento y antes de aplicar cualquier modificación.

Responsabilidad de este archivo:
- Validar rutas declaradas en el plan.
- Validar IDs de cambios.
- Validar tipos de cambios permitidos.
- Validar campos obligatorios según el tipo de operación.
- Bloquear salidas que ya existen para evitar sobrescrituras accidentales.

Este módulo NO modifica archivos.
Este módulo NO lee el contenido del documento Markdown.
Este módulo NO aplica parches.
"""

from pathlib import Path

from src.change_plan_parser import Cambio, PlanCambios


TIPOS_PERMITIDOS = {
    "insertar_antes",
    "insertar_despues",
    "reemplazar_bloque",
    "agregar_al_final_de_seccion",
    "eliminar_bloque",
}


TIPOS_CON_REFERENCIA_SIMPLE = {
    "insertar_antes",
    "insertar_despues",
    "agregar_al_final_de_seccion",
}


TIPOS_CON_REFERENCIA_DE_RANGO = {
    "reemplazar_bloque",
    "eliminar_bloque",
}


TIPOS_QUE_EXIGEN_CONTENIDO = {
    "insertar_antes",
    "insertar_despues",
    "reemplazar_bloque",
    "agregar_al_final_de_seccion",
}


def _resolver_ruta(root: Path, ruta: str) -> Path:
    """
    Convierte una ruta del plan en una ruta absoluta usable.

    Si la ruta ya es absoluta, se devuelve tal como viene.
    Si la ruta es relativa, se interpreta desde la raíz del proyecto.

    Esto permite que el validador funcione tanto con rutas normales del proyecto
    como con rutas temporales usadas por los tests.
    """

    ruta_path = Path(ruta)

    if ruta_path.is_absolute():
        return ruta_path

    return root / ruta_path


def _validar_rutas_del_plan(plan: PlanCambios, root: Path) -> list[str]:
    """
    Valida las rutas principales del plan.

    Reglas aplicadas:
    - V1: el documento base debe existir.
    - V2: el documento base y el documento de salida no deben ser el mismo archivo.
    - V10: el documento de salida no debe existir previamente.
    """

    errores = []

    ruta_base = _resolver_ruta(root, plan.documento_base)
    ruta_salida = _resolver_ruta(root, plan.documento_salida)

    if not plan.documento_base:
        errores.append("V1: documento_base no fue definido.")
    elif not ruta_base.exists():
        errores.append(f"V1: documento base no existe: {plan.documento_base}")

    if not plan.documento_salida:
        errores.append("V2: documento_salida no fue definido.")
    elif ruta_base.resolve() == ruta_salida.resolve():
        errores.append("V2: documento_base y documento_salida no pueden ser el mismo archivo.")

    if plan.documento_salida and ruta_salida.exists():
        errores.append(f"V10: documento de salida ya existe: {plan.documento_salida}")

    return errores


def _validar_ids(cambios: list[Cambio]) -> list[str]:
    """
    Valida que cada cambio tenga un ID único.

    Reglas aplicadas:
    - V4: cada cambio debe tener ID.
    - V5: no puede haber IDs duplicados.
    """

    errores = []
    ids_vistos = set()

    for indice, cambio in enumerate(cambios, start=1):
        if not cambio.id:
            errores.append(f"V4: cambio en posición {indice} no tiene id.")
            continue

        if cambio.id in ids_vistos:
            errores.append(f"V5: id duplicado: {cambio.id}")

        ids_vistos.add(cambio.id)

    return errores


def _validar_tipo(cambio: Cambio) -> list[str]:
    """
    Valida que el tipo de cambio esté dentro de los tipos permitidos.

    Regla aplicada:
    - V6: tipo de cambio permitido.
    """

    errores = []

    if cambio.tipo not in TIPOS_PERMITIDOS:
        errores.append(f"V6: tipo de cambio no permitido en {cambio.id}: {cambio.tipo}")

    return errores


def _validar_referencias(cambio: Cambio) -> list[str]:
    """
    Valida que cada cambio tenga las referencias necesarias.

    Reglas aplicadas:
    - V7: referencia obligatoria para operaciones simples.
    - V7: referencia_inicio y referencia_fin obligatorias para operaciones por rango.
    """

    errores = []

    if cambio.tipo in TIPOS_CON_REFERENCIA_SIMPLE:
        if not cambio.referencia:
            errores.append(
                f"V7: el cambio {cambio.id} requiere el campo referencia."
            )

    if cambio.tipo in TIPOS_CON_REFERENCIA_DE_RANGO:
        if not cambio.referencia_inicio:
            errores.append(
                f"V7: el cambio {cambio.id} requiere el campo referencia_inicio."
            )

        if not cambio.referencia_fin:
            errores.append(
                f"V7: el cambio {cambio.id} requiere el campo referencia_fin."
            )

    return errores


def _validar_contenido(cambio: Cambio) -> list[str]:
    """
    Valida si el contenido es obligatorio según el tipo de operación.

    Regla aplicada:
    - V8: contenido obligatorio para insertar, reemplazar y agregar.

    Nota importante:
    - eliminar_bloque NO exige contenido, porque su objetivo es borrar un rango.
    """

    errores = []

    if cambio.tipo in TIPOS_QUE_EXIGEN_CONTENIDO and not cambio.contenido:
        errores.append(
            f"V8: el cambio {cambio.id} requiere contenido."
        )

    return errores


def _validar_cambios(cambios: list[Cambio]) -> list[str]:
    """
    Valida la lista completa de cambios.

    Esta función agrupa validaciones por cambio:
    - IDs.
    - Tipo permitido.
    - Referencias obligatorias.
    - Contenido obligatorio cuando aplica.
    """

    errores = []

    if not cambios:
        errores.append("V3: el plan no contiene cambios.")

    errores.extend(_validar_ids(cambios))

    for cambio in cambios:
        errores.extend(_validar_tipo(cambio))

        if cambio.tipo in TIPOS_PERMITIDOS:
            errores.extend(_validar_referencias(cambio))
            errores.extend(_validar_contenido(cambio))

    return errores


def validar_plan_completo(plan: PlanCambios, root: Path) -> list[str]:
    """
    Valida un plan completo antes de aplicar parches.

    Parámetros:
    - plan: objeto PlanCambios ya parseado desde JSON.
    - root: carpeta raíz desde donde se interpretan las rutas relativas.

    Retorna:
    - Una lista de errores.
    - Si la lista está vacía, el plan pasó la validación estática.
    """

    errores = []

    errores.extend(_validar_rutas_del_plan(plan, root))
    errores.extend(_validar_cambios(plan.cambios))

    return errores