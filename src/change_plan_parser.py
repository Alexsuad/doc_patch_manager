# src/change_plan_parser.py

"""
Módulo encargado de cargar y normalizar planes de cambio en formato JSON.

Este archivo cumple una función sencilla pero muy importante:
convierte los datos crudos de un archivo JSON en objetos Python claros,
para que el validador y el motor de parches puedan trabajar de forma segura.

No aplica cambios al documento.
No valida referencias dentro del Markdown.
Solo carga y estructura el plan.
"""

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class Cambio:
    """
    Representa un único cambio solicitado dentro del plan de parches.

    El orden de los campos está pensado para mantener compatibilidad con los tests
    existentes del proyecto, donde algunos cambios se crean de forma posicional:

        Cambio("1", "insertar_despues", "Contenido", "# Titulo")

    En ese caso:
    - "1" es el id.
    - "insertar_despues" es el tipo.
    - "Contenido" es el contenido a insertar.
    - "# Titulo" es la referencia.

    Para operaciones por rango, como reemplazar_bloque o eliminar_bloque,
    se usan referencia_inicio y referencia_fin.
    """

    id: str
    tipo: str
    contenido: str = ""
    referencia: str = ""
    referencia_inicio: str = ""
    referencia_fin: str = ""
    incluir_referencia_fin: bool = False


@dataclass
class PlanCambios:
    """
    Representa el plan completo de cambios.

    Este objeto agrupa:
    - documento_base: archivo Markdown original.
    - documento_salida: archivo Markdown que se va a generar.
    - crear_backup: indica si se debe crear copia de seguridad.
    - generar_reporte: indica si se debe generar reporte de ejecución.
    - cambios: lista de cambios que se aplicarán al documento.
    """

    documento_base: str
    documento_salida: str
    crear_backup: bool = False
    generar_reporte: bool = False
    cambios: list[Cambio] = field(default_factory=list)


def cargar_plan_desde_archivo(ruta_plan: Path) -> dict[str, Any]:
    """
    Carga un archivo JSON desde disco y devuelve su contenido como diccionario.

    Parámetros:
    - ruta_plan: ruta del archivo JSON con el plan de cambios.

    Retorna:
    - Un diccionario con los datos leídos del JSON.

    Importante:
    Esta función solo lee el archivo. La conversión a PlanCambios se hace
    en parsear_plan().
    """

    with ruta_plan.open("r", encoding="utf-8") as archivo:
        return json.load(archivo)


def parsear_plan(datos: dict[str, Any]) -> PlanCambios:
    """
    Convierte un diccionario de datos en un objeto PlanCambios.

    Esta función toma los datos crudos del JSON y crea objetos Cambio para cada
    elemento de la lista "cambios".

    Se usan valores por defecto seguros para que el plan pueda omitir opciones
    como crear_backup o generar_reporte sin romper el flujo.
    """

    cambios = []

    for cambio_data in datos.get("cambios", []):
        cambio = Cambio(
            id=str(cambio_data.get("id", "")),
            tipo=str(cambio_data.get("tipo", "")),
            contenido=str(cambio_data.get("contenido", "")),
            referencia=str(cambio_data.get("referencia", "")),
            referencia_inicio=str(cambio_data.get("referencia_inicio", "")),
            referencia_fin=str(cambio_data.get("referencia_fin", "")),
            incluir_referencia_fin=bool(cambio_data.get("incluir_referencia_fin", False)),
        )
        cambios.append(cambio)

    return PlanCambios(
        documento_base=str(datos.get("documento_base", "")),
        documento_salida=str(datos.get("documento_salida", "")),
        crear_backup=bool(datos.get("crear_backup", False)),
        generar_reporte=bool(datos.get("generar_reporte", False)),
        cambios=cambios,
    )