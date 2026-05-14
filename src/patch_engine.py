# src/patch_engine.py

"""
Motor de aplicación de parches sobre documentos Markdown.

Este módulo recibe el contenido de un documento como texto y aplica cambios
previamente cargados desde un plan JSON.

Responsabilidad de este archivo:
- Aplicar cambios sobre texto Markdown.
- Bloquear operaciones ambiguas.
- Evitar cambios parciales cuando una referencia no es segura.
- Devolver resultados claros por cada cambio aplicado.

Este módulo NO lee archivos.
Este módulo NO guarda archivos.
Este módulo NO decide si el plan completo es válido.
"""

from src.change_plan_parser import Cambio


class PatchBloqueado(Exception):
    """
    Excepción controlada para detener la aplicación de un parche inseguro.

    Se usa cuando una referencia no existe, aparece más de una vez,
    el rango indicado es inválido o el tipo de cambio no puede aplicarse
    de forma segura.
    """


def _contar_ocurrencias(contenido: str, referencia: str) -> int:
    """
    Cuenta cuántas veces aparece una referencia exacta dentro del documento.

    Esta validación es importante porque el motor solo debe modificar texto
    cuando la referencia aparece exactamente una vez.
    """

    return contenido.count(referencia)


def _validar_referencia_unica(contenido: str, referencia: str) -> None:
    """
    Valida que una referencia exista exactamente una vez.

    Si la referencia no aparece, el cambio se bloquea.
    Si la referencia aparece más de una vez, el cambio también se bloquea,
    porque sería ambiguo decidir dónde aplicar el parche.
    """

    ocurrencias = _contar_ocurrencias(contenido, referencia)

    if ocurrencias == 0:
        raise PatchBloqueado(f"V9: referencia no encontrada: {referencia}")

    if ocurrencias > 1:
        raise PatchBloqueado(
            f"V9: referencia ambigua: {referencia} encontrada {ocurrencias} veces"
        )


def _normalizar_bloque_insertado(contenido: str) -> str:
    """
    Normaliza el contenido que se va a insertar.

    La idea es evitar que el motor dependa de si el usuario escribió o no
    un salto de línea al final del bloque.
    """

    return contenido.rstrip("\n")


def _insertar_antes(contenido_documento: str, cambio: Cambio) -> str:
    """
    Inserta contenido antes de una referencia exacta.

    Ejemplo:
    - Documento: "B"
    - Referencia: "B"
    - Contenido: "A"
    - Resultado: "A\\nB"
    """

    _validar_referencia_unica(contenido_documento, cambio.referencia)

    bloque = _normalizar_bloque_insertado(cambio.contenido)

    return contenido_documento.replace(
        cambio.referencia,
        f"{bloque}\n{cambio.referencia}",
        1,
    )


def _insertar_despues(contenido_documento: str, cambio: Cambio) -> str:
    """
    Inserta contenido después de una referencia exacta.

    Ejemplo:
    - Documento: "A"
    - Referencia: "A"
    - Contenido: "B"
    - Resultado: "A\\nB"
    """

    _validar_referencia_unica(contenido_documento, cambio.referencia)

    bloque = _normalizar_bloque_insertado(cambio.contenido)

    return contenido_documento.replace(
        cambio.referencia,
        f"{cambio.referencia}\n{bloque}",
        1,
    )


def _reemplazar_bloque(contenido_documento: str, cambio: Cambio) -> str:
    """
    Reemplaza un bloque desde referencia_inicio hasta antes de referencia_fin.

    Regla aplicada:
    - Se elimina la referencia de inicio.
    - Se elimina el contenido intermedio.
    - Se conserva la referencia final.

    Esto coincide con los tests existentes, donde reemplazar_bloque debe
    eliminar "INICIO" y "BORRAME", pero conservar "FIN".
    """

    _validar_referencia_unica(contenido_documento, cambio.referencia_inicio)
    _validar_referencia_unica(contenido_documento, cambio.referencia_fin)

    indice_inicio = contenido_documento.find(cambio.referencia_inicio)
    indice_fin = contenido_documento.find(cambio.referencia_fin)

    if indice_inicio >= indice_fin:
        raise PatchBloqueado("V9: Orden inválido entre referencia_inicio y referencia_fin")

    bloque = _normalizar_bloque_insertado(cambio.contenido)

    parte_antes = contenido_documento[:indice_inicio]
    parte_despues = contenido_documento[indice_fin:]

    return f"{parte_antes}{bloque}\n{parte_despues}"


def _agregar_al_final_de_seccion(contenido_documento: str, cambio: Cambio) -> str:
    """
    Agrega contenido antes del siguiente encabezado Markdown de nivel H1.

    Esta operación sirve para añadir texto al final de una sección concreta.

    Ejemplo:
    - Documento:
        # S1
        Contenido
        # S2

    - Referencia:
        # S1

    - Contenido:
        EXTRA

    - Resultado:
        # S1
        Contenido
        EXTRA
        # S2
    """

    _validar_referencia_unica(contenido_documento, cambio.referencia)

    lineas = contenido_documento.splitlines()
    indice_referencia = None

    for indice, linea in enumerate(lineas):
        if linea == cambio.referencia:
            indice_referencia = indice
            break

    if indice_referencia is None:
        raise PatchBloqueado(f"V9: referencia no encontrada: {cambio.referencia}")

    indice_insercion = len(lineas)

    for indice in range(indice_referencia + 1, len(lineas)):
        linea_actual = lineas[indice]

        if linea_actual.startswith("# "):
            indice_insercion = indice
            break

    bloque = _normalizar_bloque_insertado(cambio.contenido)

    lineas.insert(indice_insercion, bloque)

    return "\n".join(lineas)


def _eliminar_bloque(contenido_documento: str, cambio: Cambio) -> str:
    """
    Elimina un bloque desde referencia_inicio hasta referencia_fin.

    Reglas:
    - referencia_inicio debe existir exactamente una vez.
    - referencia_fin debe existir exactamente una vez.
    - referencia_inicio debe aparecer antes de referencia_fin.
    - Si incluir_referencia_fin es False, se conserva referencia_fin.
    - Si incluir_referencia_fin es True, también se elimina referencia_fin.
    - No exige contenido.
    """

    _validar_referencia_unica(contenido_documento, cambio.referencia_inicio)
    _validar_referencia_unica(contenido_documento, cambio.referencia_fin)

    indice_inicio = contenido_documento.find(cambio.referencia_inicio)
    indice_fin = contenido_documento.find(cambio.referencia_fin)

    if indice_inicio >= indice_fin:
        raise PatchBloqueado("V9: Orden inválido entre referencia_inicio y referencia_fin")

    parte_antes = contenido_documento[:indice_inicio]

    if cambio.incluir_referencia_fin:
        indice_final_eliminacion = indice_fin + len(cambio.referencia_fin)
        parte_despues = contenido_documento[indice_final_eliminacion:]
    else:
        parte_despues = contenido_documento[indice_fin:]

    resultado = f"{parte_antes}{parte_despues}"

    return _limpiar_saltos_despues_de_eliminar(resultado)


def _limpiar_saltos_despues_de_eliminar(contenido_documento: str) -> str:
    """
    Normaliza saltos de línea después de eliminar un bloque.

    Esta función evita que queden dobles saltos innecesarios al unir
    la parte anterior y posterior del documento.
    """

    while "\n\n" in contenido_documento:
        contenido_documento = contenido_documento.replace("\n\n", "\n")

    if contenido_documento and not contenido_documento.endswith("\n"):
        contenido_documento += "\n"

    return contenido_documento


def aplicar_cambio(contenido_documento: str, cambio: Cambio) -> str:
    """
    Aplica un único cambio sobre el contenido del documento.

    Esta función actúa como despachador:
    revisa el tipo de cambio y llama a la función interna correspondiente.
    """

    if cambio.tipo == "insertar_antes":
        return _insertar_antes(contenido_documento, cambio)

    if cambio.tipo == "insertar_despues":
        return _insertar_despues(contenido_documento, cambio)

    if cambio.tipo == "reemplazar_bloque":
        return _reemplazar_bloque(contenido_documento, cambio)

    if cambio.tipo == "agregar_al_final_de_seccion":
        return _agregar_al_final_de_seccion(contenido_documento, cambio)

    if cambio.tipo == "eliminar_bloque":
        return _eliminar_bloque(contenido_documento, cambio)

    raise PatchBloqueado(f"V6: tipo de cambio no soportado: {cambio.tipo}")


def aplicar_parches(contenido_documento: str, cambios: list[Cambio]) -> tuple[str, list[dict[str, str]]]:
    """
    Aplica una lista de cambios sobre el contenido del documento.

    Si un cambio falla, se lanza PatchBloqueado y se detiene el proceso.
    Esto evita generar documentos parcialmente modificados cuando hay errores.
    """

    contenido_actual = contenido_documento
    resultados = []

    for cambio in cambios:
        contenido_actual = aplicar_cambio(contenido_actual, cambio)

        resultados.append(
            {
                "id": cambio.id,
                "tipo": cambio.tipo,
                "ref": cambio.referencia
                or cambio.referencia_inicio
                or cambio.referencia_fin
                or "N/A",
                "estado": "APLICADO",
            }
        )

    return contenido_actual, resultados